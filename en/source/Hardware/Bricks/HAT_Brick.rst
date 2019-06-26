
:DISABLED_shoplink: ../../../shop/bricks/hat-brick.html

.. include:: HAT_Brick.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _hat_brick:

HAT Brick
=========

.. note::
  This Brick is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricks/brick_hat_tilted_[?|?].jpg              HAT Brick
	Bricks/brick_hat_horizontal_[?|?].jpg          HAT Brick
	Bricks/brick_hat_brickv_[100|].jpg             HAT Brick in Brick Viewer
	Dimensions/hat_brick_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Raspberry Pi HAT with standard RPi HAT form factor
* Has **eight** ports for Bricklets
* Onboard 5.3V power supply (5V-28V input, up to 4A)
* Measures USB and DC supply voltages
* Adds battery backed real-time clock to Raspberry Pi
* Adds low power sleep mode and RPi watchdog


.. _hat_brick_description:

Description
-----------

The HAT Brick is a `Raspberry Pi HAT <https://www.raspberrypi.org/blog/introducing-raspberry-pi-hats/>`__
with the standard RPi HAT form factor. The Brick follows the HAT specification
and it will automatically work with Raspbian without any changes.

With the HAT Brick you can connect up to **eight** :ref:`Bricklets <primer_bricklets>` to your
Raspberry Pi.

You can power the Raspberry Pi through the HAT by an external 5V-28V DC power supply. 
The onboard power supply will be able to provide very stable 5V, even under heavy load. You
can power the Raspberry Pi, connected Bricklets and USB devices connected to the 
RPi's USB connectors. Power issues with RPi's due to a voltage drop on the power supply are 
compensated by delivering slightly increased 5V (5.3V).

You can also still power the
HAT/RPi through Micro-USB. In that case you have to ensure that the HAT will be provided with stable 5V, 
for example by the official Raspberry Pi universal power supply.
The USB/DC supply voltages are measured and accessible through the API.

Additionally, the HAT has a :ref:`real-time clock with battery backup <hat_brick_real_time_clock>`
that is directly connected to the Raspberry Pi. The HAT can :ref:`turn the RPi off for a specified
time <hat_brick_low_power_sleep_mode>`. You can use the Raspberry Pi in battery powered
applications, for example to send sensor information every hour to a cloud.

A :ref:`watchdog <hat_brick_watchdog>` can also be implemented with the HAT, such that the RPi will be
restarted if it crashes or your program gets stuck.

The HAT is electrically compatible to the Raspberry Pi 2B, 3B, 3B+, 4B, Zero and Zero W. The mounting
holes are compatible to the Raspberry Pi 2/3/4. We also offer a smaller :ref:`HAT Zero Brick <hat_zero_brick>`
that has mounting holes that are compatible to the Raspberry Pi Zero.

.. note::
  The HAT Brick provides Bricklet ports with 7 poles each. You can connect Bricklets with a
  7 pole to 7 pole cable to it. Only Bricklets with 7 pole Bricklet ports are 
  supported.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               100mW (20mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    8
DC Input Voltage                  5-28V
DC Output                         5.3V, max. 4A
Sleep Current (≤1.4)*             70mW (14mA at 5V) + 1.5mW if sleep indicator LED enabled
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            65 x 56 x 25mm (2.56 x 2.20 x 0.98")
Weight                            30g 
================================  ============================================================

\*: This value is for HAT Brick with hardware version smaller or equal to 1.4.

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/hat-brick/raw/master/hardware/hat-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/hat_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/hat-brick/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _hat_brick_getting_started:

Getting Started
---------------

To get started with the HAT Brick you first have to install :ref:`Brick Daemon <brickd>`
on the Raspberry Pi. Brick Daemon acts as a proxy between the Bricklet ports
on the HAT and the API bindings. It also handles the real-time clock.

You can install Brick Daemon from the terminal with the following commands:

.. code-block:: shell

	sudo apt-get install libusb-1.0-0 libudev0 pm-utils
	wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
	sudo dpkg -i brickd_linux_latest_armhf.deb

After the Brick Daemon is installed you can put the HAT on top of the
Raspberry Pi and restart it.

Now use :ref:`Brick Viewer <brickv>` to connect to the HAT Brick and connected Bricklets. 
You can install Brick Viewer directly on the Raspberry Pi or on an external PC that has 
access to the Raspberry Pi (over Ethernet or WIFI). If you use an external PC you have 
to connect to the IP of the Raspberry Pi, otherwise to localhost.

In the Brick Viewer a new tab named "HAT Brick" as well as one Tab for each of the
connected Bricklets will appear:

.. image:: /Images/Bricks/hat_brickv.jpg
   :scale: 100 %
   :alt: HAT Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/hat_brickv.jpg

In the HAT Brick tab of the Brick Viewer you can test the sleep mode and see the
measured voltages as well as the connected Bricklets.

If you are not sure if the HAT Brick was detected correctly you can take a look
in the folder ``/proc/device-tree/hat/`` on the Raspberry Pi:

.. code-block:: shell

	cd /proc/device-tree/hat/
	echo Name: "$(tr -d '\0'<name)", Product: "$(tr -d '\0'<product)",  Product ID: "$(tr -d '\0'<product_id)", Vendor: "$(tr -d '\0'<vendor)"

This should print something like the following::

	Name: hat, Product: HAT Brick, Product ID: 0x084e, Vendor: Tinkerforge GmbH

If the folder does not exist or the data does not match the installation was not
successfull. Is the HAT Brick connected correctly? Did you restart the RPi after
you connected it?


.. _hat_brick_low_power_sleep_mode:

Low Power Sleep Mode
--------------------

The HAT Brick can turn the Raspberry Pi off and on again with a
configurable off-duration.

You can configure if the power supply of the Bricklets is to be
turned off at the same time. Addtionally the blue status LED can
be either turned off, or configured as a sleep indicator with a
1 second blink interval.

While the RPi is turned off, the real-time clock on the HAT will
still be running and set the correct time when the RPi boots
again.

For more details take a look at the ``SetSleepMode`` function in the
API.


.. _hat_brick_watchdog:

Watchdog
--------

The HAT Brick can be used as a watchdog for the Raspberry Pi. It
can restart the Raspberry Pi if it crashes or gets stuck.

To implement the watchdog you can also use the ``sleep delay`` and
``sleep duration`` parameters of the ``SetSleepMode`` function.

Watchdog implementation example (Python):

.. code-block:: python

	while True:
		hat.set_sleep_mode(10, 2, True, False, False)
		time.sleep(1)

This will tell the HAT Brick to restart the Raspberry Pi in 10 seconds in
a 1 second loop. The 10 second delay will be reset every loop-iteration. If
the Raspberry Pi crashes, the loop doesn't run anymore and the HAT Brick will
restart the Raspberry Pi.

This loop can be a standalone program or you can put the ``SetSleepMode``
call somewhere in the main loop of your application that runs on the
Raspberry Pi. In this case the Raspberry Pi is automatically restartet
if the application crahses or gets stuck.


.. _hat_brick_real_time_clock:

Real-Time Clock
---------------

The HAT Brick comes with a I2C real-time clock that is directly connected to
the Raspberry Pi. It will be automatically detected by the RPi. You can check
if it was detected with dmesg. It should have an entry that looks like::

	[    3.850299] rtc-pcf8523 1-0068: rtc core: registered rtc-pcf8523 as rtc0

If you don't have NTP available you have to initially set the real-time clock.
To do this you can set the correct date/time on the Raspberry Pi by hand
and then call

.. code-block:: shell

	hwclock --systohc

on the Raspberry Pi. This will transfer the current time set on the Raspberry Pi
to the real-time clock. You only have to do this once.

If you have NTP available the real-time clock will be updated automatically.

If you have Brick Daemon installed, it will make sure that the real-time
clock date/time is automatically transferred back to the system on the next
reboot.

Without the Brick Daemon you can also do this by yourself by calling

.. code-block:: shell

	hwclock --hctosys


Compatibility to other Boards and Images
----------------------------------------

If you use Raspbian the HAT Brick will automatically be detected and used. The pins
that are used for the communication with the Bricklets are configured automatically.

This is done through a configuration that is read by Raspian from an EEPROM on the HAT.

If you use a non-standard linux image that does not have the raspi-config framework or
a different board that has a compatible pin header but different processor this will
not work automatically.

In this case the Brick Daemon can do the necessary configuration to the SPI and GPIO 
pins. You have to add the configuration to the ``/etc/brickd.conf`` file.

For a standard Raspberry Pi you can add the following::

	bricklet.group0.spidev = /dev/spidev0.0

	bricklet.group0.cs0.driver = gpio
	bricklet.group0.cs0.name = gpio23
	bricklet.group0.cs0.num = 23

	bricklet.group0.cs1.driver = gpio
	bricklet.group0.cs1.name = gpio22
	bricklet.group0.cs1.num = 22

	bricklet.group0.cs2.driver = gpio
	bricklet.group0.cs2.name = gpio25
	bricklet.group0.cs2.num = 25

	bricklet.group0.cs3.driver = gpio
	bricklet.group0.cs3.name = gpio26
	bricklet.group0.cs3.num = 26

	bricklet.group0.cs4.driver = gpio
	bricklet.group0.cs4.name = gpio27
	bricklet.group0.cs4.num = 27

	bricklet.group0.cs5.driver = gpio
	bricklet.group0.cs5.name = gpio24
	bricklet.group0.cs5.num = 24

	bricklet.group0.cs6.driver = gpio
	bricklet.group0.cs6.name = gpio7
	bricklet.group0.cs6.num = 7

	bricklet.group0.cs7.driver = gpio
	bricklet.group0.cs7.name = gpio6
	bricklet.group0.cs7.num = 6

	bricklet.group0.cs8.driver = gpio
	bricklet.group0.cs8.name = gpio5
	bricklet.group0.cs8.num = 5

First you have to define the spi device that is used (``/dev/spidev0.0`` for the
Raspberry Pi). Then you have to define the GPIO driver, name and number for each
chip select. There are eight chip selects for the eight Bricklet ports and one 
additional chip select for the HAT itself.

If you use a completely different board you will have to take a look at the
schematics of the board to adjust the configuration. If you need help with this
the best place to ask for help is probably in the forums at 
`tinkerunity.org <https://www.tinkerunity.org>`__.


.. _hat_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: HAT_Brick_hlpi.table
