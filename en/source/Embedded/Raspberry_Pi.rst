
.. _embedded_raspberry_pi:

Raspberry Pi
============

This section describes how to use Bricks and Bricklets with a
`Raspberry Pi <https://www.raspberrypi.org/>`__ together with Debian.


Prepare SD Card
---------------

As the first step you have to set up Raspberry Pi OS on a SD card. It is
recommended to use `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`__
to do this.


Start Raspberry Pi
------------------

Connect a keyboard, a monitor and a power supply to your Raspberry Pi.
After connecting the power supply the Raspberry Pi should start booting.

At the end of the boot process you should see the a login prompt. Enter
the user name and password you choose in Raspberry Pi Imager. You should be logged in.


Install Brick Daemon
--------------------

Follow the Brick Daemon :ref:`installation guide <brickd_install_linux>`.


Install Brick Viewer
--------------------

Follow the Brick Viewer :ref:`installation guide <brickv_install_linux>`.


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
