API
---

.. code-block:: py

   import rstdoc.dcx as dcx


The functions in ``dcx.py``
are available to the ``gen_xxx(lns,**kw)`` functions (|dhy|).


.. _`dcx.verbose`:

:dcx.verbose:

.. code-block:: py

   verbose = False

Increase output if set to True.

.. _`dcx.dry_run`:

:dcx.dry_run:

.. code-block:: py

   def dry_run(dry=None, verbose_=None):

.. code-block:: py

       global _toolrunner
       global verbose
       if dry:
           if verbose_ is None:
               verbose = True
           else:
               verbose = verbose_
           _toolrunner = _Verbose(_DryRunner())
       else:
           if verbose_ is None:
               verbose = False
           else:
               verbose = verbose_
           if dry is not None or _toolrunner is None:
               _toolrunner = _Verbose(_ToolRunner())

Set or unset dry run.
For dry run verbosity is on per default.
For non-dry run verbosity is off per default.

.. _`dcx.DPI`:

:dcx.DPI:

.. code-block:: py

   DPI = 600

Used for png creation.

.. _`dcx.g_config`:

:dcx.g_config:

.. code-block:: py

   g_config = None

``g_config`` can be used to inject a global config.
This overrides the defaults
and is overriden by a ``./conf.py`` or ``../conf.py`` relative to the in file.

.. _`dcx.cmd`:

:dcx.cmd:

.. code-block:: py

   def cmd(cmdlist, **kwargs):

Runs ``cmdlist`` via subprocess.run and return stdout.
In case of problems RstDocError is raised.

:param cmdlist: command as list
:param kwargs: arguments forwarded to ``subprocess.run()``


.. _`dcx.new_cwd`:

:dcx.new_cwd:

.. code-block:: py

   @contextlib.contextmanager
   def new_cwd(apth):

Use as::

    with new_cwd(dir):
        #inside that directory


.. _`dcx.startfile`:

:dcx.startfile:

.. code-block:: py

   def startfile(filepath):

Extends the Python startfile to non-Windows platforms


.. _`dcx.tempdir`:

:dcx.tempdir:

.. code-block:: py

   def tempdir():

Make temporary directory and register it to be removed with ``atexit``.

This can be used inside a ``.stpl`` file
to create images from inlined images source,
place them in temporary file,
and include them in the final ``.docx`` or ``.odt``.


.. _`dcx.run_inkscape`:

:dcx.run_inkscape:

.. code-block:: py

   def run_inkscape(infile,  outfile, dpi=DPI):

Uses ``inkscape`` commandline to convert to ``.png``

:param infile: .svg, .eps, .pdf filename string
  (for list with actual .eps or .svg data use |dcx.svgpng| or |dcx.epspng|)
:param outfile: .png file name


.. _`dcx.rst_sphinx`:

:dcx.rst_sphinx:

.. code-block:: py

   @infile_cwd
   def rst_sphinx(
           infile, outfile, outtype=None, **config
           ):

Run Sphinx on infile.

:param infile: .txt, .rst, .rest filename (normally index.rest)
:param outfile: the path to the target file (not target directory)
:param outtype: html,... or any other sphinx writer
:param config: keys from config_defaults

::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> cd('../doc')
    >>> dry_run(True)

    >>> infile, outfile = ('index.rest',
    ... '../build/doc/sphinx_html/index.html')
    >>> rst_sphinx(infile, outfile) #doctest: +ELLIPSIS
    run (['sphinx-build', '-b', 'html', ... 'master_doc=index'],) ...

    >>> rst_sphinx('dd.rest',
    ... '../build/doc/sphinx_html/dd.html') #doctest: +ELLIPSIS
    run ([... '-b', 'singlehtml', ..., '-D', 'master_doc=dd'],) ...

    >>> rst_sphinx('dd.rest',
    ... '../build/doc/sphinx_latex/dd.tex') #doctest: +ELLIPSIS
    run ([... '-b', 'tex', ...sphinx_latex', ... 'master_doc=dd'],) ...

    >>> dry_run(False)
    >>> cd(olddir)


.. _`dcx.rst_pandoc`:

:dcx.rst_pandoc:

.. code-block:: py

   @infile_cwd
   def rst_pandoc(
           infile, outfile, outtype, **config
           ):

Run Pandoc on infile.

:param infile: .txt, .rst, .rest filename
:param outfile: the path to the target document
:param outtype: html,...
:param config: keys from config_defaults


.. _`dcx.rst_rst2`:

:dcx.rst_rst2:

.. code-block:: py

   @infile_cwd
   def rst_rst2(
           infile, outfile, outtype, **config
           ):

Run the rst2xxx docutils fontend tool on infile.

:param infile: .txt, .rst, .rest filename
:param outfile: the path to the target document
:param outtype: html,...
:param config: keys from config_defaults


.. _`dcx.PageBreakHack`:

:dcx.PageBreakHack:

.. code-block:: py

   def PageBreakHack(destination_path):

This introduces a ``PageBreak`` style into ``content.xml``
to allow the following raw page break of opendocument odt::

  .. raw:: odt

      <text:p text:style-name="PageBreak"/>

This is no good solution,
as it introduces an empty line at the top of the new page.

Unfortunately the following does not work
with or without ``text:use-soft-page-breaks="true"``

::

    .. for docutils
    .. raw:: odt

        <text:p text:style-name="PageBreak"/>

    .. for pandoc
    .. raw:: opendocument

        <text:p text:style-name="PageBreak"/>

According to C066363e.pdf it should work.

See ``utility.rst.tpl`` in the ``--stpl`` samples.


.. _`dcx.svgpng`:

:dcx.svgpng:

.. code-block:: py

   @png_post_process_if_any
   @normoutfile
   @readin
   def svgpng(infile, outfile=None, *args, **kwargs):

Converts a .svg file to a png file.

:param infile: a .svg file name or list of lines
:param outfile: if not provided the input file with new extension
  ``.png`` either in ``./_images`` or ``../_images`` or ``.``


.. _`dcx.texpng`:

:dcx.texpng:

.. code-block:: py

   @png_post_process_if_any
   @partial(in_temp_if_list, suffix='.tex')
   @infile_cwd
   def texpng(infile, outfile=None, *args, **kwargs):

Latex has several graphic packages, like

- tikz
- chemfig

that can be converted to .png with this function.

For ``.tikz`` file use |dcx.tikzpng|.

:param infile: a .tex file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided, the input file with .png
    either in ``./_images`` or ``../_images`` or ``.``


.. _`dcx.tikzpng`:

:dcx.tikzpng:

.. code-block:: py

   tikzpng = normoutfile(readin(_tikzwrap(_texwrap(texpng))))

Converts a .tikz file to a png file.

See |dcx.texpng|.

.. _`dcx.dotpng`:

:dcx.dotpng:

.. code-block:: py

   @png_post_process_if_any
   @partial(in_temp_if_list, suffix='.dot')
   @infile_cwd
   def dotpng(
           infile,
           outfile=None,
           *args,
           **kwargs
           ):

Converts a .dot file to a png file.

:param infile: a .dot file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided the input file with new extension
    ``.png`` either in ``./_images`` or ``../_images`` or ``./``


.. _`dcx.umlpng`:

:dcx.umlpng:

.. code-block:: py

   @png_post_process_if_any
   @partial(in_temp_if_list, suffix='.uml')
   @infile_cwd
   def umlpng(
           infile,
           outfile=None,
           *args,
           **kwargs
           ):

Converts a .uml file to a png file.

:param infile: a .uml file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided the input file with new extension
    ``.png`` either in ``./_images`` or ``../_images`` or ``./``


.. _`dcx.epspng`:

:dcx.epspng:

.. code-block:: py

   @png_post_process_if_any
   @partial(in_temp_if_list, suffix='.eps')
   @infile_cwd
   def epspng(
           infile,
           outfile=None,
           *args,
           **kwargs):

Converts an .eps file to a png file using inkscape.

:param infile: a .eps file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided the input file with new extension
    ``.png`` either in ``./_images`` or ``../_images`` or ``./``


.. _`dcx.pygpng`:

:dcx.pygpng:

.. code-block:: py

   @png_post_process_if_any
   @normoutfile
   @infile_cwd
   @readin
   def pygpng(
           infile, outfile=None, *args,
           **kwargs
           ):

Converts a .pyg file to a png file.

``.pyg`` contains python code that produces a graphic.
If the python code defines a ``save_to_png`` function, then that is used.
Else the following is tried

- ``pyx.canvas.canvas`` from the
  `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or
- ``svgwrite.drawing.Drawing`` from the
  `svgwrite <https://svgwrite.readthedocs.io>`__ library or
- ``cairocffi.Surface`` from `cairocffi \
  <https://cairocffi.readthedocs.io/en/stable/overview.html#basic-usage>`__
- ``pygal.Graph`` from
  `pygal <https://pygal.org>`__
- `matplotlib <https://matplotlib.org>`__.
  If ``matplotlib.pyplot.get_fignums()>1``
  the figures result ``<name><fignum>.png``

:param infile: a .pyg file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided the input file with new extension
    ``.png`` either in ``./_images`` or ``../_images`` or ``./``


.. _`dcx.dostpl`:

:dcx.dostpl:

.. code-block:: py

   @infile_cwd
   def dostpl(
           infile,
           outfile=None,
           lookup=None,
           **kwargs
           ):

Expands an `.stpl <https://bottlepy.org/docs/dev/stpl.html>`__ file.

The whole ``rstdoc.dcx`` namespace is forwarded to the template code.

``.stpl`` provides full python power:

- e.g. one can create temporary images,
  which are then included in the final .docx of .odt
  See |dcx.tempdir|.

:param infile: a .stpl file name or list of lines
:param outfile: if not provided the expanded is returned
:param lookup: lookup paths must be relative to infile

::

    >>> infile = ['hi {{2+3}}!']
    >>> dostpl(infile)
    ['hi 5!']


.. _`dcx.dorst`:

:dcx.dorst:

.. code-block:: py

   def dorst(
           infile,
           outfile=io.StringIO,
           outinfo=None,
           fn_i_ln=None
           ):

Default interpreted text role is set to math.
The link lines are added to the .rest file or .rest lines

:param infile: a .rest, .rst, .txt file name or list of lines

:param outfile: None and '-' mean standard out.
    If io.StringIO, then the lines are returned.
    For .rest ``|xxx|`` substitutions for reST link targets
    in infile are appended if no ``_links_sphinx.rst`` there

:param outinfo: specifies the tool to use
    ``html``, ``docx``, ``odt``,... via pandoc if output
    ``sphinx_html``,... via sphinx
    ``rst_html``,... via rst2xxx frontend tools
    ``[infile/][substitution.]docx[.]`` substitutions
    stands for the file used in substitutions if no ``_links_sphinx.rst``
    The infile is used, if the actual infile are lines.
    The final dot tells to stop after substitutions.

:param fn_i_ln: ``(fn, i, ln)`` of the ``.stpl``
    with all stpl includes sequenced (used by |dcx.convert|)

::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> cd('../doc')

    >>> dorst('dd.rest') #doctest: +ELLIPSIS
    ['.. default-role:: math\n', ...

    >>> dorst('ra.rest.stpl') #doctest: +ELLIPSIS
    ['.. default-role:: math\n', ...

    >>> dorst(['hi there']) #doctest: +ELLIPSIS
    ['.. default-role:: math\n', '\n', 'hi there\n', ...

    >>> dry_run(False, True)
    >>> dorst(['hi there'], None,'html') #doctest: +ELLIPSIS
    + .../rest.rest.rest
    run (['pandoc', ...
    <!DOCTYPE html>
    ...

    >>> dorst('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
    + .../ra.rest.stpl.rest
    run (['pandoc', ..., '-o', 'ra.docx'],) ...
    + ra.docx

    >>> exists('ra.docx')
    True
    >>> rmrf('ra.docx')
    >>> exists('ra.docx')
    False
    >>> rmrf('ra.rest.stpl.rest')
    >>> exists('ra.rest.stpl.rest')
    False

    >>> dorst(['hi there'],'test.html') #doctest: +ELLIPSIS
    + .../rest.rest.rest
    run (['pandoc', ..., '-o', 'test.html'],) ...

    >>> exists('test.html')
    True
    >>> rmrf('test.html')
    >>> exists('test.html')
    False
    >>> rmrf('rest.rest.rest')
    >>> exists('rest.rest.rest')
    False

    >>> dorst(['hi there'],'test.odt','rst') #doctest: +ELLIPSIS
    + ...rest.rest.rest

    >>> exists('rest.rest.rest')
    True
    >>> rmrf('rest.rest.rest')
    >>> exists('rest.rest.rest')
    False
    >>> exists('test.odt')
    True
    >>> rmrf('test.odt')
    >>> exists('test.odt')
    False
    >>> cd(olddir)



.. _`dcx.convert`:

:dcx.convert:

.. code-block:: py

   def convert(
           infile,
           outfile=io.StringIO,
           outinfo=None
           ):

Converts any of the known files.

Stpl files are forwarded to the next converter.

The main job is to normalized the input params,
because this is called from |dcx.main| and via Python.
It forwards to the right converter.

Examples::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> cd('../doc')

    >>> dry_run(False, True)

    >>> convert([' ','   hi {{2+3}}!'], outinfo='rest')
    ['   .. default-role:: math\n', '\n', ' \n', '   hi 5!\n', '\n']

    >>> convert([' ','   hi {{2+3}}!'])  #doctest: +ELLIPSIS
    + .../rest.rest.rest
    run (['pandoc', ...
    ['<!DOCTYPE html>\n', ...]
    >>> rmrf('rest.rest.rest')

    >>> infile, outfile, outinfo = ([
    ... "newpath {{' '.join(str(i)for i in range(4))}} rectstroke showpage"
    ... ],'tst.png','eps')
    >>> convert(infile, outfile, outinfo) #doctest: +ELLIPSIS
    run (['inkscape', ...tst.png'],) ...
    ...
    >>> exists('tst.png')
    True
    >>> rmrf('tst.png')
    >>> exists('tst.png')
    False

    >>> convert('ra.rest.stpl') #doctest: +ELLIPSIS
    + .../ra.rest.rest
    run (['pandoc', ..., '-o', '-'],) ...
    ['<!DOCTYPE html>\n', ...

    >>> convert('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
    + .../ra.rest.rest
    run (['pandoc', ..., '-o', 'ra.docx'],) ...
    + ra.docx

    >>> exists('ra.rest.rest')
    True
    >>> rmrf('ra.rest.rest')
    >>> exists('ra.rest.rest')
    False
    >>> exists('ra.docx')
    True
    >>> rmrf('ra.docx')
    >>> exists('ra.docx')
    False

    >>> convert('dd.rest', None,'html') #doctest: +ELLIPSIS
    + .../dd.rest.rest
    run (['pandoc', ..., '-o', '-'],) ...
    <!DOCTYPE html>
    ...

    >>> exists('dd.rest.rest')
    True
    >>> rmrf('dd.rest.rest')
    >>> exists('dd.rest.rest')
    False
    >>> cd(olddir)


:param infile:
    any of ``.tikz``, ``.svg``, ``.dot``, ``.uml``, ``.eps``, ``.pyg``
    or else stpl is assumed. Can be list of lines, too.

:param outfile: ``-`` means standard out,
    else a file name, or None for automatic (using outinfo),
    or io.StringIO to return lines instead of stdout

:param outinfo:
    ``html``, ``sphinx_html``, ``docx``, ``odt``, ``file.docx``,...
    interpet input as rest, else specifies graph type


.. _`dcx.convert_in_tempdir`:

:dcx.convert_in_tempdir:

.. code-block:: py

   convert_in_tempdir = in_temp_if_list(infile_cwd(convert))

Same as |dcx.convert|,
but creates temporary folder for a list of lines infile argument.

::

    >>> tmpfile = convert_in_tempdir("""digraph {
    ... %for i in range(3):
    ...    "From {{i}}" -> "To {{i}}";
    ... %end
    ...    }""".splitlines(), outinfo='dot')
    >>> stem_ext(tmpfile)[1]
    '.png'
    >>> tmpfile = convert_in_tempdir("""
    ... This is re{{'st'.upper()}}
    ...
    ... .. `xx`:
    ...
    ... xx:
    ...     text
    ...
    ... """.splitlines(), outinfo='rst_html')
    >>> stem_ext(tmpfile)[1]
    '.html'


.. _`dcx.rindices`:

:dcx.rindices:

.. code-block:: py

   def rindices(regex, lns):

Return the indices matching the regular expression ``regex``.

:param regex: regular expression string or compiled
:param lns: lines

::

    >>> lns=['a','ab','b','aa']
    >>> [lns[i] for i in rindices(r'^a\w*', lns)]==['a', 'ab', 'aa']
    True


.. _`dcx.rlines`:

:dcx.rlines:

.. code-block:: py

   def rlines(regex, lns):

Return the lines matched by ``regex``.

:param regex: regular expression string or compiled
:param lns: lines


.. _`dcx.doc_parts`:

:dcx.doc_parts:

.. code-block:: py

   def doc_parts(
           lns,
           relim=r"^\s*r?'''([\w.:]*)\s*\n*$",
           reid=r"\s(\w+)[(:]|(\w+)\s\=",
           reindent=r'[^#/\s]',
           signature=None,
           prefix=''
           ):

``doc_parts()`` yields doc parts delimeted by ``relim`` regular expression
possibly with id, if ``reid`` matches

If start and stop differ use regulare expression ``|`` in ``relim``.

- There is no empty line between doc string
  and preceding code lines that should be included.
- There is no empty line between doc string
  and succeeding code lines that should be included.
- Included code lines end with an empty line.

In case of ``__init__()`` the ID can come from the ``class`` line
and the included lines can be those of ``__init__()``,
if there is no empty line between the doc string
and ``class`` above as well as ``_init__()`` below.

If the included code comes only from one side of the doc string,
have an empty line at the other side.

Immediately after the initial doc string marker
there can be a prefix, e.g. ``classname.``.

:param lns: list of lines
:param relim: regular expression marking lines enclosing the documentation.
    The group is a prefix.
:param reid: extract id from preceding or succeeding non-empty lines
:param reindent: determines start of text
:param signature: if signature language is given the preceding
    or succeeding lines will be included
:param prefix: prefix to make id unique, e.g. module name. Include the dot.

::

    >>> with open(__file__) as f:
    ...     lns = f.readlines()
    ...     docparts = list(doc_parts(lns, signature='py'))
    ...     doc_parts_line = rlines('doc_parts', docparts)
    >>> doc_parts_line[1]
    ':doc_parts:\n'


.. _`dcx.rstincluded`:

:dcx.rstincluded:

.. code-block:: py

   @_memoized
   def rstincluded(
           fn,
           paths=(),
           withimg=False,
           withrest=False
           ):

Yield the files recursively included from an RST file.

:param fn: file name without path
:param paths: paths where to look for fn
:param withimg: also yield image files, not just other rst files
:param withrest: rest files are not supposed to be included

::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> list(rstincluded('ra.rest',('../doc',)))
    ['ra.rest.stpl', '_links_sphinx.rst']
    >>> list(rstincluded('sr.rest',('../doc',)))
    ['sr.rest', '_links_sphinx.rst']
    >>> list(rstincluded('meta.rest',('../doc',)))
    ['meta.rest', 'files.rst', '_traceability_file.rst', '_links_...']
    >>> 'dd.rest' in list(rstincluded(
    ... 'index.rest',('../doc',), False, True))
    True
    >>> cd(olddir)


.. _`dcx.pair`:

:dcx.pair:

.. code-block:: py

   def pair(alist, blist, cmp):

pair two sorted lists
where the second must be at least as long as the first

:param alist: first list
:param blist: second list longer or equal to alist
:param cmp: compare function

::

    >>> alist=[1,2,4,7]
    >>> blist=[1,2,3,4,5,6,7]
    >>> cmp = lambda x,y: x==y
    >>> list(pair(alist,blist,cmp))
    [(1, 1), (2, 2), (None, 3), (4, 4), (None, 5), (None, 6), (7, 7)]

    >>> alist=[1,2,3,4,5,6,7]
    >>> blist=[1,2,3,4,5,6,7]
    >>> cmp = lambda x, y: x==y
    >>> list(pair(alist, blist, cmp))
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]


.. _`dcx.gen`:

:dcx.gen:

.. code-block:: py

   def gen(
           source,
           target=None,
           fun=None,
           **kw
           ):

Take the ``gen_[fun]`` functions
enclosed by ``#def gen_[fun](lns,**kw)`` to create a new file.

:param source: either a list of lines of a path to the source code
:param target: either save to this file
    or return the generated documentation
:param fun: use ``#gen_<fun>(lns,**kw):`` to extract the documtenation
:param kw: kw arguments to the gen_<fun>() function

::

    >>> source=[i+'\\n' for i in """
    ...        #def gen(lns,**kw):
    ...        #  return [l.split('#@')[1] for l in rlines(r'^\s*#@', lns)]
    ...        #def gen
    ...        #@some lines
    ...        #@to extract
    ...        """.splitlines()]
    >>> [l.strip() for l in gen(source)]
    ['some lines', 'to extract']


.. _`dcx.parsegenfile`:

:dcx.parsegenfile:

.. code-block:: py

   def parsegenfile(genpth):

Parse the file ``genpth`` which has format ::

  sourcefile | targetfile | suffix | kw paramams or {}

``suffix`` refers to ``gen_<suffix>``.

The yields are used for the |dcx.gen| function.

:param genpth: path to gen file


.. _`dcx.RstFile.__init__`:

:dcx.RstFile.__init__:

.. code-block:: py

   class RstFile:
       def __init__(self, reststem, doc, tgts, lnks, nlns):


Contains the targets for a ``.rst`` or ``.rest`` file.

:param reststem: .rest file this doc belongs to (without extension)
:param doc: doc belonging to reststem,
    either included or itself (.rest, .rst, .stpl)
:param tgts: list of Tgt objects yielded by |dcx.RstFile.make_tgts|.
:param lnks: list of (line index, target name (``|target|``)) tuples
:param nlns: number of lines of the doc


.. _`dcx.RstFile.make_tgts`:

:dcx.RstFile.make_tgts:

.. code-block:: py

       @staticmethod
       def make_tgts(
               lns,
               doc,
               counters=None,
               fn_i_ln=None
               ):


Yields ``((line index, tag address), target, link name)``
of ``lns`` of a restructureText file.
For a .stpl file the linkname comes from the generated .rest file.

:lns: lines of the document
:doc: the rst document
:counters: if None, the starts with
    {".. figure":1,".. math":1,".. table":1,".. code":1}
:fn_i_ln: (fn, i, ln) of the .stpl with all stpl includes sequenced


.. _`dcx.links_and_tags`:

:dcx.links_and_tags:

.. code-block:: py

   def links_and_tags(adir):

Creates _links_xxx.rst`` files and a ``.tags``.

:param adir: directory for which to create links and tags

::

    >>> olddir = os.getcwd()
    >>> dry_run(False, False)
    >>> cd(dirname(__file__))
    >>> rmrf('../doc/_links_sphinx.rst')
    >>> '_links_sphinx.rst' in ls('../doc')
    False

    >>> links_and_tags('../doc')
    >>> '_links_sphinx.rst' in ls('../doc')
    True
    >>> cd(olddir)


.. _`dcx.mktree`:

:dcx.mktree:

.. code-block:: py

   def mktree(tree):


Build a directory tree from a string as returned by the tree tool.

:param tree: tree string as list of lines

The level is determined by the identation.

This is not thread-safe.

Leafs:

- ``/`` or ``\\`` to make a directory leaf

- ``<<`` to copy file from internet using ``http://`` or locally using ``file:://``

- use indented lines as file content

Example::

    >>> tree="""
    ...          a
    ...          ├aa.txt
    ...            this is aa
    ...          └u.txt<<http://docutils.sourceforge.net/docs/user/rst/quickstart.txt
    ...          b
    ...          ├c
    ...          │└d/
    ...          ├e
    ...          │└f.txt
    ...          └g.txt
    ...            this is g
    ...       """.splitlines()
    >>> #mktree(tree)


.. _`dcx.tree`:

:dcx.tree:

.. code-block:: py

   def tree(
            path,
            with_content=False,
            with_files=True,
            with_dot_files=True,
            max_depth=100
            ):

Inverse of mktree.
Like the linux tree tool, but optionally with content of files

:param path: path of which to create the tree string
:param with_content: use this only if all the files are text
:param with_files: else only directories are listed
:param with_dot_files: also include files starting with .
:param max_depth: max directory depth to list

::

    >>> path = dirname(__file__)
    >>> tree(path,False,max_depth=1).startswith('├─')
    True


.. _`dcx.initroot`:

:dcx.initroot:

.. code-block:: py

   def initroot(
           rootfldr,
           sampletype
           ):

Creates a sample tree in the file system
based on the ``example_tree`` and the ``example_stp_subtree`` in dcx.py.

rootfldr: directory name that becomes root of the sample tree
sampletype: either 'stpl' for the templated sample tree, or 'rest'


.. _`dcx.index_dir`:

:dcx.index_dir:

.. code-block:: py

   def index_dir(root):

Index a directory.

:param root: All subdirectories of ``root`` that contain a ``.rest`` or ``.rest.stpl`` file are indexed.

- expands the .stpl files
- generates the files as defined in the ``gen`` file (see example in dcx.py)
- generates ``_links_xxx.rst`` for xxx = {sphinx latex html pdf docx odt}
- generates ``.tags`` with jumps to reST targets

If dcx.verbose is set to True the indexed files are printed.


.. _`dcx.main`:

:dcx.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstdcx| shell command.

