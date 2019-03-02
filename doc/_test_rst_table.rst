
RST tables
``````````

These tests mostly originate from the history of `vim-rst-tables <https://github.com/ossobv/vim-rst-tables-py3>`_.



.. _`testCreateTable`:

:testCreateTable:

Test |retable.reformat_table| by creating a grid table from lines where columns are separated by two blanks.


.. _`testReformatEmpty`:

:testReformatEmpty:

Tests |retable.reformat_table| with a table with an empty cell.

.. _`testReflowTable`:

:testReflowTable:

Tests |retable.reflow_table| with a table whose start line was reduced.


.. _`testReflowWithReplacements`:

:testReflowWithReplacements:

Tests |retable.reflow_table| with a table containing replacement substitutions
with successive rows reduced in length.

.. _`testReflowWithLineBreak`:

:testReflowWithLineBreak:

Tests |retable.reflow_table| with a successive line lengthened.

.. _`testReTitle`:

:testReTitle:

Tests |retable.re_title| on a fixture file.

.. _`testCreateFromData`:

:testCreateFromData:

Tests creation of table from data (|retable.create_rst_table|).
