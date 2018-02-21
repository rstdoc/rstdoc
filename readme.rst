rstdoc
======

When installing via ``pip install rstdoc`` these files::

  dcx.py
  fromdocx.py
  listtable.py
  untable.py
  reflow.py
  retable.py
  vim_rst.py

and these scripts are installed::

  rstdcx
  rstfromdocx
  rstlisttable
  rstuntable
  rstreflow
  rstretable

The central tool is ``rstdcx`` or ``dcx.py``.
Following some conventions, 
explained by the example produced via ``rstdcx --init tmp``,
it supports documentation of (software) projects, by

- generating RST files from other files

- generating .tags to jump around using the Vim or Atom editor

- producing numbering for tables, figures and listings 
  consistent through docx, html and pdf by using ``|id|``
  defined in the generated ``_links_xxx.rst`` files.

The other files' purpose:

- ``fromdocx``  : Convert DOCX to RST using Pandoc and additionally copy the images and helper files 
- ``listtable`` : Convert RST grid tables to list-tables
- ``reflow``    : Reflow paragraphs and tables, for the latter using join as for listtable
- ``reimg``     : Rename images referenced in the RST file
- ``retable``   : Transforms list tables to grid tables
- ``untable``   : Converts certain column list-table (see paragraph23) to paragraphs
- ``vim_rst``   : provides RST handling to vim.

.. note::

   ``rstfromdocx -lurg doc.rst`` does all the post-processing in one step.

For those not using Vim a good alternative is the Atom editor, with these packages::

  atom-ctags  #better https://github.com/rpuntaie/atom-ctags
  language-restructuredtext
  rst-preview-pandoc
  table-editor
  rst-snippets
  atom-build       #better https://github.com/rpuntaie/atom-build
  atom-build-waf
  find-and-replace-under-cursor

``atom-build`` and ``atom-ctags`` were modified to allow finding files
by putting the relevant subdirectory into the project paths.

.. note::

   It is adviced to compare the output with the original and do some manual corrections here and there.


