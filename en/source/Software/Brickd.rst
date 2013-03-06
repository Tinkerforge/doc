.. _brickd:

Brick Daemon (brickd)
=====================

The Brick Daemon is a daemon (or service on Windows) that acts as a bridge
between the :ref:`Bricks <product_overview_bricks>`/:ref:`Bricklets
<product_overview_bricklets>` and the :ref:`API bindings <api_bindings>` for
the different programming languages.

The daemon routes data between the USB connections and TCP/IP sockets.
When using the API bindings a TCP/IP connection to the daemon is established.
This concepts allows the creation of bindings for almost every language
without any dependencies. Therefore it is possible to program Bricks and
Bricklets from embedded devices that only support specific languages,
such as smart phones.

Additionally it is possible to separate the machine running the Brick Daemon
from the machine running the user code. This allows e.g. a Brick connected
to a PC to be controlled from a smart phone or over the Internet from
another PC.


.. _brickd_installation:

Installation
------------

* :ref:`Windows <brickd_install_windows>`
* :ref:`Linux <brickd_install_linux>`
* :ref:`Mac OS X <brickd_install_macosx>`


Logging
-------

By default Brick Daemon logs messages about information, warnings and errors.

* Windows: Log messages are reported in the Windows Event Log.
* Linux and Mac OS X: Log messages are written to ``/var/log/brickd.log``.


Checking installed version
--------------------------

Since Brick Daemon version 1.0.8 you can check which Brick Daemon is currently
installed with the `--version` commandline argument:

* Windows:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd --version


Commandline Options
-------------------

Common:

* **--help**: Show help
* **--version**: Show version number
* **--check-config**: Check config file for errors
* **--debug**: Set all log levels to debug

Windows only:

* **--install**: Register as service and start it
* **--uninstall**: Stop service and unregister it
* **--console**: Force start as console application
* **--log-to-file**: Write log messages to file
