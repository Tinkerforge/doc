.. _api_bindings_python:

Python - API Bindings
=====================

**Requirements**: Python 2.5 or newer, Python 3 is also supported

The Python bindings consist of a Python egg with the bindings for all
Tinkerforge Bricks and Bricklets (``tinkerforge.egg``, the source of the
egg (in ``source/``) and all available Python examples (in ``examples/``).

You can install the egg with easy_install::

 easy_install tinkerforge.egg

After that you can use the examples as they are.

If you can't or don't want to use the egg, you can also use the source
directly, just create a folder for your project and copy the ``tinkerforge``
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

.. note::
 Windows installation hint:

 * Install easy_install: http://pypi.python.org/pypi/setuptools#windows (setuptools)
 * Open Windows command shell
 * Execute ``C:\\YourPythonDir\\Scripts\\easy_install.exe C:\\PathToEgg\\tinkerforge.egg``
