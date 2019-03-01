
.. _`rstlisttable`:

rstlisttable
============

rstlisttable: shell command
listable: rstdoc module

Convert RST grid tables to list-tables.

#. Convert grid tables in a file to list-tables. The result is output to stdout::

    $ listtable.py input.rst

#. Convert several files::

    $ listtable.py input1.rst input2.rst
    $ listtable.py *.rst

#. Use pipe (but ``cat`` might not keep the encoding)::

    $ cat in.rst | listtable.py -  | untable.py - > out.rst

Options
-------
-j, --join       e.g.002. Join method per column: 0="".join; 1=" ".join; 2="\\n".join

