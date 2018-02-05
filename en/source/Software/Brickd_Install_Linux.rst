
.. _brickd_install_linux:

Brick Daemon Installation on Linux
==================================

The :ref:`Brick Daemon <brickd>` can be installed on Debian based distribution
(Ubuntu, Mint, etc.) from a ``.deb`` file. On other distributions it can be
installed from source.


Debian Package
--------------

First, download the correct Brick Daemon ``.deb`` for your architecture from
:ref:`here <downloads_tools>`.
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

 # Use libudev1 instead of libudev0 in Ubuntu 13.04
 sudo apt-get install libusb-1.0-0 libudev0 pm-utils

 # On ARM (e.g. Raspberry Pi)
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

 # On RED Brick
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest+redbrick_armhf.deb
 sudo dpkg -i brickd_linux_latest+redbrick_armhf.deb

The Brick Daemon will be started after the installation and at startup
automatically.


From Source
-----------

To install Brick Daemon from source you need to clone/download its
`source code from GitHub <https://github.com/Tinkerforge/brickd>`__::

 git clone https://github.com/Tinkerforge/brickd

Brick Daemon uses the common Tinkerforge daemonlib. Clone/Download its
`source code from GitHub <https://github.com/Tinkerforge/daemonlib>`__ to the
``src/`` folder in the brickd clone::

 cd src/
 git clone https://github.com/Tinkerforge/daemonlib

Also install the following libraries:

* libusb-1.0
* libudev (optional for USB hotplug)
* pm-utils (optional for suspend/resume handling)

On Debian based distributions you can install the dependencies with apt-get::

 sudo apt-get install build-essential pkg-config libusb-1.0-0-dev libudev-dev pm-utils

On Fedora you can install the dependencies with yum::

 sudo yum groupinstall "Development Tools"
 sudo yum install libusb1-devel libudev-devel pm-utils-devel

On other distribution you have to search for and install the equivalent packages.

To compile and install from source run::

 cd src/brickd/
 make
 sudo make install

Run the following commands to register brickd for autostart on Debian based
Linux distributions and start it::

 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start
