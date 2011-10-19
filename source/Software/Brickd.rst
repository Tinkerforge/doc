.. _brickd:

Brick Daemon (brickd)
=====================

The Brick Daemon is a daemon (or service on Windows) that acts as a bridge 
between the :ref:`Bricks <product_overview_bricks>`/
:ref:`Bricklets <product_overview_bricklets>`
and the programming language 
:ref:`API bindings <api_bindings>`.

The daemon routes data between the USB connections and TCP sockets.
When using the API bindings a TCP connection to the daemon is established.
This concepts allows the creation of bindings for almost every language
without any dependencies. Therefore it is possible to program Bricks and
Bricklets from embedded devices that only support specific languages,
such as smart phones.

Additionally it is possible to separate the machine running the Brick Daemon
from the machine running the user code. This allows e.g. a Brick connected
to a PC to be controlled from a smart phone or over the internet from
another PC.

.. _brickd_installation:

Installation
------------

Windows
^^^^^^^

TBD

Linux
^^^^^

To install the Brick Daemon on a Debian based distribution 
(Ubuntu, Mint, etc.), download the Brick Daemon .deb from 
:ref:`here <downloads_tools>`. Right-click on the file and choose 
"Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickd_1.jpg
   :scale: 40 %
   :alt: Brickd installation step 1
   :align: center

Then click "Install Package":

.. image:: /Images/Screenshots/brickd_2.jpg
   :scale: 40 %
   :alt: Brickd installation step 2
   :align: center

Ready:

.. image:: /Images/Screenshots/brickd_3.jpg
   :scale: 40 %
   :alt: Brickd installation step 3
   :align: center

In Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.

To install Brick Daemon from the console use the following::

 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 sudo dpkg -i brickd_latest.deb

To install Brick Daemon from source, download the source from `here <https://github.com/Tinkerforge/brickb>`__ and install the dependencies:

* python-twisted 
* python-gudev 
* libusb-1.0-0

On Debian based distributions you can do that as shown above, on other
distribution you have to search for and install the equivalent packages.

To start brickd from source, change to the directory 
brickd/src/brickd/ and start with::

 sudo python brickd_linux.py

Error logs can be found in::

 /var/log/brickd.log

If you install the Debian package, brickd will be started after the
installation and at startup automatically.

Mac OS
^^^^^^

TBD

