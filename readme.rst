rstdoc
======

When installing via ``pip install rstdoc`` these files::

  dcx.py
  fromdocx.py
  listtable.py
  untable.py
  reflow.py
  retable.py
  vim_rst_tables.py

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

- ``rstfromdocx``: convert from docx using Pandoc, but additionally copying the images and helper files
- ``rstlisttable``, ``rstuntable``, ``rstreflow``, ``rstreimg``: post-processing a converted file
- ``rstretable``: RST table tools, used by ``vim_rst_tables`` for Vim

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


