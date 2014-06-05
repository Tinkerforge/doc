
:breadcrumbs: <a href="index.html">Home</a> / Primer

.. _primer:

Primer
======

The following description gives an overview for the different products and 
concepts of the Tinkerforge building block system. A detailed description of
the functions and offered APIs can be found in the documentation of each 
product. 

.. _primer_products:

Product Overview
----------------

Our products are divided into five different categories:

* :ref:`Bricks <primer_bricks>`:
  Stackable microcontroller modules for sensing and controlling over USB.
* :ref:`Bricklets <primer_bricklets>`:
  Non-stackable sensor/actuator modules that extend the features of a Brick.
* :ref:`Master Extensions <primer_master_extensions>`:
  Modules that offers alternatives to the USB interface of 
  :ref:`Master Bricks <master_brick>` (WIFI, Ethernet, RS485).
* :ref:`Power Supplies <primer_power_supplies>`:
  Modules to power a stack of Bricks, plugged below the stack.
* :ref:`Accessories <primer_accessories>`

This :ref:`tutorial <tutorial_first_steps>` explains of how everything works 
together.


.. _primer_bricks:

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

Bricks are 4 x 4cm (1.57 x 1.57") modules can be controlled by devices, such as
(embedded) PCs, over its Mini-USB connector. Every Brick basically performs one 
task. There are Bricks that perform complex sensor tasks (e.g. 
:ref:`IMU Brick <imu_brick>`), communicate (e.g. 
:ref:`Master Brick <master_brick>`) and drive motors 
(e.g. :ref:`DC Brick <dc_brick>`).

With :ref:`Bricklets <primer_bricklets>` the features of Bricks can
be extended. Dependent on the Brick it has two or four connectors for Bricklets.

Bricks can be assembled into a stack (see 
:ref:`description of stack concept <primer_stack>`). The USB interface of a 
Master Brick can be replaced by WIFI, Ethernet or RS485 with 
:ref:`Master Extensions <primer_master_extensions>`. In conjunction with the 
stack concept all Bricks and Bricklets can be controlled by WIFI or Ethernet 
instead by USB.





.. include:: Primer_bricks.table


.. _primer_bricklets:

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
:ref:`Bricks <primer_bricks>`. There are Bricklets to measure
physical quantity such as rotation, voltage, current and ambient light
as well as Bricklets for control purposes such as switching relays, digital
input/output and alphanumeric output on LCDs.

Unlike Bricks, Bricklets have no fixed size. Each Bricklet has the minimum
size possible. Each Brick has up to four connectors for Bricklets. Bricklets
can be controlled over the USB connection of the connected Brick.

Bricklets are not equipped with processors but possess their own API.
From the programmer perspective they are handeled as an independent modules.
On startup a Brick detects connected Bricklets. The Bricklet plugins,
stored in the `EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ of the Bricklet,
are loaded into the flash of the Brick. This adds new functions to the Brick,
that can then be used from the PC.


.. include:: Primer_bricklets.table


.. _primer_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_chibi_tilted_100.jpg
       :scale: 100 %
       :alt: Chibi Extension
       :align: center
       :target: _images/Extensions/extension_chibi_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_ethernet_tilted_100.jpg
       :scale: 100 %
       :alt: Ethernet Extension
       :align: center
       :target: _images/Extensions/extension_ethernet_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_rs485_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_wifi_tilted_100.jpg
       :scale: 100 %
       :alt: WIFI Extension
       :align: center
       :target: _images/Extensions/extension_wifi_tilted_800.jpg

If a :ref:`Master Brick <master_brick>` is used on its own or in a 
:ref:`stack <primer_stack>` communication is done by its USB interface.
Master Extensions extends the communication interface of Master Bricks.
There are cable based
(:ref:`RS485 <rs485_extension>`,  :ref:`Ethernet <ethernet_extension>`) and
wireless Master Extensions (:ref:`WIFI <wifi_extension>`) available. Instead
over USB Bricks and Bricklets can be controlled over WIFI or Ethernet. RS485 can
be used to interconnect Bricks and Bricklets over larger distances.

From a programming perspective the different interfaces are transparent.
A stack with Master Extension behaves as if every Brick in the stack
would be directly connected to the PC over an USB connection.

This means: You can develop an application with all modules independently 
connected to the PC over USB. Later you can stack these
modules together to stacks, add Master Bricks and cable based or wireless
Extensions and you can run the previously written code without any changes.

.. include:: Primer_extensions.table


.. _primer_power_supplies:

Power Supplies
^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

:ref:`Bricks <primer_bricks>` and :ref:`Bricklets <primer_bricklets>` can be
powered by the USB connector of the Brick. :ref:`Stacks <primer_stack>` can 
also be powered by the master of the stack over its USB connection. This option 
is limited by the USB specification to 500mA. A large stack may need more power.

To provide greater currents, Power Supplies are available.
These modules power the stack and can additionally be used to supply the power
for driver Bricks (e.g. :ref:`DC Brick <dc_brick>`). Power Supplies
have the same size as :ref:`Bricks <primer_bricks>` and are
stacked in at the bottom of the stack.

.. include:: Primer_power_supplies.table


.. _primer_accessories:

Accessories
^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Accessories/dc_jack_adapter_tilted_100.jpg
       :scale: 100 %
       :alt: DC Jack Adapter
       :align: center
       :target: _images/Accessories/dc_jack_adapter_tilted_800.jpg

.. include:: Primer_accessories.table


Concepts
--------

.. _primer_stack:

Stack of Bricks
^^^^^^^^^^^^^^^

:ref:`Bricks <primer_bricks>` can be stacked. A 
:ref:`Master Brick <master_brick>` (as the lowermost Brick) is responsible for 
the communication between all boards within the stack. This master routes the 
messages between the boards in the stack and the controlling device. This way 
only one USB connection is necessary to control all Bricks and Bricklets of a
stack. For the user, the stack behaves as if all Bricks were connected 
separately over USB with the device. The 
:ref:`stacking tutorial <tutorial_first_steps_build_stacks>` gives more
information about how to use stacks.

With :ref:`Master Extensions <primer_master_extensions>` the USB interface of
a stack can be replaced by Ethernet, WIFI or RS485. If the USB connection does
not deliver enough power :ref:`power supplies <primer_power_supplies>` can be
used to power the stack.

.. _primer_programming:

Programming/API
^^^^^^^^^^^^^^^

A general description of the programming interface can be found 
:ref:`here <programming_interface>`. An overview of the API bindings for each
programming language is given :ref:`here <api_bindings>`. The API of each 
product can be found on each product document page. Additional there can be 
found programming examples for the product in any supported programming 
language.

These Tutorials are an introduction to the usage of Bricks and Bricklets:

* :ref:`First Steps <tutorial_first_steps>`
* :ref:`Rugged Approach <tutorial_rugged_approach>`
* :ref:`Authentication <tutorial_authentication>`
