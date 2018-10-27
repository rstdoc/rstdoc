#!/usr/bin/env python

# This Python script allows you to create tiny custom Waf distributions
# for each project you have. It's very similar to Gradle's wrapper scripts.
# Your mini Waf distribution can be customized using the variables at the top
# of the script.

from __future__ import print_function
import os
import sys
import platform
import re
from shutil import move, copy
try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

# Customize these variables to your needs.
WAFDIR         = 'WAFDIR'    # Where to store the Waf distribution.
WAF_PLUGINS     = [
    # To install a plugin with your Waf distribution, simply add a tuple
    # to this list with the plugin name and HTTP/HTTPS link to the plugin
    # file.
    #
    # For example:
    # ('eclipse', 'http://waf.googlecode.com/git/waflib/extras/eclipse.py'),
]

# Don't modify these! :P
WAF_FILE        = lambda: WAFDIR + '/waf-' + WRAPPER_VERSION
USING_WINDOWS   = (platform.system() == 'Windows')

def set_version_by_dir(adir):
    global WRAPPER_VERSION
    for wafx in os.listdir(adir):
        _mo = re.search(r'waf-(\d.\d.\d\d)',wafx)
        if _mo:
            WRAPPER_VERSION = _mo.group(1)
            return True
    return False

def init_waf_version():
    global WRAPPER_VERSION
    if not os.path.exists(WAFDIR):
        if 'WAFDIR' in os.environ and set_version_by_dir(os.environ['WAFDIR']):
            existing_waf = os.path.join(os.environ['WAFDIR'],'waf-'+WRAPPER_VERSION)
            try:
                if not os.path.exists(WAFDIR):
                    os.makedirs(WAFDIR)
                copy(existing_waf, WAF_FILE())
                print('Copied from ', existing_waf)
                return
            except Exception as e:
                print('Warning: ', e)
        try:
            _url = urlretrieve('https://www.waf.io/pub/release/')
            with open(_url[0]) as f:
                WRAPPER_VERSION = re.search(r'waf-(\d.\d.\d\d)',f.read()).groups(1)[0]
        except: 
            WRAPPER_VERSION = '2.0.12' 
    else:
        set_version_by_dir(WAFDIR)

init_waf_version()

def create_init_files():
    '''Create __init__.py files in the Waf directory (and its parent directories)
       so plugins can be imported.'''
    dirs_to_check = WAFDIR.split('/')
    i = 0
    while i < len(dirs_to_check):
        dir_to_check = dirs_to_check[i]
        parent_dirs  = '/'.join(dirs_to_check[:i])
        if i == 0:
            init_file = dir_to_check + '/__init__.py'
        else:
            init_file = parent_dirs + '/' + dir_to_check + '/__init__.py'

        if not os.path.isfile(init_file):
            print('Creating', init_file, 'for importing plugins...')
            open(init_file, 'a').close()

        i += 1

def get_waf(version):
    '''Download a specific Waf release.'''
    filename = 'waf-' + version
    url      = 'http://www.waf.io/pub/release/' + filename

    print('Downloading', filename + '...')
    urlretrieve(url, filename)
    if 'WAFDIR' in os.environ:
        copy(filename,os.path.join(os.environ['WAFDIR'],'waf-'+WRAPPER_VERSION))
    move(filename, WAF_FILE())

def get_plugins():
    create_init_files()

    for tup in WAF_PLUGINS:
        name     = tup[0]
        filename = name + '.py'
        url      = tup[1]

        print('Downloading Waf plugin:', name + '...')
        urlretrieve(url, filename)
        move(filename, WAFDIR)

def waf_exec():
    '''Execute argv arguments with the downloaded Waf release.'''
    if USING_WINDOWS:
        os.system('python.exe ' + WAF_FILE() + ' ' + ' '.join(sys.argv[1:]))
    else:
        os.system('./' + WAF_FILE() + ' ' + ' '.join(sys.argv[1:]))

if __name__ == '__main__':
    if not os.path.exists(WAFDIR):
        print('Creating Waf directories...')
        os.makedirs(WAFDIR)
        create_init_files()

    if os.path.exists(WAF_FILE()):
        waf_exec()
    else:
        get_waf(WRAPPER_VERSION)
        get_plugins()
        if not USING_WINDOWS: os.system('chmod +x ' + WAF_FILE())
        waf_exec()
