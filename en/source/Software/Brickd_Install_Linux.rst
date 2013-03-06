.. _brickd_install_linux:

Brick Daemon Installation on Linux
==================================

The :ref:`Brick Daemon <brickd>` can be installed on Debian based distribution
(Ubuntu, Mint, etc.) from a ``.deb`` file. On other distributions it can be
installed from source.


Debian Package
--------------

First, download the Brick Daemon ``.deb`` from :ref:`here <downloads_tools>`.
Right-click on the file and choose "Open with GDebi Package Installer":

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

On Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.

To install Brick Daemon from the console use the following::

 sudo apt-get install libusb-1.0-0 libudev0

 # On ARM (e.g. Raspberry PI)
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

The Brick Daemon will be started after the installation and at startup
automatically.


From Source
-----------

To install Brick Daemon from source, download the source from `here
<https://github.com/Tinkerforge/brickd>`__ and install the dependencies:

* libusb-1.0-0-dev >= 1.0.8
* libudev-dev >= 173 (Optional for Hotplug)

On Debian based distributions you can install the dependencies with apt-get::

 sudo apt-get install libusb-1.0-0-dev libudev-dev

On other distribution you have to search for and install the equivalent packages.

To compile from source, change to the folder ``brickd/src/brickd/`` and run::

 make
 sudo ./brickd
