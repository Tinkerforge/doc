
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-shell">Software</a> / Shell - API Bindings

.. _api_bindings_shell:

Shell - API Bindings
====================

The Shell bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your shell scripts. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``tinkerforge``, a Python script that acts as a shell command
* ``tinkerforge-bash-completion.sh``, a Bash completion script
* in ``examples/`` the examples for every Brick and Bricklet

The Shell bindings are based on the :ref:`Python bindings <api_bindings_python>`.


Requirements
------------

* Python 2.5 or newer with ``argparse`` module, Python 3 is also supported


.. _api_bindings_shell_install:

Installation
------------

The Shell bindings can be installed, but can also be used without installation.

To install the bindings copy the ``tinkerforge`` file to a folder that is in
the ``PATH``. For example, this folder on Linux and Mac OS X::

 /usr/local/bin/

On Windows the ``Scripts/`` folder of the Python installation is a good choice::

 C:\Python27\Scripts\

To be able to call the bindings directly on Windows you have to create a
``tinkerforge.bat`` file in the ``Scripts/`` folder with the following content::

 @"C:\Python27\python.exe" "C:\Python27\Scripts\tinkerforge"

If your Python is not installed in ``C:\Python27\`` then you have to adapt the
content of the ``tinkerforge.bat`` file accordingly.

Bash Completion
^^^^^^^^^^^^^^^

IF you're using Bash as your shell then you can use the Bash completion script
``tinkerforge-bash-completion.sh``. To install it copy the
``tinkerforge-bash-completion.sh`` file to the ``/etc/bash_completion.d/``
an reload the Bash completions with the following command::

 . /etc/bash_completion

The Bash completion for ``tinkerforge`` can complete options, UIDs, Brick and
Bricklet names as well as function and callback names.


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

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``example-configuration.sh`` file from the
``examples/brick/stepper/`` folder into a new folder::

 example_project/
  -> example-configuration.sh

If you did **not** install the bindings then you have to copy the
``tinkerforge`` file to the ``example_project/`` folder too::

 example_project/
  -> tinkerforge
  -> example-configuration.sh

To make the example find the non-installed ``tinkerforge`` file all occurrences
of the ``tinkerforge`` command in the ``example-configuration.sh`` file have
to be replaced by ``./tinkerforge``.

The example starts with a comment about changing the network address using the
``--host`` and ``--port`` option if it differs from ``localhost:4223``. If the
Stepper Brick is connected locally to USB then ``localhost`` and 4223 is
correct.

.. code-block:: bash

  # connects to localhost:4223 by default, use --host and --port to change it

To control a Stepper Brick that can be found at host ``foobar`` and port 5678
the examples has to be changed as follows: each occurrence of the
``tinkerforge`` command has to be replaced by this:

.. code-block:: bash

  tinkerforge --host foobar --port 5678

The ``UID`` value has to be changed to the UID of the connected Stepper Brick,
which you can figure out using Brick Viewer:

.. code-block:: bash

  # change to your UID
  uid=XYZ

Now you're ready to test this example::

 ./example-configuration.sh


.. _api_bindings_shell_links:

API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Shell_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Shell>
   Bricks <Bricks/Bricks_Shell>
   Bricklets <Bricklets/Bricklets_Shell>
