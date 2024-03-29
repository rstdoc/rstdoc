.. _`rstdcx`:

rstdcx
======

restructuredText sources are split into two types of files:
main files considered by Sphinx, and included files.
Which of ``.rest``  or ``.rst`` is main or included is determined
by ``source_suffix`` in a ``<root>/conf.py``
or opposite to the extension of the included ``_links_sphinx.r?st`` file:

- if you have ``.. include:: /_links_sphinx.rest``,
  then the main file extension is ``.rst``

``rstdoc`` creates documentation (PDF, HTML, DOCX)
from restructuredText (``.rst``, ``.rest``) using either

- `Pandoc <https://pandoc.org>`__
- `Sphinx <http://www.sphinx-doc.org>`__
- Docutils
  `configurable <http://docutils.sourceforge.net/docs/user/config.html>`__

``rstdoc`` and ``rstdcx`` command line tools call ``dcx.py``.
which

- creates ``.tags`` to jump around with the editor

- handles `.stpl <https://bottlepy.org/docs/dev/stpl.html>`__ files

- processes ``gen`` files (see examples produced by --rest)

- creates links files (``_links_docx.r?st``, ``_links_sphinx.r?st``, ...)

- forwards known files to either Pandoc, Sphinx or Docutils

See example at the end of ``dcx.py``.
It is supposed to be used with a build tool.
``make`` and ``waf`` examples are included.

- Initialize example tree (add ``--rstrest`` to make ``.rst`` main and ``.rest`` included files):

  ::

      $ ./dcx.py --rest repo #repo/doc/{sy,ra,sr,dd,tp}.rest files OR
      $ ./dcx.py --stpl repo #repo/doc/{sy,ra,sr,dd,tp}.rest.stpl files
      $ ./dcx.py --ipdt repo #repo/pdt/AAA/{i,p,d,t}.rest.stpl files
      $ ./dcx.py --over repo #.rest all over

- Only create .tags and ``_links_xxx.r?st``:

  ::

    $ cd repo
    $ rstdoc

- Create the docs (and .tags and ``_links_xxx.r?st``) with **make**:

  ::

      $ make html #OR
      $ make epub #OR
      $ make latex #OR
      $ make docx #OR
      $ make pdf

  The latter two are done by Pandoc, the others by Sphinx.

- Create the docs (and .tags and ``_links_xxx.r?st``) with
  `waf <https://github.com/waf-project/waf>`__:

  Instead of using ``make`` one can load ``dcx.py`` (``rstdoc.dcx``) in
  `waf <https://github.com/waf-project/waf>`__.
  ``waf`` also considers all recursively included files,
  such that a change in any of them results in a rebuild.
  All files can have an additional ``.stpl`` extension to use
  `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html>`__.

  $ waf configure #also copies the latest version of waf in here
  $ waf --docs docx,sphinx_html,rst_odt
  $ #or you provide --docs during configure to always compile the docs

  - ``rst_xxx``: via
    `rst2xxx.py <http://docutils.sourceforge.net/docs/user/tools.html>`__
  - ``sphinx_xxx``: via `Sphinx <http://www.sphinx-doc.org>`__ and
  - just ``xxx``: via `Pandoc <https://pandoc.org>`__.


The following image language files should be parallel to the ``.r?st`` files.
They are automatically converted to ``.png``
and placed into ``./_images`` or ``<updir>/_images`` or else parallel to the file.

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
  If the python code defines a ``to_svg`` or a ``save_to_png`` function,
  then that is used, to create a png.
  Else the following is tried

  - ``pyx.canvas.canvas`` from the
    `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or
  - ``cairocffi.Surface`` from
    `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html>`__
  - `matplotlib <https://matplotlib.org>`__.
    If ``matplotlib.pyplot.get_fignums()>1``
    the figures result in ``<name><fignum>.png``

  The same code or the file names can be used in a ``.r?st.stpl`` file
  with ``pngembed()`` or ``dcx.svgembed()`` to embed in html output.

  ::

     {{!svgembed("egpyx.pyg",outinfo)}}
     <%
     ansvg=svgembed('''
     from svgwrite import cm, mm, drawing
     d=drawing.Drawing(viewBox=('0 0 300 300'))
     d.add(d.circle(center=(2*cm, 2*cm), r='1cm', stroke='blue', stroke_width=9))
     '''.splitlines(),outinfo)
     %>
     {{!ansvg}}


Conventions
-----------

Files

  - main files and included files: ``.rest``, ``.rst`` or vice versa.
    ``.txt`` are for literally included files (use :literal: option).
  - templates separately rendered : ``*.rest.stpl`` and ``*.rst.stpl``
    template included: ``*.rst.tpl``
    Template lookup is done in
    ``.`` and ``..`` with respect to the current file.

    - with ``%include('some.rst.tpl', param="test")`` with optional parameters
    - with ``%globals().update(include('utility.rst.tpl'))``
      if it contains only definitions

Links

- ``.. _`id`:`` are *reST targets*.
  reST targets should not be template-generated.
  The template files should have a higher or equal number of targets
  than the generated file,
  in order for tags to jump to the template original.
  If one wants to generate reST targets,
  then this should better happen in a previous step,
  e.g. with ``gen`` files mentioned above.

- References use replacement
  `substitutions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text>`__:
  ``|id|``.

- If you want an overview of the linking (traceability),
  add ``.. include:: _traceability_file.rst``
  to ``index.rest`` or another ``.rest`` parallel to it.
  It is there in the example project, to include it in tests.
  ``_traceability_file.{svg,png,rst}`` are all in the same directory.

Link files are created in link roots, which are folders where the first main file
(``.rest`` or ``.rst``) is encoutered during depth-first traversal.
Non-overlapping link root paths produce separately linked file sets.

``.. include:: /_links_sphinx.r?st``, with the one initial ``/``
instead of a relative or absolute path,
will automatically search upward for the ``_links_xxx.r?st`` file
(``_sphinx`` is replaced by what is needed by the wanted target when the docs are generated).

Sphinx ``conf.py`` is augmented by configuration for Pandoc and Docutils.
It should be where the input file is, or better at the project root
to be usable with `waf <https://github.com/waf-project/waf>`__.

See the example project created with ``--rest/stpl/ipdt/over``
and the sources of the documentation of
`rstdoc <https://github.com/rstdoc/rstdoc>`__.


``rstdcx`` CLI
--------------

``rstdcx`` is the same as ``rstdoc``.

Without parameters: creates ``|substitution|`` links and .tags ctags for reST targets.

With two or three parameters: process file or dir to out file or dir
through Pandoc, Sphinx, Docutils (third parameter):

- ``html``, ``docx``, ``odt``, ``pdf``, ... uses  Pandoc.

- ``rst_html``, ``rst_odt``, ``rst_pdf``, ...  uses
  `rst2html <http://docutils.sourceforge.net/0.6/docs/user/tools.html>`__, ...

- ``sphinx_html``, ``sphinx_pdf``, ...  uses Sphinx.
  Sphinx provides a nice entry point via the
  `sphinx bootstrap theme <https://github.com/ryan-roemer/sphinx-bootstrap-theme>`__.

4th parameter onward become python defines usable in ``.stpl`` files.

Pdf output needs latex. Else you can make odt or docx and use

- win: ``swriter.exe --headless --convert-to pdf Untitled1.odt``
- linux: ``lowriter --headless --convert-to pdf Untitled1.odt``

Inkscape (.eps, .svg), Dot (.dot), Planuml (.uml), latex (.tex,.tikz)
are converted to .png into ``./_images`` or ``<updir>/_images`` or '.'.
Any of the files can be a SimpleTemplate template (xxx.yyy.stpl).

Configuration is in ``conf.py`` or ``../conf.py``.

``rstdoc --stpl|--rest|--ipdt|-over`` create sample project trees.

``--stpl`` with ``.rest.stpl`` template files,
``--rest`` with only a doc folder with ``.rest`` files,
``--ipdt`` with inform-plan-do-test enhancement cycles
``--over`` with ``.rest`` files all over the project tree including symbolic links

Examples
--------

Example folders (see wscript and Makefile there)::

    rstdoc --rest <folder> [--rstrest]
    rstdoc --stpl <folder> [--rstrest]
    rstdoc --ipdt <folder> [--rstrest]
    rstdoc --over <folder> [--rstrest]

Use ``--rstrest`` to produce ``.rst`` for the main file,
as ``.rest`` is not recognized by github/gitlab,
who also don't support file inclusion,
so no need for two extension anyway.

Examples usages with the files generated by ``rstdoc --stpl tmp``:

.. code-block:: sh

    cd tmp/doc
    rstdcx   #expand .stpl and produce .tag and _links_xxx files

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

    #convert the graphics and place the into _images or <updir>/_images
    #if no _images directory exists they will be placed into the same directory
    rstdcx egcairo.pyg
    rstdcx egdot.dot.stpl
    rstdcx egeps.eps
    rstdcx egother.pyg
    rstdcx egplt.pyg
    rstdcx egpygal.pyg
    rstdcx egpyx.pyg
    rstdcx egsvg.svg.stpl
    rstdcx egtikz.tikz
    rstdcx egtikz1.tikz
    rstdcx eguml.uml

    #Convert graphics to a png (even if _images directory exists):
    rstdcx eguml.uml eguml.png

    #Files to other files:

    rstdoc dd.rest.stpl dd.rest
    rstdoc dd.rest.stpl dd.html html
    rstdoc dd.rest.stpl dd.html
    rstdoc sr.rest.stpl sr.html rst_html
    rstdoc dd.rest.stpl dd.docx
    rstdoc dd.rest.stpl dd.odt pandoc
    rstdoc dd.rest.stpl dd.odt
    rstdoc sr.rest.stpl sr.odt rst_odt
    rstdoc sr.rest.stpl sr.odt rst
    rstdoc index.rest build/index.html sphinx_html

    #Directories to other directories with out info:

    rstdoc . build html
    rstdoc . build sphinx_html

Grep with python re in .py, .rst, .rest, .stpl, .tpl::

    rstdoc --pygrep inline

Grep for keyword lines containing 'png'::

    rstdoc --kw png

Default keyword lines::

    .. {{{kw1,kw2
    .. {kw1,kw2}
    {{_ID3('kw1 kw2')}}
    %__ID3('kw1 kw2')
    :ID3: kw1 kw2

