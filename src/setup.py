#!/usr/bin/env python

#sudo pip install -e .
#py.test --cov rstdoc --cov-report term-missing

#sudo python setup.py bdist_wheel
#twine upload ./dist/*.whl

from setuptools import setup
import platform
import os, os.path

__version__ = '1.6.00'

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname),encoding='utf-8') as f:
        return f.read().split('\n"""')[1]

long_description = '\n'.join(["rstdoc\n======\n\n"
,open('readme.rst').read()
,read('rstdoc/dcx.py')
,read('rstdoc/fromdocx.py')
,read('rstdoc/listtable.py')
,read('rstdoc/untable.py')
,read('rstdoc/reflow.py')
,read('rstdoc/reimg.py')
,read('rstdoc/retable.py')
]).replace(
    '|rstdcx|','rstdcx_').replace(
    '|fromdocx.docx_rst_5|','``fromdocx.docx_rst_5``').replace(
    '|rstreflow|','rstreflow_')

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

    install_requires = ['pillow','pyx','pyfca','pygal','cairosvg','svgwrite','stpl','pypandoc','sphinx','sphinx_bootstrap_theme'],
    extras_require = {'develop': ['mock','pytest-coverage'],'build':['waf']},
    long_description = long_description,
    packages=['rstdoc'],
    #include_package_data=True,
    package_data={'rstdoc':['../reference.tex','../reference.docx','../readme.rst','../wafw.py']},
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

