# encoding: utf-8 

##lns=open(__file__).readlines()
##list(gen_tests(lns))
#def gen_tests(lns,**kw):
#    yield from doc_parts(lns)
#def gen_tests

import os
from rstdoc.fromdocx import main

'''

Conversion from docx
````````````````````

'''

def test_docx_to_rest(
        tmpdir #temporary directory for the -lurg converted rest file
        ):
    '''
    This tests rstfromdocx, rstlisttable rstuntable rstreflow rstreimg.
    '''
    cwd = os.getcwd()
    try:
        with open('test/fixtures/doc.rest',encoding='utf-8') as f:
            expected = f.read().replace('\\','/')
        docxabs = os.path.abspath('test/fixtures/doc.docx')
        os.chdir(tmpdir)
        main(docx=docxabs, listtable = True, untable = True, reflow = True, reimg = True)
        with open('doc/doc.rest',encoding='utf-8') as fp:
            got = fp.read()
        assert expected == got.replace('\\','/')
    finally:
        os.chdir(cwd)


