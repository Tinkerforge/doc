
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#usage-with-embedded-boards">Usage with Embedded Boards</a> / Raspberry Pi

.. _embedded_raspberry_pi:

Raspberry Pi
============

This section describes how to use Bricks and Bricklets with a
`Raspberry Pi <http://www.raspberrypi.org/>`__ together with Debian.


Prepare SD Card
---------------

In the first step you have to set up Debian on a SD Card.
There exist different Debian images, one called "Raspbian" (armhf)
and the other "Soft-Float Debian" (armel). Raspbian uses the hardware floating 
point unit (FPU) of the board and is the recommended image.

Download the latest "Raspbian" image from
`here <http://www.raspberrypi.org/downloads>`__
and follow the necessary steps of
`this <http://elinux.org/RPi_Easy_SD_Card_Setup>`__ tutorial.


Start Raspberry Pi
------------------

Connect a keyboard, a monitor and a power supply to your Raspberry Pi.
After connecting the power supply the Raspberry Pi should start booting.

At the end of the boot process you should see the a login prompt. Enter
as username "pi" and as password "raspberry". You should be logged in.


Install Brick Daemon
--------------------

How to set up Brick Daemon depends on the Debian image you're using.

Raspbian (armhf)
^^^^^^^^^^^^^^^^

If you have installed an Debian **with** hardware floating point unit support
(Raspbian) you can simply install the :ref:`Brick Daemon <brickd>` package by::

 cd /home/pi
 sudo apt-get install libusb-1.0-0 libudev
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
 sudo dpkg -i brickd_linux_latest_armhf.deb


Soft-Float Debian (armel)
^^^^^^^^^^^^^^^^^^^^^^^^^

If you have installed an Debian **without** hardware floating point unit support,
you have to compile :ref:`Brick Daemon <brickd>` from source.

First you have to download the source code from the 
`download page <http://www.tinkerforge.com/en/doc/Downloads.html#tools>`__
and put it under the home directory.

After this you have to execute the following steps::

 sudo apt-get install build-essential libusb-1.0-0-dev libudev-dev
 cd /home/pi
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

 cd /home/pi
 sudo apt-get install python python-qt4 python-qt4-gl python-qwt5-qt4 python-opengl
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

