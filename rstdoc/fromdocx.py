#!/usr/bin/env python
# encoding: utf-8 

"""
Convert DOCX file to RST in subfolder with name of DOCX file.
It also create ``conf.py``, ``index.py`` and ``Makefile``
and copies ``dcx.py`` into the folder.

See ``dcx.py`` for format conventions for the RST.

There are options to post-process through::

    --listtable (--join can be provided)
    --untable
    --reflow (--sentence True,  --join 0)
    --reimg

See reflow to do that manually.
"""

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

def prj_name(fn):
    m=re.match(r'[\s\d\W]*([^\s\W]*).*',os.path.splitext(os.path.split(fn)[1])[0])
    return m.group(1).strip('_').replace(' ','')

def extract_media(zf,fn):
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

def docxrest(fn):
    fnrst,frm = os.path.splitext(fn)
    frm = frm.strip('.')
    fnrst = os.path.normpath(os.path.join(fnrst,os.path.split(fnrst)[1]+'.rest'))
    return frm,fnrst

def write_confpy(fn):
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

def write_index(fn):
    fnn = os.path.splitext(fn)[0]
    ifn = os.path.normpath(os.path.join(fnn,'index.rest'))
    rst=os.path.splitext(os.path.split(fn)[1])[0]+'.rest'
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

def write_makefile(fn):
    mf = re.split('\s+build\s+',re.split('└ Makefile',example_tree)[1])[0]
    lns=mf.splitlines(True)
    s=re.search('\w',lns[1]).span(0)[0]
    lns = [l[s:] for l in lns]
    rst=os.path.splitext(os.path.split(fn)[1])[0]
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

def write_dcx(fn):
    dcxfile = os.path.join(os.path.split(str(Path(__file__).resolve()))[0],'dcx.py')
    shutil.copy2(dcxfile,os.path.splitext(fn)[0])

def main(**args):
    import argparse
    from .listtable import main as listtable
    from .untable import main as untable
    from .reflow import main as reflow
    from .reimg import main as reimg

    if not args:
        parser = argparse.ArgumentParser(description='''Convert DOCX to RST using pandoc.''')
        parser.add_argument('docx', action='store',help='DOCX file')
        parser.add_argument('-l', '--listtable', action='store_true', default=False, help='''postprocess through rstlisttable''')
        parser.add_argument('-u', '--untable', action='store_true', default=False, help='''postprocess through rstuntable''')
        parser.add_argument('-r', '--reflow', action='store_true', default=False, help='''postprocess through rstreflow''')
        parser.add_argument('-g', '--reimg', action='store_true', default=False, help='''postprocess through rstreimg''')
        parser.add_argument('-j', '--join', action='store', default='012',
                help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')
        args = parser.parse_args().__dict__
    
    fn = args['docx']
    zf = ZipFile(fn)
    extract_media(zf,fn)
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

