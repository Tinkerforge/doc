
.. _brickd_install_linux:

Brick Daemon Installation on Linux
==================================

The :ref:`Brick Daemon <brickd>` can be installed on Debian based distribution
(Ubuntu, Mint, etc.) from a ``.deb`` file. For Arch Linux the package 
`brickd <https://aur.archlinux.org/packages/brickd/>`_ is available in the AUR.
On other distributions the Brick Daemon can be installed from source.

Debian Package
--------------

The Brick Daemon Debian package is available in our `APT pepository
<https://download.tinkerforge.com/apt/>`__, but can also be installed manually.


APT Repository
^^^^^^^^^^^^^^

First, set up our APT repository on your system according to this
:ref:`guide <apt_repository>`. Then install the Brick Viewer package::

 sudo apt install brickd

The Brick Daemon will be started after the installation and at startup
automatically.

Manual Installation
^^^^^^^^^^^^^^^^^^^

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
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

 # On 64bit x86
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_amd64.deb
 sudo dpkg -i brickd_linux_latest_amd64.deb

 # On 32bit x86
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_i386.deb
 sudo dpkg -i brickd_linux_latest_i386.deb

 # On RED Brick
 wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest+redbrick_armhf.deb
 sudo dpkg -i brickd_linux_latest+redbrick_armhf.deb

The Brick Daemon will be started after the installation and at startup
automatically.


From Source
-----------

To install Brick Daemon from source follow the steps described in this
`README <https://github.com/Tinkerforge/brickd/blob/master/README.rst>`__.

