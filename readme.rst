rstdoc
======

`Sphinx`_ is an extension of `Docutils`_ used for many (software) projects,
but it does not support creation of `DOCX`_ files.
`Pandoc`_ does support `DOCX`_, but does not support the `Sphinx`_ extensions.

`rstdoc`_ supports working with basic ``restructuredText`` (`RST`_) 
defined by `Docutils`_ using some conventions, like  
``.rest`` files become ``.docx`` and ``.rst`` is used for included files.
The conventions are shown by the example produced via ``rstdcx --init samplerstdoc``,

The idea is, that working with text is more integrated in the 
(software) development process.

``rstdoc``'s script ``rstdcx`` (using module ``dcx.py``) 

- generates ``.tags`` files to jump around in an editor that support `ctags`_
  (Vim, Atom, VsCode, Emacs, ...)

- produces numbering for tables, figures and code listings 
  consistent through docx, html and pdf by using ``|id|``
  defined in the generated ``_links_xxx.rst`` files.

``pip install rstdoc`` installs:

  +-----------+--------------+--------------------------------------------+
  | Module    | Script       | Description                                |
  +===========+==============+============================================+
  | dcx       | rstdcx       | create ``.tags``, labels and links         |
  +-----------+--------------+--------------------------------------------+
  | fromdocx  | rstfromdocx  | Convert DOCX to RST using Pandoc           |
  +-----------+--------------+--------------------------------------------+
  | listtable | rstlisttable | Convert RST grid tables to list-tables     |
  +-----------+--------------+--------------------------------------------+
  | untable   | rstuntable   | Converts certain list-tables to paragraphs |
  +-----------+--------------+--------------------------------------------+
  | reflow    | rstreflow    | Reflow paragraphs and tables               |
  +-----------+--------------+--------------------------------------------+
  | reimg     | rstreimg     | Rename images referenced in the RST file   |
  +-----------+--------------+--------------------------------------------+
  | retable   | rstretable   | Transforms list tables to grid tables      |
  +-----------+--------------+--------------------------------------------+

- To create DOCX and PDF `Pandoc`_ is used.

- To create HTML `Sphinx`_ is used. 
  `Pandoc`_ would do as well, but `Sphinx`_ provides a nice entry point
  to all the documentation.

.. `Sphinx`_ should be there, because sphinx-contrib packages allow creating
   graphic files that can be included in normal rst. TODO: support this.

Editors
-------

Vim:

  | `vim_py3_rst <https://github.com/rpuntaie/vim_py3_rst>`_ 
  | `vim-table-mode https://github.com/dhruvasagar/vim-table-mode`_
  | `riv.vim <https://github.com/gu-fan/riv.vim>`_

Atom:

  | atom-ctags       #better: https://github.com/rpuntaie/atom-ctags
  | language-restructuredtext
  | rst-preview-pandoc
  | table-editor
  | rst-snippets
  | atom-build       #better: https://github.com/rpuntaie/atom-build
  | atom-build-waf
  | find-and-replace-under-cursor

  ``atom-build`` and ``atom-ctags`` were modified to allow finding files
  by putting the relevant subdirectory into Atom's project paths.

Of course `Emacs`_ and other `editors`_ work as well. `ReText`_ is even
specialized for RST and Markdown (MD).

.. _`editors`: http://build-me-the-docs-please.readthedocs.io/en/latest/Using_Sphinx/ToolsForReStructuredText.html
.. _`Emacs`: http://docutils.sourceforge.net/docs/user/emacs.html
.. _`ctags`: http://ctags.sourceforge.net/FORMAT
.. _`Sphinx`: http://www.sphinx-doc.org/en/stable/
.. _`Docutils`: http://docutils.sourceforge.net/
.. _`Pandoc`: https://pandoc.org/
.. _`RST`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _`DOCX`: http://www.ecma-international.org/publications/standards/Ecma-376.htm
.. _`ReText`: https://github.com/retext-project/retext

