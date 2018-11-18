
#def gen_tests(lns,**kw):
#    yield from doc_parts(lns)
#def gen_tests


# Mock out the vim library
import sys
sys.path = ['test/mocks'] + sys.path
import mock
import vim


'''

RST tables
``````````

These tests mostly originate from the history of `vim-rst-tables <https://github.com/ossobv/vim-rst-tables-py3>`_.


'''


vimvar = {}

def fake_eval(x):
    global vimvar
    return vimvar[x]

vim.eval = fake_eval
vim.current = mock.Mock()
vimvar['foo'] = 'bar'

# Begin normal module loading
import os
import unittest

# Load test subjects
from rstdoc.retable import (
    parse_table, draw_table, table_line, get_column_widths, create_rst_table,
    get_column_widths_from_border_spec, pad_fields, unify_table,
    join_rows, partition_raw_lines, split_row_into_lines, reflow_table,
    re_title,get_bounds,reformat_table, split_table_row, reflow_row_contents)

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

class TestRSTTableFormatter(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        # Default vim cursor for all tests is at line 4
        vim.current = mock.Mock()
        self.set_vim_cursor(4, 0)

    def tearDown(self):
        del vim.current

    def set_vim_cursor(self, row, col):
        vim.current.window.cursor = (row, col)

    def read_fixture(self, name):
        with open(os.path.join('test/fixtures/', name + '.txt'),encoding='utf-8') as fp:
            return fp.read().split('\n')

    def load_fixture_in_vim(self, name):
        vim.current.buffer = self.read_fixture(name)

    def ReflowTable_vim(self, expect, input):
        text_before_table = 'A piece of text before the table.\n\n'
        vim.current.buffer = (text_before_table + input).split('\n')

        ReflowTable()

        self.assertEqual(
            (text_before_table + expect).split('\n'),
            vim.current.buffer)

    def ReformatTable_vim(self, expect, input):
        text_before_table = 'A piece of text before the table.\n\n'
        vim.current.buffer = (text_before_table + input).split('\n')

        ReformatTable()

        self.assertEqual(
            (text_before_table + expect).split('\n'),
            vim.current.buffer)

    def split_table_row_equal(self, expect, input):
        self.assertEqual(expect, split_table_row(input))

    def testGetBounds(self):
        self.load_fixture_in_vim('default')
        self.assertEqual((3, 6, ''), get_table_bounds())

    def testGetBoundsOnBeginOfFile(self):
        self.load_fixture_in_vim('default')
        vim.current.window.cursor = (1, 0)
        self.assertEqual((1, 1, ''), get_table_bounds())

    def testGetBoundsOnEndOfFile(self):
        self.load_fixture_in_vim('default')
        vim.current.window.cursor = (8, 0)
        self.assertEqual((8, 9, ''), get_table_bounds())

    def testJoinSimpleRows(self):
        input_rows = [['x', 'y', 'z'], ['foo', 'bar']]
        expected = ['x\nfoo', 'y\nbar', 'z']
        self.assertEqual(expected, join_rows(input_rows))

        input_rows.append(['apple', '', 'pear'])
        expected = ['x foo apple', 'y bar', 'z pear']
        self.assertEqual(expected, join_rows(input_rows, sep=' '))

    def testPartitionRawLines(self):
        self.assertEqual([], partition_raw_lines([]))
        self.assertEqual([['']], partition_raw_lines(['']))
        self.assertEqual(
            [['foo'], ['bar']],
            partition_raw_lines(['foo', 'bar']))
        self.assertEqual(
            [['foo'], ['bar']],
            partition_raw_lines(['foo', '+----+', 'bar']))
        self.assertEqual(
            [['foo', 'bar'], ['baz']],
            partition_raw_lines(['+-----+', 'foo', 'bar', '----', 'baz']))

    def testParseSimpleTable(self):
        self.assertEqual([['x y z']], parse_table(['x y z']))
        self.assertEqual([['x', 'y z']], parse_table(['x  y z']))
        self.assertEqual([['x', 'y', 'z']], parse_table(['x  y          z']))

    def testParseTable(self):
        self.load_fixture_in_vim('default')
        expected = [
            ['Column 1', 'Column 2'],
            ['Foo', 'Put two (or more) spaces as a field separator.'],
            ['|Bar|', (
                'Even very very long lines |like| these are fine, '
                'as long as you do not put in line endings here.')],
            ['Qux', 'This is the last line.'],
        ]
        self.assertEqual(expected, parse_table(vim.current.buffer[2:6]))

    def testParseTableUnifiesColumns(self):
        input = ['x  y', 'a  b    c', 'only one']
        expected = [['x', 'y', ''], ['a', 'b', 'c'], ['only one', '', '']]
        self.assertEqual(expected, parse_table(input))

    def testUnifyTables(self):
        input = [[' x ', '  y'], ['xxx', ' yyyy ', 'zz']]
        expected = [[' x ', '  y', ''], ['xxx', ' yyyy ', 'zz']]
        self.assertEqual(expected, unify_table(input))

    def testUnifyTablesRemovesEmptyColumns(self):
        input = [['x', '', 'y'], ['xxx', '', 'yyyy', 'zz', '         ']]
        expected = [['x', 'y', ''], ['xxx', 'yyyy', 'zz']]
        self.assertEqual(expected, unify_table(input))

    def testParseDealsWithSpacesAtLineEnd(self):
        input = ['x  y     ', 'a  b ', 'only one']
        expected = [['x', 'y'], ['a', 'b'], ['only one', '']]
        self.assertEqual(expected, parse_table(input))

    def testParseValidTable(self):
        input = ['+-----+----+',
                 '| Foo | Mu |',
                 '+=====+====+',
                 '| x   | y  |',
                 '+-----+----+']
        expect = [['Foo', 'Mu'], ['x', 'y']]
        self.assertEqual(expect, parse_table(input))

    def testParseCorruptedTable(self):
        input = ['+---+---------+',
                 '| Foo | Mu                   |',
                 '+=====+====+',
                 '| x   | This became somewhat larger  |',
                 'blah   | A new line | ',
                 '+-----+----+']
        expect = [['Foo', 'Mu'],
                  ['x\nblah', 'This became somewhat larger\nA new line']]
        self.assertEqual(expect, parse_table(input))

        input = ['+---+---------+',
                 '| Foo | Mu                   |',
                 '+=====+====+',
                 '| x   | This became somewhat larger  |',
                 'blah   | A new line | ',
                 '+-----+----+']
        expect = [['Foo', 'Mu'],
                  ['x\nblah', 'This became somewhat larger\nA new line']]
        self.assertEqual(expect, parse_table(input))

    def testParseMultiLineFields(self):
        input = """\
+-----+---------------------+
| Foo | Bar                 |
+=====+=====================+
| x   | This is a long line |
|     | that is spread out  |
|     | over multiple lines |
+-----+---------------------+""".split('\n')
        expect = [['Foo', 'Bar'],
                  ['x', (
                      'This is a long line\nthat is spread out\n'
                      'over multiple lines')]]
        self.assertEqual(expect, parse_table(input))

    def testSplitRowIntoLines(self):
        input = ['Foo', 'Bar']
        expect = [['Foo', 'Bar']]
        self.assertEqual(expect, split_row_into_lines(input))
        input = ['One\nTwo\nThree', 'Only one']
        expect = [['One', 'Only one'], ['Two', ''], ['Three', '']]
        self.assertEqual(expect, split_row_into_lines(input))
        input = ['One\n\n\nThree', 'Foo\nBar']
        expect = [['One', 'Foo'], ['', 'Bar'], ['', ''], ['Three', '']]
        self.assertEqual(expect, split_row_into_lines(input))

    def testSplitTableRow(self):
        self.split_table_row_equal(
            ['Foo Bar', 'Baz', '3'],
            'Foo Bar    Baz  3   ')
        self.split_table_row_equal(
            ['|replacement|', 'text'],
            '| |replacement| | text |')
        self.split_table_row_equal(
            ['', '|replacement| texts', 'more text'],
            '| | |replacement| texts | more text |')

    def testDrawMultiLineFields(self):
        input = [['Foo', 'Bar'],
                 ['x', ('This is a long line\nthat is spread out\n'
                        'over multiple lines')]]
        expect = """\
+-----+---------------------+
| Foo | Bar                 |
+=====+=====================+
| x   | This is a long line |
|     | that is spread out  |
|     | over multiple lines |
+-----+---------------------+""".split('\n')
        self.assertEqual(expect, draw_table('', input))

    def testTableLine(self):
        self.assertEqual('', table_line([], True))
        self.assertEqual('++', table_line([0], True))
        self.assertEqual('+++', table_line([0, 0], True))
        self.assertEqual('++-+', table_line([0, 1]))
        self.assertEqual('+===+', table_line([3], True))
        self.assertEqual('+===+====+', table_line([3, 4], True))
        self.assertEqual(
            '+------------------+---+--------------------+',
            table_line([18, 3, 20]))

    def testGetColumnWidths(self):
        self.assertEqual([], get_column_widths([[]]))
        self.assertEqual([0], get_column_widths([['']]))
        self.assertEqual([1, 2, 3], get_column_widths([['x', 'yy', 'zzz']]))
        self.assertEqual(
            [3, 3, 3],
            get_column_widths([
                ['x', 'y', 'zzz'], ['xxx', 'yy', 'z'], ['xx', 'yyy', 'zz']]))

    def testGetColumnWidthsForMultiLineFields(self):
        self.assertEqual(
            [3, 6],
            get_column_widths([['Foo\nBar\nQux', 'This\nis\nreally\nneat!']]))

    def testGetColumnWidthsFromBorderSpec(self):
        input = ['+----+-----+--+-------+',
                 '| xx | xxx |  | xxxxx |',
                 '+====+=====+==+=======+']
        self.assertEqual(
            [2, 3, 0, 5],
            get_column_widths_from_border_spec(input))

    def testPadFields(self):
        table = [['Name', 'Type', 'Description'],
                 ['Lollypop', 'Candy', 'Yummy'],
                 ['Crisps', 'Snacks', 'Even more yummy, I tell you!']]
        expected_padding = [
                 [' Name     ', ' Type   ', ' Description                  '],
                 [' Lollypop ', ' Candy  ', ' Yummy                        '],
                 [' Crisps   ', ' Snacks ', ' Even more yummy, I tell you! ']]
        widths = get_column_widths(table)
        for input, expect in zip(table, expected_padding):
            self.assertEqual(expect, pad_fields(input, widths))

    def testReflowRowContentsWithEnoughWidth(self):
        input = ['Foo\nbar', 'This line\nis spread\nout over\nfour lines.']
        expect = ['Foo bar', 'This line is spread out over four lines.']
        self.assertEqual(expect, reflow_row_contents(input, [99, 99]))

    def testReflowRowContentsWithWrapping(self):
        input = ['Foo\nbar', 'This line\nis spread\nout over\nfour lines.']
        expect = ['Foo bar', 'This line is spread\nout over four lines.']
        self.assertEqual(expect, reflow_row_contents(input, [10, 20]))

        input = ['Foo\nbar', 'This line\nis spread\nout over\nfour lines.']
        expect = ['Foo bar', 'This\nline\nis\nspread\nout\nover\nfour\nlines.']
        self.assertEqual(expect, reflow_row_contents(input, [10, 6]))

    def testReflowRowContentsWithoutRoom(self):
        # #FIXME#self.assertEqual(expect, reflow_row_contents(input))
        pass

    def testDrawTable(self):
        self.assertEqual([], draw_table('', []))
        self.assertEqual(['+--+', '|  |', '+==+'], draw_table('', [['']]))
        self.assertEqual(
            ['+-----+', '| Foo |', '+=====+'],
            draw_table('', [['Foo']]))
        self.assertEqual(
                ['+-----+----+',
                 '| Foo | Mu |',
                 '+=====+====+',
                 '| x   | y  |',
                 '+-----+----+'],
                draw_table('', [['Foo', 'Mu'], ['x', 'y']]))

    def testCreateTable(self):
        '''
        Test |retable.reformat_table| by creating a grid table from lines where columns are separated by two blanks.

        '''
        self.load_fixture_in_vim('default')
        expect = """\
This is paragraph text *before* the table.

+----------+--------------------------------------------------------------------------------------------------+
| Column 1 | Column 2                                                                                         |
+==========+==================================================================================================+
| Foo      | Put two (or more) spaces as a field separator.                                                   |
+----------+--------------------------------------------------------------------------------------------------+
| |Bar|    | Even very very long lines |like| these are fine, as long as you do not put in line endings here. |
+----------+--------------------------------------------------------------------------------------------------+
| Qux      | This is the last line.                                                                           |
+----------+--------------------------------------------------------------------------------------------------+

This is paragraph text *after* the table, with
a line ending.
""".split('\n')
        ReformatTable()
        self.assertEqual(expect, vim.current.buffer)

    def testCreateComplexTable(self):
        raw_lines = self.read_fixture('multiline-cells')
        # strip off the last (empty) line from raw_lines (since that line does
        # not belong to the table
        del raw_lines[-1]
        expect = """\
+----------------+---------------------------------------------------------------+
| Feature        | Description                                                   |
+================+===============================================================+
| Ease of use    | Drop dead simple!                                             |
+----------------+---------------------------------------------------------------+
| Foo            | Bar, qux, mux.                                                |
+----------------+---------------------------------------------------------------+
| Predictability | Lorem ipsum dolor sit amet, consectetur adipiscing elit;      |
+----------------+---------------------------------------------------------------+
|                | nullam congue dapibus aliquet. Integer ūt rhoncus leo. In hac |
+----------------+---------------------------------------------------------------+
|                | habitasse platea dictumst. Phasellus pretium iaculis.         |
+----------------+---------------------------------------------------------------+
            """.rstrip().splitlines()
        #expect
        pt = parse_table(raw_lines)
        dt = draw_table('', pt)
        self.assertEqual(expect, dt)

    def testReformatEmpty(self):
        '''
        Tests |retable.reformat_table| with a table with an empty cell.
        '''
        self.ReformatTable_vim("""\
+---+-----+---+
| A | B c | D |
+===+=====+===+
| 1 |     | 2 |
+---+-----+---+""","""\
A | B c | D
1 |  | 2""")

    def testReflowTable(self):
        '''
        Tests |retable.reflow_table| with a table whose start line was reduced.

        '''
        self.load_fixture_in_vim('reflow')
        expect = """\
This is paragraph text *before* the table.

+----------+--------------------------+
| Column 1 | Column 2                 |
+==========+==========================+
| Foo      | Put two (or more) spaces |
|          | as a field separator.    |
+----------+--------------------------+
| |Bar|    | Even very very long      |
|          | lines |like| these are   |
|          | fine, as long as you do  |
|          | not put in line endings  |
|          | here.                    |
+----------+--------------------------+
| Qux      | This is the last line.   |
+----------+--------------------------+

This is paragraph text *after* the table, with
a line ending.

""".split('\n')
        ReflowTable()
        self.assertEqual(expect, vim.current.buffer)

    def testReflowWithReplacements(self):
        '''
        Tests |retable.reflow_table| with a table containing replacement substitutions
        with successive rows reduced in length.
        '''
        # The first border decides the table size.
        self.ReflowTable_vim("""\
+--------------------+-----+-----+-----+
| **Services**       | 0   | 1   | 2   |
+====================+=====+=====+=====+
| VPN Service        | |O| | |O| | |X| |
+--------------------+-----+-----+-----+""", """\
+--------------------+-----+-----+-----+
| **Services**       | 0 | 1 | 2 |
+====================+===+===+===+
| VPN Service        | |O| | |O| | |X| |
+--------------------+---+---+---+""")

    def testReflowWithLineBreak(self):
        '''
        Tests |retable.reflow_table| with a successive line lengthened.
        '''
        self.ReflowTable_vim(
            expect="""\
+-----------------+-----------------+-----------------+
| Name /          | Organisation    | Action          |
| Distribution to |                 |                 |
+-----------------+-----------------+-----------------+""",
            input="""\
+-----------------+-----------------+-----------------+
| Name /          | Organisation       | Action          |
| Distribution to |                 |                 |
+-----------------+-----------------+-----------------+"""
            )
    def testReTitle(self):
        '''
        Tests |retable.re_title| on a fixture file.
        '''
        self.load_fixture_in_vim('retitle')
        self.set_vim_cursor(1,1)
        ReTitle()
        self.set_vim_cursor(6,0)
        ReTitle()
        self.set_vim_cursor(10,0)
        ReTitle()
        self.set_vim_cursor(12,0)
        ReTitle()
        self.set_vim_cursor(15,0)
        ReTitle()
        expect = """\
====
This
====

----------
is a title
----------

Title
=====

and sub title
-------------

Qux
---
""".split('\n')
        self.assertEqual(expect, vim.current.buffer)

    def testCreateFromData(self):
        '''
        Tests creation of table from data (|retable.create_rst_table|).
        '''
        lns=[['one','two','three'],[1,2,3]]
        self.assertEqual(create_rst_table(lns), """\
+-----+-----+-------+
| one | two | three |
+-----+-----+-------+
| 1   | 2   | 3     |
+-----+-----+-------+""")
