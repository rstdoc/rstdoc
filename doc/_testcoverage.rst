============================= test session starts ==============================
platform linux -- Python 3.9.1, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/roland/mine/rstdoc, configfile: pytest.ini
plugins: Flask-Dance-3.1.0, xonsh-0.9.24, cov-2.10.1, mock-2.0.0
collected 517 items

rstdoc/dcx.py .....................                                      [  4%]
rstdoc/retable.py ..                                                     [  4%]
test/test_dcx.py ....................................................... [ 15%]
........................................................................ [ 29%]
........................................................................ [ 42%]
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

test/test_dcx.py:941: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
rstdoc/dcx.py:1028: in intmpiflister
    return normoutfile(f, suf0)(infile, outfile, *args, **kwargs)
rstdoc/dcx.py:953: in normoutfiler
    f(infile, outfile, *args, **kwargs)
rstdoc/dcx.py:922: in infilecwder
    return f(inf, outfile, *args, **kwargs)
rstdoc/dcx.py:2201: in convert
    infile = thisconverter(infile, out_(), outinfo, **kwargs)
rstdoc/dcx.py:2046: in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,
rstdoc/dcx.py:922: in infilecwder
    return f(inf, outfile, *args, **kwargs)
rstdoc/dcx.py:1178: in rst_sphinx
    cmd(sphinxcmd, outfile=outfn)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cmdlist = ['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', ...]
kwargs = {'outfile': 'sphinx_html/32828f77e24258e88a787acbc5f01352d9228051.html.rst.html', 'stderr': -1, 'stdout': -1}
cmdstr = 'sphinx-build -b singlehtml . sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team...=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=32828f77e24258e88a787acbc5f01352d9228051.html.rst'
x = 'err'
r = CompletedProcess(args=['sphinx-build', '-b', 'singlehtml', '.', 'sphinx_html', '-C', '-D', 'project=Project', '-D', 'a...rr=b'\nSphinx error:\nmaster file /tmp/tmpyngr3uoq/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n')
stdout = 'Running Sphinx v3.4.0\nloading translations [None]... not available for built-in messages\nmaking output directory...... out of date\nbuilding [singlehtml]: all documents\nupdating environment: [new config] 0 added, 0 changed, 0 removed\n'
stderr = '\nSphinx error:\nmaster file /tmp/tmpyngr3uoq/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found\n'

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
E                   sphinx-build -b singlehtml . sphinx_html -C -D project=Project -D author=Project Team -D copyright=2019, Project Team -D version=1.0 -D release=1.0.0 -D html_theme=bootstrap -D html_theme_path=/home/roland/.local/lib/python3.9/site-packages/sphinx_bootstrap_theme -D source_suffix=.rest -D numfig=0 -D smartquotes=0 -D templates_path= -D language=None -D highlight_language=none -D default_role=math -D pygments_style=sphinx -D exclude_patterns=_build,Thumbs.db,.DS_Store -D master_doc=32828f77e24258e88a787acbc5f01352d9228051.html.rst
E                   in
E                   /tmp/tmpyngr3uoq
E                   
E                   [stdout]
E                   Running Sphinx v3.4.0
E                   loading translations [None]... not available for built-in messages
E                   making output directory... done
E                   building [mo]: targets for 0 po files that are out of date
E                   building [singlehtml]: all documents
E                   updating environment: [new config] 0 added, 0 changed, 0 removed
E                   
E                   [stderr]
E                   
E                   Sphinx error:
E                   master file /tmp/tmpyngr3uoq/32828f77e24258e88a787acbc5f01352d9228051.html.rst.rest not found

rstdoc/dcx.py:776: RstDocError

----------- coverage: platform linux, python 3.9.1-final-0 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
rstdoc/__init__.py        2      0   100%
rstdoc/dcx.py          2087    193    91%   50-51, 55-56, 268-269, 273-274, 279-281, 286-287, 303-308, 343-344, 724-726, 731, 781, 789, 792, 825, 857-862, 886, 941, 1004, 1018-1019, 1120, 1140, 1147, 1149-1151, 1169-1170, 1222-1223, 1256, 1268-1270, 1295-1296, 1328-1329, 1452-1454, 1609-1611, 1619-1620, 1630-1631, 1661, 1670, 1684-1685, 1691-1692, 1910-1911, 1917-1918, 1936, 1945, 2011, 2164-2165, 2169, 2193-2194, 2448, 2519, 2537, 2552-2556, 2575, 2580, 2582, 2704, 2741-2743, 2803-2805, 2813-2821, 2840, 2891-2892, 2921, 2942-2944, 3025, 3076, 3088, 3166, 3247, 3315, 3373, 3549, 3778-3784, 3823-3856, 3896, 3910, 3969, 3979, 3983-3988, 4128-4129, 4139-4146, 6377, 6451-6452, 6467-6468, 6699-6700, 6729, 6743, 6752, 6773-6774, 6777
rstdoc/fromdocx.py      162    135    17%   83-86, 90, 94-95, 99, 110-134, 139-142, 147-159, 164-180, 185-206, 211-213, 228-304, 323-333, 337
rstdoc/listtable.py     105     11    90%   211-233, 236, 252-254, 263
rstdoc/reflow.py        151     14    91%   311-341, 344, 346, 348, 362-364, 373
rstdoc/reimg.py          81     14    83%   120-122, 150-164, 167, 181-183, 187, 196
rstdoc/retable.py       264     30    89%   238, 318-319, 425, 486-528, 532
rstdoc/untable.py       129     13    90%   88, 102-103, 243-259, 262, 275-277, 287
rstdoc/wafw.py           86     58    33%   36-41, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
---------------------------------------------------
TOTAL                  3067    468    85%

=========================== short test summary info ============================
FAILED test/test_dcx.py::test_with_images[sphinx_html] - rstdoc.dcx.RstDocErr...
================== 1 failed, 516 passed in 8660.78s (2:24:20) ==================
