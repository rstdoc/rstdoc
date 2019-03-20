# !/usr/bin/env python
# encoding: utf-8

# #### THIS GETS EXECUTED VIA GEN FILE #######
# #lns=open(__file__).readlines()
# #list(gen_head(lns))
# def gen_head(lns,**kw):
#    dl = list(rindices('^"""', lns))
#    yield from lns[dl[0]+1:dl[1]]
#    yield from lns[dl[-2]+1:dl[-1]]
# def gen_head
# #list(gen_api(lns))
# def gen_api(lns,**kw):
#    yield from doc_parts(lns, signature='py', prefix='dcx.')
# def gen_api
# #### THIS GETS EXECUTED VIA GEN FILE #######

# pylama: ignore=E402,E722,C901,W605,E101,E501,W191

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import OrderedDict, defaultdict
from hashlib import sha1 as sha
from binascii import b2a_base64
import pygal
import pyx
import stpl
from docutils.core import publish_file, publish_string
from argparse import Namespace
from types import GeneratorType
from itertools import tee
from functools import lru_cache, wraps, partial, reduce
from urllib import request
from threading import RLock
import tempfile
import subprocess as sp
import atexit
import contextlib
import shutil
import os
import io
import re
import sys
import codecs

"""
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
  then that is used, to create a png.
  Else the following is tried

  - ``pyx.canvas.canvas`` from the
    `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or
  - ``cairocffi.Surface`` from
    `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html>`__
  - ``pygal.Graph`` from `pygal <https://pygal.org>`__
  - `matplotlib <https://matplotlib.org>`__.
    If ``matplotlib.pyplot.get_fignums()>1``
    the figures result in ``<name><fignum>.png``

  The same code or the file names can be used in a ``.rest.stpl`` file
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


"""

'''
API
---

.. code-block:: py

   import rstdoc.dcx as dcx


The functions in ``dcx.py``
are available to the ``gen_xxx(lns,**kw)`` functions (|dhy|).

'''

try:
    import svgwrite.drawing
except:
    print('Warning: no svgwrite')
    svgwrite = None

try:
    import pyfca
except:
    print('Warning: no pyfca for traceability diagram')
    pyfca = None

try:
    import cairocffi
    import cairosvg
except:
    print('Warning: no cairocffi')
    cairocffi = None
    cairosvg = None

try:
    import sphinx_bootstrap_theme
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
except:
    html_theme_path = ''


class RstDocError(Exception):
    pass


_plus = '+'
_indent = '    '
_indent_text = lambda txt: '\n'.join(_indent+x for x in txt.splitlines())


class _ToolRunner:
    def svg2png(self, *args, **kwargs):
        if cairosvg:
            cairosvg.svg2png(*args, **kwargs)
        else:
            print(
              'Warning: You need cairocffi and cairosvg to convert svg to png'
            )

    def run(self, *args, **kwargs):
        if 'outfile' in kwargs:
            del kwargs['outfile']
        return sp.run(*args, **kwargs)


_toolrunner = _ToolRunner()

def opnwrite(filename):
    return open(filename, 'w', encoding='utf-8', newline='\n')


def opn(filename):
    return open(filename, encoding='utf-8')


isfile = os.path.isfile


def abspath(x):
    return os.path.abspath(x).replace('\\', '/')


isabs = os.path.isabs


def relpath(x, start=None):
    try:
        return os.path.relpath(x, start=start).replace('\\', '/')
    except ValueError:
        return abspath(x)


def dirname(x):
    return os.path.dirname(x).replace('\\', '/')

base = os.path.basename

def dir_base(x):
    return [e.replace('\\', '/') for e in os.path.split(x)]


def stem(x):
    return os.path.splitext(x)[0].replace('\\', '/')


def stem_ext(x):
    return [e.replace('\\', '/') for e in os.path.splitext(x)]


exists = os.path.exists


def cwd():
    return os.getcwd().replace('\\', '/')


mkdir = partial(os.makedirs, exist_ok=True)
cd = os.chdir
cp = shutil.copy


def ls(x='.'):
    return [e for e in sorted(os.listdir(x))]


def rmrf(x):
    try:
        if os.path.isdir(x):
            shutil.rmtree(x)
        else:
            os.remove(x)
    except:
        pass


def filenewer(infile, outfile):
    res = True
    try:
        res = os.path.getmtime(infile) > os.path.getmtime(outfile)
    except:
        pass
    return res


def normjoin(*x):
    return os.path.normpath(os.path.join(*x)).replace("\\", "/")


def updir(fn):
    return normjoin(dirname(fn), '..', base(fn))


# fn='x/y/../y/a.b'
# updir(fn) # x\a.b
# updir('a.b') # ..\a.b
# updir('a.b/a.b') # a.b
# normjoin(fn) # x\y\a.b


'''
Used for png creation.
'''
DPI = 600

# text files
_stpl = '.stpl'
_tpl = '.tpl'
_rest = '.rest'
_rst = '.rst'
_txt = '.txt'


def is_rest(x):
    return x.endswith(_rest) or x.endswith(_rest + _stpl)


def is_rst(x):
    return x.endswith(_rst) or x.endswith(_rst + _stpl) or x.endswith(
        _rst + _tpl)


# graphic files
_svg = '.svg'
_tikz = '.tikz'
_tex = '.tex'
_dot = '.dot'
_uml = '.uml'
_eps = '.eps'
_pyg = '.pyg'
_png = '.png'  # target of all others


def _is_graphic(t):
    return t != '' and any(x.endswith(t) for x in graphic_extensions)


rextgt = re.compile(
    r'(?:^|^[^\.\%\w]*\s|^\s*\(?\w+[\)\.]\s)\.\. _`?(\w[^:`]*)`?:\s*$')
# no need to consider those not starting with \w,
# because rexlinksto starts with \w
rexsubtgt = re.compile(
    r'(?:^|^[^\.\%\w]*\s|^\s*\(?\w+[\)\.]\s)\.\. \|(\w[^\|]*)\|\s\w+::')
rextitle = re.compile(r'^([!"#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~])\1+$')
rexitem = re.compile(r'^\s*:?\**(\w[^:\*]*)\**:\s*.*$')
rexoneword = re.compile(r'^\s*(\w+)\s*$')
rexname = re.compile(r'^\s*:name:\s*(\w.*)*$')
rexlnks = re.compile(r'(?:^|[^a-zA-Z`])\|(\w+)\|(?:$|[^a-zA-Z`])')
reximg = re.compile(r'(?:image|figure):: ((?:\.|/|\\|\w).*)')
rerstinclude = re.compile(r'\.\. include::\s*([\./\w\\].*)')
restplinclude = re.compile(r"""%\s*include\s*\(\s*["']([^'"]+)['"].*\)\s*""")
rexkw = re.compile(r'^\s*\.\. {')
rexkwsplit = re.compile(r'[\W_]+')

_rstlinkfixer = re.compile('#[^>]+>')


def _rst_id_fixer(matchobj):
    return matchobj.group(0).replace(' ', '-').replace('_', '-')


def _rst_id_fix(linktxt):
    return _rstlinkfixer.sub(_rst_id_fixer, linktxt, re.MULTILINE)


@lru_cache()
def here_or_updir(fldr, file):
    """
    return type:
      - fldr/file or fldr/../file, depending on where file is
      - 0 not there, 1 in fldr, 2 updir
    """
    filepth = normjoin(fldr, file)
    there = 1
    if not exists(filepth):
        filepth = updir(filepth)
        if exists(filepth):
            there = 2
        else:
            there = 0
    return (filepth, there)


# master_doc and latex_documents is determined automatically
sphinx_config_keys = """
    project
    author
    copyright
    version
    release
    html_theme
    html_theme_path
    latex_elements
    html_extra_path
    """.split()

latex_elements = {
    'preamble':
    r"""
\usepackage{pgfplots}
\usepackage{unicode-math}
\usepackage{tikz}
\usepackage{caption}
\captionsetup[figure]{labelformat=empty}
\usetikzlibrary{
  arrows,snakes,backgrounds,patterns,matrix,shapes,
  fit,calc,shadows,plotmarks,intersections
  }
"""
}

tex_wrap = r"""
\documentclass[12pt, tikz]{standalone}
\usepackage{amsmath}
""" + latex_elements['preamble'] + r"""
\pagestyle{empty}
\begin{document}
%s
\end{document}
"""


def target_id_group(targetid):
    return targetid[0]


target_id_color = {
    "ra": ("r", "lightblue"),
    "sr": ("s", "red"),
    "dd": ("d", "yellow"),
    "tp": ("t", "green")
}

_images = '_images'
# used for _traceability_file.rst and _traceability_file.svg
_traceability_file = '_traceability_file'
html_extra_path = [_traceability_file + '.svg']
pandoc_doc_optref = {
    'latex': '--template reference.tex',
    'html': {},  # each can also be dict of file:template
    'pdf': '--template reference.tex',
    'docx': '--reference-doc reference.docx',
    'odt': '--reference-doc reference.odt'
}
_pandoc_latex_pdf = [
    '--listings', '--number-sections', '--pdf-engine', 'xelatex', '-V',
    'titlepage', '-V', 'papersize=a4', '-V', 'toc', '-V', 'toc-depth=3', '-V',
    'geometry:margin=2.5cm'
]
pandoc_opts = {
    'pdf': _pandoc_latex_pdf,
    'latex': _pandoc_latex_pdf,
    'docx': [],
    'odt': [],
    'html': ['--mathml', '--highlight-style', 'pygments']
}
rst_opts = {  # http://docutils.sourceforge.net/docs/user/config.html
    'strip_comments': True,
    'report_level': 3,
    'raw_enabled': True
}

# ``list-table`` and ``code-block`` are converted to ``table`` and ``code``


def make_counters():
    return {".. figure": 1, ".. math": 1, ".. table": 1, ".. code": 1}


def name_from_directive(directive, count):
    return directive[0].upper() + directive[1:] + ' ' + str(count)


config_defaults = {
    'project': 'Project',
    'author': 'Project Team',
    'copyright': '2019, Project Team',
    'version': '1.0',
    'release': '1.0.0',
    'html_theme': 'bootstrap',
    'html_theme_path': html_theme_path,
    'latex_elements': latex_elements,
    'tex_wrap': tex_wrap,
    'target_id_group': target_id_group,
    'target_id_color': target_id_color,
    'pandoc_doc_optref': pandoc_doc_optref,
    'pandoc_opts': pandoc_opts,
    'rst_opts': rst_opts,
    'name_from_directive': name_from_directive
}

sphinx_enforced = {
    'numfig': 0,
    'smartquotes': 0,
    'source_suffix': '.rest',
    'templates_path': [],
    'language': None,
    'highlight_language': "none",
    'default_role': 'math',
    'latex_engine': 'xelatex',
    'pygments_style': 'sphinx',
    'exclude_patterns': ['_build', 'Thumbs.db', '.DS_Store']
}


'''
``g_config`` can be used to inject a global config.
This overrides the defaults
and is overriden by a ``./conf.py`` or ``../conf.py`` relative to the in file.
'''
g_config = None


@lru_cache()
def conf_py(fldr):
    """
    ``defaults``, ``g_config``, ``./conf.py`` or ``../conf.py`` is used.

    """
    config = {}
    config.update(config_defaults)
    if g_config:
        config.update(g_config)
    confpypath, there = here_or_updir(fldr, 'conf.py')
    if there:
        with opn(confpypath) as f:
            config['__file__'] = abspath(confpypath)
            eval(compile(f.read(), abspath(confpypath), 'exec'), config)
    elif g_include:
        for gi in g_include:
            confpypath = normjoin(gi,'conf.py')
            if exists(confpypath):
                config['__file__'] = abspath(confpypath)
                eval(compile(f.read(), abspath(confpypath), 'exec'), config)
                break
    config.update(sphinx_enforced)
    return config


def _fillwith(u, v):
    return [x or v for x in u]


def _joinlines(lns):
    if lns[0].endswith('\n'):
        tmp = ''.join(lns)
    else:
        tmp = '\n'.join(lns)
    return tmp.replace('\r\n', '\n')


# x=b'a\r\nb'
# _nbstr(x)==b'a\nb'
def _nbstr(x):
    return x and x.replace(b'\r\n', b'\n') or b''

# x=x.decode()
# _nstr(x)=='a\nb'


def _nstr(x):
    return x and x.replace('\r\n', '\n') or ''


def cmd(cmdlist, **kwargs):
    '''
    Runs ``cmdlist`` via subprocess.run and return stdout.
    In case of problems RstDocError is raised.

    :param cmdlist: command as list
    :param kwargs: arguments forwarded to ``subprocess.run()``

    '''

    cmdstr = ' '.join(cmdlist)
    try:
        for x in 'out err'.split():
            kwargs['std' + x] = sp.PIPE
        r = _toolrunner.run(cmdlist, **kwargs)
        try:
            stdout, stderr = _nstr(r.stdout), _nstr(r.stderr)
        except:
            stdout, stderr = _nbstr(r.stdout).decode('utf-8'), _nbstr(
                r.stderr).decode('utf-8')
        if r.returncode != 0:
            raise RstDocError('Error code %s returned from \n%s\nin\n%s\n' % (
                r.returncode, cmdstr,
                cwd()) + '\n[stdout]\n%s\n[stderr]\n%s' % (stdout, stderr))
        return stdout
    except OSError as err:
        raise RstDocError(
            'Error: Cannot run ' + cmdstr + ' in ' + cwd() + str(err))


def _imgout(inf):
    inp, inname = dir_base(inf)
    infn, infe = stem_ext(inname)
    if not _is_graphic(infe) and not _is_graphic(stem_ext(infn)[1]):
        raise ValueError('%s is not an image source' % inf)
    outp, there = here_or_updir(inp, _images)
    if not there:
        outp = inp
    outname = infn + _png
    nout = normjoin(outp, outname)
    return nout


def _unioe(args):
    i, o = [None] * 2
    try:
        (i, o), a = args[:2], args[2:]
    except:
        (i,), a = args[:1], args[1:]
    return i, o, a


def png_post_process_if_any(f):
    @wraps(f)
    def png_post_processor(*args, **kwargs):
        infile, outfile, args = _unioe(args)
        if isinstance(infile, str):
            config = conf_py(dirname(infile))
            pp = config.get('png_post_processor', None)
            if pp:
                pngfile = f(infile, outfile, *args, **kwargs)
                return pp(pngfile)
            else:
                return f(infile, outfile, *args, **kwargs)
        return f(infile, outfile, *args, **kwargs)

    return png_post_processor


def _ext(x):
    return x[0] == '.' and x or '.' + x


_cdlock = RLock()


@contextlib.contextmanager
def new_cwd(apth):
    '''
    Use as::

        with new_cwd(dir):
            #inside that directory

    '''

    prev_cwd = cwd()
    _cdlock.acquire()
    cd(apth)
    try:
        yield
    finally:
        cd(prev_cwd)
        _cdlock.release()


def startfile(filepath):
    '''
    Extends the Python startfile to non-Windows platforms

    '''

    if sys.platform.startswith('darwin'):
        sp.call(('open', filepath))
    elif os.name == 'nt':  # For Windows
        os.startfile(filepath)
    elif os.name == 'posix':  # For Linux, Mac, etc.
        sp.call(('xdg-open', filepath))


def tempdir():
    '''
    Make temporary directory and register it to be removed with ``atexit``.

    This can be used inside a ``.stpl`` file
    to create images from inlined images source,
    place them in temporary file,
    and include them in the final ``.docx`` or ``.odt``.

    '''

    atmpdir = tempfile.mkdtemp()
    atexit.register(rmrf, atmpdir)
    return atmpdir


def infile_cwd(f):
    """
    Changes into the directory of the infile if infile is a file name string.
    """

    @wraps(f)
    def infilecwder(*args, **kwargs):
        infile, outfile, args = _unioe(args)
        if isinstance(infile, str):
            ndir, inf = dir_base(infile)
        else:
            ndir, inf = '', infile
        if ndir:
            if isinstance(outfile, str) and outfile != '-':
                outfile = relpath(outfile, start=ndir)
            with new_cwd(ndir):
                return f(inf, outfile, *args, **kwargs)
        return f(infile, outfile, *args, **kwargs)

    return infilecwder


def normoutfile(f, suffix=None):
    """
    Make outfile from infile by appending suffix, or, if None,
    ``.png`` in ``./_images``
    or ``../_images``  or ``./`` from infile directory.
    The outfile is returned.
    """

    @wraps(f)
    def normoutfiler(*args, **kwargs):
        infile, outfile, args = _unioe(args)
        if isinstance(infile, str):
            if not outfile:
                if not suffix or _is_graphic(suffix):
                    outfile = _imgout(infile)
                elif suffix:
                    infn, infe = stem_ext(infile)
                    outinfo = kwargs.get('outinfo', None)
                    if outinfo.startswith('sphinx'):
                        outfile = "{1}/{0}/{2}".format(
                                  outinfo, *dir_base(infn)
                                  ) + '.' + outinfo[outinfo.find('_') + 1:]
                    else:
                        if _stpl.endswith(infe):
                            infn, infe = stem_ext(infn)
                        outfile = infn
        f(infile, outfile, *args, **kwargs)
        return outfile

    return normoutfiler

def _suffix(outinfo):
    try:
        _, suf = outinfo.split('_')
    except: #noqa
        suf = outinfo
    return suf or 'html'

def _in_2_out_name(inname,outinfo):
    instem = stem(inname)
    if instem.endswith(_rest) or instem.endswith(_rst):
        instem = stem(instem)
    res = base(instem) + '.' + _suffix(outinfo).strip('.')
    return res

def in_temp_if_list(
        f,
        suffix='stpl'
        ):
    """
    Wraps f(infile, outfile) returning None
    to produce a temporary directory/file for when infile is a list of strings.
    The temporary directory/file is removed via atexit.

    :param suffix: .dot, .uml, ... or rest.stpl,...
      default it will assume stpl and use outinfo

    To make this have an effect use after ``readin``

    - includes ``normoutfile``

    If outfile is None, outfile is derived from suffix,
    which can be `rest.stpl`, `png.svg`;
    If suffix is `.svg`, ...,
    png is assumed and will be placed into ``_images``.

    """

    @wraps(f)
    def intmpiflister(*args, **kwargs):
        infile, outfile, args = _unioe(args)
        try:
            suf0, suf1 = suffix.split('.', 1)
        except: #noqa
            outinfo = kwargs.get('outinfo', 'rest')
            if _is_graphic(outinfo):
                suf0, suf1 = outinfo, suffix
            else:
                suf0, suf1 = _suffix(outinfo) + _rest, suffix
        if not isinstance(infile, str) and infile:
            if outfile and isinstance(outfile, str):
                outfile = abspath(outfile)
            atmpdir = tempdir()
            content = _joinlines(infile).encode('utf-8')
            if outfile and isinstance(outfile, str):
                infn = stem(base(outfile))
            else:
                infn = sha(content).hexdigest()
            if suf0:
                infile = normjoin(atmpdir, '.'.join([infn, suf0, suf1]))
            else:
                infile = normjoin(atmpdir, '.'.join([infn, suf1]))
            with open(infile, 'bw') as ff:
                ff.write(content)
            return normoutfile(f, suf0)(infile, outfile, *args, **kwargs)
        return normoutfile(f, suf0)(infile, outfile, *args, **kwargs)

    return intmpiflister


def readin(f):
    """
    Decorator to read in file content and pass it on to the wrapped function.

    The config is forwarded via parameters, if the file is read in.
    """

    @wraps(f)
    def readiner(*args, **kwargs):
        infile, outfile, args = _unioe(args)
        if isinstance(infile, str):
            config = conf_py(dirname(infile))
            with opn(infile) as inf:
                return f(inf.readlines(), outfile, *args, **config, **kwargs)
        return f(infile, outfile, *args, **kwargs)

    return readiner


def run_inkscape(infile,  outfile, dpi=DPI):
    '''
    Uses ``inkscape`` commandline to convert to ``.png``

    :param infile: .svg, .eps, .pdf filename string
      (for list with actual .eps or .svg data use |dcx.svgpng| or |dcx.epspng|)
    :param outfile: .png file name

    '''

    cmd([
        'inkscape', '-z',
        '--export-dpi=%s' % dpi, '--export-area-drawing',
        '--export-background-opacity=0', infile, '--export-png=' + outfile
    ],
        outfile=outfile)


@infile_cwd
def rst_sphinx(
        infile, outfile, outtype=None, **config
        ):
    '''
    Run Sphinx on infile.

    :param infile: .txt, .rst, .rest filename (normally index.rest)
    :param outfile: the path to the target file (not target directory)
    :param outtype: html,... or any other sphinx writer
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

    '''

    cfgt = {}
    cfgt.update(config_defaults)
    cfgt.update(config)

    def dfn(n, v):
        return ['-D', n + '=' + v]

    indr, infn = dir_base(infile)
    outdr, outn = dir_base(outfile)
    outnn, outne = stem_ext(outn)
    samedir = False
    if outdr == indr:
        samedir = True
    if not indr:
        indr = '.'
    cfg = {}
    cfg.update({
        k: v
        for k, v in cfgt.items() if k in sphinx_config_keys
        and 'latex' not in k and k != 'html_extra_path'
    })
    if not outtype or outtype=='html':
        if outne == '.html':
            if infn.startswith('index.'):
                outtype = 'html'
            else:
                outtype = 'singlehtml'
        elif outne == '.tex':
            outtype = 'latex'
        else:
            outtype = outne.strip('.')
    cfg.update({k: v for k, v in sphinx_enforced.items() if 'latex' not in k})
    cfg['master_doc'] = stem(infn) #rest.rest -> .rest (see rest_rest)
    # .rest.rest contains temporary modification and is used instead of .rest
    if outtype == 'html' and is_rest(cfg['master_doc']): #... not for index.rest
        cfg['master_doc'] = stem(cfg['master_doc'])
    if samedir:
        outdr = normjoin(outdr, 'sphinx_'+outtype)
        outfn = normjoin(outdr, outn)
        print('Warning: Shinx output cannot be in same directory. Using '
              + outdr)
    else:
        outfn = outfile
    latex_elements = []
    latex_documents = []
    if 'latex' in outtype:
        cfg.update({
            k: v
            for k, v in cfgt.items()
            if k in sphinx_config_keys and 'latex' in k
        })
        cfg.update({k: v for k, v in sphinx_enforced.items() if 'latex' in k})
        try:
            latex_elements = ([
                ['-D', "latex_elements.%s=%s" % (k, v.replace('\n', ''))]
                for k, v in cfg['latex_elements'].items()
            ] + [['-D', 'latex_engine=xelatex']])
        except:
            pass
        del cfg['latex_elements']
        del cfg['latex_engine']
        latex_documents = []
    extras = ['-C'] + reduce(lambda x, y: x + y, [[
        '-D', "%s=%s" % (k, (','.join(v) if isinstance(v, list) else v))
    ] for k, v in cfg.items()] + latex_elements + latex_documents)
    sphinxcmd = ['sphinx-build', '-b', outtype, indr, outdr] + extras
    cmd(sphinxcmd, outfile=outfn)
    if outtype == 'html':
        #undo duplication via temp file's see: rest_rest
        rmrf(normjoin(outdr,cfg['master_doc']+'.rest.html'))
    if 'latex' in outtype:
        texfile = next(x for x in os.listdir(outdr) if x.endswith('.tex'))
        os.rename(normjoin(outdr, texfile), outfn)
    if 'html' in outtype and 'html_extra_path' in cfgt:
        for epth in cfgt['html_extra_path']:
            try:
                if isabs(epth):
                    epth = relpath(epth, start=indr)
                cp(epth, normjoin(outdr, epth))
            except:
                pass


def _copy_images_for(infile, outfile, with_trace):
    indr = dirname(infile)
    outdr = dirname(outfile)
    imgdir, there = here_or_updir(indr, _images)
    if there == 1:
        imgdir_tgt = normjoin(outdr, _images)
    elif there == 2:
        imgdir_tgt = normjoin(dirname(outdr), _images)
    else:
        return
    if with_trace:
        tracesvg = normjoin(indr, _traceability_file + _svg)
        if exists(tracesvg):
            try:
                cp(tracesvg, normjoin(outdr, _traceability_file + _svg))
            except:
                pass
    if exists(imgdir) and imgdir != imgdir_tgt:
        if not exists(imgdir_tgt):
            mkdir(imgdir_tgt)
        for x in os.listdir(imgdir):
            frm, twd = normjoin(imgdir, x), normjoin(imgdir_tgt, x)
            docpy = filenewer(frm, twd)
            if docpy:
                try:
                    cp(frm, twd)
                except:
                    pass


g_include = []

@infile_cwd
def rst_pandoc(
        infile, outfile, outtype, **config
        ):
    '''
    Run Pandoc on infile.

    :param infile: .txt, .rst, .rest filename
    :param outfile: the path to the target document
    :param outtype: html,...
    :param config: keys from config_defaults

    '''

    cfg = {}
    cfg.update(config_defaults)
    cfg.update(config)
    pandoccmd = ['pandoc', '--standalone', '-f', 'rst'] + cfg.get(
        'pandoc_opts', {}).get(outtype, []) + [
            '-t', 'latex'
            if outtype == 'pdf' else outtype, infile, '-o', outfile
        ]
    opt_refdoc = cfg.get('pandoc_doc_optref', {}).get(outtype, '')
    if opt_refdoc:
        if isinstance(opt_refdoc, dict):
            opt_refdoc = opt_refdoc.get(base(infile), '')
        if opt_refdoc:
            refoption, refdoc = opt_refdoc.split()
            refdocfound, there = here_or_updir('.', refdoc)
            if there:
                pandoccmd.append(refoption)
                pandoccmd.append(abspath(refdocfound))
            elif g_include:
                refdoc = dir_base(refdoc)[1]
                for gi in g_include:
                    refdoctry = normjoin(gi,refdoc)
                    if exists(refdoctry):
                        pandoccmd.append(refoption)
                        pandoccmd.append(refdoctry)
                        break
    stdout = cmd(pandoccmd, outfile=outfile)
    if outtype.endswith('html') or outtype.endswith('latex'):
        _copy_images_for(infile, outfile, outtype.endswith('html'))
    elif outtype.endswith('odt'):
        PageBreakHack(outfile)
    return stdout


def _indented_default_role_math(filelines):
    """

    .. `x`:

    xlabel:

    hello

    """
    indent = ''
    i = 0
    try:
        while not filelines[i].strip():
            i = i+1
        indent = ' '*filelines[i].index(filelines[i].lstrip())
    except:
        pass
    return indent + '.. default-role:: math\n\n'


@infile_cwd
def rst_rst2(
        infile, outfile, outtype, **config
        ):
    '''
    Run the rst2xxx docutils fontend tool on infile.

    :param infile: .txt, .rst, .rest filename
    :param outfile: the path to the target document
    :param outtype: html,...
    :param config: keys from config_defaults

    '''

    cfg = {}
    cfg.update(config_defaults)
    cfg.update(config)
    destination_path = outfile if outfile != '-' else None
    if outtype == 'odt':
        outtype = 'odf_odt'
    stdout = None
    if isinstance(infile, str):
        publish_file(
            source_path=infile,
            destination_path=destination_path,
            writer_name=outtype,
            settings_overrides=cfg['rst_opts'])
    else:
        source = _indented_default_role_math(infile) + _joinlines(infile)
        stdout = publish_string(
            source,
            destination_path=destination_path,
            writer_name=outtype,
            settings_overrides=cfg['rst_opts'])
    if destination_path:
        if outtype.endswith('html') or outtype.endswith('latex'):
            _copy_images_for(infile, outfile, outtype.endswith('html'))
        elif outtype.endswith('odt'):
            PageBreakHack(destination_path)
    return stdout


def PageBreakHack(destination_path):
    '''
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

    '''

    from zipfile import ZipFile
    odtzip = OrderedDict()
    with ZipFile(destination_path) as z:
        for n in z.namelist():
            with z.open(n) as f:
                content = f.read()
                if n == 'content.xml':
                    # break-after produces two page breaks
                    content = content.replace(
                        b'</office:automatic-styles>', b' '.join(
                            x.strip() for x in b"""<style:style
                      style:name="PageBreak"
                      style:family="paragraph"
                      style:master-page-name="rststyle-pagedefault"
                      style:parent-style-name="Standard">
                      <style:paragraph-properties fo:break-before="page"/>
                      </style:style>
                      </office:automatic-styles>""".splitlines()))
                    content = content.replace(
                        b'<office:text>',
                        b'<office:text text:use-soft-page-breaks="true">')
            odtzip[n] = content
    with ZipFile(destination_path, 'w') as z:
        for n, content in odtzip.items():
            with z.open(n, mode='w', force_zip64=True) as f:
                f.write(content)


# sphinx_html, rst_html, [pandoc_]html
rst_tools = {'pandoc': rst_pandoc, 'sphinx': rst_sphinx, 'rst': rst_rst2}


@png_post_process_if_any
@normoutfile
@readin
def svgpng(infile, outfile=None, *args, **kwargs):
    '''
    Converts a .svg file to a png file.

    :param infile: a .svg file name or list of lines
    :param outfile: if not provided the input file with new extension
      ``.png`` either in ``./_images`` or ``../_images`` or ``.``

    '''

    _toolrunner.svg2png(
        bytestring=_joinlines(infile),
        write_to=outfile,
        dpi=kwargs.get('DPI', DPI))


@png_post_process_if_any
@partial(in_temp_if_list, suffix='.tex')
@infile_cwd
def texpng(infile, outfile=None, *args, **kwargs):
    '''
    Latex has several graphic packages, like

    - tikz
    - chemfig

    that can be converted to .png with this function.

    For ``.tikz`` file use |dcx.tikzpng|.

    :param infile: a .tex file name or list of lines
        (provide outfile in the latter case)
    :param outfile: if not provided, the input file with .png
        either in ``./_images`` or ``../_images`` or ``.``

    '''

    pdffile = stem(infile) + '.pdf'
    try:
        cmd(['xelatex', '-interaction=nonstopmode', infile], outfile=pdffile)
    except RstDocError as err:
        with opn(infile) as latex:
            raise RstDocError(str(err) + '\n[latex]\n' + latex.read())
    run_inkscape(pdffile, outfile, dpi=kwargs.get('DPI', DPI))


def _texwrap(f):
    @wraps(f)
    def _texwraper(*args, **kwargs):
        texlns, outfile, args = _unioe(args)
        content = _joinlines(texlns)
        latex = kwargs.get('tex_wrap', tex_wrap) % content
        return f(latex.splitlines(), outfile, *args, **kwargs)

    return _texwraper


def _tikzwrap(f):
    @wraps(f)
    def _tikzwraper(*args, **kwargs):
        tikzlns, outfile, args = _unioe(args)
        content = _joinlines(tikzlns).strip()
        tikzenclose = [r'\begin{tikzpicture}', '%s', r'\end{tikzpicture}']
        if not content.startswith(tikzenclose[0]):
            content = _joinlines(tikzenclose) % content
        return f(content.splitlines(), outfile, *args, **kwargs)

    return _tikzwraper


'''
Converts a .tikz file to a png file.

See |dcx.texpng|.
'''
tikzpng = normoutfile(readin(_tikzwrap(_texwrap(texpng))))


@png_post_process_if_any
@partial(in_temp_if_list, suffix='.dot')
@infile_cwd
def dotpng(
        infile,
        outfile=None,
        *args,
        **kwargs
        ):
    '''
    Converts a .dot file to a png file.

    :param infile: a .dot file name or list of lines
        (provide outfile in the latter case)
    :param outfile: if not provided the input file with new extension
        ``.png`` either in ``./_images`` or ``../_images`` or ``./``

    '''

    cmd(['dot', '-Tpng', infile, '-o', outfile], outfile=outfile)


@png_post_process_if_any
@partial(in_temp_if_list, suffix='.uml')
@infile_cwd
def umlpng(
        infile,
        outfile=None,
        *args,
        **kwargs
        ):
    '''
    Converts a .uml file to a png file.

    :param infile: a .uml file name or list of lines
        (provide outfile in the latter case)
    :param outfile: if not provided the input file with new extension
        ``.png`` either in ``./_images`` or ``../_images`` or ``./``

    '''

    cmd(['plantuml', '-tpng', infile, '-o' + dirname(outfile)],
        shell=sys.platform == 'win32',
        outfile=outfile)


@png_post_process_if_any
@partial(in_temp_if_list, suffix='.eps')
@infile_cwd
def epspng(
        infile,
        outfile=None,
        *args,
        **kwargs):
    '''
    Converts an .eps file to a png file using inkscape.

    :param infile: a .eps file name or list of lines
        (provide outfile in the latter case)
    :param outfile: if not provided the input file with new extension
        ``.png`` either in ``./_images`` or ``../_images`` or ``./``

    '''

    run_inkscape(infile, outfile, dpi=kwargs.get('DPI', DPI))


@png_post_process_if_any
@normoutfile
@readin
@infile_cwd
def pygpng(
        infile, outfile=None, *args,
        **kwargs
        ):
    '''
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

    '''

    pygcode = _joinlines(infile)
    pygvars = {}
    dpi = kwargs.get('DPI', DPI)
    eval(compile(pygcode, outfile, 'exec'), pygvars)
    if 'save_to_png' in pygvars:
        pygvars['save_to_png'](outfile)
    else:
        for k, v in pygvars.items():
            if hasattr(v,'_repr_svg_'):
                _toolrunner.svg2png(
                    bytestring=v._repr_svg_(), write_to=outfile, dpi=dpi)
                break
            elif isinstance(v, pygal.Graph):
                _toolrunner.svg2png(bytestring=v.render(),
                                    write_to=outfile, dpi=dpi)
                break
            elif cairocffi and isinstance(v, cairocffi.Surface):
                v.write_to_png(target=outfile)
                break
            elif svgwrite and isinstance(v, svgwrite.drawing.Drawing):
                _toolrunner.svg2png(bytestring=v.tostring(),
                                    write_to=outfile, dpi=dpi)
                break
            else:  # try matplotlib.pyplot
                try:
                    fignums = plt.get_fignums()
                    if len(fignums) == 0:
                        continue
                    if len(fignums) > 1:
                        # makename('a.b', 1) # a1.b
                        def makename(x, i):
                            return ('{0}%s{1}' % i).format(*stem_ext(x))
                    else:

                        def makename(x, i):
                            return x
                    for i in fignums:
                        plt.figure(i).savefig(
                            makename(outfile, i), format='png')
                    plt.close()
                    break
                except:
                    continue

@readin
@infile_cwd
def pygsvg(infile, *args, **kwargs):
    '''
    Converts a .pyg file or according python code to an svg string.

    ``.pyg`` contains python code that produces an SVG graphic.
    Either there is a ``to_svg()`` function or
    the following is tried

    - ``io.BytesIO`` containing SVG, e.g via ``cairo.SVGSurface(ioobj,width,height)``
    - ``io.StringIO`` containing SVG
    - object with attribute ``_repr_svg_``
    - ``svgwrite.drawing.Drawing`` from the
      `svgwrite <https://svgwrite.readthedocs.io>`__ library or
    - ``cairocffi.SVGSurface`` from `cairocffi \
      <https://cairocffi.readthedocs.io/en/stable/overview.html#basic-usage>`__
    - ``pygal.Graph`` from
      `pygal <https://pygal.org>`__
    - `matplotlib <https://matplotlib.org>`__.

    :param infile: a .pyg file name or list of lines

    '''

    onlysvg = lambda x: '<svg'+x.split('<svg')[1]
    pygcode = _joinlines(infile)
    pygvars = {}
    eval(compile(pygcode, "pygsvg", 'exec'), pygvars)
    if 'to_svg' in pygvars:
        return onlysvg(pygvars['to_svg']())
    else:
        for k, v in pygvars.items():
            if hasattr(v,'_repr_svg_'):
                return onlysvg(v._repr_svg_())
            elif isinstance(v, pygal.Graph):
                return onlysvg(v.render().decode('utf-8'))
            elif cairocffi and isinstance(v, cairocffi.SVGSurface):
                v.finish()
                break #find io.BytesIO
            elif svgwrite and isinstance(v, svgwrite.drawing.Drawing):
                return v.tostring()
            else:  # try matplotlib.pyplot
                try:
                    fignums = plt.get_fignums()
                    if len(fignums) == 0:
                        continue
                    svgsrc = ""
                    for i in fignums:
                        bio = io.BytesIO()
                        plt.figure(i).savefig(bio,format='svg')
                        bio.seek(0)
                        svgsrc += onlysvg(bio.read().decode('utf-8'))
                    plt.close()
                    return svgsrc
                except:
                    continue
        for k, v in pygvars.items():
            if isinstance(v, io.BytesIO):
                v.seek(0)
                return onlysvg(v.read().decode('utf-8'))
            elif isinstance(v, io.StringIO):
                v.seek(0)
                return onlysvg(v.read())

def svgembed(
        pyg_or_svg, outinfo, *args, **kwargs
        ):
    '''
    If ``outinfo`` ends with ``html``, SVG is embedded.
    Else the SVG is converted to a temporary image file
    and included in the DOCX or ODT zip.

    '''

    try:
        svgsrc = pygsvg(pyg_or_svg)
    except Exception as e:
        svgsrc = _joinlines(pyg_or_svg)
    if outinfo.endswith('html') or outinfo.endswith('rest'):
        return '.. raw:: html\n\n'+_indent_text(svgsrc)
    else:
        svgfn = normjoin(tempdir(),'svg.png')
        svgpng(svgsrc.splitlines(),svgfn, *args, **kwargs)
        return ".. image:: {}".format(svgfn)


def _png64(pngfn):
    with open(pngfn,'rb') as f:
        b64 = b2a_base64(f.read())
        return '<img src="data:image/png;base64,{0}"/>'.format(b64.decode("utf-8"))


def pngembed(
        pyg_or_pngfile, outinfo, *args, **kwargs
        ):
    '''
    If ``outinfo`` ends with ``html``, the PNG is embedded.
    Else the PNG is included in the DOCX or ODT zip.

    '''

    pngfn = normjoin(tempdir(),'png.png')
    pygpng(pyg_or_pngfile,pngfn,*args,**kwargs)
    if outinfo.endswith('html') or outinfo.endswith('rest'):
        return '.. raw:: html\n\n'+_indent_text(_png64(pngfn))
    else:
        return ".. image:: {}".format(pngfn)


@infile_cwd
def dostpl(
        infile,
        outfile=None,
        lookup=None,
        **kwargs
        ):
    '''
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

    '''

    if not lookup:
        lookup = ['.', '..'] + g_include
    if isinstance(infile, str):
        lookup = [abspath(normjoin(dirname(infile), x)) for x in lookup]
        filename = abspath(infile)
    else:
        lookup = [abspath(x) for x in lookup]
        try:
            filename = abspath(outfile)
        except:
            filename = None
        infile = _joinlines(infile)
    variables = {}
    variables.update(globals())
    variables.update(kwargs)
    variables.update({'__file__': filename})
    if 'outinfo' not in variables and outfile:
        _, variables['outinfo'] = stem_ext(outfile)
    st = stpl.template(
        infile,
        template_settings={'escape_func': lambda x: x},
        template_lookup=lookup,
        **variables
    )
    if outfile:
        with opnwrite(outfile) as f:
            f.write(st)
    else:
        return st.replace('\r\n', '\n').splitlines(keepends=True)


def dorst(
        infile,
        outfile=io.StringIO,
        outinfo=None,
        fn_i_ln=None
        ):
    r'''
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

        >>> dorst(['hi there'], None,'html') #doctest: +ELLIPSIS
        <!DOCTYPE html>
        ...

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


    '''

    tool = 'pandoc'
    rsttool = rst_tools[tool]
    dinfo, binfo = None, None
    if outinfo:
        dinfo, binfo = dir_base(outinfo)
        outinfo = binfo
    if not isinstance(outfile, str) and outinfo in rst_tools:
        rsttool = rst_tools[outinfo]
        outinfo = 'html'
    else:
        try:
            tool, outinfo = outinfo.split('_')
            try:
                rsttool = rst_tools[tool]
            except:
                rsttool = None
        except:
            pass
    if isinstance(infile, str):
        infile = abspath(infile)
        with opn(infile) as f:
            filelines = f.readlines()
    else:
        filelines = infile
        infile = dinfo
        if not infile:
            infile = 'rest'
        infile = abspath(infile + _rest)
    sysout = None
    finalsysout = None
    try:
        if outfile is None or outfile == '-':
            if not outinfo:
                outinfo = 'rest'
            if outinfo.strip('.').find('.') < 0:
                outfile = stem(base(infile))+'.' + \
                    outinfo.strip('.')  # infile.rest - docx
            else:
                outfile = outinfo.strip('.')  # - - otherfile.docx
            if any(outinfo.endswith(x) for x in ['docx', 'odt', 'pdf']):
                sysout = None  # create a file in these cases
            else:
                try:
                    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
                except: #noqa
                    pass
                sysout = sys.stdout
        elif callable(outfile):
            sysout = outfile()
        else:
            _, ofext = stem_ext(outfile)
            ofext = ofext.strip('.')
            if not outinfo:  # x.rst a/b/c.docx
                outinfo = ofext
            elif outinfo in rst_tools:  # x.rst a/b/c.docx pandoc
                tool = outinfo
                rsttool = rst_tools[outinfo]
                outinfo = ofext
        try:
            if outinfo.endswith('.'):  # x.rest - docx.
                rsttool = None  # ... output the rest code with links for docx
            # drop file information from outinfo
            outinfo = outinfo.strip('.')
            t, outinfo = stem_ext(outinfo)
            if not outinfo:
                outinfo = t
            outinfo = outinfo.strip('.')
        except:
            outinfo = 'rest'

        if _rest.endswith(outinfo):
            rsttool = None  # no further processing wanted, sysout is final
        if not rsttool and not sysout:
            sysout = opnwrite(outfile)
        tmprestindir = None

        if rsttool:
            finalsysout = sysout
            tmprestindir = infile + _rest # .rest->rest_rest
            sysout = opnwrite(tmprestindir)
            infile = tmprestindir
            atexit.register(rmrf, tmprestindir)
        if sysout:
            sysout.write(_indented_default_role_math(filelines))
            links_done = False
            for x in filelines:
                if x.startswith('.. include:: _links_sphinx.rst'):
                    if tool == 'sphinx':
                        links_done = True
                    else:
                        linksfilename = normjoin(
                            dirname(infile), '_links_' + outinfo + '.rst')
                        if exists(linksfilename):
                            with opn(linksfilename) as f:
                                if tool == 'rst' and outinfo == 'html':
                                    sysout.write(_rst_id_fix(f.read()))
                                else:
                                    sysout.write(f.read())
                                links_done = True
                else:
                    sysout.write(x if x.endswith('\n') else x+'\n')
            if not links_done:
                sysout.write('\n')
                try:
                    filenoext = stem(outfile)
                except:
                    filenoext = ''
                for tgt in RstFile.make_tgts(filelines, infile,
                                             make_counters(), fn_i_ln):
                    sysout.write(
                        tgt.create_link(
                            outinfo.replace('rest', 'html'),
                            filenoext, tool))

        if rsttool:
            config = conf_py(dirname(infile))
            if sysout:
                sysout.close()
                sysout = None
            stdout = rsttool(infile, '-' if finalsysout else outfile,
                             outinfo, **config)
            if stdout is not None and finalsysout:
                finalsysout.write(stdout)
    finally:
        for x in [sysout, finalsysout]:
            if x is not None and x != sys.stdout and not isinstance(
                                                          x, io.StringIO):
                x.close()
        for x in [sysout, finalsysout]:
            if isinstance(x, io.StringIO):
                x.seek(0)
                return x.readlines()


converters = {
    _svg: svgpng,
    _tikz: tikzpng,
    _tex: texpng,
    _dot: dotpng,
    _uml: umlpng,
    _eps: epspng,
    _pyg: pygpng,
    _stpl: dostpl,
    _rst: dorst,
    _rest: dorst,
    _txt: dorst
}
graphic_extensions = {_svg, _tikz, _tex, _dot, _uml, _eps, _pyg}

def convert(
        infile,
        outfile=io.StringIO,
        outinfo=None
        ):
    r'''
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

        >>> convert('ra.rest.stpl','ra.docx') #doctest: +ELLIPSIS
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

    '''

    afile = False
    try:
        afile = infile and isfile(infile) or False
    except:
        pass
    if not afile and (infile == '-' or infile is None):
        try:
            sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
        except:
            pass
        infile = sys.stdin.readlines()
    if not outinfo:
        if outfile == '-':
            outinfo = 'rest'
        elif outfile is None or callable(outfile):
            outinfo = 'html'
        else:
            _,outinfo = stem_ext(outfile)
            outinfo = outinfo.strip('.')
    fext = None
    if isinstance(infile, str):
        nextinfile, fext = stem_ext(infile)
    else:
        fext = _stpl
        if outinfo and _is_graphic(outinfo):
            soi = outinfo.strip('.')
            nextinfile = soi + '.' + soi
        else:
            nextinfile = 'rest' + _rest
    fn_i_ln = None
    while fext in converters:
        if (outfile is None or callable(outfile)) and _is_graphic(fext):
                outfile = _imgout(nextinfile + fext)
        try:
            nextinfile, fextnext = stem_ext(nextinfile)
            if fextnext not in converters:
                fextnext = None
        except:
            fextnext = None
        out_ = lambda:outfile if not fextnext else None
        thisconverter = converters[fext]
        if thisconverter == dorst:
            infile = thisconverter(infile, out_(), outinfo, fn_i_ln)
        else:
            kwargs = {}
            if thisconverter == dostpl:
                kwargs = {'outinfo': outinfo}
                # save infile for dorst() in outinfo as "infile/outinfo"
                if fextnext in converters and converters[fextnext] == dorst:
                    if isinstance(infile, str):
                        fn_i_ln = _flatten_stpl_includes(infile)
                    else:
                        fn_i_ln = list(_flatten_stpl_includes_it(infile))
                    outinfo = nextinfile + '/' + (outinfo or '')
            infile = thisconverter(infile, out_(), **kwargs)
        if not infile:
            break
        if not fextnext:
            break
        fext = fextnext
    return infile


'''
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

'''
convert_in_tempdir = in_temp_if_list(infile_cwd(convert))


def rindices(regex, lns):
    r'''
    Return the indices matching the regular expression ``regex``.

    :param regex: regular expression string or compiled
    :param lns: lines

    ::

        >>> lns=['a','ab','b','aa']
        >>> [lns[i] for i in rindices(r'^a\w*', lns)]==['a', 'ab', 'aa']
        True

    '''

    regex = re.compile(regex)
    for i, ln in enumerate(lns):
        if regex.search(ln):
            yield i


def rlines(regex, lns):
    '''
    Return the lines matched by ``regex``.

    :param regex: regular expression string or compiled
    :param lns: lines

    '''

    return [lns[i] for i in rindices(regex, lns)]


def intervals(nms  # list of indices
              ):
    """
    Return intervals between numbers.

    ::

        >>> intervals([1, 2, 3])==[(1, 2), (2, 3)]
        True

    """
    return list(zip(nms[:], nms[1:]))


def in2s(nms  # list of indices
         ):
    """
    Convert the list into a list of couples of two elements.

    ::

        >>> in2s([1, 2, 3, 4])==[(1, 2), (3, 4)]
        True

    """
    return list(zip(nms[::2], nms[1::2]))


# re.search(reid,'OpenDevices = None').groups()
# re.search(reid,'def OpenDevices(None)').groups()
# re.search(reid,'class OpenDevices:').groups()
# re.search(reid,'    def __init__(a, b):').groups()
# re.search(relim,"  '''prefix. ").groups()
# re.search(relim,"  '''").groups()


def doc_parts(
        lns,
        relim=r"^\s*r?'''([\w.:]*)\s*\n*$",
        reid=r"\s(\w+)[(:]|(\w+)\s\=",
        reindent=r'[^#/\s]',
        signature=None,
        prefix=''
        ):
    r'''
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

    '''

    rlim = re.compile(relim)
    rid = re.compile(reid)
    rindent = re.compile(reindent)

    def foundid(lnsi):
        if not lnsi.strip():  # empty
            return False
        id = rid.search(lnsi)
        if id and id.groups():
            ids = [x for x in id.groups() if x is not None]
            if len(ids) > 0:
                return ids[0]

    ids = []

    def checkid(rng):
        i = None
        for i in rng:
            testid = foundid(lns[i])
            if testid is False:
                break
            elif not ids and isinstance(testid, str):
                ids.append(testid)
        return i

    for a, b in in2s(list(rindices(rlim, lns))):
        try:
            thisprefix = rlim.search(lns[a]).groups()[0]
        except:
            thisprefix = ''
        ids.clear()
        i = checkid(range(a - 1, 0, -1))
        j = checkid(range(b + 1, len(lns)))
        if ids:
            yield ''
            yield '.. _`' + prefix + thisprefix + ids[0] + '`:\n'
            yield ''
            yield ':' + prefix + thisprefix + ids[0] + ':\n'
            yield ''
        if signature:
            if i is not None and i < a and i > 0:
                if not lns[i].strip():  # empty
                    i = i + 1
                if i < a:
                    yield '.. code-block:: ' + signature + '\n'
                    yield ''
                    yield from ('   ' + x for x in lns[i:a])
                    yield ''
            if j is not None and j > b + 1 and j < len(lns):
                if not lns[j].strip():  # empty
                    j = j - 1
                if j > b:
                    yield '.. code-block:: ' + signature + '\n'
                    yield ''
                    yield from ('   ' + x for x in lns[b + 1:j + 1])
                    yield ''
        indent = 0
        for ln in lns[a + 1:b]:
            lnst = rindent.search(ln)
            if lnst and lnst.span():
                indent = lnst.span()[0]
                break
        yield from (x[indent:] for x in lns[a + 1:b])


# for generator function, instead of lru_cache()
_Tee = tee([], 1)[0].__class__


def _memoized(f):
    cache = {}

    def ret(*args):
        if args not in cache:
            cache[args] = f(*args)
        if isinstance(cache[args], (GeneratorType, _Tee)):
            cache[args], r = tee(cache[args])
            return r
        return cache[args]

    return ret


@lru_cache()
def _read_lines(fn):
    lns = []
    with opn(fn) as f:
        lns = list(f.readlines())
    return lns


@_memoized
def rstincluded(
        fn,
        paths=(),
        withimg=False,
        withrest=False
        ):
    '''
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

    '''

    p = ''
    for p in paths:
        nfn = normjoin(p, fn)
        if exists(nfn + _stpl):  # first, because original
            nfn = nfn + _stpl
            yield fn + _stpl
            break
        elif exists(nfn):  # while this might be generated
            yield fn
            break
    else:
        nfn = fn
        yield fn
    lns = _read_lines(nfn)
    toctree = False
    if lns:
        for aln in lns:
            if toctree:
                toctreedone = False
                if aln.startswith(' '):
                    fl = aln.strip()
                    if fl.endswith(_rest) and exists(normjoin(p, fl)):
                        toctreedone = True
                        yield from rstincluded(fl, paths)
                    continue
                elif toctreedone:
                    toctree = False
            if aln.startswith('.. toctree::'):
                if withrest:
                    toctree = True
            elif aln.strip().startswith('.. '):
                # aln = '  .. include:: some.rst'
                # aln = '  .. include:: ../some.rst'
                # aln = '.. include:: some.rst'
                # aln = '.. include:: ../some.rst'
                # aln = '  .. image:: some.png'
                # aln = '.. image:: some.png'
                # aln = '  .. figure:: some.png'
                # aln = '  .. |x y| image:: some.png'
                try:
                    f, t, _ = rerstinclude.split(aln)
                    nf = not f.strip() and t
                    if nf:
                        if is_rest(nf) and not withrest:
                            continue
                        yield from rstincluded(nf.strip(), paths)
                except:
                    if withimg:
                        m = reximg.search(aln)
                        if m:
                            yield m.group(1)
            elif restplinclude.match(aln):
                # aln="%include('some.rst.tpl', v='param')"
                # aln="   %include('some.rst.tpl', v='param')"
                f, t, _ = restplinclude.split(aln)
                nf = not f.strip() and t
                if nf:
                    thisnf = normjoin(p, nf)
                    if not exists(thisnf):
                        parntnf = normjoin(p, '..', nf)
                        if exists(parntnf):
                            nf = parntnf
                        else:
                            continue
                    yield from rstincluded(nf.strip(), paths)


_traceability_instance = None


class Traceability:
    def __init__(self, tracehtmltarget):
        self.tracehtmltarget = tracehtmltarget
        self.fcaobjsets = []
        global _traceability_instance
        _traceability_instance = self
        self.counters = None

    def appendobject(self, aset):
        self.fcaobjsets.append(aset)

    def isempty(self):
        return len(self.fcaobjsets) == 0

    # returns the rst lines of _traceability_file
    def create_traceability_file(self, directory):
        if not pyfca:
            return []
        if not self.fcaobjsets:
            return []
        config = conf_py(directory)
        target_id_group = config['target_id_group']
        target_id_color = config['target_id_color']

        def _drawnode(canvas, node, parent, center, radius):
            fillcolors = []
            nodetgtgrps = {target_id_group(x) for x in node.intent}
            for _, (groupid, groupcolor) in target_id_color.items():
                if groupid in nodetgtgrps:
                    fillcolors.append(groupcolor)
            n_grps = len(fillcolors)
            for i in range(n_grps - 1, -1, -1):
                rr = int(radius * (i + 1) / n_grps)
                parent.add(
                    canvas.circle(
                        center, rr, fill=fillcolors[i], stroke='black'))

        fca = pyfca.Lattice(self.fcaobjsets, lambda x: x)
        tr = 'tr'

        # |trXX|, |trYY|, ...

        def reflist(x, pfx=tr):
            return (
                '|' + pfx +
                ('|, |' + pfx).join([str(e)
                                     for e in sorted(x)]) + '|') if x else ''

        fcanodes = [(".. _`" + tr + "{0}`:\n\n:" + tr +
                     "{0}:\n\n{1}\n\nUp: {2}\n\nDown: {3}\n\n").format(
                         n.index, reflist(n.intent, ''), reflist(n.up),
                         reflist(n.down)) for n in fca.nodes]
        tlines = ''.join(fcanodes).splitlines(keepends=True)
        imgpath, there = here_or_updir(directory, _images)
        if not there:
            imgpath = normjoin(directory, _images)
            mkdir(imgpath)
        trcpath = normjoin(
            relpath(imgpath, start=directory), _traceability_file)
        # fig_traceability_file target
        tlines.extend([
            '.. _`fig' + _traceability_file + '`:\n', '\n',
            '.. figure:: ' + trcpath + '.png\n', '   :name:\n', '\n',
            '   |fig' + _traceability_file + '|: `FCA <%s>`__ %s' % (
                "https://en.wikipedia.org/wiki/Formal_concept_analysis",
                "diagram of dependencies"
                )
        ])
        if target_id_color is not None:
            legend = ', '.join(
                [fnm + " " + clr for fnm, (_, clr) in target_id_color.items()])
            tlines.extend([': ' + legend, '\n'])
        tlines.append('\n')
        with opnwrite(normjoin(directory, _traceability_file + _rst)) as f:
            f.write('.. raw:: html\n\n')
            f.write('    <object data="' + _traceability_file + _svg +
                    '" type="image/svg+xml"></object>\n')
            if target_id_color is not None:
                f.write(
                    '''    <p><a href="%s">FCA</a>
                  diagram of dependencies with clickable nodes: ''' % (
                      "https://en.wikipedia.org/wiki/Formal_concept_analysis"
                    )
                    + legend + '</p>\n\n')
            f.writelines(tlines)
        ld = pyfca.LatticeDiagram(fca, 4 * 297, 4 * 210)
        tracesvg = abspath(normjoin(directory, _traceability_file + _svg))

        def ttgt():
            return self.tracehtmltarget.endswith(_rest) and stem(
                self.tracehtmltarget) or self.tracehtmltarget

        ld.svg(
            target=ttgt() + '.html#' + tr, drawnode=_drawnode).saveas(tracesvg)
        tracepng = abspath(normjoin(imgpath, _traceability_file + '.png'))
        svgpng(tracesvg, tracepng)
        return tlines


def pair(alist, blist, cmp):
    '''
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

    '''

    i = 0
    for aa, bb in zip(alist, blist):
        if not cmp(aa, bb):
            break
        i = i + 1
        yield aa, bb
    alen = len(alist)
    tlen = max(alen, len(blist))
    d = 0
    for j in range(i, alen):
        for dd in range(tlen - j - d):
            bb = blist[j + d + dd]
            if not cmp(alist[j], bb):
                yield None, bb
            else:
                yield alist[j], bb
                d = d + dd
                break
        else:
            return


def gen(
        source,
        target=None,
        fun=None,
        **kw
        ):
    '''
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

    '''

    if isinstance(source, str):
        lns = []
        try:
            lns = _read_lines(source)
        except:
            sys.stderr.write("ERROR: {} cannot be opened\n".format(source))
            return
    else:
        lns = source
        source = ""
    if '.' not in sys.path:
        sys.path.append('.')
    if fun:
        gen_regex = r'#\s*def gen_' + fun + r'(\w*(lns,\*\*kw):)*'
    else:
        gen_regex = r'#\s*def gen(\w*(lns,\*\*kw):)*'
    iblks = list(rindices(gen_regex, lns))
    py3 = [
        lns[k][lns[i].index('#') + 1:] for i, j in in2s(iblks)
        for k in range(i, j)
    ]
    indent = py3[0].index(py3[0].lstrip())
    py3 = '\n'.join(x[indent:] for x in py3)
    eval(compile(py3, source + r'#\s*gen', 'exec'), globals())
    if fun:
        gened = list(eval('gen_' + fun + '(lns,**kw)'))
    else:  # else eval all gen_ funtions
        gened = []
        for i in iblks[0::2]:
            gencode = re.split(r"#\s*def |:", lns[i])[1]  # gen(lns,**kw)
            gened += list(eval(gencode))
    if target:
        drn = dirname(target)
        if drn and not exists(drn):
            mkdir(drn)
        with opnwrite(target) as o:
            o.write(''.join(((x or '\n') for x in gened)))
    else:
        return gened


def parsegenfile(genpth):
    '''
    Parse the file ``genpth`` which has format ::

      sourcefile | targetfile | suffix | kw paramams or {}

    ``suffix`` refers to ``gen_<suffix>``.

    The yields are used for the |dcx.gen| function.

    :param genpth: path to gen file

    '''

    try:
        genfilelns = _read_lines(genpth)
    except: #noqa
        sys.stderr.write("ERROR: {} cannot be opened\n".format(genpth))
        return

    for ln in genfilelns:
        if ln[0] != '#':
            try:
                f, t, d, a = [x.strip() for x in ln.split('|')]
                kw = eval(a)
                yield f, t, d, kw
            except:
                pass


def _flatten_stpl_includes_it(fn):
    """
    This flattens the .stpl includes
    to have all targets align to those in the .rest file.
    Targets must be *explicit* in all ``.stpl`` and ``.tpl``,
    i.e. they must not be created by stpl code.
    This is needed to make the .tags jump to the original
    and not the generated file.
    """
    flns = []
    if isinstance(fn, str):
        if exists(fn):
            flns = _read_lines(fn)
        else:
            parnt = updir(fn)
            if exists(parnt):
                flns = _read_lines(parnt)
    else:
        flns = fn
        fn = '-'
    for i, ln in enumerate(flns):
        # ln = '% include("../test.rst.stpl", v="aparam")'
        m = restplinclude.match(ln)
        if m:
            includedtpl = m.group(1)
            yield from _flatten_stpl_includes(
                normjoin(dirname(fn), includedtpl))
        else:
            yield fn, i, ln


@lru_cache()
def _flatten_stpl_includes(fn):
    return list(_flatten_stpl_includes_it(fn))


class Tgt:

    line_search_range = 8

    def __init__(
            self,
            lnidx,  # line index
            target  # target name
    ):
        self.lnidx = lnidx
        self.target = target
        self.tagentry = None  # (path, line index)
        self.lnkname = None  # link name

    def is_inside_literal(self, lns):
        try:  # skip literal blocks
            indentation = re.search(r'\w', lns[self.lnidx]).span()[0] - 3
            if indentation > 0:
                for iprev in range(self.lnidx - 1, 0, -1):
                    prev = lns[iprev]
                    if prev:
                        newspc, _ = next((ich, ch)
                                         for ich, ch in enumerate(prev)
                                         if ch != ' ' and ch != '\t')
                        if newspc < indentation:
                            prev = prev.strip()
                            if prev:
                                if not prev.startswith(
                                        '.. ') and prev.endswith('::'):
                                    return True
                                return False
        except:
            pass

    def find_lnkname(self,
                     lns,
                     counters
                     ):
        """Tgt.

        Determines the link name for this target.
        It searches the following lines for either

        :param lns: the rest linese
        :param counters: the counters for the directives (see make_counters())

        - a title
        - ``:name:`` immediately below a directive
          (a counter is used if no name is given)
        - a ``:xxx:`` or ``xxx:`` or
        - a single word ``xxx``

        """
        lenlns = len(lns)
        lnkname = self.target
        for j in range(self.lnidx + 2, self.lnidx + self.line_search_range):
            # j=i+2
            if j > lenlns - 1:
                break
            lnj = lns[j]
            if rextitle.match(lnj):
                lnkname = lns[j - 1].strip()
                if not lnkname:
                    lnkname = lns[j + 1].strip()
                break
            # j, lns=1,".. figure::\n  :name: linkname".splitlines();lnj=lns[j]
            # j, lns=1,".. figure::\n  :name:".splitlines();lnj=lns[j]
            # j, lns=1,".. math::\n  :name: linkname".splitlines();lnj=lns[j]
            itm = rexname.match(lnj)
            if itm:
                lnkname, = itm.groups()
                lnj1 = lns[j - 1].split('::')[0].replace(
                    'list-table', 'table').replace('code-block',
                                                   'code').strip()
                if counters and not lnkname and lnj1 in counters:
                    lnkname = name_from_directive(
                        lnj1.strip('. '), counters[lnj1])
                    counters[lnj1] += 1
                    break
                elif lnkname:
                    lnkname = lnkname.strip()
                    break
            # lnj=":linkname: words"
            itm = rexitem.match(lnj)
            if itm:
                lnkname, = itm.groups()
                break
            itm = rexoneword.match(lnj)
            if itm:
                lnkname, = itm.groups()
                break
            lnkname = self.target
        self.lnkname = lnkname

    def create_link(self,
                    linktype,
                    reststem,
                    tool
                    ):
        """Tgt.

        Creates a link.
        If bouth linktype and reststem are empty,
        then this is an internal link.

        :param linktype: file extension:
            one of rest, html, docx, odt, latex, pdf
        :param reststem:  the file name without extension
            (not used for linktype='sphinx' or 'rest')
        :param tool: pandoc, sphinx or rst

        """
        if reststem and linktype:
            targetfile = reststem + '.' + linktype
        else:
            targetfile = ''
        id = self.target
        if linktype == 'latex':
            linktype = 'pdf'
        if tool == 'sphinx':
            tgte = ".. |{0}| replace:: :ref:`{1}<{2}>`\n".format(
                self.target, self.lnkname, id)
        else:
            if linktype == 'odt':
                # https://github.com/jgm/pandoc/issues/3524
                tgte = ".. |{0}| replace:: `{1} <../{2}#{3}>`__\n".format(
                    self.target, self.lnkname, targetfile, id)
            else:
                tgte = ".. |{0}| replace:: `{1} <{2}#{3}>`__\n".format(
                    self.target, self.lnkname, targetfile, id)
        if tool == 'rst' and linktype == 'html':
            return _rst_id_fix(tgte)
        else:
            return tgte

    def create_tag(self):
        return r'{0}	{1}	/\.\. _`\?{0}`\?:/;"		line:{2}'.format(
            self.target, self.tagentry[0], self.tagentry[1])


class RstFile:
    def __init__(self, reststem, doc, tgts, lnks, nlns):
        '''RstFile.

        Contains the targets for a ``.rst`` or ``.rest`` file.

        :param reststem: .rest file this doc belongs to (without extension)
        :param doc: doc belonging to reststem,
            either included or itself (.rest, .rst, .stpl)
        :param tgts: list of Tgt objects yielded by |dcx.RstFile.make_tgts|.
        :param lnks: list of (line index, target name (``|target|``)) tuples
        :param nlns: number of lines of the doc

        '''

        self.reststem = reststem
        self.doc = doc
        self.tgts = tgts
        self.lnks = lnks
        self.nlns = nlns

    def __str__(self):
        return str((self.doc, self.restname))

    def add_links_and_tags(self, add_tgt, add_linksto):
        iterlnks = iter(self.lnks)
        prevtgt = None
        # unknowntgts = []
        tgt = None
        for tgt in self.tgts:
            if tgt.lnidx is not None:
                add_linksto(prevtgt, tgt.lnidx, iterlnks)  # , unknowntgts)
                add_tgt(tgt, self.reststem)
                prevtgt = tgt
        if tgt:
            add_linksto(prevtgt, tgt.lnidx, iterlnks)  # , unknowntgts)

    @staticmethod
    def make_lnks(lns  # lines of the document
                  ):
        """RestFile.

        Yields (index, link name) for ``lns``.

        """

        for i, ln in enumerate(lns):
            mo = rexlnks.findall(ln)
            for g in mo:
                yield i, g

    @staticmethod
    def make_tgts(
            lns,
            doc,
            counters=None,
            fn_i_ln=None
            ):
        '''RstFile.

        Yields ``((line index, tag address), target, link name)``
        of ``lns`` of a restructureText file.
        For a .stpl file the linkname comes from the generated .rest file.

        :lns: lines of the document
        :doc: the rst document
        :counters: if None, the starts with
            {".. figure":1,".. math":1,".. table":1,".. code":1}
        :fn_i_ln: (fn, i, ln) of the .stpl with all stpl includes sequenced

        '''

        if counters is None:
            counters = make_counters()
        itgts = list(rindices(rextgt, lns))
        if fn_i_ln:
            lns1 = [x[2] for x in fn_i_ln]
            itgts1 = list(rindices(rextgt, lns1))
        else:
            lns1 = lns
            itgts1 = itgts
        if len(itgts) < len(itgts1):
            paired_itgts_itgts1 = pair(itgts, itgts1,
                                       lambda x, y: lns[x] == lns1[y])
        elif len(itgts) > len(itgts1):
            paired_itgts_itgts1 = ((i, j) for (
                j, i) in pair(itgts1, itgts, lambda x, y: lns1[x] == lns[y]))
        else:
            paired_itgts_itgts1 = zip(itgts, itgts1)
        lenlns = len(lns)
        lenlns1 = len(lns1)
        for i, i1 in paired_itgts_itgts1:
            ii, iis, iilen = (i, lns, lenlns) if i else (i1, lns1, lenlns1)
            cur = iis[ii]
            tgt = Tgt(ii, rextgt.search(cur).group(1))
            if tgt.is_inside_literal(iis):
                continue
            tgt.find_lnkname(iis, counters)
            tgt.lnkidx = i
            if i1:
                if fn_i_ln:
                    tgt.tagentry = fn_i_ln[i1][:2]
                else:
                    tgt.tagentry = (doc, ii)
            else:
                tgt.tagentry = (doc.replace(_stpl, ''), ii)
            yield tgt

    @staticmethod
    def substs(lns  # lines of the rst document
               ):
        """RestFile.

        Return all substitution targets in the rst lns

        ::

            >>> list(RstFile.substs('''
            ...   .. |sub| image:: xx
            ...   .. |s-b| date::
            ...   '''.splitlines()))
            ['sub', 's-b']

        """

        for i, ln in enumerate(lns):
            asub = rexsubtgt.search(ln)
            if asub:
                yield asub.group(1)


class Fldr(OrderedDict):
    def __init__(
            self,
            folder
            ):
        """
        Represents a directory.

        It is an ordered list of {rst file: RstFile object}.

        :self.folder: is the directory path
        :self.allfiles: set of all files in the directory
        :self.alltgts: set of all targets in the directory
        :self.allsubsts: set of all substitutions in the directory
        :self.counters: the counters for each rest file

        """

        self.folder = folder
        self.allfiles = set()
        self.alltgts = set()
        self.allsubsts = set()
        self.rest_counters = defaultdict(dict)

    def __str__(self):
        return str(list(sorted(self.keys())))

    def scandir(
            self,
            fs
            ):
        """Fldr.

        Scans the directory for rest files.
        All files (.rest and included .rst)
        are added if there is at least one ``.rest[.stpl]``.

        :param fs:  all files in the directory as returned by ``os.walk()``

        Sphinx index.rest is processed last.

        ``allfiles``, ``alltgts`` and ``allsubsts`` get filled.

        """

        sofar = set([])
        sphinx_index = None
        # reversed puts the rest.stpl before the .rest
        for afs in reversed(sorted(fs)):
            fullpth = normjoin(self.folder, afs).replace("\\", "/")
            if is_rest(afs):
                if afs.startswith('index.rest'):
                    sphinx_index = (afs, fullpth)
                    continue
                fullpth_nostpl = fullpth.replace(_stpl, '')
                if fullpth_nostpl in sofar:
                    continue
                sofar.add(fullpth_nostpl)
                self.add_rest(afs, fullpth)
        if sphinx_index:
            self.add_rest(*sphinx_index)

    def add_rest(self,
                 restfile,
                 fullpth,
                 exclude_paths_substrings=['_links_', _traceability_file]):
        """Fldr.

        Scans a rest file for included files and constructs all the targets.

        """

        pths = []
        has_traceability = False
        for restinc in rstincluded(restfile, (self.folder, )):
            pth = normjoin(self.folder, restinc).replace("\\", "/")
            if _traceability_file + _rst in restinc:
                if pyfca and _traceability_instance is None:
                    Traceability(stem(restfile))
                    has_traceability = True
                    continue
            if any(x in pth for x in exclude_paths_substrings):
                continue
            pths.append(pth)

        reststem = pths[0]
        reststem = stem(stem(reststem))
        if reststem not in self.rest_counters:
            self.rest_counters[reststem] = make_counters()
        counters = self.rest_counters[reststem]
        if has_traceability:
            _traceability_instance.counters = counters

        self.allfiles |= set(pths)

        for doc in pths:
            rstpath = doc.replace(_stpl, '')
            if doc.endswith(_stpl) and exists(rstpath):
                lns = _read_lines(doc.replace(_stpl, ''))
                fn_i_ln = _flatten_stpl_includes(doc)
                tgts = list(RstFile.make_tgts(lns, doc, counters, fn_i_ln))
            elif not doc.endswith(_tpl) and not doc.endswith(_txt) and exists(
                    doc):
                lns = _read_lines(doc)
                tgts = list(RstFile.make_tgts(lns, doc, counters))
            else:
                continue
            lnks = list(RstFile.make_lnks(lns))
            rstfile = RstFile(base(reststem), doc, tgts, lnks, len(lns))
            self[doc] = rstfile
            self.alltgts |= set([t.target for t in rstfile.tgts])
            self.allsubsts |= set(RstFile.substs(lns))

    def create_links_and_tags(self, scanroot):
        """Fldrs.

        Creates links_xxx.rst and .tags files
        for a directory at scanroot/directory

        The target IDs are grouped.
        To every group a color is associated. See ``conf.py``.
        This is used to color an FCA lattice diagram
        in "_traceability_file.rst".
        The diagram nodes are clickable in HTML.

        """

        tagentries = []
        upcnt = 0
        if self.folder.strip():
            relfolder = relpath(self.folder, start=scanroot)
            if '/' in relfolder:
                upcnt = len(relfolder.split('/'))
        links_types = "sphinx latex html pdf docx odt".split()
        linkfiles = [(linktype, []) for linktype in links_types]

        def add_tgt(tgt, reststem):
            for linktype, linklines in linkfiles:
                linklines.append(
                    tgt.create_link(
                        linktype, reststem,
                        linktype if linktype == 'sphinx' else 'pandoc'))
            if isabs(tgt.tagentry[0]):
                tgt.tagentry = (relpath(tgt.tagentry[0], start=scanroot),
                                tgt.tagentry[1])
            tgt.tagentry = ("../" * upcnt + tgt.tagentry[0], tgt.tagentry[1])
            tagentries.append(tgt.create_tag())

        def add_links_comments(comment):
            for _, linklines in linkfiles:
                linklines.append(comment)

        def add_linksto(prevtgt, lnidx, iterlnks, ojlnk=[0, None]):
            # all the links from the block following prevtgt up to this tgt
            linksto = []

            def chkappend(x):
                if not prevtgt or x != prevtgt.target:
                    linksto.append(x)

            if ojlnk[1] and ojlnk[0] < lnidx:  # first link in the new prevtgt
                if ojlnk[1] in self.alltgts:
                    chkappend(ojlnk[1])
                elif ojlnk[1] not in self.allsubsts:
                    linksto.append('-' + ojlnk[1])
                    # unknowntgts.append(ojlnk[1])
                ojlnk[1] = None
            if ojlnk[1] is None:  # remaining links in prevtgt up to this tgt
                for j, lnk in iterlnks:
                    if j > lnidx:  # links upcnt to this target
                        ojlnk[:] = j, lnk
                        break
                    else:
                        if lnk in self.alltgts:
                            chkappend(lnk)
                        elif lnk not in self.allsubsts:
                            linksto.append('-' + lnk)
                            # unknowntgts.append(lnk)
            if _traceability_instance:
                if prevtgt and linksto:
                    _traceability_instance.appendobject(
                        set([
                            x for x in linksto
                            if not x.startswith('-') and not x.startswith('_')
                        ] + [prevtgt.target]))
            if linksto:
                linksto = '.. .. ' + ','.join(linksto) + '\n\n'
                add_links_comments(linksto)

        for rstfile in self.values():
            add_links_comments('\n.. .. {0}\n\n'.format(rstfile.doc))
            rstfile.add_links_and_tags(add_tgt, add_linksto)
        if _traceability_instance:
            tlns = _traceability_instance.create_traceability_file(self.folder)
            trcrst = normjoin(self.folder, _traceability_file + _rst)
            if tlns:
                for tgt in RstFile.make_tgts(tlns, trcrst,
                                             _traceability_instance.counters):
                    add_tgt(tgt, _traceability_instance.tracehtmltarget)
        for linktype, linklines in linkfiles:
            with opnwrite(normjoin(self.folder,
                                   '_links_%s.rst' % linktype)) as f:
                f.write('\n'.join(linklines))
        ctags_python = ""
        try:
            ctags_python = cmd(
                [
                    'ctags', '-R', '--sort=0', '--fields=+n',
                    '--languages=python', '--python-kinds=-i', '-f', '-', '*'
                ],
                cwd=self.folder)
        finally:
            with opnwrite(normjoin(self.folder, '.tags')) as f:
                f.write(ctags_python)
                f.write('\n'.join(tagentries))


class Fldrs(OrderedDict):
    def __init__(
            self,
            scanroot='.'
            ):
        """
        Represents a directory hierarchy below ``scanroot``.
        The paths are relative to ``scanroot``.

        :param scanroot: root path to start scanning
            for independent doc directories

        It is a dict ordere by insertion of {directory: Fldr objects}

        """

        self.scanroot = scanroot

    def __str__(self):
        return super().__str__()

    def scandirs(self):
        for p, ds, fs in os.walk(self.scanroot):
            if not p.endswith(_images):
                directory = normjoin(p)
                fldr = Fldr(directory)
                fldr.scandir(fs)
                if len(fldr):
                    self[directory] = fldr


def links_and_tags(adir):
    '''
    Creates _links_xxx.rst`` files and a ``.tags``.

    :param adir: directory for which to create links and tags

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

    '''

    fldrs = Fldrs(adir)
    fldrs.scandirs()
    for fldr in fldrs.values():
        fldr.create_links_and_tags(fldrs.scanroot)

def _kw_from_path(dir):
    """use file of path up to ``.git`` as keywords

    >>> dir="/pro jects/me_about-this-1.rst"
    >>> _kw_from_path(dir)==frozenset({'me', 'this', '1', 'about'})
    True

    """
    fr = dir
    fn = None
    while True:
        fr,fn = dir_base(fr)
        if not fn:
            break
        if exists(normjoin(fr,'.git')):
            break
    if fn:
        fn = relpath(dir,fr)
    else:
        fn = base(dir)
    fpth = stem(fn)
    if fpth.endswith(_rst) or fpth.endswith(_rest):
        fpth = stem(fpth)
    res = re.split(rexkwsplit,fpth)
    return frozenset(res)

def _kw_from_line(ln):
    """make  a frozenset out of keyword line

    >>> ln='.. {kw1,kw2-kw3.kw4}'
    >>> _kw_from_line(ln) == frozenset({'kw1','kw2','kw3','kw4'})
    True
    >>> ln='   .. {kw1,trag}'
    >>> _kw_from_line(ln) == frozenset({'kw1', 'trag'})
    True

    """
    return frozenset(x for x in re.split(rexkwsplit,ln.lower()) if x)

def grep(
      regexp=rexkw, 
      dir=None, 
      exts=set(['.rst','.rest','.stpl','.tpl','.py'])):
    '''
    .. {grep}

    Uses python re to find ``regexp`` and return 
    ``[(file,1-based index,line),...]``
    in *dir* (default: os.getcwd()) for ``exts`` files

    :param regexp: default is a rst-commented keywords list
    :param dir: default is current dir
    :param exts: the extension of files searched

    >>> list(grep(dir=dirname(__file__))) [0][2]
    '.. {grep}'

    '''
    if dir is None:
        dir = os.getcwd()
    regexp = re.compile(regexp)
    for root, dirs, files in os.walk(dir):
        for name in files:
            if any(name.endswith(ext) for ext in exts):
                f = normjoin(root,name)
                if not f.endswith('.py') and not f.endswith(_stpl) and exists(f+_stpl):
                    continue
                with open(f,encoding="utf-8") as fb:
                    lines=[l.strip() for l in fb.readlines()]
                    res = [(i,lines[i]) for i in rindices(regexp, lines)]
                    for (i,l) in res:
                        yield (f,i+1,l)

def yield_with_kw (kws, fn_ln_kw=None, **kwargs):
    '''
    Find keyword lines in ``fn_ln_kw`` list or using grep(),
    that contain the keywords in kws.

    Keyword line::
      
        .. {kw1,kw2}

    :param kws: string will be split by non-chars
    :param fn_ln_kw: list of (file, line, keywords) tuples 
                     or ``regexp`` for grep()

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

    '''
    if fn_ln_kw is None:
        fn_ln_kw = grep(**kwargs)
    elif isinstance(fn_ln_kw,str): 
        fn_ln_kw = grep(fn_ln_kw, **kwargs)
    oldfn = None
    qset = _kw_from_line(kws)
    for i,(fn,ln,kw) in enumerate(fn_ln_kw):
        #i,(fn,ln,kw) = next(enumerate(fn_ln_kw))
        if fn != oldfn:
            fnkw = _kw_from_path(fn)
            oldfn = fn
        kws = _kw_from_line(kw)|fnkw
        if kws and qset<=kws:
            yield i,[fn,ln,kw]


# ==============> for building with WAF

try:
    from waflib import TaskGen, Task

    @lru_cache()
    def _ant_glob_stpl(bldpath, *stardotext):
        res = []
        already = set([])
        for an_ext in stardotext:
            stplsfirst = bldpath.ant_glob(an_ext + _stpl)
            for anode in stplsfirst:
                already.add(stem(anode.name))
                res.append(anode)
            nonstpls = bldpath.ant_glob(an_ext)
            for anode in nonstpls:
                if anode.name not in already:
                    res.append(anode)
        return res

    gensrc = {}

    @TaskGen.feature('gen_files')
    @TaskGen.before('process_rule')
    def gen_files(self):
        global gensrc
        gensrc = {}
        rootpth = self.bld.path.abspath()
        if rootpth not in sys.path:
            sys.path.append(rootpth)
        genpth = self.path.make_node('gen').abspath()
        if exists(genpth):
            for f, t, fun, kw in parsegenfile(genpth):
                gensrc[t] = f
                frm = self.path.find_resource(f)
                twd = self.path.make_node(t)
                self.create_task('GENTSK', frm, twd, fun=fun, kw=kw)

    class GENTSK(Task.Task):
        def run(self):
            frm = self.inputs[0]
            twd = self.outputs[0]
            twd.parent.mkdir()
            gen(frm.abspath(), twd.abspath(), fun=self.fun, **self.kw)

    def get_docs(bld):
        docs = [x.lower() for x in bld.options.docs]
        if not docs:
            docs = [x.lower() for x in bld.env.docs]
        return docs

    @lru_cache()
    def get_files_in_doc(path, node):
        srcpath = node.parent.get_src()
        orgd = node.parent.abspath()
        d = srcpath.abspath()
        n = node.name
        nod = None
        if node.is_bld(
                        ) and not node.name.endswith(
                            _stpl
                            ) and not node.name.endswith(_tpl):
            nod = srcpath.find_node(node.name + _stpl)
        if not nod:
            nod = node
        ch = rstincluded(n, (d, orgd), True, True)
        deps = []
        nodeitself = True
        for x in ch:
            if nodeitself:
                nodeitself = False
                continue
            isrst = is_rst(x)
            # else cyclic dependency for _links_xxx.rst
            if isrst and x.startswith('_links_'):
                continue
            nd = srcpath.find_node(x)
            if not nd:
                if isrst and not x.endswith(_stpl) and not x.endswith(_tpl):
                    nd = srcpath.find_node(x + _stpl)
            deps.append(nd)
        depsgensrc = [
            path.find_node(gensrc[x]) for x in deps if x and x in gensrc
        ]
        rs = [x for x in deps if x] + depsgensrc
        return (list(sorted(set(rs), key=lambda a: a.name)), [])

    @TaskGen.feature('gen_links')
    @TaskGen.after('gen_files')
    def gen_links(self):
        docs = get_docs(self.bld)
        if docs:
            for so in self.path.ant_glob('*.stpl'):
                tsk = Namespace()
                tsk.inputs = (so, )
                tsk.env = self.env
                tsk.generator = self
                render_stpl(tsk, self.bld)
            links_and_tags(self.path.abspath())

    def render_stpl(tsk, bld):
        bldpath = bld.path.get_bld().abspath()
        ps = tsk.inputs[0].abspath()
        try:
            pt = tsk.outputs[0].abspath()
        except:
            if ps.endswith(_stpl):
                pt = stem(ps)
            else:
                raise RstDocError('No target for %s' % ps)
        env = dict(tsk.env)
        env.update(tsk.generator.__dict__)
        env['bldpath'] = bldpath
        dostpl(ps, pt, **env)

    class STPL(Task.Task):
        always_run = True

        def run(self):
            render_stpl(self, self.generator.bld)

    @TaskGen.extension(_stpl)
    def stpl_taskgen(self, node):  # expand into same directory
        nn = node.parent.make_node(stem(node.name))
        self.create_task('STPL', node, nn)
        try:
            self.get_hook(nn)(self, nn)
        except:
            pass

    def gen_ext_tsk(self, node,
                    ext):  # into _images or ../_images in source path
        srcfldr = node.parent.get_src()
        _imgpath, _ = here_or_updir(srcfldr.abspath(), _images)
        imgpath = relpath(_imgpath, start=srcfldr.abspath())
        outnode = srcfldr.make_node(
            normjoin(imgpath,
                     stem(node.name) + '.png'))
        self.create_task(ext[1:].upper(), node, outnode)

    @TaskGen.extension(_tikz)
    def tikz_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, _tikz)

    class TIKZ(Task.Task):
        def run(self):
            tikzpng(self.inputs[0].abspath(), self.outputs[0].abspath())

    @TaskGen.extension(_svg)
    def svg_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, _svg)

    class SVG(Task.Task):
        def run(self):
            svgpng(self.inputs[0].abspath(), self.outputs[0].abspath())

    @TaskGen.extension('.dot')
    def dot_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, '.dot')

    class DOT(Task.Task):
        run_str = "${dot} -Tpng ${SRC} -o${TGT}"

    @TaskGen.extension('.uml')
    def uml_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, '.uml')

    class UML(Task.Task):
        run_str = "${plantuml} ${SRC} -o${TGT[0].parent.abspath()}"

    @TaskGen.extension('.eps')
    def eps_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, '.eps')

    class EPS(Task.Task):
        run_str = ("${inkscape} -z --export-dpi=${DPI} --export-area-drawing" +
                   " --export-background-opacity=0 ${SRC} --export-png=${TGT}")

    @TaskGen.extension('.pyg')
    def pyg_to_png_taskgen(self, node):
        gen_ext_tsk(self, node, '.pyg')

    class PYG(Task.Task):
        def run(self):
            pygpng(self.inputs[0].abspath(), self.outputs[0].abspath())

    @TaskGen.extension(_rest)
    def docs_taskgen(self, node):
        docs = get_docs(self.bld)
        d = get_files_in_doc(self.path, node)

        def rstscan():
            return d

        if node.name != "index.rest":
            for doctgt in docs:
                if doctgt.startswith('sphinx_'):
                    continue
                doctype = _suffix(doctgt)
                out_node = node.parent.find_or_declare("{0}/{1}.{2}".format(
                    doctgt, stem(node.name), doctype))
                self.create_task(
                    'NonSphinxTask', [node],
                    out_node,
                    scan=rstscan,
                    doctgt=doctgt)
        else:
            for doctgt in docs:
                if not doctgt.startswith('sphinx_'):
                    continue
                doctype = doctgt.split('_')[1]
                out_node = node.parent.find_or_declare("{0}/{1}.{2}".format(
                    doctgt, stem(node.name), doctype.replace('latex', 'tex')))
                self.create_task(
                    'SphinxTask', [node],
                    out_node,
                    scan=rstscan,
                    doctype=doctype,
                    config_py_try=(self.path.abspath(),
                                   self.bld.path.get_src().abspath()))

    class NonSphinxTask(Task.Task):
        def run(self):
            dorst(self.inputs[0].abspath(), self.outputs[0].abspath(),
                  self.doctgt)

    class SphinxTask(Task.Task):
        always_run = True

        def run(self):
            for atry in self.config_py_try:
                confpypath, there = here_or_updir(atry, 'conf.py')
                if there:
                    break
            config = conf_py(dirname(confpypath))
            # rst_sphinx needs it relative to infile
            if 'html_extra_path' in config:
                config['html_extra_path'] = [
                    normjoin(dirname(confpypath), x)
                    for x in config['html_extra_path']
                ]
            else:
                config['html_extra_path'] = html_extra_path
            rst_sphinx(self.inputs[0].abspath(), self.outputs[0].abspath(),
                       self.doctype, **config)

    def options(opt):
        def docscb(option, opt, value, parser):
            setattr(parser.values, option.dest, value.split(','))

        opt.add_option(
            "--docs",
            type='string',
            action="callback",
            callback=docscb,
            dest='docs',
            default=[],
            help="""Comma-separated list of
html, docx, pdf, sphinx_html (default)
or any other of http://www.sphinx-doc.org/en/master/usage/builders"""
        )

    def configure(cfg):
        cfg.env['docs'] = cfg.options.docs
        for x in 'plantuml dot inkscape'.split():
            try:
                cfg.env[x] = cfg.find_program(x)
            except cfg.errors.ConfigurationError:
                cfg.to_log(x + ' was not found (ignoring)')
        config = conf_py(cfg.path.abspath())
        cfg.env['DPI'] = str(config.get('DPI', DPI))

    def build(bld):
        bld.src2bld = lambda f: bld(
            features='subst', source=f, target=f, is_copy=True)

        def gen_files():
            bld(name="process gen file", features="gen_files")

        bld.gen_files = gen_files

        def gen_links():
            bld(name="create links and .tags", features="gen_links")

        bld.gen_links = gen_links
        # use like bld(rule=bld.stpl, source='x.h.stpl')
        # to compile stpl only, else do without rule
        bld.stpl = lambda tsk: render_stpl(tsk, bld)

        def build_docs():
            global g_config
            if exists(normjoin(bld.srcnode.abspath(), 'conf.py')):
                g_config = conf_py(bld.srcnode.abspath())
            docs = get_docs(bld)
            if docs:
                bld.gen_files()
                bld.gen_links()
                for anext in '*.tikz *.svg *.dot *.uml *.pyg *.eps'.split():
                    for anextf in _ant_glob_stpl(bld.path, anext):
                        bld(name='build ' + anext, source=anextf)
                bld.add_group()
                bld(name='build all rest',
                    source=[
                        x for x in _ant_glob_stpl(bld.path, '*.rest', '*.rst')
                        if not x.name.endswith(_rst)
                    ])
                bld.add_group()

        bld.build_docs = build_docs

except:
    pass

# ==============< for building with WAF

# pandoc --print-default-data-file reference.docx > reference.docx
# pandoc --print-default-data-file reference.odt > reference.odt
# pandoc --print-default-template=latex
# then modified in format and not to use figure labels
# this is for mktree(): first line of file content must not be empty!
example_tree = r'''
       build/
       dcx.py << file:///__file__
       reference.tex << file:///__tex_ref__
       reference.docx << file:///__docx_ref__
       reference.odt << file:///__odt_ref__
       wafw.py << file:///__wafw__
       waf
         #!/usr/bin/env sh
         shift
         ./wafw.py "$@"
       waf.bat
         @setlocal
         @set PYEXE=python
         @where %PYEXE% 1>NUL 2>NUL
         @if %ERRORLEVEL% neq 0 set PYEXE=py
         @%PYEXE% -x "%~dp0wafw.py" %*
         @exit /b %ERRORLEVEL%
       wscript
         #vim: syntax=python
         from waflib import Logs
         Logs.colors_lst['BLUE']='\x1b[01;36m'
         top='.'
         out='build'
         def options(opt):
           opt.load('dcx', tooldir='.')
         def configure(cfg):
           cfg.load('dcx', tooldir='.')
         def build(bld):
           #defines bld.gen_files(), bld.gen_links(), bld.build_docs()
           bld.load('dcx', tooldir='.')
           bld.recurse('doc')
       docutils.conf
         [general]
         halt_level: severe
         report_level: error
       conf.py
         project = 'sample'
         author = project+' Project Team'
         copyright = '2019, '+author
         version = '1.0'
         release = '1.0.0'
         try:
             import sphinx_bootstrap_theme
             html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
             html_theme = 'bootstrap'
         except:
             pass
         #these are enforced by rstdoc, but keep them for sphinx-build
         numfig = 0
         smartquotes = 0
         source_suffix = '.rest'
         templates_path = []
         language = None
         highlight_language = "none"
         default_role = 'math'
         pygments_style = 'sphinx'
         exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
         master_doc = 'index'
         html_extra_path=["doc/_traceability_file.svg"] #relative to conf.py
         import os
         on_rtd = os.environ.get('READTHEDOCS') == 'True'
         if not on_rtd:
             latex_engine = 'xelatex'
             #You can postprocess pngs.default: png_post_processor = None
             def png_post_processor(filename):
                 from PIL import Image, ImageChops
                 def trim(im):
                     bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
                     diff = ImageChops.difference(im, bg)
                     diff = ImageChops.add(diff, diff, 2.0, -100)
                     bbox = diff.getbbox()
                     if bbox:
                         return im.crop(bbox)
                 im = Image.open(filename)
                 im = trim(im)
                 im.save(filename)
                 return filename
             #the following are default and can be omitted
             latex_elements = {'preamble':r"""
             \usepackage{pgfplots}
             \usepackage{unicode-math}
             \usepackage{tikz}
             \usepackage{caption}
             \captionsetup[figure]{labelformat=empty}
             \usetikzlibrary{arrows,snakes,backgrounds,patterns,matrix,shapes,fit,calc,shadows,plotmarks,intersections}
             """
             }
             #new in rstdcx/dcx/py
             tex_wrap = r"""
             \documentclass[12pt,tikz]{standalone}
             \usepackage{amsmath}
             """+latex_elements['preamble']+r"""
             \pagestyle{empty}
             \begin{document}
             %s
             \end{document}
             """
             DPI = 600
             target_id_group = lambda targetid: targetid[0]
             target_id_color={"ra":("r","lightblue"), "sr":("s","red"),
                "dd":("d","yellow"), "tp":("t","green")}
             pandoc_doc_optref={'latex': '--template ../reference.tex',
                              'html': {},#each can also be dict of file:template
                              'pdf': '--template ../reference.tex',
                              'docx': '--reference-doc ../reference.docx',
                              'odt': '--reference-doc ../reference.odt'
                              }
             _pandoc_latex_pdf = ['--listings','--number-sections','--pdf-engine',
                'xelatex','-V','titlepage','-V','papersize=a4',
                '-V','toc','-V','toc-depth=3','-V','geometry:margin=2.5cm']
             pandoc_opts = {'pdf':_pandoc_latex_pdf,'latex':_pandoc_latex_pdf,
                'docx':[],'odt':[],
                'html':['--mathml','--highlight-style','pygments']}
             rst_opts = { #http://docutils.sourceforge.net/docs/user/config.html
                         'strip_comments':True
                         ,'report_level':3
                         ,'raw_enabled':True
                         }
             def name_from_directive(directive,count):
                 return directive[0].upper() + directive[1:] + ' ' + str(count)
       Makefile
         SPHINXOPTS  = -c .
         SPHINXBLD   = sphinx-build
         SPHINXPROJ  = sample
         DOCDIR      = doc/
         DOCBACK     = ../
         DCXFROMDOC  = ../
         BLDDIR      = build/doc/
         STPLS       = $(wildcard $(DOCDIR)*.stpl)
         STPLTGTS    = $(STPLS:%.stpl=%)
         SRCS        = $(filter-out $(DOCDIR)index.rest,$(wildcard $(DOCDIR)*.rest))
         SRCSTPL     = $(wildcard $(DOCDIR)*.rest.stpl)
         IMGS        = \
         	$(wildcard $(DOCDIR)*.pyg)\
         	$(wildcard $(DOCDIR)*.eps)\
         	$(wildcard $(DOCDIR)*.tikz)\
         	$(wildcard $(DOCDIR)*.svg)\
         	$(wildcard $(DOCDIR)*.uml)\
         	$(wildcard $(DOCDIR)*.dot)\
         	$(wildcard $(DOCDIR)*.eps.stpl)\
         	$(wildcard $(DOCDIR)*.tikz.stpl)\
         	$(wildcard $(DOCDIR)*.svg.stpl)\
         	$(wildcard $(DOCDIR)*.uml.stpl)\
         	$(wildcard $(DOCDIR)*.dot.stpl)
         PNGS=$(subst $(DOCDIR),$(DOCDIR)_images/,\
         	$(patsubst %.eps,%.png,\
         	$(patsubst %.pyg,%.png,\
         	$(patsubst %.tikz,%.png,\
         	$(patsubst %.svg,%.png,\
         	$(patsubst %.uml,%.png,\
         	$(patsubst %.dot,%.png,\
         	$(patsubst %.eps.stpl,%.png,\
         	$(patsubst %.dot.stpl,%.png,\
         	$(patsubst %.tikz.stpl,%.png,\
         	$(patsubst %.svg.stpl,%.png,\
         	$(patsubst %.uml.stpl,%.png,$(IMGS)))))))))))))
         DOCXS = $(subst $(DOCDIR),$(BLDDIR)docx/,$(SRCS:%.rest=%.docx))\
         	$(subst $(DOCDIR),$(BLDDIR)docx/,$(SRCSTPL:%.rest.stpl=%.docx))
         PDFS  = $(subst $(DOCDIR),$(BLDDIR)pdf/,$(SRCS:%.rest=%.pdf))\
         	$(subst $(DOCDIR),$(BLDDIR)pdf/,$(SRCSTPL:%.rest.stpl=%.pdf))
         .PHONY: docx help Makefile docxdir pdfdir stpl index imgs
         stpl: $(STPLTGTS)
         %:%.stpl
         	@cd $(DOCDIR) && stpl "$(<F)" "$(@F)"
         imgs: $(PNGS)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.pyg
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.eps
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.tikz
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.svg
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.uml
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         $(DOCDIR)_images/%.png:$(DOCDIR)%.dot
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py $(<F)
         docxdir: ${BLDDIR}docx
         pdfdir: ${BLDDIR}pdf
         MKDIR_P = mkdir -p
         ${BLDDIR}docx:
         	@${MKDIR_P} ${BLDDIR}docx
         ${BLDDIR}pdf:
         	@${MKDIR_P} ${BLDDIR}pdf
         index:
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py
         help:
         	@$(SPHINXBLD) -M help "$(DOCDIR)" "$(BLDDIR)" $(SPHINXOPTS) $(O)
         	@echo "  docx        to docx"
         	@echo "  pdf         to pdf"
         #http://www.sphinx-doc.org/en/stable/usage/builders/
         html dirhtml singlehtml htmlhelp qthelp applehelp devhelp epub latex text man texinfo pickle json xml pseudoxml: Makefile index stpl imgs
         	@$(SPHINXBLD) -M $@ "$(DOCDIR)" "$(BLDDIR)" $(SPHINXOPTS) $(O)
         docx:  docxdir index stpl imgs $(DOCXS)
         $(BLDDIR)docx/%.docx:$(DOCDIR)%.rest
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py "$(<F)" "$(DOCBACK)$@"
         pdf: pdfdir index stpl imgs $(PDFS)
         $(BLDDIR)pdf/%.pdf:$(DOCDIR)%.rest
         	@cd $(DOCDIR) && python $(DCXFROMDOC)dcx.py "$(<F)" "$(DOCBACK)$@"
       __code__
         └ some.h
             /*
             #def gen_tst(lns,**kw):
             #  return [l.split('@')[1] for l in rlines(r'^\s*@',lns)]
             #def gen_tst
             #def gen_tstdoc(lns,**kw):
             #  return ['#) '+l.split('**')[1] for l in rlines(r'^/\*\*',lns)]
             #def gen_tstdoc

             @//generated from some.h
             @#include <assert.h>
             @#include "some.h"
             @int main()
             @{
             */

             /**Test add1()
             @assert(add1(1)==2);
             */
             int add1(int a)
             {
               return a+1;
             }

             /**Test add2()
             @assert(add2(1)==3);
             */
             int add2(int a)
             {
               return a+2;
             }

             /*
             @}
             */
       doc
        ├ _images/
        ├ wscript_build
            bld.build_docs()
        ├ index.rest
            ============
            Project Name
            ============

            .. toctree::
               ra.rest
               sr.rest
               dd.rest
               tp.rest

            One can also have a

            - issues.rest for issues

            - pp.rest for the project plan
              (with backlog, epics, stories, tasks)

            .. REMOVE THIS IF NO LINKING OVERVIEW WANTED
            .. include:: _traceability_file.rst

            .. include:: _links_sphinx.rst

        ├ ra.rest
            Risk Analysis
            =============

            .. _`rz7`:

            :rz7: risk calculations

            Risk calculations are done with python in the ``.stpl`` file.

            .. include:: _links_sphinx.rst

        ├ sr.rest
            Software/System Requirements
            ============================

            .. _`s97`:

            Requirements are testable (see |t9a|).

            .. _`su7`:

            ``dcx.py`` produces its own labeling
            consistent across DOCX, PDF, HTML.

            .. _`sy7`:

            A Requirement Group
            -------------------

            .. _`s3a`:

            :s3a: brief description

            Don't count the ID, since the order will change.
            The IDs have the first letter of the file
            and 2 or more random letters of ``[0-9a-z]``.
            Use an editor macro to generate IDs.

            A link: |s3a|

            If one prefers ordered IDs, one can use templates::

              %id = lambda x=[0]: x.append(x[-1]+1) or "s{:0>2}".format(x[-1])

              .. _`soi`:

              :{{id()}}: auto numbered.

            The disadvantage is that the id will differ
            between rst and final doc.
            When this is needed in an included file
            use template include: ``%include('x.rst.tpl`)``
            See the the ``test/stpl`` directory.

            Every ``.rest`` has this line at the end::

               .. include:: _links_sphinx.rst

            .. include:: _links_sphinx.rst

        ├ dd.rest
            Design Description
            ==================

            .. _`d97`:

            :d97: Independent DD IDs

              The relation with RS IDs is m-n.
              Links like |s3a| can be scattered over more DD entries.

            .. _`dx3`:

            .. figure:: _images/egtikz1.png
               :name:
               :width: 30%

               |dx3|: Create from egtikz1.tikz

            .. _`dz3`:

            .. figure:: _images/egtikz.png
               :name:
               :width: 50%

               |dz3|: Create from egtikz.tikz

               The usage of ``:name:`` produces:
                 ``WARNING: Duplicate explicit target name: ""``. Ignore.

            Reference via |dz3|.

            ``.tikz``, ``.svg``, ``.dot``,  ``.uml``, ``.eps`` or ``.stpl``
            thereof and ``.pyg``, are converted to ``.png``.

            .. _`dz4`:

            .. figure:: _images/egsvg.png
               :name:

               |dz4|: Created from egsvg.svg.stpl

            .. _`dz5`:

            .. figure:: _images/egdot.png
               :name:

               |dz5|: Created from egdot.dot.stpl

            .. _`dz6`:

            .. figure:: _images/eguml.png
               :name:

               |dz6|: Created from eguml.uml

            .. _`dz7`:

            .. figure:: _images/egplt.png
               :name:
               :width: 30%

               |dz7|: Created from egplt.pyg

            .. _`dz8`:

            .. figure:: _images/egpyx.png
               :name:

               |dz8|: Created from egpyx.pyg

            .. _`dr8`:

            .. figure:: _images/egcairo.png
               :name:

               |dr8|: Created from egcairo.pyg

            .. _`ds8`:

            .. figure:: _images/egpygal.png
               :name:
               :width: 30%

               |ds8|: Created from egpygal.pyg

            .. _`dsx`:

            .. figure:: _images/egother.png
               :name:

               |dsx|: Created from egother.pyg

            .. _`du8`:

            .. figure:: _images/egeps1.png
               :name:

               |du8|: Created from egeps1.eps

            .. _`d98`:

            .. figure:: _images/egeps.png
               :name:

               |d98|: Created from egeps.eps

            .. _`dua`:

            |dua|: Table legend

            .. table::
               :name:

               +--------+--------+
               | A      | B      |
               +========+========+
               | |eps1| | |eps|  |
               +--------+--------+

            .. _`dta`:

            |dta|: Table legend

            .. list-table::
               :name:
               :widths: 20 80
               :header-rows: 1

               * - Bit
                 - Function

               * - 0
                 - afun

            Reference |dta| does not show ``dta``.

            .. _`dyi`:

            |dyi|: Listing showing struct.

            .. code-block:: cpp
               :name:

               struct astruct{
                  int afield; //afield description
               }

            .. _`d9x`:

            .. math::
               :name:

               V = \frac{K}{r^2}

            ``:math:`` is the default inline role: `mc^2`

            .. _`d99`:

            :OtherName: Keep names the same all over.

            Here instead of ``d99:`` we use ``:OtherName:``,
            but now we have two synonyms for the same item.
            This is no good. If possible, keep ``d99`` in the source
            and in the final docs.

            The item target must be in the same file as the item content.
            The following would not work::

              .. _`dh5`:

              .. include:: somefile.rst

            .. |eps1| image:: _images/egeps1.png
            .. |eps| image:: _images/egeps.png

            .. include:: _links_sphinx.rst

        ├ tp.rest
            Test Plan
            =========

            .. _`t9a`:

            Requirement Tests
            -----------------

            No duplication. Only reference the requirements to be tested.

            - |s97|
            - |su7|
            - |s3a|
            - |rz7|

            Or better: reference the according SR chapter,
            else changes there would need an update here.

            - Test |sy7|

            Unit Tests
            ----------

            Use ``.rst`` for included files
            and start the file with ``_`` if generated.

            - |d97|
            - |dx3|
            - |dz4|
            - |dz5|
            - |dz6|
            - |dz7|
            - |dz8|
            - |dsx|
            - |du8|
            - |d98|
            - |dua|
            - |dta|
            - |dyi|
            - |d9x|
            - |d99|

            .. include:: _sometst.rst

            .. include:: _links_sphinx.rst

        ├ egtikz.tikz
            [thick,red]
            \draw (0,0) grid (3,3);
            \foreach \c in {(0,0), (1,0), (2,0), (2,1), (1,2)}
                \fill \c + (0.5,0.5) circle (0.42);
        ├ egtikz1.tikz
            \begin{scope}[blend group = soft light]
            \fill[red!30!white]   ( 90:1.2) circle (2);
            \fill[green!30!white] (210:1.2) circle (2);
            \fill[blue!30!white]  (330:1.2) circle (2);
            \end{scope}
            \node at ( 90:2)    {Typography};
            \node at ( 210:2)   {Design};
            \node at ( 330:2)   {Coding};
            \node [font=\Large] {\LaTeX};
        ├ egsvg.svg.stpl
            <?xml version="1.0" encoding="utf-8"?>
            <svg xmlns="http://www.w3.org/2000/svg"
                fill="none" version="1.1" width="110pt" height="60pt"
                stroke-width="0.566929" stroke-miterlimit="10.000000">
            %for i in range(10):
              <path fill="none" stroke="#f00" stroke-width="1"
                  d="M10,55 C15,5 100,5 100,{{i*5}}" />
            %end
            %for i in range(10):
              <path fill="none" stroke="#f40" stroke-width="1" d="M10,
                  {{i*5}} C15,5 100,5 100,55" />
            %end
            <text x="50" y="50" fill="red">Hi!</text>
            </svg>
        ├ egdot.dot.stpl
            digraph {
            %for i in range(3):
                "From {{i}}" -> "To {{i}}";
            %end
                }
        ├ eguml.uml
            @startuml
            'style options
            skinparam monochrome true
            skinparam circledCharacterRadius 0
            skinparam circledCharacterFontSize 0
            skinparam classAttributeIconSize 0
            hide empty members
            Class01 <|-- Class02
            Class03 *-- Class04
            Class05 o-- Class06
            Class07 .. Class08
            Class09 -- Class10
            @enduml
        ├ egplt.pyg
            #vim: syntax=python
            import matplotlib.pyplot as plt
            import numpy as np
            x = np.random.randn(1000)
            plt.hist( x, 20)
            plt.grid()
            plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
            plt.show()
        ├ egpyx.pyg
            import pyx
            c = pyx.canvas.canvas()
            c.stroke(pyx.path.circle(0,0,2),
                [pyx.style.linewidth.Thick,pyx.color.rgb.red])
            c.text(1, 1, 'Hi', [pyx.color.rgb.red])
        ├ egpygal.pyg
            import pygal
            diagram=pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4)
        ├ egother.pyg
            from PIL import Image, ImageDraw, ImageFont
            im = Image.new("RGBA",size=(50,50),color=(155,0,100))
            draw = ImageDraw.Draw(im)
            draw.rectangle(((0, 0), (40, 40)), fill="red")
            draw.text((20, 20), "123")
            save_to_png = lambda out_file: im.save(out_file, "PNG")
        ├ egeps.eps
            1 0 0 setrgbcolor
            newpath 6 2 36 54 rectstroke
            showpage
        ├ egeps1.eps
            0 0 1 setrgbcolor
            newpath 6 2 36 54 rectstroke
            showpage
        ├ egcairo.pyg
            import cairocffi as cairo
            surface = cairo.SVGSurface(None, 200, 200)
            context = cairo.Context(surface)
            x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
            x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
            context.set_source_rgba(1, 0.2, 0.2, 0.6)
            context.scale(200, 200)
            context.set_line_width(0.04)
            context.move_to(x, y)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()
            context.set_line_width(0.02)
            context.move_to(x, y)
            context.line_to(x1, y1)
            context.move_to(x2, y2)
            context.line_to(x3, y3)
            context.stroke()
        ├ gen
            #from|to|gen_xxx|kwargs
            ../__code__/some.h | _sometst.rst                | tstdoc | {}
            ../__code__/some.h | ../build/__code__/some_tst.c | tst    | {}'''

# replaces from '├ index.rest' to '├ egtikz.tikz'
example_stp_subtree = r'''
        ├ model.py
            """
            Contains definitions used in 
            - template files (``.rst.tpl`` or standalone ``.rest.stpl``)
            - test programs
            """
            from pint import UnitRegistry
            u = UnitRegistry()
            u.define('percent = 0.01*count = %')
            def U(*k,sep=", "):
                """
                Returns string of quantity, with units if possible.
                """
                try:
                    return sep.join(["{:~P}"]*len(k)).format(*k)
                except:
                    res = sep.join(["{}"]*len(k)).format(*k)
                    if res == 'None':
                        res = '-'
                    return res
            # Definitions e.g. x_some = 3.5*u.hour #see |x_some_doc|
        ├ utility.rst.tpl
            % import sys
            % import os
            % sys.path.append(os.path.dirname(__file__))
            % from model import *
            % cntr = lambda alist0,prefix='',width=2: alist0.append(
            %        alist0[-1]+1) or ("{}{:0>%s}"%width).format(prefix,alist0[-1])
            % II = lambda prefix,alist0,short:':{}: **{}**'.format(
            %      cntr(alist0,prefix),short)
            % #define in file e.g.
            % #SR=lambda short,alist0=[0]:II('SR',alist0,short)
            % #and use like {{SR('Item Title')}}
            %def pagebreak():
            .. raw:: openxml

                <w:p>
                  <w:r>
                    <w:br w:type="page"/>
                  </w:r>
                </w:p>

            .. raw:: html

                <p style="page-break-before: always;">&nbsp;</p>

            .. raw:: latex

                \pagebreak

            .. for docutils
            .. raw:: odt

                <text:p text:style-name="PageBreak"/>

            .. for pandoc
            .. raw:: opendocument

                <text:p text:style-name="PageBreak"/>

            %end
        ├ index.rest
            .. encoding: utf-8
            .. vim: syntax=rst

            ============
            Project Name
            ============

            .. toctree::
               sy.rest
               ra.rest
               sr.rest
               dd.rest
               tp.rest

            One can also have a

            - issues.rest for issues

            - pp.rest for the project plan
              (with backlog, epics, stories, tasks)

            .. REMOVE THIS IF NO LINKING OVERVIEW WANTED
            .. include:: _traceability_file.rst

            .. include:: _links_sphinx.rst

        ├ sy.rest.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            % globals().update(include('utility.rst.tpl'))
            % SY=lambda short,alist0=[0]:II('SY',alist0,short)

            .. _`sy_system_scope`:

            ############
            System Scope
            ############

            .. _`sy_general_idea`:

            {{SY('General Idea')}}

              Source code is text done in a good editor.
              Use the same editor also for documentation.
              Jump around like in hypertext.

            .. include:: _links_sphinx.rst
        ├ ra.rest.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            % globals().update(include('utility.rst.tpl'))
            % RA=lambda short,alist0=[0]:II('RA',alist0,short)

            .. _`ra_risk_analysis`:

            #############
            Risk Analysis
            #############

            .. _`r_restructured_text`:

            Advantages
            ==========

            {{RA('Restructured Text')}}

              We use `restructuredText \
              <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
              together with `SimpleTemplate \
              <https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax>`_.

              This is very flexible:

              - it allows to generate boilerplate text with python
              - it allows to link the text across documents
              - it allows to have many final formats (html, docx, pdf, odt, ...)
              - ...

            .. _`ra_risks`:

            Risks
            =====

            .. _`r_editor`:

            {{RA('Wrong Editor')}}

              This is not for people that only know how to edit in MS Words.
              Users should have embraced a good text editor.
              Software guys normally have.

              One needs a good text editor that supports ctags.
              These have been tested

              - `atom <https://atom.io/>`_
              - `vim <https://www.vim.org/>`_

            .. include:: _links_sphinx.rst
        ├ sr.rest.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            % globals().update(include('utility.rst.tpl'))
            % SR=lambda short,alist0=[0]:II('SR',alist0,short)

            .. _`sr_software_system_requirements`:

            ############################
            Software/System Requirements
            ############################

            .. _`sr_general`:

            General
            =======

            .. _`sr_testable`:

            {{SR('Testable')}}

              Requirements are testable (see |tp_requirement_tests|).

            .. _`sr_style`:

            {{SR('Style')}}

              In a restructuredText file, have one sentence in one line.

              Make long sentences into

              - lists

                - with sub items, if needed

              - or simply make more sentences out of it

              A link: |sr_style|.

            .. _`sr_a_requirement_group`:

            A Requirement Group
            ===================

            .. _`sr_id`:

            {{SR('ID')}}

              The ID seen in the final document is numbered
              by a python function.
              In the restructuredText files there is no numbering.
              The targets use keywords instead.
              This way one can rearrange the items
              keeping the items sorted and still referentially consistent.

              The ID shall not contain any hyphens
              or dots or other non-identifier characters,
              as some final formats, like DOCX, demand that.

            .. include:: _links_sphinx.rst
        ├ dd.rest.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            % globals().update(include('utility.rst.tpl'))
            % DD=lambda short,alist0=[0]:II('DD',alist0,short)

            .. _`dd_design_description`:

            ##################
            Design Description
            ##################

            .. _`dd_traceability`:

            {{DD('Traceability')}}

              ``dcx.py`` associates all links between two targets
              to the first target.
              This can be used as traceability.

              Warnings issued during conversion to final documents
              help to keep the documents consistent.

            .. _`dd_name`:

            {{DD('Name')}}

              For targeted

              - ``.. table::``
              - ``.. list-table::``
              - ``.. figure::``
              - ``.. code-block::``
              - ``.. math::``

              use ``:name:``.
              In the legend use the same ID as in the target definition.

              .. _`dd_figure`:

              .. figure:: _images/egtikz.png
                 :name:
                 :width: 50%

                 |dd_figure|: Caption here.
                 Reference this via ``|dd_figure|``.

            For testing purpose the following is rendered via include files.

            Include normal .rst way, where the .rst might be gnerated by a ``.rst.stpl``

            .. include:: dd_included.rst

            Include the stpl way

            %include('dd_diagrams.tpl',DD=DD) # you optionally can provide python definitions

            Pandoc does not know about `definitions in included files \
            <https://github.com/jgm/pandoc/issues/4160>`__.

            .. |eps1| image:: _images/egeps1.png
            .. |eps| image:: _images/egeps.png

            .. include:: _links_sphinx.rst

        ├ dd_included.rst.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            .. _`dd_code`:

            |dd_code|: Listing showing struct.

            .. code-block:: cpp
               :name:

               struct xxx{
                  int yyy; //yyy for zzz
               }

            Include normal ``.rst``.

            .. include:: dd_tables.rst

            Again include the stpl way.

            %include('dd_math.tpl')

        ├ dd_tables.rst
            .. encoding: utf-8
            .. vim: syntax=rst

            .. _`dd_table`:

            |dd_table|: Table legend

            .. table::
               :name:

               +--------+--------+
               | A      | B      |
               +========+========+
               | |eps1| | |eps|  |
               +--------+--------+

            .. _`dd_list_table`:

            |dd_list_table|: Table legend

            .. list-table::
               :name:
               :widths: 20 80
               :header-rows: 1

               * - Bit
                 - Function

               * - 0
                 - xxx

            Reference |dd_table| or |dd_list_table| does not show
            ``dd_table`` or ``dd_list_table``.

        ├ dd_math.tpl
            .. encoding: utf-8
            .. vim: syntax=rst

            .. _`dd_math`:

            .. math::
               :name:

               V = \frac{K}{r^2}

            ``:math:`` is the default inline role: `mc^2`

            With `sympy <www.sympy.org>`_ one can have formulas in ``some.py``
            that are usable for calculation.
            The formulas can be converted to latex
            in the ``.stpl`` or ``.tpl`` file.

            %def hyp(a,b):
            %    return a**2+b**2
            %end

            The long side of a rectangular triangle with legs
            {{3}} and {{4}} is {{hyp(3,4)**0.5}}. See |hyp|.

            .. _`hyp`:

            .. math::
                :name:

                %import sympy
                %from sympy.abc import a,b,c
                {{sympy.latex(sympy.Eq(c,hyp(a,b)))}}

        ├ dd_diagrams.tpl
            .. encoding: utf-8
            .. vim: syntax=rst

            .. _`dd_diagrams`:

            {{DD('Diagrams')}}

              .. _`exampletikz1`:

              .. figure:: _images/egtikz1.png
                 :name:
                 :width: 30%

                 |exampletikz1|: Create from egtikz1.tikz

                 The usage of ``:name:`` produces: ``WARNING:
                 Duplicate explicit target name: ""``. Ignore.

              Reference via |exampletikz1|.

              ``.tikz``, ``.svg``, ``.dot``,  ``.uml``, ``.eps`` or ``.stpl``
              thereof and ``.pyg``, are converted to ``.png``.

              .. _`examplesvg`:

              .. figure:: _images/egsvg.png
                 :name:

                 |examplesvg|: Created from egsvg.svg.stpl

              .. _`exampledot`:

              .. figure:: _images/egdot.png
                 :name:

                 |exampledot|: Created from egdot.dot.stpl

              .. _`exampleuml`:

              .. figure:: _images/eguml.png
                 :name:

                 |exampleuml|: Created from eguml.uml

              .. _`exampleplt`:

              .. figure:: _images/egplt.png
                 :name:
                 :width: 30%

                 |exampleplt|: Created from egplt.pyg

              .. _`examplepyx`:

              .. figure:: _images/egpyx.png
                 :name:

                 |examplepyx|: Created from egpyx.pyg

              .. _`examplecairo`:

              .. figure:: _images/egcairo.png
                 :name:

                 |examplecairo|: Created from egcairo.pyg

              .. _`examplepygal`:

              .. figure:: _images/egpygal.png
                 :name:
                 :width: 30%

                 |examplepygal|: Created from egpygal.pyg

              .. _`exampleother`:

              .. figure:: _images/egother.png
                 :name:

                 |exampleother|: Created from egother.pyg

              .. _`exampleeps1`:

              .. figure:: _images/egeps1.png
                 :name:

                 |exampleeps1|: Created from egeps1.eps

              .. _`exampleeps`:

              .. figure:: _images/egeps.png
                 :name:

                 |exampleeps|: Created from egeps.eps

              %if False:
              .. _`target_more_than_in_rest`:

                 It is OK to have more targets in the .stpl file.
              %end

        ├ tp.rest.stpl
            .. encoding: utf-8
            .. vim: syntax=rst

            % globals().update(include('utility.rst.tpl'))
            % TP=lambda short,alist0=[0]:II('TP',alist0,short)

            .. _`tp_test_plan`:

            #########
            Test Plan
            #########

            .. _`tp_requirement_tests`:

            Requirement Tests
            =================

            .. _`tp_test_types`:

            {{TP('Test Types')}}

              Performance tests are only one kind of tests.

            .. _`tp_no_duplication`:

            {{TP('No duplication')}}

              Since items in other documents are phrased as tests,
              there is no need to repeat the text here.

              - |sr_id|

              Or better: Reference the according chapter:

              - Test |sr_a_requirement_group|

            .. _`tp_unit_tests`:

            Unit Tests
            ==========

            .. _`tp_gen_file`:

            {{TP('gen file')}}

              Use ``.rst`` for included files
              and start the file with ``_`` if generated.
              How test documentation files are generated
              from test source code can be specified in the ``gen`` file.

            .. include:: _links_sphinx.rst'''


def mktree(tree):
    '''

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

    '''

    for treestart, t in enumerate(tree):
        try:
            ct = re.search(r'[^\s├│└]', t).span()[0]
            break
        except:
            continue
    t1 = [t[ct:] for t in tree[treestart:]]
    entry_re = re.compile(r'^(\w[^ </\\]*)(\s*<<\s*|\s*[\\/]\s*)*(\w.*)*')
    it1 = list(rindices(entry_re, t1))
    lt1 = len(t1)
    it1.append(lt1)
    for c, f in intervals(it1):
        ef, ed, eg = entry_re.match(t1[c]).groups()
        if ef:
            if c < f - 1:
                p1 = t1[c + 1].find('└') + 1
                p2 = t1[c + 1].find('├') + 1
                ix = (p1 >= 0 and p1 or p2) - 1
                if ix >= 0 and ix <= len(ef):
                    mkdir(ef)
                    with new_cwd(ef):
                        mktree(t1[c + 1:f])
                else:
                    t0 = t1[c + 1:f]
                    try:
                        ct = re.search(r'[^\s│]', t0[0]).span()[0]
                    except:
                        print(c, f, '\n'.join(t0[:10]))
                        print("FIRST LINE OF FILE CONTENT MUST NOT BE EMPTY!")
                    tt = [t[ct:] + '\n' for t in t0]
                    with opnwrite(ef) as fh:
                        fh.writelines(tt)
            elif eg:
                try:
                    request.urlretrieve(eg, ef)
                except Exception as err:
                    print("Error ", err)
            elif ed and (('\\' in ed) or ('/' in ed)):
                mkdir(ef)
            else:
                with opnwrite(ef) as f:
                    f.write('')


def tree(
         path,
         with_content=False,
         with_files=True,
         with_dot_files=True,
         max_depth=100
         ):
    '''
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

    '''

    subprefix = ['│  ', '   ']
    entryprefix = ['├─', '└─']

    def _tree(path, prefix):
        for p, ds, fs in os.walk(path):
            # p, ds, fs = path, [], os.listdir()
            lends = len(ds)
            lenfs = len(fs)
            if len(prefix) / 3 >= max_depth:
                return
            for i, d in enumerate(sorted(ds)):
                yield prefix + entryprefix[i == lends + lenfs - 1] + d
                yield from _tree(
                    normjoin(p, d), prefix + subprefix[i == lends + lenfs - 1])
            del ds[:]
            if with_files:
                for i, f in enumerate(sorted(fs)):
                    if with_dot_files or not f.startswith('.'):
                        yield prefix + entryprefix[i == lenfs - 1] + f
                        if with_content:
                            pf = normjoin(p, f)
                            lns = _read_lines(pf)
                            for ln in lns:
                                yield prefix + subprefix[1] + ln

    return '\n'.join(_tree(path, ''))


def initroot(
        rootfldr,
        sampletype
        ):
    '''
    Creates a sample tree in the file system
    based on the ``example_tree`` and the ``example_stp_subtree`` in dcx.py.

    rootfldr: directory name that becomes root of the sample tree
    sampletype: either 'stpl' for the templated sample tree, or 'rest'

    '''

    # rootfldr, sampletype = 'tmp', 'rest'
    stpltype = sampletype == 'stpl'
    thisfile = __file__.replace('\\', '/')
    tex_ref = normjoin(dirname(thisfile), 'reference.tex')
    docx_ref = normjoin(dirname(thisfile), 'reference.docx')
    odt_ref = normjoin(dirname(thisfile), 'reference.odt')
    wafw = normjoin(dirname(thisfile), 'wafw.py')
    inittree = [
        l for l in example_tree.replace(
            '__file__', thisfile).replace(
            '__tex_ref__', tex_ref).replace(
            '__docx_ref__', docx_ref).replace(
            '__odt_ref__', odt_ref).replace(
            '__wafw__', wafw).replace(
            '__code__', rootfldr).splitlines()
    ]
    if stpltype:

        def _replace_lines(origlns, start, stop, insertlns):
            return origlns[:list(rindices(start, origlns))
                           [0]] + insertlns + origlns[list(
                               rindices(stop, origlns))[0]:]

        inittree = _replace_lines(inittree, '├ index.rest', '├ egtikz.tikz',
                                  example_stp_subtree.splitlines())
    mkdir(rootfldr)
    with new_cwd(rootfldr):
        mktree(inittree)


def index_dir(root):
    '''
    Index a directory.

    :param root: All subdirectories of ``root`` that contain a ``.rest`` or ``.rest.stpl`` file are indexed.

    - expands the .stpl files
    - generates the files as defined in the ``gen`` file (see example in dcx.py)
    - generates ``_links_xxx.rst`` for xxx = {sphinx latex html pdf docx odt}
    - generates ``.tags`` with jumps to reST targets

    '''

    # link, gen and tags per directory
    fldrs = Fldrs(root)
    fldrs.scandirs()
    for directory, fldr in fldrs.items():
        # generated files need to be there to be indexed
        genpth = normjoin(directory, 'gen')
        if exists(genpth):
            try:
                for f, t, d, kw in parsegenfile(genpth):
                    gen(normjoin(directory, f),
                        target=normjoin(directory, t),
                        fun=d,
                        **kw)
            except Exception as err:
                print('Generating files in %s seems not meant to be done: %s' %
                      (genpth, str(err)))
        # we need to do the templates here, because ``create_links_and_tags()`` needs them
        for f in os.listdir(directory):
            if f.endswith(_stpl):
                dpth = normjoin(directory, f)
                if isfile(dpth):
                    outpth = stem(dpth)
                    try:
                        dostpl(dpth, outpth)
                    except Exception as err:
                        print('Error expanding %s: %s' % (dpth, str(err)))
        fldr.create_links_and_tags(root)


description = (

"""
``rstdcx`` CLI
--------------

Without parameters: creates ``|substitution|`` links and .tags ctags for reST targets.

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

"""

)


def main(**args):
    '''
    This corresponds to the |rstdcx| shell command.

    '''

    import argparse

    if not args:
        parser = argparse.ArgumentParser(description=description,
                          formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument(
            '--rest',
            dest='restroot',
            action='store',
            help='Create a sample directory structure with .rest files.')
        parser.add_argument(
            '--stpl',
            dest='stplroot',
            action='store',
            help='Create a sample directory structure with .rest.stpl files.')
        parser.add_argument(
            '--pygrep',
            dest='pygrep',
            action='store',
            help='Grep rst doc using python regular expressions.')
        parser.add_argument(
            '--kw',
            dest='kw',
            action='store',
            help='List keyword lines (.. {kw1,kw2,...}) that contain all given as parameter, e.g kw1,kw2.')
        parser.add_argument(
            '-I',
            action='append',
            metavar='folder',
            nargs=1,
            help='Add folders to look for ``conf.py``, ``.[s]tpl`` and reference.docx/odt/tex')
        parser.add_argument(
            'infile',
            nargs='?',
            help='''\
Integrates Sphinx, Pandoc and Docutils to produce output supported by any of them.
To use all three, restructuredText must not use Sphinx extensions.
Input file, dir or - for stdin.''')
        parser.add_argument(
            'outfile',
            nargs='?',
            help='Output file, dir or - or nothing to print to std out.')
        parser.add_argument(
            'outtype',
            nargs='?',
            default=None,
            help="""One of {pandoc,sphinx,}x{html,docx,...}
or omitted for default (pandoc) (- if further code paramters are given)."""
        )
        parser.add_argument(
            'code',
            nargs='*',
            help="""Further parameters are python code,
to define variables that can be used in templates."""
        )
        args = parser.parse_args().__dict__

    if 'code' in args and args['code'] is not None and args['code'] != []:
        code = '\n'.join(args['code'])
        eval(compile(code, '<string>', 'exec'), globals())

    if 'stplroot' in args and args['stplroot']:
        initroot(args['stplroot'], 'stpl')
    elif 'restroot' in args and args['restroot']:
        initroot(args['restroot'], 'rest')
    elif 'pygrep' in args and args['pygrep']:
        for f,i,l in grep(args['pygrep']):
            print('"{}":{} {}'.format(f,i,l))
    elif 'kw' in args and args['kw']:
        for _, (f,i,l) in yield_with_kw(args['kw']):
            print('"{}":{} {}'.format(f,i,l))
    elif 'infile' in args and args['infile']:
        for x in 'infile outfile outtype'.split():
            if x not in args:
                args[x] = None
        if 'I' in args and args['I']:
            g_include[:] = reduce(lambda x,y:x+y,args['I'],[])
        outinfo = args['outtype'] if args['outtype'] != '-' else None
        outfile = args['outfile']
        infiles = [args['infile']]
        outfiles = [args['outfile']]
        notexistsout = outfile and outfile!='-' and not os.path.exists(outfile)
        imgfiles = []
        if os.path.isdir(args['infile']):
            index_dir(args['infile'])
            if outfile is None:
                return
            imgfiles = [x for x in os.listdir(args['infile']) if _is_graphic(stem_ext(x)[1])]
            infiles = [x for x in os.listdir(args['infile']) if is_rest(x)]
            if notexistsout:
                mkdir(outfile)
        elif outfile:
            bout = base(outfile)
            fdo = bout.find('.')
            if notexistsout and not (fdo>0 and fdo<len(bout)-1):
                mkdir(outfile)
        if outinfo and outfile and os.path.isdir(outfile):
            if outinfo.startswith('sphinx'):
                onlyindex = [x for x in infiles if x.find('index.')>=0];
                if len(onlyindex)>0:
                    infiles = onlyindex;
            outfiles = [normjoin(outfile, _in_2_out_name(inf,outinfo)) for inf in infiles]
        for i in imgfiles:
            convert(i,None)
        for i,o in zip(infiles,outfiles):
            convert(i,o,outinfo)
    else:
        index_dir('.')

if __name__ == '__main__':
    main()
