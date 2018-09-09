
%if version==1:

.. _`s1`:

:s{{id()}}: version one

It is possible to have more targets in the stpl but not vice versa.

%else:

.. _`s2`:

:s{{id()}}: version two

It is possible to have more targets in the stpl but not vice versa.
This can be used to have one source for slightly differing texts.

%end

The following is generated from a ``.stpl`` file before inclusion.

.. include:: normalfromstpl.rst

%include('subsub.rst.tpl')


