#!/usr/bin/env python
#encoding: utf-8 

"""
Support script to create final documentation (PDF, HTML, DOCX)
from restructuredText (RST). 

It creates

- _links_pdf.rst _links_docx.rst _links_sphinx.rst

- .tags

- processes ``gen`` files (see examples produced by --init)

See folder layout at the end of the file.

Usage
-----

Initialize example tree::

  $ python ./dcx.py --init tmp

Only create .tags and _links_xxx.rst::

  $ cd tmp/src/doc
  $ python ./dcx.py

Create the docs (and .tags and _links_xxx.rst):

  $ make html
  $ make dcx
  $ make pdf

``waf`` build also considers all recursive include dependencies. 
In wscript::

  def configure(cfg)
      cfg.load('dcx',tooldir='.')
      ...
      
  def build(bld):
      bld.load('dcx',tooldir='.')
      ...

Hyperlinks work in HTML, DOCX and PDF.

- Open all DOCX in advance to do without the virus warning.

- Use ``Alt+<-`` to go back in Acrobat Reader after a jump.

The generated ctags file works for:

  - vim

  - atom with atom-ctags

  - visual studio code with ctagsx

Conventions
-----------

Main files have ``.rest`` extension, converted by Sphinx and Pandoc.
Included files have extension ``.rst`` ignored by Sphinx (see conf.py).

In the src tree the only files (not folders) start with ``_`` are generated.

See further conventions by the example created with ``--init`` 
(end of this file).

"""

import sys
import os
import re
from pathlib import Path
from urllib import request
import argparse
import string
from functools import reduce
from collections import OrderedDict,defaultdict

retitle = re.compile(r'^([!"#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~])\1+$')
reitem = re.compile(r'^:(\w[^:]*):\s.*$')
renamed = re.compile(r'^\s*:name:\s*(\w.*)*$')

#>>>> nj
nj = lambda *x:os.path.normpath(os.path.join(*x))

#>>>> rindices
def rindices(r,lns):
  """Return the indices matching a regular expression
  >>> lns=['a','ab','b','aa']
  >>> [lns[i] for i in rindices(r'^a\w*',lns)]==['a', 'ab', 'aa']
  True
  """
  if isinstance(r,str):
    r = re.compile(r)
  return filter(lambda x:r.search(lns[x]),range(len(lns)))

#>>>> rlines
def rlines(r,lns):
  return [lns[i] for i in rindices(r,lns)]

#>>>> intervals
"""
>>> intervals([1,2,3])==[(1, 2), (2, 3)]
True
"""
intervals = lambda it: list(zip(it[:],it[1:]))

#>>>> in2s
"""
>>> in2s([1,2,3,4])==[(1, 2), (3, 4)]
True
"""
in2s = lambda it: list(zip(it[::2],it[1::2]))

def genrstincluded(fn,path=None):
    """return recursively all files included from an rst file"""
    if path:
        nfn = os.path.normpath(os.path.join(path,fn))
    else:
        nfn = fn
    yield fn
    lns = None
    with open(nfn,'r',encoding='utf-8') as f:
        lns = f.readlines()
    toctree = False
    if lns:
        for e in lns:
            if toctree:
                toctreedone = False
                if e.startswith(' '):
                    fl=e.strip()
                    if '.rest' in fl or '.rst' in fl and os.path.exists(fl):
                        toctreedone = True
                        yield from genrstincluded(fl,path)
                    continue
                elif toctreedone:
                    toctree = False
            if e.startswith('.. toctree::'):
                toctree = True
            elif e.startswith('.. '):
                try:
                    f,t=e[3:].split('include:: ')
                    nf = not f and t
                    if nf:
                        yield from genrstincluded(nf.strip(),path)
                except:
                    pass

def genfldrincluded(
        directory='.'
        ,parse_extensions = ['.rest']
        ,exclude_paths_substrings = ['_links_','index.rest']
        ):
    """ find all files in ``directory`` ending in ``parse_extensions``
    and all files recursively included
    excluding those that contain ``exclude_paths_substrings``
    """
    for p,ds,fs in os.walk(directory):
        for f in fs:
            if any([f.endswith(x) for x in parse_extensions]):
                pf=nj(p,f)
                if any([x in pf for x in exclude_paths_substrings]):
                    continue
                res = []
                for ff in genrstincluded(f,p):
                    if any([x in ff for x in exclude_paths_substrings]):
                        continue
                    pth=nj(p,ff)
                    if any([x in pth for x in exclude_paths_substrings]):
                        continue
                    res.append(pth)
                yield res

def links(lns):
    r = re.compile(r'\|(\w+)\|')
    for i,ln in enumerate(lns):
        mo = r.findall(ln)
        for g in mo:
            yield i,g

g_counters=defaultdict(dict)
def linktargets(lns,docnumber):
    #docprefix = str(docnumber)+'.'
    docprefix = ' '
    if docnumber not in g_counters:
        g_counters[docnumber] = {".. figure":1,".. math":1,".. table":1,".. code":1} #=list-table,code-block
    counters=g_counters[docnumber]
    itgts = rindices(r'^\.\. _`?(\w[^:`]*)`?:\s*$',lns)
    lenlns = len(lns)
    for i in itgts:
        tgt = lns[i].strip(' ._:`\n')
        lnkname = tgt
        for j in range(i+2,i+8):
            if j >= lenlns-1:
                break
            lnj = lns[j]
            if retitle.match(lnj):
                lnkname=lns[j-1].strip()
                break
            #lnj=":lnkname: words"
            itm = reitem.match(lnj)
            if itm:
                lnkname, = itm.groups()
                break
            #j,lns=1,".. figure::\n  :name: lnkname".splitlines();lnj=lns[j]
            #j,lns=1,".. figure::\n  :name:".splitlines();lnj=lns[j]
            #j,lns=1,".. math::\n  :name: lnkname".splitlines();lnj=lns[j]
            itm = renamed.match(lnj)
            if itm:
                lnkname, = itm.groups()
                lnj1 = lns[j-1].split('::')[0].replace('list-table','table').replace('code-block','code')
                if not lnkname and lnj1 in counters:
                    lnkname = lnj1[3].upper()+lnj1[4:]+docprefix+str(counters[lnj1])
                    counters[lnj1]+=1
                    break
                elif lnkname:
                    lnkname = lnkname.strip()
                    break
                else:
                    lnkname = tgt
        yield i, tgt, lnkname

def gen(source,target=None,fun=None,**kw):
    """ take the gen[_fun] functions enclosed by #def gen[_fun] to create a new file.
    >>> source=[i+'\\n' for i in '''
    ...        #def gen(lns,**kw):
    ...        #  return [l.split('#@')[1] for l in rlines('^\s*#@',lns)]
    ...        #def gen
    ...        #@some lines
    ...        #@to extrace
    ...        '''.splitlines()]
    >>> [l.strip() for l in gen(source)]
    ['some lines', 'to extrace']
    """
    if isinstance(source,list):
        lns = source
        source = ""
    else:
        lns = []
        try:
            with open(source,'r',encoding='utf-8') as f:
                lns = f.readlines()
        except:
            sys.stderr.write("ERROR: {} cannot be opened\n".format(source))
            return
    iblks = list(rindices(r'#def gen(\w*(lns,\*\*kw):)*',lns))
    py3 = '\n'.join([lns[k][lns[i].index('#')+1:] 
            for i,j in in2s(iblks) 
            for k in range(i,j)])
    eval(compile(py3,source+'#gen','exec'),globals())
    if fun:
        gened = eval('gen_'+fun+'(lns,**kw)')
    else:
        gened = []
        for i in iblks[0::2]:
            cd = re.split("#def |:",lns[i])[1]#gen(lns,**kw)
            gened += eval(cd)
    if target:
        with open(target,'w',encoding='utf-8') as o:
            o.write(''.join(gened))
    else:
        return list(gened)

def genfile(gf):
    with open(gf,'r') as f:
        genfilelns = f.readlines()
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

def mktree(tree):
    """ Build a directory tree from a string as returned by the tree tool.

    For same level, identation must be the same.
    So don't start with '''a in the example below.

    In addition 
    
    leafs:

    - / or \\ to make a directory leaf

    - << to copy file from internet using http:// or locally using file:://

    - use indented lines as file content

    >>> tree=[l for l in '''
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
    ...       '''.splitlines() if l.strip()]
    >>> True#mktree(tree) 
    True
    """
    ct = re.search(r'[^\s├│└]',tree[0]).span()[0]
    t1 = [t[ct:] for t in tree]
    entry_re = re.compile(r'^(\w[^ </\\]*)(\s*<<\s*|\s*[\\/]\s*)*(\w.*)*')
    it1 = list(rindices(entry_re,t1))
    lt1 = len(t1)
    it1.append(lt1)
    for c,f in intervals(it1):
        ef,ed,eg = entry_re.match(t1[c]).groups()
        if ef:
            if c<f-1:
                i1 = t1[c+1].find('└')+1
                i2 = t1[c+1].find('├')+1
                ix = (i1>=0 and i1 or i2)-1
                if ix >= 0 and ix <= len(ef):
                    mkdir(ef)
                    old = os.getcwd()
                    os.chdir(ef)
                    mktree(
                      t1[c+1:f]
                      )
                    os.chdir(old)
                else:
                    t0 = t1[c+1:f]
                    ct = re.search(r'[^\s│]',t0[0]).span()[0]
                    tt = [t[ct:]+'\n' for t in t0]
                    with open(ef,'w') as fh:
                        fh.writelines(tt)
            elif eg:
                request.urlretrieve(eg,ef)
            elif ed and (('\\' in ed) or ('/' in ed)):
                mkdir(ef)
            else:
                Path(ef).touch()

def genfldrs(scanroot='.'):
    odir = os.getcwd()
    os.chdir(scanroot)
    fldr_lnktgts = OrderedDict()
    fldr_allfiles = defaultdict(set) #fldr, files
    fldr_alltgts = defaultdict(set) #all link target ids
    dcns=set([])
    for dcs in genfldrincluded('.'): 
        rest = [adc for adc in dcs if adc.endswith('.rest')][0]
        fldr,fln = os.path.split(rest)
        fldr_allfiles[fldr] |= set(dcs)
        restn=os.path.splitext(fln)[0]
        dcns.add(restn)
        for doc in dcs:
            try: #generated files might not be there
                with open(doc,'r',encoding='utf-8') as f:
                    lns = f.readlines()
                lnks = list(links(lns))
                tgts = list(linktargets(lns,len(dcns)))
                if fldr not in fldr_lnktgts:
                    fldr_lnktgts[fldr] = []
                fldr_lnktgts[fldr].append((restn,doc,len(lns),lnks,tgts))
                fldr_alltgts[fldr] |= set([n for ni,n,nn in tgts])
            except:
                pass
    for fldr,lnktgts in fldr_lnktgts.items():
        allfiles = fldr_allfiles[fldr]
        alltgts = fldr_alltgts[fldr]
        yield fldr, (lnktgts,allfiles,alltgts)
    os.chdir(odir)

doctypes = "sphinx docx pdf".split()
def lnksandtags(fldr,lnktgts,allfiles,alltgts):
    _tgtsdoc = [(dt,[]) for dt in doctypes]
    tags = []
    orestn = None
    up = 0
    if (fldr.strip()):
       up = len(fldr.split(os.sep))
    #unknowntgts = []
    for restn, doc, lenlns, lnks, tgts in lnktgts:
         fin = doc.replace("\\","/")
         if restn != orestn:
             orestn = restn
             print('    '+restn+'.rest')
         if not doc.endswith(restn+'.rest'):
             print('        '+doc)
         for _,di in _tgtsdoc:
             di.append('\n.. .. {0}\n\n'.format(fin))
         iterlnks = iter(lnks)
         def add_linksto(i,ojlnk=None):
             linksto = []
             if ojlnk and ojlnk[0] < i:
                 if ojlnk[1] in alltgts:
                     linksto.append(ojlnk[1])
                 else:
                     linksto.append('-'+ojlnk[1])
                     #unknowntgts.append(ojlnk[1])
                 ojlnk = None
             if ojlnk is None:
                 for j, lnk in iterlnks:
                     if j > i:#links up to this target
                         ojlnk = j,lnk
                         break
                     else:
                         if lnk in alltgts:
                             linksto.append(lnk)
                         else:
                             linksto.append('-'+lnk)
                             #unknowntgts.append(lnk)
             if linksto:
                 linksto = '.. .. ' + ','.join(linksto) + '\n\n'
                 for _,ddi in _tgtsdoc:
                     ddi.append(linksto)
             return ojlnk
         ojlnk=None
         for i,tgt,lnkname in tgts:
             ojlnk = add_linksto(i,ojlnk)
             for ddn,ddi in _tgtsdoc:
                 if ddn=='sphinx':
                     tgte = ".. |{0}| replace:: :ref:`{1}<{0}>`\n".format(tgt,lnkname)
                 elif ddn=='docx':
                     tgte = ".. |{0}| replace:: `{1} <{2}#{0}>`_\n".format(tgt,lnkname,restn+'.docx')
                 elif ddn=='pdf':
                     tgte = ".. |{0}| replace:: `{1} <{2}#{0}>`_\n".format(tgt,lnkname,restn+'.pdf')
                 ddi.append(tgte)
             tags.append('{0}	{1}	/^\.\. _`\?{0}`\?:/;"		line:{2}'.format(tgt,"../"*up+fin,i+1))
         ojlnk = add_linksto(lenlns,ojlnk)
    for ddn,ddi in _tgtsdoc:
        with open(nj(fldr,'_links_%s.rst'%ddn),'w',encoding='utf-8') as f:
            f.write('\n'.join(ddi));
    with open(nj(fldr,'.tags'),'wb') as f:
        f.write('\n'.join(tags).encode('utf-8'));

#==============> for building with WAF

try:
    from waflib import TaskGen, Task
    import bottle

    gensrc={}
    @TaskGen.feature('gen_file')
    @TaskGen.before('process_rule')
    def gen_file(self):
        global gensrc
        gensrc={}
        for f,t,fun,kw in genfile(self.path.make_node('gen').abspath()):
            gensrc[t]=f
            frm = self.path.find_resource(f)
            twd = self.path.make_node(t)
            self.create_task('gentsk',frm,twd,fun=fun,kw=kw)
    class gentsk(Task.Task):
        def run(self):
            try:
                frm = self.inputs[0]
                twd = self.outputs[0]
                gen(frm.abspath(),twd.abspath(),fun=self.fun,**self.kw)
            except: pass
    @TaskGen.extension('.rest')
    def gendoc(self,node):
        def rstscan():
            apth = node.abspath()
            d,n = os.path.split(apth)
            deps = [self.path.find_node(x) for x in genrstincluded(n,d) if '_links_' not in x]
            depsgensrc = [self.path.find_node(gensrc[x]) for x in deps if x and x in gensrc] 
            return ([x for x in deps if x]+depsgensrc,[])
        out_node_docx = node.parent.find_or_declare('docx/'+node.name[:-len('.rest')]+'.docx')
        out_node_pdf = node.parent.find_or_declare('pdf/'+node.name[:-len('.rest')]+'.pdf')
        out_node = node.change_ext('.docx')
        docs = [x.lower() for x in self.bld.options.docs]
        if not docs:
            docs = [x.lower() for x in self.env.docs]
        if node.name != "index.rest":
            if 'docx' in docs or 'defaults' in docs:
                self.create_task('docx', node, out_node_docx, scan=rstscan)
            if 'pdf' in docs:
                self.create_task('pdf', node, out_node_pdf, scan=rstscan)
        else:
            out_nodes = [self.path.get_src().make_node(x) for x in ['_links_'+x+'.rst' for x in doctypes]+['.tags']]
            self.create_task('rstindex',node,out_nodes,scan=rstscan)
            if 'html' in docs:
                self.create_task('sphinx',node,out_node.parent,cwd=os.path.dirname(node.abspath()),scan=rstscan)
    class rstindex(Task.Task):
        def run(self):
            ps = self.inputs[0].abspath()
            psfldr, psname = os.path.split(ps)
            for fldr, (lnktgts,allfiles,alltgts) in genfldrs(psfldr):
                lnksandtags(fldr,lnktgts,allfiles,alltgts)
    class pdf(Task.Task):
        def run(self):
            from subprocess import Popen, PIPE
            frm = self.inputs[0].abspath()
            twd = self.outputs[0].abspath()
            srcpth = self.generator.path.get_src()
            reftex = 'reference.tex'
            if srcpth.find_node(reftex):
                refparam = "--template {0}"
            elif srcpth.find_node('../'+reftex):
                refparam = "--template ../{0}"
            else:
                refparam = ""
            pandoc = ' '.join(["pandoc --listings",refparam,
                "-V titlepage -f rst --pdf-engine xelatex",
                "--number-sections -V papersize=a4 -V toc -V toc-depth=3",
                "-V geometry:margin=2.5cm -o {1}"]).format(reftex,twd)
            drnm = os.path.dirname(frm)
            with open(frm,'rb') as f:
                i1 = f.read().replace(b'\n.. include:: _links_sphinx.rst',b'')
            with open(nj(drnm,'_links_pdf.rst'),'rb') as f:
                i2 = f.read()
            p = Popen(pandoc, stdin=PIPE, cwd=drnm)
            p.stdin.write(i1)
            p.stdin.write(i2)
            p.stdin.close()    
            p.wait()
    class docx(Task.Task):
        def run(self):
            from subprocess import Popen, PIPE
            frm = self.inputs[0].abspath()
            twd = self.outputs[0].abspath()
            srcpth = self.generator.path.get_src()
            refdocx = 'reference.docx'
            if srcpth.find_node(refdocx):
                pandoc = "pandoc --reference-doc={0} -f rst -t docx -o {1}".format(refdocx,twd)
            elif srcpth.find_node('../'+refdocx):
                pandoc = "pandoc --reference-doc=../{0} -f rst -t docx -o {1}".format(refdocx,twd)
            else:
                pandoc = "pandoc -f rst -t docx -o "+twd
            drnm = os.path.dirname(frm)
            with open(frm,'rb') as f:
                i1 = f.read().replace(b'\n.. include:: _links_sphinx.rst',b'')
            with open(nj(drnm,'_links_docx.rst'),'rb') as f:
                i2 = f.read()
            p = Popen(pandoc, stdin=PIPE, cwd=drnm)
            p.stdin.write(i1)
            p.stdin.write(i2)
            p.stdin.close()    
            p.wait()
    class sphinx(Task.Task):
        run_str = 'sphinx-build -Ea -b html . ${TGT}/html -c ..'

    def options(opt):
        def docscb(option, opt, value, parser):
            setattr(parser.values, option.dest, value.split(','))
        opt.add_option("--docs", type='string', action="callback", callback= docscb, dest='docs', default=[],
            help="Like html,docx (default) or html,pdf or html,docx,pdf at configure or build (default None)") 

    def configure(cfg):
        cfg.env['docs'] = cfg.options.docs

    def build(bld):
        bld.src2bld = lambda f: bld(features='subst',source=f,target=f,is_copy=True)
        def gen_file():
            bld(features="gen_file")
            bld.add_group()
        bld.gen_file = gen_file
        def build_doc():
            bld(source="index.rest")
            bld.add_group()
            bld(source=[x for x in bld.path.ant_glob("*.rest") if "index.rest" not in x.name])
        bld.build_doc = build_doc
        def stpl(tsk):
            bldpath = bld.path.get_bld()
            ps = tsk.inputs[0].abspath()
            pt = tsk.outputs[0].abspath()
            lookup,name=os.path.split(ps)
            env = tsk.env
            env.update(tsk.generator.__dict__)
            st=bottle.template(name
                    ,template_lookup = [lookup]
                    ,bldpath = bldpath.abspath()
                    ,options = bld.options
                    ,**env
                    ) 
            with open(pt,mode='w',encoding="utf-8") as f: 
                f.write(st)
        bld.stpl=stpl
        bld.declare_chain('stpl',ext_in=['.stpl'],ext_out=[''],rule=stpl)

except:
    pass

#==============< for building with WAF

if __name__=='__main__':
  parser = argparse.ArgumentParser(description='''Sample RST Documentation for HTML and DOCX.
    Creates |substitution| links and ctags for link targets.
    ''')
  parser.add_argument('--init', dest='root', action='store',
                      help='''create a sample folder structure. 
                      Afterwards run "make html" or "make docx" form "doc" folder.''')
  args = parser.parse_args()

  if args.root:
    thisfile = str(Path(__file__).resolve()).replace('\\','/')
    try:#win32
        thisfile = thisfile.split(':')[1]
    except: pass
    #{{ stands for {
    #first line non-empty!
    tree=[l for l in r'''
       src
        ├ code
        │   └ some.h
                /*
                #def gen_tst(lns,**kw):
                #  return [l.split('@')[1] for l in rlines('^\s*@',lns)]
                #def gen_tst
                #def gen_tstdoc(lns,**kw):
                #  return ['#) '+l.split('**')[1] for l in rlines('^/\*\*',lns)]
                #def gen_tstdoc

                @//generated from some.h
                @#include <assert.h>
                @#include "some.h"
                @int main()
                @{{
                */

                /**Test add1()
                @assert(add1(1)==2);
                */
                int add1(int a)
                {{
                  return a+1;
                }}

                /**Test add2()
                @assert(add2(1)==3);
                */
                int add2(int a)
                {{
                  return a+2;
                }}

                /*
                @}}
                */
        │
        └ doc
           ├ _static
           │    └ img.png << https://assets-cdn.github.com/images/modules/logos_page/Octocat.png
           ├ dcx.py << file://{0}
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
           ├ ra.rest
           │  Risk Analysis
           │  =============
           │  
           │  .. _`rz7`:
           │  
           │  :rz7: Hand-in-hand with SR
           │        Risk analysis could be generated from a python file,
           │        where calculation are done.
           │  
           │  Similarly one can have a 
           │  
           │  - is.rest for issues
           │  
           │  - pp.rest for the project plan 
           │    (with backlog, epics, stories, tasks) 
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
           │    Don't count the ID, since the order will change.
           │    Instead: The IDs have the first letter of the file 
           │    and 2 or more random letters of ``[0-9a-z]``.
           │    Use an editor macro to generate IDs.
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
           │  ``dcx.py`` produces its own labeling consistent across DOCX, PDF, HTML,
           │  and same as Sphinx (useful for display math). 
           │  
           │  .. _`dz7`:
           │  
           │  :dz7: Independent DD IDs
           │  
           │    The relation with RS IDs is m-n. Links like |s3a|
           │    can be scattered over more DD entries.  
           │  
           │  .. _`dz3`:
           │  
           │  .. figure:: _static/img.png
           │     :name:
           │  
           │     |dz3|: Caption here.
           │  
           │     The usage of ``:name:`` produces: ``WARNING: Duplicate explicit target name: ""``. Ignore.
           │  
           │  Reference via |dz3|.
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
           │       - xxx
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
           │     struct xxx{{
           │        int yyy; //yyy for zzz
           │     }}
           │  
           │  Reference |dyi| does not show ``dyi``.
           │  
           │  .. _`d9x`:
           │  
           │  .. math:: 
           │     :name:
           │  
           │     V = \frac{{K}}{{r^2}}
           │  
           │  Reference |d9x| does not show ``d9x``.
           │  
           │  .. _`d99`:
           │  
           │  :SameName: Keep names the same all over.
           │  
           │    Here instead of ``:d99:`` we use ``:SameName:``, but now we have two synonyms for the same item.
           │    This is no good. If possible, keep ``d99`` in the source and in the final docs.
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
           │   Test Plan
           │   =========
           │   
           │   .. _`t9a`:
           │   
           │   Requirement Tests
           │   -----------------
           │
           │   No duplication. Only reference the requirements to be tested.
           │
           │   - |s3a|
           │
           │   Or better: reference the according SR chapter, else changes there would need an update here.
           │
           │   - Test |sy7|
           │
           │   Unit Tests
           │   ----------
           │
           │   Use ``.rst`` for included files and start the file with ``_`` if generated.
           │   
           │   .. include:: _sometst.rst
           │
           │   .. include:: _links_sphinx.rst
           │
           ├ gen
              #from|to|gen_xxx|kwargs
              ../code/some.h | _sometst.rst                | tstdoc | {{}}
              ../code/some.h | ../../build/code/some_tst.c | tst    | {{}}
           ├ conf.py
              extensions = ['sphinx.ext.autodoc',
                  'sphinx.ext.todo',
                  'sphinx.ext.mathjax',
                  'sphinx.ext.viewcode',
                  'sphinx.ext.graphviz',
                  ]
              numfig = False
              templates_path = ['_templates']
              source_suffix = '.rest'
              master_doc = 'index'
              project = 'DocxSample'
              author = project+' Project Team'
              copyright = '2017, '+author
              version = '1.0'
              release = '1.0.0'
              language = None
              exclude_patterns = []
              pygments_style = 'sphinx'
              todo_include_todos = True
              import sphinx_bootstrap_theme
              html_theme = 'bootstrap'
              html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
              latex_elements = {{
                      'preamble':r"""
                      \usepackage{{caption}}
                      \captionsetup[figure]{{labelformat=empty}}
                      """
                      }}
              latex_documents = [
                  (master_doc, 'docxsample.tex', project+' Documentation',
                   author, 'manual'),
              ]
           └ Makefile
              SPHINXOPTS    = 
              SPHINXBUILD   = sphinx-build
              SPHINXPROJ    = docxsmpl
              SOURCEDIR     = .
              BUILDDIR      = ../../build/doc
              .PHONY: docx help Makefile docxdir pdfdir index
              docxdir: ${{BUILDDIR}}/docx
              pdfdir: ${{BUILDDIR}}/pdf
              MKDIR_P = mkdir -p
              ${{BUILDDIR}}/docx:
              	${{MKDIR_P}} ${{BUILDDIR}}/docx
              ${{BUILDDIR}}/pdf:
              	${{MKDIR_P}} ${{BUILDDIR}}/pdf
              index:
              	python dcx.py
              help:
              	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
              	@echo "  docx        to docx"
              	@echo "  pdf         to pdf"
              %: Makefile index
              	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
              docx: docxdir index
              	cat ra.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/ra.docx"
              	cat sr.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/sr.docx"
              	cat dd.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/dd.docx"
              	cat tp.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/tp.docx"
              pdf: pdfdir index
              	cat ra.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/ra.pdf"
              	cat sr.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/sr.pdf"
              	cat dd.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/dd.pdf"
              	cat tp.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g'  | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/tp.pdf"
       build
        ├ code/
        └ doc
          ├ html/
          └ docx/
       '''.format(thisfile).splitlines() if l.strip()]
    mkdir(args.root)
    oldd = os.getcwd()
    os.chdir(args.root)
    mktree(tree)
    os.chdir(oldd)
  else:
    #link, gen and tags per folder
    for fldr, (lnktgts,allfiles,alltgts) in genfldrs('.'):
        print(fldr)
        #generate files
        gf = nj(fldr,'gen')
        if os.path.exists(gf):
            for f,t,d,kw in genfile(gf):
                gen(nj(fldr,f),target=nj(fldr,t),fun=d,**kw)
        lnksandtags(fldr,lnktgts,allfiles,alltgts)

