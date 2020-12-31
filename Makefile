.PHONY: test doctest man check dist up devinstall tag

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
	py.test -vv --doctest-modules --cov=rstdoc --cov-report term-missing

doctest:
	waf configure && waf --docs sphinx_html --tests

man:
	python setup.py --print | pandoc -s -f rst -t man -o rstdoc.1

check:
	restview --long-description --strict

dist: man
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`

devinstall:
	sudo pip install -e .

tag: devinstall
	$(eval TAGMSG="v$(shell rstdoc --version | cut -d ' ' -f 2)")
	echo $(TAGMSG)
	git tag -s $(TAGMSG) -m"$(TAGMSG)"
	git verify-tag $(TAGMSG)
	git push origin $(TAGMSG) --follow-tags
