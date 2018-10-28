#!/usr/bin/env python

#sudo pip install -e .
#py.test --cov rstdoc --cov-report term-missing

#sudo python setup.py bdist_wheel
#twine upload ./dist/*.whl

from setuptools import setup
import platform
import os, os.path
import io
import sys

sys.path.append('./src/rstdoc')
from dcx import dorst

__version__ = '1.6.1'

def read(fname,separator='\n"""'):
    with open(os.path.join(os.path.dirname(__file__), fname),encoding='utf-8') as f:
        return f.read().split(separator)[1]

long_description = '\n'.join(["rstdoc\n======\n\n"
,open('readme.rst').read()
,read('src/rstdoc/dcx.py')
,read('src/rstdoc/dcx.py',separator="'''\\").split("'''")[0]
,read('src/rstdoc/fromdocx.py')
,read('src/rstdoc/listtable.py')
,read('src/rstdoc/untable.py')
,read('src/rstdoc/reflow.py')
,read('src/rstdoc/reimg.py')
,read('src/rstdoc/retable.py')
])

long_description = '\n'.join(dorst(long_description.splitlines()))

setup(name = 'rstdoc',
    version = __version__,
    description = 'rstdoc - support documentation in restructedText (rst)',
    license = 'MIT',
    author = 'Roland Puntaier',
    keywords=['Documentation'],
    author_email = 'roland.puntaier@gmail.com',
    url = 'https://github.com/rpuntaie/rstdoc',
    classifiers = [
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

    install_requires = ['pillow','pyx','pyfca','pygal','cairosvg','svgwrite',
        'stpl','pypandoc','sphinx','sphinx_bootstrap_theme','pyfakefs','pint'],
    extras_require = {'develop': ['mock','pytest-coverage'],'build':['waf']},
    long_description = long_description,
    packages=['rstdoc'],
    package_dir = {'rstdoc': 'src/rstdoc'},
    package_data = {'rstdoc':['reference.tex','reference.docx','reference.odt','wafw.py']},
    zip_safe=False,
    tests_require=['pytest','pytest-coverage','mock'],
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

