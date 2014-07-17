
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-python">Software</a> / Python - API Bindings

.. _api_bindings_python:

Python - API Bindings
=====================

**Requirements**: Python 2.5 or newer, Python 3 is also supported

The Python bindings (:ref:`download <downloads_bindings_examples>`) consist of
the Python source code of the bindings for all Tinkerforge Bricks and Bricklets
(in ``source/``) and all available Python examples (in ``examples/``).

You can install the bindings using `setuptools
<https://pypi.python.org/pypi/setuptools>`__ by executing the following
command in the ``source/`` folder::

 python setup.py install

The bindings are also available on the Python Package Index `PyPI
<https://pypi.python.org>`__. You can install them with the Python Package
Installer `pip <https://pip.pypa.io>`__ using the following command::

 pip install tinkerforge

After that you can use the examples as they are.


Testing an Example
------------------

If you can't or don't want to install the bindings, you can also use the source
directly, just create a folder for your project and copy the ``tinkerforge/``
folder from ``source/`` and the example you want to try in there
(e.g. the Stepper configuration example from
``examples/brick/stepper/example_configuration.py``)::

 example_folder/
  -> tinkerforge/
  -> example_configuration.py

If you just want to use a few Bricks or Bricklets and you don't want to
have this many files in you project, you can also copy the files as they are
needed. For the Stepper Brick examples we need ``ip_connection.py`` and
``brick_stepper.py``. After copying these in the project folder::

 example_folder/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

we have to remove the ``tinkerforge`` package from the examples, i.e. instead of:

.. code-block:: python

 from tinkerforge.ip_connection import IPConnection
 from tinkerforge.brick_stepper import Stepper

we use:

.. code-block:: python

 from ip_connection import IPConnection
 from brick_stepper import Stepper

After that, the example can be executed again.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_Python_links.table
