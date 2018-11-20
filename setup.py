#!/usr/bin/env python

"""
#install: latex, plantuml, graphviz, inkscape

#test
py.test -vv --cov=rstdoc --cov-report term-missing
#or
waf configure && waf --docs sphinx_html --tests

#install
pip uninstall rstdoc
pip install -e .
#or
python setup.py bdist_wheel
pip install dist/rstdoc-X.Y.Z-py3-non-any.whl

#upload
sudo python setup.py bdist_wheel
twine upload ./dist/*.whl
"""

from setuptools import setup
import os
import sys

__version__ = '1.6.4'

sys.path.append('./rstdoc')
from dcx import dorst

def read(fname, separator='\n"""'):
    with open(os.path.join(os.path.dirname(__file__), fname),
              encoding='utf-8') as f:
        return f.read().split(separator)[1]


long_description = '\n'.join([
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

long_description = ''.join([x for x in dorst(long_description.splitlines())
                            if not x.startswith('.. _`')])

setup(name='rstdoc',
      version=__version__,
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

      install_requires=['pillow', 'pyx', 'pyfca', 'pygal', 'cairosvg',
                        'svgwrite', 'stpl', 'pypandoc', 'sphinx',
                        'sphinx_bootstrap_theme', 'pint'],
      extras_require={'develop': ['mock', 'pytest-coverage'],
                      'build': ['waf']},
      long_description=long_description,
      packages=['rstdoc'],
      package_data={'rstdoc': ['reference.tex', 'reference.docx',
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
              'rstfromdocx=rstdoc.fromdocx:main',
              'rstuntable=rstdoc.untable:main',
              ]
      },

      )
