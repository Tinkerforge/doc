
.. _primer:

Primer
======

The following description gives an overview for the different products and 
concepts of the Tinkerforge building block system. A detailed description of
the functions and offered APIs can be found in the documentation of each 
product. 

.. _primer_products:

Products
--------

Our products are divided into five different categories:

* :ref:`Bricks <primer_bricks>`:
  Stackable microcontroller modules for sensing and controlling over USB.
* :ref:`Bricklets <primer_bricklets>`:
  Non-stackable sensor/actuator modules that extend the features of a Brick.
* :ref:`Master Extensions <primer_master_extensions>`:
  Modules that offers alternatives to the USB interface of 
  :ref:`Master Bricks <master_brick>` (Wi-Fi, Ethernet, RS485).
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

  * - .. image:: /Images/Bricks/brick_red_tilted_top_front_100.jpg
       :scale: 100 %
       :alt: RED Brick
       :align: center
       :target: _images/Bricks/brick_red_tilted_top_front_800.jpg

    - .. image:: /Images/Bricks/brick_master21_tilted_front_100.jpg
       :scale: 100 %
       :alt: Master Brick
       :align: center
       :target: _images/Bricks/brick_master21_tilted_front_800.jpg

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

    - .. image:: /Images/Bricks/brick_imu_v2_tilted1_100.jpg
       :scale: 100 %
       :alt: IMU Brick 2.0
       :align: center
       :target: _images/Bricks/brick_imu_v2_tilted1_800.jpg

.. include:: Primer_bricks.content

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

    - .. image:: /Images/Bricklets/bricklet_analog_in_v2_tilted1_100.jpg
       :scale: 100 %
       :alt: Analog In Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_analog_in_v2_tilted1_800.jpg

.. include:: Primer_bricklets.content

.. include:: Primer_bricklets.table


.. _primer_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_ethernet_tilted_100.jpg
       :scale: 100 %
       :alt: Ethernet Extension
       :align: center
       :target: _images/Extensions/extension_ethernet_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_rs485_v11_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_v11_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_wifi2_tilted_100.jpg
       :scale: 100 %
       :alt: WIFI Extension 2.0
       :align: center
       :target: _images/Extensions/extension_wifi2_tilted_800.jpg

.. include:: Primer_extensions.content

.. include:: Primer_extensions.table


.. _primer_power_supplies:

Power Supplies
^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply11_tilted_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply11_tilted_800.jpg

.. include:: Primer_power_supplies.content

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

.. include:: Primer_accessories.content

.. include:: Primer_accessories.table


Concepts
--------

.. _primer_stack:

Stack of Bricks
^^^^^^^^^^^^^^^

.. image:: /Images/Bricks/brick_master_stack_front_big_350.jpg
    :scale: 100 %
    :alt: Image of Stack of Bricks
    :align: center
    :target: _images/Bricks/brick_master_stack_front_big_800.jpg

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
a stack can be replaced by :ref:`Ethernet <ethernet_extension>`, 
:ref:`Wi-Fi <wifi_extension>` or :ref:`RS485 <rs485_extension>`. 
If the USB connection does not deliver enough power 
:ref:`power supplies <primer_power_supplies>` can be used to power the stack.

.. _primer_programming:

Programming/API
^^^^^^^^^^^^^^^

A general description of the programming interface can be found 
:ref:`here <programming_interface>`. An overview of the API bindings for each
programming language is given :ref:`here <api_bindings>`. The API of each 
product, including examples in any supported programming language, can be found
on each product document page.

These Tutorials are an introduction to the usage of Bricks and Bricklets:

* :ref:`First Steps <tutorial_first_steps>`
* :ref:`Rugged Approach <tutorial_rugged_approach>`
* :ref:`Authentication <tutorial_authentication>`
