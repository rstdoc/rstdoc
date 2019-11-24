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

"""

Examples
========

Example folders (see wscript and Makefile there)::

    rstdoc --rest <folder> [--rstrest]
    rstdoc --stpl <folder> [--rstrest]
    rstdoc --ipdt <folder> [--rstrest]
    rstdoc --over <folder> [--rstrest]

Just create .tags and _links_xxx files::

    rstdoc

Single files to stdout::

    rstdoc dd.rest.stpl - rest
    rstdoc dd.rest.stpl - html.
    rstdoc dd.rest.stpl - docx.
    rstdoc dd.rest.stpl - newname.docx.
    rstdoc dd.rest.stpl - html
    rstdoc dd.rest.stpl
    rstdoc sr.rest.stpl - rst_html
    rstdoc dd.rest.stpl - newname.docx.
    stpl dd.rest.stpl | rstdoc - - dd.html.
    stpl dd.rest.stpl | rstdoc - - dd.html

Files to other files::

    rstdoc dd.rest.stpl dd.rest
    rstdoc dd.rest.stpl dd.html html
    rstdoc dd.rest.stpl dd.html
    rstdoc sr.rest.stpl sr.html rst_html
    rstdoc dd.rest.stpl dd.docx
    rstdoc dd.rest.stpl dd.odt pandoc
    rstdoc dd.rest.stpl dd.odt
    rstdoc sr.rest.stpl sr.odt rst_odt
    rstdoc sr.rest.stpl sr.odt rst
    rstdoc index.rest build/index.html sphinx_html
    rstdoc egcairo.pyg
    rstdoc egdot.dot.stpl
    rstdoc egeps.eps
    rstdoc egother.pyg
    rstdoc egplt.pyg
    rstdoc egpygal.pyg
    rstdoc egpyx.pyg
    rstdoc egsvg.svg.stpl
    rstdoc egtikz.tikz
    rstdoc egtikz1.tikz
    rstdoc eguml.uml
    rstdoc eguml.uml eguml.png

Directories to other directories with out info::

    rstdoc . build html
    rstdoc . build sphinx_html

Grep with python re in .py, .rst, .rest, .stpl, .tpl:

    rstdoc --pygrep inline

Grep for keyword lines containing 'png':

    rstdoc --kw png

Default keyword lines::

    .. {kw1,kw2}
    {{_ID3('kw1 kw2')}}
    %__ID3('kw1 kw2')
    :ID3: kw1 kw2

"""


import sys
import os
from itertools import product
sys.path = ['test/mocks'] + sys.path
import pytest
import re
import rstdoc.dcx as dcx
from rstdoc.dcx import *
from txdir import tree_to_view
import time

def ttv(*a,**ka):
    res = '\n'.join(tree_to_view(*a,with_content=False,**ka))
    res = res.replace('├─ ','├ ').replace('└─ ','└ ').replace('│  ','│ ').replace('   ','  ')

    return res

'''

rstdcx, dcx.py
``````````````

'''

import subprocess
def run(x,**kwargs):
    if 'win' in sys.platform:
        return subprocess.run(x,shell=True,**kwargs)
    else:
        return subprocess.run(x,shell=False,**kwargs)

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

        header, figure, list-table, table,
        code-block, code, math, definition (:id:)
    '''
    lns,res = lnsres
    tgts = list(RstFile.make_tgts(lns,0,
        {".. figure":1,".. math":1,".. table":1,".. code":1}
        ))
    assert next((x.target,x.lnkname) for x in tgts)==res

def test_dcx_regex():
    '''
    Test the regular expressions used in dcx.py.

    '''

    assert list(rexlnks.findall('|xx| A `|lnk|` here |gos11|\n'
                                )) == ['xx', 'gos11']
    assert list(rexlnks.findall('  | |xeps1| | |xeps|  |'
                                )) == ['xeps1', 'xeps']
    assert list(rexlnks.findall('     |dd_figure|: Caption here.'
                                )) == ['dd_figure']
    assert rextgt.search('.. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('  .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('#) .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('- .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('2) .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('2. .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('(a) .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('| .. _`_t11`:').group(1) == '_t11'
    assert rextgt.search('  * - .. _`_t11`:').group(1) == '_t11'
    assert rexitem.match(':t11:').group(1) == 't11'
    assert rexitem.match('**t11**:').group(1) == 't11'
    assert rexitem.match('*t11*:').group(1) == 't11'
    assert reximg.search(r'.. image:: ..\img.png'
                         ).group(1) == r'..\img.png'
    assert reximg.search(r'.. |c:\x y\im.jpg| image:: /tmp/img.png'
                         ).group(1) == '/tmp/img.png'
    assert reximg.search(r'.. image:: c:\tmp\img.png'
                         ).group(1) == r'c:\tmp\img.png'
    assert reximg.search(r'.. figure:: \\public\img.png'
                         ).group(1) == r'\\public\img.png'
    assert rerstinclude.split('.. include:: test.rst'
                              ) == ['', 'test.rst', '']
    assert rerstinclude.split('.. include:: ../test.rst'
                              ) == ['', '../test.rst', '']
    assert rerstinclude.split('  .. include:: ../test.rst'
                              ) == ['  ', '../test.rst', '']
    assert restplinclude.split('%include("test.rst.stpl",v="aparam")'
                               ) == ['', 'test.rst.stpl', '']
    assert restplinclude.split('%include("../test.rst.stpl",v="aparam")'
                               ) == ['', '../test.rst.stpl', '']
    assert restplinclude.split(' % include(  "../test.rst.stpl",v="aparam")'
                               ) == [' ', '../test.rst.stpl', '']
    with pytest.raises(AttributeError):
        rextgt.search('x  .. _`_t11`:').group(1)
    with pytest.raises(AttributeError):
        rextgt.search('.. .. _`_t11`:').group(1)
    with pytest.raises(AttributeError):
        rextgt.search('%# .. _`_t11`:').group(1)
    rexsubtgt.search(' .. |t-1| image:: ').group(1) == 't-1'
    with pytest.raises(AttributeError):
        rextgt.search('%# .. |t11| xx::').group(1)
    with pytest.raises(AttributeError):
        rexitem.match(':``t11``:').group(1)
    with pytest.raises(AttributeError):
        rexitem.match('.. _xx:').group(1)
    with pytest.raises(AttributeError):
        rexitem.match('.. xx:').group(1)

@pytest.yield_fixture
def tmpworkdir(tmpdir):
    """
    Create a temporary working working directory.
    """
    cwd = os.getcwd()
    os.chdir(tmpdir.strpath)
    yield tmpdir
    os.chdir(cwd)

@pytest.yield_fixture(params=[(0,'rest'),(0,'stpl'),(0,'ipdt'),(0,'over'),(1,'rest'),(1,'stpl'),(1,'ipdt'),(1,'over')])
def rstinit(request, tmpworkdir):
    rR, smp = request.param
    #rR,smp=0,'rst'
    smpl = 'tmp%i_%s' % (rR,smp)
    rstrest = ['--rstrest'] if rR else []
    rcmd = ['rstdcx']+(['--rstrest']if rR else[])+['--'+smp,smpl]
    r = run(rcmd)
    assert r.returncode == 0
    oldd = os.getcwd()
    os.chdir(os.path.join(tmpworkdir, smpl))
    yield os.getcwd()
    os.chdir(oldd)

def initfor(rstinitret,smplk):
    #rstinitret='/tmp/pytest-of-roland/pytest-684/test_waf_samples_html_rstinit70/tmp1_over/build/'
    #smplk='over'
    res = len(re.split('tmp.?_'+smplk,rstinitret))>1
    return res

def mkrR(rstinitret): #swap .rest .rst
    def rR(x):
        if isinstance(x,list) or isinstance(x,tuple):
            return [rR(xx) for xx in x]
        if 'tmp1_' in rstinitret:
            x = x.replace('tmp_','tmp1_')
            x = x.replace('.rst','.rrrr')
            x = x.replace('.rest','.rst')
            x = x.replace('.rrrr','.rest')
        else:
            x = x.replace('tmp_','tmp0_')
        return x
    return rR
def test_rstincluded(rstinit):
    '''
    Tests |dcx.rstincluded|.

    '''

    rR = mkrR(rstinit)
    if '1_' in base(rstinit): dcx._set_rstrest('.rst')
    if  initfor(rstinit,'stpl'):
        assert list(rstincluded(rR('ra.rest.stpl'),(r'./doc',))) == rR([
                'ra.rest.stpl', '_links_sphinx.rst'])
        assert list(rstincluded(rR('sy.rest.stpl'),(r'./doc',))) == rR([
                'sy.rest.stpl', '_links_sphinx.rst'])
        assert list(rstincluded(rR('sr.rest.stpl'),(r'./doc',))) == rR([
                'sr.rest.stpl', '_links_sphinx.rst'])
        assert list(rstincluded(rR('dd.rest.stpl'),(r'./doc',))) == rR([
                'dd.rest.stpl', 'dd_included.rst.stpl', 'dd_tables.rst',
                'dd_math.tpl', 'dd_diagrams.tpl', '_links_sphinx.rst'])
        assert list(rstincluded(rR('tp.rest.stpl'),(r'./doc',))) == rR([
                'tp.rest.stpl', '_links_sphinx.rst'])
    elif  initfor(rstinit,'rest'):
        assert list(rstincluded(rR('ra.rest'),(r'./doc',))) == rR([
                'ra.rest', '_links_sphinx.rst'])
        assert list(rstincluded(rR('sr.rest'),(r'./doc',))) == rR([
                'sr.rest', '_links_sphinx.rst', '_links_sphinx.rst'])
        assert list(rstincluded(rR('dd.rest'),(r'./doc',))) == rR([
                'dd.rest', 'somefile.rst', '_links_sphinx.rst'])
        assert list(rstincluded(rR('tp.rest'),(r'./doc',))) == rR([
                'tp.rest', '_sometst.rst', '_links_sphinx.rst'])
    elif  initfor(rstinit,'ipdt'):
        assert list(rstincluded(rR('i.rest.stpl'),(r'./pdt/001',))) == rR([
                'i.rest.stpl', 'i_included.rst.stpl', 'i_tables.rst',
                'i_math.tpl', 'i_diagrams.tpl'])
    elif  initfor(rstinit,'over'):
        assert True

def test_init(rstinit):
    '''
    Tests the initialization of a sample directory tree
    with the ``--stpl tmp`` or ``--rest tmp`` options.

    '''

    rR = mkrR(rstinit)
    if  initfor(rstinit,'ipdt'):
        assert set(ttv('.').splitlines())==set(rR("""\
├ c/
│ └ some.h
├ pdt/
│ ├ 000/
│ │ ├ d.rest.stpl
│ │ ├ gen
│ │ ├ i.rest.stpl
│ │ ├ p.rest.stpl
│ │ ├ repo.pyg
│ │ └ t.rest.stpl
│ ├ 001/
│ │ ├ egcairo.pyg
│ │ ├ egdot.dot.stpl
│ │ ├ egeps.eps
│ │ ├ egother.pyg
│ │ ├ egplt.pyg
│ │ ├ egpygal.pyg
│ │ ├ egpyx.pyg
│ │ ├ egsvg.svg.stpl
│ │ ├ egtikz.tikz
│ │ ├ egtikz1.tikz
│ │ ├ eguml.uml
│ │ ├ i.rest.stpl
│ │ ├ i_diagrams.tpl
│ │ ├ i_included.rst
│ │ ├ i_included.rst.stpl
│ │ ├ i_math.tpl
│ │ └ i_tables.rst
│ ├ conf.py
│ ├ docutils.conf
│ ├ index.rest.stpl
│ └ pdt.rst.tpl
├ waf
├ waf.bat
├ wafw.py
└ wscript""").splitlines())
    elif  initfor(rstinit,'stpl'):
        assert set(ttv('.').splitlines())==set(rR("""\
├ build/
├ doc/
│ ├ _images/
│ ├ dd.rest.stpl
│ ├ dd_diagrams.tpl
│ ├ dd_included.rst.stpl
│ ├ dd_math.tpl
│ ├ dd_tables.rst
│ ├ egcairo.pyg
│ ├ egdot.dot.stpl
│ ├ egeps.eps
│ ├ egother.pyg
│ ├ egplt.pyg
│ ├ egpygal.pyg
│ ├ egpyx.pyg
│ ├ egsvg.svg.stpl
│ ├ egtikz.tikz
│ ├ egtikz1.tikz
│ ├ eguml.uml
│ ├ gen
│ ├ index.rest
│ ├ model.py
│ ├ ra.rest.stpl
│ ├ sr.rest.stpl
│ ├ sy.rest.stpl
│ ├ tp.rest.stpl
│ └ utility.rst.tpl
├ tmp_stpl/
│ └ some.h
├ Makefile
├ conf.py
├ dcx.py
├ docutils.conf
├ reference.docx
├ reference.odt
├ reference.tex
├ waf
├ waf.bat
├ wafw.py
└ wscript""").splitlines())
    elif  initfor(rstinit,'rest'):
        assert set(ttv('.').splitlines())==set(rR("""\
├ Makefile
├ build/
├ conf.py
├ dcx.py
├ doc/
│ ├ _images/
│ ├ dd.rest
│ ├ egcairo.pyg
│ ├ egdot.dot.stpl
│ ├ egeps.eps
│ ├ egother.pyg
│ ├ egplt.pyg
│ ├ egpygal.pyg
│ ├ egpyx.pyg
│ ├ egsvg.svg.stpl
│ ├ egtikz.tikz
│ ├ egtikz1.tikz
│ ├ eguml.uml
│ ├ gen
│ ├ index.rest
│ ├ ra.rest
│ ├ sr.rest
│ └ tp.rest
├ docutils.conf
├ reference.docx
├ reference.odt
├ reference.tex
├ tmp_rest/
│ └ some.h
├ waf
├ waf.bat
├ wafw.py
└ wscript""").splitlines())
    elif  initfor(rstinit,'over'):
        assert set(ttv('.').splitlines())==set(rR("""\
├ dev/
│ ├ hw/
│ │ ├ casing/
│ │ │ ├ plan.rest
│ │ │ ├ scad/
│ │ │ └ test/
│ │ │   └ stability.rest
│ │ ├ pcb1/
│ │ │ ├ pcb1.sch
│ │ │ ├ plan.rest
│ │ │ └ test/
│ │ └ test/
│ ├ issues/
│ │ ├ issue1.rest
│ │ └ issue2.rest
│ ├ sw/
│ │ ├ android/
│ │ │ ├ app/
│ │ │ ├ plan.rest
│ │ │ └ testapp/
│ │ ├ fw/
│ │ │ ├ controller1/
│ │ │ │ └ C/
│ │ │ │   └ init.c
│ │ │ ├ plan.rest
│ │ │ └ test/
│ │ └ test/
│ └ test/
├ doc/
│ ├ index.rest
│ └ tutorial.rest
├ org/
│ ├ contributor/
│ │ └ c1/
│ │   ├ assigned.rest
│ │   └ log/
│ │     └ 2019.rest
│ ├ discussion/
│ │ └ topic1.rest
│ ├ mediation/
│ │ └ conflict1.rest
│ └ process/
│   └ SOP/
│     └ purchase.rest
├ pdt/
│ └ 000/
│   ├ do.rest
│   ├ info.rest
│   ├ plan.rest
│   └ test.rest
├ contribution.rest
├ index.rest
├ readme.rest
├ waf
├ waf.bat
├ wafw.py
└ wscript""").splitlines())


def test_dcx_alone_samples(rstinit):
    '''
    Tests calling ``rstdcx``/``dcx.py`` without parameters.

    '''

    rR = mkrR(rstinit)
    if  initfor(rstinit,'ipdt') or initfor(rstinit,'over'): #has no separate dcx.py
        r = run(['rstdoc'])
    else:
        r = run(['python', 'dcx.py'])
    assert r.returncode == 0
    if  initfor(rstinit,'over'):
        assert exists(".tags")
    elif  initfor(rstinit,'ipdt'):
        assert exists("build/c/some_tst.c")
        assert exists(rR("pdt/000/i.rest"))
        assert exists(rR("pdt/000/p.rest"))
        assert exists(rR("pdt/000/d.rest"))
        assert exists(rR("pdt/000/t.rest"))
        assert exists(rR("pdt/000/_sometst.rst"))
        assert exists(rR("pdt/001/i.rest"))
        assert exists(rR("pdt/001/i_included.rst"))
        assert exists(rR("pdt/001/egdot.dot"))
        assert exists(rR("pdt/001/egsvg.svg"))
        assert exists(rR("pdt/_links_sphinx.rst"))
        assert exists(rR("pdt/_links_latex.rst"))
        assert exists(rR("pdt/_links_html.rst"))
        assert exists(rR("pdt/_links_pdf.rst"))
        assert exists(rR("pdt/_links_docx.rst"))
        assert exists(rR("pdt/_links_odt.rst"))
        assert exists(".tags")
        assert '\tpdt/000/' in open(".tags").read()
        assert '<file:../000/' in open(rR("pdt/_links_html.rst")).read()
    elif  initfor(rstinit,'rest'):
        assert exists("doc/egdot.dot")
        assert exists("doc/egsvg.svg")
        assert exists(rR("doc/_sometst.rst"))
        assert exists(rR("build/tmp_rest/some_tst.c"))
        assert exists(rR("doc/_traceability_file.rst"))
        assert exists(rR("doc/_links_sphinx.rst"))
        assert exists(rR("doc/_links_latex.rst"))
        assert exists(rR("doc/_links_html.rst"))
        assert exists(rR("doc/_links_pdf.rst"))
        assert exists(rR("doc/_links_docx.rst"))
        assert exists(rR("doc/_links_odt.rst"))
        assert exists(".tags")
        assert '\tdoc/' in open(".tags").read()
        assert '<file:dd.html' in open(rR("doc/_links_html.rst")).read()
    elif  initfor(rstinit,'stpl'):
        assert exists(rR("doc/dd.rest"))
        assert exists(rR("doc/dd_included.rst"))
        assert exists(rR("doc/egdot.dot"))
        assert exists(rR("doc/egsvg.svg"))
        assert exists(rR("doc/ra.rest"))
        assert exists(rR("doc/sr.rest"))
        assert exists(rR("doc/sy.rest"))
        assert exists(rR("doc/tp.rest"))
        assert exists(rR("doc/_sometst.rst"))
        assert exists(rR("build/tmp_stpl/some_tst.c"))
        assert exists(rR("doc/_traceability_file.rst"))
        assert exists(rR("doc/_links_sphinx.rst"))
        assert exists(rR("doc/_links_latex.rst"))
        assert exists(rR("doc/_links_html.rst"))
        assert exists(rR("doc/_links_pdf.rst"))
        assert exists(rR("doc/_links_docx.rst"))
        assert exists(rR("doc/_links_odt.rst"))
        assert exists(rR(".tags"))
        assert '\tdoc/' in open(".tags").read()
        assert '<file:dd.html' in open(rR("doc/_links_html.rst")).read()

@pytest.mark.parametrize('cmd_result',[
    ('rstdcx dd.rest.stpl - rest',['default-role:: math',r'<file:dd.html#'])
    ,('rstdcx dd.rest.stpl - html.',['default-role:: math',r'<file:dd.html#'])
    ,('rstdcx dd.rest.stpl - docx.',['default-role:: math',r'<file:dd.docx#'])
    ,('rstdcx dd.rest.stpl - newname.docx.',['default-role:: math',r'<file:newname.docx#'])
    ,('rstdcx dd.rest.stpl - html',["DOCTYPE html",'ref="file:dd.html#'])
    ,('rstdcx dd.rest.stpl',["DOCTYPE html",'ref="file:dd.html#'])
    ,('rstdcx sr.rest.stpl - rst_html',["DOCTYPE html",'ref="file:sr.html#'])
    ,('rstdcx dd.rest.stpl - newname.docx.',['default-role:: math',r'<file:newname.docx#'])
    ,('stpl dd.rest.stpl | rstdcx - - dd.html.',['default-role:: math',r'<file:dd.html#'])
    ,('stpl dd.rest.stpl | rstdcx - - dd.html',["DOCTYPE html",'ref="file:dd.html#'])
])
def test_dcx_in_out(rstinit,cmd_result):
    '''
    Tests calling ``rstdcx``/``dcx.py``
    with in-file or standard in to standard out.

    '''
    rR = mkrR(rstinit)
    if  initfor(rstinit,'ipdt') or initfor(rstinit,'over'):
        return
    cmd,result = cmd_result
    tcmd = rR(cmd)
    os.chdir('doc')
    if not os.path.exists(tcmd.split()[1]):
        if tcmd.startswith('stpl'):
            return
        else:
            tcmd = tcmd.replace('.stpl','')
    r = subprocess.run(tcmd,shell=True,stdout=subprocess.PIPE)
    assert r.returncode == 0
    out = r.stdout.decode('utf-8')
    for res in result:
        assert re.search(res,out)

@pytest.mark.parametrize('cmd_exists_not_exists',[
(['dd.rest.stpl','dd.rest'],['dd.rest'],[])
,(['dd.rest.stpl','dd.html','html'],['dd.html'],['dd.rest'])
,(['dd.rest.stpl','dd.html'],['dd.html'],['dd.rest'])
,(['sr.rest.stpl','sr.html','rst_html'],['sr.html'],['sr.rest'])
,(['dd.rest.stpl','dd.docx'],['dd.docx'],['dd.rest'])
,(['dd.rest.stpl','dd.odt','pandoc'],['dd.odt'],['dd.rest'])
,(['dd.rest.stpl','dd.odt'],['dd.odt'],['dd.rest'])
,(['sr.rest.stpl','sr.odt','rst_odt'],['sr.odt'],['sr.rest'])
,(['sr.rest.stpl','sr.odt','rst'],['sr.odt'],['sr.rest'])
,(['index.rest','build/index.html','sphinx_html'],['build/index.html'],[])
,(['egcairo.pyg'],['_images/egcairo.png'],[])
,(['egdot.dot.stpl'],['_images/egdot.png'],['egdot.dot'])
,(['egeps.eps'],['_images/egeps.png'],[])
,(['egother.pyg'],['_images/egother.png'],[])
,(['egplt.pyg'],['_images/egplt.png'],[])
,(['egpygal.pyg'],['_images/egpygal.png'],[])
,(['egpyx.pyg'],['_images/egpyx.png'],[])
,(['egsvg.svg.stpl'],['_images/egsvg.png'],['egsvg.svg'])
,(['egtikz.tikz'],['_images/egtikz.png'],[])
,(['egtikz1.tikz'],['_images/egtikz1.png'],[])
,(['eguml.uml'],['_images/eguml.png'],[])
,(['eguml.uml','eguml.png'],['eguml.png'],['_images/eguml.png'])
,(['.','build','html'],['build/dd.html'],[])
,(['.','build','sphinx_html'],['build/index.html'],[])
])
def test_dcx_out_file(rstinit,cmd_exists_not_exists):
    '''
    Tests calling ``rstdcx``/``dcx.py``
    with in-file and out-file and out type parameter.

    '''
    if  initfor(rstinit,'ipdt') or initfor(rstinit,'over'):
        return
    rR = mkrR(rstinit)
    cmd,result,notexists = cmd_exists_not_exists
    tcmd = rR(cmd)
    os.chdir('doc')
    notrest = tcmd[0].replace('.stpl','')
    if not os.path.exists(tcmd[0]):
        tcmd[0] = notrest
        if len(tcmd)>1 and tcmd[1]==notrest:
            return
        notrest = None
    ncmd = [r'rstdcx']+tcmd
    r=run(ncmd)
    assert r.returncode == 0
    assert os.path.exists(rR(result[0]))
    if notrest:
        for ne in notexists:
            assert not os.path.exists(rR(ne))

@pytest.yield_fixture(params=['docx','pdf','html'])
def makebuild(request,rstinit):
    oldd = os.getcwd()
    if not initfor(rstinit,'ipdt') and not initfor(rstinit,'over'):
        r=run(['make',request.param])
        assert r.returncode == 0
        os.chdir('build')
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def tree3(x,maxdepth=3):
    tres = ttv(x,with_dot=False,maxdepth=maxdepth)
    return tres

def test_make_samples(makebuild):
    '''
    Tests building the samples with Makefile

    '''

    rstinit,target = makebuild
    rR = mkrR(rstinit)
    if  initfor(rstinit,'ipdt') or initfor(rstinit,'over'):
        return
    elif  initfor(rstinit,'rest'):
        expected_no_html=rR("""\
├ doc/
│ └ {0}/
│   ├ dd.{0}
│   ├ ra.{0}
│   ├ sr.{0}
│   └ tp.{0}
└ tmp_rest/
  └ some_tst.c""")
        if target in ['docx','pdf']:
            expected=expected_no_html.format(target)
        elif target=='html':
            expected=rR("""\
├ doc/
│ ├ doctrees/
│ │ ├ dd.doctree
│ │ ├ environment.pickle
│ │ ├ index.doctree
│ │ ├ ra.doctree
│ │ ├ sr.doctree
│ │ └ tp.doctree
│ └ html/
│   ├ _images/
│   ├ _sources/
│   ├ _static/
│   ├ _traceability_file.svg
│   ├ dd.html
│   ├ genindex.html
│   ├ index.html
│   ├ objects.inv
│   ├ ra.html
│   ├ search.html
│   ├ searchindex.js
│   ├ sr.html
│   └ tp.html
└ tmp_rest/
  └ some_tst.c""")
        assert tree3(rstinit)==expected
    elif  initfor(rstinit,'stpl'):
        expected_no_html=rR("""\
├ doc/
│ └ {0}/
│   ├ dd.{0}
│   ├ ra.{0}
│   ├ sr.{0}
│   ├ sy.{0}
│   └ tp.{0}
└ tmp_stpl/
  └ some_tst.c""")
        if target in ['docx','pdf']:
            expected=expected_no_html.format(target)
        elif target=='html':
            expected=rR("""\
├ doc/
│ ├ doctrees/
│ │ ├ dd.doctree
│ │ ├ environment.pickle
│ │ ├ index.doctree
│ │ ├ ra.doctree
│ │ ├ sr.doctree
│ │ ├ sy.doctree
│ │ └ tp.doctree
│ └ html/
│   ├ _images/
│   ├ _sources/
│   ├ _static/
│   ├ _traceability_file.svg
│   ├ dd.html
│   ├ genindex.html
│   ├ index.html
│   ├ objects.inv
│   ├ ra.html
│   ├ search.html
│   ├ searchindex.js
│   ├ sr.html
│   ├ sy.html
│   └ tp.html
└ tmp_stpl/
  └ some_tst.c""")
        assert tree3(rstinit)==expected

waf_some = ['docx','odt','pdf','html','latex',
            'sphinx_html','sphinx_latex','rst_html','rst_latex','rst_odt']
waf_non_sphinx = [x for x in waf_some if not x.startswith('sphinx')]
waf_sphinx = [x for x in waf_some if x.startswith('sphinx')]

@pytest.yield_fixture(params=waf_some)
def wafbuild(request,rstinit):
    r1=run(['waf','configure'])
    assert r1.returncode==0
    r2=run(['waf','--docs',request.param])
    assert r2.returncode==0
    oldd = os.getcwd()
    os.chdir('build')
    yield (os.getcwd(),request.param)
    os.chdir(oldd)

def test_waf_samples(wafbuild):
    '''
    Tests running Waf on the sample projects.

    '''
    rstinit,target = wafbuild
    try:
        _,ext = target.split('_')
    except: ext = target
    if ext.endswith('latex') or ext.endswith('html'):
        extra = '\n│ ├ _images'
        if ext.endswith('html'):
            extra += '\n│ ├ _traceability_file.svg'
    else:
        extra = ''
    if  initfor(rstinit,'over'):
        expected_non_sphinx="""\
├ dev/
│ ├ hw/
│ │ ├ casing/
│ │ └ pcb1/
│ ├ issues/
│ │ ├ issue1.{0}
│ │ └ issue2.{0}
│ └ sw/
│   ├ android/
│   └ fw/
├ doc/
│ └ tutorial.{0}
├ org/
│ ├ contributor/
│ │ └ c1/
│ ├ discussion/
│ │ └ topic1.{0}
│ ├ mediation/
│ │ └ conflict1.{0}
│ └ process/
│   └ SOP
├ pdt/
│ └ 000/
│   ├ do.{0}
│   ├ info.{0}
│   ├ plan.{0}
│   └ test.{0}
├ contribution.{0}
└ readme.{0}"""
        if target in waf_non_sphinx or target=='sphinx_html':
            expected=expected_non_sphinx.format(ext)
        else:
            expected="""
└ sphinx_latex/
  ├ Makefile
  ├ index.tex
"""
        realout = tree3(rstinit,4)
        for x in expected.splitlines():
            xchk=x.strip('└│├ ')
            assert realout.find(xchk)>=0, "%s not found"%xchk
    elif  initfor(rstinit,'ipdt'):
        expected_non_sphinx="""\
└ pdt/
  ├ 000/
  │ ├ d.{0}
  │ ├ i.{0}
  │ ├ p.{0}
  │ └ t.{0}
  └ 001/
      └ i.{0}"""
        if target in waf_non_sphinx:
            expected = expected_non_sphinx.format(ext)
        elif target=='sphinx_html':
            expected="""\
└ pdt/
  ├ 000/
  │ ├ d.html
  │ ├ i.html
  │ ├ p.html
  │ └ t.html
  ├ 001/
  │ └ i.html
  ├ _images/
  │ ├ egcairo.png
  │ ├ egdot.png
  │ ├ egeps.png
  │ ├ egother.png
  │ ├ egplt.png
  │ ├ egpygal.png
  │ ├ egpyx.png
  │ ├ egsvg.png
  │ ├ egtikz.png
  │ ├ egtikz1.png
  │ ├ eguml.png
  │ └ repo.png
  ├ genindex.html
  ├ index.html
  ├ _traceability_file.svg
  └ _traceability_file.png"""
        elif target=='sphinx_latex':
            expected="""\
└ pdt/
  ├ Makefile
  ├ _traceability_file.png
  ├ egcairo.png
  ├ egdot.png
  ├ egeps.png
  ├ egother.png
  ├ egplt.png
  ├ egpygal.png
  ├ egpyx.png
  ├ egsvg.png
  ├ egtikz.png
  ├ egtikz1.png
  ├ eguml.png
  ├ index.tex
  ├ make.bat
  └ repo.png"""
        realout = tree3(target)
        for x in expected.splitlines():
            xchk=x.strip('└│├ ')
            assert realout.find(xchk)>=0, "%s not found"%xchk
    else:#not idpt or over
        is_stpl = initfor(rstinit,'stpl')
        #rstinit='/tmp/pytest-of-roland/pytest-702/test_waf_samples_sphinx_html_r0/tmp0_rest/build'
        tmpx_xxx = re.search('(tmp.?_\w+)',rstinit).groups()[0]
        expected_non_sphinx="""\
├ doc/
│ └ {0}{2}
│   ├ dd.{1}
│   ├ ra.{1}
│   ├ sr.{1}
"""+("""\
│   ├ sy.{1}
""" if is_stpl else '')+"""\
│   └ tp.{1}
├ {3}
│ └ some_tst.c
└ config.log"""
        if target in waf_non_sphinx:
            expected=expected_non_sphinx.format(target,ext,extra,tmpx_xxx)
        elif target=='sphinx_latex':
            expected="""\
├ doc/
│ └ sphinx_latex/
│   ├ Makefile
│   ├ _traceability_file.png
│   ├ egcairo.png
│   ├ egdot.png
│   ├ egeps.png
│   ├ egother.png
│   ├ egplt.png
│   ├ egpygal.png
│   ├ egpyx.png
│   ├ egsvg.png
│   ├ egtikz.png
│   ├ egtikz1.png
│   ├ eguml.png
│   ├ make.bat
│   ├ python.ist
│   ├ index.tex
├ {}/
│ └ some_tst.c
└ config.log""".format(tmpx_xxx)
        elif target=='sphinx_html':
            expected="""\
├ doc/
│ └ sphinx_html/
│   ├ _images/
│   ├ _sources/
│   ├ _static/
│   ├ _traceability_file.svg
│   ├ dd.html
│   ├ index.html
│   ├ ra.html
│   ├ sr.html
"""+("""\
│   ├ sy.html
""" if is_stpl else '')+"""\
│   └ tp.html
├ {}/
│ └ some_tst.c
└ config.log""".format(tmpx_xxx)
        realout = tree3(rstinit)
        for x in expected.splitlines():
            xchk=x.strip('└│├ ')
            assert realout.find(xchk)>=0, "%s not found"%xchk

def test_docparts_after():
    '''
    Tests |dcx.doc_parts| with different parameters for documentation extraction.

    '''

    res = list(doc_parts(['/// \\brief\n',"/// afun's description\n","//\n"
        ,'void afun(\n','int x //int variable\n',')\n','\n'],
        signature='cpp',relim=r'\\brief|//$',reid=r'\s(\w\+)\('))
    assert res == ['.. code-block:: cpp\n', '', '   void afun(\n',
        '   int x //int variable\n', '   )\n', '', "afun's description\n"]


_a_fix = lambda x: os.path.join(os.path.dirname(__file__),'fixtures',x)
def _cp_pyg():
    for x in os.listdir(_a_fix('')):
        if x.endswith('.pyg'):
            shutil.copy2(_a_fix(x),x)


@pytest.mark.parametrize( 'outinfo',[
    'pdf','docx','html','odt','latex',
    'rst_odt','rst_html','rst_latex','sphinx_html'])
def test_with_images(outinfo):
    with opn(_a_fix('with_images.rest.stpl')) as fp:
        lines = fp.readlines()
    filename = convert_in_tempdir(lines,outinfo=outinfo)
    assert exists(filename)

@pytest.mark.parametrize('infile,outext',
                         product(['with_images','png_embed','svg_embed'],
                             ['.pdf', '.docx', '.html', '.odt', '.latex'])
                         )
def test_convert_with_images_no_outinfo(tmpworkdir,infile,outext):
    '''
    Tests |dcx.convert| with images on the fly in ``rest.stpl`` files
    for different targets.

    '''

    import shutil
    if 'embed' in infile:
        _cp_pyg()
    shutil.copy2(_a_fix(infile)+'.rest.stpl',infile+'.rest.stpl')
    filename = infile+outext
    convert(infile+'.rest.stpl',filename,None)
    assert exists(filename)

@pytest.mark.parametrize('infile,outext',
                         product(['with_images','png_embed','svg_embed'],
                             ['.html', '.docx'])
                         )
def test_include_cmd(tmpworkdir,infile,outext):
    '''
    Tests |rstdcx| with -I option and ``.rest.stpl`` files generating images on the fly
    and embedding for HTML and DOCX.

    '''

    if 'embed' in infile:
        _cp_pyg()
    r=run(['rstdcx',infile+'.rest.stpl', infile+outext, '-I', dirname(_a_fix(infile))])
    assert r.returncode == 0
    assert exists(infile+outext)

def test_pygrep():
    os.chdir(_a_fix(''))
    r = run(['rstdcx','--pygrep', 'inline'],stdout=subprocess.PIPE)
    outlines = r.stdout.decode().splitlines()
    assert len(outlines) > 0
    for x in outlines:
        assert 'inline' in x

def test_kw():
    os.chdir(_a_fix(''))
    r = run(['rstdcx','--kw', 'png'],stdout=subprocess.PIPE)
    outlines = r.stdout.decode().splitlines()
    assert len(outlines) > 0
    for x in outlines:
        assert 'png' in x

# vim: ts=4 sw=4 sts=4 et noai nocin nosi inde=
