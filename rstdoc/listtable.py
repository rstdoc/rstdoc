#!/usr/bin/env python
# encoding: utf-8 

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

combine = {
        0:lambda e: [''.join([ee.strip() for ee in e]).strip()],
        1:lambda e: [' '.join([ee.strip() for ee in e]).strip()],
        2:lambda e: [ee[len(re.split('[^ ]',e[0])[0]):].rstrip() for ee in e]
        }
_header = lambda line: line.startswith('+==')
_isgridline = lambda line: line.startswith('+--') or _header(line)
def row_to_listtable(row,colwidths,withheader,join,tableend):
    nColumns = len(colwidths)
    def splitline(lne): 
        st = 1
        sl = []
        for s in colwidths:
            nst = s+st
            sl.append(lne[st:nst])
            st = nst+1
        return sl
    output = []
    output = [combine[int(join[c]if c<len(join)else join[-1])](e) 
        for c,e in enumerate(zip(*[splitline(lne)
        for lne in row if not _isgridline(lne)]))]
    clms = [(('       ' if j else ('     - ' if i else '   * - '))+xx) for i,x in enumerate(output) 
        for j,xx in enumerate(x)]
    if len(row)==1:
        colwidth = str(int(100 / nColumns))
        colwidth = (' ' + colwidth) * nColumns
        yield ".. list-table::\n"
        yield "   :widths:{0}\n".format(colwidth)
        yield "   :header-rows: {0}\n".format(withheader)
        clms += ['']
    for clm in clms:
        yield clm + '\n'
    yield '\n'

def gridtable(
        data #from file.readlines() or str.splitlines(True)
        ,join='012'
        ,process_row = row_to_listtable
        ):
    """Convert grid table to list table with same column number throughout.
    """
    grid = False
    insert = False
    row = []
    withheader = 0
    lendata=len(data)
    for iL,line in enumerate(data):
        if _isgridline(line):
            grid = True
            insert = True
            row.append(line)
        elif grid and line.strip().startswith('|'):
            row.append(line)
        else:
            grid = False
        if grid:
            if insert:
                insert = False
                if len(row)==1:
                    colwidths = [len(x) for x in line.split('+')[1:-1]]
                    withheader = 0
                    for t in range(iL,len(data)):
                        tL = data[t].strip()
                        if tL[0]=='+': 
                            withheader = int(len(tL)>1 and tL[1]=='=')
                            break
                tableend = 1
                try:
                    tableend = int(data[iL+1].strip()[0] not in '+|')
                except: pass
                yield from process_row(row,colwidths,withheader,join,tableend)
                row = []
        else:
            yield line

def main():
    import argparse
    import codecs
    import sys
    #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

    parser = argparse.ArgumentParser(description='''Convert RST grid table to list-table.''')
    parser.add_argument('INPUT', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
    parser.add_argument('-j', '--join', action='store', default='012',
            help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')

    args = parser.parse_args()
    join = args.join
    for infile in args.INPUT:
        data = infile.readlines()
        for ln in gridtable(data, join):
            sys.stdout.write(ln)


if __name__ == '__main__':
    main()
