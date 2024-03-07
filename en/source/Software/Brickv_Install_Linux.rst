
.. _brickv_install_linux:

Brick Viewer Installation on Linux
==================================

**Requirements**: Python 3.5 and PyQt 5.5 with QtOpenGL or newer

The :ref:`Brick Viewer <brickv>` can be installed on Debian based distribution
(Ubuntu, Mint, etc.) from a ``.deb`` file. For Arch Linux the package 
`brickv <https://aur.archlinux.org/packages/brickv/>`_ is available in the AUR.
On other distributions the Brick Viewer can be installed from source.

Debian Package
--------------

The Brick Viewer Debian package is available via our APT repository,
but can also be installed manually.

APT Repository
^^^^^^^^^^^^^^

First, set up our APT repository on your system according to this
:ref:`guide <apt_repository>`. Then install the Brick Viewer package::

 sudo apt install brickv

You can start the Brick Viewer in the application menu under electronic
or in a terminal with::

 brickv

Manual Installation
^^^^^^^^^^^^^^^^^^^

First, download the Brick Viewer ``.deb`` from :ref:`here <downloads_tools>`.
Right-click on the file and choose "Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickv_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_linux_1.jpg

Then click "Install Package":

.. image:: /Images/Screenshots/brickv_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_linux_2.jpg

Ready:

.. image:: /Images/Screenshots/brickv_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 3
   :align: center
   :target: ../_images/Screenshots/brickv_linux_3.jpg

In Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.
You can start the Brick Viewer in the application menu under electronic
or in a terminal with::

 brickv

To install Brick Viewer from the terminal use the following::

 sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtopengl python3-serial python3-tz python3-tzlocal
 wget --backups=1 https://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb


From Source
-----------

To install Brick Viewer from source, download the source from
:ref:`here <downloads_tools>` and install the dependencies:

* python3 (>= 3.5)
* python3-pyqt5 (>= 5.5)
* python3-pyqt5.qtopengl
* python3-serial
* python3-tz
* python3-tzlocal

On Debian based distributions you install them via ``apt-get``. On other
distribution you have to search for and install the equivalent packages::

 sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtopengl python3-serial python3-tz python3-tzlocal

First you have to build the Qt ``.ui`` files,
change to the folder ``src/`` and run::

 python build_src.py

After that you should be able to start brickv from source, change to the folder
``src/brickv/`` and start with::

 python main.py
