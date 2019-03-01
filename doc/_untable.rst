
.. _`rstuntable`:

rstuntable
==========

rstuntable: shell command
untable: rstdoc module

Convert tables of following format to paragraphs with an ID.
The '-' in ID is removed and the ID is made lower case.
**Bold** is removed.

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - **ID-XY-00**
     - text goes here

   * - **ID-XY-01**
     - text again goes here


If the first entry does contain no word chars or spaces between words,
then the table stays. For a different behavior replace paragraph23.

A file produced from a docx using pandoc or ``fromdocx.py`` will
need a pre-processing via ``rstlisttable`` to convert grid tables to ``list-table`` tables.
This is done in one step with ``rstfromdocx -lu doc.rst``.

