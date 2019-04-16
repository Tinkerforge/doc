
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
* Has eight ports for Bricklets
* Integrates DC power supply (5V-28V input)
* Measures USB and DC supply voltages
* Adds battery backed real-time clock to Raspberry Pi
* Adds low power sleep mode and RPi watchdog


.. _hat_brick_description:

Description
-----------

TBD


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


.. _hat_brick_low_power_sleep_mode:

Low Power Sleep Mode
--------------------


.. _hat_brick_watchdog:

Watchdog
--------


.. _hat_brick_real_time_clock:

Real-Time Clock
---------------


.. _hat_brick_test:

Test your HAT Brick
-------------------

TODO

..
	.. image:: /Images/Bricks/brick_hat_brickv.jpg
	   :scale: 100 %
	   :alt: HAT Brick in Brick Viewer
	   :align: center
	   :target: ../../_images/Bricks/brick_hat_brickv.jpg



.. _hat_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: HAT_Brick_hlpi.table
