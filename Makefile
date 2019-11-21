.PHONY: man test up check dist

test:
	py.test -vv --doctest-modules --cov=rstdoc --cov-report term-missing

doctest:
	waf configure && waf --docs sphinx_html --tests

man:
	python setup.py --print | pandoc -s -f rst -t man -o rstdoc.1

check:
	restview --long_description --strict

dist: man
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`



