Many companies use `DOCX <http://www.ecma-international.org/publications/standards/Ecma-376.htm>`_
and thus produce an information barrier.
Working with text is more integrated in the (software) development process.
A final format can be `DOCX`_, but, at least during development, text is better.

`Sphinx <http://www.sphinx-doc.org/en/stable/>`__
is an extension of `Docutils <http://docutils.sourceforge.net/>`__
used for many (software) projects,
but it does not support creation of `DOCX`_ files, which certain companies demand.
`Pandoc <https://pandoc.org/>`__
does support `DOCX`_, but does not support the Sphinx extensions,
hence ``:ref:`` and the like cannot be used.

This python package supports working with 
`RST <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
as documentation format without depending on Sphinx.

- link RST documents (``.rest``) using 
  `substitutions <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions>`__
  (generated in ``_links_xxx.rst``)
- create a ``.tags`` file to jump around in an editor that support 
  `ctags <http://ctags.sourceforge.net/FORMAT>`__
- `RST`_ handling with python: reformat/create `RST`_ tables
- postprocess Pandoc's conversion from `DOCX`_ to `RST`_
- preprocess Pandoc's conversion from `RST`_ to `DOCX`_
- Support in building with `WAF <https://github.com/waf-project/waf>`_ (or ``Makefile``)

  - expand 
    `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax>`_ 
    template files ``.stpl``
  - ``.tikz``, ``.svg``, ``.dot``,  ``.uml``, ``.eps`` or ``.stpl`` thereof, and ``.pyg`` for Python-generated graphics, are converted to ``.png``
    and placed into ``./_images`` or ``../_images``
  - a ``gen`` file specifies how `RST`_ should be generated from source code files (see ``dcx.py``)

The conventions used are shown 

- by the example produced via ``rstdcx --rest samplerstdoc`` or ``rstdcx --stpl sampletemplated``
- by the documentation sources that can be found at 
  https://github.com/rpuntaie/rstdoc/tree/master/doc 

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

- ``html``, ``docx``, ``pdf``, ... uses  Pandoc.

- ``rst_html``, ``rst_pdf``, ...  uses 
  `rst2html <http://docutils.sourceforge.net/0.6/docs/user/tools.html>`__, ...

- ``sphinx_html``, ``sphinx_pdf``, ...  uses Sphinx.
  Sphinx provides a nice entry point via the 
  `sphinx bootstrap theme <https://github.com/ryan-roemer/sphinx-bootstrap-theme>`__.

