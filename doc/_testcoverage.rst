============================= test session starts ==============================
platform linux -- Python 3.8.0, pytest-5.2.4, py-1.8.0, pluggy-0.13.0
rootdir: /home/roland/mine/rstdoc, inifile: pytest.ini
plugins: mock-1.11.0, cov-2.8.1
collected 518 items

rstdoc/dcx.py ......................                                     [  4%]
rstdoc/retable.py ..                                                     [  4%]
test/test_dcx.py ....................................................... [ 15%]
........................................................................ [ 29%]
........................................................................ [ 43%]
........................................................................ [ 56%]
........................................................................ [ 70%]
........................................................................ [ 84%]
....F.......................                                             [ 90%]
test/test_fromdocx.py .                                                  [ 90%]
test/test_rst_tables.py ..................................               [ 96%]
test/test_unretable.py ................                                  [100%]

=================================== FAILURES ===================================
________________________ test_with_images[sphinx_html] _________________________

outinfo = 'sphinx_html'

    @pytest.mark.parametrize( 'outinfo',[
        'pdf','docx','html','odt','latex',
        'rst_odt','rst_html','rst_latex','sphinx_html'])
    def test_with_images(outinfo):
        with opn(_a_fix('with_images.rest.stpl')) as fp:
            lines = fp.readlines()
>       filename = convert_in_tempdir(lines,outinfo=outinfo)

test/test_dcx.py:1018: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
rstdoc/dcx.py:1017: in intmpiflister
    return normoutfile(f, suf0)(infile, outfile, *args, **kwargs)
rstdoc/dcx.py:944: in normoutfiler
    f(infile, outfile, *args, **kwargs)
rstdoc/dcx.py:913: in infilecwder
    return f(inf, outfile, *args, **kwargs)
rstdoc/dcx.py:2192: in convert
    infile = thisconverter(infile, out_(), outinfo, **kwargs)
rstdoc/dcx.py:2037: in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,
rstdoc/dcx.py:913: in infilecwder
    return f(inf, outfile, *args, **kwargs)
rstdoc/dcx.py:1170: in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cmdlist = ['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', ...]
kwargs = {'outfile': 'sphinx_html/32828f77e24258e88a787acbc5f01352d9228051.html.rst.html', 'stderr': -1, 'stdout': -1}
cmdstr = 'sphinx-build -b singlehtml . sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team...=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=32828f77e24258e88a787acbc5f01352d9228051.html.rst'
x = 'err'
r = CompletedProcess(args=['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', '-D', 'project=Project', '-D', 'a...rr=b'\nSphinx error:\nmaster file /tmp/tmpzzlwn5oi/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n')
stdout = 'Running Sphinx v2.2.1\nloading translations [None]... not available for built-in messages\nmaking output directory...... out of date\nbuilding [singlehtml]: all documents\nupdating environment: [new config] 0 added, 0 changed, 0 removed\n'
stderr = '\nSphinx error:\nmaster file /tmp/tmpzzlwn5oi/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n'

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
E                   /tmp/tmpzzlwn5oi
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
E                   master file /tmp/tmpzzlwn5oi/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found

rstdoc/dcx.py:767: RstDocError

----------- coverage: platform linux, python 3.8.0-final-0 -----------
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
/home/roland/mine/rstdoc/rstdoc/__init__.py        2      0   100%
/home/roland/mine/rstdoc/rstdoc/dcx.py          2043    160    92%   49-50, 54-55, 263-264, 268-269, 274-276, 281-282, 298-303, 338-339, 715-717, 722, 772, 780, 783, 816, 848-853, 877, 932, 995, 1007-1008, 1105, 1112, 1132, 1139, 1141-1143, 1161-1162, 1214-1215, 1248, 1260-1262, 1287-1288, 1320-1321, 1444-1446, 1601-1603, 1611-1612, 1622-1623, 1653, 1662, 1676-1677, 1683-1684, 1902-1903, 1909-1910, 1928, 1938, 2004, 2155-2156, 2160, 2184-2185, 2439, 2510, 2528, 2543-2547, 2566, 2571, 2573, 2695, 2732-2734, 2794-2796, 2804-2812, 2831, 2882-2883, 2912, 2933-2935, 3016, 3067, 3079, 3157, 3238, 3364, 3539, 3743, 3800, 3814, 3873, 3883, 3887-3892, 4031-4032, 4042-4049, 6280, 6353-6354, 6369-6370, 6594-6595, 6624, 6638, 6647, 6668-6669, 6672
/home/roland/mine/rstdoc/rstdoc/fromdocx.py      160    134    16%   82-85, 89, 93-94, 98, 109-133, 138-141, 146-158, 163-179, 184-205, 210-212, 227-302, 321-331, 335
/home/roland/mine/rstdoc/rstdoc/listtable.py     103     10    90%   210-231, 234, 250-252, 261
/home/roland/mine/rstdoc/rstdoc/reflow.py        149     13    91%   310-339, 342, 344, 346, 360-362, 371
/home/roland/mine/rstdoc/rstdoc/reimg.py          79     13    84%   119-121, 149-162, 165, 179-181, 185, 194
/home/roland/mine/rstdoc/rstdoc/retable.py       262     29    89%   237, 317-318, 424, 485-526, 530
/home/roland/mine/rstdoc/rstdoc/untable.py       127     12    91%   87, 101-102, 242-257, 260, 273-275, 285
/home/roland/mine/rstdoc/rstdoc/wafw.py           86     58    33%   36-41, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
----------------------------------------------------------------------------
TOTAL                                           3011    429    86%

================== 1 failed, 517 passed in 4280.95s (1:11:20) ==================
