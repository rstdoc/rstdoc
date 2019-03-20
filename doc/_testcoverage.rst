============================= test session starts ==============================
platform linux -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
rootdir: /home/roland/mine/rstdoc, inifile:
plugins: cov-2.6.0, pyfakefs-3.5
collected 217 items

rstdoc/dcx.py ..F...............F                                        [  8%]
rstdoc/retable.py ..                                                     [  9%]
test/test_dcx.py ....................................................... [ 35%]
........................................................................ [ 68%]
................FF                                                       [ 76%]
test/test_fromdocx.py F                                                  [ 76%]
test/test_rst_tables.py ..................................               [ 92%]
test/test_unretable.py ................                                  [100%]

=================================== FAILURES ===================================
______________________ [doctest] rstdoc.dcx._kw_from_path ______________________
3206 use file of path up to ``.git`` as keywords
3207 
3208     >>> dir="/pro jects/me_about-this-1.rst"
3209     >>> _kw_from_path(dir)
Expected:
    frozenset({'me', 'this', '1', 'about'})
Got:
    frozenset({'about', 'this', 'me', '1'})

/home/roland/mine/rstdoc/rstdoc/dcx.py:3209: DocTestFailure
______________________ [doctest] rstdoc.dcx.yield_with_kw ______________________
3288 
3289     >>> list(yield_with_kw('a',[('a/b',1,'a b'),('c/d',1,'c d')]))
3290     [(0, ['a/b', 1, 'a b'])]
3291     >>> list(yield_with_kw('a c',[('a/b',1,'a b'),('c/d',1,'c d')]))
3292     []
3293     >>> list(yield_with_kw('a',[('a/b',1,'a b'),('c/d',1,'a c d')]))
3294     [(0, ['a/b', 1, 'a b']), (1, ['c/d', 1, 'a c d'])]
3295     >>> kwargs={'dir':normjoin(dirname(__file__),'../test/fixtures')}
3296     >>> kws = 'svg'
3297     >>> len(list(yield_with_kw(kws,**kwargs)))
Expected:
    6
Got:
    12

/home/roland/mine/rstdoc/rstdoc/dcx.py:3297: DocTestFailure
_________________________________ test_pygrep __________________________________

    def test_pygrep():
        os.chdir(_a_fix(''))
        r = subprocess.run(['rstdcx','--pygrep', 'inline'],shell=True,stdout=subprocess.PIPE)
        outlines = r.stdout.decode().splitlines()
>       assert len(outlines) > 0
E       assert 0 > 0
E        +  where 0 = len([])

../test_dcx.py:727: AssertionError
----------------------------- Captured stderr call -----------------------------
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
Ignoring line 5873 in mapping file 'psfonts.map': Unknown token '<DSSerif-Bold'
Ignoring line 5875 in mapping file 'psfonts.map': Unknown token '<DSSerifUni-Bold'
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
Ignoring line 5873 in mapping file 'psfonts.map': Unknown token '<DSSerif-Bold'
Ignoring line 5875 in mapping file 'psfonts.map': Unknown token '<DSSerifUni-Bold'
___________________________________ test_kw ____________________________________

    def test_kw():
        os.chdir(_a_fix(''))
        r = subprocess.run(['rstdcx','--kw', 'png'],shell=True,stdout=subprocess.PIPE)
        outlines = r.stdout.decode().splitlines()
>       assert len(outlines) > 0
E       assert 0 > 0
E        +  where 0 = len([])

../test_dcx.py:735: AssertionError
----------------------------- Captured stderr call -----------------------------
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
Ignoring line 5873 in mapping file 'psfonts.map': Unknown token '<DSSerif-Bold'
Ignoring line 5875 in mapping file 'psfonts.map': Unknown token '<DSSerifUni-Bold'
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
Ignoring line 5873 in mapping file 'psfonts.map': Unknown token '<DSSerif-Bold'
Ignoring line 5875 in mapping file 'psfonts.map': Unknown token '<DSSerifUni-Bold'
______________________________ test_docx_to_rest _______________________________

tmpdir = local('/tmp/pytest-of-roland/pytest-10/test_docx_to_rest0')

    def test_docx_to_rest(
            tmpdir #temporary directory for the -lurg converted rest file
            ):
        '''
        This tests rstfromdocx, rstlisttable rstuntable rstreflow rstreimg.
        '''
        cwd = os.getcwd()
        try:
            with open(os.path.join(os.path.dirname(__file__),'fixtures', 'doc.rest'),encoding='utf-8') as f:
                expected = f.read().replace('\\','/')
            docxabs = os.path.abspath('test/fixtures/doc.docx')
            os.chdir(tmpdir)
>           main(docx=docxabs, listtable = True, untable = True, reflow = True, reimg = True)

../test_fromdocx.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../../rstdoc/fromdocx.py:266: in main
    extract_media(adocx)
../../rstdoc/fromdocx.py:105: in extract_media
    zf = ZipFile(adocx)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipfile.ZipFile [closed]>
file = '/home/roland/mine/rstdoc/test/fixtures/test/fixtures/doc.docx'
mode = 'r', compression = 0, allowZip64 = True, compresslevel = None

    def __init__(self, file, mode="r", compression=ZIP_STORED, allowZip64=True,
                 compresslevel=None):
        """Open the ZIP file with mode read 'r', write 'w', exclusive create 'x',
            or append 'a'."""
        if mode not in ('r', 'w', 'x', 'a'):
            raise ValueError("ZipFile requires mode 'r', 'w', 'x', or 'a'")
    
        _check_compression(compression)
    
        self._allowZip64 = allowZip64
        self._didModify = False
        self.debug = 0  # Level of printing: 0 through 3
        self.NameToInfo = {}    # Find file info given name
        self.filelist = []      # List of ZipInfo instances for archive
        self.compression = compression  # Method of compression
        self.compresslevel = compresslevel
        self.mode = mode
        self.pwd = None
        self._comment = b''
    
        # Check if we were passed a file-like object
        if isinstance(file, os.PathLike):
            file = os.fspath(file)
        if isinstance(file, str):
            # No, it's a filename
            self._filePassed = 0
            self.filename = file
            modeDict = {'r' : 'rb', 'w': 'w+b', 'x': 'x+b', 'a' : 'r+b',
                        'r+b': 'w+b', 'w+b': 'wb', 'x+b': 'xb'}
            filemode = modeDict[mode]
            while True:
                try:
>                   self.fp = io.open(file, filemode)
E                   FileNotFoundError: [Errno 2] No such file or directory: '/home/roland/mine/rstdoc/test/fixtures/test/fixtures/doc.docx'

/usr/lib/python3.7/zipfile.py:1182: FileNotFoundError

----------- coverage: platform linux, python 3.7.0-final-0 -----------
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
/home/roland/mine/rstdoc/rstdoc/__init__.py        0      0   100%
/home/roland/mine/rstdoc/rstdoc/dcx.py          1840    363    80%   241-243, 247-249, 254-257, 262-263, 280, 313-314, 402, 507, 606, 616-618, 624, 669, 673-674, 682, 685, 718, 750-755, 810, 872, 978, 985, 1003, 1010-1012, 1030-1031, 1050, 1063, 1082-1083, 1113, 1125-1127, 1152-1153, 1185-1186, 1307-1309, 1459-1461, 1476-1477, 1487-1488, 1520, 1526, 1545-1546, 1552-1553, 1752-1753, 1759-1760, 1778, 1785, 1840, 1980-1981, 1985, 2009-2010, 2262, 2325-2333, 2336, 2351, 2355-2357, 2366-2370, 2389, 2394, 2396, 2432-2433, 2520, 2557-2559, 2610-2612, 2620-2621, 2640, 2691-2692, 2718, 2739-2741, 2822, 2873, 2885, 2956, 3037, 3063, 3074, 3095, 3107, 3167, 3264, 3307, 3325-3628, 4898-4900, 4907-4908, 4912-4913, 4961-4964, 5038-5039, 5049-5050, 5203-5204, 5211-5212, 5214-5215, 5219, 5231, 5240, 5255
/home/roland/mine/rstdoc/rstdoc/fromdocx.py      160    129    19%   78-81, 85, 89-90, 94, 106-129, 134-137, 142-154, 159-175, 180-201, 206-208, 226-263, 267-298, 317-327, 331
/home/roland/mine/rstdoc/rstdoc/listtable.py     103     28    73%   205-257, 261
/home/roland/mine/rstdoc/rstdoc/reflow.py        149     33    78%   123-124, 305-367, 371
/home/roland/mine/rstdoc/rstdoc/reimg.py          79     69    13%   84-122, 137-188, 192
/home/roland/mine/rstdoc/rstdoc/retable.py       262     29    89%   237, 317-318, 424, 485-526, 530
/home/roland/mine/rstdoc/rstdoc/untable.py       127     29    77%   85, 99-100, 120, 235-279, 283
/home/roland/mine/rstdoc/rstdoc/wafw.py           86     54    37%   39-40, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
----------------------------------------------------------------------------
TOTAL                                           2806    734    74%

=============================== warnings summary ===============================
/home/roland/mine/rstdoc/rstdoc/dcx.py:2551: DeprecationWarning: invalid escape sequence \s
  '''

/usr/lib/python3.7/site-packages/pygal/_compat.py:23: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
  from collections import Iterable

/home/roland/mine/rstdoc/rstdoc/fromdocx.py:180: DeprecationWarning: invalid escape sequence \s
  mf = re.split(r'\s\s+__code__', re.split('\s\sMakefile', example_tree)[1])[0]

/home/roland/mine/rstdoc/rstdoc/reflow.py:115: DeprecationWarning: invalid escape sequence \.
  ss = re.split('(?<!e\.g)\.\s+', txt)

/home/roland/mine/rstdoc/rstdoc/reflow.py:157: DeprecationWarning: invalid escape sequence \.
  re_literal = re.compile('^(?!\.\. ).*::\s*$')

/home/roland/mine/rstdoc/rstdoc/reflow.py:230: DeprecationWarning: invalid escape sequence \*
  res = re.sub('\*\*\*\*+', '', d)

/home/roland/mine/rstdoc/rstdoc/reflow.py:234: DeprecationWarning: invalid escape sequence \w
  res = re.sub('(\w)\s+\*\*\s*$', r'\1**', res)

/home/roland/mine/rstdoc/rstdoc/reflow.py:236: DeprecationWarning: invalid escape sequence \s
  res = re.sub('^\s*\*\*\s*(\*\*)*$', r'', res)

/home/roland/mine/rstdoc/rstdoc/reflow.py:250: DeprecationWarning: invalid escape sequence \s
  nbe = re.compile('\s+$')

/home/roland/mine/rstdoc/rstdoc/retable.py:61: DeprecationWarning: invalid escape sequence \s
  '''^(\s*)(([#*=\-^~+_.,"'!$%&\\\(\)/:;<>?@\[\]`{|}])\\3+)\s*$''')

/home/roland/mine/rstdoc/rstdoc/retable.py:328: DeprecationWarning: invalid escape sequence \s
  match = re.match('^(\s*).*$', lines[upper])

/home/roland/mine/rstdoc/rstdoc/untable.py:97: DeprecationWarning: invalid escape sequence \w
  if _no == None and (not re.search('\w', id) or ' ' in id.strip() or

/home/roland/mine/rstdoc/rstdoc/listtable.py:158: DeprecationWarning: invalid escape sequence \s
  indent = re.search('\s*', line).span()[1]

/usr/lib/python3.7/site-packages/docutils/io.py:245: DeprecationWarning: 'U' mode is deprecated
  self.source = open(source_path, mode, **kwargs)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1065: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  elif el.getchildren():
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1066: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for child in el.getchildren():
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)

<doctest rstdoc.dcx.gen[0]>:7: DeprecationWarning: invalid escape sequence \s

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/docutils/io.py:245: DeprecationWarning: 'U' mode is deprecated
  self.source = open(source_path, mode, **kwargs)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1617: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if self.current_element.getchildren()[-1].tail:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1620: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  self.current_element.getchildren()[-1].tail = text
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1617: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if self.current_element.getchildren()[-1].tail:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1620: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  self.current_element.getchildren()[-1].tail = text
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1616: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  if len(self.current_element.getchildren()) > 0:
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1065: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  elif el.getchildren():
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1066: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for child in el.getchildren():
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)
/usr/lib/python3.7/site-packages/docutils/writers/odf_odt/__init__.py:1137: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
  for subel in el.getchildren(): walk(subel)

/usr/lib/python3.7/site-packages/docutils/io.py:245: DeprecationWarning: 'U' mode is deprecated
  self.source = open(source_path, mode, **kwargs)
/usr/lib/python3.7/site-packages/docutils/io.py:245: DeprecationWarning: 'U' mode is deprecated
  self.source = open(source_path, mode, **kwargs)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/docutils/io.py:245: DeprecationWarning: 'U' mode is deprecated
  self.source = open(source_path, mode, **kwargs)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/matplotlib/figure.py:445: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  % get_backend())
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)
/usr/lib/python3.7/site-packages/defusedxml/ElementTree.py:68: DeprecationWarning: The html argument of XMLParser() is deprecated
  _XMLParser.__init__(self, html, target, encoding)

source:180: DeprecationWarning: invalid escape sequence \s

-- Docs: https://docs.pytest.org/en/latest/warnings.html
============ 5 failed, 212 passed, 1694 warnings in 1292.31 seconds ============
