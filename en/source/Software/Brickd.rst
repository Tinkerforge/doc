
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

.. _brickd_installation:

Installation
------------

* :ref:`Linux <brickd_install_linux>`
* :ref:`Windows <brickd_install_windows>`
* :ref:`macOS <brickd_install_macos>`

.. toctree::
   :hidden:

   Linux <Brickd_Install_Linux>
   Windows <Brickd_Install_Windows>
   macOS <Brickd_Install_MacOSX>


Logging
-------

By default Brick Daemon logs messages about information, warnings and errors.
This includes basic information about USB hotplug and TCP/IP connections.

* Linux and macOS: Log messages are written to::

   /var/log/brickd.log

* Windows: Log messages are written to a log file called ``brickd.log`` in the
  Brick Daemon data directory:

  * Windows XP::

     C:\Documents und Settings\All Users\Application Data\Tinkerforge\Brickd\brickd.log

  * Windows Vista or newer::

     C:\ProgramData\Tinkerforge\Brickd\brickd.log

  You can use the ``logviewer.exe`` tool (part of the brickd installation) to
  view this log file. The tool also includes a Live Log view.

If the default logging configuration has not enough details to debug a problem
then there is the debug level log. This is not enable by default because it
drastically increases the mount of log messages and can have an impact on the
packet routing performance of brickd.

* Windows: The ``logviewer.exe`` tool includes a Live Log view that can be
  switched to debug level.


Configuration
-------------

The Brick Daemon configuration is stored in a file using a key-value format:

* Windows: The configuration file is called ``brickd.ini`` and stored in the
  Brick Daemon data directory:

  * Windows XP::

     C:\Documents und Settings\All Users\Application Data\Tinkerforge\Brickd\brickd.ini

  * Windows Vista or newer::

     C:\ProgramData\Tinkerforge\Brickd\brickd.ini

  You can use the ``logviewer.exe`` tool (part of the brickd installation) to
  edit this config file.
* Linux and macOS: The configuration file is called ``brickd.conf`` and
  stored in::

   /etc/brickd.conf

After changing the configuration file Brick Daemon has to be restarted to pick
up the changes:

* Linux (systemd)::

   sudo systemctl restart brickd

* Linux (SysVinit)::

   sudo /etc/init.d/brickd restart

* Windows: You can use the ``logviewer.exe`` tool (part of the brickd
  installation) to restart the Brick Daemon service.
* macOS::

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

* Linux::

   brickd --version

* Windows XP:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd.exe" --version

* Windows Vista or newer:

  .. code-block:: none

    "C:\Program Files (x86)\Tinkerforge\Brickd\brickd.exe" --version

* macOS (until Brick Daemon 2.2.1)::

   /usr/libexec/brickd.app/Contents/MacOS/brickd --version

* macOS (since Brick Daemon 2.2.2)::

   /usr/local/libexec/brickd.app/Contents/MacOS/brickd --version
