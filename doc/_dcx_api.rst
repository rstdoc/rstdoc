API
---

.. code-block:: py

   import rstdoc.dcx as dcx


The functions in ``dcx.py``
are available to the ``gen_xxx(lns,**kw)`` functions (|dhy|).


.. _`dcx.is_project_root_file`:

:dcx.is_project_root_file:

.. code-block:: py

   def is_project_root_file(filename):

.. code-block:: py

       return filename=='.git' or filename=='waf' or filename=='Makefile' or filename.lower().startswith('readme')

Identifies the root of the project by a file name contained there.


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
and is overriden by an updir ``conf.py``.

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


.. _`dcx.up_dir`:

:dcx.up_dir:

.. code-block:: py

   def up_dir(match,start=None):

Find a parent path producing a match on one of its entries.
Without a match an empty string is returned.

:param match: a function returning a bool on a directory entry
:param start: absolute path or None
:return: directory with a match on one of its entries

>>> up_dir(lambda x: False)
''


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

:param infile: .txt, .rst, .rest filename
:param outfile: the path to the target file (not target directory)
:param outtype: html, latex,... or any other sphinx writer
:param config: keys from config_defaults

::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> cd('../doc')

    >>> infile, outfile = ('index.rest',
    ... '../build/doc/sphinx_html/index.html')
    >>> rst_sphinx(infile, outfile) #doctest: +ELLIPSIS
    >>> exists(outfile)
    True

    >>> infile, outfile = ('dd.rest',
    ... '../build/doc/sphinx_html/dd.html')
    >>> rst_sphinx(infile, outfile) #doctest: +ELLIPSIS
    >>> exists(outfile)
    True

    >>> infile, outfile = ('dd.rest',
    ... '../build/doc/sphinx_latex/dd.tex')
    >>> rst_sphinx(infile, outfile) #doctest: +ELLIPSIS
    >>> exists(outfile)
    True

    >>> cd(olddir)


.. _`dcx.g_include`:

:dcx.g_include:

.. code-block:: py

   g_include = []

One can append paths to ``rstdoc.dcx.g_include`` for stpl expansion
or finding other files.

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

According to
`C066363e.pdf <https://standards.iso.org/ittf/PubliclyAvailableStandards/c066363_ISO_IEC_26300-1_2015.zip>`__
it should work.

See ``utility.rst.tpl`` in the ``--stpl`` created example project tree.


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
      ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


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
:param outfile: if not provided, the input file with
              ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


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
    ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


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
    ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


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
    ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


.. _`dcx.pygpng`:

:dcx.pygpng:

.. code-block:: py

   @png_post_process_if_any
   @normoutfile
   @readin
   @infile_cwd
   def pygpng(
           infile, outfile=None, *args,
           **kwargs
           ):

Converts a .pyg file to a png file.

``.pyg`` contains python code that produces a graphic.
If the python code defines a ``to_svg`` or a ``save_to_png`` function,
then that is used.
Else the following is tried

- ``pyx.canvas.canvas`` from the
  `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or
- ``svgwrite.drawing.Drawing`` from the
  `svgwrite <https://svgwrite.readthedocs.io>`__ library or
- ``cairocffi.Surface`` from
  `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html#basic-usage>`__
- `matplotlib <https://matplotlib.org>`__.
  If ``matplotlib.pyplot.get_fignums()>1``
  the figures result ``<name><fignum>.png``

:param infile: a .pyg file name or list of lines
    (provide outfile in the latter case)
:param outfile: if not provided the input file with new extension
    ``.png`` in ``./_images``, ``<updir>/_images`` or parallel to infile.


.. _`dcx.pygsvg`:

:dcx.pygsvg:

.. code-block:: py

   @readin
   @infile_cwd
   def pygsvg(infile, *args, **kwargs):

Converts a .pyg file or according python code to an svg string.

``.pyg`` contains python code that produces an SVG graphic.
Either there is a ``to_svg()`` function or
the following is tried

- ``io.BytesIO`` containing SVG, e.g via ``cairo.SVGSurface(ioobj,width,height)``
- ``io.StringIO`` containing SVG
- object with attribute ``_repr_svg_``
- ``svgwrite.drawing.Drawing`` from the
  `svgwrite <https://svgwrite.readthedocs.io>`__ library or
- ``cairocffi.SVGSurface`` from
  `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html#basic-usage>`__
- `matplotlib <https://matplotlib.org>`__.

:param infile: a .pyg file name or list of lines


.. _`dcx.svgembed`:

:dcx.svgembed:

.. code-block:: py

   def svgembed(
           pyg_or_svg, outinfo, *args, **kwargs
           ):

If ``outinfo`` ends with ``html``, SVG is embedded.
Else the SVG is converted to a temporary image file
and included in the DOCX or ODT zip.


.. _`dcx.pngembed`:

:dcx.pngembed:

.. code-block:: py

   def pngembed(
           pyg_or_pngfile, outinfo, *args, **kwargs
           ):

If ``outinfo`` ends with ``html``, the PNG is embedded.
Else the PNG is included in the DOCX or ODT zip.


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

``.stpl`` is unrestrained python:

- e.g. one can create temporary images,
  which are then included in the final .docx of .odt
  See |dcx.tempdir|.

:param infile: a .stpl file name or list of lines
:param outfile: if not provided the expanded is returned
:param lookup: lookup paths can be absolute or relative to infile

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
           fn_i_ln=None,
           **kwargs
           ):

Default interpreted text role is set to math.
The link lines are added to the rest file or rst lines

:param infile: a .rest, .rst, .txt file name or list of lines

:param outfile: None and '-' mean standard out.

    If io.StringIO, then the lines are returned.
    ``|xxx|`` substitutions for reST link targets
    in infile are appended if no ``_links_sphinx.rst`` there

:param outinfo: specifies the tool to use.

    - ``html``, ``docx``, ``odt``,... via pandoc
    - ``sphinx_html``,... via sphinx
    - ``rst_html``,... via rst2xxx frontend tools

    General format of outinfo::

        [infile/][tgtfile.]docx[.]

    ``infile`` is used, if the function infile param are lines.

    ``tgtfile`` is target file used in links.

    ``tgtfile`` is the target file to create.
    A final dot tells not to create the target file.
    This is of use in the command line
    if piping a file to rstdoc then to pandoc.
    The doc will only be generated by pandoc,
    but links need to know the doc to link to already before that.

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

    >>> dorst(['hi there'], None,'html') #doctest: +ELLIPSIS
    <!DOCTYPE html>
    ...

    >>> drst=lambda x,y: dorst(x,y,None,pandoc_doc_optref={'docx':'--reference-doc doc/reference.'+y.split('.')[1]})
    >>> dorst('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
    >>> exists('ra.docx')
    True
    >>> rmrf('ra.docx')
    >>> exists('ra.docx')
    False
    >>> rmrf('ra.rest.stpl.rest')
    >>> exists('ra.rest.stpl.rest')
    False

    >>> dorst(['hi there'],'test.html') #doctest: +ELLIPSIS
    >>> exists('test.html')
    True
    >>> rmrf('test.html')
    >>> exists('test.html')
    False
    >>> rmrf('rest.rest.rest')
    >>> exists('rest.rest.rest')
    False

    >>> dorst(['hi there'],'test.odt','rst') #doctest: +ELLIPSIS
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
           outinfo=None,
           **kwargs
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

    >>> convert([' ','   hi {{2+3}}!'], outinfo='rest')
    ['   .. default-role:: math\n', '\n', ' \n', '   hi 5!\n', '\n']

    >>> convert([' ','   hi {{2+3}}!'])  #doctest: +ELLIPSIS
    ['<!DOCTYPE html>\n', ...]
    >>> rmrf('rest.rest.rest')

    >>> infile, outfile, outinfo = ([
    ... "newpath {{' '.join(str(i)for i in range(4))}} rectstroke showpage"
    ... ],'tst.png','eps')
    >>> 'tst.png' in convert(infile, outfile, outinfo) #doctest: +ELLIPSIS
    True
    >>> exists('tst.png')
    True
    >>> rmrf('tst.png')
    >>> exists('tst.png')
    False

    >>> convert('ra.rest.stpl') #doctest: +ELLIPSIS
    ['<!DOCTYPE html>\n', ...

    >>> cnvrt=lambda x,y: convert(x,y,None,pandoc_doc_optref={'docx':'--reference-doc doc/reference.'+y.split('.')[1]})
    >>> cnvrt('ra.rest.stpl','ra.docx')
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
but creates temporary dir for a list of lines infile argument.

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
    ... .. _`xx`:
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

``doc_parts()`` yields doc parts delimited by ``relim`` regular expression
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
:param withimg: also yield image files, not just other RST files
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

:param source: either a list of lines or a path to the source code
:param target: either save to this file
    or return the generated documentation
:param fun: use ``#gen_<fun>(lns,**kw):`` to extract the documentation
:param kw: kw arguments to the ``gen_<fun>()`` function

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

Parse the file ``genpth`` which is either 

- python code or

- has format ::

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

:param reststem: rest file this doc belongs to (without extension)
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
For a .stpl file the linkname comes from the generated RST file.

:param lns: lines of the document
:param doc: the rst/rest document for tags
:param counters: if None, the starts with
    {".. figure":1,".. math":1,".. table":1,".. code":1}
:fn_i_ln: (fn, i, ln) of the .stpl with all stpl includes sequenced


.. _`dcx.links_and_tags`:

:dcx.links_and_tags:

.. code-block:: py

   def links_and_tags(
       scanroot='.'
       ):

Creates ``_links_xxx.rst`` files and a ``.tags``.

:param scanroot: directory for which to create links and tags

::

    >>> olddir = os.getcwd()
    >>> cd(dirname(__file__))
    >>> rmrf('../doc/_links_sphinx.rst')
    >>> '_links_sphinx.rst' in ls('../doc')
    False

    >>> links_and_tags('../doc')
    >>> '_links_sphinx.rst' in ls('../doc')
    True
    >>> cd(olddir)


.. _`dcx.grep`:

:dcx.grep:

.. code-block:: py

   def grep(
         regexp=rexkw,
         dir=None,
         exts=set(['.rst','.rest','.stpl','.tpl','.adoc','.md','.wiki','.py','.jl','.lua','.tex',
                   '.js', '.h','.c','.hpp','.cpp','.java','.cs','.vb','.r','.sh','.vim','.el',
                   '.php','.sql','.swift','.go','.rb','.m','.pl','.rs','.f90','.dart','.bib',
                   '.yml','.mm','.d','.lsp','.kt','.hs','.lhs','.ex','.scala','.clj']),
         **kwargs
   ):

.. {grep}

Uses python re to find ``regexp`` and return
``[(file,1-based index,line),...]``
in *dir* (default: os.getcwd()) for ``exts`` files

:param regexp: default is '^\s*\.\. {'
:param dir: default is current dir
:param exts: the extension of files searched


.. code-block:: py

   def yield_with_kw (kws, fn_ln_kw=None, **kwargs):

Find keyword lines in ``fn_ln_kw`` list or using grep(),
that contain the keywords in kws.

Keyword line are either of::

    .. {{{kw1,kw2
    .. {kw1,kw2}
    {{_ID3('kw1 kw2')}}
    %__ID3('kw1 kw2')
    :ID3: kw1 kw2

``..`` can also be two comment chars of popular programming languages.
This is due to ``dcx.rexkw``, which you can change.
See also ``dcx.grep()`` for the keyword parameters.

:param kws: string will be split by non-chars
:param fn_ln_kw: list of (file, line, keywords) tuples
                 or ``regexp`` for grep()

::

    >>> list(yield_with_kw('a',[('a/b',1,'a b'),('c/d',1,'c d')]))
    [(0, ['a/b', 1, 'a b'])]
    >>> list(yield_with_kw('a c',[('a/b',1,'a b'),('c/d',1,'c d')]))
    []
    >>> list(yield_with_kw('a',[('a/b',1,'a b'),('c/d',1,'a c d')]))
    [(0, ['a/b', 1, 'a b']), (1, ['c/d', 1, 'a c d'])]
    >>> kwargs={'dir':normjoin(dirname(__file__),'../test/fixtures')}
    >>> kws = 'svg'
    >>> len(list(yield_with_kw(kws,**kwargs)))
    6
    >>> kws = 'png'
    >>> len(list(yield_with_kw(kws,**kwargs)))
    7


.. _`dcx.Counter.__init__`:

:dcx.Counter.__init__:

.. code-block:: py

   class Counter:
       def __init__(self, before_first=0):


Counter object.

:param before_first: first-1 value

::

    >>> myc = Counter()
    >>> myc()
    1
    >>> myc()
    2


.. _`dcx.x`:

:dcx.x:

.. code-block:: py

   gpdtid = pdtid
   def pdtAAA(pdtfile,dct,pdtid=pdtid,
               pdtfileid=lambda x:'ipdt'[int(x[0])]):

``pdtAAA`` is for use in an ``.stpl`` document::

    % pdtAAA(__main_file__,globals())

See the example generated with::

    rstdoc --ipdt

:param pdtfile: file path of pdt
:param dct: dict to take up the generated defines
:param pdtid: function returning the ID for the ``pdt`` cycle
    or regular expression with group for full path
    or regular expression for just the base name without extension (``pdtok``)
:param pdtfileid: extracts/maps a file base name to one of the letters ipdt.
                  E.g. to have the files in order one could name them {0,1,2,3}.rest.stpl,
                  and map each to one of 'ipdt'.

A ``pdt`` is a project enhancement cycle with its own documentation.
``pdt`` stands for

- plan: why
- do: specification
- test: tests according specification

Additionally there should be an

- inform: non-technical purpose for or from external people.

There can also be *only* the ``inform`` document, if the ``pdt`` item is only informative.

The repo looks like this (preferred)::

    project repo
        pdt
            ...
            AAA
                i*.rest.stpl
                p*.rest.stpl
                d*.rest.stpl
                t*.rest.stpl

or::

    project repo
        pdt
            ...
            AAA.rst.stpl

In the first case, the ``UID`` starts with ``{i,p,d,t}AAA``.
This is useful to trace related items by their plan-do-test-aspect.

Further reading: `pdt <https://github.com/rpuntaie/pdt>`__

``pdtAAA`` makes these Python defines:

- ``_[x]AAA`` returns next item number as AAABB. Use: ``{{_[x]AAA('kw1')}}``
- ``_[x]AAA_``, ``_[x]AAA__``, ``_[x]AAA___``, ... returns headers. Use: ``{{_[x]AAA_('header text')}}``
- ``__[x]AAA``, same as ``_[x]AAA``, but use: ``%__[x]AAA('kw1')`` (needs _printlist in dct)
- ``__[x]AAA_``, ``__[x]AAA__``, ``__[x]AAA___``, ... Use: ``%__[x]AAA_('header text')``

A, B are base36 letters and x is the initial of the file.
The generated macros do not work for indented text, as they produce line breaks in RST text.

::

    >>> dct={'_printlist':str}
    >>> pdtfile = "a/b/a.rest.stpl"
    >>> pdtAAA(pdtfile,dct,pdtid=r'.*/(.)\.rest\.stpl')
    >>> dct['_a']('x y').strip()
    '.. {a01 x y}\\n\\na01: **x y**'
    >>> dct['__a']('x y').strip() #needs _printlist
    "['\\\\n.. {a02 x y}\\\\n\\\\na02: **x y**', '\\\\n']"
    >>> dct={}
    >>> pdtfile = "pdt/000/d.rest.stpl"
    >>> pdtAAA(pdtfile,dct)
    >>> dct['_d000']('x y').strip()
    '.. {d00001 x y}\\n\\nd00001: **x y**'
    >>> dct={}
    >>> pdtfile = "a/b/003.rest.stpl"
    >>> pdtAAA(pdtfile,dct)
    >>> dct['_003']('x y').strip()
    '.. {00301 x y}\\n\\n00301: **x y**'
    >>> dct['_003_']('x y')
    '\\n.. {003 x y}\\n\\n003 x y\\n======='
    >>> pdtfile="a/b/003/d.rest.stpl"
    >>> pdtAAA(pdtfile,dct)
    >>> dct['_003']('x y').strip()
    '.. {00301 x y}\\n\\n00301: **x y**'
    >>> dct['_d003']('x y').strip()
    '.. {d00301 x y}\\n\\nd00301: **x y**'
    >>> dct['_003_']('x y')
    '\\n.. {003 x y}\\n\\n003 x y\\n======='
    >>> dct['_d003_']('x y')
    '\\n.. {d003 x y}\\n\\nd003 x y\\n========'


.. _`dcx.index_toctree`:

:dcx.index_toctree:

.. code-block:: py

   def index_toctree(index_file):

Construct::

    .. toctree::
        file1
        file2

for the sphinx index file,
i.e. ``index.rest.stpl`` or ``index.rst.stpl``.
Use like::

    {{! index_toctree(__file__) }}


.. _`dcx.initroot`:

:dcx.initroot:

.. code-block:: py

   def initroot(
           rootfldr
           ,sampletype
           ):

Creates a sample tree in the file system.

:param rootfldr: directory name that becomes root of the sample tree
:param sampletype: either 'ipdt' or 'stpl' for templated sample trees, or 'rest' or 'over' for non-templated

See ``example_rest_tree``, ``example_stpl_subtree``, ``example_ipdt_tree``, ``example_over_tree`` in dcx.py.


.. _`dcx.index_dir`:

:dcx.index_dir:

.. code-block:: py

   def index_dir(
       root='.'
       ):

Index a directory.

:param root: All subdirectories of ``root`` that contain a ``.rest`` or ``.rest.stpl`` file are indexed.

- expands the .stpl files
- generates the files as defined in the ``gen`` file (see example in dcx.py)
- generates ``_links_xxx.rst`` for xxx = {sphinx latex html pdf docx odt}
- generates ``.tags`` with jumps to reST targets


.. _`dcx.main`:

:dcx.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstdcx| shell command.

