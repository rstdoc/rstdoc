#!/usr/bin/env python
# encoding: utf-8 

#def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
#def gen_head(lns,**kw)
#def gen_api(lns,**kw):
#    yield from doc_parts(lns,signature='py',prefix='listtable.')
#def gen_api

"""

.. _`rstlisttable`:

rstlisttable
============

rstlisttable: shell command
listable: rstdoc module

Convert RST grid tables to list-tables.

Usage
-----

#. Convert grid tables in a file to list-tables. The result is output to stdout::

      $ listtable.py input.rst

#. Convert several files::

      $ listtable.py input1.rst input2.rst
      $ listtable.py *.rst

#. Use pipe (but ``cat`` might not keep the encoding)::

      $ cat in.rst | listtable.py -  | untable.py - > out.rst

Options
-------
-j, --join       e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join

"""



#''' starts api doc parts (see doc_parts())
'''
API
---


.. code-block:: py

   import rstdoc.listtable as listtable


'''

import re

def combine2(e):
    res = [ee[len(re.split('[^ ]',e[0])[0]):].rstrip() for ee in e]
    while res and not res[-1].strip():
        del res[-1]
    if not res:
        res = ['']
    return res

combine = {
        0:lambda e: [''.join([ee.strip() for ee in e]).strip()],
        1:lambda e: [' '.join([ee.strip() for ee in e]).strip()],
        2:combine2
        }
_header = lambda line: line.startswith('+==')
_isgridline = lambda line: line.startswith('+--') or _header(line)
def row_to_listtable(
        row #list of cells for the row
        ,colwidths #The widths of the columns
        ,withheader #produce :header-rows: 1
        ,join #0,1,2 telling how to combine the lines of a cell
        ,indent #indentation of the table
        ,tableend #True, if end of table
        ):
    '''
    This is the default ``process_row`` parameter of |listtable.gridtable|.

    join: join lines of cell with

    - 0 = without space 
    - 1 = with space
    - 2 = keep multi-line

    '''
    nColumns = len(colwidths)
    def splitline(lne): 
        st = indent + 1
        sl = []
        for s in colwidths:
            nst = s+st
            sl.append(lne[st:nst])
            st = nst+1
        return sl
    output = []
    output = [combine[int(join[c]if c<len(join)else join[-1])](e) 
        for c,e in enumerate(zip(*[splitline(lne)
            for lne in row if not _isgridline(lne[indent:])]))]
    clms = [(('       ' if j else ('     - ' if i else '   * - '))+xx) for i,x in enumerate(output) 
        for j,xx in enumerate(x)]
    indentstr = ' '*indent
    if len(row)==1:
        colwidth = str(int(100 / nColumns))
        colwidth = (' ' + colwidth) * nColumns
        yield indentstr+".. list-table::\n"
        yield indentstr+"   :widths:{0}\n".format(colwidth)
        yield indentstr+"   :header-rows: {0}\n".format(withheader)
        clms += ['']
    for clm in clms:
        yield indentstr + clm + '\n'
    yield indentstr+'\n'

def gridtable(
        data #from file.readlines() or str.splitlines(True)
        ,join='012' #join column 0 without space, column 1 with space and leave the rest as-is
        ,process_row=row_to_listtable #creates a list-table entry for the row
        ):
    '''
    Convert grid table to list table with same column number throughout.
    See |listtable.row_to_listtable|.
    '''
    grid = False
    insert = False
    row = []
    withheader = 0
    lendata=len(data)
    indent = 0
    for iL,line in enumerate(data):
        if _isgridline(line.strip()):
            indent = re.search('\s*',line).span()[1]
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
                yield from process_row(row,colwidths,withheader,join,indent,tableend)
                row = []
                indent = 0
        else:
            yield line

def main(
        **args #keyword arguments. If empty the arguments are taken from ``sys.argv``.
        ):
    '''
    This corresponds to the |rstlisttable| shell command.

    ``rstfile`` is the file name

    ``in_place`` defaults to False

    ``join`` defaults to "012"

    
    '''
    import argparse
    import codecs
    import sys

    if not args:
        parser = argparse.ArgumentParser(description='''Convert RST grid tables to list-tables.''')
        parser.add_argument('rstfile', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
        parser.add_argument('-j', '--join', action='store', default='012',
                help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')
        parser.add_argument('-i', '--in-place', action='store_true', default=False,
                help='''change the file itself''')
        args = parser.parse_args().__dict__

    if not 'in_place' in args: args['in_place'] = False
    if not 'join' in args: args['join'] = '012'

    if isinstance(args['rstfile'],str): args['rstfile'] = [argparse.FileType('r',encoding='utf-8')(args['rstfile'])]

    for infile in args['rstfile']:
        data = infile.readlines()
        infile.close()
        if args['in_place']:
            f = open(infile.name,'w',encoding='utf-8',newline='\n')
        else:
            #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...  makes problems with pdb, though
            sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
            sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
            f = sys.stdout
        try:
            f.writelines(gridtable(data,args['join']))
        finally:
            if args['in_place']:
                f.close()


if __name__ == '__main__':
    main()
