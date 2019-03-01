API
---

.. code-block:: py

   import rstdoc.untable as untable


.. _`untable.paragraph23`:

:untable.paragraph23:

.. code-block:: py

   def paragraph23(row, nColumns, org, islast, withheader):

For process_row parameter of ``untable``. 

For a table of 2 or 3 columns, transform to text.
The first column must hold only one line for an ID.

If not transformed to paragraph, then the orginal text (org) is yielded.

:param row: list of strings representing the row
:param nColumns: number of columns in the table
:param org: orginal text
:param islast: this call is with the last table entry
:param withheader: the table has a header line


.. _`untable.untable`:

:untable.untable:

.. code-block:: py

   def untable(lns, process_row=paragraph23):

Transform a RST list-table to normal paragraphs.
The table is supposed to have this format:

- The first column holds an ID.
- Optionally the second column holds keywords.
- The last column holds the details.

:param lns: list of strings
:param process_row: called for each row to transform to paragraph


.. _`untable.main`:

:untable.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstuntable| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

``rstfile`` is the file name

``in_place`` defaults to False

