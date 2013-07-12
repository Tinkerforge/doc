
:breadcrumbs: <a href="index.html">Home</a> / Product Overview

.. _product_overview:

Product Overview
================

Our products are divided into five different categories:

* :ref:`Bricks <product_overview_bricks>`:
  Stackable microcontroller boards for sensing and controlling.
* :ref:`Bricklets <product_overview_bricklets>`:
  Non-stackable sensor/actor boards that extend the features of a Brick.
* :ref:`Master Extensions <product_overview_master_extensions>`:
  Boards that extend the communication interfaces of a
  :ref:`Master Brick <master_brick>`.
* :ref:`Power Supplies <product_overview_power_supplies>`:
  Boards to power a stack of Bricks, plugged below the stack.
* :ref:`Accessories <product_overview_accessories>`

See the :ref:`tutorial <tutorial_first_steps>` for an explanation of how
everything works together.


.. _product_overview_bricks:

Bricks
------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricks/brick_master_tilted_front_100.jpg
       :scale: 100 %
       :alt: Master Brick
       :align: center
       :target: _images/Bricks/brick_master_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_dc_tilted_front_100.jpg
       :scale: 100 %
       :alt: DC Brick
       :align: center
       :target: _images/Bricks/brick_dc_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_stepper_tilted_front_100.jpg
       :scale: 100 %
       :alt: Stepper Brick
       :align: center
       :target: _images/Bricks/brick_stepper_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_servo_tilted_front_100.jpg
       :scale: 100 %
       :alt: Servo Brick
       :align: center
       :target: _images/Bricks/brick_servo_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_imu_tilted_front_100.jpg
       :scale: 100 %
       :alt: IMU Brick
       :align: center
       :target: _images/Bricks/brick_imu_tilted_front_800.jpg

Bricks are 4 x 4cm (1.57 x 1.57") boards equipped with a 32-bit ARM
microcontroller, an USB port, two status LEDs, connectors for
stacking and up to four connectors for
:ref:`Bricklets <product_overview_bricklets>`.
There are Bricks that perform complex
sensor tasks (e.g. :ref:`IMU Brick <imu_brick>`),
communicate (e.g. :ref:`Master Brick <master_brick>`)
and drive motors (e.g. :ref:`DC Brick <dc_brick>`).

Bricks can be assembled into a stack. A Master Brick at the bottom of a
stack is responsible for the communication all boards within the stack.
This master routes the messages between the boards in the stack and the PC
(:ref:`High Level Programming Interface <pi_hlpi>`).
For the user, the stack behaves as if all Bricks were connected separately
over USB with the PC.
See the :ref:`stacking tutorial <tutorial_first_steps_build_stacks>` for more
information about stacks.

Besides the :ref:`High Level Programming Interface <pi_hlpi>` it will also
possible to use Bricks with an :ref:`On Device Programming Interface <pi_odpi>`.

.. include:: Product_Overview_bricks.table


.. _product_overview_bricklets:

Bricklets
---------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricklets/bricklet_dual_relay_tilted_100.jpg
       :scale: 100 %
       :alt: Dual Relay Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_dual_relay_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_joystick_tilted_100.jpg
       :scale: 100 %
       :alt: Joystick Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_joystick_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_lcd_20x4_tilted_100.jpg
       :scale: 100 %
       :alt: LCD 20x4 Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_lcd_20x4_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_temperature_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Temperature IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_temperature_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_linear_poti_tilted_100.jpg
       :scale: 100 %
       :alt: Linear Poti Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_linear_poti_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_distance_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Distance IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_distance_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_voltage_tilted_100.jpg
       :scale: 100 %
       :alt: Voltage Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_voltage_tilted_800.jpg

Bricklets can be used to extend the features of
:ref:`Bricks <product_overview_bricks>`. There are Bricklets to measure
physical quantity such as rotation, voltage, current and ambient light
as well as Bricklets for control purposes such as switching relays, digital
input/output and alphanumeric output on LCDs.

Unlike Bricks, Bricklets have no fixed size. Each Bricklet has the minimum
size possible. Each Brick has up to four connectors for Bricklets.

On startup a Brick detects connected Bricklets. The Bricklet plugins,
stored in the `EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ of the Bricklet,
are loaded into the flash of the Brick. This adds new functions to the Brick,
that can then be used from the PC.

See :ref:`High Level Programming Interface <pi_hlpi>` for more information.

.. include:: Product_Overview_bricklets.table


.. _product_overview_master_extensions:

Master Extensions
-----------------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_chibi_tilted_100.jpg
       :scale: 100 %
       :alt: Chibi Extension
       :align: center
       :target: _images/Extensions/extension_chibi_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_rs485_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_tilted_800.jpg

When using the :ref:`High Level Programming Interface <pi_hlpi>` concept,
:ref:`Master Bricks <master_brick>` can route messages between
:ref:`Bricks <product_overview_bricks>` and the PC. To establish a connection
between a PC and the Master Brick, typically the USB port is used.
Master Extensions can be utilized to change the interface of a Master Brick.
There are cable based and wireless Master Extensions available. From a
programming perspective the different interfaces are transparent.
A stack with Master Extension behaves as if every board in the stack
would be directly connected to the PC over an USB connection.

This means: You can develop an application with all
boards independently connected to the PC over USB. Later you can stack these
boards together to stacks, add Master Bricks and cable based or wireless
Extensions and you can run the previously written code without any changes.

.. include:: Product_Overview_extensions.table


.. _product_overview_power_supplies:

Power Supplies
--------------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

A stack can be powered by the master of the stack over its USB connection.
This option is limited by the USB specification to 500mA.
A large stack may need more power than 500mA.

To provide greater currents, Power Supplies are available.
These boards power the stack and can additionally be used to supply the power
for driver Bricks (e.g. :ref:`DC Brick <dc_brick>`). Power Supplies
have the same size as :ref:`Bricks <product_overview_bricks>` and are
stacked in at the bottom of the stack.

.. include:: Product_Overview_power_supplies.table


.. _product_overview_accessories:

Accessories
-----------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Accessories/dc_jack_adapter_tilted_100.jpg
       :scale: 100 %
       :alt: DC Jack Adapter
       :align: center
       :target: _images/Accessories/dc_jack_adapter_tilted_800.jpg

.. include:: Product_Overview_accessories.table
