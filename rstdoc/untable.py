#!/usr/bin/env python
# encoding: utf-8 

#test with
#py.test --doctest-modules untable.py

"""
Convert tables of following format to paragraphs with an ID.
The '-' in ID is removed and the ID is made lower case.
**Bold** is removed.

A file produced from a docx using pandoc or ``fromdocx.py`` will
need a pre-processing via ``listtable.py`` to convert grid tables to ``list-table`` tables.

"""

import re
from textwrap import wrap

def paragraph23(row,nColumns,org,islast,withheader):
    """Sample process_row function If not transformed to paragraph, then org must be yielded.

    This expects 3 columns and the first must have only one line, which holds an ID.
    """
    #import pdb; pdb.set_trace()
    strp = lambda rr: ' '.join([r.strip() for r in rr])
    if (nColumns == 2 or nColumns == 3) and len(row[0])==1:
        id = strp(row[0]).lower().replace('-','').replace('*','')
        yield '.. _`{}`:\n\n'.format(id)
        yield '{0}:\n\n'.format(id)
        if nColumns == 3:
            l1 = strp(row[1])
            for w in wrap(l1):
                yield l1+'\n'
            yield '\n'
            idx = 2
        else:
            idx = 1
        for r in row[idx]:
            yield r.strip()+'\n'
    else:
        yield from org
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

def main():
    import codecs
    import sys
    import argparse

    #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...
    #makes problems with pdb, though
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

    parser = argparse.ArgumentParser(description='''Converts 3 column list-table entries to paragraphs and leaves the rest unchanged.''')
    parser.add_argument('INPUT', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')

    args = parser.parse_args()
    for infile in args.INPUT:
        data = infile.readlines()
        for ln in untable(data):
            sys.stdout.write(ln)

if __name__ == '__main__':
    main()

