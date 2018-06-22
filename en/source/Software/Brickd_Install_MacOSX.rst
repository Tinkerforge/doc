
.. _brickd_install_macos:

Brick Daemon Installation on macOS
==================================

**Requirements**: macOS 10.8 (Mountain Lion) or newer

The :ref:`Brick Daemon <brickd>` can be installed from a ``.dmg`` file.


Disk Image
----------

First, download the Brick Daemon ``.dmg`` from :ref:`here <downloads_tools>`.
Click on the downloaded file, this should open the disk image:

.. image:: /Images/Screenshots/brickd_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation step 1
   :align: center
   :target: ../_images/Screenshots/brickd_macos_1.jpg

Then click ``INSTALL``, this should open a password prompt. But it might show the
following error message instead for Brick Daemon 2.0.8 and older versions:

.. image:: /Images/Screenshots/brickd_macos_not_signed_1_small.jpg
   :scale: 100 %
   :alt: Brickd installation: Error message on macOS Mountain Lion
   :align: center
   :target: ../_images/Screenshots/brickd_macos_not_signed_1.jpg

Since macOS Mountain Lion only signed software can be installed by default.
Brick Daemon and its installer are signed since version 2.0.9. For 2.0.8 and
older versions macOS might show you the error message saying that the
installer is broken when you try to install it. To install 2.0.8 or older you
need to lower your system security settings to allow installing unsigned
software by clicking:

* System Preferences
* Security & Privacy
* Allow applications downloaded from: Anywhere

Now click ``INSTALL`` again. macOS Mountain Lion might show this warning:

.. image:: /Images/Screenshots/brickd_macos_not_signed_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation: Warning message on macOS Mountain Lion
   :align: center
   :target: ../_images/Screenshots/brickd_macos_not_signed_2.jpg

Click "Open", this should open a password prompt now. Root access
is needed to add the Brick Daemon to your Launchd Daemons.

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
