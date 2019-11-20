.PHONY: man test up check dist

test:
	py.test -vv --doctest-modules --cov=rstdoc --cov-report term-missing

man:
	./long_description.py | pandoc -s -f rst -t man -o rstdoc.1

check:
	./long_description.py --check

dist: man
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`


