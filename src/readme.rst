
This python packages supports working with `RST`_  as documentation format:

- postprocess `Pandoc`_'s conversion from `DOCX`_ to `RST`_
- preprocess `Pandoc`_'s conversion from `RST`_ to `DOCX`_
- link the `RST`_ documents (``_links_xxx.rst`` files)
- create a ``.tags`` file
- reformat/create `RST`_ tables
- expand template files ``.stpl``
- convert ``.tikz`` to ``.png`` files and place them ``./_images`` or ``../_images``
- generated files from source code using the ``gen`` file

`Sphinx`_ is an extension of `Docutils`_ used for many (software) projects,
but it does not support creation of `DOCX`_ files.
`Pandoc`_ does support `DOCX`_, but does not support the `Sphinx`_ extensions.

``rstdoc`` supports working with ``restructuredText`` (`RST`_) 
defined by `Docutils`_ using some conventions.
The conventions are shown by the example produced via ``rstdcx --init samplerstdoc``,

The idea is, that working with text is more integrated in the 
(software) development process.

``rstdoc``'s ``rstdcx`` (``dcx.py``) 

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


.. _`editors`: http://build-me-the-docs-please.readthedocs.io/en/latest/Using_Sphinx/ToolsForReStructuredText.html
.. _`Emacs`: http://docutils.sourceforge.net/docs/user/emacs.html
.. _`ctags`: http://ctags.sourceforge.net/FORMAT
.. _`Sphinx`: http://www.sphinx-doc.org/en/stable/
.. _`Docutils`: http://docutils.sourceforge.net/
.. _`Pandoc`: https://pandoc.org/
.. _`RST`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _`DOCX`: http://www.ecma-international.org/publications/standards/Ecma-376.htm

