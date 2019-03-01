.. _`rstreflow`:

rstreflow
=========

rstreflow: shell command
reflow: rstdoc module

Reflow tables and paragraphs in a rst document produced from a docx.

Post-process a docx in this order::

    rstfromdocx doc.docx
    rstlisttable doc/doc.rst > doc/tmp.rst
    rstuntable doc/tmp.rst > doc/tmp1.rst
    rstreflow doc/tmp1.rst > doc/tmp2.rst
    rstreimg doc/tmp2.rst > doc/tmp3.rst
    rm doc/doc.rst
    mv doc/tmp3.rst doc/doc.rst
    rm doc/tmp*

Check the intermediate results.

Else one can also do inplace::

    rstfromdocx doc.docx
    rstlisttable -i doc/doc.rst
    rstuntable -i doc/doc.rst
    rstreflow -i doc/doc.rst
    rstreimg -i doc/doc.rst

.. note:: DOCX to RST using Pandoc

   ``rstfromdocx -lurg doc.rst`` converts a docx to RST and
   does all the post-processing in one step.

   It is adviced, though, to compare the output with the original and do some manual
   corrections here and there.

