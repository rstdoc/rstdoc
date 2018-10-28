import sys
sys.path = ['src/test/mocks'] + sys.path
import pytest
from rstdoc.untable import untable
from rstdoc.retable import retable
from rstdoc.listtable import gridtable
from rstdoc.reflow import reflow

undata = '''\
.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - **CCC-DDD-001**
     - **General 1**
     - This is general
       General

       General
   * - **xXx-010**
     - sd
     -
'''.splitlines()
undatares='''\
.. _`cccddd001`:

cccddd001:

**General 1**

This is general
General

General
.. _`xxx010`:

xxx010:

sd

'''
def test_untable0(request):
    res = '\n'.join(untable(undata))
    assert res == undatares

qfdata = '''\
the quick
brown fox
jumps

- over
the lazy

- dog

|dta|: Table legend

.. list-table::
   :name:
   :widths: 20 80
   :header-rows: 1

   * - Bit
     - Function

   * - 0
       1
     - xxx
       yyy

And some more text.
'''.splitlines()
qfdatauntable = '''\
the quick
brown fox
jumps

- over
the lazy

- dog

|dta|: Table legend

.. _`bit`:

bit:

Function

.. _`01`:

01:

xxx
yyy

And some more text.'''
def test_untable1():
    def rowfun(row,nColumns,org,islast,withheader):
        for rc in row:
            for r in rc:
                assert 'And some more text' not in r
        yield from org
    untable(qfdata,rowfun)
def test_untable2():
    res = '\n'.join(untable(qfdata))
    assert res == qfdatauntable

def test_retable0():
    res = '\n'.join(list(retable(qfdata)))
    res.splitlines()[-4] == '+-----+----------+'

datacomment = '''\
the quick
brown fox
jumps

- over
the lazy

- dog

|dta|: Table legend

.. .. list-table::
..    :name:
..    :widths: 20 80
..    :header-rows: 1
.. 
..    * - Bit
..      - Function
.. 
..    * - 0
..      - xxx

And some more text.
'''.splitlines()

def test_retablecomment():
    res = '\n'.join(list(retable(datacomment)))
    res.splitlines()[-4] != '+-----+----------+'

badtables='''\
**Current measurement**

+-----+-----+-----+
| **V | **R | **A |
| alu | eso | ccu |
| e** | lut | rac |
|     | ion | y** |
|     | **  |     |
+-----+-----+-----+
| 0;  | 10  | ±   |
| 0.0 | µA  | 10  |
| 5   |     | %;  |
| –   |     |     |
| 15  |     | or  |
| mA  |     | ±   |
|     |     | 5µA |
|     |     | whi |
|     |     | che |
|     |     | ver |
|     |     | gre |
|     |     | ate |
|     |     | r   |
+-----+-----+-----+

**Voltage measurement**

+-----+-----+-----+
| **V | **R | **A |
| alu | eso | ccu |
| e** | lut | rac |
|     | ion | y** |
|     | **  |     |
+-----+-----+-----+
| 0;  |     |  x  |
| ±   |     |     |
| 90  |     |     |
| V   |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+

'''.splitlines(True)
badtableres='''\
**Current measurement**

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **Value**
     - **Resolution**
     - **Accuracy**

   * - 0;0.05–15mA
     - 10µA
     - ±10%;or±5µAwhichevergreater


**Voltage measurement**

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **Value**
     - **Resolution**
     - **Accuracy**

   * - 0;±90V
     - 
     - x


'''
def test_listtablebasic0():
    res = ''.join(gridtable(badtables,join='0'))
    assert res == badtableres


badtable012='''\
**Document History**

+-----------------+-----------------+-----------------+-----------------+
| Version         | Date            | Who             | Change          |
+-----------------+-----------------+-----------------+-----------------+
| 1.0             | 10.07.2015      | xxxxxxx         | Initial setup   |
|                 |                 |                 | of document     |
+-----------------+-----------------+-----------------+-----------------+
| 1.6             | DRAFT           |                 | Updated: Manual |
|                 |                 |                 | tests in System |
|                 |                 |                 | performance     |
|                 |                 |                 | test cases      |
+-----------------+-----------------+-----------------+-----------------+
'''.splitlines(True)
badtable012res='''\
**Document History**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 0


   * - Version
     - Date
     - Who
     - Change

   * - 1.0
     - 10.07.2015
     - xxxxxxx
     - Initial setup
       of document

   * - 1.6
     - DRAFT
     - 
     - Updated: Manual
       tests in System
       performance
       test cases

'''
def test_listtablebasic012():
    res = ''.join(gridtable(badtable012,join='012'))
    assert res == badtable012res

def test_listtablebasic012indent():
    res = ''.join(gridtable([' '*3+x for x in badtable012],join='012'))
    assert res == ''.join([' '*3+x for x in badtable012res.splitlines(True)])

joindata='''\
line before

+---+---+---+
| A | x | + |
+===+===+===+
| B | y | 2 |
| C | z | 3 |
+---+---+---+

line after
'''.splitlines(True)
jd1='''\
line before

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - A
     - x
     - +

   * - BC
     - y z
     - 2
       3


line after
'''
jd2='''\
line before

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - A
     - x
     - +

   * - BC
     - yz
     - 2 3


line after
'''
jd3='''\
line before

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - A
     - x
     - +

   * - BC
     - yz
     - 23


line after
'''

def test_listtablejoin1():
    res = ''.join(gridtable(joindata))
    assert res == jd1

def test_listtablejoin2():
    res = ''.join(gridtable(joindata,join='001'))
    assert res == jd2

def test_listtablejoin3():
    res = ''.join(gridtable(joindata,join='0'))
    assert res == jd3

badtablereflow='''\
**Current measurement**

+-------------+----------------+-----------------------------+
| **Value**   | **Resolution** | **Accuracy**                |
+-------------+----------------+-----------------------------+
| 0;0.05–15mA | 10µA           | ±10%;or±5µAwhichevergreater |
+-------------+----------------+-----------------------------+

**Voltage measurement**

+-----------+----------------+--------------+
| **Value** | **Resolution** | **Accuracy** |
+-----------+----------------+--------------+
| 0;±90V    |                | x            |
+-----------+----------------+--------------+

'''
def test_reflow0():
    res = ''.join(reflow(badtables,join='0'))
    assert res == badtablereflow

reflowqfd = '''\
the quick brown fox jumps

- over the lazy

- dog

|dta|: Table legend

.. list-table::
   :name:
   :widths: 20 80
   :header-rows: 1

   * - Bit
     - Function

   * - 0 1
     - xxx yyy

And some more text.
'''
def test_reflowqf():
    res = ''.join(reflow(qfdata))
    assert res == reflowqfd

refl='''\
Title
---

:id: description goes
here.

- A
sentence
per
line.
That is a 
good idea.

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
=====  =====  =======

| line
| stay


::
   this
   as
   is

This too::

   as::
   .. is::
   - ok?
'''.splitlines(True)
reflres='''\
Title
-----

:id: description goes here.

- A sentence per line. That is a good idea.

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
=====  =====  =======

| line
| stay


::
   this
   as
   is

This too::

   as::
   .. is::
   - ok?
'''
def test_reflowqf1():
   res = ''.join(reflow(refl))
   assert res == reflres

refl2='''\
============
Title
============

   Some text here.
   It should keep
   the indentation.

- A
sentence
per
line.
That is a 
good idea.
'''.splitlines(True)
refl2res='''\
=====
Title
=====

   Some text here.
   It should keep the indentation.

- A sentence per line.
  That is a good idea.
'''
def test_reflowqf2():
   res = ''.join(reflow(refl2,sentence=True))
   assert res == refl2res

rfec='''\
.. list-table::
   :widths: 25 25 25 25
   :header-rows: 0


   * - 
     - **Basic**
     - **Intermediate**
     - **Advanced**

   * - **OK**
     - a is equal b if c
     is equal d or is it not well let us see
     if it works out after all
     - 
     - 

   * - **NOT**
     - 
     - 
     - 
'''.splitlines(True)
rfecres='''\
.. list-table::
   :widths: 25 25 25 25
   :header-rows: 0


   * -
     - **Basic**
     - **Intermediate**
     - **Advanced**

   * - **OK**
     - a is equal b if c is equal d or is it not well let us see if it works
       out after all
     -
     -

   * - **NOT**
     -
     -
     -
'''
def test_reflowemptycells():
   res = ''.join(reflow(rfec))
   assert res == rfecres

