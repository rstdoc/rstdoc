API
---

.. code-block:: py

   import rstdoc.reimg as reimg


.. _`reimg.reimg`:

:reimg.reimg:

.. code-block:: py

   def reimg(data, prefix):

This renames all the images in the rst file converted from docx, to avoid

- images having strange names

- collision of image names from different docx

:param data: rst file read by f.read()
:param prefix: string prefix for images, should be derived from docx file name


.. _`reimg.main`:

:reimg.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstreimg| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

``rstfile`` is the file name

``in_place`` defaults to False

