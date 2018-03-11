#!/usr/bin/env python

#py.test --cov rstdoc --cov-report term-missing

#sudo python setup.py bdist_wheel
#twine upload ./dist/*.whl

from setuptools import setup
import platform
import os, os.path

__version__ = '1.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),encoding='utf-8').read()

long_description = '\n'.join([
read('readme.rst')
,read('rstdoc/dcx.py').split('\n"""')[1]
,read('rstdoc/fromdocx.py').split('\n"""')[1]
,read('rstdoc/listtable.py').split('\n"""')[1]
,read('rstdoc/untable.py').split('\n"""')[1]
,read('rstdoc/reflow.py').split('\n"""')[1]
,read('rstdoc/reimg.py').split('\n"""')[1]
,read('rstdoc/retable.py').split('\n"""')[1]
])

setup(name = 'rstdoc',
    version = __version__,
    description = 'rstdoc - support documentation in restructedText (rst)',
    license = 'MIT',
    author = 'Roland Puntaier',
    keywords=['Documentation'],
    author_email = 'roland.puntaier@gmail.com',
    url = 'https://github.com/rpuntaie/rstdoc',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Topic :: Utilities',
        ],

    install_requires = ['stpl','pypandoc','sphinx','sphinxcontrib-tikz','sphinx_bootstrap_theme'],
    extras_require = {'develop': ['mock','pytest-coverage'],'build':['waf']},
    long_description = long_description,
    packages=['rstdoc'],
    include_package_data=True,
    package_data={'rstdoc':['rstdoc/reference.tex']},
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

