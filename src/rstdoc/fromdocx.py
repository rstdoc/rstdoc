#!/usr/bin/env python
# encoding: utf-8 
#def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
#def gen_head(lns,**kw)
#def gen_api(lns,**kw):
#    yield from doc_parts(lns,signature='py',prefix='fromdocx.')
#def gen_api

"""
.. _`rstfromdocx`:

rstfromdocx
===========

rstfromdocx: shell command
fromdocx: rstdoc module

Convert DOCX to RST in a subfolder named after the DOCX file.
It also create ``conf.py``, ``index.py`` and ``Makefile``
and copies ``dcx.py`` into the folder.

See |rstdcx| for format conventions for the RST.

There are options to post-process through::

    --listtable (--join can be provided)
    --untable
    --reflow (--sentence True,  --join 0)
    --reimg

``rstfromdocx -lurg`` combines all of these.

To convert more DOCX documents into the same 
RST documentation folder, proceed like this:

- rename/copy the original DOCX to the name you want for the rest file
- run ``rstfromdocx -lurg doc1.docx``
- check the output in the ``doc1`` subfolder
- repeat the previous 2 steps with the next DOCX files
- create a new folder, e.g. ``doc``
- merge all other folders into that new folder

See |rstreflow| to do that manually.
"""


#''' starts api doc parts (see doc_parts())
'''
API
---


.. code-block::

   import rstdoc.fromdocx as fromdocx

'''


from zipfile import ZipFile
import pypandoc
import os
import shutil
from glob import glob
import re
import time
from pathlib import Path
from .dcx import example_tree, rindices

def mkdir(fn):
    try:
        os.mkdir(fn)
    except:
        pass

_rstname = lambda fn: os.path.splitext(os.path.split(fn)[1])[0]

def prj_name(fn):
    m=re.match(r'[\s\d\W]*([^\s\W]*).*',_rstname(fn))
    return m.group(1).strip('_').replace(' ','')

def extract_media(
        fn #docx file name
        ):
    '''
    extract media files from a docx file
    '''
    zf = ZipFile(fn)
    pwd=os.getcwd()
    try:
        fnn = os.path.splitext(fn)[0]
        mkdir(fnn)
        media=[x for x in zf.infolist() if 'media/' in x.filename]
        os.chdir(fnn)
        mkdir('media')
        os.chdir('media')
        for m in media:
            #m = media[0]
            zf.extract(m)
            try:
                shutil.move(m.filename,os.getcwd())
            except:pass
        for f in glob('word/media/*'):
            os.remove(f)
        os.rmdir('word/media')
        os.rmdir('word')
    finally:
        os.chdir(pwd)

def docxrest(
        fn #docx file name
        ):
    '''
    returns 'docx' and file name of ``.rest`` file.
    '''
    fnrst,frm = os.path.splitext(fn)
    frm = frm.strip('.')
    fnrst = os.path.normpath(os.path.join(fnrst,os.path.split(fnrst)[1]+'.rest'))
    return frm,fnrst

def write_confpy(
        fn #docx file name
        ):
    '''
    Takes the conf.py from the ``example_tree`` in ``rstdoc.dcx``.
    '''
    confpy = re.split('\s*.\s*Makefile',example_tree.split('conf.py')[1])[0]
    pn = prj_name(fn)
    confpy = confpy.replace('docxsample',pn).replace('2017',time.strftime('%Y'))
    lns=confpy.splitlines(True)
    s=re.search('\w',lns[1]).span(0)[0]
    confpy=''.join([l[s:] for l in lns])
    fnn = os.path.splitext(fn)[0]
    cpfn = os.path.normpath(os.path.join(fnn,'conf.py'))
    if os.path.exists(cpfn):
        return
    with open(cpfn,'w',encoding='utf-8') as f:
        f.write(confpy)

def write_index(
        fn #docx file name
        ):
    '''
    Adds a the generated .rest to ``toctree`` in index.rest
    or generates new index.rest.
    '''
    fnn = os.path.splitext(fn)[0]
    ifn = os.path.normpath(os.path.join(fnn,'index.rest'))
    rst = _rstname(fn)+'.rest'
    prjname = prj_name(fn)
    hp = '='*len(prjname)
    if os.path.exists(ifn):
        with open(ifn,'r') as f:
            lns = f.readlines()
    else:
        lns = [x+'\n' for x in ['.. vim: syntax=rst','',hp,prjname,hp,'','.. toctree::']]
    itoc = list(rindices('toctree',lns))[0]
    lns = lns[:itoc+1]+['    '+rst+'\n']+lns[itoc+1:]
    with open(ifn,'w') as f:
        f.writelines(lns)

def write_makefile(
        fn #docx file name
        ):
    '''
    Takes the Makefile from the ``example_tree`` in ``rstdoc.dcx``.
    '''
    mf = re.split('\s+build\s+',re.split('└ Makefile',example_tree)[1])[0]
    lns=mf.splitlines(True)
    s=re.search('\w',lns[1]).span(0)[0]
    lns = [l[s:] for l in lns]
    rst = _rstname(fn)
    idoc = list(rindices('^docx:',lns))[0]
    ipdf = list(rindices('^pdf:',lns))[0]
    doce = lns[idoc+1].replace('sr',rst)
    pdfe = lns[ipdf+1].replace('sr',rst)
    lns=lns[:idoc+1]+[lns[ipdf]]
    fnn = os.path.splitext(fn)[0]
    mffn = os.path.normpath(os.path.join(fnn,'Makefile'))
    if os.path.exists(mffn):
        with open(mffn,'r') as f:
            lns = f.readlines()
    idoc = list(rindices('^docx:',lns))[0]
    ipdf = list(rindices('^pdf:',lns))[0]
    lns=lns[:idoc+1]+[doce]+lns[idoc+1:ipdf+1]+[pdfe]+lns[ipdf+1:]
    with open(mffn,'w',encoding='utf-8') as f:
        f.writelines(lns)

def write_dcx(
        fn #docx file name
        ):
    '''
    Writes the dcx.py into the folder generated for the docx.
    '''
    dcxfile = os.path.join(os.path.split(str(Path(__file__).resolve()))[0],'dcx.py')
    shutil.copy2(dcxfile,os.path.splitext(fn)[0])

def main(
        **args #keyword arguments. If empty the arguments are taken from ``sys.argv``.
        ):
    '''
    This corresponds to the |rstfromdocx| shell command.
    '''
    import argparse
    from .listtable import main as listtable
    from .untable import main as untable
    from .reflow import main as reflow
    from .reimg import main as reimg

    if not args:
        parser = argparse.ArgumentParser(description='''Convert DOCX to RST using Pandoc and additionally copy the images and helper files.''')
        parser.add_argument('docx', action='store',help='DOCX file')
        parser.add_argument('-l', '--listtable', action='store_true', default=False, help='''postprocess through rstlisttable''')
        parser.add_argument('-u', '--untable', action='store_true', default=False, help='''postprocess through rstuntable''')
        parser.add_argument('-r', '--reflow', action='store_true', default=False, help='''postprocess through rstreflow''')
        parser.add_argument('-g', '--reimg', action='store_true', default=False, help='''postprocess through rstreimg''')
        parser.add_argument('-j', '--join', action='store', default='012',
                help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')
        args = parser.parse_args().__dict__
    
    fn = args['docx']
    extract_media(fn)
    frm,fnrst = docxrest(fn)
    #pypandoc.convert_file(fn,'rst',frm,outputfile=fnrst)
    rst=pypandoc.convert(fn,'rst',frm)
    with open(fnrst,'w',encoding='utf-8',newline='\n') as f:
        f.write('.. vim: syntax=rst\n\n')
        f.writelines([x+'\n' for x in rst.splitlines()])
    write_confpy(fn)
    write_index(fn)
    write_makefile(fn)
    write_dcx(fn)

    for a in 'listtable untable reflow reimg'.split():
        if args[a]:
            args['in_place'] = True
            args['sentence'] = True
            if a=='reflow':
                args['join'] = '0'
            args['INPUT'] = [argparse.FileType('r',encoding='utf-8')(fnrst)]
            eval(a)(**args)

if __name__ == '__main__':
    main()

