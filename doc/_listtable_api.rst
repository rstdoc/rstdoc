API
---


.. code-block:: py

   import rstdoc.listtable as listtable



.. _`listtable.row_to_listtable`:

:listtable.row_to_listtable:

.. code-block:: py

   def row_to_listtable(
           row ,colwidths ,withheader ,join ,indent ,tableend
       ):

This is the default ``process_row`` parameter of |listtable.gridtable|.

:param row: list of cells for the row
:param colwidths: The widths of the columns
:param withheader: produce :header-:param rows: 1
:param join: 0,1,2 telling how to combine the lines of a cell

- 0 = without space
- 1 = with space
- 2 = keep multi-line

:param indent: indentation of the table
:param tableend: True, if end of table



.. _`listtable.gridtable`:

:listtable.gridtable:

.. code-block:: py

   def gridtable(
           data ,join='012' ,process_row=row_to_listtable
       ):

Convert grid table to list table with same column number throughout.
See |listtable.row_to_listtable|.

:param data: from file.readlines() or str.splitlines(True)
:param join: join column 0 without space, column 1 with space and leave the rest as-is
:param process_row: creates a list-table entry for the row

.. _`listtable.main`:

:listtable.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstlisttable| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

``rstfile`` is the file name

``in_place`` defaults to False

``join`` defaults to "012"


