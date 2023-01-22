=========
CHANGELOG
=========

TODO
====

- use docutils make_id() to create the external target in the _links_xxx.rst files

- test tags on vscode, and add to docs


20230122 - v1.8.2
=================

- allow atx headers starting with a number of # chars
- run and fix tests with new pandoc, docutils, sphinx version

20201231- v1.8.1
================

- ``--version`` option
- fix regression tests
- more flexible ``pdtid()`` and ``pdtAAA()``

20191124 - v1.8.0
=================

No changelog yet.
Some later entries from git log:

- fix tests
- ``--rstrest`` to have sample project with .rst main and .rest
- use txdir
- ``/_links_sphinx.rst`` to search up dir
- ``--ipdt`` and ``--over`` sample project added
- support links accross directories
- allow control over file name in temporary directory
- targets with relative path
- do all stpl files in the tree, not just those in doc dir
- gen file can now also be python code
- cairosvg is brittle on windows. use inkscape in case of problems
- fix test, as pandoc 2.7 produces simple table now, instead of grid table
- added pytest.ini to suppress deprecation warnings
- grep and keyword search
- generated files for readthedocs
- work without sphinx_bootstrap_theme

20190228 - v1.6.8
=================

no changelog yet
