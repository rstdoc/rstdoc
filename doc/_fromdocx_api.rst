API
---


.. code-block:: py

   import rstdoc.fromdocx as fromdocx


.. _`fromdocx.extract_media`:

:fromdocx.extract_media:

.. code-block:: py

   def extract_media(adocx):

extract media files from a docx file to a subfolder named after the docx

:param adocx: docx file name


.. _`fromdocx.main`:

:fromdocx.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstfromdocx| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

listtable, untable, reflow, reimg default to False.

returns: The file name of the generated file.


.. _`fromdocx.docx_rst_5`:

:fromdocx.docx_rst_5:

.. code-block:: py

   def docx_rst_5(docx ,rename ,sentence=True):

Creates 5 rst files:

- without postprocessing: rename/rename.rest
- with listtable postprocessing: rename/rename_l.rest
- with untable postprocessing: rename/rename_u.rest
- with reflow postprocessing: rename/rename_r.rest
- with reimg postprocessing: rename/rename_g.rest

:param docx: the docx file name
:param rename: the new name to give to the converted files (no extension)
:param sentence: split sentences into new lines (reflow)

