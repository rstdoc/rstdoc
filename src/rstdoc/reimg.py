#!/usr/bin/env python
# encoding: utf-8 

#def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
#def gen_head(lns,**kw)
#def gen_api(lns,**kw):
#    yield from doc_parts(lns,signature='py',prefix='reimg.')
#def gen_api

"""
.. _`rstreimg`:

rstreimg
========

rstreimg: shell command
reimg: rstdoc module

Reimg renames the images in the rst file and the files themselves.
It uses part of the document name and a number as new names.

This is useful, if more RST documents converted from DOCX
should be combined in one directory and
the names of the images have no meaning (image13,...).

"""


#''' starts api doc parts (see doc_parts())
'''
API
---

.. code-block:: py

   import rstdoc.reimg as reimg

'''


import os
import re
import difflib
import shutil
from .dcx import reximg

imguse = re.compile(r'\|(\w[^|\\ ]*(?: \\\|)?[^|]*\w)\|(?! image::)')
imgdecl = re.compile(r'\|(\w[^|\\ ]*(?: \\\|)?[^|]*\w)\| image:: (\w.*)')
#imguse.search(r'|G:\_Projects\gBYM\trunk\Design\gEstimPRO\Documentation\UIspecificationresources\Electrode_surface_area.png|')
#md=imgdecl.search(r' |G:\_Projects\gBYM\trunk\Design\gEstimPRO\Documentation\UIspecificationresources\Electrode_surface_area.png| image:: media/image3.png')
#md.group(1),md.group(2)
#('G:\\_Projects\\gBYM\\trunk\\Design\\gEstimPRO\\Documentation\\UIspecificationresources\\Electrode_surface_area.png', 'media/image3.png')
#xm=imguse.search(r'''|G:\_Projects\gBYM\trunk\Design\gEstimPRO\Documentation\UI
#specificationresources\Electrode_surface_area.png|''')
#xm.group(1).replace('\n',' ')
#'G:\_Projects\gBYM\trunk\Design\gEstimPRO\Documentation\UI specificationresources\Electrode_surface_area.png'
#xm=imguse.search('|  |xy| |')
#xm.group(1).replace('\n',' ')
#'xy'
#xm=imguse.search('| |UL \| Marks for North America| |')
#xm.group(1).replace('\n',' ')
#'UL \| Marks for North America'

#with open('doc.rest',encoding='utf-8') as f:
#    data = f.read()
#prefix = 'doc'
#with open('doc1.rest','w',encoding='utf-8') as f:
#    f.write(reimg(data,prefix))

def reimg(
    data #rst file read by f.read()
    ,prefix #string prefix for images, should be derived from docx file name
    ):
    '''
    This renames all the images in the rst file converted from docx, to avoid

    - images having strange names

    - collision of image names from different docx

    '''
    i = 1
    fp = lambda x: x.split('image::')[1].strip()
    chfilemap = {}
    for m in reximg.finditer(data):
        oldp = m.group(0)
        d,f = os.path.split(oldp)
        if oldp not in chfilemap:
            i = i + 1
            newn = prefix+'{:03}'.format(i)+os.path.splitext(f)[1]
            newp = os.path.join(d,newn)
            chfilemap[oldp] = newp
    for oldp,newp in chfilemap.items():
        try:
            shutil.move(fp(oldp),fp(newp))
        except: pass
        data=data.replace(oldp,newp)
    declaremap = {}
    for m in imgdecl.finditer(data):
        declaremap[m.group(1)]= os.path.splitext(os.path.split(m.group(2))[1])[0]
    toreplace = {}
    for m in imguse.finditer(data):
        used = m.group(1)
        cm = difflib.get_close_matches(used,declaremap.keys())
        try:
            declared = cm[0]
            newn = declaremap[declared]
            toreplace[used] = newn
            if used != declared:
                toreplace[declared] = newn
        except Exception as e:
            print(e,', no image for:',used)
    for o,n in toreplace.items():
        data = data.replace('|'+o+'|', '|'+n+'|')
    return data

def main(
        **args #keyword arguments. If empty the arguments are taken from ``sys.argv``.
        ):
    '''
    This corresponds to the |rstreimg| shell command.

    ``rstfile`` is the file name

    ``in_place`` defaults to False

    '''
    import codecs
    import sys
    import argparse

    def prefix(fn):
        m=re.match(r'[\s\d\W]*([^\s\W]*).*',os.path.splitext(os.path.split(fn)[1])[0])
        return m.group(1).strip('_').replace(' ','').replace('_','')[:6]

    if not args:
        parser = argparse.ArgumentParser(description='''Rename images referenced in the RST file.''')
        parser.add_argument('rstfile', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
        parser.add_argument('-i', '--in-place', action='store_true', default=False,
                help='''change the file itself''')
        args = parser.parse_args().__dict__

    if not 'in_place' in args: args['in_place'] = False
    if isinstance(args['rstfile'],str): args['rstfile'] = [argparse.FileType('r',encoding='utf-8')(args['rstfile'])]

    for infile in args['rstfile']:
        od = os.getcwd()
        data = infile.read()
        infile.close()
        if args['in_place']:
            f = open(infile.name,'w',encoding='utf-8',newline='\n')
        else:
            #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...  makes problems with pdb, though
            sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
            sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
            f = sys.stdout
        np = os.path.dirname(infile.name)
        try:
            if np:
                os.chdir(np)
            f.write(reimg(data,prefix(infile.name)))
        finally:
            os.chdir(od)
            if args['in_place']:
                f.close()

if __name__ == '__main__':
    main()


