.. _brickd:

Brick Daemon (brickd)
=====================

Der Brick Daemon ist ein Daemon (bzw. Service für Windows) der als eine Brücke
zwischen :ref:`Bricks <product_overview_bricks>`/:ref:`Bricklets
<product_overview_bricklets>` und den :ref:`API Bindings <api_bindings>` für die
verschiedenen Programmiersprachen fungiert..

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

Windows
^^^^^^^

To install the Brick Deamon (Service) on a Windows, download the
Brick Deamon .exe form :ref:`here <downloads_tools>`.
Click on the downloaded file, this should open the installer:

.. image:: /Images/Screenshots/brickd_windows_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

You can choose the actions of the installer:

* **Install Brickd Program** will copy the program files
* **Register Brickd Service** will install it as a Windows service

Typically you want the installer to perform both tasks.
Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickd_windows_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Next the installation path will be questioned.
Change it if necessary and click "Install".

At the end of the installation process a window will come
up which informs you, that you may have to install the
Brick drivers manually (see section below). Press "OK"
and reboot your PC.


Windows Driver Installation
"""""""""""""""""""""""""""

Depending on your Windows version it is necessary
to install a Brick driver. This driver needs to be installed for each of your
Bricks independently.

Connect your Brick over USB to your PC. If a driver installation
is necessary you should see an window like below:

.. image:: /Images/Screenshots/brickd_windows_driver_1_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_1.jpg

If you have not installed the driver before,
Windows does not know our drivers and you have to specify the
driver location. You can find the drivers in your Brick Daemon installation
folder. If you have installed the drivers before, you can choose the
"Install the software automatically" option since Windows already knows
the driver location.

.. image:: /Images/Screenshots/brickd_windows_driver_2_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_2.jpg

Choose the driver location manually.

.. image:: /Images/Screenshots/brickd_windows_driver_3_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_3.jpg

You will find them in your Brickd program folder in the "drivers" folder.

.. image:: /Images/Screenshots/brickd_windows_driver_4_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

After a successful installation the Brick should use a driver called "Brick_Driver".
You can test the Brick by using the :ref:`Brick Viewer<brickv>`.

.. note::
 Under Windows 7 it is possible that Windows tries to install the
 drivers automatically and you don't have the choice to choose them manually.
 This automatic driver installation can fail without
 your notice. If you don't see Bricks in the Brick Viewer, please check in
 the Windows "Device Manager" that the drivers for the connected Bricks are
 installed correctly. If not, please choose the ``drivers`` folder in Brick
 Daemon installation and install the drivers manually.


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
   :target: ../_images/Screenshots/brickd_linux_1.jpg

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
 sudo dpkg -i brickd_linux_latest.deb

To install Brick Daemon from source, download the source from `here
<https://github.com/Tinkerforge/brickd>`__ and install the dependencies:

* python-twisted
* python-gudev
* libusb-1.0-0

On Debian based distributions you can do that as shown above, on other
distribution you have to search for and install the equivalent packages.

To start brickd from source, change to the folder
brickd/src/brickd/ and start with::

 sudo python brickd_linux.py

Error logs can be found in::

 /var/log/brickd.log

If you install the Debian package, brickd will be started after the
installation and at startup automatically.


Mac OS X
^^^^^^^^

To install the Brick Daemon on Mac OS X download the .dmg
from :ref:`here <downloads_tools>`. Click on the downloaded file, this
should open the package:

.. image:: /Images/Screenshots/brickd_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_macos_1.jpg

Then click "INSTALL", this should open a password prompt.
Root access is needed to add the Brick Daemon
to your Launchd Daemons.

.. image:: /Images/Screenshots/brickd_macos_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_macos_2.jpg

After this an "Installation Finished" window should come up.
Click "OK".

.. image:: /Images/Screenshots/brickd_macos_3_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 3
   :align: center
   :target: ../_images/Screenshots/brickd_macos_3.jpg

You have finished the installation. The Brick Daemon should be started upon
installation and it should be started automatically after restarts.

If for some reason brickd doesn't run or it has crashed, you can start it
from the terminal with::

 sudo launchctl start com.tinkerforge.brickd

.. note::
 Since Mac OS X Mountain Lion only signed software can be installed by default.
 Currently the Brick Daemon and its installer is not signed. This makes Mac OS X
 show you an error message saying that the installer is broken when you try to
 install it. For now you need to lower your system security settings to allow
 installing unsigned software by clicking:

 * System Settings
 * Security & Privacy
 * Allow applications downloaded from: Anywhere


Checking installed version
--------------------------

Since Brick Daemon version 1.0.8 you can check which Brick Daemon is currently
installed with the `--version` commandline argument:

* Windows:

  .. code-block:: none

    "C:\Program Files\Tinkerforge\Brickd\brickd_windows.exe" --version

* Linux::

   brickd --version

* Mac OS X::

   /usr/libexec/brickd.app/Contents/MacOS/brickd_macosx --version
