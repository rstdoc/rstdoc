project = 'rstdoc'
author = 'Roland Puntaier'
copyright = '2018, '+author
version = '1.6.8'
release = '1.6.8.0'

try:
    import sphinx_bootstrap_theme
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
    html_theme = 'bootstrap'
except:
    pass

#these are enforced by rstdoc, but you need to keep them here if you call sphinx-build directly
numfig = 0
smartquotes = 0
source_suffix = '.rest'
templates_path = []
language = None
highlight_language = "none"
default_role = 'math'
pygments_style = 'sphinx'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'

import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if not on_rtd:

    latex_engine = 'xelatex'
    
    #You can postprocess pngs. Here an example. default: png_post_processor = None
    def png_post_processor(filename):
        from PIL import Image, ImageChops
        def trim(im):
            bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
            diff = ImageChops.difference(im, bg)
            diff = ImageChops.add(diff, diff, 2.0, -100)
            bbox = diff.getbbox()
            if bbox:
                return im.crop(bbox)
        im = Image.open(filename)
        im = trim(im)
        im.save(filename)
        return filename
    
    #remove the following, if you don't change them, because they are default anyway
    latex_elements = {'preamble':r"""
    \usepackage{pgfplots}
    \usepackage{unicode-math}
    \usepackage{tikz}
    \usepackage{caption}
    \captionsetup[figure]{labelformat=empty}
    \usetikzlibrary{arrows,snakes,backgrounds,patterns,matrix,shapes,fit,calc,shadows,plotmarks,intersections}
    """
    }
    
    #new in rstdcx/dcx/py
    tex_wrap = r"""
    \documentclass[12pt,tikz]{standalone}
    \usepackage{amsmath}
    """+latex_elements['preamble']+r"""
    \pagestyle{empty}
    \begin{document}
    %s
    \end{document}
    """
    DPI = 600
    target_id_group = lambda targetid: targetid[0]
    target_id_color={"ra":("r","lightblue"), "sr":("s","red"), "dd":("d","yellow"), "tp":("t","green")}
    html_extra_path=["_traceability_file.svg"] #relative to conf.py
    pandoc_doc_optref={'latex': '--template ../reference.tex',
                     'html': {},#each can also be dict of file:template
                     'pdf': '--template ../reference.tex',
                     'docx': '--reference-doc ../reference.docx',
                     'odt': '--reference-doc ../reference.odt'
                     }
    _pandoc_latex_pdf = ['--listings','--number-sections','--pdf-engine','xelatex','-V','titlepage','-V','papersize=a4','-V','toc','-V','toc-depth=3','-V','geometry:margin=2.5cm']
    pandoc_opts = {'pdf':_pandoc_latex_pdf,'latex':_pandoc_latex_pdf,'docx':[],'odt':[],'html':['--mathml','--highlight-style','pygments']}
    rst_opts = { #http://docutils.sourceforge.net/docs/user/config.html
                'strip_comments':True
                ,'report_level':3
                ,'raw_enabled':True
                }
    name_from_directive = lambda directive,count: directive[0].upper()+directive[1:]+' '+str(count)
