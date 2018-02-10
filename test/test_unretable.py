import pytest
from rstdoc.untable import untable
from rstdoc.retable import retable

def test_untable(request):
    data = '''\
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
'''
    data=data.splitlines()

    assert list(untable(data)) == ['.. _`cccddd001`:\n\n',
        ':cccddd001:\n\n',
        '**General 1**\n',
        '\n',
        'This is general\n',
        'General\n',
        '\n',
        'General\n',
        '.. _`xxx010`:\n\n',
        ':xxx010:\n\n',
        'sd\n',
        '\n',
        '\n']

data = '''\
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
     - xxx

And some more text.
'''.splitlines()

def test_untable1():
    def rowfun(row,nColumns,org,islast,withheader):
        for rc in row:
            for r in rc:
                assert 'And some more text' not in r
        yield from org
    res = list(untable(data,rowfun))

def test_retable():
    res = '\n'.join(list(retable(data)))
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


