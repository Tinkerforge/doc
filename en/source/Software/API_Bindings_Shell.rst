
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-shell">Software</a> / Shell - API Bindings

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


.. _api_bindings_shell_install:

Installation
------------

TODO


Testing an Example
------------------

To test a Shell example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.





All examples are meant for typical Unix shells such as Bash. They will work
on Linux and Mac OS X as they are. There are Bash ports for Windows that allow
to run the examples unmodified, too.


.. _api_bindings_shell_links:

API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Shell_links.table
