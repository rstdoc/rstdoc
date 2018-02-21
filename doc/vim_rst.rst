vim_rst
=======

Usage
-----

In your ``.vimrc`` you create shortcuts, like for example::

  let mapleader = ","
  let maplocalleader = ","
  py3 << EOF
  from rstdoc import vim_rst
  EOF
  nnoremap <silent> <leader>etf :call ReformatTable()<CR>
  nnoremap <silent> <leader>etr :call ReflowTable()<CR>


Creating a new table
~~~~~~~~~~~~~~~~~~~~

1. Open a reStructuredText (.rst, .rest) file
2. Create some kind of table outline::

      This is paragraph text *before* the table.

      Column 1  Column 2
      Foo    Put two (or more) spaces as a field separator.
      |Bar|  Even very very long lines |like| these are fine, as long as you do not put in line endings here.
      Qux    This is the last line.

      This is paragraph text *after* the table.

2. Put your cursor somewhere in the table.
3. To create the table, press ``,etf``. The output will look something like this::

      This is paragraph text *before* the table.

      +----------+----------------------------------------------------------+
      | Column 1 | Column 2                                                 |
      +==========+==========================================================+
      | Foo      | Put two (or more) spaces as a field separator.           |
      +----------+----------------------------------------------------------+
      | |Bar|    | Even very very long lines |like| these are fine, as long |
      |          | as you do not put in line endings here.                  |
      +----------+----------------------------------------------------------+
      | Qux      | This is the last line.                                   |
      +----------+----------------------------------------------------------+

      This is paragraph text *after* the table.


Re-flowing an existing table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, you may have a column that contains enough data that your
table is a little hard to work with.  To fix that kind of problem,
you can define the column width you would prefer, and re-flow your table.

1. Change the number of "---" signs in the top row of your table to match
   the column widths you would prefer.
2. Put your cursor somewhere in the table.
3. Press ``,etr`` to re-flow the table.

.. .. Changes
.. .. -------
.. .. 
.. .. - Original code by Vincent Driessen (@nvie), lastly in 2015,
.. ..   probably BSD License. `<https://github.com/nvie/vim-rst-tables>`_.
.. .. - Updated for Python3 by Roland Puntaier (@rpuntaie) in 2016. 
.. .. - Again updated for Python3 by Walter Doekes (@wdoekes) in 2017. Added vendor
.. ..   dependencies for easier install. Added debian packaging rules.
.. .. - @wdoekes: Added support for ``|replacements|`` inside tables. From now on the
.. ..   column delimiters must have leading/trailing whitespace.
.. .. - @rpuntaie: Integrated the python code into rstdoc in 2018 and uploaded to pypi. 
.. ..   It can be used from Python and from vim in the described way.

