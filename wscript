from waflib import Logs
Logs.colors_lst['BLUE']='\x1b[01;36m'
top='.'
out='../build'
def options(opt):
  opt.load('dcx',tooldir='rstdoc')
def configure(cfg):
  cfg.load('dcx',tooldir='rstdoc')
def build(bld):
  #defines bld.stpl(), bld.gen_files(), bld.gen_links(), bld.build_docs()
  bld.load('dcx',tooldir='rstdoc')
  bld.recurse('doc')
