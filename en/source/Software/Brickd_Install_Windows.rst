
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="Brickd.html">Brick Daemon (brickd)</a> / Brick Daemon Installation on Windows

.. _brickd_install_windows:

Brick Daemon Installation on Windows
====================================

**Requirements**: Windows XP or newer

The :ref:`Brick Daemon <brickd>` can be installed from a setup ``.exe`` file.


Installer
---------

First, download the Brick Daemon installer ``.exe`` form :ref:`here
<downloads_tools>`. Click on the downloaded file, this should open the
installer:

.. image:: /Images/Screenshots/brickd_windows_1.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_windows_1.jpg

You can choose the actions of the installer:

* **Install Brick Daemon** will copy the program files.
* **Register Brick Daemon as Service** will install it as a autostarting
  Windows service. Without this you need to start Brick Daemon manually. Manual
  start is only useful for advanced debugging purposes.
* **Install/Update Brick Driver** will install/update the USB driver for
  Bricks (only Windows XP, Vista, 7). This driver is required if you want to
  use Bricks connected to USB.
* **Install/Update RED Brick Driver** will install/update the USB driver
  for RED Bricks (nur Windows XP, Vista, 7). This driver is required if you
  want to use RED Bricks connected to USB.
* **Install/Update RED Brick Serial Console Driver** will install/update
  the driver for the serial console of RED Bricks. This driver is required if
  you want to use the serial console of RED Bricks connected to USB.

Typically you want the installer to perform all tasks.
Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickd_windows_2.jpg
   :scale: 100 %
   :alt: Brickd installation step 2
   :align: center
   :target: ../_images/Screenshots/brickd_windows_2.jpg

Next the installation path can be configured.
Change it if necessary and click "Install" to start the installation process.


.. _brickd_install_windows_driver:

Manual Driver Installation
--------------------------

The Brick Daemon installer automatically installs all necessary drivers, except
the corresponding step were deselected toring installation. There are rare cases
in which the automatic driver installation fails. In all this cases it can be
necessary to manually install the required drivers.

Windows XP, Vista, 7
^^^^^^^^^^^^^^^^^^^^

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

You will find them in your Brickd program folder in the ``drivers\brick`` folder.

.. image:: /Images/Screenshots/brickd_windows_driver_4_small.jpg
   :scale: 100 %
   :alt: Brickd driver installation step 4
   :align: center
   :target: ../_images/Screenshots/brickd_windows_driver_4.jpg

After a successful installation the Brick should use a driver called
"Tinkerforge Brick". You can test the Brick by using the
:ref:`Brick Viewer<brickv>`.

.. note::
 On Windows 7 it is possible that Windows tries to install the
 drivers automatically and you don't have the choice to choose them manually.
 This automatic driver installation can fail without
 your notice. If you don't see Bricks in the Brick Viewer, please check in
 the Windows "Device Manager" that the drivers for the connected Bricks are
 installed correctly. If not, please choose the ``drivers\brick\win7`` folder in
 Brick Daemon installation and install the drivers manually.


Windows 8, 8.1 and 10
^^^^^^^^^^^^^^^^^^^^^

Since Windows 8 no driver for Bricks is needed anymore. Windows 8 and later
recognizes Bricks automatically.
