
.. _brickv_install_windows:

Brick Viewer Installation on Windows
====================================

**Requirements**: Windows 8.1 or newer

The :ref:`Brick Viewer <brickv>` can be installed from a setup ``.exe`` file.


Installer
---------

First, download the Brick Viewer installer ``.exe`` form :ref:`here
<downloads_tools>`. Click on the downloaded file, this should open the
installer:

.. image:: /Images/Screenshots/brickv_windows_1.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_windows_1.jpg

You can choose the actions of the installer:

* **Install Brick Viewer** will copy the program files.
* **Install/Update ESP32 Bootloader Driver** will install/update the USB bootloader
  driver for ESP32 (Ethernet) Bricks. This driver is necessary to do ESP32
  (Ethernet) Brick firmware updates using Brick Viewer.

Typically you want the installer to perform all tasks.
Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickv_windows_2.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_windows_2.jpg

Next the installation path can be configured.
Change it if necessary, but ensure that the path contains ASCII characters only,
especially avoid umlauts.
Brick Viewer cannot be started if non-ASCII characters are in the installation
path, due to a bug in the Python ``pywintypes`` module.

Finally click "Install" to start the installation process.
