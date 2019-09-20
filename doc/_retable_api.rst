API
---


.. code-block:: py

   import rstdoc.retable as retable



.. _`retable.title_some`:

:retable.title_some:

.. code-block:: py

   title_some = """=-^"'`._~+:;,"""

The rst title order was partly taken from https://github.com/jimklo/atom-rst-snippets
then converted to http://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html

.. _`retable.reformat_table`:

:retable.reformat_table:

.. code-block:: py

   def reformat_table(lines, row=0, col=0, withheader=0):

Create or reformat a grid table in lines.
The table is delimited by emtpy lines starting from (row,col).

:param lines: list of strings
:param row: of cursor position,
:param col: ... as only the lines delimited by an empty line are used
:param withheader: user the first line as table header


.. _`retable.create_rst_table`:

:retable.create_rst_table:

.. code-block:: py

   def create_rst_table(data, withheader=0):

Create a rst table from data

Example::

    >>> lns=[['one','two','three'],[1,2,3]]
    >>> create_rst_table(lns)
    '+-----+-----+-------+\n| one | two | three |\n+-----+-----+-------+\n| 1   | 2   | 3     |\n+-----+-----+-------+'

:param data: list of list of data


.. _`retable.reflow_table`:

:retable.reflow_table:

.. code-block:: py

   def reflow_table(lines, row=0, col=0):

Adapt an existing table to the widths of the first line.
The table is delimited by emtpy lines starting from (row,col).

lines: list of strings
row: of cursor position,
col: ... as only the lines delimited by an empty line are considered


.. _`retable.re_title`:

:retable.re_title:

.. code-block:: py

   def re_title(lines, row=0, col=0, down=0):

Adjust the under- or overline of a title.

:param lines: list of lines
:param row: of cursor position,
:param col: ... as only the lines delimited by an empty line are considered
:param down: >0down, <0up

::

    >>> lines="""\
    ...   ###########
    ...       title
    ...   ###########
    ...   """.splitlines()
    >>> re_title(lines)
    >>> lines
    ['      #####', '      title', '      #####', '  ']



.. _`retable.retable`:

:retable.retable:

.. code-block:: py

   def retable(lns):

Transform listtable to grid table.
Yield the resulting lines.

:param lns: list of strings


.. _`retable.main`:

:retable.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstretable| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

``rstfile`` is the file name

``in_place`` defaults to False

