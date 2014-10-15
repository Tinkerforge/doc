
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / DC Brick
:shoplink: ../../../shop/bricks/dc-brick.html

.. include:: DC_Brick.substitutions


.. _dc_brick:

DC Brick
========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_dc_tilted_front_350.jpg",
	               "Bricks/brick_dc_tilted_front_600.jpg",
	               "DC Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_tilted_back_100.jpg",
	             "Bricks/brick_dc_tilted_back_600.jpg",
	             "DC Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_motor_setup_100.jpg",
	             "Bricks/brick_dc_motor_setup_600.jpg",
	             "DC Brick with motor")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_caption_100.jpg",
	             "Bricks/brick_dc_caption_600.jpg",
	             "DC Brick with caption")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_top_100.jpg",
	             "Bricks/brick_dc_top_600.jpg",
	             "DC Brick top")
	}}
	{{
	    tfdocimg("Bricks/brick_dc_bottom_100.jpg",
	             "Bricks/brick_dc_bottom_600.jpg",
	             "DC Brick bottom")
	}}
	{{
	    tfdocimg("Dimensions/dc_brick_dimensions_100.png",
	             "Dimensions/dc_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Controls one brushed DC motor with max. **28V** and **5A** (peak) over USB
* API for many programming languages available
* Direction, velocity and acceleration controllable
* Extendable via two Bricklets ports
* Configurable overtemperature and overcurrent callbacks

.. _dc_brick_description:

Description
-----------

With the DC :ref:`Brick <primer_bricks>` you are able to control one 
`DC brushed motor <http://en.wikipedia.org/wiki/Brushed_DC_electric_motor>`__
(max. **28V** and **5A** (peak)) over **USB**. With the provided API for many
:ref:`programming languages<dc_brick_programming_interface>` you can control the 
direction, velocity and acceleration of the connected motor.

Two :ref:`Bricklet <primer_bricklets>` ports can be used to extend the 
features of this Brick. It can also be used together with other Bricks in a
:ref:`stack <primer_stack>`. For example an additional 
:ref:`Master Brick <master_brick>` with
:ref:`Master Extension <primer_master_extensions>` allows 
to replace the USB connection by other cable based
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
or wireless (:ref:`WIFI <wifi_extension>`) connections.

Besides methods to control the connected motor the API provide the possibility
to measure current consumption or the voltage of the power supply. 
In case of overtemperature and overcurrent callbacks can be triggered. 
These can be used to react properly in your own program to these events.
For battery driven applications an undervoltage callback is user configurable to 
prevent damaging batteries caused by depth discharge. Additionally, the drive 
mode can be switched between Drive/Brake and Drive/Coast 
(see :ref:`Drive Modes <dc_brick_drive_mode>`).

With the power supply connector jack (black) motors can be powered directly. If 
a stack is used, the connected motors can also be powered through the stack. 
The Brick switches automatically to the external power supply if connected.





Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Maximum Motor Current             | Peak: 5A
                                  | Continous: > 3A (depends on cooling)
Minimum/Maximum Input Voltage     6V/28V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
PWM Frequency                     Configurable, 1-20kHz, default 15kHz
Velocity                          -32767 to 32767, full reverse to full forward, 0=stop
Acceleration                      0 to 65535, velocity/s, increment for velocity/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40 x 40 x 17mm (1.57 x 1.57 x 0.67")
Weight                            18g
Current Consumption               53mA
================================  ============================================================


Resources
---------

* MC33926 datasheet (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/datasheets/MC33926.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/hardware/dc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dc_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dc-brick/zipball/master>`__)

.. _dc_brick_connectivity:


Connectivity
------------

The following picture depicts the different connection possibilities of the
DC Brick.

.. image:: /Images/Bricks/brick_dc_caption_600.jpg
   :scale: 100 %
   :alt: DC Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_dc_caption_800.jpg

.. _dc_brick_test:


Test your DC Brick
------------------

|test_intro|

Connect a DC brushed motor to the Brick and a suitable power supply.
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick with motor
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

Before you can test your Brick you need to enable the driver chip by ticking the
"Enable" checkbox. You have three sliders to control
the velocity (forward and backward), the acceleration and the
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency which
is used by the driver chip to control the connected motor.

On the right you see
the voltages of the two power sources and the current consumption.
Below you find a graphical representation of the velocity of the motor.
At the bottom you can configure the minimum motor voltage, which allows for
undervoltage callbacks if the voltage is too low.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <dc_brick_drive_mode>` for more information).

|test_pi_ref|


Power Supply
------------

The connected motor can be powered through the black on-board power-connector
or through a :ref:`Power Supply <primer_power_supplies>` in a
stack. The Brick switches automatically to the on-board power-connector when a 
voltage above 1V is measured there.


.. warning::
  Keep in mind that the Brick switches automatically. So e.g. if you have a stack
  and remove your external battery connected to the Brick it will use the 
  stack power supply. If you then enable the motor it is driver with the voltage
  supplied by the stack which might be higher then your battery voltage
  

.. _dc_brick_drive_mode:


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


Error LED
---------

The red LED is enabled if the supply voltage is below the minimum voltage
(configurable) or the driver chip is in emergency shutdown state.

An emergency shutdown is triggered if either the current consumption
is too high (above 5A) or the temperature of the driver chip is too high
(above 175°C). These two possibilities are essentially the same, since the
temperature will reach this threshold immediately if the motor consumes too
much current.

To get the Brick operational again you have to increase the voltage or in the
latter case you have to let the driver chip cool down and enable it again.


.. _dc_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: DC_Brick_hlpi.table


..
	FAQ
	---

	Motor is not running correctly
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	**Reasons:**
	 * Voltage drop, caused by the connected motor.
	 * Low input voltage for the DC Brick.
	 * Not correctly connected.
	 * Defective motor.

	**Solutions:**
	 * Check input voltage. If too low, increase voltage.
	 * More powerful power supply. Typically batteries are better suited than wall power adapters.
	 * In case of you are using batteries to power the device, check the voltage of
	   the batteries and keep in mind that this voltage can break-in while delivering
	   high currents.
	 * Reduce the load of the motor.
	 * Check connection between Brick and motor.
	 * Change Motor when defect.
