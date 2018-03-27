#!/usr/bin/env python
# encoding: utf-8 

#def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
#def gen_head(lns,**kw)

"""

.. _`untable`:

rstuntable, untable.py
======================

Convert tables of following format to paragraphs with an ID.
The '-' in ID is removed and the ID is made lower case.
**Bold** is removed.

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - **ID-XY-00**
     - text goes here

   * - **ID-XY-01**
     - text again goes here


If the first entry does contain no word chars or spaces between words,
then the table stays. For a different behavior replace paragraph23.

A file produced from a docx using pandoc or ``fromdocx.py`` will
need a pre-processing via ``rstlisttable`` to convert grid tables to ``list-table`` tables.
This is done in one step with ``rstfromdocx -lu doc.rst``.

"""

import re
from textwrap import wrap

_no = None
def paragraph23(row,nColumns,org,islast,withheader):
    """Sample process_row function If not transformed to paragraph, then org must be yielded.

    This expects 3 columns and the first must have only one line, which holds an ID.
    """
    #import pdb; pdb.set_trace()
    strp = lambda rr: ' '.join([r.strip() for r in rr])
    global _no
    if _no!=None and _no:
        yield from org
    elif (_no!=None and not _no) or (_no==None and (nColumns == 2 or nColumns == 3) and len(row[0])==1):
        id = strp(row[0]).lower().replace('-','').replace('*','')

        row1=row[-1][:]
        while row1 and not row1[-1].strip():
            del row1[-1]
        if not row1:
            row1 = ['']

        if _no==None and (not re.search('\w',id) or ' ' in id.strip() or (len(row1)==1 and row1[0].startswith('*'))):
            _no = True
            yield from org
        else:
            _no = False
            if id:
                id = id.replace(' ','')
                yield '.. _`{}`:'.format(id)
                yield ''
                yield '{0}:'.format(id)
                yield ''
            if nColumns == 3:
                l1 = strp(row[1])
                for w in wrap(l1):
                    yield l1
                yield ''
                idx = 2
            else:
                idx = 1
            for r in row[idx]:
                yield r.strip()
    else:
        yield from org
    if islast:
        _no = None
    del org[:]

tblre = [
    re.compile(r'^\s+')
    ,re.compile(r'^\s+:')
    ,re.compile(r'^\s+\* -')
    ,re.compile(r'^\s+-')
    ]
def refindE(res,ln):
    #are=tblre[0]
    for are in res:
        m = are.search(ln)
        if m:
            yield m.span()[1]
        else:
            yield -1
def untable(data,process_row=paragraph23):
    hT = -1
    nColumns = 0
    row = []
    rowc = None
    org = []
    endT = False
    indE = len(".. * -")
    withheader = 0
    for ln in data:
        if hT==-1:
            hT = ln.find('.. list-table')
            if hT > -1:
                org.append(ln)
            else: 
                yield ln
        else:
            lnstrp = len(ln.strip())
            ind = list(refindE(tblre,ln))
            chk = [ind[0] >= hT+indE+1, ind[1] >= hT+3, ind[2] == hT+indE, ind[3] == hT+indE, lnstrp == 0]
            endT = not any(chk)
            if chk[1]:
                #ln='ss'
                hr = ln.split(':header-rows:')
                if len(hr)>1:
                    withheader = int(hr[1])
            if endT:
                if rowc != None:
                    row.append(rowc)
                    yield from process_row(row,nColumns,org,True,withheader)
                withheader = 0
                hT=-1
                nColumns=0
                row=[]
                rowc = None
                del org[:]
                yield ln
                continue
            elif chk[2]:
                if rowc != None:
                    row.append(rowc)
                    yield from process_row(row,nColumns,org,False,withheader)
                rowc = [ln[ind[2]+1:]]
                org.append(ln)
                row = []
                nColumns = 1
            elif chk[3]:
                row.append(rowc)
                rowc = [ln[ind[3]+1:]]
                org.append(ln)
                nColumns += 1
            elif rowc != None:
                rowc.append(ln)
                org.append(ln)
            else:
                org.append(ln)
    if rowc and not endT:
        row.append(rowc)
        yield from process_row(row,nColumns,org,True,withheader)

def main(**args):
    import codecs
    import sys
    import argparse

    if not args:
        parser = argparse.ArgumentParser(description='''Converts certain column list-table (see paragraph23) to paragraphs.''')
        parser.add_argument('INPUT', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
        parser.add_argument('-i', '--in-place', action='store_true', default=False,
                help='''change the file itself''')
        args = parser.parse_args().__dict__

    for infile in args['INPUT']:
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
            f.writelines(untable(data))
        finally:
            if args['in_place']:
                f.close()

if __name__ == '__main__':
    main()

