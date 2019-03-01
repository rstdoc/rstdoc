.. _`rstdcx`:

rstdcx
======

Support script to create documentation (PDF, HTML, DOCX)
from restructuredText (RST, reST) using either

- `Pandoc <https://pandoc.org>`__
- `Sphinx <http://www.sphinx-doc.org>`__
- Docutils
  `configurable <http://docutils.sourceforge.net/docs/user/config.html>`__

``rstdoc`` installs the ``rstdcx`` command line tool that calls ``dcx.py``.
It

- processes ``gen`` files (see examples produced by --rest)

- handles `.stpl <https://bottlepy.org/docs/dev/stpl.html>`__ files

- creates ``.tags`` to jump around with the editor

- creates links files like
  ``_links_pdf.rst``, ``_links_docx.rst``, ``_links_sphinx.rst``

- forwards known files to either Pandoc, Sphinx or Docutils

  Sphinx ``conf.py`` is augmented by configuration for Pandoc and Docutils.
  It should be where the input file is or above. If used with
  `waf <https://github.com/waf-project/waf>`__,
  it can also be where the main wscript is.

See example at the end of ``dcx.py``.
It is supposed to be used with a build tool.
``make`` and ``waf`` examples are included.

- Initialize example tree.
  This copies ``dcx.py`` into the example tree
  to be independent from possible future changes::

  $ ./dcx.py --rest tmp #.rest files OR
  $ ./dcx.py --stpl tmp #.rest.stpl files

- Only create .tags and _links_xxx.rst::

  $ cd tmp/doc
  $ ./dcx.py

- Create the docs (and .tags and _links_xxx.rst) with **make**::

  $ make html #OR
  $ make epub #OR
  $ make latex #OR
  $ make docx #OR
  $ make pdf

  The latter two are done by Pandoc, the others by Sphinx.

- Create the docs (and .tags and _links_xxx.rst) with
  `waf <https://github.com/waf-project/waf>`__:

  Instead of using ``make`` one can load ``dcx.py`` in
  `waf <https://github.com/waf-project/waf>`__.
  ``waf`` also considers all recursively included files,
  such that a change in any of them results in a rebuild of the documentation.
  All files can have an additional ``.stpl`` extension to use
  `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html>`__.

  $ waf configure #also copies the latest version of waf in here
  $ waf --docs docx,sphinx_html,rst_odt
  $ #or you provide --docs during configure to always compile the docs

  - ``rst_xxx`` via
    `rst2xxx.py <http://docutils.sourceforge.net/docs/user/tools.html>`__
  - ``sphinx_xxx`` via `Sphinx <http://www.sphinx-doc.org>`__ and
  - just ``xxx`` via `Pandoc <https://pandoc.org>`__.


The following image language files should be parallel to the ``.rest`` files.
They are automatically converted to ``.png``
and placed into ``./_images`` or ``../_images``.

- ``.tikz`` or ``.tikz.stpl``.
  This needs LaTex.

- `.svg <http://svgpocketguide.com/book/>`__ or ``.svg.stpl``

- ``.dot`` or ``.dot.stpl``

  This needs `graphviz <https://graphviz.gitlab.io/gallery/>`__.

- `.uml <http://plantuml.com/command-line>`__ or ``.uml.stpl``

  This needs `plantuml <http://plantuml.com/command-line>`__ .
  Provide either

  - ``plantuml.bat`` with e.g. ``java -jar "%~dp0plantuml.jar" %*``  or
  - ``plantuml`` sh script with
    ``java -jar `dirname $BASH_SOURCE`/plantuml.jar "$@"``

- ``.eps`` or ``.eps.stpl`` embedded postscript files.

  This needs `inkscape <https://inkscape.org/en/>`__.

- ``.pyg`` contains python code that produces a graphic.
  If the python code defines a ``save_to_png`` function,
  then that is used, which allows to use whatever python library you want
  (`graph_tool <https://graph-tool.skewed.de/static/doc/quickstart.html>`__,
  `igraph <http://igraph.org/python/doc/tutorial/tutorial.html>`__,...)
  Else the following is tried

  - ``pyx.canvas.canvas`` from the
    `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or
  - ``cairocffi.Surface`` from
    `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html>`__
  - ``pygal.Graph`` from `pygal <https://pygal.org>`__
  - `matplotlib <https://matplotlib.org>`__.
    If ``matplotlib.pyplot.get_fignums()>1``
    the figures result in ``<name><fignum>.png``

Conventions
-----------

- Files

  - main docs end in ``.rest``
  - ``.rst`` are included and ignored by Sphinx (see ``conf.py``).
  - ``.txt`` are literally included (use :literal: option).
  - templates ``x.rest.stpl`` and ``y.rst.stpl`` are rendered separately.
  - ``some.rst.tpl`` are template included
    Template lookup is done in
    ``.`` and ``..`` with respect to the current file.

    - with ``%include('some.rst.tpl', param="test")`` with optional parameters
    - with ``%globals().update(include('utility.rst.tpl'))``
      if it contains only definitions

- ``.. _`id`:`` are *reST targets*.
  reST targets should not be template-generated.
  The template files should have a higher or equal number of targets
  than the generated file,
  in order for tags to jump to the template original.
  If one wants to generate reST targets,
  then this should better happen in a previous step,
  e.g. with ``gen`` files mentioned above.

- References use replacement `substitutions \
  <http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text>`__:
  ``|id|``.

- If you want an overview of the linking (traceability),
  add ``.. include:: _traceability_file.rst``
  to ``index.rest`` or another ``.rest`` file.
  It is there in the generated samples to include it in tests.
  You might want to remove that line, if you start with the samples.

See the example created with ``--rest`` or ``--stpl``
at the end of this file and the sources of the documentation of
`rstdoc <https://github.com/rpuntaie/rstdoc>`__.


``rstdcx`` CLI
--------------

Without parameters: creates |substitution| links and .tags ctags for reST targets.

With two or three parameters: process file or dir to out file or dir
through Pandoc, Sphinx, Docutils (third parameter):

- ``html``, ``docx``, ``pdf``, ... uses  Pandoc.

- ``rst_html``, ``rst_pdf``, ...  uses 
  `rst2html <http://docutils.sourceforge.net/0.6/docs/user/tools.html>`__, ...

- ``sphinx_html``, ``sphinx_pdf``, ...  uses Sphinx.
  Sphinx provides a nice entry point via the 
  `sphinx bootstrap theme <https://github.com/ryan-roemer/sphinx-bootstrap-theme>`__.

4th parameter onward become python defines usable in ``.stpl`` files.

Inkscape (.eps, .svg), Dot (.dot), Planuml (.uml), latex (.tex,.tikz)
are converted to .png into ``./_images`` or ``../_images``.
Any of the files can be a SimpleTemplate template (xxx.yyy.stpl).

Configuration is in ``conf.py`` or ``../conf.py``.

Examples with the files generated with the ``--stpl tmp``:

.. code-block:: sh

    cd tmp/doc
    rstdcx   #expand .stpl and produce _links_xxx.rst and .tags

    #expand stpl and append substitutions (for simple expansion use ``stpl <file> .``)
    rstdcx dd.rest.stpl - rest           # expand to stdout, appending dd.html substitutions, to pipe to Pandoc
    rstdcx dd.rest.stpl - html.          # as before
    rstdcx dd.rest.stpl - docx.          # expand to stdout, appending dd.docx substitutions, to pipe to Pandoc
    rstdcx dd.rest.stpl - newname.docx.  # expand template, appending substitutions for target newname.docx
    rstdcx dd.rest.stpl - html           # expand to stdout, already process through Pandoc to produce html on stdout
    rstdcx dd.rest.stpl                  # as before
    rstdcx sy.rest.stpl - rst_html       # expand template, already process through Docutils to produce html on stdout
    stpl sy.rest.stpl | rstdcx - - sy.html. # appending sy.html substitutions, e.g. to pipe to Pandoc
    stpl dd.rest.stpl | rstdcx - - dd.html  # appending tp.html substitutions and produce html on stdout via Pandoc
    rstdcx dd.rest.stpl dd.rest          # expand into dd.rest, appending substitutions for target dd.html
    rstdcx dd.rest.stpl dd.html html     # expand template, process through Pandoc to produce dd.html
    rstdcx dd.rest.stpl dd.html          # as before
    rstdcx dd.rest.stpl dd.html rst_html # expand template, already process through Docutils to produce dd.html
    rstdcx dd.rest.stpl dd.docx          # expand template, process through Pandoc to produce dd.docx
    rstdcx dd.rest.stpl dd.odt pandoc    # expand template, process through Pandoc to produce dd.odt
    rstdcx dd.rest.stpl dd.odt           # as before
    rstdcx dd.rest.stpl dd.odt rst_odt   # expand template, process through Docutils to produce dd.odt
    rstdcx dd.rest.stpl dd.odt rst       # as before
    rstdcx . build html                  # convert current dir to build output dir using pandoc
    rstdcx . build sphinx_html           # ... using sphinx (if no index.rest, every file separately)

    #Sphinx is not file-oriented
    #but with rstdcx you need to provide the files to give Sphinx ``master_doc`` (normally: index.rest)
    #Directly from ``.stpl`` does not work with Sphinx
    rstdcx index.rest ../build/index.html sphinx_html   # via Sphinx the output directory must be different

    #convert the graphics and place the into _images or ../_images
    #if no _images directory exists they will placed into the same folder
    rstdcx egcairo.pyg
    rstdcx egdot.dot.stpl
    rstdcx egeps.eps
    rstdcx egeps1.eps
    rstdcx egother.pyg
    rstdcx egplt.pyg
    rstdcx egpygal.pyg
    rstdcx egpyx.pyg
    rstdcx egsvg.svg.stpl
    rstdcx egtikz.tikz
    rstdcx egtikz1.tikz
    rstdcx eguml.uml

    #convert graphics to a png here (even if _images directory exists)
    rstdcx eguml.uml eguml.png

