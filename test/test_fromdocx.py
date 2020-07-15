# encoding: utf-8

##lns=open(__file__).readlines()
##list(gen_tests(lns))
#def gen_tests(lns,**kw):
#    yield from doc_parts(lns)
#def gen_tests

import os
import shutil
from rstdoc.fromdocx import main as fromdocx
from rstdoc.listtable import main as listtable
from rstdoc.untable import main as untable
from rstdoc.reflow import main as reflow
from rstdoc.reimg import main as reimg

'''

Conversion from docx
````````````````````

'''

## does not work, as pandoc changed to simple table output between 2.3 and 2.7
# def test_docx_to_rest(
#         tmpdir #temporary directory for the -lurg converted rest file
#         ):
#     '''
#     This tests rstfromdocx, rstlisttable, rstuntable, rstreflow, rstreimg.
#     '''
#     cwd = os.getcwd()
#     try:
#         with open(os.path.join(os.path.dirname(__file__),'fixtures', 'doc.rest'),encoding='utf-8') as f:
#             expected = f.read().replace('\\','/')
#         docxabs = os.path.join(os.path.dirname(__file__),'fixtures','doc.docx')
#         os.chdir(tmpdir)
#         fromdocx(docx=docxabs, listtable = True, untable = True, reflow = True, reimg = True)
#         with open('doc/doc.rest',encoding='utf-8') as fp:
#             got = fp.read()
#         assert expected == got.replace('\\','/')
#     finally:
#         os.chdir(cwd)


def test_lurg(
        tmpdir #temporary directory for the -lurg converted rest file
        ):
    '''
    This tests rstlisttable, rstuntable, rstreflow, rstreimg.
    '''
    cwd = os.getcwd()
    try:
        with open(os.path.join(os.path.dirname(__file__),'fixtures', 'doc.rest'),encoding='utf-8') as f:
            expected = f.read().replace('\\','/')
        rstfile = os.path.join(os.path.dirname(__file__),'fixtures/doc/doc.rest')
        os.chdir(tmpdir)
        shutil.copy2(rstfile,'doc.rest')
        listtable(rstfile='doc.rest',in_place=True,sentence=True)
        untable(rstfile='doc.rest',in_place=True,sentence=True)
        reflow(rstfile='doc.rest',join='0', in_place=True,sentence=True)
        reimg(rstfile='doc.rest',in_place=True,sentence=True)
        with open('doc.rest',encoding='utf-8') as fp:
            got = fp.read()
        assert expected == got.replace('\\','/')
    finally:
        os.chdir(cwd)



# vim: ts=4 sw=4 sts=4 et noai nocin nosi
