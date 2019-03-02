
rstdcx, dcx.py
``````````````


.. _`test_lnkname`:

:test_lnkname:

Test the extraction of the name for different kinds of targets::

    header, figure, list-table, table,
    code-block, code, math, definition (:id:)

.. _`test_dcx_regex`:

:test_dcx_regex:

Test the regular expressions used in dcx.py.


.. _`test_rstincluded`:

:test_rstincluded:

Tests |dcx.rstincluded|.


.. _`test_init`:

:test_init:

Tests the initialization of a sample directory tree
with the ``--stpl tmp`` or ``--rest tmp`` options.


.. _`test_dcx_alone_samples`:

:test_dcx_alone_samples:

Tests calling ``rstdcx``/``dcx.py`` without parameters.


.. _`test_dcx_in_out`:

:test_dcx_in_out:

Tests calling ``rstdcx``/``dcx.py``
with in-file or standard in to standard out.


.. _`test_dcx_out_file`:

:test_dcx_out_file:

Tests calling ``rstdcx``/``dcx.py``
with in-file and out-file and out type parameter.


.. _`test_make_samples`:

:test_make_samples:

Tests building the samples with Makefile


.. _`test_waf_samples`:

:test_waf_samples:

Tests running Waf on the sample projects.


.. _`test_docparts_after`:

:test_docparts_after:

Tests |dcx.doc_parts| with different parameters for documentation extraction.

