#!/usr/bin/env python

"""
#install: latex, plantuml, graphviz, inkscape

#pump version:
doc/conf.py
rstdoc/_version.py

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
import sys
from importlib.machinery import SourceFileLoader

here = abspath(dirname(__file__))

_version = SourceFileLoader("_version", join(here,'rstdoc','_version.py')).load_module()

long_description = SourceFileLoader("long_description", join(here,'long_description.py')).load_module()

setup(name='rstdoc',
      version=_version.__version__,
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
      long_description=long_description.long_description,
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
