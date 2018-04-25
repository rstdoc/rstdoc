SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = docxsmpl
SOURCEDIR     = .
BUILDDIR      = ../../build/doc
.PHONY: pdf docx help Makefile docxdir pdfdir index
docxdir: ${BUILDDIR}/docx
pdfdir: ${BUILDDIR}/pdf
MKDIR_P = mkdir -p
${BUILDDIR}/docx:
	${MKDIR_P} ${BUILDDIR}/docx
${BUILDDIR}/pdf:
	${MKDIR_P} ${BUILDDIR}/pdf
index:
	python ../rstdoc/dcx.py
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "  docx        to docx"
	@echo "  pdf         to pdf"
%: Makefile index
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
docx: docxdir index
	cat index.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/_trace.docx"
	cat sr.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/sr.docx"
	cat dd.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/dd.docx"
	cat tp.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/tp.docx"
	cat rstdoc.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/rstdoc.docx"
	stpl ra.rest.stpl ra.rest
	cat ra.rest _links_docx.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst -t docx -o "$(BUILDDIR)/docx/ra.docx"
pdf: pdfdir index
	cat index.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/_trace.pdf"
	cat sr.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/sr.pdf"
	cat dd.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/dd.pdf"
	cat tp.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g'  | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/tp.pdf"
	cat rstdoc.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g'  | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/rstdoc.pdf"
	stpl ra.rest.stpl ra.rest
	cat ra.rest _links_pdf.rst | sed -e's/^.. include:: _links_sphinx.rst//g' | pandoc -f rst --pdf-engine xelatex --number-sections -V papersize=a4 -V toc -V toc-depth=3 -V geometry:margin=2.5cm -o "$(BUILDDIR)/pdf/ra.pdf"
