#!/usr/bin/env python

"""
#install: latex, plantuml, graphviz, inkscape

#version:
doc/conf.py
rstdoc/__init__.py

#test
rm -rf test/__pycache__
py.test -vv --doctest-modules --cov=rstdoc --cov-report term-missing
#or
waf configure && waf --docs sphinx_html --tests

#install
pip uninstall rstdoc
pip install pillow pyx pyfca cairosvg numpy matplotlib sympy pint svgwrite
pip install drawsvg stpl pypandoc docutils sphinx sphinx_bootstrap_theme
pip install -e .
#or
python setup.py bdist_wheel
pip install dist/rstdoc-X.Y.Z-py3-non-any.whl

#upload
restview --long-description --strict
sudo python setup.py bdist_wheel
twine upload ./dist/*.whl
"""

from setuptools import setup
from os.path import abspath,dirname,join
import os
import sys
import re
import ast

here = abspath(dirname(__file__))
os.chdir(here)

_version_re = re.compile(r'__version__\s*=\s*(.*)')
with open(os.path.join(here, 'rstdoc','__init__.py'), 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

def long_description():
      def read(fname, separator='\n"""'):
          with open(join(here, fname),
                    encoding='utf-8') as f:
              return f.read().split(separator)[1]
      ld = '\n'.join([
          open('readme.rst').read(),
          read('rstdoc/dcx.py'),
          read('rstdoc/dcx.py', separator="'''\\").split("'''")[0],
          read('rstdoc/fromdocx.py'),
          read('rstdoc/listtable.py'),
          read('rstdoc/untable.py'),
          read('rstdoc/reflow.py'),
          read('rstdoc/reimg.py'),
          read('rstdoc/retable.py')
          ])
      try:
          sys.path.append(join(here, 'rstdoc'))
          from dcx import dorst
      except:
          try:
              from rstdoc.dcx import dorst
          except:
              def dorst(linelist):
                  return linelist
      ld = ''.join([x for i,x in enumerate(
                        dorst(ld.splitlines())
                        ) if not x.startswith('.. _`') and i>0])
      return ld


if __name__ == '__main__':
    if sys.argv[1] == '--print':
        try:
            sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
        except:
            pass
        print(long_description())
    else:
        setup(name='rstdoc',
      version=version,
      description='rstdoc - support documentation in restructedText (rst)',
      license='MIT',
      author='Roland Puntaier',
      keywords=['Documentation'],
      author_email='roland.puntaier@gmail.com',
      url='https://github.com/rpuntaie/rstdoc',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Information Technology',
          'Topic :: Utilities',
          ],
      install_requires=['cffi','cairocffi','cairosvg',
                        'pillow', 'pyx', 'pyfca', 'pygal',
                        'numpy', 'matplotlib','sympy','pint','drawsvg',
                        'svgwrite', 'stpl', 'pypandoc', 'docutils',
                        'sphinx', 'sphinx_bootstrap_theme',
                        'gitpython', 'pyyaml','txdir'],
      extras_require={'develop': ['mock', 'virtualenv', 'pytest-coverage'],
                      'build': ['waf']},
      long_description=long_description(),
      packages=['rstdoc'],
      package_data={'rstdoc': ['../readme.rst','reference.tex', 'reference.docx',
                               'reference.odt', 'wafw.py']},
      zip_safe=False,
      tests_require=['pytest', 'pytest-coverage', 'mock'],
      entry_points={
          'console_scripts': [
              'rstlisttable=rstdoc.listtable:main',
              'rstreflow=rstdoc.reflow:main',
              'rstreimg=rstdoc.reimg:main',
              'rstretable=rstdoc.retable:main',
              'rstdcx=rstdoc.dcx:main',
              'rstdoc=rstdoc.dcx:main',
              'rstfromdocx=rstdoc.fromdocx:main',
              'rstuntable=rstdoc.untable:main',
              ]
      },
)
