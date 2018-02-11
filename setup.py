#!/usr/bin/env python

#py.test --cov remdups --cov-report term-missing

#sudo python setup.py bdist_wheel
#twine upload ./dist/*.whl

from setuptools import setup
import platform
import os, os.path

__version__ = '1.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

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

    install_requires = [],
    extras_require = {'develop': ['pytest-coverage']},
    long_description = read('README.rst'),
    packages=['rstdoc'],
    include_package_data=False,
    zip_safe=False,
    tests_require=[],
    entry_points={
         'console_scripts': [
         'rstdoc = rstdoc.rstdoc:rstdoc',
              ]
      },

    )

