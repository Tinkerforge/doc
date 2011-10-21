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

To install the Brick Deamon (Service) on a Windows version, download the
brick Deamon .exe form :ref:`here downloads_tools>`. 
Click on the downloaded file, this should open the installer:

.. image:: /Images/Screenshots/brickd_windows_1.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

You can choose the actions of the installer:
 
 * **Install Brickd Programm** will copy the program files
 * **Install Brickd Service** will install it as a Windows service

Typically you want the installer to perform both tasks.
Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickd_windows_2.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Next you will be the installation path will be questioned.
Change it if necessary and click "Install".

At the end of the installation process a window will come
up which informs you, that you may have to install the
Bricks drivers manually (see section below). Press "OK"
and reboot your PC.




Windows Driver Installation
"""""""""""""""""""""""""""

Dependend on your Windows version it may be necessary
to install a Brick driver for each Brick you like to connect
independently.

Connect your Brick over USB to your PC. If a driver installation
is necessary you should see an window like below:

.. image:: /Images/Screenshots/brickd_windows_driver_1.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_1.jpg

Since Windows does not know our drivers we have to specify the 
drivers which are automatically be installed during the Brick Deamon
installation.

.. image:: /Images/Screenshots/brickd_windows_driver_2.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_2.jpg

Choose the driver location manually.

.. image:: /Images/Screenshots/brickd_windows_driver_3.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_3.jpg

You will find them in your Brickd programm directory in the "drivers" folder.

.. image:: /Images/Screenshots/brickd_windows_driver_4.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

After a sucessful installation the Brick should use a driver called "Brick_Driver".
You can test the Brick by using the :ref:`Brick Viewer<brickv>`.

Linux
^^^^^

To install the Brick Daemon on a Debian based distribution 
(Ubuntu, Mint, etc.), download the Brick Daemon .deb from 
:ref:`here <downloads_tools>`. Right-click on the file and choose 
"Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickd_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_linux__1.jpg

Then click "Install Package":

.. image:: /Images/Screenshots/brickd_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_linux_2.jpg

Ready:

.. image:: /Images/Screenshots/brickd_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_linux_3.jpg

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

.. note:: Mac OS will come soon.

