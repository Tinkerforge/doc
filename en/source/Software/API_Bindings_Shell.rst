
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - API Bindings

.. _api_bindings_shell:

Shell - API Bindings
====================

**Requirements**: Python 2.5 or newer with argparse module, Python 3 is also supported

The Shell bindings (:ref:`download <downloads_bindings_examples>`) consist of
a Python script to interact with all
Tinkerforge Bricks and Bricklets (``tinkerforge``), a corresponding Bash
Completion script (``tinkerforge-bash-completion.sh``) and all available Shell
examples (in ``examples/``).

To get Bash Completion to work the ``tinkerforge`` script has to be in ``PATH``.
For example by copying it to ``/usr/local/bin/``. The Bash Completion script
``tinkerforge-bash-completion.sh`` has to be in ``/etc/bash_completion.d/``.
Bash Completion can then be reloaded by::

 . /etc/bash_completion


Testing an Example
------------------

All examples are meant for typical Unix shells such as Bash. They will work
on Linux and Mac OS X as they are. There are Bash ports for Windows that allow
to run the examples unmodified, too.


More Examples and Projects
--------------------------

All the small examples contained in the ZIP file of the bindings can also be
found in the API documentation of the :ref:`Bricks <product_overview_bricks>` and
:ref:`Bricklets <product_overview_bricklets>`.

Further project descriptions can be found in the :ref:`kits <index_kits>` section.

.. FIXME: add a list with direct links here
