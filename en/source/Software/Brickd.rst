
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / Brick Daemon (brickd)

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

* Windows: Log messages are reported in the Windows Event Log. You can use the
  ``eventlog.exe`` tool (part of the brickd installation) to view the Windows
  Event Log filtered for brickd messages.
* Linux and Mac OS X: Log messages are written to ``/var/log/brickd.log``.


.. _brickd_authentication:

Authentication Configuration
----------------------------

Since Brick Daemon version 2.1.0 authentication is supported, but disabled by
default. To enable it you have to configure an authentication secret in the
Brick Daemon configuration file.

* Windows: The configuration file is called ``brickd.ini`` and stored in the
  Brick Daemon installation directory::

   C:\Program Files\Tinkerforge\Brickd\brickd.ini

* Linux and Mac OS X: The configuration file is called ``brickd.conf`` and
  stored in::

   /etc/brickd.conf

The configuration file has a key-value format. The authentication secret can
be 64 ASCII characters long and has ``authentication.secret`` as key. An empty
value or removing the ``authentication.secret`` key disables authentication.
Here is the authentication part of an example configuration using
``My Authentication Secret!`` as secret::

  authentication.secret = My Authentication Secret!

Afterwards Brick Daemon has to be restarted to pick up the configuration change:

* Windows:

  Open the "Computer Management", navigate to the "Services" section and
  restart the Brick Daemon service.
* Linux::

   sudo /etc/init.d/brickd restart

* Mac OS X::

   sudo launchctl stop com.tinkerforge.brickd
   sudo launchctl start com.tinkerforge.brickd

Now every TCP/IP connection to the Brick Daemon has to prove that it knows the
authentication secret before normal communication can occur. See the
:ref:`authentication tutorial <tutorial_authentication>` for more information.


Checking Installed Version
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

* ``--help`` shows help and exits
* ``--version`` shows version number and exits
* ``--check-config`` checks config file for errors
* ``--debug`` sets all log levels to debug
* ``--libusb-debug`` sets libusb log level to debug

Windows only:

* ``--install`` registers Brick Daemon as service and start it
* ``--uninstall`` stops service and unregister it
* ``--console`` forces start as console application
* ``--log-to-file`` writes log messages to a file
