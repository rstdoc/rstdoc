highlight_language = "none"
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    ]
numfig = False
smartquotes = False
default_role = 'math'
templates_path = ['_templates']
source_suffix = '.rest'
master_doc = 'index'
project = 'RST Documentation'
author = project+' Project Team'
copyright = '2018, '+author
version = '1.0'
release = '1.0.0'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
import sphinx_bootstrap_theme
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
latex_engine = 'xelatex'
tikz_transparent = True
tikz_proc_suite = 'ImageMagick'
tikz_tikzlibraries = 'arrows,snakes,backgrounds,patterns,matrix,shapes,fit,calc,shadows,plotmarks,intersections'
tikz_latex_preamble = r"""
\usepackage{unicode-math}
\usepackage{tikz}
%\usepackage{tikz-uml}
\usepackage{caption}
\captionsetup[figure]{labelformat=empty}
"""
latex_elements = {
'preamble':tikz_latex_preamble+r"\usetikzlibrary{""" + tikz_tikzlibraries+ '}'
}
latex_documents = [
    (master_doc, project.replace(' ','')+'.tex',project+' Documentation',author,'manual'),
]
#rstdoc
target_id_group = lambda targetid: targetid[0]
target_id_color={
    "meta":("m","white"),
    "ra":("r","lightblue"),
    "sr":("s","red"),
    "dd":("d","yellow"), 
    "tp":("t","green"),
    "rstdoc":("o","pink")}
html_extra_path=["_images/_traceability_file.svg"] #IF YOU DID .. include:: _traceability_file.rst
pandoc_doc_optref={'latex': '--template reference.tex',
                 'html': {},#each can also be dict of file:template
                 'pdf': '--template reference.tex',
                 'docx': '--reference-doc reference.docx',
                 'odt': '--reference-doc reference.odt'
                 }
latex_pdf = ['--listings','--number-sections','--pdf-engine','xelatex','-V','titlepage','-V','papersize=a4','-V','toc','-V','toc-depth=3','-V','geometry:margin=2.5cm']
pandoc_opts = {'pdf':latex_pdf,'latex':latex_pdf,'docx':[],'odt':[],'html':['--mathml','--highlight-style','pygments']}
rst2_opts = {'odt':['--leave-comments'],'html':['--leave-comments']}#see ``rst2html.py --help`` or ``rst2odt.py --help``

