from waflib import Logs
Logs.colors_lst['BLUE']='\x1b[01;36m'
top='.'
out='build'
def options(opt):
  opt.load('dcx',tooldir='rstdoc')
  opt.add_option("--tests", default=False, action="store_true", help="Run the tests") 
def configure(cfg):
  cfg.load('dcx',tooldir='rstdoc')
def build(bld):
  bld.load('dcx',tooldir='rstdoc')
  if bld.options.tests:
      bld.exec_command('py.test --doctest-modules --cov=rstdoc --cov-report term-missing > doc/_testcoverage.rst')
  bld.recurse('doc')
