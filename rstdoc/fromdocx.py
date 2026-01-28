#!/usr/bin/env python
# encoding: utf-8

# def gen_head(lns,**kw):
#    b,e = list(rindices('^"""',lns))[:2]
#    return lns[b+1:e]
# def gen_head(lns,**kw)
# def gen_api(lns,**kw):
#    yield from doc_parts(lns,signature='py',prefix='fromdocx.')
# def gen_api

from .reimg import main as reimg
from .reflow import main as reflow
from .untable import main as untable
from .listtable import main as listtable
from .dcx import example_rest_tree, rindices
from pathlib import Path
import time
import re
from glob import glob
import shutil
import os
import pypandoc
from zipfile import ZipFile
from rstdoc import __version__

"""
.. _`rstfromdocx`:

rstfromdocx
===========

| rstfromdocx: shell command
| fromdocx: rstdoc module

Convert DOCX to RST in a subfolder of current dir, named after the DOCX file.
It also creates ``conf.py``, ``index.py`` and ``Makefile``
and copies ``dcx.py`` into the folder.

See |rstdcx| for format conventions for the RST.

There are options to post-process through::

    --listtable (--join can be provided)
    --untable
    --reflow (--sentence True,  --join 0)
    --reimg

``rstfromdocx -lurg`` combines all of these.

To convert more DOCX documents into the same
RST documentation folder, proceed like this:

- rename/copy the original DOCX to the name you want for the ``.rest`` file
- run ``rstfromdocx -lurg doc1.docx``; instead of -lurg use your own options
- check the output in the ``doc1`` subfolder
- repeat the previous 2 steps with the next DOCX files
- create a new folder, e.g. ``doc``
- merge all other folders into that new folder

``fromdocx.docx_rst_5`` creates 5 different rst files with different postprocessing.

See |rstreflow| for an alternative proceeding.


"""



'''
API
---


.. code-block:: py

   import rstdoc.fromdocx as fromdocx

'''


def _mkdir(fn):
    try:
        os.mkdir(fn)
    except:
        pass


def _rstname(fn):
    return os.path.splitext(os.path.split(fn)[1])[0]


def _prj_name(fn):
    m = re.match(r'[\s\d\W]*([^\s\W]*).*', _rstname(fn))
    return m.group(1).strip('_').replace(' ', '')


def _fldrhere(n):
    return os.path.abspath(os.path.split(os.path.splitext(n)[0])[1])


def extract_media(adocx):
    '''
    extract media files from a docx file to a subfolder named after the docx

    :param adocx: docx file name

    '''

    zf = ZipFile(adocx)
    pwd = os.getcwd()
    try:
        fnn = _fldrhere(adocx)
        _mkdir(fnn)
        media = [x for x in zf.infolist() if 'media/' in x.filename]
        os.chdir(fnn)
        _mkdir('media')
        os.chdir('media')
        for m in media:
            #m = media[0]
            zf.extract(m)
            try:
                shutil.move(m.filename, os.getcwd())
            except:
                pass
        try:
            for f in glob('word/media/*'):
                os.remove(f)
            os.rmdir('word/media')
            os.rmdir('word')
        except:
            pass
    finally:
        os.chdir(pwd)


def _docxrest(adocx):
    # returns file name of ``.rest`` file.
    _, frm = os.path.split(adocx)
    fnrst = os.path.splitext(frm)[0]
    fnrst = os.path.join(_fldrhere(adocx), fnrst + '.rest')
    return fnrst


def _write_confpy(adocx):
    # Takes the conf.py from the ``example_rest_tree`` in ``rstdoc.dcx``.
    confpy = re.split(r'\s*.\s*Makefile', example_rest_tree.split('conf.py')[1])[0]
    pn = _prj_name(adocx)
    confpy = confpy.replace('docxsample', pn).replace('2017',
                                                      time.strftime('%Y'))
    lns = confpy.splitlines(True)
    s = re.search(r'\w', lns[1]).span(0)[0]
    confpy = ''.join([l[s:] for l in lns])
    fnn = _fldrhere(adocx)
    cpfn = os.path.normpath(os.path.join(fnn, 'conf.py'))
    if os.path.exists(cpfn):
        return
    with open(cpfn, 'w', encoding='utf-8') as f:
        f.write(confpy)


def _write_index(adocx):
    # Adds a the generated .rest to ``toctree`` in index.rest or generates new index.rest.
    fnn = _fldrhere(adocx)
    ifn = os.path.normpath(os.path.join(fnn, 'index.rest'))
    rst = _rstname(adocx) + '.rest'
    prjname = _prj_name(adocx)
    hp = '=' * len(prjname)
    if os.path.exists(ifn):
        with open(ifn, 'r') as f:
            lns = f.readlines()
    else:
        lns = [
            x + '\n' for x in
            ['.. vim: syntax=rst', '', hp, prjname, hp, '', '.. toctree::']
        ]
    itoc = list(rindices('toctree', lns))[0]
    lns = lns[:itoc + 1] + ['    ' + rst + '\n'] + lns[itoc + 1:]
    with open(ifn, 'w') as f:
        f.writelines(lns)


def _write_makefile(adocx):
    # Takes the Makefile from the ``example_rest_tree`` in ``rstdoc.dcx``.
    mf = re.split(r'\s\s+__code__', re.split('\s\sMakefile', example_rest_tree)[1])[0]
    lns = mf.splitlines(True)
    s = re.search(r'\w', lns[1]).span(0)[0]
    lns = [l[s:] for l in lns]
    rst = _rstname(adocx)
    idoc = list(rindices('^docx:', lns))[0]
    ipdf = list(rindices('^pdf:', lns))[0]
    doce = lns[idoc + 1].replace('sr', rst)
    pdfe = lns[ipdf + 1].replace('sr', rst)
    lns = lns[:idoc + 1] + [lns[ipdf]]
    fnn = _fldrhere(adocx)
    mffn = os.path.normpath(os.path.join(fnn, 'Makefile'))
    if os.path.exists(mffn):
        with open(mffn, 'r') as f:
            lns = f.readlines()
    idoc = list(rindices('^docx:', lns))[0]
    ipdf = list(rindices('^pdf:', lns))[0]
    lns = lns[:idoc + 1] + [doce] + lns[idoc + 1:ipdf + 1] + [
        pdfe
    ] + lns[ipdf + 1:]
    with open(mffn, 'w', encoding='utf-8') as f:
        f.writelines(lns)


def _write_dcx(adocx):
    # Writes the dcx.py into the folder generated for the docx.
    dcxfile = os.path.join(
        os.path.split(str(Path(__file__).resolve()))[0], 'dcx.py')
    shutil.copy2(dcxfile, _fldrhere(adocx))

## The below function converts notes, admonitions etc into their respective .rst directives

def process_rst_admonitions(rst_text):
    """
    Correctly converts multi-line admonitions (e.g., "**Note**: ...") into properly 
    indented RST directives. Removes bold/italic markers added by Pandoc.

    Args:
        rst_text (str): The input RST text generated from Pandoc.

    Returns:
        str: The processed RST text with correctly formatted multi-line directives.
    """
    directive_mappings = {
        "note": "note",
        "see also": "seealso", 
        "attention": "attention",
        "caution": "caution",
        "error": "error",
        "danger": "danger",
        "hint": "hint",
        "tip": "tip",
        "important": "important",
        "warning": "warning",
    }

    # More flexible regex pattern to match various formatting
    keywords_pattern = "|".join(re.escape(key) for key in directive_mappings.keys())
    
    # Pattern to match the directive line
    pattern = re.compile(
        rf"^\s*[\*_]*\s*({keywords_pattern})\s*[\*_]*\s*:\s*(.*)",
        re.IGNORECASE
    )

    # Split into paragraphs but preserve empty lines
    paragraphs = re.split(r'\n\s*\n', rst_text)
    processed_paragraphs = []

    for paragraph in paragraphs:
        if not paragraph.strip():
            processed_paragraphs.append(paragraph)
            continue

        lines = paragraph.split('\n')
        first_line = lines[0].strip()
        match = pattern.match(first_line)

        if match:
            # Extract the keyword and normalize it
            keyword = match.group(1).lower().strip()
            rest_of_first_line = match.group(2).strip()
            
            # Remove ONLY leading/trailing ** or * markers (not internal ones)
            # This handles: "** This is text **" -> "This is text"
            while rest_of_first_line.startswith('**') or rest_of_first_line.startswith('*'):
                if rest_of_first_line.startswith('**'):
                    rest_of_first_line = rest_of_first_line[2:].lstrip()
                else:
                    rest_of_first_line = rest_of_first_line[1:].lstrip()
            
            while rest_of_first_line.endswith('**') or rest_of_first_line.endswith('*'):
                if rest_of_first_line.endswith('**'):
                    rest_of_first_line = rest_of_first_line[:-2].rstrip()
                else:
                    rest_of_first_line = rest_of_first_line[:-1].rstrip()
            
            # Get the directive name
            directive = directive_mappings.get(keyword, "note")

            # Create the directive line
            if rest_of_first_line:
                # If there's content on the first line, include it
                new_lines = [f".. {directive}:: {rest_of_first_line}"]
            else:
                # If no content on first line, just create the directive
                new_lines = [f".. {directive}::"]
            
            # Process remaining lines with proper indentation
            for line in lines[1:]:
                if line.strip():  # Non-empty line
                    new_lines.append(f"   {line.rstrip()}")
                else:  # Empty line - preserve but with minimal indentation
                    new_lines.append("   ")

            processed_paragraphs.append('\n'.join(new_lines))
        else:
            # This paragraph is not a directive, leave unchanged
            processed_paragraphs.append(paragraph)
    
    return '\n\n'.join(processed_paragraphs)

def main(**args):
    '''
    This corresponds to the |rstfromdocx| shell command.

    :param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

    listtable, untable, reflow, reimg default to False.

    returns: The file name of the generated file.

    '''

    import argparse

    if not args:
        parser = argparse.ArgumentParser(
            description=
            '''Convert DOCX to RST using Pandoc and additionally copy the images and helper files.'''
        )
        parser.add_argument('--version', action='version', version = __version__)
        parser.add_argument('docx', action='store', help='DOCX file')
        parser.add_argument(
            '-l',
            '--listtable',
            action='store_true',
            default=False,
            help='''postprocess through rstlisttable''')
        parser.add_argument(
            '-u',
            '--untable',
            action='store_true',
            default=False,
            help='''postprocess through rstuntable''')
        parser.add_argument(
            '-r',
            '--reflow',
            action='store_true',
            default=False,
            help='''postprocess through rstreflow''')
        parser.add_argument(
            '-g',
            '--reimg',
            action='store_true',
            default=False,
            help='''postprocess through rstreimg''')
        parser.add_argument(
            '-j',
            '--join',
            action='store',
            default='012',
            help=
            '''e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join'''
        )
        args = parser.parse_args().__dict__

    adocx = args['docx']
    extract_media(adocx)
    fnrst = _docxrest(adocx)
    rst = pypandoc.convert_file(adocx, 'rst', 'docx')
    rst = process_rst_admonitions(rst)  # ← Added this line
    with open(fnrst, 'w', encoding='utf-8', newline='\n') as f:
        f.write('.. vim: syntax=rst\n\n')
        f.writelines([x + '\n' for x in rst.splitlines()])
    _write_confpy(adocx)
    _write_index(adocx)
    _write_makefile(adocx)
    _write_dcx(adocx)

    if 'listtable' not in args:
        args['listtable'] = False
    if 'untable' not in args:
        args['untable'] = False
    if 'reflow' not in args:
        args['reflow'] = False
    if 'reimg' not in args:
        args['reimg'] = False

    if 'join' not in args:
        args['join'] = '012'

    for a in 'listtable untable reflow reimg'.split():
        if args[a]:
            args['in_place'] = True
            args['sentence'] = True
            if a == 'reflow':
                args['join'] = '0'
            args['rstfile'] = [argparse.FileType('r', encoding='utf-8')(fnrst)]
            eval(a)(**args)

    return fnrst


def docx_rst_5(docx ,rename ,sentence=True):
    '''
    Creates 5 rst files:

    - without postprocessing: rename/rename.rest
    - with listtable postprocessing: rename/rename_l.rest
    - with untable postprocessing: rename/rename_u.rest
    - with reflow postprocessing: rename/rename_r.rest
    - with reimg postprocessing: rename/rename_g.rest

    :param docx: the docx file name
    :param rename: the new name to give to the converted files (no extension)
    :param sentence: split sentences into new lines (reflow)

    '''

    shutil.copy2(docx, rename + ".docx")
    rstfn = main(docx=rename + ".docx")
    r, _ = os.path.splitext(rstfn)
    shutil.copy2(rstfn, r + '_l.rest')
    listtable(rstfile=r + '_l.rest', in_place=True)
    shutil.copy2(r + '_l.rest', r + '_u.rest')
    untable(rstfile=r + '_u.rest', in_place=True)
    shutil.copy2(r + '_u.rest', r + '_r.rest')
    reflow(rstfile=r + '_r.rest', in_place=True, sentence=sentence)
    shutil.copy2(r + '_r.rest', r + '_g.rest')
    reimg(rstfile=r + '_g.rest', in_place=True)


if __name__ == '__main__':
    main()

# vim: ts=4 sw=4 sts=4 et noai nocin nosi
