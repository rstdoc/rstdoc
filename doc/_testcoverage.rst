============================= test session starts ==============================
platform linux -- Python 3.8.0, pytest-5.2.4, py-1.8.0, pluggy-0.13.0
rootdir: /home/roland/mine/rstdoc, inifile: pytest.ini
plugins: mock-1.11.0, cov-2.8.1
collected 518 items

rstdoc/dcx.py .....FF.F.............                                     [  4%]
rstdoc/retable.py ..                                                     [  4%]
test/test_dcx.py ....................................................... [ 15%]
........................................................................ [ 29%]
........................................................................ [ 43%]
............FFFFFFFFF............FF.FFFFFFFFF............FF............. [ 56%]
.............................................................FF..FF..FF. [ 70%]
.FF..FF..FF..FF..FF..FF..FFFFFFFFFEFFFFFFFE..FF..FF..FF..FF..FF..FF..... [ 84%]
....F.......................                                             [ 90%]
test/test_fromdocx.py .                                                  [ 90%]
test/test_rst_tables.py ..................................               [ 96%]
test/test_unretable.py ................                                  [100%]

==================================== ERRORS ====================================
___________ ERROR at setup of test_waf_samples[sphinx_html-rstinit7] ___________

request = <SubRequest 'wafbuild' for <Function test_waf_samples[sphinx_html-rstinit7]>>
rstinit = '/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over'

    @pytest.yield_fixture(params=waf_some)
    def wafbuild(request,rstinit):
        r1=run(['waf','configure'])
        assert r1.returncode==0
        r2=run(['waf','--docs',request.param])
>       assert r2.returncode==0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['waf', '--docs', 'sphinx_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:717: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.162s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/build'
[1/2] Compiling index.rst
[2/2] Compiling doc/index.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/build'
---------------------------- Captured stderr setup -----------------------------
Build failed
Traceback (most recent call last):
  File "/home/roland/.local/bin/.waf3-2.0.18-483914458327fa78927e9f946b6ff914/waflib/Task.py", line 180, in process
    ret=self.run()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 3984, in run
    rst_sphinx(inpth, self.outputs[0].abspath(),
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1158, in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
rstdoc.dcx.RstDocError: Error code 2 returned from 
sphinx-build -b html . build/sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=index
in
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over

[stdout]
Running Sphinx v2.2.1
loading translations [None]... not available for built-in messages
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 6 source files that are out of date
updating environment: [new config] 6 added, 0 changed, 0 removed
reading sources... [ 16%] _links_docx
reading sources... [ 33%] _links_html
reading sources... [ 50%] _links_latex
reading sources... [ 66%] _links_odt
reading sources... [ 83%] _links_pdf
reading sources... [100%] _links_sphinx


[stderr]

Sphinx error:
master file /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/index.rest not found


Traceback (most recent call last):
  File "/home/roland/.local/bin/.waf3-2.0.18-483914458327fa78927e9f946b6ff914/waflib/Task.py", line 180, in process
    ret=self.run()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 3984, in run
    rst_sphinx(inpth, self.outputs[0].abspath(),
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1158, in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
rstdoc.dcx.RstDocError: Error code 2 returned from 
sphinx-build -b html . ../build/sphinx_html/doc -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=index
in
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/doc

[stdout]
Running Sphinx v2.2.1
loading translations [None]... not available for built-in messages
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 0 source files that are out of date
updating environment: [new config] 0 added, 0 changed, 0 removed

[stderr]

Sphinx error:
master file /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r7/tmp1_over/doc/index.rest not found


__________ ERROR at setup of test_waf_samples[sphinx_latex-rstinit7] ___________

request = <SubRequest 'wafbuild' for <Function test_waf_samples[sphinx_latex-rstinit7]>>
rstinit = '/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over'

    @pytest.yield_fixture(params=waf_some)
    def wafbuild(request,rstinit):
        r1=run(['waf','configure'])
        assert r1.returncode==0
        r2=run(['waf','--docs',request.param])
>       assert r2.returncode==0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['waf', '--docs', 'sphinx_latex'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:717: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.171s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/build'
[1/2] Compiling index.rst
[2/2] Compiling doc/index.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/build'
---------------------------- Captured stderr setup -----------------------------
Build failed
Traceback (most recent call last):
  File "/home/roland/.local/bin/.waf3-2.0.18-483914458327fa78927e9f946b6ff914/waflib/Task.py", line 180, in process
    ret=self.run()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 3984, in run
    rst_sphinx(inpth, self.outputs[0].abspath(),
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1158, in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
rstdoc.dcx.RstDocError: Error code 2 returned from 
sphinx-build -b latex . build/sphinx_latex -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=index -D latex_elements.preamble=\usepackage{pgfplots}\usepackage{unicode-math}\usepackage{tikz}\usepackage{caption}\captionsetup[figure]{labelformat=empty}\usetikzlibrary{  arrows,snakes,backgrounds,patterns,matrix,shapes,  fit,calc,shadows,plotmarks,intersections  } -D latex_engine=xelatex
in
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over

[stdout]
Running Sphinx v2.2.1
loading translations [None]... not available for built-in messages
building [mo]: targets for 0 po files that are out of date
building [latex]: all documents
updating environment: [new config] 6 added, 0 changed, 0 removed
reading sources... [ 16%] _links_docx
reading sources... [ 33%] _links_html
reading sources... [ 50%] _links_latex
reading sources... [ 66%] _links_odt
reading sources... [ 83%] _links_pdf
reading sources... [100%] _links_sphinx


[stderr]
WARNING: no Babel option known for language 'None'

Sphinx error:
master file /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/index.rest not found


Traceback (most recent call last):
  File "/home/roland/.local/bin/.waf3-2.0.18-483914458327fa78927e9f946b6ff914/waflib/Task.py", line 180, in process
    ret=self.run()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 3984, in run
    rst_sphinx(inpth, self.outputs[0].abspath(),
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1158, in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
rstdoc.dcx.RstDocError: Error code 2 returned from 
sphinx-build -b latex . ../build/sphinx_latex/doc -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=index -D latex_elements.preamble=\usepackage{pgfplots}\usepackage{unicode-math}\usepackage{tikz}\usepackage{caption}\captionsetup[figure]{labelformat=empty}\usetikzlibrary{  arrows,snakes,backgrounds,patterns,matrix,shapes,  fit,calc,shadows,plotmarks,intersections  } -D latex_engine=xelatex
in
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/doc

[stdout]
Running Sphinx v2.2.1
loading translations [None]... not available for built-in messages
building [mo]: targets for 0 po files that are out of date
building [latex]: all documents
updating environment: [new config] 0 added, 0 changed, 0 removed

[stderr]
WARNING: no Babel option known for language 'None'

Sphinx error:
master file /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_7/tmp1_over/doc/index.rest not found


=================================== FAILURES ===================================
_________________________ [doctest] rstdoc.dcx.convert _________________________
2084         >>> exists('tst.png')
2085         True
2086         >>> rmrf('tst.png')
2087         >>> exists('tst.png')
2088         False
2089 
2090         >>> convert('ra.rest.stpl') #doctest: +ELLIPSIS
2091         ['<!DOCTYPE html>\n', ...
2092 
2093         >>> convert('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
UNEXPECTED EXCEPTION: RstDocError("Error code 1 returned from \npandoc --standalone -f rst -t docx ra.rest.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx\nin\n/home/roland/mine/rstdoc/doc\n\n[stdout]\n\n[stderr]\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65\npandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)\n")
Traceback (most recent call last):

  File "/usr/lib/python3.8/doctest.py", line 1328, in __run
    exec(compile(example.source, filename, "single",

  File "<doctest rstdoc.dcx.convert[12]>", line 1, in <module>

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1250, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (

rstdoc.dcx.RstDocError: Error code 1 returned from 
pandoc --standalone -f rst -t docx ra.rest.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx
in
/home/roland/mine/rstdoc/doc

[stdout]

[stderr]
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65
pandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)


/home/roland/mine/rstdoc/rstdoc/dcx.py:2093: UnexpectedException
___________________ [doctest] rstdoc.dcx.convert_in_tempdir ____________________
1041         >>> exists('tst.png')
1042         True
1043         >>> rmrf('tst.png')
1044         >>> exists('tst.png')
1045         False
1046 
1047         >>> convert('ra.rest.stpl') #doctest: +ELLIPSIS
1048         ['<!DOCTYPE html>\n', ...
1049 
1050         >>> convert('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
UNEXPECTED EXCEPTION: RstDocError("Error code 1 returned from \npandoc --standalone -f rst -t docx ra.rest.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx\nin\n/home/roland/mine/rstdoc/doc\n\n[stdout]\n\n[stderr]\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65\npandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)\n")
Traceback (most recent call last):

  File "/usr/lib/python3.8/doctest.py", line 1328, in __run
    exec(compile(example.source, filename, "single",

  File "<doctest rstdoc.dcx.convert_in_tempdir[12]>", line 1, in <module>

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1250, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (

rstdoc.dcx.RstDocError: Error code 1 returned from 
pandoc --standalone -f rst -t docx ra.rest.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx
in
/home/roland/mine/rstdoc/doc

[stdout]

[stderr]
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65
pandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)


/home/roland/mine/rstdoc/rstdoc/dcx.py:1050: UnexpectedException
__________________________ [doctest] rstdoc.dcx.dorst __________________________
1834         ['.. default-role:: math\n', ...
1835 
1836         >>> dorst(['hi there']) #doctest: +ELLIPSIS
1837         ['.. default-role:: math\n', '\n', 'hi there\n', ...
1838 
1839         >>> dorst(['hi there'], None,'html') #doctest: +ELLIPSIS
1840         <!DOCTYPE html>
1841         ...
1842 
1843         >>> dorst('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
UNEXPECTED EXCEPTION: RstDocError("Error code 1 returned from \npandoc --standalone -f rst -t docx ra.rest.stpl.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx\nin\n/home/roland/mine/rstdoc/doc\n\n[stdout]\n\n[stderr]\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'r' at line 393 column 45\n[WARNING] Reference not found for 'f' at line 393 column 54\n[WARNING] Reference not found for 'v' at line 393 column 60\npandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)\n")
Traceback (most recent call last):

  File "/usr/lib/python3.8/doctest.py", line 1328, in __run
    exec(compile(example.source, filename, "single",

  File "<doctest rstdoc.dcx.dorst[7]>", line 1, in <module>

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1250, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (

rstdoc.dcx.RstDocError: Error code 1 returned from 
pandoc --standalone -f rst -t docx ra.rest.stpl.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx
in
/home/roland/mine/rstdoc/doc

[stdout]

[stderr]
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65
[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65
[WARNING] Reference not found for 'r' at line 393 column 45
[WARNING] Reference not found for 'f' at line 393 column 54
[WARNING] Reference not found for 'v' at line 393 column 60
pandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)


/home/roland/mine/rstdoc/rstdoc/dcx.py:1843: UnexpectedException
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists1] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd1/tmp1_rest'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.html', 'html'], ['dd.html'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.html', 'html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd1/tmp1_rest/doc/dd.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists2] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd2/tmp1_rest'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.html'], ['dd.html'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd2/tmp1_rest/doc/dd.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists3] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd3/tmp1_rest'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.html', 'rst_html'], ['sr.html'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.html', 'rst_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd3/tmp1_rest/doc/sr.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists4] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd4/tmp1_rest'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.docx'], ['dd.docx'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.docx'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd4/tmp1_rest/doc/dd.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists5] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd5/tmp1_rest'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.odt', 'pandoc'], ['dd.odt'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.odt', 'pandoc'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd5/tmp1_rest/doc/dd.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists6] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd6/tmp1_rest'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.odt'], ['dd.odt'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.odt'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd6/tmp1_rest/doc/dd.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists7] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd7/tmp1_rest'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.odt', 'rst_odt'], ['sr.odt'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.odt', 'rst_odt'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd7/tmp1_rest/doc/sr.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists8] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd8/tmp1_rest'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.odt', 'rst'], ['sr.odt'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.odt', 'rst'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd8/tmp1_rest/doc/sr.rest'
______________ test_dcx_out_file[rstinit4-cmd_exists_not_exists9] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd9/tmp1_rest'
cmd_exists_not_exists = (['index.rest', 'build/index.html', 'sphinx_html'], ['build/index.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'index.rest', 'build/index.html', 'sphinx_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd9/tmp1_rest/doc/index.rest'
_____________ test_dcx_out_file[rstinit4-cmd_exists_not_exists22] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd22/tmp1_rest'
cmd_exists_not_exists = (['.', 'build', 'html'], ['build/dd.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
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
>       assert os.path.exists(result[0])
E       AssertionError: assert False
E        +  where False = <function exists at 0x7f3285cde1f0>('build/dd.html')
E        +    where <function exists at 0x7f3285cde1f0> = <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'>.exists
E        +      where <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'> = os.path

/home/roland/mine/rstdoc/test/test_dcx.py:597: AssertionError
----------------------------- Captured stderr call -----------------------------
_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_____________ test_dcx_out_file[rstinit4-cmd_exists_not_exists23] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit4_cmd23/tmp1_rest'
cmd_exists_not_exists = (['.', 'build', 'sphinx_html'], ['build/index.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
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
>       assert os.path.exists(result[0])
E       AssertionError: assert False
E        +  where False = <function exists at 0x7f3285cde1f0>('build/index.html')
E        +    where <function exists at 0x7f3285cde1f0> = <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'>.exists
E        +      where <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'> = os.path

/home/roland/mine/rstdoc/test/test_dcx.py:597: AssertionError
----------------------------- Captured stderr call -----------------------------
_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists1] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd1/tmp1_stpl'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.html', 'html'], ['dd.html'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.html', 'html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd1/tmp1_stpl/doc/dd.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists2] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd2/tmp1_stpl'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.html'], ['dd.html'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd2/tmp1_stpl/doc/dd.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists3] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd3/tmp1_stpl'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.html', 'rst_html'], ['sr.html'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.html', 'rst_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd3/tmp1_stpl/doc/sr.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists4] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd4/tmp1_stpl'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.docx'], ['dd.docx'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.docx'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd4/tmp1_stpl/doc/dd.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists5] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd5/tmp1_stpl'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.odt', 'pandoc'], ['dd.odt'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.odt', 'pandoc'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd5/tmp1_stpl/doc/dd.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists6] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd6/tmp1_stpl'
cmd_exists_not_exists = (['dd.rest.stpl', 'dd.odt'], ['dd.odt'], ['dd.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'dd.rest', 'dd.odt'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd6/tmp1_stpl/doc/dd.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists7] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd7/tmp1_stpl'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.odt', 'rst_odt'], ['sr.odt'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.odt', 'rst_odt'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd7/tmp1_stpl/doc/sr.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists8] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd8/tmp1_stpl'
cmd_exists_not_exists = (['sr.rest.stpl', 'sr.odt', 'rst'], ['sr.odt'], ['sr.rest'])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'sr.rest', 'sr.odt', 'rst'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd8/tmp1_stpl/doc/sr.rest'
______________ test_dcx_out_file[rstinit5-cmd_exists_not_exists9] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd9/tmp1_stpl'
cmd_exists_not_exists = (['index.rest', 'build/index.html', 'sphinx_html'], ['build/index.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', 'index.rest', 'build/index.html', 'sphinx_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1900, in dorst
    with opn(infile) as f:
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 321, in opn
    return open(filename, encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd9/tmp1_stpl/doc/index.rest'
_____________ test_dcx_out_file[rstinit5-cmd_exists_not_exists22] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd22/tmp1_stpl'
cmd_exists_not_exists = (['.', 'build', 'html'], ['build/dd.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
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
>       assert os.path.exists(result[0])
E       AssertionError: assert False
E        +  where False = <function exists at 0x7f3285cde1f0>('build/dd.html')
E        +    where <function exists at 0x7f3285cde1f0> = <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'>.exists
E        +      where <module 'posixpath' from '/usr/lib/python3.8/posixpath.py'> = os.path

/home/roland/mine/rstdoc/test/test_dcx.py:597: AssertionError
----------------------------- Captured stderr call -----------------------------
_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_____________ test_dcx_out_file[rstinit5-cmd_exists_not_exists23] ______________

rstinit = '/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl'
cmd_exists_not_exists = (['.', 'build', 'sphinx_html'], ['build/index.html'], [])

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
        if  rstinit.endswith('ipdt') or rstinit.endswith('over'):
            return
        cmd,result,notexists = cmd_exists_not_exists
        tcmd = []
        tcmd.extend(cmd)
        os.chdir('doc')
        notrest = tcmd[0].replace('.stpl','')
        if not os.path.exists(tcmd[0]):
            tcmd[0] = notrest
            if len(tcmd)>1 and tcmd[1]==notrest:
                return
            notrest = None
        ncmd = [r'rstdcx']+tcmd
        r=run(ncmd)
>       assert r.returncode == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = CompletedProcess(args=['rstdcx', '.', 'build', 'sphinx_html'], returncode=1).returncode

/home/roland/mine/rstdoc/test/test_dcx.py:596: AssertionError
----------------------------- Captured stderr call -----------------------------
_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
Traceback (most recent call last):
  File "/home/roland/.local/bin/rstdcx", line 11, in <module>
    load_entry_point('rstdoc', 'console_scripts', 'rstdcx')()
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 6589, in main
    convert(i,o,outinfo)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 902, in infilecwder
    return f(inf, outfile, *args, **kwargs)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1158, in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 756, in cmd
    raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
rstdoc.dcx.RstDocError: Error code 2 returned from 
sphinx-build -b singlehtml . build -C -D project=sample -D author=sample Project Team -D copyright=2019, sample Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rst -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=_sometst.rest
in
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc

[stdout]
Running Sphinx v2.2.1
loading translations [None]... not available for built-in messages
building [mo]: targets for 0 po files that are out of date
building [singlehtml]: all documents
updating environment: [new config] 12 added, 0 changed, 0 removed
reading sources... [  8%] _links_docx
reading sources... [ 16%] _links_html
reading sources... [ 25%] _links_latex
reading sources... [ 33%] _links_odt
reading sources... [ 41%] _links_pdf
reading sources... [ 50%] _links_sphinx
reading sources... [ 58%] dd
reading sources... [ 66%] index
reading sources... [ 75%] ra
reading sources... [ 83%] sr
reading sources... [ 91%] sy
reading sources... [100%] tp


[stderr]
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:9: WARNING: Duplicate explicit target name: "".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:9: WARNING: Duplicate explicit target name: "".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:9: WARNING: Duplicate explicit target name: "".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:9: WARNING: Duplicate explicit target name: "".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:149: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:43: WARNING: Undefined substitution referenced: "dd_figure".
dd_included.rest:6: WARNING: Undefined substitution referenced: "dd_code".
dd_tables.rest:6: WARNING: Undefined substitution referenced: "dd_table".
dd_tables.rest:14: WARNING: Undefined substitution referenced: "eps1".
dd_tables.rest:19: WARNING: Undefined substitution referenced: "dd_list_table".
dd_tables.rest:32: WARNING: Undefined substitution referenced: "dd_table".
dd_tables.rest:32: WARNING: Undefined substitution referenced: "dd_list_table".
dd_included.rest:39: WARNING: Undefined substitution referenced: "hyp".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:67: WARNING: Undefined substitution referenced: "exampletikz1".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:72: WARNING: Undefined substitution referenced: "exampletikz1".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:82: WARNING: Undefined substitution referenced: "examplesvg".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:89: WARNING: Undefined substitution referenced: "exampledot".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:96: WARNING: Undefined substitution referenced: "exampleuml".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:104: WARNING: Undefined substitution referenced: "exampleplt".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:111: WARNING: Undefined substitution referenced: "examplepyx".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:118: WARNING: Undefined substitution referenced: "examplecairo".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:126: WARNING: Undefined substitution referenced: "examplepygal".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:133: WARNING: Undefined substitution referenced: "exampleother".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/dd.rst:140: WARNING: Undefined substitution referenced: "exampleeps".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/index.rst:23: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_traceability_file.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/index.rst:25: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/ra.rst:49: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/sr.rst:58: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/sr.rst:20: WARNING: Undefined substitution referenced: "tp_requirement_tests".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/sr.rst:36: WARNING: Undefined substitution referenced: "sr_style".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/sy.rst:19: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/tp.rst:49: WARNING: Problems with "include" directive path:
InputError: [Errno 2] No such file or directory: '_links_sphinx.rest'.
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/tp.rst:29: WARNING: Undefined substitution referenced: "sr_id".
/tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/tp.rst:33: WARNING: Undefined substitution referenced: "sr_a_requirement_group".

Sphinx error:
master file /tmp/pytest-of-roland/pytest-597/test_dcx_out_file_rstinit5_cmd23/tmp1_stpl/doc/_sometst.rest.rst not found

_______________________ test_waf_samples[docx-rstinit2] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt/build', 'docx')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279ac5030>('doc/')
E                +    where <built-in method find of str object at 0x7f3279ac5030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ docx/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.174s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egpyx.pyg
[10/19] Compiling pdt/001/egcairo.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egplt.pyg
[13/19] Compiling pdt/001/egother.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/p.rest
[18/19] Compiling pdt/000/t.rest
[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt/build'
'build' finished successfully (11.533s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit20/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[docx-rstinit3] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit30/tmp0_over/build', 'docx')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.docx not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3318dd0>('dd.docx')
E                +    where <built-in method find of str object at 0x5580e3318dd0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ docx/\n  ├ contribution.docx\n  ├ dev/\n  │ ├ hw/\n  │ ...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.docx'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit30/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit30/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.163s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit30/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling org/process/SOP/purchase.rest
[ 6/19] Compiling dev/issues/issue2.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling org/discussion/topic1.rest
[15/19] Compiling pdt/000/info.rest
[16/19] Compiling readme.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit30/tmp0_over/build'
'build' finished successfully (3.663s)
_______________________ test_waf_samples[docx-rstinit6] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt/build', 'docx')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279ae94f0>('doc/')
E                +    where <built-in method find of str object at 0x7f3279ae94f0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ docx/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.151s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egother.pyg
[11/19] Compiling pdt/001/egplt.pyg
[12/19] Compiling pdt/001/egpyx.pyg
[13/19] Compiling pdt/000/repo.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt/build'
'build' finished successfully (11.997s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit60/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[docx-rstinit7] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit70/tmp1_over/build', 'docx')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.docx not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3319040>('dd.docx')
E                +    where <built-in method find of str object at 0x5580e3319040> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ docx/\n  ├ contribution.docx\n  ├ dev/\n  │ ├ hw/\n  │ ...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.docx'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit70/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit70/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.172s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit70/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling org/process/SOP/purchase.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling dev/hw/casing/plan.rst
[ 8/19] Compiling org/discussion/topic1.rst
[ 9/19] Compiling doc/tutorial.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling readme.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling org/contributor/c1/assigned.rst
[17/19] Compiling dev/sw/fw/plan.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_docx_rstinit70/tmp1_over/build'
'build' finished successfully (3.676s)
________________________ test_waf_samples[odt-rstinit2] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt/build', 'odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279ac5ae0>('doc/')
E                +    where <built-in method find of str object at 0x7f3279ac5ae0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ odt/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.160s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpyx.pyg
[ 9/19] Compiling pdt/001/egother.pyg
[10/19] Compiling pdt/001/egplt.pyg
[11/19] Compiling pdt/001/egcairo.pyg
[12/19] Compiling pdt/000/repo.pyg
[13/19] Compiling pdt/001/egpygal.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/t.rest
[18/19] Compiling pdt/000/p.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt/build'
'build' finished successfully (12.059s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit2_0/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
________________________ test_waf_samples[odt-rstinit3] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit3_0/tmp0_over/build', 'odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.odt not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3318dd0>('dd.odt')
E                +    where <built-in method find of str object at 0x5580e3318dd0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ odt/\n  ├ contribution.odt\n  ├ dev/\n  │ ├ hw/\n  │ ├ ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.odt'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit3_0/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit3_0/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.164s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit3_0/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/issues/issue2.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling dev/hw/casing/plan.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling doc/tutorial.rest
[14/19] Compiling readme.rest
[15/19] Compiling org/process/SOP/purchase.rest
[16/19] Compiling org/contributor/c1/log/2019.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit3_0/tmp0_over/build'
'build' finished successfully (2.968s)
________________________ test_waf_samples[odt-rstinit6] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt/build', 'odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279bb7e70>('doc/')
E                +    where <built-in method find of str object at 0x7f3279bb7e70> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ odt/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.171s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egplt.pyg
[ 9/19] Compiling pdt/000/repo.pyg
[10/19] Compiling pdt/001/egpygal.pyg
[11/19] Compiling pdt/001/egpyx.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egcairo.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt/build'
'build' finished successfully (11.068s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit6_0/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
________________________ test_waf_samples[odt-rstinit7] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit7_0/tmp1_over/build', 'odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.odt not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39f9290>('dd.odt')
E                +    where <built-in method find of str object at 0x5580e39f9290> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ odt/\n  ├ contribution.odt\n  ├ dev/\n  │ ├ hw/\n  │ ├ ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.odt'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit7_0/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit7_0/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.155s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit7_0/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling dev/sw/fw/plan.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling org/discussion/topic1.rst
[ 8/19] Compiling org/contributor/c1/assigned.rst
[ 9/19] Compiling dev/hw/casing/plan.rst
[10/19] Compiling doc/tutorial.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/mediation/conflict1.rst
[14/19] Compiling org/contributor/c1/log/2019.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling readme.rst
[17/19] Compiling org/process/SOP/purchase.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_odt_rstinit7_0/tmp1_over/build'
'build' finished successfully (2.970s)
________________________ test_waf_samples[pdf-rstinit2] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt/build', 'pdf')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f327999ee70>('doc/')
E                +    where <built-in method find of str object at 0x7f327999ee70> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ pdf/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.164s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egother.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egpyx.pyg
[13/19] Compiling pdt/001/egplt.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/t.rest
[18/19] Compiling pdt/000/p.rest
[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt/build'
'build' finished successfully (55.604s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit2_0/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
________________________ test_waf_samples[pdf-rstinit3] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit3_0/tmp0_over/build', 'pdf')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.pdf not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a285c0>('dd.pdf')
E                +    where <built-in method find of str object at 0x5580e3a285c0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ pdf/\n  ├ contribution.pdf\n  ├ dev/\n  │ ├ hw/\n  │ ├ ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.pdf'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit3_0/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit3_0/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.178s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit3_0/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue2.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling readme.rest
[15/19] Compiling org/process/SOP/purchase.rest
[16/19] Compiling dev/issues/issue1.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit3_0/tmp0_over/build'
'build' finished successfully (2m51.776s)
________________________ test_waf_samples[pdf-rstinit6] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt/build', 'pdf')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f32798ad290>('doc/')
E                +    where <built-in method find of str object at 0x7f32798ad290> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ pdf/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.160s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz1.tikz
[ 4/19] Compiling pdt/001/egtikz.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/000/repo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/001/egcairo.pyg
[12/19] Compiling pdt/001/egplt.pyg
[13/19] Compiling pdt/001/egother.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/001/i.rst
[16/19] Compiling pdt/000/d.rst
[17/19] Compiling pdt/000/p.rst
[18/19] Compiling pdt/000/i.rst
[19/19] Compiling pdt/000/t.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt/build'
'build' finished successfully (55.759s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit6_0/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
________________________ test_waf_samples[pdf-rstinit7] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit7_0/tmp1_over/build', 'pdf')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.pdf not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39e2220>('dd.pdf')
E                +    where <built-in method find of str object at 0x5580e39e2220> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ pdf/\n  ├ contribution.pdf\n  ├ dev/\n  │ ├ hw/\n  │ ├ ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.pdf'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit7_0/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit7_0/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.145s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit7_0/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling dev/sw/fw/plan.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling dev/hw/casing/plan.rst
[ 8/19] Compiling org/contributor/c1/assigned.rst
[ 9/19] Compiling doc/tutorial.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling org/discussion/topic1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling readme.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling dev/issues/issue1.rst
[17/19] Compiling org/process/SOP/purchase.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_pdf_rstinit7_0/tmp1_over/build'
'build' finished successfully (2m51.821s)
_______________________ test_waf_samples[html-rstinit2] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt/build', 'html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f32798ab620>('doc/')
E                +    where <built-in method find of str object at 0x7f32798ab620> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ html/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.159s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egplt.pyg
[ 9/19] Compiling pdt/001/egother.pyg
[10/19] Compiling pdt/001/egpygal.pyg
[11/19] Compiling pdt/001/egpyx.pyg
[12/19] Compiling pdt/000/repo.pyg
[13/19] Compiling pdt/001/egcairo.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/000/t.rest
[16/19] Compiling pdt/000/d.rest
[17/19] Compiling pdt/000/p.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[18/19] Compiling pdt/000/i.rest
[19/19] Compiling pdt/001/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt/build'
'build' finished successfully (11.689s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit20/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[html-rstinit3] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit30/tmp0_over/build', 'html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a23ae0>('_images')
E                +    where <built-in method find of str object at 0x5580e3a23ae0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ html/\n  ├ contribution.html\n  ├ dev/\n  │ ├ hw/\n  │ ...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.html'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit30/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit30/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.161s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit30/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling contribution.rest
[ 4/19] Compiling org/process/SOP/purchase.rest
[ 5/19] Compiling org/discussion/topic1.rest
[ 6/19] Compiling dev/issues/issue2.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling pdt/000/info.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling dev/issues/issue1.rest
[15/19] Compiling dev/sw/fw/plan.rest
[16/19] Compiling readme.rest
[17/19] Compiling pdt/000/test.rest
[18/19] Compiling dev/hw/casing/test/stability.rest
[19/19] Compiling dev/hw/pcb1/plan.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit30/tmp0_over/build'
'build' finished successfully (2.718s)
_______________________ test_waf_samples[html-rstinit6] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt/build', 'html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f32798a49b0>('doc/')
E                +    where <built-in method find of str object at 0x7f32798a49b0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ html/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.160s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egpyx.pyg
[10/19] Compiling pdt/001/egother.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egplt.pyg
[13/19] Compiling pdt/001/egcairo.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/p.rst
[18/19] Compiling pdt/000/t.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt/build'
'build' finished successfully (11.707s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit60/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[html-rstinit7] ________________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit70/tmp1_over/build', 'html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a299e0>('_images')
E                +    where <built-in method find of str object at 0x5580e3a299e0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ html/\n  ├ contribution.html\n  ├ dev/\n  │ ├ hw/\n  │ ...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.html'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit70/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit70/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.149s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit70/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling dev/sw/fw/plan.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling org/discussion/topic1.rst
[ 8/19] Compiling dev/hw/casing/plan.rst
[ 9/19] Compiling org/contributor/c1/assigned.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling readme.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling doc/tutorial.rst
[17/19] Compiling org/process/SOP/purchase.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_html_rstinit70/tmp1_over/build'
'build' finished successfully (2.711s)
_______________________ test_waf_samples[latex-rstinit2] _______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt/build', 'latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f32798ad3c0>('doc/')
E                +    where <built-in method find of str object at 0x7f32798ad3c0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ latex/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.164s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpyx.pyg
[ 9/19] Compiling pdt/001/egother.pyg
[10/19] Compiling pdt/001/egplt.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egcairo.pyg
[13/19] Compiling pdt/001/egpygal.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/001/i.rest
[16/19] Compiling pdt/000/t.rest
[17/19] Compiling pdt/000/p.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[18/19] Compiling pdt/000/i.rest
[19/19] Compiling pdt/000/d.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt/build'
'build' finished successfully (11.782s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[latex-rstinit3] _______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit3/tmp0_over/build', 'latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a5b100>('_images')
E                +    where <built-in method find of str object at 0x5580e3a5b100> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ latex/\n  ├ contribution.latex\n  ├ dev/\n  │ ├ hw/\n  ... org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.latex'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.162s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit3/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling contribution.rest
[ 4/19] Compiling org/process/SOP/purchase.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/issues/issue2.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling readme.rest
[15/19] Compiling dev/sw/fw/plan.rest
[16/19] Compiling dev/hw/casing/plan.rest
[17/19] Compiling pdt/000/test.rest
[18/19] Compiling dev/hw/casing/test/stability.rest
[19/19] Compiling dev/hw/pcb1/plan.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit3/tmp0_over/build'
'build' finished successfully (2.900s)
_______________________ test_waf_samples[latex-rstinit6] _______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt/build', 'latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f32799be030>('doc/')
E                +    where <built-in method find of str object at 0x7f32799be030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ latex/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.172s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz1.tikz
[ 4/19] Compiling pdt/001/egtikz.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egplt.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt/build'
'build' finished successfully (11.823s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_______________________ test_waf_samples[latex-rstinit7] _______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit7/tmp1_over/build', 'latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39efd70>('_images')
E                +    where <built-in method find of str object at 0x5580e39efd70> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ latex/\n  ├ contribution.latex\n  ├ dev/\n  │ ├ hw/\n  ... org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.latex'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.159s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit7/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling contribution.rst
[ 5/19] Compiling pdt/000/test.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling org/discussion/topic1.rst
[ 8/19] Compiling org/contributor/c1/assigned.rst
[ 9/19] Compiling dev/hw/casing/plan.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling doc/tutorial.rst
[14/19] Compiling readme.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling org/contributor/c1/log/2019.rst
[17/19] Compiling org/process/SOP/purchase.rst
[18/19] Compiling dev/hw/pcb1/plan.rst
[19/19] Compiling dev/sw/fw/plan.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_latex_rstinit7/tmp1_over/build'
'build' finished successfully (2.915s)
____________________ test_waf_samples[sphinx_html-rstinit0] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39ed0e0>('build/')
E                +    where <built-in method find of str object at 0x5580e39ed0e0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_html/\n│ └ doc/\n│   ├ _images/\n│   ├ _sources/...nv\n│   ├ ra.html\n│   ├ search.html\n│   ├ searchindex.js\n│   ├ sr.html\n│   └ tp.html\n└ tmp0_rest/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.170s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest/build'
[ 1/14] Compiling tmp0_rest/some.h
[ 2/14] Compiling tmp0_rest/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egpyx.pyg
[ 9/14] Compiling doc/egplt.pyg
[10/14] Compiling doc/egpygal.pyg
[11/14] Compiling doc/egcairo.pyg
[12/14] Compiling doc/egother.pyg
[13/14] Compiling doc/egeps.eps
[14/14] Compiling doc/index.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest/build'
'build' finished successfully (13.962s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r0/tmp0_rest/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
____________________ test_waf_samples[sphinx_html-rstinit1] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e392a0b0>('build/')
E                +    where <built-in method find of str object at 0x5580e392a0b0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_html/\n│ └ doc/\n│   ├ _images/\n│   ├ _sources/...ml\n│   ├ search.html\n│   ├ searchindex.js\n│   ├ sr.html\n│   ├ sy.html\n│   └ tp.html\n└ tmp0_stpl/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.159s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl/build'
[ 1/14] Compiling tmp0_stpl/some.h
[ 2/14] Compiling tmp0_stpl/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egplt.pyg
[ 9/14] Compiling doc/egpygal.pyg
[10/14] Compiling doc/egother.pyg
[11/14] Compiling doc/egcairo.pyg
[12/14] Compiling doc/egpyx.pyg
[13/14] Compiling doc/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

[14/14] Compiling doc/index.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl/build'
'build' finished successfully (14.776s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r1/tmp0_stpl/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
____________________ test_waf_samples[sphinx_html-rstinit2] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a3bfb0>('doc/')
E                +    where <built-in method find of str object at 0x5580e3a3bfb0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_html/\n  └ pdt/\n    ├ 000...aceability_file.svg\n    ├ genindex.html\n    ├ index.html\n    ├ objects.inv\n    ├ search.html\n    └ searchindex.js'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.171s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt/build'
[ 1/15] Compiling c/some.h
[ 2/15] Compiling c/some.h
[ 3/15] Compiling pdt/001/egtikz.tikz
[ 4/15] Compiling pdt/001/egtikz1.tikz
[ 5/15] Compiling pdt/001/egsvg.svg
[ 6/15] Compiling pdt/001/egdot.dot
[ 7/15] Compiling pdt/001/eguml.uml
[ 8/15] Compiling pdt/001/egplt.pyg
[ 9/15] Compiling pdt/001/egcairo.pyg
[10/15] Compiling pdt/001/egpygal.pyg
[11/15] Compiling pdt/001/egother.pyg
[12/15] Compiling pdt/001/egpyx.pyg
[13/15] Compiling pdt/000/repo.pyg
[14/15] Compiling pdt/001/egeps.eps
[15/15] Compiling pdt/index.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt/build'
'build' finished successfully (14.593s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
____________________ test_waf_samples[sphinx_html-rstinit3] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r3/tmp0_over/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a1ecb0>('_images/')
E                +    where <built-in method find of str object at 0x5580e3a1ecb0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_html/\n  ├ _sources/\n  │ ├ contribution.rest.tx...cussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  ├ readme.html\n  ├ search.html\n  └ searchindex.js'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.178s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r3/tmp0_over/build'
[1/2] Compiling index.rest
[2/2] Compiling doc/index.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r3/tmp0_over/build'
'build' finished successfully (7.174s)
____________________ test_waf_samples[sphinx_html-rstinit4] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a84ef0>('build/')
E                +    where <built-in method find of str object at 0x5580e3a84ef0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_html/\n│ └ doc/\n│   ├ _images/\n│   ├ _sources/...nv\n│   ├ ra.html\n│   ├ search.html\n│   ├ searchindex.js\n│   ├ sr.html\n│   └ tp.html\n└ tmp1_rest/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.171s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest/build'
[ 1/14] Compiling tmp1_rest/some.h
[ 2/14] Compiling tmp1_rest/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egcairo.pyg
[ 9/14] Compiling doc/egpyx.pyg
[10/14] Compiling doc/egplt.pyg
[11/14] Compiling doc/egother.pyg
[12/14] Compiling doc/egpygal.pyg
[13/14] Compiling doc/egeps.eps
[14/14] Compiling doc/index.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest/build'
'build' finished successfully (13.950s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r4/tmp1_rest/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
____________________ test_waf_samples[sphinx_html-rstinit5] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a0e8e0>('build/')
E                +    where <built-in method find of str object at 0x5580e3a0e8e0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_html/\n│ └ doc/\n│   ├ _images/\n│   ├ _sources/...ml\n│   ├ search.html\n│   ├ searchindex.js\n│   ├ sr.html\n│   ├ sy.html\n│   └ tp.html\n└ tmp1_stpl/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.161s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl/build'
[ 1/14] Compiling tmp1_stpl/some.h
[ 2/14] Compiling tmp1_stpl/some.h
[ 3/14] Compiling doc/egtikz1.tikz
[ 4/14] Compiling doc/egtikz.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egcairo.pyg
[ 9/14] Compiling doc/egother.pyg
[10/14] Compiling doc/egpyx.pyg
[11/14] Compiling doc/egpygal.pyg
[12/14] Compiling doc/egplt.pyg
[13/14] Compiling doc/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

[14/14] Compiling doc/index.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl/build'
'build' finished successfully (15.560s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r5/tmp1_stpl/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
____________________ test_waf_samples[sphinx_html-rstinit6] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt/build', 'sphinx_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a20030>('doc/')
E                +    where <built-in method find of str object at 0x5580e3a20030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_html/\n  └ pdt/\n    ├ 000...aceability_file.svg\n    ├ genindex.html\n    ├ index.html\n    ├ objects.inv\n    ├ search.html\n    └ searchindex.js'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.171s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt/build'
[ 1/15] Compiling c/some.h
[ 2/15] Compiling c/some.h
[ 3/15] Compiling pdt/001/egtikz.tikz
[ 4/15] Compiling pdt/001/egtikz1.tikz
[ 5/15] Compiling pdt/001/egsvg.svg
[ 6/15] Compiling pdt/001/egdot.dot
[ 7/15] Compiling pdt/001/eguml.uml
[ 8/15] Compiling pdt/001/egpygal.pyg
[ 9/15] Compiling pdt/001/egplt.pyg
[10/15] Compiling pdt/001/egpyx.pyg
[11/15] Compiling pdt/001/egother.pyg
[12/15] Compiling pdt/001/egcairo.pyg
[13/15] Compiling pdt/000/repo.pyg
[14/15] Compiling pdt/001/egeps.eps
[15/15] Compiling pdt/index.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt/build'
'build' finished successfully (14.610s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_html_r6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit0] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a4c2f0>('build/')
E                +    where <built-in method find of str object at 0x5580e3a4c2f0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_latex/\n│ └ doc/\n│   ├ LICRcyr2utf8.xdy\n│   ├ ...nxhowto.cls\n│   ├ sphinxmanual.cls\n│   ├ sphinxmessages.sty\n│   └ sphinxmulticell.sty\n└ tmp0_rest/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.151s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest/build'
[ 1/14] Compiling tmp0_rest/some.h
[ 2/14] Compiling tmp0_rest/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egcairo.pyg
[ 9/14] Compiling doc/egother.pyg
[10/14] Compiling doc/egpyx.pyg
[11/14] Compiling doc/egplt.pyg
[12/14] Compiling doc/egpygal.pyg
[13/14] Compiling doc/egeps.eps
[14/14] Compiling doc/index.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest/build'
'build' finished successfully (13.570s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_0/tmp0_rest/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit1] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a90c80>('build/')
E                +    where <built-in method find of str object at 0x5580e3a90c80> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_latex/\n│ └ doc/\n│   ├ LICRcyr2utf8.xdy\n│   ├ ...nxhowto.cls\n│   ├ sphinxmanual.cls\n│   ├ sphinxmessages.sty\n│   └ sphinxmulticell.sty\n└ tmp0_stpl/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.167s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl/build'
[ 1/14] Compiling tmp0_stpl/some.h
[ 2/14] Compiling tmp0_stpl/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egpyx.pyg
[ 9/14] Compiling doc/egother.pyg
[10/14] Compiling doc/egplt.pyg
[11/14] Compiling doc/egpygal.pyg
[12/14] Compiling doc/egcairo.pyg
[13/14] Compiling doc/egeps.eps
[14/14] Compiling doc/index.rest
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl/build'
'build' finished successfully (15.673s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_1/tmp0_stpl/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit2] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39ed0e0>('doc/')
E                +    where <built-in method find of str object at 0x5580e39ed0e0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_latex/\n  └ pdt/\n    ├ LI...phinxhighlight.sty\n    ├ sphinxhowto.cls\n    ├ sphinxmanual.cls\n    ├ sphinxmessages.sty\n    └ sphinxmulticell.sty'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.169s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt/build'
[ 1/15] Compiling c/some.h
[ 2/15] Compiling c/some.h
[ 3/15] Compiling pdt/001/egtikz.tikz
[ 4/15] Compiling pdt/001/egtikz1.tikz
[ 5/15] Compiling pdt/001/egsvg.svg
[ 6/15] Compiling pdt/001/egdot.dot
[ 7/15] Compiling pdt/001/eguml.uml
[ 8/15] Compiling pdt/001/egpygal.pyg
[ 9/15] Compiling pdt/001/egplt.pyg
[10/15] Compiling pdt/000/repo.pyg
[11/15] Compiling pdt/001/egcairo.pyg
[12/15] Compiling pdt/001/egpyx.pyg
[13/15] Compiling pdt/001/egother.pyg
[14/15] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/15] Compiling pdt/index.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt/build'
'build' finished successfully (12.574s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit3] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_3/tmp0_over/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _traceability_file.png not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a5fab0>('_traceability_file.png')
E                +    where <built-in method find of str object at 0x5580e3a5fab0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_latex/\n  ├ LICRcyr2utf8.xdy\n  ├ LICRlatin2utf8...y\n  ├ sphinxhighlight.sty\n  ├ sphinxhowto.cls\n  ├ sphinxmanual.cls\n  ├ sphinxmessages.sty\n  └ sphinxmulticell.sty'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.177s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_3/tmp0_over/build'
[1/2] Compiling index.rest
[2/2] Compiling doc/index.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_3/tmp0_over/build'
'build' finished successfully (5.674s)
___________________ test_waf_samples[sphinx_latex-rstinit4] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3155060>('build/')
E                +    where <built-in method find of str object at 0x5580e3155060> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_latex/\n│ └ doc/\n│   ├ LICRcyr2utf8.xdy\n│   ├ ...nxhowto.cls\n│   ├ sphinxmanual.cls\n│   ├ sphinxmessages.sty\n│   └ sphinxmulticell.sty\n└ tmp1_rest/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.147s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest/build'
[ 1/14] Compiling tmp1_rest/some.h
[ 2/14] Compiling tmp1_rest/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egcairo.pyg
[ 9/14] Compiling doc/egother.pyg
[10/14] Compiling doc/egpyx.pyg
[11/14] Compiling doc/egplt.pyg
[12/14] Compiling doc/egpygal.pyg
[13/14] Compiling doc/egeps.eps
[14/14] Compiling doc/index.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest/build'
'build' finished successfully (13.499s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_4/tmp1_rest/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit5] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: build/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a60520>('build/')
E                +    where <built-in method find of str object at 0x5580e3a60520> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n├ sphinx_latex/\n│ └ doc/\n│   ├ LICRcyr2utf8.xdy\n│   ├ ...nxhowto.cls\n│   ├ sphinxmanual.cls\n│   ├ sphinxmessages.sty\n│   └ sphinxmulticell.sty\n└ tmp1_stpl/\n  └ some_tst.c'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.159s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl/build'
[ 1/14] Compiling tmp1_stpl/some.h
[ 2/14] Compiling tmp1_stpl/some.h
[ 3/14] Compiling doc/egtikz.tikz
[ 4/14] Compiling doc/egtikz1.tikz
[ 5/14] Compiling doc/egsvg.svg
[ 6/14] Compiling doc/egdot.dot
[ 7/14] Compiling doc/eguml.uml
[ 8/14] Compiling doc/egplt.pyg
[ 9/14] Compiling doc/egpygal.pyg
[10/14] Compiling doc/egother.pyg
[11/14] Compiling doc/egcairo.pyg
[12/14] Compiling doc/egpyx.pyg
[13/14] Compiling doc/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../doc/_images/egeps.png

[14/14] Compiling doc/index.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl/build'
'build' finished successfully (14.402s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_5/tmp1_stpl/doc/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
___________________ test_waf_samples[sphinx_latex-rstinit6] ____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt/build', 'sphinx_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a8fc20>('doc/')
E                +    where <built-in method find of str object at 0x5580e3a8fc20> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ sphinx_latex/\n  └ pdt/\n    ├ LI...phinxhighlight.sty\n    ├ sphinxhowto.cls\n    ├ sphinxmanual.cls\n    ├ sphinxmessages.sty\n    └ sphinxmulticell.sty'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.168s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt/build'
[ 1/15] Compiling c/some.h
[ 2/15] Compiling c/some.h
[ 3/15] Compiling pdt/001/egtikz.tikz
[ 4/15] Compiling pdt/001/egtikz1.tikz
[ 5/15] Compiling pdt/001/egsvg.svg
[ 6/15] Compiling pdt/001/egdot.dot
[ 7/15] Compiling pdt/001/eguml.uml
[ 8/15] Compiling pdt/001/egplt.pyg
[ 9/15] Compiling pdt/001/egcairo.pyg
[10/15] Compiling pdt/000/repo.pyg
[11/15] Compiling pdt/001/egother.pyg
[12/15] Compiling pdt/001/egpygal.pyg
[13/15] Compiling pdt/001/egpyx.pyg
[14/15] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/15] Compiling pdt/index.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt/build'
'build' finished successfully (12.782s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_sphinx_latex_6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
_____________________ test_waf_samples[rst_html-rstinit2] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt/build', 'rst_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279e81030>('doc/')
E                +    where <built-in method find of str object at 0x7f3279e81030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_html/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.157s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egplt.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/t.rest
[18/19] Compiling pdt/000/p.rest
[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt/build'
'build' finished successfully (11.956s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rst:13: (ERROR/3) Undefined substitution referenced: "eps1".
_____________________ test_waf_samples[rst_html-rstinit3] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti3/tmp0_over/build', 'rst_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3895460>('_images')
E                +    where <built-in method find of str object at 0x5580e3895460> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_html/\n  ├ contribution.html\n  ├ dev/\n  │ ├ hw/\n...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.html'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.163s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti3/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling dev/issues/issue2.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling readme.rest
[15/19] Compiling org/process/SOP/purchase.rest
[16/19] Compiling org/mediation/conflict1.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti3/tmp0_over/build'
'build' finished successfully (1.637s)
_____________________ test_waf_samples[rst_html-rstinit6] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt/build', 'rst_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279a12030>('doc/')
E                +    where <built-in method find of str object at 0x7f3279a12030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_html/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.146s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egplt.pyg
[ 9/19] Compiling pdt/000/repo.pyg
[10/19] Compiling pdt/001/egpygal.pyg
[11/19] Compiling pdt/001/egpyx.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egcairo.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt/build'
'build' finished successfully (11.720s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rest:13: (ERROR/3) Undefined substitution referenced: "eps1".
_____________________ test_waf_samples[rst_html-rstinit7] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti7/tmp1_over/build', 'rst_html')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a83f60>('_images')
E                +    where <built-in method find of str object at 0x5580e3a83f60> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_html/\n  ├ contribution.html\n  ├ dev/\n  │ ├ hw/\n...├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.html'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.170s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti7/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling pdt/000/info.rst
[ 6/19] Compiling org/discussion/topic1.rst
[ 7/19] Compiling dev/hw/casing/plan.rst
[ 8/19] Compiling dev/issues/issue2.rst
[ 9/19] Compiling org/contributor/c1/assigned.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling doc/tutorial.rst
[15/19] Compiling org/process/SOP/purchase.rst
[16/19] Compiling readme.rst
[17/19] Compiling dev/sw/fw/plan.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_html_rsti7/tmp1_over/build'
'build' finished successfully (1.637s)
_____________________ test_waf_samples[rst_latex-rstinit2] _____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt/build', 'rst_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f327b045670>('doc/')
E                +    where <built-in method find of str object at 0x7f327b045670> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_latex/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.166s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egplt.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/t.rest
[18/19] Compiling pdt/000/p.rest
[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt/build'
'build' finished successfully (11.862s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rst:13: (ERROR/3) Undefined substitution referenced: "eps1".
_____________________ test_waf_samples[rst_latex-rstinit3] _____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst3/tmp0_over/build', 'rst_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3136f80>('_images')
E                +    where <built-in method find of str object at 0x5580e3136f80> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_latex/\n  ├ contribution.latex\n  ├ dev/\n  │ ├ hw/... org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.latex'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.178s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst3/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling readme.rest
[15/19] Compiling org/process/SOP/purchase.rest
[16/19] Compiling dev/issues/issue2.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst3/tmp0_over/build'
'build' finished successfully (1.637s)
_____________________ test_waf_samples[rst_latex-rstinit6] _____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt/build', 'rst_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279e81030>('doc/')
E                +    where <built-in method find of str object at 0x7f3279e81030> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_latex/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.160s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/001/egcairo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/000/repo.pyg
[12/19] Compiling pdt/001/egplt.pyg
[13/19] Compiling pdt/001/egother.pyg
[14/19] Compiling pdt/001/egeps.eps
[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt/build'
'build' finished successfully (11.854s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rest:13: (ERROR/3) Undefined substitution referenced: "eps1".
_____________________ test_waf_samples[rst_latex-rstinit7] _____________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst7/tmp1_over/build', 'rst_latex')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: _images not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e39fb690>('_images')
E                +    where <built-in method find of str object at 0x5580e39fb690> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_latex/\n  ├ contribution.latex\n  ├ dev/\n  │ ├ hw/... org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.latex'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.168s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst7/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling dev/hw/pcb1/plan.rst
[ 5/19] Compiling pdt/000/info.rst
[ 6/19] Compiling org/discussion/topic1.rst
[ 7/19] Compiling dev/hw/casing/plan.rst
[ 8/19] Compiling dev/issues/issue2.rst
[ 9/19] Compiling doc/tutorial.rst
[10/19] Compiling org/contributor/c1/assigned.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling readme.rst
[15/19] Compiling org/process/SOP/purchase.rst
[16/19] Compiling org/mediation/conflict1.rst
[17/19] Compiling dev/sw/fw/plan.rst
[18/19] Compiling contribution.rst
[19/19] Compiling pdt/000/test.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_latex_rst7/tmp1_over/build'
'build' finished successfully (1.631s)
______________________ test_waf_samples[rst_odt-rstinit2] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt/build', 'rst_odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279a2f170>('doc/')
E                +    where <built-in method find of str object at 0x7f3279a2f170> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_odt/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.162s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egplt.pyg
[ 9/19] Compiling pdt/000/repo.pyg
[10/19] Compiling pdt/001/egpygal.pyg
[11/19] Compiling pdt/001/egpyx.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egcairo.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rest
[16/19] Compiling pdt/001/i.rest
[17/19] Compiling pdt/000/t.rest
[18/19] Compiling pdt/000/p.rest
[19/19] Compiling pdt/000/i.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt/build'
'build' finished successfully (12.394s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin2/tmp0_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rst:13: (ERROR/3) Undefined substitution referenced: "eps1".
______________________ test_waf_samples[rst_odt-rstinit3] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin3/tmp0_over/build', 'rst_odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.odt not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3319040>('dd.odt')
E                +    where <built-in method find of str object at 0x5580e3319040> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_odt/\n  ├ contribution.odt\n  ├ dev/\n  │ ├ hw/\n  ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.odt'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin3/tmp0_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin3/tmp0_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.166s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin3/tmp0_over/build'
[ 1/19] Compiling pdt/000/do.rest
[ 2/19] Compiling dev/sw/android/plan.rest
[ 3/19] Compiling dev/hw/casing/test/stability.rest
[ 4/19] Compiling dev/hw/pcb1/plan.rest
[ 5/19] Compiling pdt/000/info.rest
[ 6/19] Compiling org/discussion/topic1.rest
[ 7/19] Compiling dev/hw/casing/plan.rest
[ 8/19] Compiling org/contributor/c1/assigned.rest
[ 9/19] Compiling doc/tutorial.rest
[10/19] Compiling org/mediation/conflict1.rest
[11/19] Compiling pdt/000/plan.rest
[12/19] Compiling dev/issues/issue1.rest
[13/19] Compiling org/contributor/c1/log/2019.rest
[14/19] Compiling readme.rest
[15/19] Compiling org/process/SOP/purchase.rest
[16/19] Compiling dev/issues/issue2.rest
[17/19] Compiling dev/sw/fw/plan.rest
[18/19] Compiling contribution.rest
[19/19] Compiling pdt/000/test.rest
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin3/tmp0_over/build'
'build' finished successfully (3.850s)
______________________ test_waf_samples[rst_odt-rstinit6] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt/build', 'rst_odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: doc/ not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x7f3279a2f2b0>('doc/')
E                +    where <built-in method find of str object at 0x7f3279a2f2b0> = '├ c/\n│ └ some_tst.c\n├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_odt/\n  └ pdt/\n    ├ 000/\n    └ 001/'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.172s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt/build'
[ 1/19] Compiling c/some.h
[ 2/19] Compiling c/some.h
[ 3/19] Compiling pdt/001/egtikz.tikz
[ 4/19] Compiling pdt/001/egtikz1.tikz
[ 5/19] Compiling pdt/001/egsvg.svg
[ 6/19] Compiling pdt/001/egdot.dot
[ 7/19] Compiling pdt/001/eguml.uml
[ 8/19] Compiling pdt/001/egpygal.pyg
[ 9/19] Compiling pdt/000/repo.pyg
[10/19] Compiling pdt/001/egpyx.pyg
[11/19] Compiling pdt/001/egcairo.pyg
[12/19] Compiling pdt/001/egother.pyg
[13/19] Compiling pdt/001/egplt.pyg
[14/19] Compiling pdt/001/egeps.eps
DPI: 600
Background RRGGBBAA: ffffff00
Area 7.33333:2:56.6667:75.3333 exported to 308 x 458 pixels (600 dpi)
Bitmap saved as: ../pdt/001/_images/egeps.png

[15/19] Compiling pdt/000/d.rst
[16/19] Compiling pdt/001/i.rst
[17/19] Compiling pdt/000/t.rst
[18/19] Compiling pdt/000/p.rst
[19/19] Compiling pdt/000/i.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt/build'
'build' finished successfully (12.448s)
---------------------------- Captured stderr setup -----------------------------
/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin6/tmp1_ipdt/pdt/001/_images/egplt.png:8: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
i_tables.rest:13: (ERROR/3) Undefined substitution referenced: "eps1".
______________________ test_waf_samples[rst_odt-rstinit7] ______________________

wafbuild = ('/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin7/tmp1_over/build', 'rst_odt')

    def test_waf_samples(wafbuild):
        '''
        Tests running Waf on the sample projects.
    
        '''
        rstinit,target = wafbuild
        try:
            _,ext = target.split('_')
        except: ext = target
        if ext.endswith('latex') or ext.endswith('html'):
            extra = '\n│     ├ _images'
            if ext.endswith('html'):
                extra += '\n│     ├ _traceability_file.svg'
        else:
            extra = ''
        if  rstinit.endswith('over'):
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
            realout = tree3(rstinit)
            for x in expected.splitlines():
                xchk=x.strip('└│├ ')
                assert realout.find(xchk)>=0, "%s not found"%xchk
        elif  rstinit.endswith('ipdt'):
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
            is_stpl = rstinit.endswith('stpl')
            tmpx_xxx = base(rstinit)
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
>               assert realout.find(xchk)>=0, "%s not found"%xchk
E               AssertionError: dd.odt not found
E               assert -1 >= 0
E                +  where -1 = <built-in method find of str object at 0x5580e3a277b0>('dd.odt')
E                +    where <built-in method find of str object at 0x5580e3a277b0> = '├ c4che/\n│ ├ _cache.py\n│ └ build.config.py\n├ config.log\n└ rst_odt/\n  ├ contribution.odt\n  ├ dev/\n  │ ├ hw/\n  ... ├ org/\n  │ ├ contributor/\n  │ ├ discussion/\n  │ ├ mediation/\n  │ └ process/\n  ├ pdt/\n  │ └ 000/\n  └ readme.odt'.find

/home/roland/mine/rstdoc/test/test_dcx.py:898: AssertionError
---------------------------- Captured stdout setup -----------------------------
Setting top to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin7/tmp1_over 
Setting out to                           : /tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin7/tmp1_over/build 
Checking for program 'plantuml'          : /usr/bin/plantuml 
Checking for program 'dot'               : /usr/bin/dot 
Checking for program 'inkscape'          : /usr/bin/inkscape 
'configure' finished successfully (0.165s)
Waf: Entering directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin7/tmp1_over/build'
[ 1/19] Compiling pdt/000/do.rst
[ 2/19] Compiling dev/sw/android/plan.rst
[ 3/19] Compiling dev/hw/casing/test/stability.rst
[ 4/19] Compiling contribution.rst
[ 5/19] Compiling pdt/000/test.rst
[ 6/19] Compiling dev/issues/issue2.rst
[ 7/19] Compiling org/discussion/topic1.rst
[ 8/19] Compiling org/contributor/c1/assigned.rst
[ 9/19] Compiling doc/tutorial.rst
[10/19] Compiling org/mediation/conflict1.rst
[11/19] Compiling pdt/000/plan.rst
[12/19] Compiling dev/issues/issue1.rst
[13/19] Compiling org/contributor/c1/log/2019.rst
[14/19] Compiling readme.rst
[15/19] Compiling pdt/000/info.rst
[16/19] Compiling dev/hw/casing/plan.rst
[17/19] Compiling org/process/SOP/purchase.rst
[18/19] Compiling dev/hw/pcb1/plan.rst
[19/19] Compiling dev/sw/fw/plan.rst
Waf: Leaving directory `/tmp/pytest-of-roland/pytest-597/test_waf_samples_rst_odt_rstin7/tmp1_over/build'
'build' finished successfully (3.852s)
________________________ test_with_images[sphinx_html] _________________________

outinfo = 'sphinx_html'

    @pytest.mark.parametrize( 'outinfo',[
        'pdf','docx','html','odt','latex',
        'rst_odt','rst_html','rst_latex','sphinx_html'])
    def test_with_images(outinfo):
        with opn(_a_fix('with_images.rest.stpl')) as fp:
            lines = fp.readlines()
>       filename = convert_in_tempdir(lines,outinfo=outinfo)

../test/test_dcx.py:926: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../rstdoc/dcx.py:1007: in intmpiflister
    return normoutfile(f, suf0)(infile, outfile, *args, **kwargs)
../rstdoc/dcx.py:934: in normoutfiler
    f(infile, outfile, *args, **kwargs)
../rstdoc/dcx.py:902: in infilecwder
    return f(inf, outfile, *args, **kwargs)
../rstdoc/dcx.py:2172: in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
../rstdoc/dcx.py:2021: in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,
../rstdoc/dcx.py:902: in infilecwder
    return f(inf, outfile, *args, **kwargs)
../rstdoc/dcx.py:1158: in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cmdlist = ['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', ...]
kwargs = {'outfile': 'sphinx_html/32828f77e24258e88a787acbc5f01352d9228051.html.rst.html', 'stderr': -1, 'stdout': -1}
cmdstr = 'sphinx-build -b singlehtml . sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team...=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=32828f77e24258e88a787acbc5f01352d9228051.html.rst'
x = 'err'
r = CompletedProcess(args=['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', '-D', 'project=Project', '-D', 'a...rr=b'\nSphinx error:\nmaster file /tmp/tmpml393eie/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n')
stdout = 'Running Sphinx v2.2.1\nloading translations [None]... not available for built-in messages\nmaking output directory...... out of date\nbuilding [singlehtml]: all documents\nupdating environment: [new config] 0 added, 0 changed, 0 removed\n'
stderr = '\nSphinx error:\nmaster file /tmp/tmpml393eie/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n'

    def cmd(cmdlist, **kwargs):
        '''
        Runs ``cmdlist`` via subprocess.run and return stdout.
        In case of problems RstDocError is raised.
    
        :param cmdlist: command as list
        :param kwargs: arguments forwarded to ``subprocess.run()``
    
        '''
    
        cmdstr = ' '.join(cmdlist)
        try:
            for x in 'out err'.split():
                kwargs['std' + x] = sp.PIPE
            r = _toolrunner.run(cmdlist, **kwargs)
            try:
                stdout, stderr = _nstr(r.stdout), _nstr(r.stderr)
            except:
                stdout, stderr = _nbstr(r.stdout).decode('utf-8'), _nbstr(
                    r.stderr).decode('utf-8')
            if r.returncode != 0:
>               raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
                    r.returncode, cmdstr,
                    cwd()) + '\n[stdout]\n%s\n[stderr]\n%s' % (stdout, stderr))
E                   rstdoc.dcx.RstDocError: Error code 2 returned from 
E                   sphinx-build -b singlehtml . sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/usr/lib/python3.8/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=32828f77e24258e88a787acbc5f01352d9228051.html.rst
E                   in
E                   /tmp/tmpml393eie
E                   
E                   [stdout]
E                   Running Sphinx v2.2.1
E                   loading translations [None]... not available for built-in messages
E                   making output directory... done
E                   building [mo]: targets for 0 po files that are out of date
E                   building [singlehtml]: all documents
E                   updating environment: [new config] 0 added, 0 changed, 0 removed
E                   
E                   [stderr]
E                   
E                   Sphinx error:
E                   master file /tmp/tmpml393eie/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found

../rstdoc/dcx.py:756: RstDocError

----------- coverage: platform linux, python 3.8.0-final-0 -----------
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
/home/roland/mine/rstdoc/rstdoc/__init__.py        2      0   100%
/home/roland/mine/rstdoc/rstdoc/dcx.py          2022    172    91%   49-50, 54-55, 263-264, 268-269, 274-276, 281-282, 298-303, 338-339, 438-439, 443-447, 452-453, 690, 704-706, 711, 761, 769, 772, 805, 837-842, 866, 922, 985, 997-998, 1095, 1102, 1122, 1129-1131, 1149-1150, 1182, 1201-1202, 1235, 1247-1249, 1274-1275, 1307-1308, 1431-1433, 1588-1590, 1598-1599, 1609-1610, 1640, 1649, 1663-1664, 1670-1671, 1887-1888, 1894-1895, 1913, 1923, 1989, 2138-2139, 2143, 2167-2168, 2419, 2490, 2523-2527, 2546, 2551, 2553, 2675, 2712-2714, 2774-2776, 2784-2792, 2811, 2862-2863, 2892, 2913-2915, 2996, 3047, 3059, 3137, 3218, 3344, 3517, 3721, 3778, 3792, 3850, 3860, 3864-3869, 4008-4009, 4019-4026, 4059, 6257, 6330-6331, 6346-6347, 6528-6529, 6558, 6570, 6579, 6593-6596, 6601
/home/roland/mine/rstdoc/rstdoc/fromdocx.py      160    134    16%   78-81, 85, 89-90, 94, 105-129, 134-137, 142-154, 159-175, 180-201, 206-208, 223-298, 317-327, 331
/home/roland/mine/rstdoc/rstdoc/listtable.py     103     10    90%   210-231, 234, 250-252, 261
/home/roland/mine/rstdoc/rstdoc/reflow.py        149     13    91%   310-339, 342, 344, 346, 360-362, 371
/home/roland/mine/rstdoc/rstdoc/reimg.py          79     13    84%   117-119, 147-160, 163, 177-179, 183, 192
/home/roland/mine/rstdoc/rstdoc/retable.py       262     29    89%   237, 317-318, 424, 485-526, 530
/home/roland/mine/rstdoc/rstdoc/untable.py       127     12    91%   85, 99-100, 240-255, 258, 271-273, 283
/home/roland/mine/rstdoc/rstdoc/wafw.py           86     58    33%   36-41, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
----------------------------------------------------------------------------
TOTAL                                           2990    441    85%

============= 72 failed, 444 passed, 2 error in 4094.68s (1:08:14) =============
