============================= test session starts ==============================
platform linux -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
rootdir: /home/roland/mine/rstdoc, inifile:
plugins: cov-2.6.0, pyfakefs-3.5
collected 211 items

rstdoc/dcx.py ...............                                            [  7%]
rstdoc/retable.py ..                                                     [  8%]
test/test_dcx.py ....................................................... [ 34%]
........................................................................ [ 68%]
................                                                         [ 75%]
test/test_fromdocx.py .                                                  [ 76%]
test/test_rst_tables.py ..................................               [ 92%]
test/test_unretable.py ................                                  [100%]

----------- coverage: platform linux, python 3.7.0-final-0 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
rstdoc/__init__.py        0      0   100%
rstdoc/dcx.py          1785    359    80%   241-243, 247-249, 254-257, 262-263, 280, 313-314, 402, 505, 604, 614-616, 622, 667, 671-672, 680, 683, 716, 748-753, 808, 870, 976, 983, 1001, 1008-1010, 1028-1029, 1048, 1061, 1080-1081, 1111, 1123-1125, 1150-1151, 1183-1184, 1305-1307, 1457-1459, 1474-1475, 1485-1486, 1518, 1524, 1543-1544, 1550-1551, 1750-1751, 1757-1758, 1776, 1783, 1838, 1978-1979, 1983, 2007-2008, 2261, 2324-2332, 2335, 2350, 2354-2356, 2365-2369, 2388, 2393, 2395, 2431-2432, 2519, 2556-2558, 2609-2611, 2619-2620, 2639, 2690-2691, 2717, 2738-2740, 2821, 2872, 2884, 2955, 3036, 3062, 3073, 3093-3094, 3106, 3166, 3210-3513, 4781-4783, 4790-4791, 4795-4796, 4844-4847, 4921-4922, 4932-4933, 5076-5077, 5086, 5098, 5107, 5119, 5122
rstdoc/fromdocx.py      160     36    78%   80-81, 119-120, 123, 126-127, 152, 165-166, 193-194, 226-263, 278, 280, 282, 284, 317-327, 331
rstdoc/listtable.py     103     12    88%   210-231, 234, 236, 239, 250-252, 261
rstdoc/reflow.py        149     14    91%   310-339, 342, 344, 346, 349, 360-362, 371
rstdoc/reimg.py          79     15    81%   101-102, 117-119, 147-160, 163, 165, 177-179, 192
rstdoc/retable.py       262     29    89%   237, 317-318, 424, 485-526, 530
rstdoc/untable.py       127     13    90%   85, 99-100, 240-255, 258, 260, 271-273, 283
rstdoc/wafw.py           86     54    37%   39-40, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
---------------------------------------------------
TOTAL                  2751    532    81%


=============================== warnings summary ===============================
/home/roland/mine/rstdoc/rstdoc/dcx.py:2550: DeprecationWarning: invalid escape sequence \s
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

-- Docs: https://docs.pytest.org/en/latest/warnings.html
================= 211 passed, 1693 warnings in 1305.45 seconds =================
