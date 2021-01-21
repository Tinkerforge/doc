
:shoplink: ../../../shop/bricklets/performance-dc-bricklet.html

.. include:: Performance_DC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _performance_dc_bricklet:

Performance DC Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_performance_dc_tilted1_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_top_[?|?].jpg              Performance DC Bricklet
	Bricklets/bricklet_performance_dc_tilted2_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_caption_[?|?].jpg          Performance DC Bricklet
	Bricklets/bricklet_performance_dc_brickv_[100|].jpg          Performance DC Bricklet in Brick Viewer
	Dimensions/performance_dc_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Controls one brushed DC motor with max. **36V** and **10A** (continuously)
* Direction, velocity and acceleration controllable
* Two configurable opto-coupled GPIOs for end-stops or similar
* Status, error, direction and GPIO LEDs
* Configurable overtemperature and overcurrent callbacks


.. _performance_dc_bricklet_description:

Description
-----------

With the Performance DC :ref:`Bricklet <primer_bricks>` you are able to control one 
`DC brushed motor <https://en.wikipedia.org/wiki/Brushed_DC_electric_motor>`__
(max. **36V** and **10A** (continuously)). With the provided API for many
:ref:`programming languages <performance_dc_bricklet_programming_interface>` you can control the 
direction, velocity and acceleration of the connected motor. Additionally, the 
drive mode can be switched between Drive/Brake and Drive/Coast 
(see :ref:`Drive Modes <performance_dc_bricklet_drive_mode>`).

Besides methods to control the connected motor the API provide the possibility
to measure current consumption or the input voltage. 
In case of overtemperature and overcurrent callbacks can be triggered. 

The Bricklet comes with two opto-coupled inputs that can be configured as end-stops.

Six user-configurable status LEDs can be used to show the GPIO state,
motor direction, errors and more.



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               60mW (12mA at 5V) without motor
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Motor Current             10A continous
Minimum/Maximum Input Voltage     6V/36V
PWM Frequency                     Configurable, 1-50kHz, default 20kHz
Velocity                          -32767 to 32767, full reverse to full forward, 0=stop
Acceleration/Deceleration         0 to 65535, velocity/s, increment for velocity/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            80 x 80 x 22mm (3.15 x 3.15 x 0.87")
Weight                            50g
================================  ============================================================


Resources
---------

* DRV8701 datasheet (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/raw/master/datasheets/drv8701.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/raw/master/hardware/performance-dc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/performance_dc_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/performance-dc-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _performance_dc_bricklet_connectivity:


Connectivity
------------

The following picture depicts the different connection possibilities of the
Performance DC Bricklet.

.. image:: /Images/Bricklets/bricklet_performance_dc_caption_600.jpg
   :scale: 100 %
   :alt: Performance DC Bricklet with caption
   :align: center
   :target: ../../_images/Bricklets/bricklet_performance_dc_caption_800.jpg


.. _performance_dc_bricklet_test:

Test your Performance DC Bricklet
---------------------------------

|test_intro|

|test_connect|.
Connect a DC brushed motor and a suitable power supply to the Bricklet and a suitable power supply.

|test_tab|

.. image:: /Images/Bricklets/bricklet_performance_dc_brickv.jpg
   :scale: 100 %
   :alt: Performance DC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_performance_dc_brickv.jpg

Before you can test your Bricklet you need to enable the driver chip by ticking the
"Enable" checkbox. You have four sliders to control
the velocity (forward and backward), the acceleration, deceleration and the
`PWM <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency which
is used by the driver chip to control the connected motor.

On the right you see
the input voltage and the current consumption.
Below you find a graphical representation of the velocity of the motor.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <performance_dc_bricklet_drive_mode>` for more information).

|test_pi_ref|


.. _performance_dc_bricklet_drive_mode:

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


.. _performance_dc_bricklet_error_led:

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


.. _performance_dc_bricklet_case:

Case
----

TBD

..
	A `laser-cut case for the Performance DC Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-performance-dc-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_performance_dc_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Performance DC Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_performance_dc_case_1000.jpg

	.. include:: Performance_DC.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/performance_dc_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Performance DC Bricklet
	   :align: center
	   :target: ../../_images/Exploded/performance_dc_exploded.png

	|bricklet_case_hint|


.. _performance_dc_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Performance_DC_hlpi.table
