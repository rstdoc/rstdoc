Many companies use `DOCX`_ and thus produce an information barrier.
Working with text is more integrated in the (software) development process.
A final format can be `DOCX`_, but, at least during development, text is better.

`Sphinx`_ is an extension of `Docutils`_ used for many (software) projects,
but it does not support creation of `DOCX`_ files, which certain companies demand.
`Pandoc`_ does support `DOCX`_, but does not support the `Sphinx`_ extensions.

This python packages supports working with `RST`_ as documentation format without depending on `Sphinx`_:

- link `RST`_ documents (``_links_xxx.rst`` files)
- create a ``.tags`` file to jump around in an editor that support `ctags`_
- `RST`_ handling with python: reformat/create `RST`_ tables
- postprocess `Pandoc`_'s conversion from `DOCX`_ to `RST`_
- preprocess `Pandoc`_'s conversion from `RST`_ to `DOCX`_
- Support in building with `WAF`_ or ``Makefile``

  - expand `SimpleTemplate`_ template files ``.stpl``
  - convert ``.tikz`` to ``.png`` files and place them ``./_images`` or ``../_images``
  - generated files from source code using a ``gen`` file

The conventions used are shown 

- by the example produced via ``rstdcx --init samplerstdoc``
- by the documentation sources that can be found at 
  https://github.com/rpuntaie/rstdoc/tree/master/src/doc 

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
.. _`SimpleTemplate`: https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax
.. _`waf`: https://github.com/waf-project/waf

