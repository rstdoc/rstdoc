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
from restructuredText (RST). 

- For HTML ``Sphinx`` is used.
- For PDF ``Pandoc`` is used (``Sphinx`` would work, too).
- For DOCX ``Pandoc`` is used, therefore *no Sphinx extension*.

``rstdcx``, or ``dcx.py`` 

- processes ``gen`` files (see examples produced by --init)

- creates .tags  _links_pdf.rst _links_docx.rst _links_sphinx.rst

See example at the end of ``dcx.py``.

Usage
-----

With ``rstdoc`` installed, ``./dcx.py`` in the following examples can be replaced by ``rstdcx``.

- Initialize example tree::

  $ ./dcx.py --init tmp

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

- Create the docs (and .tags and _links_xxx.rst) with **waf** (preferred):

  Instead of using ``make`` one can load ``dcx.py`` in `waf <https://github.com/waf-project/waf>`__.
  ``waf`` also considers all recursively included files,
  such that a change in any of them results in a rebuild of the documentation. 
  All files can have an additional ``.stpl`` extension to use `SimpleTemplate <https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax>`__.

    $ waf configure
    $ waf --docs docx,sphinx_html

  Images are placed into ``./_images`` or ``../_images``.
  The following image languages should be parallel to the ``.rest`` files and are automatically converted to ``.png`` and and placed into ``images``.

  - ``.tikz`` or ``.tikz.stpl``. 
    This needs LaTex and `sphinxcontrib-tikz <https://bitbucket.org/philexander/tikz>`__ and is rather slow.

  - `.svg <http://svgpocketguide.com/book/>`__ or ``.svg.stpl``

  - `.dot <https://graphviz.gitlab.io/gallery/>`__ or ``.dot.stpl``

  - `.uml <http://plantuml.com/command-line>`__ or ``.uml.stpl``
    This needs a plantuml.bat with e.g. ``java -jar %~dp0plantuml.jar %*`` 
    or plantuml sh script with ``java -jar `dirname $BASH_SOURCE`/plantuml.jar "$@"``.

  - `.plt` should contain python matplotlib code with one ``show()`` line

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

- ``.. _`id`:`` are targets.
  *RST targets* must not be template-generated. The templates can have more targets than the generated file.
  If one wants to generate also rst targets, then this must happen in a previous step, e.g. with ``gen``.

- References use replacement `substitutions`_: ``|id|``.
  
See the example created with ``--init`` at the end of this file and the sources of the documentation of 
`rstdoc <https://github.com/rpuntaie/rstdoc>`__.

.. _`substitutions`: http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text

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
from pathlib import Path
from urllib import request
from functools import lru_cache
from collections import OrderedDict,defaultdict
from itertools import chain, tee
from types import GeneratorType
from argparse import Namespace

try:
    from cairosvg import svg2png
    def csvg2png(file,write_to):
        try:
            svg2png(url="file:///"+file, write_to=write_to)
        except:
            svg2png(url="file://"+file, write_to=write_to)
except Exception as e:
    print('cairosvg svg2png not available:',e)
    def csvg2png(file,write_to): pass

try:
    import pyfca
except Exception as e:
    print('pyfca not available:',e)
    pyfca = None

Tee = tee([], 1)[0].__class__
def memoized(f):
    cache={}
    def ret(*args):
        if args not in cache:
            cache[args]=f(*args)
        if isinstance(cache[args], (GeneratorType, Tee)):
            cache[args], r = tee(cache[args])
            return r
        return cache[args]
    return ret

verbose = False
_stpl = '.stpl'
_tpl = '.tpl'
_tikz = '.tikz'
is_rest = lambda x: x.endswith('.rest') or x.endswith('.rest'+_stpl)
is_rst = lambda x: x.endswith('.rst') or x.endswith('.rst'+_stpl) or x.endswith('.rst.tpl')

rextgt = re.compile(r'(?:^|^[^\.\%\w]*\s|^\s*\(?\w+[\)\.]\s)\.\. _`?(\w[^:`]*)`?:\s*$')
rextitle = re.compile(r'^([!"#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~])\1+$')
rexitem = re.compile(r'^\s*:?(\w[^:]*):\s*.*$')
rexoneword = re.compile(r'^\s*(\w+)\s*$')
rexname = re.compile(r'^\s*:name:\s*(\w.*)*$')
rexlinksto = re.compile(r'[^`]?\|(\w+)\|[^`]?')
reximg = re.compile(r'image:: ((?:\.|/|\\|\w).*)')
#list(rexlinksto.findall('|xx| A |lnk| here |gos|'))
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
#rexitem.match(':``t11``:').group(1)#nok
#rexitem.match(':t11:').group(1)#ok
#reximg.search('.. image:: ..\img.png').group(1)
#reximg.search(r'.. |c:\x y\im.jpg| image:: /tmp/img.png').group(1)
#reximg.search(r'.. image:: c:\tmp\img.png').group(1)
#reximg.search(r'.. image:: \\public\img.png').group(1)
rerstinclude = re.compile(r'\.\. include::\s*([\./\w\\].*)')
restplinclude = re.compile(r'''%\s*include\s*\(\s*["']([^'"]+)['"].*\)\s*''')
#rerstinclude.split('.. include:: test.rst')
#rerstinclude.split('.. include:: ../test.rst')
#rerstinclude.split('  .. include:: ../test.rst')
#restplinclude.split('%include("test.rst.stpl",v="aparam")')
#restplinclude.split('%include("../test.rst.stpl",v="aparam")')
#restplinclude.split('% include(  "../test.rst.stpl",v="aparam")')


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


def conf_py(fldr):
    """
    conf.py or ../conf.py is used for both sphinx and pandoc.
    """
    confpy = opnj(fldr,'conf.py')
    if not op.exists(confpy):
        confpy = updir(confpy)
    config={}
    with open(confpy,encoding='utf-8') as f:
        eval(compile(f.read(),op.abspath(confpy),'exec'),config)
    return config


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

      >>> list(doc_parts(open(__file__).readlines(),signature='py'))

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
            yield
            yield '.. _`'+prefix+thisprefix+ids[0]+'`:\n'
            yield
            yield ':'+prefix+thisprefix+ids[0]+':\n'
            yield
        if signature:
            if i is not None and i < a and i > 0:
                if not lns[i].strip():#empty
                    i = i+1
                if i < a:
                    yield '.. code-block:: '+signature+'\n'
                    yield
                    yield from ('   '+x for x in lns[i:a])
                    yield
            if j is not None and j > b+1 and j < len(lns):
                if not lns[j].strip():#empty
                    j = j-1
                if j > b:
                    yield '.. code-block:: '+signature+'\n'
                    yield
                    yield from ('   '+x for x in lns[b+1:j+1])
                    yield
        indent = 0
        for ln in lns[a+1:b]:
            lnst = rindent.search(ln)
            if lnst and lnst.span():
                indent = lnst.span()[0]
                break;
        yield from (x[indent:] for x in lns[a+1:b])

@lru_cache()
def _read_lines(fn):
    lns = []
    with open(fn,'r',encoding='utf-8') as f:
        lns = f.readlines()
    return lns

def _read_stpl_lines_it(fn):
    """
    This flattens the .stpl includes to have all targets align to those in the .rest file.
    Targets must not be *explicit* in all .stpl. They must not be created by stpl.
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
        m = restplinclude.match(ln)
        if m: 
            yield from _read_stpl_lines(op.join(op.dirname(fn),m.group(1)))
        else:
            yield fn,i,ln

@lru_cache()
def _read_stpl_lines(fn):
    return list(_read_stpl_lines_it(fn))

@memoized
def rstincluded(
    fn #file name without path
    ,paths=() #paths where to look for fn
    ,withimg=False #also yield image files, not just other rst files
    ):
    '''
    Yield the files recursively included from an RST file.
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
            elif e.startswith('.. '):
                #e = '.. include:: some.rst'
                #e = '.. include:: ../some.rst'
                #e = '.. image:: some.png'
                #e = '.. figure:: some.png'
                #e = '.. |x y| image:: some.png'
                try:
                    f,t,_ = rerstinclude.split(e)
                    nf = not f and t
                    if nf and not nf.startswith('_links_'):
                        yield from rstincluded(nf.strip(),paths)
                except:
                    if withimg:
                        m = reximg.search(e)
                        if m:
                            yield m.group(1)
            elif restplinclude.match(e): 
                #e="%include('some.rst.tpl',v='param')"
                f,t,_=restplinclude.split(e)
                nf = not f and t
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
        mo = rexlinksto.findall(ln)
        for g in mo:
            yield i,g

def pair(a,b,cmp):
    """ pair two sorted lists
    b must be longer than a
    >>> a=[1,2,4,7]
    ... b=[1,2,3,4,5,6,7]
    ... cmp = lambda x,y: x==y
    ... list(pair(a,b,cmp))
    [(1, 1), (2, 2), (None, 3), (4, 4), (None, 5), (None, 6), (7, 7)]
    """
    i = 0
    for i,(aa,bb) in enumerate(zip(a,b)):
        if not cmp(aa,bb):
            break
        yield aa,bb
    alen = len(a)
    tlen = max(alen,len(b))
    d = 0
    for j in range(i,alen):
        for dd in range(tlen-j-d):
            bb = b[j+d+dd]
            if not cmp(a[j],bb):
                yield None,bb
            else:
                yield a[j],bb
                d = d+dd
                break
        else:
            return

class RstDocError(Exception):
    pass

g_counters=defaultdict(dict)

def make_tgts(
    lns  #lines of the document
    ,doc #doc .rest file name
    ,fil=None #stpl lines
    ):
    '''
    Yields line index, target and link name of ``lns`` of a RST file (lns)
    and zip to flattened stpl for .tags.
    '''

    docprefix = ' '
    if doc not in g_counters:
        g_counters[doc] = {".. figure":1,".. math":1,".. table":1,".. code":1} #=list-table,code-block
    counters=g_counters[doc]
    itgts = list(rindices(rextgt,lns))
    if fil:
        lns1 = [x[2] for x in fil]
        itgts1 = list(rindices(rextgt,lns1))
    else:
        lns1 = lns
        itgts1 = itgts
    if len(itgts)<len(itgts1):
        paired_itgts_itgts1 = pair(itgts,itgts1,lambda x,y:lns[x]==lns1[y])
    elif len(itgts)>len(itgts1):
        raise RstDocError(".rest has more targets (.. _`xx`:) than .stpl. Either not up-to-date (run 'stpl {0}' first) or targets generated (don't).".format(doc))
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
        yield (i,fil[i1][:2] if fil else (doc,ii)), tgt, lnkname

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
                    ct = re.search(r'[^\s│]',t0[0]).span()[0]
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
        dcns=set([])
        for dcs in fldrincluded('.'): 
            rest = next(adc for adc in dcs if is_rest(adc))
            restpath,restext = op.splitext(rest)
            fldr,restname = op.split(restpath)
            fldr_allfiles[fldr] |= set(dcs)
            if restext == _stpl:
                reststpl = True
                restname=op.splitext(restname)[0]
            else:
                reststpl = False
            dcns.add(restname)
            for doc in dcs:
                if doc==rest and reststpl and op.exists(restpath):
                    lns = _read_lines(restpath)
                    fil = _read_stpl_lines(doc)
                    tgts = list(make_tgts(lns,doc,fil))
                elif not doc.endswith('.tpl') and not doc.endswith('.txt') and op.exists(doc):
                    #.txt are considered literal include
                    #%include('x.rst.tpl') were considered in first branch
                    lns = _read_lines(doc)
                    tgts = list(make_tgts(lns,doc))
                else:
                    continue
                lnks = list(make_lnks(lns))
                if fldr not in fldr_lnktgts:
                    fldr_lnktgts[fldr] = []
                fldr_lnktgts[fldr].append((restname,doc,len(lns),lnks,tgts))
                fldr_alltgts[fldr] |= set([n for ni,n,nn in tgts])
        for fldr,lnktgts in fldr_lnktgts.items():
            allfiles = fldr_allfiles[fldr]
            alltgts = fldr_alltgts[fldr]
            yield fldr, (lnktgts,allfiles,alltgts)
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
    ,lnktgts  #list of links and targets in a document (restname, doc, lenlns, lnks, tgts)
    ,allfiles #all files in one folder
    ,alltgts  #all targets of the whole folder
    ):
    '''
    Creates links_xxx.rst and .tags files for a folder ``fldr`` in that folder.

    If ``pyfca`` is available also the dependencies file ``_trace.rst`` is created.

    conf.py entries::

      file_id_color={
          "meta":("m","white"),
          "ra":("r","lightblue"),
          "sr":("s","red"),
          "dd":("d","yellow"), 
          "tp":("t","green"),
          "rstdoc":("o","pink")}
      html_extra_path=["_images/_trace.svg"]

    IDs starting with the letter in file_id_color are assumed to be from that file.
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
            file_id_color=config['file_id_color']
            def _drawnode(canvas,node,parent,c,r): 
                od = []
                its = {x[0] for x in node.intent}
                for k,(k0,v) in file_id_color.items():
                    if k0 in its:
                        od.append(v)
                odl = len(od)
                for i in range(odl-1,-1,-1):
                    rr = int(r*(i+1)/odl)
                    parent.add(canvas.circle(c,rr,fill=od[i],stroke='black'))
        except:
            _drawnode = None
            file_id_color=None
        fca = pyfca.Lattice(objects,lambda x:x)
        tr = 'tr'
        reflist = lambda x,pfx=tr: ('|'+pfx+('|, |'+pfx).join([str(x)for x in sorted(x)])+'|') if x else ''
        trace = [(".. _`"+tr+"{0}`:\n\n:"+tr+"{0}:\n\n{1}\n\nUp: {2}\n\nDown: {3}\n\n").format(
                n.index, reflist(n.intent,''), reflist(n.up), reflist(n.down))
                for n in fca.nodes]
        tlines = ''.join(trace).splitlines(keepends=True)
        tlines.extend(['.. _`trace`:\n','\n','.. figure:: _images/'+trace_file_name+'.png\n','   :name:\n','\n',
          '   |trace|: `FCA <https://en.wikipedia.org/wiki/Formal_concept_analysis>`__ diagram of dependencies'])
        if file_id_color is not None:
            legend=', '.join([fnm+" "+clr for fnm,(_,clr) in file_id_color.items()])
            tlines.extend([': '+legend,'\n'])
        tlines.append('\n')
        with open(opnj(fldr,trace_file_name+'.rst'),'w',encoding='utf-8') as f:
            f.write('.. raw:: html\n\n')
            #needs in conf.py: html_extra_path=["_images/_trace.svg"]
            f.write('    <object data="'+trace_file_name+'.svg" type="image/svg+xml"></object>\n')
            if file_id_color is not None:
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
    def add_target(tgt,lnkname,restname,upcnt,fi):
        for linktype,linklines in linkfiles:
            linklines.append(create_link(linktype,restname,tgt,lnkname))
        tagentries.append(r'{0}	{1}	/\.\. _`\?{0}`\?:/;"		line:{2}'.format(tgt,"../"*upcnt+fi[0],fi[1]))
    def add_linksto(i,tgt,iterlnks,ojlnk=None): #all the links away from the block following this tgt to next tgt
        linksto = []
        if ojlnk and ojlnk[0] < i:
            if ojlnk[1] in alltgts:
                linksto.append(ojlnk[1])
            else:
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
                    else:
                        linksto.append('-'+lnk)
                        #unknowntgts.append(lnk)
        if linksto:
            if ojlnk:
                objects.append(set([x for x in linksto if not x.startswith('-') and not x.startswith('_')]+[tgt]))
            linksto = '.. .. ' + ','.join(linksto) + '\n\n'
            for _,linklines in linkfiles:
                linklines.append(linksto)
        return ojlnk
    orestname = None
    for restname, doc, lenlns, lnks, tgts in lnktgts:
         if restname != orestname:
             orestname = restname
             if verbose:
                 print('    '+restname+'.rest')
         if not is_rest(doc):
             if verbose:
                 print('        '+doc)
         for _,linklines in linkfiles:
             linklines.append('\n.. .. {0}\n\n'.format(doc))
         iterlnks = iter(lnks)
         ojlnk=None
         for (i,fi),tgt,lnkname in tgts:
             if i is not None:
               ojlnk = add_linksto(i,tgt,iterlnks,ojlnk)
               add_target(tgt,lnkname,restname,upcnt,fi)
         ojlnk = add_linksto(lenlns,None,iterlnks,ojlnk)
    if len(objects)>0:
        tlns = tracelines()
        if tlns:
            for (_,fi),tgt,lnkname in make_tgts(tlns,trace_file_name+'.rst') :
                add_target(tgt,lnkname,trace_target,0,fi)
    for linktype,linklines in linkfiles:
        with open(opnj(fldr,'_links_%s.rst'%linktype),'w',encoding='utf-8') as f:
            f.write('\n'.join(linklines));
    try:
        subprocess.run(['ctags','-R','--sort=0','--fields=+n','--languages=python','--python-kinds=-i','-f','.tags','*'],cwd=fldr)
    except: pass
    with open(opnj(fldr,'.tags'),'ab') as f:
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
            for so in self.path.ant_glob('*.rest.stpl'):
                tsk = Namespace()
                tsk.inputs=(so,)
                tsk.env = self.env
                tsk.generator = self
                render_stpl(tsk,self.bld)
            for fldr, (lnktgts,allfiles,alltgts) in fldrs(self.path.abspath()):
                links_and_tags(fldr,lnktgts,allfiles,alltgts)
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
            eval(compile(confpy.read(encoding='utf-8'),confpy.abspath(),'exec'),config)
            sphinxmock = SphinxMock()
            tikzfn = tikz.render_tikz(sphinxmock,{'tikz':self.inputs[0].read(encoding='utf-8')},sphinxmock.builder.libs)
            os.replace(tikzpth.make_node(tikzfn).abspath(),self.outputs[0].abspath())
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
    @TaskGen.extension('.plt')#python matplotlib plot: have one show() line in there
    def plt_to_png(self,node):
        gen_ext_tsk(self,node,'.plt')
    class PLT(Task.Task):
        def run(self):
            plt = self.inputs[0].read()
            plt = plt.replace('show()',"savefig(r'{}', format='png')".format(self.outputs[0].abspath()))
            plt = "import matplotlib as mpl\nmpl.use('Agg')\n"+plt
            pltvars={}
            eval(compile(plt,self.inputs[0].abspath(),'exec'),pltvars)
    @TaskGen.extension('.rest')
    def gen_docs(self,node):
        docs=get_docs(self.bld)
        d = get_files_in_doc(self.path,node)
        rstscan = lambda: d
        if node.name != "index.rest":
            for doctgt in docs:
                if doctgt.startswith('sphinx_'):
                    continue
                out_node = node.parent.find_or_declare("{0}/{1}.{0}".format(doctgt,node.name[:-len('.rest')]))
                pan = self.create_task('viapandoc', [node], out_node, scan=rstscan, pandoc_to=doctgt)
                if doctgt == 'html':
                    _images = node.parent.make_node('_images')
                    if _images.exists():
                        for x in _images.ant_glob('*'):
                            tx = _images.parent.find_or_declare('html/_images/'+x.name)
                            self.bld(features='subst',source=x,target=tx,is_copy=True)
        else:
            for doctgt in docs:
                if not doctgt.startswith('sphinx_'):
                    continue
                out_node = node.parent.get_bld()
                self.create_task('viasphinx',[node],out_node,cwd=node.parent.abspath(),scan=rstscan,sphinx_builder=doctgt)
    class viapandoc(Task.Task):
        def run(self):
            frm = self.inputs[0].abspath()
            twd = self.outputs[0].abspath()
            dr = self.inputs[0].parent.get_src()
            config = conf_py(dr.abspath())
            linksfile = '_links_'+self.pandoc_to+'.rst'
            cmd = ['pandoc','--standalone','-f','rst']+config.get('pandoc_opts',{}).get(self.pandoc_to,[]
                )+['-t','latex' if self.pandoc_to=='pdf' else self.pandoc_to,'-o',twd]
            opt_refdoc = config.get('pandoc_doc_optref',{}).get(self.pandoc_to,'')
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
            oldp = os.getcwd()
            os.chdir(dr.abspath())
            try:
                with open(frm,'rb') as f:
                    k1 = f.read().replace(b'\n.. include:: _links_sphinx.rst',b'')
                links_file = dr.find_resource(linksfile)
                with open(links_file.abspath(),'rb') as f:
                    k2 = f.read()
                p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
                p.stdin.write(k1)
                p.stdin.write(k2)
                p.stdin.close()    
                p.wait()
            finally:
                os.chdir(oldp)
    class viasphinx(Task.Task):
        always_run = True
        def run(self):
            dr = self.inputs[0].parent
            tgt = self.outputs[0].find_or_declare(self.sphinx_builder).abspath()
            relconfpy,confpy,_ = _pth_nde_parent(dr,'conf.py')
            confdir = op.split(relconfpy)[0]
            cwd=self.get_cwd().abspath()
            subprocess.run(['sphinx-build','-Ea', '-b', self.sphinx_builder.split('_')[1], dr.abspath(), tgt]+(
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
                for anext in '*.tikz *.svg *.dot *.uml *.plt'.split():
                    for anextf in _ant_glob_stpl(bld.path,anext):
                        bld(name='build '+anext,source=anextf)
                        if anext.endswith('tikz'):
                            bld.add_group()#else test fails under linux
                bld.add_group()
                bld(name='build all rest',source=[x for x in _ant_glob_stpl(bld.path,'*.rest','*.rst')if not x.name.endswith('.rst')])
                bld.add_group()
        bld.build_docs = build_docs

except:
    pass

#==============< for building with WAF

#this is for mktree(): first line of file content must not be empty!
example_tree = r'''
       src
        ├ dcx.py << file:///__file__
        ├ reference.tex << file:///__tex_ref__
        ├ code
        │   └ some.h
                /*
                #def gen_tst(lns,**kw):
                #  return [l.split('@')[1] for l in rlines(r'^\s*@',lns)]
                #def gen_tst
                #def gen_tstdoc(lns,**kw):
                #  return ['#) '+l.split('**')[1] for l in rlines('^/\*\*',lns)]
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

        └ doc
           ├ wscript_build
           │    bld.build_docs()
           ├ index.rest
           │  ============
           │  Project Name
           │  ============
           │
           │  .. toctree::
           │     ra.rest
           │     sr.rest
           │     dd.rest
           │     tp.rest
           │
           │  One can also have a 
           │  
           │  - issues.rest for issues
           │  
           │  - pp.rest for the project plan 
           │    (with backlog, epics, stories, tasks) 
           │
           │  .. include:: _trace.rst
           │  
           │  .. include:: _links_sphinx.rst
           │  
           ├ ra.rest
           │  Risk Analysis
           │  =============
           │  
           │  .. _`rz7`:
           │  
           │  :rz7: risk calculations
           │  
           │  Risk calculations are done with python in the ``.stpl`` file.
           │  
           │  .. include:: _links_sphinx.rst
           │  
           ├ sr.rest
           │  Software/System Requirements
           │  ============================
           │
           │  Requirements mostly phrased as tests (see |t9a|). 
           │
           │  .. _`sy7`:
           │
           │  A Requirement Group
           │  -------------------
           │
           │  .. _`s3a`:
           │
           │  :s3a: brief description
           │
           │  Don't count the ID, since the order will change.
           │  The IDs have the first letter of the file and 2 or more random letters of ``[0-9a-z]``.
           │  Use an editor macro to generate IDs.
           │  
           │  If one prefers ordered IDs, one can use templates::
           │  
           │    %id = lambda x=[0]: x.append(x[-1]+1) or "s{:0>2}".format(x[-1])
           │  
           │    .. _`soi`:
           │  
           │    :{{id()}}: auto numbered.
           │  
           │  The disadvantage is that the id will differ between rst and final doc.
           │  When this is needed in an included file use template include: ``%include('x.rst.tpl`)``
           │  See the the ``test/stpl`` folder.
           │
           │  Every ``.rest`` has this line at the end::
           │  
           │     .. include:: _links_sphinx.rst
           │  
           │  .. include:: _links_sphinx.rst
           │  
           ├ dd.rest
           │  Design Description
           │  ==================
           │  
           │  ``dcx.py`` produces its own labeling consistent across DOCX, PDF, HTML.
           │  
           │  .. _`dz7`:
           │  
           │  :dz7: Independent DD IDs
           │  
           │    The relation with RS IDs is m-n. Links like |s3a| can be scattered over more DD entries.  
           │  
           │  .. _`dz3`:
           │  
           │  .. figure:: _images/exampletikz.png
           │     :name:
           │  
           │     |dz3|: Caption here.
           │  
           │     The usage of ``:name:`` produces: ``WARNING: Duplicate explicit target name: ""``. Ignore.
           │  
           │  Reference via |dz3|.
           │  
           │  ``.tikz``, ``.svg``, ``.dot``,  ``.uml`` or ``.plt``, or ``.stpl`` thereof, are converted to ``.png``.
           │  
           │  .. image:: _images/examplesvg.png
           │  
           │  .. image:: _images/exampledot.png
           │  
           │  .. image:: _images/exampleuml.png
           │  
           │  .. image:: _images/exampleplt.png
           │  
           │  .. _`dua`:
           │  
           │  |dua|: Table legend
           │  
           │  .. table::
           │     :name:
           │  
           │     +----+----+
           │     | A  | B  |
           │     +====+====+
           │     | 10 | 11 |
           │     +----+----+
           │  
           │  .. _`dta`:
           │  
           │  |dta|: Table legend
           │  
           │  .. list-table::
           │     :name:
           │     :widths: 20 80
           │     :header-rows: 1
           │  
           │     * - Bit
           │       - Function
           │  
           │     * - 0
           │       - afun
           │  
           │  Reference |dta| does not show ``dta``.
           │  
           │  .. _`dyi`:
           │  
           │  |dyi|: Listing showing struct.
           │  
           │  .. code-block:: cpp
           │     :name:
           │  
           │     struct astruct{
           │        int afield; //afield description 
           │     }
           │  
           │  Reference |dyi| does not show ``dyi``.
           │  
           │  .. _`d9x`:
           │  
           │  .. math:: 
           │     :name:
           │  
           │     V = \frac{K}{r^2}
           │  
           │  Reference |d9x| does not show ``d9x``.
           │  
           │  .. _`d99`:
           │  
           │  :OtherName: Keep names the same all over.
           │  
           │  Here instead of ``d99:`` we use ``:OtherName:``, but now we have two synonyms for the same item.
           │  This is no good. If possible, keep ``d99`` in the source and in the final docs.
           │  
           │  Reference |d99| does not show ``d99``.
           │  
           │  The item target must be in the same file as the item content. The following would not work::
           │  
           │    .. _`dh5`:
           │    
           │    .. include:: somefile.rst   
           │  
           │  .. include:: _links_sphinx.rst
           │  
           ├ tp.rest
           │  Test Plan
           │  =========
           │  
           │  .. _`t9a`:
           │  
           │  Requirement Tests
           │  -----------------
           │
           │  No duplication. Only reference the requirements to be tested.
           │
           │  - |s3a|
           │
           │  Or better: reference the according SR chapter, else changes there would need an update here.
           │
           │  - Test |sy7|
           │
           │  Unit Tests
           │  ----------
           │
           │  Use ``.rst`` for included files and start the file with ``_`` if generated.
           │  
           │  .. include:: _sometst.rst
           │
           │  .. include:: _links_sphinx.rst
           │
           ├ exampletikz.tikz
              [thick]
              \draw (0,0) grid (3,3);
              \foreach \c in {(0,0), (1,0), (2,0), (2,1), (1,2)}
                  \fill \c + (0.5,0.5) circle (0.42);
           ├ examplesvg.svg.stpl
              <?xml version="1.0" encoding="utf-8"?>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" version="1.1" width="172.079pt" height="115.386pt" stroke-width="0.566929" stroke-miterlimit="10.000000">
              %for i in range(10):
                <path fill="none" stroke="#f00" stroke-width="1" d="M10,55 C15,5 100,5 100,{{i*5}}" />
              %end
              %for i in range(10):
                <path fill="none" stroke="#f40" stroke-width="1" d="M10,{{i*5}} C15,5 100,5 100,55" />
              %end
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
           ├ exampleplt.plt
              #vim: syntax=python
              import matplotlib.pyplot as plt
              import numpy as np
              x = np.random.randn(1000)
              plt.hist( x, 20)
              plt.grid()
              plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
              plt.show()
           ├ gen
              #from|to|gen_xxx|kwargs
              ../code/some.h | _sometst.rst                | tstdoc | {}
              ../code/some.h | ../../build/code/some_tst.c | tst    | {}
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
              copyright = '2017, '+author
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
              file_id_color={"ra":("r","lightblue"), "sr":("s","red"), "dd":("d","yellow"), "tp":("t","green")}
              
              pandoc_doc_optref={'latex': '--template reference.tex',
                               'html': {},#each can also be dict of file:template
                               'pdf': '--template reference.tex',
                               'docx': '--reference-doc reference.docx',
                               'odt': '--reference-doc reference.odt'
                               }

              latex_pdf = ['--listings','--number-sections','--pdf-engine','xelatex','-V','titlepage','-V','papersize=a4','-V','toc','-V','toc-depth=3','-V','geometry:margin=2.5cm']
              pandoc_opts = {'pdf':latex_pdf,'latex':latex_pdf,'docx':[],'odt':[],'html':['--mathml','--highlight-style','pygments']}
           └ Makefile
              SPHINXOPTS    = 
              SPHINXBUILD   = sphinx-build
              SPHINXPROJ    = docxsmpl
              SOURCEDIR     = .
              BUILDDIR      = ../../build/doc
              .PHONY: docx help Makefile docxdir pdfdir index
              docxdir: ${BUILDDIR}/docx
              pdfdir: ${BUILDDIR}/pdf
              MKDIR_P = mkdir -p
              ${BUILDDIR}/docx:
              	${MKDIR_P} ${BUILDDIR}/docx
              ${BUILDDIR}/pdf:
              	${MKDIR_P} ${BUILDDIR}/pdf
              index:
              	python ../dcx.py
              help:
              	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
              	@echo "  docx        to docx"
              	@echo "  pdf         to pdf"
              %: Makefile index
              	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
              docx: docxdir index
              	cat sr.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/sr.docx"
              	cat dd.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/dd.docx"
              	cat tp.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/tp.docx"
              	cat ra.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/ra.docx"
              pdf: pdfdir index
              	cat sr.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/sr.pdf"
              	cat dd.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/dd.pdf"
              	cat tp.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g'  | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/tp.pdf"
              	cat ra.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/ra.pdf"
       build/'''

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
    parser.add_argument('--init', dest='root', action='store',
                        help='''create a sample folder structure. 
                        Afterwards run "make html" or "make docx" form "doc" folder.''')
    parser.add_argument('-v','--verbose', action='store_true',
                        help='''Show files recursively included by each rest''')
    parser.add_argument('-o','--out', dest='doctype', action='store',
                        help='''either .ext or out file to determine the type Create link replacements for this doc type.''')
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

  iroot = args['root']
  global verbose
  verbose = args['verbose']
  if iroot:
    thisfile = str(Path(__file__).resolve()).replace('\\','/')
    tex_ref = opnj(op.split(thisfile)[0],'..','reference.tex')
    tree=[l for l in example_tree.replace(
        '__file__',thisfile).replace('__tex_ref__',tex_ref).splitlines() if l.strip()]
    mkdir(iroot)
    oldd = os.getcwd()
    try:
        os.chdir(iroot)
        mktree(tree)
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
            #TODO make tests 
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
    for fldr, (lnktgts,allfiles,alltgts) in fldrs('.'):
        if verbose:
            print(fldr)
        #generate files
        genpth = opnj(fldr,'gen')
        if op.exists(genpth):
            for f,t,d,kw in parsegenfile(genpth):
                gen(opnj(fldr,f),target=opnj(fldr,t),fun=d,**kw)
        links_and_tags(fldr,lnktgts,allfiles,alltgts)

if __name__=='__main__':
  main()

