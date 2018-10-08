#!/usr/bin/env python
#encoding: utf-8

##lns=open(__file__).readlines()
##list(gen_head(lns))
#def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
#def gen_head
##list(gen_api(lns))
#def gen_api(lns,**kw):
#    yield from doc_parts(lns,signature='py',prefix='dcx.')
#def gen_api

"""
.. _`rstdcx`:

rstdcx
======

Support script to create documentation (PDF, HTML, DOCX)
from restructuredText (RST) using either

- `Sphinx <http://www.sphinx-doc.org>`__
- `Pandoc <https://pandoc.org>`__
- Docutils front-end tools like `rst2html.py <http://docutils.sourceforge.net/docs/user/tools.html>`__

``rstdcx``, or ``dcx.py`` 

- processes ``gen`` files (see examples produced by --init)

- handles `.stpl <https://bottlepy.org/docs/dev/stpl.html>`__ files

- creates ``.tags`` to jump around with the editor

- creates links files like ``_links_pdf.rst``, ``_links_docx.rst``, ``_links_sphinx.rst``

See example at the end of ``dcx.py``.

Usage
-----

With ``rstdoc`` installed, ``./dcx.py`` in the following examples can be replaced by ``rstdcx``.

- Initialize example tree with one of::

  $ ./dcx.py --init tmp #.rest files
  $ ./dcx.py --stpl tmp #.rest.stpl files

- Only create .tags and _links_xxx.rst::

  $ cd tmp/src/doc
  $ ./dcx.py

- Create the docs (and .tags and _links_xxx.rst) with **make**::

  $ make html
  $ make epub
  $ make latex
  $ make docx
  $ make pdf

  The latter two are done by Pandoc, the others by Sphinx.
  With ``waf`` below you would use ``sphinx_xxx`` for Sphinx builds, else Pandoc is used.

- Create the docs (and .tags and _links_xxx.rst) with **waf** (preferred):

  Instead of using ``make`` one can load ``dcx.py`` in `waf <https://github.com/waf-project/waf>`__.
  ``waf`` also considers all recursively included files,
  such that a change in any of them results in a rebuild of the documentation. 
  All files can have an additional ``.stpl`` extension to use `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax>`__.

    $ waf configure
    $ waf --docs docx,sphinx_html,rst_odt

  ``rst_xxx`` via `rst2xxx.py <http://docutils.sourceforge.net/docs/user/tools.html>`__
  ``sphinx_xxx`` via `Sphinx <http://www.sphinx-doc.org>`__ and
  just ``xxx`` via `Pandoc <https://pandoc.org>`__.

  Images are placed into ``./_images`` or ``../_images``.
  The following image languages should be parallel to the ``.rest`` files and are automatically converted to ``.png`` and and placed into ``images``.

  - ``.tikz`` or ``.tikz.stpl``. 
    This needs LaTex and `sphinxcontrib-tikz <https://bitbucket.org/philexander/tikz>`__ and is rather slow.

  - `.svg <http://svgpocketguide.com/book/>`__ or ``.svg.stpl``

  - `.dot <https://graphviz.gitlab.io/gallery/>`__ or ``.dot.stpl``

  - `.uml <http://plantuml.com/command-line>`__ or ``.uml.stpl``
    This needs a plantuml.bat with e.g. ``java -jar "%~dp0plantuml.jar" %*`` 
    or plantuml sh script with ``java -jar `dirname $BASH_SOURCE`/plantuml.jar "$@"``.

  - ``.eps`__ or ``.eps.stpl`` embedded postscript files.
    This needs Ghostscript installed on the system.

  - ``.pyg`` contains python code that produces a graphic.
    If the python code defines a ``save_to_png`` function,
    then that is used.
    Else the following is tried

    - ``pyx.canvas.canvas`` from the `pyx <http://pyx.sourceforge.net/manual/graphics.html>`__ library or 
    - ``cairocffi.Surface`` from `cairocffi <https://cairocffi.readthedocs.io/en/stable/overview.html#basic-usage>`__
    - ``pygal.Graph`` from `pygal <https://pygal.org>`__
    - `matplotlib <https://matplotlib.org>`__. If ``matplotlib.pyplot.get_fignums()>1`` the figures result ``<name><fignum>.png`` 
    
Conventions
-----------

- Files 

  - main docs end in ``.rest``
  - ``.rst`` are included and ignored by Sphinx (see conf.py).
  - ``.txt`` are literally included (use :literal: option).
  - templates ``x.rest.stpl`` and ``y.rst.stpl`` are rendered separately before ``.. include: y.rst``.
  - ``some.rst.tpl`` are template included
    Template lookup is done in in ``.`` and ``..`` with respect to the current file.

    - with ``%include('some.rst.tpl',param="test")`` with optional parameters
    - with ``%globals().update(include('utility.rst.tpl'))`` if it contains only definitions

- ``.. _`id`:`` are RST targets.
  *RST targets* should not be template-generated. 
  The template files should have a higher or equal number of targets than the generated file,
  in order for tags to jump to the template original.
  If one wants to generate also rst targets, then this should happen in a previous step, 
  e.g. with ``gen`` files mentioned above. 

- References use replacement `substitutions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text>`__: ``|id|``.
  
See the example created with ``--init`` of ``--stpl`` at the end of this file and the sources of the documentation of 
`rstdoc <https://github.com/rpuntaie/rstdoc>`__.

"""


'''
API
---

.. code-block:: py

   import rstdoc.dcx as dcx


The functions in ``dcx.py`` are available to the ``gen_xxx(lns,**kw)`` functions (|dhy|).

'''

import sys
import os
import re
import subprocess
import io
from threading import Lock
from pathlib import Path
from urllib import request
from functools import lru_cache
from collections import OrderedDict,defaultdict
from itertools import chain, tee
from types import GeneratorType
from argparse import Namespace

DPI = 72

_tikzlock = Lock()

try:
    import cairocffi
    from cairosvg import svg2png
    def csvg2png(file,write_to):
        try:
            svg2png(url="file://"+file, write_to=write_to, dpi=DPI)
        except:
            svg2png(url="file:///"+file, write_to=write_to, dpi=DPI)
except Exception as e:
    print('cairosvg svg2png not available:',e)
    def svg2png(file,write_to): pass
    def csvg2png(file,write_to): pass

try:
    import pyfca
except Exception as e:
    print('pyfca not available:',e)
    pyfca = None

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except Exception as e:
    print('matplotlib not available:',e)
    plt = None


try:
    import pyx
except Exception as e:
    print('pyx not available:',e)
    pyx = None

try:
    import pygal
except Exception as e:
    print('pygal not available:',e)
    pygal = None

try:
    from PIL import Image, ImageChops
    def _trim_png(filename):
        def trim(im):
            bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
            diff = ImageChops.difference(im, bg)
            diff = ImageChops.add(diff, diff, 2.0, -100)
            bbox = diff.getbbox()
            if bbox:
                return im.crop(bbox)
        im = Image.open(filename)
        im = trim(im)
        im.save(filename)

    import ghostscript
    #rebbox = re.compile(r'%%BoundingBox:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+')
    _ghostscriptlock = Lock()
except Exception as e:
    print('ghostscript or PIL not available:',e)
    ghostscript = None

@lru_cache()
def conf_py(fldr):
    """
    ``conf.py`` or ``../conf.py`` is used for both sphinx and pandoc.

    """

    confpy = opnj(fldr,'conf.py')
    if not op.exists(confpy):
        confpy = updir(confpy)
    config={}
    with open(confpy,encoding='utf-8') as f:
        eval(compile(f.read(),op.abspath(confpy),'exec'),config)
    return config

verbose = False
_stpl = '.stpl'
_tpl = '.tpl'
_tikz = '.tikz'
is_rest = lambda x: x.endswith('.rest') or x.endswith('.rest'+_stpl)
is_rst = lambda x: x.endswith('.rst') or x.endswith('.rst'+_stpl) or x.endswith('.rst.tpl')

rextgt = re.compile(r'(?:^|^[^\.\%\w]*\s|^\s*\(?\w+[\)\.]\s)\.\. _`?(\w[^:`]*)`?:\s*$')
rexsubtgt = re.compile(r'(?:^|^[^\.\%\w]*\s|^\s*\(?\w+[\)\.]\s)\.\. \|(\w[^\|]*)\|\s\w+::')#no need to consider those not starting with \w, because rexlinksto starts with \w
rextitle = re.compile(r'^([!"#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~])\1+$')
rexitem = re.compile(r'^\s*:?\**(\w[^:\*]*)\**:\s*.*$')
rexoneword = re.compile(r'^\s*(\w+)\s*$')
rexname = re.compile(r'^\s*:name:\s*(\w.*)*$')
rexlnks = re.compile(r'(?:^|\s)\|(\w+)\|(?:\s|$)')
#list(rexlnks.findall('|xx| A `|lnk|` here |gos|\n'))#['xx', 'gos']
#list(rexlnks.findall('| |xeps1| | |xeps|  |'))
#rextgt.search('.. _`_t11`:').group(1)
#rextgt.search('  .. _`_t11`:').group(1)
#rextgt.search('#) .. _`_t11`:').group(1)
#rextgt.search('- .. _`_t11`:').group(1)
#rextgt.search('2) .. _`_t11`:').group(1)
#rextgt.search('2. .. _`_t11`:').group(1)
#rextgt.search('(a) .. _`_t11`:').group(1)
#rextgt.search('| .. _`_t11`:').group(1)
#rextgt.search('  * - .. _`_t11`:').group(1)
#rextgt.search('x  .. _`_t11`:').group(1)#nok
#rextgt.search('.. .. _`_t11`:').group(1)#nok
#rextgt.search('%# .. _`_t11`:').group(1)#nok
#rexsubtgt.search(' .. |t-1| image:: ').group(1)#ok
#rextgt.search('%# .. |t11| xx::').group(1)#nok
#rexitem.match(':``t11``:').group(1)#nok
#rexitem.match('.. _xx:').group(1)#nok
#rexitem.match('.. xx:').group(1)#nok
#rexitem.match(':t11:').group(1)#ok
#rexitem.match('**t11**:').group(1)#ok
#rexitem.match('*t11*:').group(1)#ok
reximg = re.compile(r'(?:image|figure):: ((?:\.|/|\\|\w).*)')
#reximg.search('.. image:: ..\img.png').group(1)
#reximg.search(r'.. |c:\x y\im.jpg| image:: /tmp/img.png').group(1)
#reximg.search(r'.. image:: c:\tmp\img.png').group(1)
#reximg.search(r'.. figure:: \\public\img.png').group(1)
rerstinclude = re.compile(r'\.\. include::\s*([\./\w\\].*)')
restplinclude = re.compile(r'''%\s*include\s*\(\s*["']([^'"]+)['"].*\)\s*''')
#rerstinclude.split('.. include:: test.rst')
#rerstinclude.split('.. include:: ../test.rst')
#rerstinclude.split('  .. include:: ../test.rst')
#restplinclude.split('%include("test.rst.stpl",v="aparam")')
#restplinclude.split('%include("../test.rst.stpl",v="aparam")')
#restplinclude.split(' % include(  "../test.rst.stpl",v="aparam")')

op = os.path
opnj = lambda *x:op.normpath(op.join(*x))
updir = lambda fn: opnj(op.dirname(fn),'..',op.split(fn)[1])
#fn='x/y/../y/a.b'
#updir(fn)#x\a.b
#updir('a.b')#..\a.b
#updir('a.b/a.b')#a.b
#opnj(fn)#x\y\a.b

trace_file_name = '_trace' #used for _trace.rst and _trace.svg
trace_target= 'index'

def rindices(
    r #regular expression string or compiled
    ,lns #lines
    ):
    r'''
    Return the indices matching the regular expression ``r``.

    ::

      >>> lns=['a','ab','b','aa']
      >>> [lns[i] for i in rindices(r'^a\w*',lns)]==['a', 'ab', 'aa']
      True

    '''

    if isinstance(r,str):
        r = re.compile(r)
    for i,ln in enumerate(lns):
        if r.search(ln):
            yield i 

def rlines(
    r #regular expression string or compiled
    ,lns #lines
    ):
    '''
    Return the lines matched by ``r``.
    '''

    return [lns[i] for i in rindices(r,lns)]

def intervals(
    nms #list of indices
    ):
    """
    Return intervals between numbers.

    ::

      >>> intervals([1,2,3])==[(1, 2), (2, 3)]
      True

    """
    return list(zip(nms[:],nms[1:]))

def in2s(
    nms #list of indices
    ):
    """
    Convert the list into a list of couples of two elements.
    
    ::

      >>> in2s([1,2,3,4])==[(1, 2), (3, 4)]
      True

    """
    return list(zip(nms[::2],nms[1::2]))


#re.search(reid,'OpenDevices = None').groups()
#re.search(reid,'def OpenDevices(None)').groups()
#re.search(reid,'class OpenDevices:').groups()
#re.search(reid,'    def __init__(a,b):').groups()

#re.search(relim,"  '''prefix. ").groups()
#re.search(relim,"  '''").groups()

def doc_parts(
    lns #list of lines
    ,relim=r"^\s*'''([\w.:]*)\s*\n*$" #regular expression marking lines enclosing the documentation. The group is a prefix.
    ,reid=r"\s(\w+)[(:]|(\w+)\s\=" #extract id from preceding or succeeding non-empty lines
    ,reindent=r'[^#/\s]' #determines start of text
    ,signature=None #if signature language is given the preceding or succeeding lines will be included
    ,prefix='' #prefix to make id unique, e.g. module name. Include the dot.
    ):
    '''
    ``doc_parts()`` yields doc parts delimeted by ``relim`` regular expression
    possibly with id, if ``reid`` matches 

    If start and stop differ use regulare expression ``|`` in ``relim``.

    ::

      >>> with open(__file__,encoding='utf-8') as f:
      ...     lns = f.readlines()
      ...     docparts = list(doc_parts(lns,signature='py'))
      ...     doc_parts_line = rlines('doc_parts',docparts)
      >>> doc_parts_line[1]
      'doc_parts(\n'

    - There is no empty line between doc string and preceding code lines that should be included.
    - There is no empty line between doc string and succeeding code lines that should be included.
    - Included code lines end with an empty line.

    In case of ``__init__()`` the ID can come from the ``class`` line
    and the included lines can be those of ``__init__()``,
    if there is no empty line between the doc string and ``class`` above as well as ``_init__()`` below.

    If the included code comes only from one side of the doc string, have an empty line at the other side.

    Immediately after the initial doc string marker there can be a prefix, e.g. ``classname.``.

    '''

    rlim = re.compile(relim)
    rid = re.compile(reid)
    rindent = re.compile(reindent)
    def foundid(lnsi):
        if not lnsi.strip():#empty
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
            elif not ids and isinstance(testid,str):
                ids.append(testid)
        return i
    for a,b in in2s(list(rindices(rlim,lns))):
        try:
            thisprefix = rlim.search(lns[a]).groups()[0]
        except:
            thisprefix = ''
        ids.clear()
        i = checkid(range(a-1,0,-1))
        j = checkid(range(b+1,len(lns)))
        if ids:
            yield ''
            yield '.. _`'+prefix+thisprefix+ids[0]+'`:\n'
            yield ''
            yield ':'+prefix+thisprefix+ids[0]+':\n'
            yield ''
        if signature:
            if i is not None and i < a and i > 0:
                if not lns[i].strip():#empty
                    i = i+1
                if i < a:
                    yield '.. code-block:: '+signature+'\n'
                    yield ''
                    yield from ('   '+x for x in lns[i:a])
                    yield ''
            if j is not None and j > b+1 and j < len(lns):
                if not lns[j].strip():#empty
                    j = j-1
                if j > b:
                    yield '.. code-block:: '+signature+'\n'
                    yield ''
                    yield from ('   '+x for x in lns[b+1:j+1])
                    yield ''
        indent = 0
        for ln in lns[a+1:b]:
            lnst = rindent.search(ln)
            if lnst and lnst.span():
                indent = lnst.span()[0]
                break;
        yield from (x[indent:] for x in lns[a+1:b])

#for generator function, instead of lru_cache()
_Tee = tee([], 1)[0].__class__
def _memoized(f):
    cache={}
    def ret(*args):
        if args not in cache:
            cache[args]=f(*args)
        if isinstance(cache[args], (GeneratorType, _Tee)):
            cache[args], r = tee(cache[args])
            return r
        return cache[args]
    return ret

@lru_cache()
def _read_lines(fn):
    lns = []
    with open(fn,'r',encoding='utf-8') as f:
        lns = f.readlines()
    return lns

def _read_stpl_lines_it(fn):
    """
    This flattens the .stpl includes to have all targets align to those in the .rest file.
    Targets must be *explicit* in all ``.stpl`` and ``.tpl``, i.e. they must not be created by stpl code.
    This is needed to make the .tags jump to the original and not the generated file.
    """
    flns = []
    if op.exists(fn):
        flns = _read_lines(fn)
    else:
        parnt = updir(fn)
        if op.exists(parnt):
            flns = _read_lines(parnt)
    for i,ln in enumerate(flns):
        #ln = '% include("../test.rst.stpl",v="aparam")'
        m = restplinclude.match(ln)
        if m: 
            includedtpl = m.group(1)
            yield from _read_stpl_lines(op.join(op.dirname(fn),includedtpl))
        else:
            yield fn,i,ln

@lru_cache()
def _read_stpl_lines(fn):
    return list(_read_stpl_lines_it(fn))

@_memoized
def rstincluded(
    fn #file name without path
    ,paths=() #paths where to look for fn
    ,withimg=False #also yield image files, not just other rst files
    ):
    '''
    Yield the files recursively included from an RST file.

    >>> list(rstincluded('ra.rest',paths=('../doc',)))
    ['ra.rest.stpl', '_links_sphinx.rst']
    >>> list(rstincluded('sr.rest',paths=('../doc',)))
    ['sr.rest', '_links_sphinx.rst']
    >>> list(rstincluded('meta.rest',paths=('../doc',)))
    ['meta.rest', 'files.rst', '_trace.rst', '_links_sphinx.rst']
    >>> 'dd.rest'in list(rstincluded('index.rest',paths=('../doc',)))
    True

    '''

    p = ''
    for p in paths:
        nfn = opnj(p,fn)
        if op.exists(nfn+_stpl): #first, because original
            nfn = nfn+_stpl
            yield fn+_stpl
            break
        elif op.exists(nfn): #while this might be generated
            yield fn
            break
    else:
        nfn = fn
        yield fn
    lns = _read_lines(nfn)
    toctree = False
    if lns:
        for e in lns:
            if toctree:
                toctreedone = False
                if e.startswith(' '):
                    fl=e.strip()
                    if fl.endswith('.rest') and op.exists(op.join(p,fl)):
                        toctreedone = True
                        yield from rstincluded(fl,paths)
                    continue
                elif toctreedone:
                    toctree = False
            if e.startswith('.. toctree::'):
                toctree = True
            elif e.strip().startswith('.. '):
                #e = '  .. include:: some.rst'
                #e = '  .. include:: ../some.rst'
                #e = '.. include:: some.rst'
                #e = '.. include:: ../some.rst'
                #e = '  .. image:: some.png'
                #e = '.. image:: some.png'
                #e = '  .. figure:: some.png'
                #e = '  .. |x y| image:: some.png'
                try:
                    f,t,_ = rerstinclude.split(e)
                    nf = not f.strip() and t
                    if nf:
                        yield from rstincluded(nf.strip(),paths)
                except:
                    if withimg:
                        m = reximg.search(e)
                        if m:
                            yield m.group(1)
            elif restplinclude.match(e): 
                #e="%include('some.rst.tpl',v='param')"
                #e="   %include('some.rst.tpl',v='param')"
                f,t,_=restplinclude.split(e)
                nf = not f.strip() and t
                if nf:
                    thisnf = op.join(p,nf)
                    if not op.exists(thisnf):
                        parntnf = opnj(p,'..',nf)
                        if op.exists(parntnf): 
                            nf = parntnf
                        else:
                            continue
                    yield from rstincluded(nf.strip(),paths)

def fldrincluded(
        directory='.'
        ,exclude_paths_substrings = ['_links_','index.rest',trace_file_name]
        ):
    ''' 
    Yield a list of .rest files for each directory below ``directory``.
    The list also includes all files recursively included via these `.rest` files,
    excluding those that contain ``exclude_paths_substrings``

    >>> metafrozenset = frozenset(['../doc/meta.rest', '../doc/files.rst'])
    >>> metafrozenset in set(frozenset(x) for x in fldrincluded('../doc'))
    True

    '''

    global trace_target
    sofar = []
    for p,ds,fs in os.walk(directory):
        for f in reversed(sorted(fs)):
            if is_rest(f):
                pf=opnj(p,f)
                if any([x in pf for x in exclude_paths_substrings]):
                    continue
                if pf in sofar:
                    continue
                sofar.append(pf)
                if pf.endswith(_stpl):
                    sofar.append(pf[:-len(_stpl)])
                pths = []
                for ff in rstincluded(f,(p,)):
                    if trace_file_name in ff:
                        trace_target = op.splitext(f)[0]
                    if any([x in ff for x in exclude_paths_substrings]):
                        continue
                    pth=opnj(p,ff)
                    if any([x in pth for x in exclude_paths_substrings]):
                        continue
                    pths.append(pth.replace("\\","/"))
                yield pths

def make_lnks(lns):
    for i,ln in enumerate(lns):
        mo = rexlnks.findall(ln)
        for g in mo:
            yield i,g

def pair(
    alist #first list
    ,blist #second list longer or equal to alist
    ,cmp #compare function
    ):
    ''' 
    pair two sorted lists where the second must be at least as long as the first
    
    >>> alist=[1,2,4,7]
    ... blist=[1,2,3,4,5,6,7]
    ... cmp = lambda x,y: x==y
    ... list(pair(alist,blist,cmp))
    [(1, 1), (2, 2), (None, 3), (4, 4), (None, 5), (None, 6), (7, 7)]

    '''

    i = 0
    for i,(aa,bb) in enumerate(zip(alist,blist)):
        if not cmp(aa,bb):
            break
        yield aa,bb
    alen = len(alist)
    tlen = max(alen,len(blist))
    d = 0
    for j in range(i,alen):
        for dd in range(tlen-j-d):
            bb = blist[j+d+dd]
            if not cmp(alist[j],bb):
                yield None,bb
            else:
                yield alist[j],bb
                d = d+dd
                break
        else:
            return

class RstDocError(Exception):
    pass

g_counters=defaultdict(dict)

def get_substitutions(
    lns  #lines of the rst document
    ):
    '''
    Return all substitution targets in the restructuredText lns

    >>> list(get_substitutions("""
    ...   .. |sub| image:: xx
    ...   .. |s-b| date::
    ...   """.splitlines()))
    ['sub', 's-b']


    '''
    for i,ln in enumerate(lns):
        asub = rexsubtgt.search(ln)
        if asub:
            yield asub.group(1)


def make_tgts(
    lns  #lines of the document
    ,docrest #doc .rest or .rest.stpl file name
    ,stpl_lns=None #the lines of the .stpl file that generated the .rest file
    ):
    '''
    Yields ((line index, linkname), target, link name) of ``lns`` of a restructureText file.
    For a .stpl file the linkname comes from the generated .rest file.

    '''

    docprefix = ' '
    if docrest not in g_counters:
        g_counters[docrest] = {".. figure":1,".. math":1,".. table":1,".. code":1} #=list-table,code-block
    counters=g_counters[docrest]
    itgts = list(rindices(rextgt,lns))
    if stpl_lns:
        lns1 = [x[2] for x in stpl_lns]
        itgts1 = list(rindices(rextgt,lns1))
    else:
        lns1 = lns
        itgts1 = itgts
    if len(itgts)<len(itgts1):
        paired_itgts_itgts1 = pair(itgts,itgts1,lambda x,y:lns[x]==lns1[y])
    elif len(itgts)>len(itgts1):
        print("Warning: rest has more targets (.. _`xx`:) than stpl. Either not up-to-date (run 'stpl {0}' first) or targets generated: tags will not link to stpl.".format(docrest))
        paired_itgts_itgts1 = ((i,j) for (j,i) in pair(itgts1,itgts,lambda x,y:lns1[x]==lns[y]))
    else:
        paired_itgts_itgts1 = zip(itgts,itgts1)
    lenlns = len(lns)
    lenlns1 = len(lns1)
    def is_literal(ii,iis,spc):
        for iprev in range(ii-1,0,-1):
           prev = iis[iprev]
           if prev:
               newspc,_ = next((ich,ch) for ich,ch in enumerate(prev) if ch!=' ' and ch!='\t')
               if newspc<spc:
                   prev = prev.strip()
                   if prev:
                       if not prev.startswith('.. ') and prev.endswith('::'):
                           return True
                       return False
    for i,i1 in paired_itgts_itgts1:
        ii,iis,iilen = (i,lns,lenlns) if i else (i1,lns1,lenlns1)
        cur = iis[ii]
        tgt = rextgt.search(cur).group(1)
        #cur = ' .. _`x`:'
        try:#skip literal blocks
            spc = re.search(r'\w',cur).span()[0]-3
            if spc>0 and is_literal(ii,iis,spc):
                continue
        except:
            pass
        lnkname = tgt
        for j in range(ii+2,ii+8):
            #j=i+2
            if j > iilen-1:
                break
            lnj = iis[j]
            if rextitle.match(lnj):
                lnkname=iis[j-1].strip()
                if not lnkname:
                    lnkname=iis[j+1].strip()
                break
            #j,iis=1,".. figure::\n  :name: lnkname".splitlines();lnj=iis[j]
            #j,iis=1,".. figure::\n  :name:".splitlines();lnj=iis[j]
            #j,iis=1,".. math::\n  :name: lnkname".splitlines();lnj=iis[j]
            itm = rexname.match(lnj)
            if itm:
                lnkname, = itm.groups()
                lnj1 = iis[j-1].split('::')[0].replace('list-table','table').replace('code-block','code').strip()
                if not lnkname and lnj1 in counters:
                    lnkname = lnj1[3].upper()+lnj1[4:]+docprefix+str(counters[lnj1])
                    counters[lnj1]+=1
                    break
                elif lnkname:
                    lnkname = lnkname.strip()
                    break
            #lnj=":lnkname: words"
            itm = rexitem.match(lnj)
            if itm:
                lnkname, = itm.groups()
                break
            itm = rexoneword.match(lnj)
            if itm:
                lnkname, = itm.groups()
                break
            lnkname = tgt
        #tgts
        if i1:
            yield (i,stpl_lns[i1][:2] if stpl_lns else (docrest,ii)), tgt, lnkname
        else:
            yield (i,(docrest.replace(_stpl,''),ii)), tgt, lnkname

def gen(
    source #either a list of lines of a path to the source code
    ,target=None #either save to this file or return the generated documentation
    ,fun=None #use ``#gen_<fun>(lns,**kw):`` to extract the documtenation
    ,**kw #kw arguments to the gen_<fun>() function
    ):
    r''' 
    Take the ``gen_[fun]`` functions enclosed by ``#def gen_[fun](lns,**kw)`` to create a new file.

    Example::

        >>> source=[i+'\\n' for i in """
        ...        #def gen(lns,**kw):
        ...        #  return [l.split('#@')[1] for l in rlines(r'^\s*#@',lns)]
        ...        #def gen
        ...        #@some lines
        ...        #@to extrace
        ...        """.splitlines()]
        >>> [l.strip() for l in gen(source)]
        ['some lines', 'to extrace']

    '''

    if isinstance(source,list):
        lns = source
        source = ""
    else:
        lns = []
        try:
            lns = _read_lines(source)
        except:
            sys.stderr.write("ERROR: {} cannot be opened\n".format(source))
            return
    if '.' not in sys.path:
        sys.path.append('.')
    if fun:
        gen_regex = r'#def gen_'+fun+r'(\w*(lns,\*\*kw):)*'
    else:
        gen_regex = r'#def gen(\w*(lns,\*\*kw):)*'
    iblks = list(rindices(gen_regex,lns))
    py3 = '\n'.join([lns[k][lns[i].index('#')+1:] 
            for i,j in in2s(iblks) 
            for k in range(i,j)])
    eval(compile(py3,source+'#gen','exec'),globals())
    if fun:
        gened = list(eval('gen_'+fun+'(lns,**kw)'))
    else:#else eval all gen_ funtions
        gened = []
        for i in iblks[0::2]:
            cd = re.split("#def |:",lns[i])[1]#gen(lns,**kw)
            gened += list(eval(cd))
    if target:
        drn = op.dirname(target)
        if drn and not op.exists(drn):
            os.makedirs(drn)
        with open(target,'w',encoding='utf-8') as o:
            o.write(''.join(((x or '\n') for x in gened)))
    else:
        return gened

def parsegenfile(
    genpth #path to gen file
    ):
    '''
    Parse the file ``genpth`` which has format ::

      sourcefile | targetfile | suffix | kw paramams or {}

    ``suffix`` refers to ``gen_<suffix>``.

    The yields are used for the |dcx.gen| function.
    '''

    try:
        genfilelns = _read_lines(genpth)
    except:
        sys.stderr.write("ERROR: {} cannot be opened\n".format(genpth))
        return
        
    for ln in genfilelns:
        if ln[0] != '#':
            try:
              f,t,d,a = [x.strip() for x in ln.split('|')]
              kw=eval(a)
              yield f,t,d,kw
            except: pass

def mkdir(ef):
    try:
        os.mkdir(ef)
    except:
        pass

def mktree(
    tree #tree string as list of lines
    ):
    ''' 

    Build a directory tree from a string as returned by the tree tool.

    The level is determined by the identation.

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

    for treestart,t in enumerate(tree):
        try:
            ct = re.search(r'[^\s├│└]',t).span()[0]
            break
        except:
            continue
    t1 = [t[ct:] for t in tree[treestart:]]
    entry_re = re.compile(r'^(\w[^ </\\]*)(\s*<<\s*|\s*[\\/]\s*)*(\w.*)*')
    it1 = list(rindices(entry_re,t1))
    lt1 = len(t1)
    it1.append(lt1)
    for c,f in intervals(it1):
        ef,ed,eg = entry_re.match(t1[c]).groups()
        if ef:
            if c<f-1:
                p1 = t1[c+1].find('└')+1
                p2 = t1[c+1].find('├')+1
                ix = (p1>=0 and p1 or p2)-1
                if ix >= 0 and ix <= len(ef):
                    mkdir(ef)
                    old = os.getcwd()
                    try:
                        os.chdir(ef)
                        mktree(
                          t1[c+1:f]
                          )
                    finally:
                        os.chdir(old)
                else:
                    t0 = t1[c+1:f]
                    try:
                        ct = re.search(r'[^\s│]',t0[0]).span()[0]
                    except:
                        print(c,f,'\n'.join(t0[:10]))
                        print("FIRST LINE OF FILE CONTENT MUST NOT BE EMPTY!")
                    tt = [t[ct:]+'\n' for t in t0]
                    with open(ef,'w',encoding='utf-8') as fh:
                        fh.writelines(tt)
            elif eg:
                try:
                    request.urlretrieve(eg,ef)
                except: pass
            elif ed and (('\\' in ed) or ('/' in ed)):
                mkdir(ef)
            else:
                Path(ef).touch()

def tree(
    path #path of which to create the tree string
    ,with_content=False #use this only if all the files are text
    ,with_files=True #else only directories are listed
    ,with_dot_files=True #also include files starting with .
    ,max_depth=100 #max folder depth to list
    ):
    '''
    Inverse of mktree.
    Like the linux tree tool, but optionally with content of files

    ::

      >>> path='.'
      >>> tree(path,False)
      >>> tree(path,True)

    '''

    subprefix = ['│  ', '   '] 
    entryprefix = ['├─', '└─']
    def _tree(path, prefix):
        for p,ds,fs in os.walk(path):
            #p,ds,fs = path,[],os.listdir()
            lends = len(ds)
            lenfs = len(fs)
            if len(prefix)/3 >= max_depth:
                return
            for i,d in enumerate(sorted(ds)):
                yield prefix + entryprefix[i==lends+lenfs-1] + d
                yield from _tree(op.join(p,d),prefix+subprefix[i==lends+lenfs-1])
            del ds[:]
            if with_files:
                for i,f in enumerate(sorted(fs)):
                    if with_dot_files or not f.startswith('.'):
                        yield prefix + entryprefix[i==lenfs-1] + f
                        if with_content:
                            for ln in _read_lines(op.join(p,f)):
                                yield prefix + subprefix[1] + ln
    return '\n'.join(_tree(path, ''))


def fldrs(
    scanroot='.' #root path to start scanning for independent doc folders
    ):
    '''
    Yields::

        fldr, (lnktgts,allfiles,alltgts)

    These are used by |dcx.links_and_tags|.
    '''

    odir = os.getcwd()
    try:
        os.chdir(scanroot)
        fldr_lnktgts = OrderedDict()
        fldr_allfiles = defaultdict(set) #fldr, files
        fldr_alltgts = defaultdict(set) #all link target ids
        fldr_substitutions = defaultdict(set) #all link target ids
        dcns=set([])
        for dcs in fldrincluded('.'): 
            rest = next(adc for adc in dcs if is_rest(adc))
            restpath,restext = op.splitext(rest)
            fldr,name_without_rest = op.split(restpath)
            fldr_allfiles[fldr] |= set(dcs)
            if restext == _stpl:
                reststpl = True
                name_without_rest=op.splitext(name_without_rest)[0]
            else:
                reststpl = False
            dcns.add(name_without_rest)
            for doc in dcs:
                if doc==rest and reststpl and op.exists(restpath):
                    lns = _read_lines(restpath)
                    stpl_lns = _read_stpl_lines(doc)
                    tgts = list(make_tgts(lns,doc,stpl_lns))
                elif not doc.endswith('.tpl') and not doc.endswith('.txt') and op.exists(doc):
                    #.txt are considered literal include
                    #%include('x.rst.tpl') were considered via STPL in the first branch
                    #.tpl MUST NOT HAVE TARGETS
                    lns = _read_lines(doc)
                    tgts = list(make_tgts(lns,doc))
                else:
                    continue
                lnks = list(make_lnks(lns))
                if fldr not in fldr_lnktgts:
                    fldr_lnktgts[fldr] = []
                fldr_lnktgts[fldr].append((name_without_rest,doc,len(lns),lnks,tgts))
                fldr_alltgts[fldr] |= set([n for _,n,_ in tgts])
                fldr_substitutions[fldr] |= set(get_substitutions(lns)) 
        for fldr,lnktgts in fldr_lnktgts.items():
            allfiles = fldr_allfiles[fldr]
            alltgts = fldr_alltgts[fldr]
            substitutions = fldr_substitutions[fldr]
            yield fldr, (lnktgts,allfiles,alltgts,substitutions)
    finally:
        os.chdir(odir)

links_types = "sphinx latex html pdf docx odt".split()
def create_link(linktype,filenoext,tgt,lnkname):
    if linktype == 'latex':
        linktype = 'pdf'
    if linktype=='sphinx':
        tgte = ".. |{0}| replace:: :ref:`{1}<{0}>`\n".format(tgt,lnkname)
    elif linktype=='odt':
        #https://github.com/jgm/pandoc/issues/3524
        tgte = ".. |{0}| replace:: `{1} <../{2}#{0}>`__\n".format(tgt,lnkname,filenoext+'.'+linktype)
    else:
        tgte = ".. |{0}| replace:: `{1} <{2}#{0}>`__\n".format(tgt,lnkname,filenoext+'.'+linktype)
    return tgte

def links_and_tags(
    fldr #folder path
    ,lnktgts  #list of links and targets in a document (name_without_rest, doc, lenlns, lnks, tgts)
    ,allfiles #all files in one folder
    ,alltgts  #all targets of the whole folder
    ,substitutions  #all substitution definitions in the whole folder
    ):
    '''
    Creates links_xxx.rst and .tags files for a folder ``fldr`` in that folder.

    If ``pyfca`` is available also the dependencies file ``_trace.rst`` is created.

    conf.py entries::

      target_id_group = lambda targetid: targetid[0]
      target_id_color={
          "meta":("m","white"),
          "ra":("r","lightblue"),
          "sr":("s","red"),
          "dd":("d","yellow"), 
          "tp":("t","green"),
          "rstdoc":("o","pink")}
      html_extra_path=["_images/_trace.svg"]

    The target IDs are grouped. To every group a color is associated. See ``conf.py``.
    This is used to color an FCA lattice diagram in "_trace.rst".
    The diagram nodes are clickable in HTML.

    For ``_trace.png`` one needs the cairosvg library.

    '''

    linkfiles = [(linktype,[]) for linktype in links_types]
    tagentries = []
    objects = [] #in FCA sense: set of target tgt with all its links to other targets 
    upcnt = 0
    if (fldr.strip()):
       upcnt = len(fldr.split(os.sep))
    #unknowntgts = []
    def tracelines():
        try:
            config = conf_py(fldr)
            target_id_group = config['target_id_group']
            target_id_color = config['target_id_color']

            def _drawnode(canvas,node,parent,center,radius): 
                fillcolors = []
                nodetgtgrps = {target_id_group(x) for x in node.intent}
                for _,(groupid,groupcolor) in target_id_color.items():
                    if groupid in nodetgtgrps:
                        fillcolors.append(groupcolor)
                n_grps = len(fillcolors)
                for i in range(n_grps-1,-1,-1):
                    rr = int(radius*(i+1)/n_grps)
                    parent.add(canvas.circle(center,rr,fill=fillcolors[i],stroke='black'))
        except Exception as e:
            print('Warning: ',e)
            _drawnode = None
            target_id_color=None
        print('='*30+'1')#XXX
        fca = pyfca.Lattice(objects,lambda x:x)
        tr = 'tr'
        reflist = lambda x,pfx=tr: ('|'+pfx+('|, |'+pfx).join([str(x)for x in sorted(x)])+'|') if x else ''
        trace = [(".. _`"+tr+"{0}`:\n\n:"+tr+"{0}:\n\n{1}\n\nUp: {2}\n\nDown: {3}\n\n").format(
                n.index, reflist(n.intent,''), reflist(n.up), reflist(n.down))
                for n in fca.nodes]
        tlines = ''.join(trace).splitlines(keepends=True)
        tlines.extend(['.. _`trace`:\n','\n','.. figure:: _images/'+trace_file_name+'.png\n','   :name:\n','\n',
          '   |trace|: `FCA <https://en.wikipedia.org/wiki/Formal_concept_analysis>`__ diagram of dependencies'])
        if target_id_color is not None:
            legend=', '.join([fnm+" "+clr for fnm,(_,clr) in target_id_color.items()])
            tlines.extend([': '+legend,'\n'])
        tlines.append('\n')
        print('='*30+'1')#XXX
        with open(opnj(fldr,trace_file_name+'.rst'),'w',encoding='utf-8') as f:
            f.write('.. raw:: html\n\n')
            #needs in conf.py: html_extra_path=["_images/_trace.svg"]
            f.write('    <object data="'+trace_file_name+'.svg" type="image/svg+xml"></object>\n')
            if target_id_color is not None:
                f.write('    <p><a href="https://en.wikipedia.org/wiki/Formal_concept_analysis">FCA</a> diagram of dependencies with clickable nodes: '+legend+'</p>\n\n')
            f.writelines(tlines)
        ld = pyfca.LatticeDiagram(fca,4*297,4*210)
        mkdir(opnj(fldr,"_images"))
        tracesvg = op.abspath(opnj(fldr,"_images",trace_file_name+'.svg'))
        ttgt = lambda : trace_target.endswith('.rest') and op.splitext(trace_target)[0] or trace_target
        ld.svg(target=ttgt()+'.html#'+tr,drawnode=_drawnode).saveas(tracesvg)
        pngf = tracesvg.replace('.svg','.png')
        csvg2png(file=tracesvg, write_to=pngf)
        return tlines
    def add_target(tgt,lnkname,name_without_rest,upcnt,fi):
        for linktype,linklines in linkfiles:
            linklines.append(create_link(linktype,name_without_rest,tgt,lnkname))
        tagentries.append(r'{0}	{1}	/\.\. _`\?{0}`\?:/;"		line:{2}'.format(tgt,"../"*upcnt+fi[0],fi[1]))
    def add_linksto(i,tgt,iterlnks,ojlnk=None): #all the links away from the block following this tgt to next tgt
        linksto = []
        print('='*40,ojlnk)#XXX
        if ojlnk and ojlnk[0] < i:
            if ojlnk[1] in alltgts:
                linksto.append(ojlnk[1])
            elif ojlnk[1] not in substitutions:
                linksto.append('-'+ojlnk[1])
                #unknowntgts.append(ojlnk[1])
            tgt = ojlnk[2]
            ojlnk = None
        if ojlnk is None:
            for j, lnk in iterlnks:
                if j > i:#links upcnt to this target
                    ojlnk = j,lnk,tgt
                    break
                else:
                    if lnk in alltgts:
                        linksto.append(lnk)
                    elif lnk not in substitutions:
                        linksto.append('-'+lnk)
                        #unknowntgts.append(lnk)
        if linksto:
            if ojlnk:
                objects.append(set([x for x in linksto if not x.startswith('-') and not x.startswith('_')]+[tgt]))
            linksto = '.. .. ' + ','.join(linksto) + '\n\n'
            for _,linklines in linkfiles:
                linklines.append(linksto)
        return ojlnk
    olddc = None
    for name_without_rest, doc, lenlns, lnks, tgts in lnktgts:
         for _,linklines in linkfiles:
             linklines.append('\n.. .. {0}\n\n'.format(doc))
         iterlnks = iter(lnks)
         ojlnk=None
         for (i,fi),tgt,lnkname in tgts:
             if i is not None:
               ojlnk = add_linksto(i,tgt,iterlnks,ojlnk)
               add_target(tgt,lnkname,name_without_rest,upcnt,fi)
         ojlnk = add_linksto(lenlns,None,iterlnks,ojlnk)
         if not verbose:
             continue
         if '/'+name_without_rest+'.' in doc:
             print('    '+doc)
         else:
             print('        '+doc)
    print('='*30+'1')#XXX
    if len(objects)>0:
        tlns = tracelines()
        if tlns:
            for (_,fi),tgt,lnkname in make_tgts(tlns,trace_file_name+'.rst') :
                add_target(tgt,lnkname,trace_target,0,fi)
    for linktype,linklines in linkfiles:
        with open(opnj(fldr,'_links_%s.rst'%linktype),'w',encoding='utf-8') as f:
            f.write('\n'.join(linklines));
    try:
        subprocess.run(['ctags','-R','--sort=0','--fields=+n','--languages=python','--python-kinds=-i','-f','.tags','*'],
            cwd=fldr if fldr else os.getcwd())
        with open(opnj(fldr,'.tags'),'ab') as f:
            f.write('\n'.join(tagentries).encode('utf-8'));
    except Exception as e: 
        print('Warning: ctags failed with ', e, fldr)
        with open(opnj(fldr,'.tags'),'wb') as f:
            f.write('\n'.join(tagentries).encode('utf-8'));

#==============> for building with WAF

try:
    from waflib import TaskGen, Task
    import stpl

    @lru_cache()
    def _ant_glob_stpl(bldpath,*stardotext):
        res = []
        sofar = []
        for an_ext in stardotext:
          stplsfirst = bldpath.ant_glob(an_ext+_stpl)
          for anode in stplsfirst:
              sofar.append(anode.name[:-len(_stpl)])
              res.append(anode)
          nonstpls = bldpath.ant_glob(an_ext)
          for anode in nonstpls:
              if anode.name not in sofar:
                  res.append(anode)
        return res
    @lru_cache()
    def _pth_nde_parent(foldernode,name):
        existsin = lambda x: op.exists(op.join(x.abspath(),name))
        _parent = foldernode.parent
        if existsin(_parent):
            pth = '../'+name
            nde = _parent.find_node(name)
        else:
            pth = name
            _parent = foldernode
            if existsin(_parent):
                nde = _parent.find_node(name)
            else:
                nde = _parent.make_node(name)
        return pth,nde,_parent.abspath()
    gensrc={}
    @TaskGen.feature('gen_files')
    @TaskGen.before('process_rule')
    def gen_files(self):
        global gensrc
        gensrc={}
        for f,t,fun,kw in parsegenfile(self.path.make_node('gen').abspath()):
            gensrc[t]=f
            frm = self.path.find_resource(f)
            twd = self.path.make_node(t)
            self.create_task('gentsk',frm,twd,fun=fun,kw=kw)
    class gentsk(Task.Task):
        def run(self):
            frm = self.inputs[0]
            twd = self.outputs[0]
            twd.parent.mkdir()
            gen(frm.abspath(),twd.abspath(),fun=self.fun,**self.kw)
    def get_docs(bld):
        docs = [x.lower() for x in bld.options.docs]
        if not docs:
            docs = [x.lower() for x in bld.env.docs]
        return docs
    @lru_cache()
    def get_files_in_folder(path):
        deps = []
        for rest in _ant_glob_stpl(path,'*.rest'):
            if not rest.name.startswith('index'):
                fles = rstincluded(rest.name,(rest.parent.abspath(),))
                for x in fles:
                    isrst = is_rst(x)
                    if isrst and x.startswith('_links_'):#else cyclic dependency for _links_xxx.rst
                        continue
                    nd = path.find_node(x)
                    if not nd:
                        if isrst and not x.endswith(_stpl) and not x.endswith('.tpl'):
                            nd = path.find_node(x+_stpl)
                    deps.append(nd)
        depsgensrc = [path.find_node(gensrc[x]) for x in deps if x and x in gensrc] 
        rs = [x for x in deps if x]+depsgensrc
        return (list(sorted(set(rs),key=lambda a:a.name)),[])
    @lru_cache()
    def get_files_in_doc(path,node):
        srcpath = node.parent.get_src()
        orgd = node.parent.abspath()
        d = srcpath.abspath()
        n = node.name
        nod = None
        if node.is_bld() and not node.name.endswith(_stpl) and not x.endswith('.tpl'):
            nod = srcpath.find_node(node.name+_stpl)
        if not nod:
            nod = node
        ch = rstincluded(n,(d,orgd),True)
        deps = []
        nodeitself=True
        for x in ch:
            if nodeitself:
                nodeitself = False
                continue
            isrst = is_rst(x)
            if isrst and x.startswith('_links_'):#else cyclic dependency for _links_xxx.rst
                    continue
            nd = srcpath.find_node(x)
            if not nd:
                if isrst and not x.endswith(_stpl) and not x.endswith('.tpl'):
                    nd = srcpath.find_node(x+_stpl)
            deps.append(nd)
        depsgensrc = [path.find_node(gensrc[x]) for x in deps if x and x in gensrc] 
        rs = [x for x in deps if x]+depsgensrc
        return (list(sorted(set(rs),key=lambda a:a.name)),[])
    @TaskGen.feature('gen_links')
    @TaskGen.after('gen_files')
    def gen_links(self):
        docs=get_docs(self.bld)
        if docs:
            for so in self.path.ant_glob('*.stpl'):
                tsk = Namespace()
                tsk.inputs=(so,)
                tsk.env = self.env
                tsk.generator = self
                render_stpl(tsk,self.bld)
            for fldr, (lnktgts,allfiles,alltgts,substitutions) in fldrs(self.path.abspath()):
                links_and_tags(fldr,lnktgts,allfiles,alltgts,substitutions)
    def render_stpl(tsk,bld):
        bldpath = bld.path.get_bld()
        ps = tsk.inputs[0].abspath()
        try:
            pt = tsk.outputs[0].abspath()
        except:
            if ps.endswith(_stpl):
                pt = ps[:-len(_stpl)]
            else:
                raise RstDocError('No target for %s'%ps)
        lookup,name=op.split(ps)
        env = dict(tsk.env)
        env.update(tsk.generator.__dict__)
        #if the .stpl needs a parameter, then this fails, since it is intended to be used as include file only: name it .tpl then
        st=stpl.template(name
                ,template_settings={'esceape_func':lambda x:x}
                ,template_lookup = [lookup,op.split(lookup)[0]]
                ,bldpath = bldpath.abspath()
                ,options = bld.options
                ,__file__ = ps.replace('\\','/')
                ,**env
                )
        with open(pt,mode='w',encoding="utf-8",newline="\n") as f:
            f.write(st)
    class Stpl(Task.Task):
        always_run = True
        def run(self):
            render_stpl(self,self.generator.bld)
    @TaskGen.extension(_stpl)
    def expand_stpl(self,node):#expand into same folder
        nn = node.parent.make_node(node.name[:-len(_stpl)])
        self.create_task('Stpl',node,nn)
        try:
            self.get_hook(nn)(self, nn)
        except:
            pass
    def gen_ext_tsk(self,node,ext):#into _images or ../_images in source path
        srcfldr = node.parent.get_src()
        _,imgnde,__ = _pth_nde_parent(srcfldr,'_images')
        self.create_task(ext[1:].upper(),node,imgnde.make_node(node.name[:-len(ext)]+'.png'))
    @TaskGen.extension(_tikz)
    def tikz_to_png(self,node):
        gen_ext_tsk(self,node,_tikz)
    class TIKZ(Task.Task):
        def run(self):
            from sphinxcontrib import tikz
            class Builder:
                def __init__(s):
                    s.config = Namespace(**config)
                    s.imgpath,s.imgnode,s.outdir = _pth_nde_parent(tikzpth,'_images')
                    s.name = 'html'
                    try:
                        s.libs = s.config.tikz_tikzlibraries
                        s.libs = s.libs.replace(' ', '').replace('\t', '').strip(', ')
                    except AttributeError as e:
                        raise ValueError(str(e).replace('Namespace','conf.py'))
            class SphinxMock:
                def __init__(s):
                    s.builder = Builder()
                    tikz.builder_inited(s)
            tikzpth = self.inputs[0].parent.get_src()
            _,confpy,__ = _pth_nde_parent(tikzpth,'conf.py')
            config={}
            try:
                _tikzlock.acquire()
                eval(compile(confpy.read(encoding='utf-8'),confpy.abspath(),'exec'),config)
                sphinxmock = SphinxMock()
                tikzfn = tikz.render_tikz(sphinxmock,{'tikz':self.inputs[0].read(encoding='utf-8')},sphinxmock.builder.libs)
                os.replace(tikzpth.make_node(tikzfn).abspath(),self.outputs[0].abspath())
            finally:
                _tikzlock.release()
    @TaskGen.extension('.svg')
    def svg_to_png(self,node):
        gen_ext_tsk(self,node,'.svg')
    class SVG(Task.Task):
        def run(self):
            csvg2png(file=self.inputs[0].abspath(), write_to=self.outputs[0].abspath())
    @TaskGen.extension('.dot')
    def dot_to_png(self,node):
        gen_ext_tsk(self,node,'.dot')
    class DOT(Task.Task):
        run_str = "${dot} -Tpng ${SRC} -o${TGT}"
    @TaskGen.extension('.uml')
    def uml_to_png(self,node):
        gen_ext_tsk(self,node,'.uml')
    class UML(Task.Task):
        run_str = "${plantuml} ${SRC} -o${TGT[0].parent.abspath()}"
    @TaskGen.extension('.eps')
    def eps_to_png(self,node):
        gen_ext_tsk(self,node,'.eps')
    class EPS(Task.Task):
        def run(self):
            epsfile = self.inputs[0].abspath().replace('\\','/')
            epspng = self.outputs[0].abspath().replace('\\','/')

            with open(epsfile,'rb') as f:
                epscontent = f.read()

            ################## this resizes to BoundingBox, but don't know how to translate first, to avoid clipping content
            #args = ("-q -dNOPAUSE -dBATCH -dSAFER -sDEVICE=bbox %s"%epsfile).encode('utf-8').split()
            #try:
            #    _ghostscriptlock.acquire()
            #    outbbox = io.BytesIO()
            #    errbbox = io.BytesIO()
            #    with ghostscript.Ghostscript(*args,stdout=outbbox,stderr=errbbox) as gs:
            #        gs.run_string(epscontent)
            #    ghostscript.cleanup()
            #finally:
            #    _ghostscriptlock.release()
            #errbbox.seek(0)
            #outbb = errbbox.read().decode('utf-8')
            #pagesize = ''
            #try:
            #    bbx = [int(x) for x in rebbox.search(outbb).groups()]
            #    pagesize = '-g{}x{}'.format(bbx[2]-bbx[0],bbx[3]-bbx[1])
            #    #translate="-{} -{} translate\n".format(bbx[0],bbx[1]).encode('utf-8')
            #    #epscontent = translate+epscontent
            #except: pass
            #args = ("-r%s -q -dNOPAUSE -dBATCH -dSAFER -sDEVICE=png16m "%DPI+pagesize+" -sOutputFile=%s %s"%(epspng,epsfile)).encode('utf-8').split()
            ################## use _trim_png() instead

            args = ("-r%s -q -dNOPAUSE -dBATCH -dSAFER -sDEVICE=png16m -sOutputFile=%s %s"%(DPI,epspng,epsfile)).encode('utf-8').split()
            try:
                _ghostscriptlock.acquire()
                out = io.BytesIO()
                with ghostscript.Ghostscript(*args,stdout=out) as gs:
                    gs.run_string(epscontent)
                ghostscript.cleanup()
            finally:
                _ghostscriptlock.release()

            _trim_png(epspng)

    @TaskGen.extension('.pyg')
    def pyg_to_png(self,node):
        gen_ext_tsk(self,node,'.pyg')
    class PYG(Task.Task):
        def run(self):
            pygcode = self.inputs[0].read()
            pygvars={}
            eval(compile(pygcode,self.inputs[0].abspath(),'exec'),pygvars)
            if 'save_to_png' in pygvars:
                pygvars['save_to_png'](self.outputs[0].abspath())
            else:
                for k,v in pygvars.items():
                    if isinstance(v,pyx.canvas.canvas):
                        svg2png(bytestring=v._repr_svg_(),write_to=self.outputs[0].abspath(), dpi=DPI)
                        break
                    elif isinstance(v,pygal.Graph):
                        svg2png(bytestring=v.render(),write_to=self.outputs[0].abspath(), dpi=DPI)
                        break
                    elif isinstance(v,cairocffi.Surface):
                        v.write_to_png(target=self.outputs[0].abspath())
                        break
                    else: #try matplotlib.pyplot
                        try:
                            fignums = plt.get_fignums()
                            if len(fignums) == 0: 
                                continue
                            if len(fignums) > 1: 
                                makename=lambda x,i: '{0}{2}{1}'.format(*list(os.path.splitext(x))+[i])
                            else:
                                makename=lambda x,i: x
                            for i in fignums:
                                plt.figure(i).savefig(makename(self.outputs[0].abspath(),i),format='png')
                                plt.close(i)
                            break
                        except: 
                            continue
    @TaskGen.extension('.rest')
    def gen_docs(self,node):
        docs=get_docs(self.bld)
        d = get_files_in_doc(self.path,node)
        rstscan = lambda: d
        if node.name != "index.rest":
            for doctgt in docs:
                if doctgt.startswith('sphinx_'):
                    continue
                if doctgt.startswith('rst_'):
                    doctype = doctgt.split('_')[1]
                    rsttool = 'rst2'
                else:
                    rsttool = 'pandoc'
                    doctype = doctgt
                out_node = node.parent.find_or_declare("{0}/{1}.{2}".format(doctgt,node.name[:-len('.rest')],doctype))
                linksfile = node.parent.get_src().find_resource('_links_'+doctype+'.rst')
                self.create_task('NonSphinxTask', [node], out_node, scan=rstscan, rsttool='pandoc', doctype=doctype, linksfile=linksfile)
                if doctgt.endswith('html') or doctgt.endswith('latex'):
                    _images = node.parent.make_node('_images')
                    if _images.exists():
                        for x in _images.ant_glob('*'):
                            tx = _images.parent.find_or_declare(doctgt+'/_images/'+x.name)
                            self.bld(features='subst',source=x,target=tx,is_copy=True)
        else:
            for doctgt in docs:
                if not doctgt.startswith('sphinx_'):
                    continue
                out_node = node.parent.get_bld()
                sphinxoutput = out_node.find_or_declare(doctgt).abspath()
                doctype = doctgt.split('_')[1]
                self.create_task('SphinxTask',[node],out_node,cwd=node.parent.abspath(),scan=rstscan,doctype=doctype,sphinxoutput=sphinxoutput)
    class NonSphinxTask(Task.Task):
        def run(self):
            frm = self.inputs[0].abspath()
            twd = self.outputs[0].abspath()
            dr = self.inputs[0].parent.get_src()
            config = conf_py(dr.abspath())
            if self.rsttool == 'pandoc':
                cmd = ['pandoc','--standalone','-f','rst']+config.get('pandoc_opts',{}).get(self.doctype,[]
                    )+['-t','latex' if self.doctype=='pdf' else self.doctype,'-o',twd]
                opt_refdoc = config.get('pandoc_doc_optref',{}).get(self.doctype,'')
                if opt_refdoc:
                    if isinstance(opt_refdoc,dict):
                        opt_refdoc = opt_refdoc.get(inputs[0].name,'')
                    if opt_refdoc:
                        refoption,refdoc = opt_refdoc.split()
                        rd = dr.make_node(refdoc)
                        if not rd.exists(): 
                            rd = dr.parent.make_node(refdoc)
                            if not rd.exists():
                                rd = None
                        if rd:
                            cmd.append(refoption)
                            cmd.append(rd.abspath())
            elif self.rsttool == 'rst2':
                cmd = ['rst2'+self.rst2+'.py','-r3','--input-encoding=utf-8','-',twd]+ config.get(
                    'rst2_opts',{}).get(self.rst2,[])
            oldp = os.getcwd()
            os.chdir(dr.abspath())
            try:
                with open(frm,'rb') as f:
                    k1 = f.read().replace(b'\n.. include:: _links_sphinx.rst',b'')
                p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
                if 'default_role' in config:
                    p.stdin.write(b'.. default-role:: '+config['default_role'].encode('utf-8')+b'\n')
                p.stdin.write(k1)
                try:
                    with open(self.linksfile.abspath(),'rb') as f:
                        k2 = f.read()
                    p.stdin.write(k2)
                except:
                    print('_links_'+self.doctype+'.rst missing! NO CROSS REFERENCE POSSIBLE.')
                p.stdin.close()    
                p.wait()
            finally:
                os.chdir(oldp)
    class SphinxTask(Task.Task):
        always_run = True
        def run(self):
            dr = self.inputs[0].parent
            relconfpy,confpy,_ = _pth_nde_parent(dr,'conf.py')
            confdir = op.split(relconfpy)[0]
            cwd=self.get_cwd().abspath()
            subprocess.run(['sphinx-build','-Ea', '-b', self.doctype, dr.abspath(), self.sphinxoutput]+(
                ['-c',confdir] if confdir else []),cwd=cwd)

    def options(opt):
        def docscb(option, opt, value, parser):
            setattr(parser.values, option.dest, value.split(','))
        opt.add_option("--docs", type='string', action="callback", callback= docscb, dest='docs', default=[],
            help="Comma-separated list of html,docx,pdf,sphinx_html (default) or any other of http://www.sphinx-doc.org/en/master/usage/builders") 

    def configure(cfg):
        cfg.env['docs'] = cfg.options.docs
        try:
            cfg.env['plantuml'] = cfg.find_program('plantuml')
        except cfg.errors.ConfigurationError:
            cfg.to_log('plantuml was not found (ignoring)')
        try:
            cfg.env['dot'] = cfg.find_program('dot')
        except cfg.errors.ConfigurationError:
            cfg.to_log('dot was not found (ignoring)')

    def build(bld):
        bld.src2bld = lambda f: bld(features='subst',source=f,target=f,is_copy=True)
        def gen_files():
            bld(name="process gen file",features="gen_files")
        bld.gen_files = gen_files
        def gen_links():
            bld(name="create links and .tags",features="gen_links")
        bld.gen_links = gen_links
        bld.stpl = lambda tsk: render_stpl(tsk,bld) #use like bld(rule=bld.stpl,source='x.h.stpl') to compile stpl only, else do without rule
        def build_docs():
            docs=get_docs(bld)
            if docs:
                bld.gen_files()
                bld.gen_links()
                for anext in '*.tikz *.svg *.dot *.uml *.pyg *.eps'.split():
                    for anextf in _ant_glob_stpl(bld.path,anext):
                        bld(name='build '+anext,source=anextf)
                bld.add_group()
                bld(name='build all rest',source=[x for x in _ant_glob_stpl(bld.path,'*.rest','*.rst')if not x.name.endswith('.rst')])
                bld.add_group()
        bld.build_docs = build_docs

except:
    pass

#==============< for building with WAF

#this is for mktree(): first line of file content must not be empty!
example_tree = r'''
       build/
       src
        ├ dcx.py << file:///__file__
        ├ reference.tex << file:///__tex_ref__
        ├ wafw.py << file:///__wafw__
        ├ waf
            #!/usr/bin/env sh
            shift
            ./wafw.py "$@"
        ├ waf.bat
            @setlocal
            @set PYEXE=python
            @where %PYEXE% 1>NUL 2>NUL
            @if %ERRORLEVEL% neq 0 set PYEXE=py
            @%PYEXE% -x "%~dp0wafw.py" %*
            @exit /b %ERRORLEVEL%
        ├ wscript
            from waflib import Logs
            Logs.colors_lst['BLUE']='\x1b[01;36m'
            
            top='.'
            out='../build'
            
            def options(opt):
              opt.load('dcx',tooldir='.')
            
            def configure(cfg):
              cfg.load('dcx',tooldir='.')
            
            def build(bld):
              #defines bld.gen_files(), bld.gen_links(), bld.build_docs()
              bld.load('dcx',tooldir='.')
              bld.recurse('doc')
        ├ docutils.conf
            [general]
            halt_level: severe
            report_level: error
        ├ conf.py
            extensions = ['sphinx.ext.autodoc',
                'sphinx.ext.todo',
                'sphinx.ext.mathjax',
                'sphinx.ext.viewcode',
                'sphinx.ext.graphviz',
                ]
            numfig = False
            smartquotes = False
            default_role = 'math'
            templates_path = ['_templates']
            source_suffix = '.rest'
            master_doc = 'index'
            project = 'sample'
            author = project+' Project Team'
            copyright = '2018, '+author
            version = '1.0'
            release = '1.0.0'
            language = None
            highlight_language = "none"
            exclude_patterns = []
            pygments_style = 'sphinx'
            todo_include_todos = True
            import sphinx_bootstrap_theme
            html_theme = 'bootstrap'
            html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
            latex_engine = 'xelatex'
            tikz_transparent = True
            tikz_proc_suite = 'ImageMagick'
            tikz_tikzlibraries = 'arrows,snakes,backgrounds,patterns,matrix,shapes,fit,calc,shadows,plotmarks,intersections'
            tikz_latex_preamble = r"""
            \usepackage{unicode-math}
            \usepackage{tikz}
            \usepackage{caption}
            \captionsetup[figure]{labelformat=empty}
            """
            latex_elements = {
            'preamble':tikz_latex_preamble+r"\usetikzlibrary{""" + tikz_tikzlibraries+ '}'
            }
            latex_documents = [
                (master_doc, project.replace(' ','')+'.tex',project+' Documentation',author,'manual'),
            ]
            #new in rstdoc
            target_id_group = lambda targetid: targetid[0]
            target_id_color={"ra":("r","lightblue"), "sr":("s","red"), "dd":("d","yellow"), "tp":("t","green")}
            html_extra_path=["doc/_images/_trace.svg"]
            pandoc_doc_optref={'latex': '--template reference.tex',
                             'html': {},#each can also be dict of file:template
                             'pdf': '--template reference.tex',
                             'docx': '--reference-doc reference.docx',
                             'odt': '--reference-doc reference.odt'
                             }
            latex_pdf = ['--listings','--number-sections','--pdf-engine','xelatex','-V','titlepage','-V','papersize=a4','-V','toc','-V','toc-depth=3','-V','geometry:margin=2.5cm']
            pandoc_opts = {'pdf':latex_pdf,'latex':latex_pdf,'docx':[],'odt':[],'html':['--mathml','--highlight-style','pygments']}
            rst2_opts = {'odt':['--leave-comments'],'html':['--leave-comments']}#see ``rst2html.py --help`` or ``rst2odt.py --help``
        ├ Makefile
            SPHINXOPTS    = -c .
            SPHINXBUILD   = sphinx-build
            SPHINXPROJ    = sample
            SOURCEDIR     = ./doc#./ needed due to the follwing subst
            BUILDDIR      = ../build/doc
            SOURCEFILES   = $(filter-out $(SOURCEDIR)/index.rest,$(wildcard $(SOURCEDIR)/*.rest))
            DOCXFILES     = $(subst $(SOURCEDIR),$(BUILDDIR)/docx,$(SOURCEFILES:%.rest=%.docx))
            PDFFILES      = $(subst $(SOURCEDIR),$(BUILDDIR)/pdf,$(SOURCEFILES:%.rest=%.pdf))
            .PHONY: docx help Makefile docxdir pdfdir index
            docxdir: ${BUILDDIR}/docx
            pdfdir: ${BUILDDIR}/pdf
            MKDIR_P = mkdir -p
            ${BUILDDIR}/docx:
            	@${MKDIR_P} ${BUILDDIR}/docx
            ${BUILDDIR}/pdf:
            	@${MKDIR_P} ${BUILDDIR}/pdf
            index:
            	@python $(SOURCEDIR)/../dcx.py
            help:
            	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
            	@echo "  docx        to docx"
            	@echo "  pdf         to pdf"
            #http://www.sphinx-doc.org/en/stable/usage/builders/
            html dirhtml singlehtml htmlhelp qthelp applehelp devhelp epub latex text man texinfo pickle json xml pseudoxml: Makefile index
            	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
            docx:  docxdir index $(DOCXFILES)
            # in the following the ../ needs to be repeated for every dir in SOURCEDIR
            $(BUILDDIR)/docx/%.docx:$(SOURCEDIR)/%.rest
            	@cd $(SOURCEDIR) && echo .. default-role:: math | cat - "$(<:$(subst ./,,$(SOURCEDIR))/%=%)" _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx --reference-doc ../reference.docx -o ../"$@"
            pdf: pdfdir index $(PDFFILES)
            $(BUILDDIR)/pdf/%.pdf:$(SOURCEDIR)/%.rest
            	@cd $(SOURCEDIR) && echo .. default-role:: math | cat - "$(<:$(subst ./,,$(SOURCEDIR))/%=%)" _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm --template ../reference.tex -o ../"$@"
        ├ code
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
        └ doc
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
               
               .. include:: _trace.rst
               
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
               
               ``dcx.py`` produces its own labeling consistent across DOCX, PDF, HTML.
               
               .. _`sy7`:
               
               A Requirement Group
               -------------------
               
               .. _`s3a`:
               
               :s3a: brief description
               
               Don't count the ID, since the order will change.
               The IDs have the first letter of the file and 2 or more random letters of ``[0-9a-z]``.
               Use an editor macro to generate IDs.
               
               If one prefers ordered IDs, one can use templates::
               
                 %id = lambda x=[0]: x.append(x[-1]+1) or "s{:0>2}".format(x[-1])
               
                 .. _`soi`:
               
                 :{{id()}}: auto numbered.
               
               The disadvantage is that the id will differ between rst and final doc.
               When this is needed in an included file use template include: ``%include('x.rst.tpl`)``
               See the the ``test/stpl`` folder.
               
               Every ``.rest`` has this line at the end::
               
                  .. include:: _links_sphinx.rst
               
               .. include:: _links_sphinx.rst
               
           ├ dd.rest
               Design Description
               ==================
               
               .. _`d97`:
               
               :d97: Independent DD IDs
               
                 The relation with RS IDs is m-n. Links like |s3a| can be scattered over more DD entries.  
               
               .. _`dx3`:
               
               .. figure:: _images/exampletikz1.png
                  :name:
                  :width: 30%
               
                  |dx3|: Create from exampletikz1.tikz
               
               .. _`dz3`:
               
               .. figure:: _images/exampletikz.png
                  :name:
                  :width: 50%
               
                  |dz3|: Create from exampletikz.tikz
               
                  The usage of ``:name:`` produces: ``WARNING: Duplicate explicit target name: ""``. Ignore.
               
               Reference via |dz3|.
               
               ``.tikz``, ``.svg``, ``.dot``,  ``.uml``, ``.eps`` or ``.stpl`` thereof and ``.pyg``, are converted to ``.png``.
               
               .. _`dz4`:
               
               .. figure:: _images/examplesvg.png
                  :name:
               
                  |dz4|: Created from examplesvg.svg.stpl
               
               .. _`dz5`:
               
               .. figure:: _images/exampledot.png
                  :name:
               
                  |dz5|: Created from exampledot.dot.stpl
               
               .. _`dz6`:
               
               .. figure:: _images/exampleuml.png
                  :name:
               
                  |dz6|: Created from exampleuml.uml
               
               .. _`dz7`:
               
               .. figure:: _images/exampleplt.png
                  :name:
                  :width: 30%
               
                  |dz7|: Created from exampleplt.pyg
               
               .. _`dz8`:
               
               .. figure:: _images/examplepyx.png
                  :name:
               
                  |dz8|: Created from examplepyx.pyg
               
               .. _`dr8`:
               
               .. figure:: _images/examplecairo.png
                  :name:
               
                  |dr8|: Created from examplecairo.pyg
               
               .. _`ds8`:
               
               .. figure:: _images/examplepygal.png
                  :name:
                  :width: 30%
               
                  |ds8|: Created from examplepygal.pyg
               
               .. _`dsx`:
               
               .. figure:: _images/exampleother.png
                  :name:
               
                  |dsx|: Created from exampleother.pyg
               
               .. _`du8`:
               
               .. figure:: _images/exampleeps1.png
                  :name:
               
                  |du8|: Created from exampleeps1.eps
               
               .. _`d98`:
               
               .. figure:: _images/exampleeps.png
                  :name:
               
                  |d98|: Created from exampleeps.eps
               
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
               
               Here instead of ``d99:`` we use ``:OtherName:``, but now we have two synonyms for the same item.
               This is no good. If possible, keep ``d99`` in the source and in the final docs.
               
               The item target must be in the same file as the item content. The following would not work::
               
                 .. _`dh5`:
                 
                 .. include:: somefile.rst   
               
               .. |eps1| image:: _images/exampleeps1.png
               .. |eps| image:: _images/exampleeps.png
               
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
               
               Or better: reference the according SR chapter, else changes there would need an update here.
               
               - Test |sy7|
               
               Unit Tests
               ----------
               
               Use ``.rst`` for included files and start the file with ``_`` if generated.
               
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
               
           ├ exampletikz.tikz
               [thick,red]
               \draw (0,0) grid (3,3);
               \foreach \c in {(0,0), (1,0), (2,0), (2,1), (1,2)}
                   \fill \c + (0.5,0.5) circle (0.42);
           ├ exampletikz1.tikz
               \begin{scope}[blend group = soft light]
               \fill[red!30!white]   ( 90:1.2) circle (2);
               \fill[green!30!white] (210:1.2) circle (2);
               \fill[blue!30!white]  (330:1.2) circle (2);
               \end{scope}
               \node at ( 90:2)    {Typography};
               \node at ( 210:2)   {Design};
               \node at ( 330:2)   {Coding};
               \node [font=\Large] {\LaTeX};
           ├ examplesvg.svg.stpl
               <?xml version="1.0" encoding="utf-8"?>
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" version="1.1" width="110pt" height="60pt" stroke-width="0.566929" stroke-miterlimit="10.000000">
               %for i in range(10):
                 <path fill="none" stroke="#f00" stroke-width="1" d="M10,55 C15,5 100,5 100,{{i*5}}" />
               %end
               %for i in range(10):
                 <path fill="none" stroke="#f40" stroke-width="1" d="M10,{{i*5}} C15,5 100,5 100,55" />
               %end
               <text x="50" y="50" fill="red">Hi!</text>
               </svg>
           ├ exampledot.dot.stpl
               digraph {
               %for i in range(3):    
                   "From {{i}}" -> "To {{i}}";
               %end
                   }
           ├ exampleuml.uml
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
           ├ exampleplt.pyg
               #vim: syntax=python
               import matplotlib.pyplot as plt
               import numpy as np
               x = np.random.randn(1000)
               plt.hist( x, 20)
               plt.grid()
               plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
               plt.show()
           ├ examplepyx.pyg
               import pyx
               c = pyx.canvas.canvas()
               c.stroke(pyx.path.circle(0,0,2),[pyx.style.linewidth.Thick,pyx.color.rgb.red])
               c.text(1, 1, 'Hi',[pyx.color.rgb.red])
           ├ examplepygal.pyg
               import pygal
               diagram=pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4)
           ├ exampleother.pyg
               from PIL import Image, ImageDraw, ImageFont
               im = Image.new("RGBA",size=(50,50),color=(155,0,100))
               draw = ImageDraw.Draw(im)
               draw.rectangle(((0, 0), (40, 40)), fill="red")
               draw.text((20, 20), "123")
               save_to_png = lambda out_file: im.save(out_file, "PNG")
           ├ exampleeps.eps
               1 0 0 setrgbcolor
               newpath 6 2 36 54 rectstroke
               showpage
           ├ exampleeps1.eps
               0 0 1 setrgbcolor
               newpath 6 2 36 54 rectstroke
               showpage
           ├ examplecairo.pyg
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
               ../code/some.h | _sometst.rst                | tstdoc | {}
               ../code/some.h | ../../build/code/some_tst.c | tst    | {}'''

#replaces from '├ index.rest' to '├ exampletikz.tikz'
_example_stpl = r'''
           ├ model.py
               """
               This contains definitions used in template files ending in ``.stpl``.
               """
               from pint import UnitRegistry
               u = UnitRegistry()
               u.define('percent = 0.01*count = %')
               def U(*k,sep=", "):
                   """
                   Returns string where pint quantities are formatted with units, if possible, else normally.
                   """
                   try:
                       return sep.join(["{:~P}"]*len(k)).format(*k)
                   except:
                       res = sep.join(["{}"]*len(k)).format(*k)
                       if res == 'None':
                           res = '-'
                       return res
               # Definitions
               max_charging_time = 3.5*u.hour #in |hw_charger|
           ├ utility.rst.tpl
               % import sys, os
               % sys.path.append(os.path.dirname(__file__))
               % from model import *
               % cntr = lambda alist0,prefix='',width=2: alist0.append(alist0[-1]+1) or ("{}{:0>%s}"%width).format(prefix,alist0[-1])
               % II=lambda prefix,alist0,short:':{}: **{}**'.format(cntr(alist0,prefix),short)
               % #define in file e.g. ``SR=lambda short,alist0=[0]:II('SR',alist0,short)`` and use like ``{{SR('Item Title')}}``
               % from rstdoc.retable import title_some as title_order
               % def HH(title,newlevel=None,markers=title_order,level=[0]):#works only at beginning of line
               %    if newlevel is not None:
               %      level[0] = newlevel
               %    end
               %    m = markers[level[0]]
               {{title}}
               {{m*len(title)}}
               % end
               % #use like ``{{HH('title here')}}`` or ``{{HH('subtitle',level+1)}}`` or ``{{HH('title',0)}}``, or better write manually
               % def pagebreak():
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
               % end
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
               
               .. include:: _trace.rst
               
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
               
                 We use `restructuredText <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
                 together with `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax>`_.
               
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
               
               .. _`sr_a_requirement_group`:
               
               A Requirement Group
               ===================
               
               .. _`sr_id`:
               
               {{SR('ID')}}
               
                 The ID seen in the final document is numbered by a python function.
                 In the restructuredText files there is no numbering.
                 The targets use key words instead.
                 This way one can rearrange the items keeping the items sorted and still referentially consistent.
                 
                 The ID shall not contain any hyphens or dots or other non-identifier characters,
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
               
                 ``dcx.py`` associates all links between two targets to the first target.
                 This can be used as traceability.
               
                 Warnings issued during conversion to final documents help to keep the documents consistent.  
               
               .. _`dd_name`:
               
               {{DD('Name')}}
               
                 For targeted ``.. table::``, ``.. list-table::``, ``.. figure::``, ``.. code-block::`` and ``.. math::`` use ``:name:``.
                 In the legend use the same ID as in the target definition.
               
                 .. _`dd_figure`:
               
                 .. figure:: _images/exampletikz.png
                    :name:
                    :width: 50%
               
                    |dd_figure|: Caption here.
                    Reference this via ``|dd_figure|``.
               
                 .. _`dd_code`:
               
                 |dd_code|: Listing showing struct.
               
                 .. code-block:: cpp
                    :name:
               
                    struct xxx{
                       int yyy; //yyy for zzz
                    }
               
                 .. include normal .rst
                 .. include:: dd_tables.rst
               
                 .. include rst that was generated from .rst.stpl
                 .. include:: dd_math.rst
               
               .. include the stpl way
               %include('dd_diagrams.tpl',DD=DD)#you need to provide python definitions
               
               .. include:: _links_sphinx.rst
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
               
               Reference |dd_table| or |dd_list_table| does not show ``dd_table`` or ``dd_list_table``.
               
               .. |eps1| image:: _images/exampleeps1.png
               .. |eps| image:: _images/exampleeps.png
               
           ├ dd_math.rst.stpl
               .. encoding: utf-8
               .. vim: syntax=rst
               
               .. _`dd_math`:
               
               .. math:: 
                  :name:
               
                  V = \frac{K}{r^2}
               
               ``:math:`` is the default inline role: `mc^2`
               
               With `sympy <www.sympy.org>`_ one can have formulas in ``some.py`` that are usable for calculation.
               The formulas can be converted to latex in the ``.stpl`` or ``.tpl`` file.
               
               %def hyp(a,b):
               %    return a**2+b**2
               %end
               
               The long side of a rectangular triangle with legs {{3}} and {{4}} is {{hyp(3,4)**0.5}}. See |hyp|.
               
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
                 
                 .. figure:: _images/exampletikz1.png
                    :name:
                    :width: 30%
                 
                    |exampletikz1|: Create from exampletikz1.tikz
                 
                    The usage of ``:name:`` produces: ``WARNING: Duplicate explicit target name: ""``. Ignore.
                 
                 Reference via |exampletikz1|.
                 
                 ``.tikz``, ``.svg``, ``.dot``,  ``.uml``, ``.eps`` or ``.stpl`` thereof and ``.pyg``, are converted to ``.png``.
                 
                 .. _`examplesvg`:
                 
                 .. figure:: _images/examplesvg.png
                    :name:
                 
                    |examplesvg|: Created from examplesvg.svg.stpl
                 
                 .. _`exampledot`:
                 
                 .. figure:: _images/exampledot.png
                    :name:
                 
                    |exampledot|: Created from exampledot.dot.stpl
                 
                 .. _`exampleuml`:
                 
                 .. figure:: _images/exampleuml.png
                    :name:
                 
                    |exampleuml|: Created from exampleuml.uml
                 
                 .. _`exampleplt`:
                 
                 .. figure:: _images/exampleplt.png
                    :name:
                    :width: 30%
                 
                    |exampleplt|: Created from exampleplt.pyg
                 
                 .. _`examplepyx`:
                 
                 .. figure:: _images/examplepyx.png
                    :name:
                 
                    |examplepyx|: Created from examplepyx.pyg
                 
                 .. _`examplecairo`:
                 
                 .. figure:: _images/examplecairo.png
                    :name:
                 
                    |examplecairo|: Created from examplecairo.pyg
                 
                 .. _`examplepygal`:
                 
                 .. figure:: _images/examplepygal.png
                    :name:
                    :width: 30%
                 
                    |examplepygal|: Created from examplepygal.pyg
                 
                 .. _`exampleother`:
                 
                 .. figure:: _images/exampleother.png
                    :name:
                 
                    |exampleother|: Created from exampleother.pyg
                 
                 .. _`exampleeps1`:
                 
                 .. figure:: _images/exampleeps1.png
                    :name:
                 
                    |exampleeps1|: Created from exampleeps1.eps
                 
                 .. _`exampleeps`:
                 
                 .. figure:: _images/exampleeps.png
                    :name:
                 
                    |exampleeps|: Created from exampleeps.eps

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
               
                 Since items in other documents are phrased as tests, there is no need to repeat the text here.
               
                 - |sr_id|
               
                 Or better: Reference the according chapter:
               
                 - Test |sr_a_requirement_group|
               
               .. _`tp_unit_tests`:
               
               Unit Tests
               ==========
               
               .. _`tp_gen_file`:
               
               {{TP('gen file')}}
               
                 Use ``.rst`` for included files and start the file with ``_`` if generated.
                 How test documentation files are generated from test source code can be specified in the ``gen`` file.
               
               .. include:: _links_sphinx.rst
               '''

def main(**args):
  '''
  This corresponds to the |rstdcx| shell command.
  '''

  import codecs
  import argparse

  if not args:
    parser = argparse.ArgumentParser(description='''Sample RST Documentation for HTML and DOCX.
      Creates |substitution| links and ctags for link targets.
      ''')
    parser.add_argument('--init', dest='initroot', action='store',
                        help='Create a sample folder structure.')
    parser.add_argument('--stpl', dest='stplroot', action='store',
                        help='Create a stpl templated sample folder structure.')
    parser.add_argument('-v','--verbose', action='store_true',
                        help='''Show files recursively included by each rest''')
    parser.add_argument('infile', nargs='?',
            help='Input file or - for stdin. If not given all directories below are scanned.')
    parser.add_argument('outfile', nargs='?',
            help='Output file or - or nothing to print to std out.')
    parser.add_argument('outtype', nargs='?',default='html',
            help='Extension with starting dot (default: html). The target file name will be the in-file with this extension.')
    args = parser.parse_args().__dict__


  filelines = None
  try:
    filename = infile = args['infile']

    isfile = infile and os.path.isfile(infile) or False
    if not isfile and infile == '-':
        try:
            sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach()) 
        except: pass
        filelines = sys.stdin.readlines()
    elif isfile:
        file = filename.replace('\\','/')
        with open(file,'r',encoding='utf-8') as f:
            filelines = f.readlines()
  except: pass

  initroot = args['initroot']
  stplroot = args['stplroot']
  global verbose
  verbose = args['verbose']
  if initroot is not None or stplroot is not None:
    thisfile = str(Path(__file__).resolve()).replace('\\','/')
    tex_ref = opnj(op.split(thisfile)[0],'..','reference.tex')
    wafw = opnj(op.split(thisfile)[0],'..','wafw.py')
    inittree=[l for l in example_tree.replace(
        '__file__',thisfile).replace(
        '__tex_ref__',tex_ref).replace(
        '__wafw__',wafw).splitlines()]
    if initroot is None:
        _replace_lines = lambda origlns,start,stop,insertlns: origlns[
            :list(rindices(start,origlns))[0]]+insertlns+origlns[list(rindices(stop,origlns))[0]:]
        inittree = _replace_lines(inittree,'├ index.rest','├ exampletikz.tikz',_example_stpl.splitlines())
    doroot = lambda x: initroot and x(initroot) or stplroot and x(stplroot)
    doroot(mkdir)
    oldd = os.getcwd()
    try:
        doroot(os.chdir)
        mktree(inittree)
        os.chdir('src')
        subprocess.run("pandoc --print-default-data-file reference.docx > reference.docx",shell=True)
    finally:
        os.chdir(oldd)
  elif filelines:
    outfile = args['outfile']
    outtype = args['outtype']
    outf = None
    try:
        if outfile is None or outfile=='-':
            try:
                sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
            except: pass
            outf = sys.stdout
            #filename,outfile,outtype='example.txt','example.rst','html' #example.html
            #filename,outfile,outtype='-','-','example.html' #-.html
            #filename,outfile,outtype='-','-','html' #example.html
            if filename == '-':
                try:
                    filename,outtype = outtype.split('.')
                except: pass
            outfile = os.path.splitext(filename)[0]+'.'+outtype 
        else:
            outf  = open(outfile,'w',encoding='utf-8')
        filenoext=os.path.splitext(outfile)[0]
        outf.write(''.join(filelines))
        outf.write('\n')
        for (i,fi),tgt,lnkname in make_tgts(filelines,filename):
            outf.write(create_link(outtype,filenoext,tgt,lnkname))
    finally:
        if outf is not None and outf != sys.stdout:
            outf.close()
  else:
    #link, gen and tags per folder
    for fldr, (lnktgts,allfiles,alltgts,substitutions) in fldrs('.'):
        if verbose:
            print(fldr)
        #generate files
        genpth = opnj(fldr,'gen')
        if op.exists(genpth):
            for f,t,d,kw in parsegenfile(genpth):
                gen(opnj(fldr,f),target=opnj(fldr,t),fun=d,**kw)
        links_and_tags(fldr,lnktgts,allfiles,alltgts,substitutions)

if __name__=='__main__':
  main()

