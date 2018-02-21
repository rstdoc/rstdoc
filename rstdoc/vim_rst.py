#!/usr/bin/env python
# encoding: utf-8 

"""
In the ``.vimrc`` do::

    import rstdoc.vim_rst

Then these vim functions will be defined:

- ``ReformatTable`` from e.g. double space separated format (by cursor pos, not '<,'>)
- ``ReflowTable`` adapts to new first line (by cursor pos, not '<,'>)
- ``ReTitle`` fixes the header underlines (by cursor pos, not '<,'>)
- ``UnderLine`` and ``TitleLine`` for titles and headings
- ``RstDcxInit``: cd, then it will create a sample tree structure
- ``RstDcx``: will update link and tag files starting from current dir
- ``ListTable``: convert grid tables to list-table

A sample configuration in the vimrc::


"""

import vim
from pathlib import Path

from vim_bridge import bridged
from .retable import ReformatTable, ReflowTable, ReTitle, get_bounds
from .dcx import main as dcx
from .listtable import gridtable

def get_table_bounds():
    row,col = vim.current.window.cursor
    row,col,m = get_bounds(vim.current.buffer,row-1,col-1)
    return row+1,col+1,m

@bridged #makes ReformatTable vim function
def reformat_table():
    row,col = vim.current.window.cursor
    ReformatTable(vim.current.buffer,row-1,col-1,1)

@bridged #makes ReflowTable vim function
def reflow_table():
    row,col = vim.current.window.cursor
    ReflowTable(vim.current.buffer,row-1,col-1)

@bridged #makes ReTitle vim function
def re_title():
    row,col = vim.current.window.cursor
    ReTitle(vim.current.buffer,row-1,col-1)

@bridged
def under_line(chr):
    #chr='='
    pos=vim.current.window.cursor[0]-1
    cline=vim.current.buffer[pos]
    nl=chr*len(cline)
    vim.current.buffer[pos:pos+1] = [cline,nl]

@bridged
def title_line(chr):
    #chr='='
    pos=vim.current.window.cursor[0]-1
    cline=vim.current.buffer[pos]
    nl=chr*len(cline)
    vim.current.buffer[pos:pos+1] = [nl,cline,nl]

@bridged
def rst_dcx_init():
    dcx(root='.',verbose=False)
    
@bridged
def rst_dcx():
    dcx(root=None,verbose=False)
    tags=','.join([str(x.absolute()) for x in Path('.').glob("**/.tags")])
    vim.eval('''execute("set tags=./.tags,.tags,'''+tags.replace('\\','/')+'")')

@bridged
def list_table(join):
    s,e=vim.current.range.start,vim.current.range.end
    print(s,e)
    lns = ["xxx"]*10
    lt = list(gridtable(lns,join))
    #vim.current.buffer[vim.current.range.start:vim.current.range.end+1] = lt


+-------+-------+
| xa    | xb    |
+=======+=======+
| xa    | xb    |
+-------+-------+
| xa    | xb    |
+-------+-------+
| xa    | xb    |
+-------+-------+

