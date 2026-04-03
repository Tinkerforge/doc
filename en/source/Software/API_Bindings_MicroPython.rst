
.. _api_bindings_micropython:

MicroPython - API Bindings
==========================

The MicroPython bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from MicroPython scripts running on
microcontroller boards such as ESP32, Raspberry Pi Pico and others. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``source/`` the source code of the bindings as flat ``.py`` files
* in ``examples/`` the examples for every Brick and Bricklet
* in ``stubs/`` the ``.pyi`` type stub files for IDE code completion

Requirements
------------

* `MicroPython <https://micropython.org/>`__ 1.17 or newer
* A MicroPython-capable board with WiFi or Ethernet networking (e.g. ESP32,
  Raspberry Pi Pico W)

.. _api_bindings_micropython_install:

Installation
------------

Since MicroPython boards have limited filesystems and do not support pip or
setuptools, there is no package installer. Instead, copy the binding files
directly onto your board.

Copy the ``.py`` files from the ``source/`` folder of the
:ref:`ZIP file <downloads_bindings_examples>` to your board using a tool such as
`mpremote <https://docs.micropython.org/en/latest/reference/mpremote.html>`__,
`Thonny <https://thonny.org/>`__ or
`ampy <https://github.com/scientificit/ampy>`__. For example, using mpremote::

 mpremote cp source/ip_connection.py :
 mpremote cp source/bricklet_temperature_v2.py :

Copy only the bindings you actually need to save space on the board. At
minimum, you always need ``ip_connection.py`` plus the binding file for each
device you want to use.

WiFi Setup
----------

For WiFi-capable boards (e.g. ESP32), the network connection must be
established before connecting to a Brick Daemon. This can be done using
MicroPython's ``network`` module:

.. code-block:: python

  import network

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect("YOUR_SSID", "YOUR_PASSWORD")

  while not wlan.isconnected():
      pass

  print("Connected:", wlan.ifconfig())

hmac Module (for Authentication)
--------------------------------

If you want to use authentication (``ipcon.authenticate()``), the ``hmac``
module is required. Most MicroPython builds do not include it by default.
Install it using MicroPython's package manager (requires a network connection)::

 import mip
 mip.install("hmac")

Testing an Example
------------------

To test a MicroPython example :ref:`Brick Daemon <brickd>` and :ref:`Brick
Viewer <brickv>` have to be installed first. Brick Daemon acts as a proxy
between the USB interface of the Bricks and the API bindings. Brick Viewer
connects to Brick Daemon and helps to figure out basic information about the
connected Bricks and Bricklets.

As an example let's test the configuration example for the Stepper Brick.
For this copy the ``example_configuration.py`` file from the
``examples/brick/stepper/`` folder and the required binding files to your
board::

 board/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. When running on a microcontroller board, replace
``localhost`` with the IP address of the computer running Brick Daemon. The
``UID`` value has to be changed to the UID of the connected Stepper Brick,
which you can figure out using Brick Viewer:

.. code-block:: python

  HOST = "192.168.1.100"
  PORT = 4223
  UID = "XXYYZZ" # Change XXYYZZ to the UID of your Stepper Brick

Now you're ready to run this example on your board::

 mpremote run example_configuration.py

.. note::
 Unlike the regular Python bindings, MicroPython bindings use a flat module
 structure. Imports use the form ``from ip_connection import IPConnection``
 instead of ``from tinkerforge.ip_connection import IPConnection``.

.. note::
 The MicroPython bindings use a synchronous/polling architecture. There is no
 background thread for callback dispatch. You must call
 ``ipcon.dispatch_callbacks(seconds)`` periodically to handle incoming
 callbacks. Use a negative value for infinite dispatching:
 ``ipcon.dispatch_callbacks(-1)``.

.. note::
 Auto-reconnect is not supported in the MicroPython bindings because it
 requires background threads. You must handle reconnection explicitly in your
 code.

Reducing File Size with mpy-cross
----------------------------------

The ``.py`` binding files can be compiled to MicroPython bytecode (``.mpy``
files) to reduce file size and speed up import times. This is done using the
``mpy-cross`` tool.

.. important::
 The ``mpy-cross`` version must match the MicroPython firmware version on your
 board. For example, if your board runs MicroPython 1.23.x, you need
 ``mpy-cross`` from the 1.23 release. Using a mismatched version will result
 in import errors on the board.

Install ``mpy-cross`` matching your firmware version::

 pip install mpy-cross==1.23.0  # adjust version to match your firmware

Compile a binding file::

 mpy-cross bricklet_temperature_v2.py

This creates ``bricklet_temperature_v2.mpy`` in the same directory. Copy the
``.mpy`` file to your board instead of the ``.py`` file. All imports work the
same way — MicroPython automatically finds ``.mpy`` files.

To compile all binding files at once::

 for f in source/*.py; do mpy-cross "$f"; done

Typical size reduction is around 70-80% compared to the original ``.py`` files.

IDE Support with Type Stubs
---------------------------

The ZIP file includes a ``stubs/`` folder with ``.pyi`` type stub files for all
bindings. These provide code completion, type checking and inline documentation
in IDEs such as VS Code (with Pylance) or PyCharm.

To use the stubs, configure your IDE to include the ``stubs/`` folder as an
extra analysis path. For VS Code, add the following to your ``.vscode/settings.json``:

.. code-block:: json

 {
   "python.analysis.extraPaths": ["path/to/stubs"]
 }

The stubs contain full type annotations and docstrings for all device classes,
methods and constants. They are not needed on the board itself — they are only
used by the IDE during development.

API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_MicroPython_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MicroPython>
   Bricks <Bricks_MicroPython>
   Bricks (Discontinued) <Bricks_MicroPython_Discontinued>
   Bricklets <Bricklets_MicroPython>
   Bricklets (Discontinued) <Bricklets_MicroPython_Discontinued>
