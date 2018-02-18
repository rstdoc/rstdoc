#!/usr/bin/env python
# encoding: utf-8 

"""
In the ``.vimrc`` do::

    from rstdoc.vim_rst_tables import *

The the vim functions ``ReformatTable``, ``ReflowTable`` and ``ReTitle`` are available.
"""

import vim

from vim_bridge import bridged
from .retable import ReformatTable, ReflowTable, ReTitle, get_bounds

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
