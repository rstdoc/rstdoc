============================= test session starts ==============================
platform linux -- Python 3.8.0, pytest-5.2.4, py-1.8.0, pluggy-0.13.0
rootdir: /home/roland/mine/rstdoc, inifile: pytest.ini
plugins: mock-1.11.0, cov-2.8.1
collected 318 items

rstdoc/dcx.py .....FF.F.............                                     [  6%]
rstdoc/retable.py ..                                                     [  7%]
test/test_dcx.py ....................................................... [ 24%]
........................................................................ [ 47%]
........................................................................ [ 70%]
............................................                             [ 83%]
test/test_fromdocx.py .                                                  [ 84%]
test/test_rst_tables.py ..................................               [ 94%]
test/test_unretable.py ................                                  [100%]

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

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 904, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1252, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 758, in cmd
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
1043         >>> exists('tst.png')
1044         True
1045         >>> rmrf('tst.png')
1046         >>> exists('tst.png')
1047         False
1048 
1049         >>> convert('ra.rest.stpl') #doctest: +ELLIPSIS
1050         ['<!DOCTYPE html>\n', ...
1051 
1052         >>> convert('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
UNEXPECTED EXCEPTION: RstDocError("Error code 1 returned from \npandoc --standalone -f rst -t docx ra.rest.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx\nin\n/home/roland/mine/rstdoc/doc\n\n[stdout]\n\n[stderr]\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65\npandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)\n")
Traceback (most recent call last):

  File "/usr/lib/python3.8/doctest.py", line 1328, in __run
    exec(compile(example.source, filename, "single",

  File "<doctest rstdoc.dcx.convert_in_tempdir[12]>", line 1, in <module>

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2172, in convert
    infile = thisconverter(infile, out_(), outinfo, fn_i_ln)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 904, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1252, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 758, in cmd
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


/home/roland/mine/rstdoc/rstdoc/dcx.py:1052: UnexpectedException
__________________________ [doctest] rstdoc.dcx.dorst __________________________
1836         ['.. default-role:: math\n', ...
1837 
1838         >>> dorst(['hi there']) #doctest: +ELLIPSIS
1839         ['.. default-role:: math\n', '\n', 'hi there\n', ...
1840 
1841         >>> dorst(['hi there'], None,'html') #doctest: +ELLIPSIS
1842         <!DOCTYPE html>
1843         ...
1844 
1845         >>> dorst('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
UNEXPECTED EXCEPTION: RstDocError("Error code 1 returned from \npandoc --standalone -f rst -t docx ra.rest.stpl.rest -o ra.docx --reference-doc /home/roland/mine/reference.docx\nin\n/home/roland/mine/rstdoc/doc\n\n[stdout]\n\n[stderr]\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.rstfile.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'file:rstdoc.docx#dcx.counter.__init_' at chunk line 1 column 65\n[WARNING] Reference not found for 'r' at line 393 column 45\n[WARNING] Reference not found for 'f' at line 393 column 54\n[WARNING] Reference not found for 'v' at line 393 column 60\npandoc: /home/roland/mine/reference.docx: openBinaryFile: does not exist (No such file or directory)\n")
Traceback (most recent call last):

  File "/usr/lib/python3.8/doctest.py", line 1328, in __run
    exec(compile(example.source, filename, "single",

  File "<doctest rstdoc.dcx.dorst[7]>", line 1, in <module>

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 2021, in dorst
    stdout = rsttool(infile, '-' if finalsysout else outfile,

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 904, in infilecwder
    return f(inf, outfile, *args, **kwargs)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 1252, in rst_pandoc
    stdout = cmd(pandoccmd, outfile=outfile)

  File "/home/roland/mine/rstdoc/rstdoc/dcx.py", line 758, in cmd
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


/home/roland/mine/rstdoc/rstdoc/dcx.py:1845: UnexpectedException

----------- coverage: platform linux, python 3.8.0-final-0 -----------
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
/home/roland/mine/rstdoc/rstdoc/__init__.py        2      0   100%
/home/roland/mine/rstdoc/rstdoc/dcx.py          2020    181    91%   50-51, 55-56, 264-265, 269-270, 275-277, 282-283, 299-304, 339-340, 437-449, 453-454, 692, 706-708, 713, 763, 771, 774, 807, 839-844, 868, 924, 987, 999-1000, 1097, 1104, 1124, 1131-1133, 1151-1152, 1184, 1203-1204, 1237, 1249-1251, 1276-1277, 1309-1310, 1433-1435, 1590-1592, 1600-1601, 1611-1612, 1642, 1651, 1665-1666, 1672-1673, 1889-1890, 1896-1897, 1915, 1925, 1989, 2138-2139, 2143, 2167-2168, 2419, 2490, 2508, 2523-2527, 2546, 2551, 2553, 2675, 2712-2714, 2774-2776, 2784-2792, 2811, 2862-2863, 2892, 2913-2915, 2996, 3047, 3059, 3137, 3218, 3344, 3517, 3721, 3778, 3792, 3850, 3860, 3864-3869, 4008-4009, 4019-4026, 4059, 6257, 6262-6264, 6330-6331, 6346-6347, 6528-6529, 6558, 6570, 6579, 6593-6596, 6601
/home/roland/mine/rstdoc/rstdoc/fromdocx.py      160    134    16%   78-81, 85, 89-90, 94, 105-129, 134-137, 142-154, 159-175, 180-201, 206-208, 223-298, 317-327, 331
/home/roland/mine/rstdoc/rstdoc/listtable.py     103     10    90%   210-231, 234, 250-252, 261
/home/roland/mine/rstdoc/rstdoc/reflow.py        149     13    91%   310-339, 342, 344, 346, 360-362, 371
/home/roland/mine/rstdoc/rstdoc/reimg.py          79     13    84%   117-119, 147-160, 163, 177-179, 183, 192
/home/roland/mine/rstdoc/rstdoc/retable.py       262     29    89%   237, 317-318, 424, 485-526, 530
/home/roland/mine/rstdoc/rstdoc/untable.py       127     12    91%   85, 99-100, 240-255, 258, 271-273, 283
/home/roland/mine/rstdoc/rstdoc/wafw.py           86     58    33%   36-41, 47-55, 60-63, 70-84, 88-95, 98-107, 111-114, 117-128
----------------------------------------------------------------------------
TOTAL                                           2988    450    85%

================== 3 failed, 315 passed in 2185.14s (0:36:25) ==================
