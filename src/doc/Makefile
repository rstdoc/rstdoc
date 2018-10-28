SPHINXOPTS  = -c .
SPHINXBLD   = sphinx-build
SPHINXPROJ  = sample
SRCDIR      = ./
DCXPATH     = ../rstdoc
BLDDIR      = ../../build/doc
STPLS       = $(wildcard $(SRCDIR)*.stpl)
STPLTGTS    = $(STPLS:%.stpl=%)
SRCS        = $(filter-out $(SRCDIR)index.rest,$(wildcard $(SRCDIR)*.rest))
SRCSTPL     = $(wildcard $(SRCDIR)*.rest.stpl)
IMGS        = \
	$(wildcard $(SRCDIR)*.pyg)\
	$(wildcard $(SRCDIR)*.eps)\
	$(wildcard $(SRCDIR)*.tikz)\
	$(wildcard $(SRCDIR)*.svg)\
	$(wildcard $(SRCDIR)*.uml)\
	$(wildcard $(SRCDIR)*.dot)\
	$(wildcard $(SRCDIR)*.eps.stpl)\
	$(wildcard $(SRCDIR)*.tikz.stpl)\
	$(wildcard $(SRCDIR)*.svg.stpl)\
	$(wildcard $(SRCDIR)*.uml.stpl)\
	$(wildcard $(SRCDIR)*.dot.stpl)
PNGS=$(subst $(SRCDIR),$(SRCDIR)_images/,\
	$(patsubst %.eps,%.png,\
	$(patsubst %.pyg,%.png,\
	$(patsubst %.tikz,%.png,\
	$(patsubst %.svg,%.png,\
	$(patsubst %.uml,%.png,\
	$(patsubst %.dot,%.png,\
	$(patsubst %.eps.stpl,%.png,\
	$(patsubst %.dot.stpl,%.png,\
	$(patsubst %.tikz.stpl,%.png,\
	$(patsubst %.svg.stpl,%.png,\
	$(patsubst %.uml.stpl,%.png,$(IMGS)))))))))))))
DOCXS = $(subst $(SRCDIR),$(BLDDIR)/docx/,$(SRCS:%.rest=%.docx))\
	$(subst $(SRCDIR),$(BLDDIR)/docx/,$(SRCSTPL:%.rest.stpl=%.docx))
PDFS  = $(subst $(SRCDIR),$(BLDDIR)/pdf/,$(SRCS:%.rest=%.pdf))\
	$(subst $(SRCDIR),$(BLDDIR)/pdf/,$(SRCSTPL:%.rest.stpl=%.pdf))
.PHONY: docx help Makefile docxdir pdfdir stpl index imgs
stpl: $(STPLTGTS)
%:%.stpl
	@cd $(SRCDIR) && stpl "$(<F)" "$(@F)"
imgs: $(PNGS)
$(SRCDIR)_images/%.png:$(SRCDIR)%.pyg
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
$(SRCDIR)_images/%.png:$(SRCDIR)%.eps
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
$(SRCDIR)_images/%.png:$(SRCDIR)%.tikz
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
$(SRCDIR)_images/%.png:$(SRCDIR)%.svg
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
$(SRCDIR)_images/%.png:$(SRCDIR)%.uml
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
$(SRCDIR)_images/%.png:$(SRCDIR)%.dot
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py $(<F)
docxdir: ${BLDDIR}/docx
pdfdir: ${BLDDIR}/pdf
MKDIR_P = mkdir -p
${BLDDIR}/docx:
	@${MKDIR_P} ${BLDDIR}/docx
${BLDDIR}/pdf:
	@${MKDIR_P} ${BLDDIR}/pdf
index:
	@python $(DCXPATH)/dcx.py
help:
	@$(SPHINXBLD) -M help "$(SRCDIR)" "$(BLDDIR)" $(SPHINXOPTS) $(O)
	@echo "  docx        to docx"
	@echo "  pdf         to pdf"
#http://www.sphinx-doc.org/en/stable/usage/builders/
html dirhtml singlehtml htmlhelp qthelp applehelp devhelp epub latex text man texinfo pickle json xml pseudoxml: Makefile index stpl imgs
	@$(SPHINXBLD) -M $@ "$(SRCDIR)" "$(BLDDIR)" $(SPHINXOPTS) $(O)
docx:  docxdir index stpl imgs $(DOCXS)
$(BLDDIR)/docx/%.docx:$(SRCDIR)%.rest
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py "$(<F)" "$@"
pdf: pdfdir index stpl imgs $(PDFS)
$(BLDDIR)/pdf/%.pdf:$(SRCDIR)%.rest
	@cd $(SRCDIR) && python $(DCXPATH)/dcx.py "$(<F)" "$@"
