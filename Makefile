.PHONY: test
test:
	rm -rf build
	rm -rf doc/build
	rm -rf doc/dcx.py
	rm -rf doc/doc/
	rm -rf doc/docutils.conf
	rm -rf doc/reference.docx
	rm -rf doc/reference.odt
	rm -rf doc/reference.tex
	rm -rf doc/waf
	rm -rf doc/waf.bat
	rm -rf doc/wafw.py
	rm -rf doc/wscript
	rm -rf doc/_links_*
	rm -rf doc/_images
	rm -rf doc/_traceability_*
	type waf && py.test -vv --doctest-modules --cov=rstdoc --cov-report term-missing

.PHONY: doc
doc:
	waf configure --docs sphinx_html,rst_html,rst_odt,html,odt,docx
	waf
	waf --docs pdf

.PHONY: doctest
doctest:
	waf configure && waf --docs sphinx_html --tests

.PHONY: man
man:
	python setup.py --print | pandoc -s -f rst -t man -o rstdoc.1

.PHONY: check
check:
	/usr/bin/man -l rstdoc.1
	restview --long-description --strict

.PHONY: dist
dist: man
	sudo python setup.py bdist_wheel

.PHONY: up
up:
	twine upload dist/`ls dist -rt | tail -1`

.PHONY: devinstall
devinstall:
	sudo pip install -e .

.PHONY: tag
tag: devinstall
	$(eval TAGMSG="v$(shell rstdoc --version | cut -d ' ' -f 2)")
	echo $(TAGMSG)
	git tag -s $(TAGMSG) -m"$(TAGMSG)"
	git verify-tag $(TAGMSG)
	git push origin $(TAGMSG) --follow-tags
