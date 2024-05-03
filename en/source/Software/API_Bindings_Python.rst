
.. _api_bindings_python:

Python - API Bindings
=====================

The Python bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Python scripts. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``source/`` the source code of the bindings (including a ``setup.py``
  install script)
* in ``examples/`` the examples for every Brick and Bricklet

Requirements
------------

* Python 2.6 or newer, Python 3 is also supported

.. _api_bindings_python_install:

Installation
------------

There are three ways to install the Python bindings:
from our :ref:`APT repository <api_bindings_python_install_apt>` for Debian
based Linux distributions or
from :ref:`PyPI <api_bindings_python_install_pypi>` or
from :ref:`source <api_bindings_python_install_source>`.
But the bindings can also be used
:ref:`without installing <api_bindings_python_install_without>` them first.

.. _api_bindings_python_install_apt:

From APT Repository
^^^^^^^^^^^^^^^^^^^

The bindings are available in our APT repository for Debian based Linux
distributions (in this case you don't even need the ZIP file for the bindings).
Follow the :ref:`setup guide <apt_repository_setup>` then install the bindings:

* For Python 3::

   sudo apt install python3-tinkerforge

* For Python 2::

   sudo apt install python-tinkerforge

Now you're ready to test an example. The Debian package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

.. _api_bindings_python_install_pypi:

From PyPI
^^^^^^^^^

The bindings are available on the Python Package Index `PyPI
<https://pypi.python.org/pypi/tinkerforge>`__. You can install them with the
Python Package Installer `pip <https://pip.pypa.io>`__ using the following
command (in this case you don't even need the ZIP file for the bindings).
Depending on your Python installation you might have to execute this with
``sudo`` or as administrator::

 pip install tinkerforge

Now you're ready to test an example. The PyPI package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

.. _api_bindings_python_install_source:

From Source
^^^^^^^^^^^

The ``source/`` directory contains a ``setup.py`` install script that requires
the `setuptools <https://pypi.python.org/pypi/setuptools>`__ for Python to be
installed. To install the bindings just execute the following command in the
``source/`` directory. Depending on your Python installation you might have to
execute this with ``sudo`` or as administrator::

 python setup.py install

Currently this installation method still works, but it is marked as deprecated.
Use `pip <https://pip.pypa.io>`__ instead::

 pip install .

Now you're ready to test an example.

.. _api_bindings_python_install_without:

Without Installation
^^^^^^^^^^^^^^^^^^^^

You can use the bindings without having to install them. Just put the
``tinkerforge/`` folder from ``source/`` folder in the same folder as your
Python script and Python will automatically find the bindings. The section
about testing an example has more details about this.

Testing an Example
------------------

To test a Python example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``example_configuration.py`` file from the
``examples/brick/stepper/`` folder into a new folder::

 example_project/
  -> example_configuration.py

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: python

  HOST = "localhost"
  PORT = 4223
  UID = "XXYYZZ" # Change XXYYZZ to the UID of your Stepper Brick

If you did install the bindings then you're now ready to test this example::

 python example_configuration.py

If you did **not** install the bindings then you can also use the source of the
bindings directly. Just copy the ``tinkerforge/`` folder from the ``source/``
folder to your ``example_project/`` folder and Python will automatically find
the bindings::

 example_project/
  -> tinkerforge/
  -> example_configuration.py

Now you're ready to test this example::

 python example_configuration.py

API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_Python_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Python>
   Bricks <Bricks_Python>
   Bricks (Discontinued) <Bricks_Python_Discontinued>
   Bricklets <Bricklets_Python>
   Bricklets (Discontinued) <Bricklets_Python_Discontinued>
