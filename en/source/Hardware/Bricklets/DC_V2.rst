
:DISABLED_shoplink: ../../../shop/bricklets/dc-v2-bricklet.html

.. include:: DC_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dc_v2_bricklet:

DC Bricklet 2.0
===============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dc_v2_tilted_[?|?].jpg           DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_w_connector_[?|?].jpg      DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_tilted2_[?|?].jpg          DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_horizontal_[?|?].jpg       DC Bricklet 2.0
	Bricklets/bricklet_dc_v2_w_motor_[?|?].jpg          DC Bricklet 2.
	Bricklets/bricklet_dc_v2_brickv_[100|].jpg          DC Bricklet 2.0 in Brick Viewer
	Dimensions/dc_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Controls one brushed DC motor with max. **28V** and **5A** (peak) over USB
* API for many programming languages available
* Direction, velocity and acceleration controllable
* Configurable overtemperature and overcurrent callbacks


.. _dc_v2_bricklet_description:

Description
-----------

With the DC :ref:`Bricklet <primer_bricklets>` 2.0 you are able to control one 
`DC brushed motor <https://en.wikipedia.org/wiki/Brushed_DC_electric_motor>`__
(max. **28V** and **5A** (peak)) over **USB**. With the provided API for many
:ref:`programming languages<dc_brick_programming_interface>` you can control the 
direction, velocity and acceleration of the connected motor.

Besides methods to control the connected motor the API provide the possibility
to measure current consumption and the voltage of the power supply. 
In case of overtemperature and overcurrent callbacks can be triggered. 
These can be used to react properly in your own program to these events.

The drive  mode can be switched between Drive/Brake and Drive/Coast 
(see :ref:`Drive Modes <dc_brick_drive_mode>`).

The DC Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               50mW (10mA at 5V) without motor
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Motor Current             | Peak: 5A
                                  | Continous: > 3A (depends on cooling)
Minimum/Maximum Input Voltage     6V/28V
PWM Frequency                     Configurable, 1-20kHz, default 15kHz
Velocity                          -32767 to 32767, full reverse to full forward, 0=stop
Acceleration                      0 to 65535, velocity/s, increment for velocity/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 15mm (1,57 x 1,57 x 0,59")
Weight                            12g
================================  ============================================================


Resources
---------

* MC33926 datasheet (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/raw/master/datasheets/MC33926.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/raw/master/hardware/dc-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dc_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dc-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://a360.co/3gNZ8h1>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/dc_v2/dc-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/dc_v2/dc-v2.FCStd>`__)


Connectivity
------------

The following picture depicts the different connection possibilities of the
DC Bricklet 2.0.

.. image:: /Images/Bricklets/bricklet_dc_v2_caption_600.jpg
   :scale: 100 %
   :alt: DC Bricklet 2.0 with caption
   :align: center
   :target: ../../_images/Bricklets/bricklet_dc_v2_caption_800.jpg


.. _dc_v2_bricklet_test:

Test your DC Bricklet 2.0
-------------------------

|test_intro|

|test_connect|.
Connect a DC brushed motor and a suitable power supply to the Bricklet and a suitable power supply.

|test_tab|

.. image:: /Images/Bricklets/bricklet_dc_v2_brickv.jpg
   :scale: 100 %
   :alt: DC Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dc_v2_brickv.jpg

|test_pi_ref|

Before you can test your Bricklet you need to enable the driver chip by ticking the
"Enable" checkbox. You have four sliders to control
the velocity (forward and backward), the acceleration, deceleration and the
`PWM <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency which
is used by the driver chip to control the connected motor.

On the right you see the input voltage and the current consumption.
Below you find a graphical representation of the velocity of the motor.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <dc_v2_bricklet_drive_mode>` for more information).


.. _dc_v2_bricklet_drive_mode:

Drive Modes
-----------

There are two possible modes of motor controls:

* Drive/Brake

  In this mode the motor is always either driving or braking, there is no
  freewheeling possible. A more linear correlation between PWM and velocity
  is an advantage of this mode.
  Therefore it is possible to accelerate more precise.
  Typically motors can be driven with slower velocities in this mode.
  Disadvantageous is a higher current consumption and a resulting faster
  heat-up of the driver chip.

* Drive/Coast

  In this mode the motor is either driving or freewheeling.
  Advantageous is a lower current consumption and a resulting slower heat-up.
  The control of the velocity and acceleration is less precise, it can
  "lag behind".


.. _dc_v2_bricklet_error_led:

Error LED
---------

The red error LED has three different states:

* Off: No error present.
* 1s interval blinking: Input voltage too low (below 6V).
* 250ms interval blinking: Overtemperature or overcurrent.

If an over-temperature or -current event occurs the motor
will stop running and the driver will be turned off. 
You need to explicitely call the enable function to start
the driver again.


.. _dc_v2_bricklet_case:

Case
----

TBD

..
	A `laser-cut case for the DC Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-dc-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_dc_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for DC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_dc_v2_case_1000.jpg

	.. include:: DC_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/dc_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for DC Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/dc_v2_exploded.png

	|bricklet_case_hint|


.. _dc_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: DC_V2_hlpi.table
