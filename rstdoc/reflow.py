#!/usr/bin/env python
# encoding: utf-8 

"""
Reflow tables and paragraphs.
"""

import re
from textwrap import wrap
from listtable import gridtable, row_to_listtable
from retable import retable, titlerex, ReTitle

_pgrphrex=[
        re.compile(r'\s+'),
        re.compile(r'\s*-\s'),
        re.compile(r'\s*\*\s'),
        re.compile(r'\s*\w\.\s'),
        re.compile(r'\s*#\.\s'),
        re.compile(r'\s*:\w\+:\s'),
        ]

def reflowparagraph(p, sentence=False):
    if p:
        if len(p)==3 and titlerex.match(p[0]) and titlerex.match(p[2]) or len(p)==2 and titlerex.match(p[1]):
            ReTitle(p,0,0)
            yield from p
        elif p[0][0] == '=': #simple table
            yield from p
        elif len(p[0])>3 and p[0][0:3]=='.. ': #directive, comment
            yield from p
        else:
            st = 0
            mo = ''
            for rp in _pgrphrex:
                m = rp.match(p[0])
                if m:
                    st = m.span()[1]
                    mo = m.group(0)
                    break
            if p[0] and st < len(p[0]) and p[0][st] in '|+':
                yield from p
            else:
                if sentence:
                    txt = ' '.join([p[0][st:]]+[pp.strip() for pp in p[1:]])
                    wraptxt = []
                    for ph in txt.split('. '):
                        wraptxt.extend(wrap(ph))
                        wraptxt[-1]+='.'
                    else:
                        wraptxt[-1]=wraptxt[-1][:-1]
                else:
                    txt = '\n'.join([p[0][st:]]+[pp.strip() for pp in p[1:]])
                    wraptxt = wrap(txt)
                lmo = 0
                for tl in wraptxt:
                    if not lmo:
                        yield mo+tl
                        lmo = len(mo)
                    else:
                        yield ' '*lmo+tl
        del p[:]

def reflowparagraphs(data,sentence=False):
    #yield from data
    p = []
    literal = False
    reflowp = lambda p: reflowparagraph(p,sentence)
    re_literal = re.compile('^(?!\.\. ).*::\s*$')
    for dd in data:
        if dd.strip() == '':
            dds = ['']
        else:
            dds = dd.splitlines()
        for d in dds:
            if literal and d and d[0]!=' ':
                p.append(d)
                literal = False
            elif literal:
                yield d
            elif re_literal.search(d):
                p.append(d)
                yield from reflowp(p)
                literal = True
            else:
                dstrip = d.strip()
                if not dstrip:
                    yield from reflowp(p)
                    yield d
                elif any([rp.match(dstrip) for rp in _pgrphrex]):
                    yield from reflowp(p)
                    p.append(d)
                else:
                    p.append(d)
    yield from reflowp(p)

def rmextrablankline(data):
    bk = 0
    for d in data:
        if not d.strip():
            bc = bc+1
        else:
            bc = 0
        if bc < 3:
            yield d

def no3star(data):
    for d in data:
        yield d.replace('***','**')

def noblankend(data):
    nbe = re.compile('\s+$')
    for d in data:
        yield nbe.sub('',d)

class reflowrow():
    def __init__(self):
        self.tbl = []
    def __call__(self,row,colwidths,withheader,join,tableend):
        for lne in row_to_listtable(row,colwidths,withheader,join,tableend):
            if not tableend or lne.strip():
                self.tbl.append(lne)
        if tableend:
            yield from retable(self.tbl)
            del self.tbl[:]

def reflow(data,join='1',sentence=False):
    r = reflowrow()
    for ln in noblankend(
            no3star(
                rmextrablankline(
                    reflowparagraphs(
                        gridtable(data, join, r),
                        sentence
                        )
                    )
                )
            ):
        yield ln+'\n'


if __name__ == '__main__':
    import codecs
    import sys
    import argparse

    #'≥'.encode('cp1252') # UnicodeEncodeError on Windows, therefore...
    #makes problems with pdb, though
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

    parser = argparse.ArgumentParser(prog="rstreflow", 
        description='''Reflow paragraphs and tables, for the latter using join as for listtable''')
    parser.add_argument('INPUT', type=argparse.FileType('r',encoding='utf-8'), nargs='+', help='RST file(s)')
    parser.add_argument('-j', '--join', action='store', default='012',
            help='''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join''')
    parser.add_argument('-s', '--sentence', action='store_true', default=False,
            help='''Break lines at the end of sentences.''')

    args = parser.parse_args()
    join = args.join
    for infile in args.INPUT:
        data = infile.readlines()
        for ln in reflow(data,join):
            sys.stdout.write(ln)

