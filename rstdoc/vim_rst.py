#!/usr/bin/env python
# encoding: utf-8 

"""
In the ``.vimrc`` do::

    from rstdoc.vim_rst import *

to import these python functions that work on the Vim buffer

- ``ReformatTable`` creates table around cursor from e.g. double space separated format
- ``ReflowTable`` adapts table around cursor to new first line
- ``ReTitle`` fixes the header underlines around cursor
- ``UnderLine`` and ``TitleLine`` for titles and headings
- ``RstDcxInit``: cd, then it will create a sample tree structure
- ``RstDcx``: will update link and tag files starting from current dir
- ``ListTable``: convert grid tables to list-table

A sample configuration in the vimrc::

  " let mapleader = ","
  " let maplocalleader = ","
  py3 << EOF
  from rstdoc.vim_rst import *
  EOF
  nnoremap <silent> <leader>etf :py3 ReformatTable()<CR>
  nnoremap <silent> <leader>etr :py3 ReflowTable()<CR>
  nnoremap <silent> <leader>ett :py3 ReTable()<CR>
  command! -narg=1 U py3 UnderLine(<f-args>) 
  command! -narg=1 T py3 TitleLine(<f-args>) 

Example::

      Column 1  Column 2
      Foo    Put two (or more) spaces as a field separator.
      |Bar|  Even very very long lines |like| these are fine, as long as you do not put in line endings here.
      Qux    This is the last line.

``,etf`` should reformat to::

      +----------+----------------------------------------------------------+
      | Column 1 | Column 2                                                 |
      +==========+==========================================================+
      | Foo      | Put two (or more) spaces as a field separator.           |
      +----------+----------------------------------------------------------+
      | |Bar|    | Even very very long lines |like| these are fine, as long |
      |          | as you do not put in line endings here.                  |
      +----------+----------------------------------------------------------+
      | Qux      | This is the last line.                                   |
      +----------+----------------------------------------------------------+

Change the number of "-" in the top line,
then ``,etr`` should adapt the rest to those widths.

"""

import vim
from pathlib import Path

from .retable import reformat_table, reflow_table, re_title, get_bounds
from .dcx import main as dcx
from .listtable import gridtable

def get_table_bounds():
    row,col = vim.current.window.cursor
    row,col,m = get_bounds(vim.current.buffer,row-1,col-1)
    return row+1,col+1,m

def ReformatTable():
    row,col = vim.current.window.cursor
    reformat_table(vim.current.buffer,row-1,col-1,1)

def ReflowTable():
    row,col = vim.current.window.cursor
    reflow_table(vim.current.buffer,row-1,col-1)

def ReTitle():
    row,col = vim.current.window.cursor
    re_title(vim.current.buffer,row-1,col-1)

def UnderLine(chr):
    #chr='='
    pos=vim.current.window.cursor[0]-1
    cline=vim.current.buffer[pos]
    nl=chr*len(cline)
    vim.current.buffer[pos:pos+1] = [cline,nl]

def TitleLine(chr):
    #chr='='
    pos=vim.current.window.cursor[0]-1
    cline=vim.current.buffer[pos]
    nl=chr*len(cline)
    vim.current.buffer[pos:pos+1] = [nl,cline,nl]

def RstDcxInit():
    dcx(root='.',verbose=False)
    
def RstDcx():
    dcx(root=None,verbose=False)
    tags=','.join([str(x.absolute()) for x in Path('.').glob("**/.tags")])
    vim.eval('''execute("set tags=./.tags,.tags,'''+tags.replace('\\','/')+'")')

def ListTable(join):
    c_r=vim.current.range
    #lns=vim.current.buffer[c_r[0]:c_r[1]+1]
    #print(c_r[:])
    lt = list(gridtable(c_r[:],join))
    vim.current.buffer[c_r.start:c_r.end+1] = lt

