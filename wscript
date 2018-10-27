from waflib import Logs
Logs.colors_lst['BLUE']='\x1b[01;36m'
top='src'
out='build'
def options(opt):
  opt.load('dcx',tooldir='src/rstdoc')
  opt.add_option("--tests", default=False, action="store_true", help="Run the tests") 
def configure(cfg):
  cfg.load('dcx',tooldir='src/rstdoc')
def build(bld):
  bld.load('dcx',tooldir='src/rstdoc')
  if bld.options.tests:
      bld.exec_command('py.test --cov rstdoc --cov-report term-missing > src/doc/_testcoverage.rst')
  bld.recurse('src/doc')
