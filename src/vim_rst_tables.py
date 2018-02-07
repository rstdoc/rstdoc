#!/usr/bin/env python
# encoding: utf-8 

import vim

from vim_bridge import bridged
from reflow import ReformatTable, ReflowTable

@bridged #makes ReformatTable vim function
def reformat_table():
    ReformatTable(vim.current.buffer,*vim.current.window.cursor)

@bridged #makes ReflowTable vim function
def reflow_table():
    ReflowTable(vim.current.buffer,*vim.current.window.cursor)

