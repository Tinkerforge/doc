.. _product_overview:

Product Overview
----------------

There are four different types of hardware components:

* :ref:`Bricks <product_overview_bricks>`: 
  Stackable microcontroller boards for sensing and controlling.
* :ref:`Master Extensions <product_overview_master_extensions>`:
  Boards that extend the communication interfaces of a
  :ref:`Master Brick <master_brick>`.
* :ref:`Bricklets <product_overview_bricklets>`:
  Non-stackable sensor/actor boards that extend the features of a Brick.
* :ref:`Power Supplies <product_overview_powersupplies>`:
  Boards to power a stack of Bricks, plugged below the stack.


See the :ref:`tutorial <tutorial>` for an explanation of how everything works
together.


.. _product_overview_bricks:

Bricks
^^^^^^

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


Bricks are 4 x 4cm (1.57" x 1.57") boards equipped with a 32bit
microcontroller, an USB port, two status LEDs, connectors for 
stacking and up to four connectors for 
:ref:`Bricklets <product_overview_bricklets>`. 
There are Bricks that perform complex 
sensor tasks (e.g. :ref:`IMU Brick <imu_brick>`), 
communicate (e.g. :ref:`Master Brick <master_brick>`) 
and drive motors (e.g. :ref:`DC Brick <dc_brick>`).

Bricks can be stacked together to a stack. A Master Brick
at the bottom of this stack can control all boards within the stack.
This master routes the messages between the boards in the stack and the PC
(:ref:`High Level Programming Interface <pi_hlpi>`).
For the user, the stack behaves as if all Bricks were connected separately 
over USB with the PC. 
See :ref:`Tutorial Stacking <tutorial_build_stacks>` for more information
about stacks.

Besides the :ref:`High Level Programming Interface <pi_hlpi>` it is also
possible to use Bricks with the :ref:`On Device Programming Interface <pi_hlpi>`.

.. include:: Product_Overview_bricks.table

.. _product_overview_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

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
would be directly connected to the PC over an USB connection. This means:

You can develop an application with all
boards independently connected to the PC over USB. Later you can stack these 
boards together to stacks, add Master Bricks and cable based or wireless
Extensions and you can run the previously written code without any changes.

.. csv-table::
   :header: "Name", "Description"
   :widths: 20, 70 

   ":ref:`chibi_extension`", "Wireless Chibi Master Extension"
   ":ref:`rs485_extension`", "Cable based RS485 Master Extension"


.. _product_overview_bricklets:

Bricklets
^^^^^^^^^

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
physical values such as rotation, voltage, current and ambient light
as well as Bricklets for control purposes such as
switching relays, digital input/output and drawing on LCDs. 

Unlike Bricks, Bricklets have no fixed size. Each Bricklet has the minimum 
size possible. Each Brick has up to four connectors for Bricklets.

On startup a Brick detects connected Bricklets. The Bricklet plugins,
stored in the EEPROM of the Bricklet, are copied into the flash of the
Brick. This adds methods to the Brick, that can then be called from the PC.

See :ref:`High Level Programming Interface <pi_hlpi>` for more information.

.. include:: Product_Overview_bricklets.table

.. _product_overview_powersupplies:

Power Supplies
^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

A stack can be powered by the
master of the stack over its USB connection. 
This option is limited by the USB specification (500mA). 
A large stack may need more power than 500mA.

To provide greater currents, Power Supplies are available.
These boards power the stack and can additionally be used to supply the power
for driver Bricks (e.g. :ref:`DC Brick <dc_brick>`). Power Supplies
have the same size as :ref:`Bricks <product_overview_bricks>` and are
stacked in at the bottom of the stack.

.. csv-table::
   :header: "Name", "Description"
   :widths: 30, 60

   ":ref:`step-down`", "Powers a stack with 6-27V input"

