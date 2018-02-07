#!/usr/bin/env python
# encoding: utf-8 

#modified from
#https://github.com/rackerlabs/docs-rackspace/blob/master/tools/table.py
#in
#https://gist.github.com/rpuntaie/c23c1b6af41055df9482f1eecd1a70d9

#test with
#py.test --doctest-modules listtable.py

"""
Convert RST grid tables to list-tables.

Basic usage
-----------
#. Convert grid tables in a file to list-tables. The result is output to stdout::

      $ listtable.py input.rst

#. Convert several files::

      $ listtable.py input1.rst input2.rst
      $ listtable.py *.rst

#. Use pipe:

      $ cat in.rst | listtable.py -  | untable.py - > out.rst

Options
-------
-j, --join       e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join

.. important::

    Always build your document and compare the rendered list-table to the
    original rendered grid table. It is very possible that some errors may
    occur that require manual fixes, especially when converting complex tables.

Notes
-----
- The script does not create titles for tables. After conversion, you may
  want to manually add titles.
- The script sets all columns to the same width: ``100 / col_num``. After
  conversion, you may want to manually edit ``:width:``.
- The script automatically uses the first row of the table as a header.
  After conversion, you may want to manually edit ``:header-rows:``.
- The script requires a blank line after each table. If the blank line is at
  the end of the file, you must add an extra line temporarily for the script
  to process the table correctly.
"""

import re

def tolisttable(
        data
        ,join='012'
        ):
    """convert grid table to list table

    >>> data = ['line\\n','\\n','+---+---+---+\\n','| A | x | + |\\n','+===+===+===+\\n','| B | y | 2 |\\n','| C | z | 3 |\\n','+---+---+---+\\n']
    >>> ''.join(tolisttable(data))
    'line\\n\\n.. list-table::\\n   :widths: 33 33 33\\n   :header-rows: 1\\n\\n\\n   * - A\\n     - x\\n     - +\\n\\n   * - BC\\n     - y z\\n     - 2\\n       3\\n\\n'
    >>> ''.join(tolisttable(data,join='001'))
    'line\\n\\n.. list-table::\\n   :widths: 33 33 33\\n   :header-rows: 1\\n\\n\\n   * - A\\n     - x\\n     - +\\n\\n   * - BC\\n     - yz\\n     - 2 3\\n\\n'
    >>> ''.join(tolisttable(data,join='0'))
    'line\\n\\n.. list-table::\\n   :widths: 33 33 33\\n   :header-rows: 1\\n\\n\\n   * - A\\n     - x\\n     - +\\n\\n   * - BC\\n     - yz\\n     - 23\\n\\n'

    """
    grid = False
    insert = False
    gridtable = []
    header = lambda line: line.startswith('+==')
    withheader = int(any([header(ln) for ln in data]))
    S = []
    isgridline = lambda line: line.startswith('+--') or header(line)
    def splitline(line): 
        st = 1
        sl = []
        for s in S:
            nst = len(s)+st
            sl.append(line[st:nst])
            st = nst+1
        return sl
    combine = {
            0:lambda e: [''.join([ee.strip() for ee in e]).strip()],
            1:lambda e: [' '.join([ee.strip() for ee in e]).strip()],
            2:lambda e: [ee[len(re.split('[^ ]',e[0])[0]):].rstrip() for ee in e]
            }
    for line in data:
        if isgridline(line):
            S = line.split('+')[1:-1]
            grid = True
            insert = True
            gridtable.append(line)
            col_num = line.count('+') - 1
            col_width = str(int(100 / col_num))
            col_width = (' ' + col_width) * col_num
        elif grid and line.startswith('|'):
            gridtable.append(line)
        else:
            grid = False
        if grid:
            if insert:
                insert = False
                output = []
                output = [combine[int(join[c]if c<len(join)else join[-1])](e) 
                    for c,e in enumerate(zip(*[splitline(line)
                    for line in gridtable if not isgridline(line)]))]
                clms = [(('       ' if j else ('     - ' if i else '   * - '))+xx) for i,x in enumerate(output) 
                    for j,xx in enumerate(x)]
                if len(gridtable)==1:
                    yield ".. list-table::\n"
                    yield "   :widths:{0}\n".format(col_width)
                    yield "   :header-rows: {0}\n".format(withheader)
                    clms += ['']
                for clm in clms:
                    yield clm + '\n'
                yield '\n'
                gridtable = []
        else:
            yield line

if __name__ == '__main__':
    import argparse
    import codecs
    import sys
    #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

    parser = argparse.ArgumentParser(prog="table", description='''Convert RST grid table to list-table.''')
    parser.add_argument('INPUT', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
    parser.add_argument('-j', '--join', action='store', default='012',
            help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')

    args = parser.parse_args()
    join = args.join
    for infile in args.INPUT:
        data = infile.readlines()
        for ln in tolisttable(data, join):
            sys.stdout.write(ln)

