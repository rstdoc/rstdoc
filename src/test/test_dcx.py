# encoding: utf-8 

##lns=open(__file__).readlines()
##list(gen_tests(lns))
#def gen_tests(lns,**kw):
#    yield from doc_parts(lns)
#def gen_tests

#require installed waf:
#win32:
#  pip install -I waftools
#  wafinstall -v2.0.6
#linux: 
#  git clone https://bitbucket.org/Moo7/waftools
#  cd waftools
#  pip install -e .
#  possibly edit .local to local
#  sudo wafinstall -v2.0.6 -s --user

import sys
import os
sys.path = ['..','test/mocks','mocks'] + sys.path
import pytest
import glob
from rstdoc.dcx import (
    g_counters
    ,make_tgts
    ,tree
    ,mktree
    ,main
    ,doc_parts
    ,rstincluded
    )


'''

rstdcx, dcx.py
``````````````

'''


import subprocess
def run(x):
    if 'win' in sys.platform:
        return subprocess.run(x,shell=True)
    else:
        return subprocess.run(x,shell=False)

try:
    subprocess.run(['python3','--version'])
    Python = 'python3'
except FileNotFoundError:
    Python = 'python' #must also be python 3

_lnkname=[
("""
.. _`id`:

:idname: **key words** and some more text.
And some more text.
""".splitlines(),('id', 'idname')),
("""
.. _`id`:

:idname: 

**key words** and some more text.
""".splitlines(),('id','idname')),
("""
.. _`sy7`:

A Requirement Group
-------------------
ss""".splitlines(),('sy7','A Requirement Group')),
("""
.. _`dz3`:

.. figure:: _images/exampletikz.png
  :name:""".splitlines(),('dz3','Figure 1')),
("""
.. _`dua`:

|dua|: Table legend

.. table::
  :name:""".splitlines(),('dua','Table 1')),
("""
.. _`dta`:

|dta|: Table legend

.. list-table::
  :name:""".splitlines(),('dta','Table 1')),
("""
.. _`dyi`:

|dyi|: Listing showing struct.

.. code-block:: cpp
   :name:""".splitlines(),('dyi','Code 1')),
("""
.. _`dyi`:

|dyi|: Listing showing struct.

.. code:: cpp
   :name:""".splitlines(),('dyi','Code 1')),
("""
.. _`d9x`:

.. math:: 
   :name:
""".splitlines(),('d9x','Math 1'))
]

@pytest.mark.parametrize('lnsres',_lnkname)
def test_lnkname(lnsres):
    '''
    Test the extraction of the name for different kinds of targets::

        header, figure, list-table, table, code-block, code, math, definition (:id:) 
    '''
    #lns,res=_lnkname[6]
    lns,res = lnsres
    g_counters.clear()
    got = list(make_tgts(lns,0))[0][1:]
    assert got==res

@pytest.yield_fixture
def tmpworkdir(tmpdir):
    """
    Create a temporary working working directory.
    """
    cwd = os.getcwd()
    os.chdir(tmpdir.strpath)
    yield tmpdir
    os.chdir(cwd)

@pytest.yield_fixture
def rststpl(tmpworkdir):
    smpl='smpl'
    r=run(['rstdcx','--stpl',smpl])
    assert r.returncode == 0
    oldd=os.getcwd()
    #import pdb;pdb.set_trace()
    os.chdir(os.path.join(tmpworkdir,smpl,'src'))
    yield os.getcwd()
    os.chdir(oldd)
    
@pytest.yield_fixture
def rstinit(tmpworkdir):
    smpl='smpl'
    r=run(['rstdcx','--init',smpl])
    assert r.returncode == 0
    oldd=os.getcwd()
    #import pdb;pdb.set_trace()
    os.chdir(os.path.join(tmpworkdir,smpl,'src'))
    yield os.getcwd()
    os.chdir(oldd)

def test_rstincluded_stpl(rststpl):
    assert list(rstincluded('ra.rest.stpl',(r'.\doc',))) == [
            'ra.rest.stpl', '_links_sphinx.rst']
    assert list(rstincluded('sy.rest.stpl',(r'.\doc',))) == [
            'sy.rest.stpl', '_links_sphinx.rst']
    assert list(rstincluded('sr.rest.stpl',(r'.\doc',))) == [
            'sr.rest.stpl', '_links_sphinx.rst']
    assert list(rstincluded('dd.rest.stpl',(r'.\doc',))) == [
            'dd.rest.stpl', 'dd_included.rst.stpl', 'dd_tables.rst', 'dd_math.tpl', 'dd_diagrams.tpl', '_links_sphinx.rst']
    assert list(rstincluded('tp.rest.stpl',(r'.\doc',))) == [
            'tp.rest.stpl', '_links_sphinx.rst']

def test_rstincluded_init(rstinit):
    assert list(rstincluded('ra.rest',(r'.\doc',))) == [
            'ra.rest', '_links_sphinx.rst']
    assert list(rstincluded('sr.rest',(r'.\doc',))) == [
            'sr.rest', '_links_sphinx.rst', '_links_sphinx.rst']
    assert list(rstincluded('dd.rest',(r'.\doc',))) == [
            'dd.rest', 'somefile.rst', '_links_sphinx.rst']
    assert list(rstincluded('tp.rest',(r'.\doc',))) == [
            'tp.rest', '_sometst.rst', '_links_sphinx.rst']

def test_init(rstinit):
    '''
    Tests |dcx.mktree|.
    Check tree created by ``rstdcx --init smpl``
    '''
    assert tree('.')=="""\
├─code
│  └─some.h
├─doc
│  ├─dd.rest
│  ├─examplecairo.pyg
│  ├─exampledot.dot.stpl
│  ├─exampleeps.eps
│  ├─exampleeps1.eps
│  ├─exampleother.pyg
│  ├─exampleplt.pyg
│  ├─examplepygal.pyg
│  ├─examplepyx.pyg
│  ├─examplesvg.svg.stpl
│  ├─exampletikz.tikz
│  ├─exampletikz1.tikz
│  ├─exampleuml.uml
│  ├─gen
│  ├─index.rest
│  ├─ra.rest
│  ├─sr.rest
│  ├─tp.rest
│  └─wscript_build
├─Makefile
├─conf.py
├─dcx.py
├─docutils.conf
├─reference.docx
├─reference.tex
├─waf
├─waf.bat
├─wafw.py
└─wscript"""

def test_dcx_alonenostpl(rstinit,capfd):
    '''
    Check the output of rstdcx or dcx.py.
    '''
    r=run([Python,'dcx.py','--verbose'])
    assert r.returncode == 0
    out, err = capfd.readouterr()
    assert '\n'.join(out.splitlines()) == """\
doc
    doc/tp.rest
    doc/sr.rest
    doc/ra.rest
    doc/dd.rest
    doc/index.rest"""

@pytest.yield_fixture(params=['docx','pdf','html'])
def makebuild(request,rstinit):
    oldd = os.getcwd()
    r=run(['make',request.param])
    assert r.returncode == 0
    os.chdir(os.path.join('..','build'))
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def test_makenostpl(makebuild):
    '''
    Run make with the sample Makefile.
    '''
    target=makebuild[1]
    if target=='docx':
        expected="""\
├─code
│  └─some_tst.c
└─doc
   └─docx
      ├─dd.docx
      ├─ra.docx
      ├─sr.docx
      └─tp.docx"""
    elif target=='pdf':
        expected="""\
├─code
│  └─some_tst.c
└─doc
   └─pdf
      ├─dd.pdf
      ├─ra.pdf
      ├─sr.pdf
      └─tp.pdf"""
    elif target=='html':
        expected="""\
├─code
│  └─some_tst.c
└─doc
   ├─doctrees
   │  ├─dd.doctree
   │  ├─environment.pickle
   │  ├─index.doctree
   │  ├─ra.doctree
   │  ├─sr.doctree
   │  └─tp.doctree
   └─html
      ├─_images
      ├─_sources
      ├─_static
      ├─_traceability_file.svg
      ├─dd.html
      ├─genindex.html
      ├─index.html
      ├─objects.inv
      ├─ra.html
      ├─search.html
      ├─searchindex.js
      ├─sr.html
      └─tp.html"""
    assert tree(makebuild[0],with_dot_files=False,max_depth=3)==expected

@pytest.yield_fixture(params=['docx','pdf','html','sphinx_html','rst_html'])
def wafbuild(request,rstinit):
    r1=run(['waf','configure'])
    assert r1.returncode==0
    r2=run(['waf','--docs',request.param])
    assert r2.returncode==0
    oldd = os.getcwd()
    os.chdir(os.path.join('..','build'))
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def test_wafnostpl(wafbuild):
    '''
    Run Waf on the sample project.
    Waf needs to be installed 
    
    - either in the system or 
    - added manually to the root folder of the project

    '''
    target=wafbuild[1]
    if target=='docx':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─docx
│     ├─dd.docx
│     ├─ra.docx
│     ├─sr.docx
│     └─tp.docx
└─config.log"""
    elif target=='pdf':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─pdf
│     ├─dd.pdf
│     ├─ra.pdf
│     ├─sr.pdf
│     └─tp.pdf
└─config.log"""
    elif target=='sphinx_html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─sphinx_html
│     ├─_images
│     ├─_sources
│     ├─_static
│     ├─_traceability_file.svg
│     ├─dd.html
│     ├─genindex.html
│     ├─index.html
│     ├─objects.inv
│     ├─ra.html
│     ├─search.html
│     ├─searchindex.js
│     ├─sr.html
│     └─tp.html
└─config.log"""
    elif target=='html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─html
│     ├─_images
│     ├─dd.html
│     ├─ra.html
│     ├─sr.html
│     └─tp.html
└─config.log"""
    elif target=='rst_html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─rst_html
│     ├─_images
│     ├─dd.html
│     ├─ra.html
│     ├─sr.html
│     └─tp.html
└─config.log"""
    assert set(tree(wafbuild[0],with_dot_files=False,max_depth=3).splitlines())-{'│     ├─.doctrees'}==set(expected.splitlines())


@pytest.yield_fixture
def rstsampleswithstpl(rstinit):
    os.rename('doc/ra.rest','doc/ra.rest.stpl')
    yield os.getcwd()

def test_dcx_alonewithstpl(rstsampleswithstpl,capfd):
    '''
    Check the output of rstdcx or dcx.py when there is a ``.stpl`` file.
    '''
    r=run([Python,'dcx.py','--verbose'])
    assert r.returncode == 0
    out, err = capfd.readouterr()
    assert '\n'.join(out.splitlines()) == """\
doc
    doc/tp.rest
    doc/sr.rest
    doc/ra.rest.stpl
    doc/dd.rest
    doc/index.rest"""

def wafit(doctype):
    oldd = os.getcwd()
    r1=run(['waf','configure'])
    assert r1.returncode==0
    r2=run(['waf','--docs',doctype])
    assert r2.returncode==0
    os.chdir(os.path.join('..','build'))
    yield (os.getcwd(),doctype)
    os.chdir(oldd)

@pytest.yield_fixture(params=['docx','pdf','sphinx_html'])
def wafbuildwithstpl(request,rstsampleswithstpl):
    yield from wafit(request.param)

def test_wafwithstpl(wafbuildwithstpl):
    '''
    Run Waf for the case when a main file exists as template (``.stpl``).
    '''
    target=wafbuildwithstpl[1]
    if target=='docx':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─docx
│     ├─dd.docx
│     ├─ra.docx
│     ├─sr.docx
│     └─tp.docx
└─config.log"""
    elif target=='pdf':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─pdf
│     ├─dd.pdf
│     ├─ra.pdf
│     ├─sr.pdf
│     └─tp.pdf
└─config.log"""
    elif target=='sphinx_html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─sphinx_html
│     ├─_images
│     ├─_sources
│     ├─_static
│     ├─_traceability_file.svg
│     ├─dd.html
│     ├─genindex.html
│     ├─index.html
│     ├─objects.inv
│     ├─ra.html
│     ├─search.html
│     ├─searchindex.js
│     ├─sr.html
│     └─tp.html
└─config.log"""
    assert set(tree(wafbuildwithstpl[0],with_dot_files=False,max_depth=3).splitlines())-{'│     ├─.doctrees'}==set(expected.splitlines())


@pytest.yield_fixture
def rststplsample(rstinit):
    tree=r"""
        doc
         ├is.rest
            Issues
            ======
            This file includes an rst file.

            .. include:: is1.rst

            The rst file is generated from an rst.stpl file.
         ├is1.rst.stpl
            %import sys

            .. image:: _images/tictactoe.png

            We are in {{sys.platform}}.
         ├tictactoe.tikz.stpl
            [thick]
            \draw (0,0) grid (3,3);
            %for i,j in {(0,0), (1,0), (2,0), (2,1), (2,2), (1,2)}:
                  \fill ({{i+0.5}},{{j+0.5}}) circle (0.42);
            %end
        """.splitlines()
    mktree(tree)
    open('doc/index.rest','a',encoding='utf-8').write("\n   is.rest\n")
    yield os.getcwd()

@pytest.yield_fixture(params=['docx','pdf','sphinx_html'])
def wafrststpl(request,rststplsample):
    yield from wafit(request.param)

def test_wafrststpl(wafrststpl):
    '''
    Run Waf for the case when an included file exists as template (``.stpl``).
    '''
    target=wafrststpl[1]
    if target=='docx':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─docx
│     ├─dd.docx
│     ├─is.docx
│     ├─ra.docx
│     ├─sr.docx
│     └─tp.docx
└─config.log"""
    elif target=='pdf':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─pdf
│     ├─dd.pdf
│     ├─is.pdf
│     ├─ra.pdf
│     ├─sr.pdf
│     └─tp.pdf
└─config.log"""
    elif target=='sphinx_html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─sphinx_html
│     ├─_images
│     ├─_sources
│     ├─_static
│     ├─_traceability_file.svg
│     ├─dd.html
│     ├─genindex.html
│     ├─index.html
│     ├─is.html
│     ├─objects.inv
│     ├─ra.html
│     ├─search.html
│     ├─searchindex.js
│     ├─sr.html
│     └─tp.html
└─config.log"""
    assert set(tree(wafrststpl[0],with_dot_files=False,max_depth=3).splitlines())-{'│     ├─.doctrees'}==set(expected.splitlines())
    assert sys.platform in open(glob.glob(os.path.join('..','src','doc','is1.rst'))[0],encoding='utf-8').read()
    if target=='sphinx_html':
        assert sys.platform in open(glob.glob(os.path.join('doc',target,'is.*'))[0],encoding='utf-8').read()

def test_selfdoc():
    selfdoc_accoridng_doc_gen=os.path.join('doc','_dcx_api.rst')
    try:
        os.remove(selfdoc_accoridng_doc_gen)
    except: pass
    main(initroot=None,stplroot=None,verbose=True)
    assert os.path.exists(selfdoc_accoridng_doc_gen)

def test_docparts_after():
    res = list(doc_parts(['/// \\brief\n',"/// afun's description\n","//\n"
        ,'void afun(\n','int x //int variable\n',')\n','\n'],
        signature='cpp',relim=r'\\brief|//$',reid=r'\s(\w\+)\('))
    assert res == ['.. code-block:: cpp\n', '', '   void afun(\n',
        '   int x //int variable\n', '   )\n', '', "afun's description\n"]

