API
---

.. code-block:: py

   import rstdoc.reflow as reflow


.. _`reflow.reflowparagraph`:

:reflow.reflowparagraph:

.. code-block:: py

   def reflowparagraph(p, sentence=False):

Reflow a paragaph using ``textwarp.wrap``. Possibly split sentences.

:param p: paragraph
:param sentence: if True lines are split at the end of the sentence


.. _`reflow.reflowparagraphs`:

:reflow.reflowparagraphs:

.. code-block:: py

   def reflowparagraphs(lns, sentence=False):

Reflow paragraphs using |reflow.reflowparagraph|.

:param lns: lines from rst file
:param sentence: if True lines are split at the end of the sentence


.. _`reflow.nostrikeout`:

:reflow.nostrikeout:

.. code-block:: py

   def nostrikeout(lns):

Removes ``[strikeout:xxx]``

:param lns: lines from rst file


.. _`reflow.rmextrablankline`:

:reflow.rmextrablankline:

.. code-block:: py

   def rmextrablankline(lns):

Remove excessive blank lines.

:param lns: lines from rst file


.. _`reflow.no3star`:

:reflow.no3star:

.. code-block:: py

   def no3star(lns):

Removes three stars, as they are not supported by docutils.

:param lns: lines from rst file


.. _`reflow.noblankend`:

:reflow.noblankend:

.. code-block:: py

   def noblankend(lns):

Removes blanks at the end of the line.

:param lns: lines from rst file


.. _`reflow.reflowrow`:

:reflow.reflowrow:

.. code-block:: py

   class reflowrow():

This replaces |listtable.row_to_listtable| in |listtable.gridtable| to reflow a grid table.


.. _`reflow.reflow`:

:reflow.reflow:

.. code-block:: py

   def reflow(lns, join='1', sentence=False):

Combines all rst corrections of this file.

:param lns: lines from rst file
:param join: 0 no space, 1 with space, 2 keep as-is
:param sentence: if True lines are split at the end of the sentence


.. _`reflow.main`:

:reflow.main:

.. code-block:: py

   def main(**args):

This corresponds to the |rstreflow| shell command.

:param args: Keyword arguments. If empty the arguments are taken from ``sys.argv``.

``rstfile`` is the file name

``in_place`` defaults to False

