
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / Brick Daemon (brickd)

.. _brickd:

Brick Daemon (brickd)
=====================

The Brick Daemon is a daemon (or service on Windows) that acts as a bridge
between the :ref:`Bricks <primer_bricks>`/:ref:`Bricklets
<primer_bricklets>` and the :ref:`API bindings <api_bindings>` for
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


Requirements
------------

* Windows XP or newer
* Linux with libusb 1.0 or newer
* Mac OS X 10.8 or newer


.. _brickd_installation:

Installation
------------

* :ref:`Windows <brickd_install_windows>`
* :ref:`Linux <brickd_install_linux>`
* :ref:`Mac OS X <brickd_install_macosx>`

.. toctree::
   :hidden:

   Windows <Brickd_Install_Windows>
   Linux <Brickd_Install_Linux>
   Mac OS X <Brickd_Install_MacOSX>


Logging
-------

By default Brick Daemon logs messages about information, warnings and errors.
This includes basic information about USB hotplug and TCP/IP connections.

* Windows: Log messages are reported in the Windows Event Log. You can use the
  ``logviewer.exe`` tool (part of the brickd installation) to view the Windows
  Event Log filtered for brickd messages.
* Linux and Mac OS X: Log messages are written to ``/var/log/brickd.log``.

If the default logging configuration has not enough details to debug a problem
then there is the debug level log. This is not enable by default because it
drastically increases the mount of log messages and can have an impact on the
packet routing performance of brickd.

* Windows: The ``logviewer.exe`` tool also includes a Live Debug Log view that
  connects to the currently running brickd and displays a full debug log.


Configuration
-------------

The Brick Daemon configuration is stored in a file using a key-value format:

* Windows: The configuration file is called ``brickd.ini`` and stored in the
  Brick Daemon installation directory::

   C:\Program Files\Tinkerforge\Brickd\brickd.ini

* Linux and Mac OS X: The configuration file is called ``brickd.conf`` and
  stored in::

   /etc/brickd.conf

After changing the configuration file Brick Daemon has to be restarted to pick
up the changes:

* Windows:

  Open the "Computer Management", navigate to the "Services" section and
  restart the Brick Daemon service.
* Linux::

   sudo /etc/init.d/brickd restart

* Mac OS X::

   sudo launchctl stop com.tinkerforge.brickd
   sudo launchctl start com.tinkerforge.brickd

If there are errors in the configuration file then Brick Daemon will report
them in the log.

.. _brickd_websockets:

WebSockets
^^^^^^^^^^

`WebSockets <https://en.wikipedia.org/wiki/WebSocket>`__ are supported since
Brick Daemon version 2.1.0 , but disabled by default. To enable it you have to
configure the WebSocket port in the Brick Daemon configuration file.

The WebSocket port option has ``listen.websocket_port`` as key. An value of
0 or removing the ``listen.websocket_port`` key disables the WebSocket support.
Here is the WebSocket part of an example configuration using the recommended
value 4280 as WebSocket port:

.. code-block:: none

  listen.websocket_port = 4280

Afterwards Brick Daemon has to be restarted to pick up the configuration
change. Now the browser version of the :ref:`JavaScript bindings
<api_bindings_javascript>` can connect to Brick Daemon and control Bricks
and Bricklets.

.. note::

 As WebSockets basically allow any website in your browser to connect to your
 Bricks and Bricklets we recommended that you use :ref:`authentication
 <tutorial_authentication>` in combination with WebSockets.


.. _brickd_authentication:

Authentication
^^^^^^^^^^^^^^

Authentication is supported since Brick Daemon version 2.1.0, but disabled by
default. To enable it you have to configure an authentication secret in the
Brick Daemon configuration file.

The authentication secret can be 64 ASCII characters long and has
``authentication.secret`` as key. An empty value or removing the
``authentication.secret`` key disables authentication. Here is the
authentication part of an example configuration using
``My Authentication Secret!`` as secret::

  authentication.secret = My Authentication Secret!

Afterwards Brick Daemon has to be restarted to pick up the configuration
change. Now every TCP/IP connection to the Brick Daemon has to prove that it
knows the authentication secret before normal communication can occur. See the
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

Windows only:

* ``--install`` registers Brick Daemon as service and start it
* ``--uninstall`` stops service and unregister it
* ``--console`` forces start as console application
* ``--log-to-file`` writes log messages to a file
