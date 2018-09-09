#!/usr/bin/env python

# This Python script allows you to create tiny custom Waf distributions
# for each project you have. It's very similar to Gradle's wrapper scripts.
# Your mini Waf distribution can be customized using the variables at the top
# of the script.

from __future__ import print_function
import os
import sys
import platform
from shutil import move
try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

# Customize these variables to your needs.
WRAPPER_VERSION = '2.0.11'      # Version of Waf to use.
WAF_DIR         = 'waf'  # Where to store the Waf distribution.
WAF_PLUGINS     = [
    # To install a plugin with your Waf distribution, simply add a tuple
    # to this list with the plugin name and HTTP/HTTPS link to the plugin
    # file.
    #
    # For example:
    # ('eclipse', 'http://waf.googlecode.com/git/waflib/extras/eclipse.py'),
]

# Don't modify these! :P
WAF_FILE        = WAF_DIR + '/waf-' + WRAPPER_VERSION
USING_WINDOWS   = (platform.system() == 'Windows')

def create_init_files():
    '''Create __init__.py files in the Waf directory (and its parent directories)
       so plugins can be imported.'''
    dirs_to_check = WAF_DIR.split('/')
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
    move(filename, WAF_FILE)

def get_plugins():
    create_init_files()

    for tup in WAF_PLUGINS:
        name     = tup[0]
        filename = name + '.py'
        url      = tup[1]

        print('Downloading Waf plugin:', name + '...')
        urlretrieve(url, filename)
        move(filename, WAF_DIR)

def waf_exec():
    '''Execute argv arguments with the downloaded Waf release.'''
    if USING_WINDOWS:
        os.system('python.exe ' + WAF_FILE + ' ' + ' '.join(sys.argv[1:]))
    else:
        os.system('./' + WAF_FILE + ' ' + ' '.join(sys.argv[1:]))

if __name__ == '__main__':
    if not os.path.exists(WAF_DIR):
        print('Creating Waf directories...')
        os.makedirs(WAF_DIR)
        create_init_files()

    if os.path.exists(WAF_FILE):
        waf_exec()
    else:
        get_waf(WRAPPER_VERSION)
        get_plugins()
        if not USING_WINDOWS: os.system('chmod +x ' + WAF_FILE)
        waf_exec()
