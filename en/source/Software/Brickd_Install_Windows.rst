
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="Brickd.html">Brick Daemon (brickd)</a> / Brick Daemon Installation on Windows

.. _brickd_install_windows:

Brick Daemon Installation on Windows
====================================

**Requirements**: Windows XP or newer

The :ref:`Brick Daemon <brickd>` can be installed from a setup ``.exe`` file.


Installer
---------

First, download the Brick Daemon ``.exe`` form :ref:`here <downloads_tools>`.
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


.. _brickd_install_windows_driver:

Driver Installation (Windows XP, Vista, 7)
------------------------------------------

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
 installed correctly. If not, please choose the ``drivers\brick`` folder in
 Brick Daemon installation and install the drivers manually.


Driver Installation (Windows 8, 8.1 and 10)
-------------------------------------------

Since Windows 8 no driver is needed anymore. Windows 8 and later recognizes
the hardware automatically and correctly.
