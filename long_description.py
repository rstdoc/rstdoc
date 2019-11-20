#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
from os.path import abspath, dirname, join
from tempfile import NamedTemporaryFile
import subprocess as sp

here = abspath(dirname(__file__))
try:
    sys.path.append(join(here, 'rstdoc'))
    from dcx import dorst
except:
    try:
        from rstdoc.dcx import dorst
    except:
        def dorst(linelist):
            return linelist

def read(fname, separator='\n"""'):
    with open(join(here, fname),
              encoding='utf-8') as f:
        return f.read().split(separator)[1]


long_description = '\n'.join([
    open('readme.rst').read(),
    read('rstdoc/dcx.py'),
    read('rstdoc/dcx.py', separator="'''\\").split("'''")[0],
    read('rstdoc/fromdocx.py'),
    read('rstdoc/listtable.py'),
    read('rstdoc/untable.py'),
    read('rstdoc/reflow.py'),
    read('rstdoc/reimg.py'),
    read('rstdoc/retable.py')
    ])

long_description = ''.join([x for i,x in enumerate(
                        dorst(long_description.splitlines()))
                        if not x.startswith('.. _`') and i>0])


if __name__ == '__main__':
    try:
        assert sys.argv[1] == '--check'
        with NamedTemporaryFile(suffix='.rst') as f:
            f.write(long_description.encode('utf-8'))
            sp.run('restview --pypi-strict '+f.name,shell=True)
    except Exception as err:
        try:
            sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
        except:
            pass
        print(long_description)
