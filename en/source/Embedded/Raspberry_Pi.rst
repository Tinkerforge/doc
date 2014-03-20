
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#embedded-boards">Embedded Boards</a> / Raspberry Pi

.. _embedded_raspberry_pi:

Raspberry Pi
============

This section describes how to use Bricks and Bricklets with a
`Raspberry Pi <http://www.raspberrypi.org/>`__ together with Debian.


Prepare SD Card
---------------

In the first step you have to set up Debian on a SD card. There are two ways
to do this.

There is the recommended `New Out of Box Software (NOOBS)
<http://www.raspberrypi.org/downloads>`__ approach. You just download the NOOBS
ZIP file unpack it to an SD card and boot your Raspberry Pi from it. Then
follow the steps in the graphical installer and select "Raspbian" to be
installed.

If you don't want to use NOOBS there is also the old and more manual way to
download one of the different Debian images. There is one called "Raspbian"
(armhf) and the other one called "Soft-Float Debian" (armel). Raspbian uses
the hardware floating point unit (FPU) of the board and is the recommended one.
Download the latest `Raspbian image <http://www.raspberrypi.org/downloads>`__
and follow the necessary steps of this `SD card setup tutorial
<http://elinux.org/RPi_Easy_SD_Card_Setup>`__.


Start Raspberry Pi
------------------

Connect a keyboard, a monitor and a power supply to your Raspberry Pi.
After connecting the power supply the Raspberry Pi should start booting.

At the end of the boot process you should see the a login prompt. Enter
as user name ``pi`` and as password ``raspberry``. You should be logged in.


Install Brick Daemon
--------------------

How to set up Brick Daemon depends on the Debian image you're using.

Raspbian (armhf)
^^^^^^^^^^^^^^^^

If you have installed an Debian **with** hardware floating point unit support
(Raspbian) you can simply install the :ref:`Brick Daemon <brickd>` package by
executing (if ``libudev0`` isn't available install ``libudev1`` instead)::

 sudo apt-get install libusb-1.0-0 libudev0 pm-utils
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb

The Brick Daemon will be started after the installation and at startup
automatically.

Updates can be installed by repeating the last two commands::

 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb


Soft-Float Debian (armel)
^^^^^^^^^^^^^^^^^^^^^^^^^

If you have installed an Debian **without** hardware floating point unit support,
you have to compile :ref:`Brick Daemon <brickd>` from source.

First you have to download the source code from the 
`download page <http://www.tinkerforge.com/en/doc/Downloads.html#tools>`__
and put it under the ``home`` directory.

After this you have to execute the following steps::

 sudo apt-get install build-essential pkg-config libusb-1.0-0-dev libudev-dev pm-utils
 unzip Tinkerforge-brickd-vX.Y.Z-W-***.zip (modify filename)
 cd Tinkerforge-brickd-vX.Y.Z-W-*** (modify folder name)
 cd src/brickd
 make
 sudo make install
 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start


Install Brick Viewer
--------------------

To install the :ref:`Brick Viewer <brickv>` software execute the following
commands::

 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl python-serial
 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb

``apt-get`` might complain about dependencies that are not going to be installed.
If this happens ``apt-get`` suggest to run ``sudo apt-get -f install`` which
should resolve this problem and install re required dependencies.

Ensure that you have Python 2 installed (this is the default in Raspbian anyway),
because Brick Viewer doesn't work with Python 3 yet.

Updates can be installed by repeating the last two commands::

 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_linux_latest.deb


Access from outside
-------------------

You can use the Raspberry Pi to run the Brick Daemon and control the attached
devices from the outside. For example you can use this to control stuff from
your mobile phone.

To do this you have to change the host the IP Connection is connecting to in
your code from "localhost" to the IP address of the Raspberry Pi.


Reported Problems
-----------------

The USB port of the Raspberry Pi may not be able to handle the power
that is needed by a big stack of Bricks and Bricklets. In this case you
should use a :ref:`Step-Down Power Supply <step_down_power_supply>`.
