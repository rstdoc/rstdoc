# encoding: utf-8 

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
from rstdoc.dcx import (
    g_counters
    ,linktargets
    ,tree
    )

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

.. figure:: _images/smpl.png
  :name:""".splitlines(),('dz3','Figure 1')),
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
    #lns,res=_lnkname[6]
    lns,res = lnsres
    g_counters.clear()
    got = list(linktargets(lns,0))[0][1:]
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
def rstsamples(tmpworkdir):
    smpl='smpl'
    r=run(['rstdcx','--init',smpl])
    assert r.returncode == 0
    oldd=os.getcwd()
    #import pdb;pdb.set_trace()
    os.chdir(os.path.join(tmpworkdir,smpl,'src'))
    yield os.getcwd()
    os.chdir(oldd)

def test_init(rstsamples):
    assert tree('.')=="""\
├─code
│  └─some.h
├─doc
│  ├─Makefile
│  ├─conf.py
│  ├─dd.rest
│  ├─gen
│  ├─index.rest
│  ├─ra.rest
│  ├─smpl.tikz
│  ├─sr.rest
│  ├─tp.rest
│  └─wscript_build
├─dcx.py
├─reference.docx
├─reference.tex
└─wscript"""

def test_dcx_alonenostpl(rstsamples,capfd):
    r=run([Python,'dcx.py','--verbose'])
    assert r.returncode == 0
    out, err = capfd.readouterr()
    assert '\n'.join(out.splitlines()) == """\
doc
    dd.rest
    ra.rest
    sr.rest
    tp.rest"""

@pytest.yield_fixture(params=['docx','pdf','html'])
def makebuild(request,rstsamples):
    oldd = os.getcwd()
    os.chdir('doc')
    r=run(['make',request.param])
    assert r.returncode == 0
    os.chdir(os.path.join('..','..','build'))
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

#The sample Makefile does not support
#conversion from .rest.stpl to .rest
def test_makenostpl(makebuild):
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
      ├─_sources
      ├─_static
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

@pytest.yield_fixture(params=['docx','pdf','html'])
def wafbuild(request,rstsamples):
    r1=run(['waf','configure'])
    assert r1.returncode==0
    r2=run(['waf','--docs',request.param])
    assert r2.returncode==0
    oldd = os.getcwd()
    os.chdir(os.path.join('..','build'))
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def test_wafnostpl(wafbuild):
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
    elif target=='html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  └─html
│     ├─.doctrees
│     ├─_images
│     ├─_sources
│     ├─_static
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
    assert tree(wafbuild[0],with_dot_files=False,max_depth=3)==expected


@pytest.yield_fixture
def rstsampleswithstpl(rstsamples):
    os.rename('doc/ra.rest','doc/ra.rest.stpl')
    yield os.getcwd()

def test_dcx_alonewithstpl(rstsampleswithstpl,capfd):
    r=run([Python,'dcx.py','--verbose'])
    assert r.returncode == 0
    out, err = capfd.readouterr()
    assert '\n'.join(out.splitlines()) == """\
doc
    dd.rest
    ra.rest
    sr.rest
    tp.rest"""

@pytest.yield_fixture(params=['docx','pdf','html'])
def wafbuildwithstpl(request,rstsampleswithstpl):
    oldd = os.getcwd()
    r1=run(['waf','configure'])
    assert r1.returncode==0
    r2=run(['waf','--docs',request.param])
    assert r2.returncode==0
    os.chdir(os.path.join('..','build'))
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def test_wafwithstpl(wafbuildwithstpl):
    target=wafbuildwithstpl[1]
    if target=='docx':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  ├─docx
│  │  ├─dd.docx
│  │  ├─ra.docx
│  │  ├─sr.docx
│  │  └─tp.docx
│  └─ra.rest
└─config.log"""
    elif target=='pdf':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  ├─pdf
│  │  ├─dd.pdf
│  │  ├─ra.pdf
│  │  ├─sr.pdf
│  │  └─tp.pdf
│  └─ra.rest
└─config.log"""
    elif target=='html':
        expected="""\
├─c4che
│  ├─_cache.py
│  └─build.config.py
├─code
│  └─some_tst.c
├─doc
│  ├─html
│  │  ├─.doctrees
│  │  ├─_images
│  │  ├─_sources
│  │  ├─_static
│  │  ├─dd.html
│  │  ├─genindex.html
│  │  ├─index.html
│  │  ├─objects.inv
│  │  ├─ra.html
│  │  ├─search.html
│  │  ├─searchindex.js
│  │  ├─sr.html
│  │  └─tp.html
│  └─ra.rest
└─config.log"""
    assert tree(wafbuildwithstpl[0],with_dot_files=False,max_depth=3)==expected
