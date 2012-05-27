.. _embedded_raspberry_pi:

Raspberry Pi
============

This section describes how to use Bricks/Bricklets with an 
`Raspberry Pi <http://www.raspberrypi.org/>`__ together
with Debian "squeeze".

Prepare SD Card
---------------

In the first step you have to set up squeeze on a SD Card. 
Download the latest Debian image from 
`here <http://www.raspberrypi.org/downloads>`__
and follow the necessary steps of this description:  
`http://www.raspberrypi.org/downloads <http://elinux.org/RPi_Easy_SD_Card_Setup>`__.

Start Raspberry Pi
------------------

Connect a keyboard, a monitor and a powersupply to your Raspberry Pi.
After connecting the powersupply the Raspberry Pi should start booting.

At the end of the boot process you should the a login prompt. Enter
as username "pi" and as password "raspberry". You should be logged in.

Set up Brickd/Brickv
--------------------

To install the :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer<brickv>` Software 
install it with the following commands::

 cd /home/pi
 sudo apt-get install python-twisted python-gudev libusb-1.0-0
 wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest.deb
 sudo dpkg -i brickd_latest.deb

 cd /home/pi
 sudo apt-get install python python-qt4 python-qwt5-qt4 python-matplotlib python-scipy python-opengl python-numpy python-qt4-gl
 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo dpkg -i brickv_latest.deb

Access from outside
-------------------

You can use the Raspberry Pi to run the Brick Deamon but control the attached 
devices from the outside. For example you can use this to control stuff from 
your mobile phone.

To do this you have to change the host the IPConnection is connecting to in 
your code from "localhost" to the IP of the Raspberry Pi.

Reported Problems
-----------------

There is problem with the powersupply of the Raspberry Pi when you use 
a system with many Bricks and Bricklets. The reason is that the Raspberry Pi 
itself is powered by USB. So this powersupply has to power the Raspberry Pi
and your connected stuff. If you facing any problems with the powersupply,
please reduce the amount of connected Bricks and Bricklets or power them
indepentently with a :ref:`Powersupply <product_overview_powersupplies>`.


