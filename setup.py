#!/usr/bin/env python

"""
#install: latex, plantuml, graphviz, inkscape

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
import os
import sys

#also change ing doc/conf.py
__version__ = '1.7.0'

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

long_description = ''.join([x for i,x in enumerate(
                        dorst(long_description.splitlines()))
                        if not x.startswith('.. _`') and i>0])

##to check with ``restview --pypi-strict long_description.rst``
#with open('long_description.rst','w',encoding='utf-8') as f:
#    f.write(long_description)

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

      install_requires=['cffi','cairocffi','cairosvg',
                        'pillow', 'pyx', 'pyfca',
                        'numpy', 'matplotlib','sympy','pint','drawsvg',
                        'svgwrite', 'stpl', 'pypandoc', 'docutils',
                        'sphinx', 'sphinx_bootstrap_theme'],
      extras_require={'develop': ['mock', 'virtualenv', 'pytest-coverage'],
                      'build': ['waf']},
      long_description=long_description,
      packages=['rstdoc'],
      package_data={'rstdoc': ['../readme.rst','reference.tex', 'reference.docx',
                               'reference.odt', 'wafw.py']},
      zip_safe=False,
      tests_require=['pytest', 'pyyaml', 'pytest-coverage', 'mock'],
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
