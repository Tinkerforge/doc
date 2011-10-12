.. _master_brick:

Master Brick
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricks/brick_master_tilted_front_350.jpg", 
	             "Bricks/brick_master_tilted_front_100.jpg", 
	             "Bricks/brick_master_tilted_front_800.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_tilted_back_350.jpg", 
	             "Bricks/brick_master_tilted_back_100.jpg", 
	             "Bricks/brick_master_tilted_back_800.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_stack_front_big_350.jpg", 
	             "Bricks/brick_master_stack_front_big_100.jpg", 
	             "Bricks/brick_master_stack_front_big_1200.jpg", 
	             "Master Brick in Stack") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_stack_back_big_350.jpg", 
	             "Bricks/brick_master_stack_back_big_100.jpg", 
	             "Bricks/brick_master_stack_back_big_1200.jpg", 
	             "Master Brick in Stack") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_top_350.jpg", 
	             "Bricks/brick_master_top_100.jpg", 
	             "Bricks/brick_master_top_800.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_bottom_350.jpg", 
	             "Bricks/brick_master_bottom_100.jpg", 
	             "Bricks/brick_master_bottom_800.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/dc_brick_dimensions_350.png", 
	             "Dimensions/dc_brick_dimensions_100.png", 
	             "Dimensions/dc_brick_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

The Master :ref:`Brick <product_overview_bricks>`
is equipped with a 32-bit ARM microcontroller and can be
used for two purposes. First of all it has **four** 
:ref:`Bricklet <product_overview_bricklets>` ports and therefore is ideally 
suited for applications where a great many of Bricklets are used.

Secondly, the Master Brick can be used for communication purposes.
When building a stack the lowermost Master Brick
acts as the master of this stack and routes all communication between the
boards of the stack and the PC. Other Master Bricks in the stack detect this 
and does not act as master. They are only provide their attached Bricklets.

In the simple case the communication with a stack is routed 
over the USB connection of the master. This interface can be changed with 
:ref:`Master-Extensions <product_overview_master_extensions>`. There are
Master-Extensions for cablebased interfaces (RS485, Ethernet) and wireless interfaces (Zigbee, WLAN). 
Extensions will be plugged on the topside of the master. The master detect them
and use this additional interface.

In the future it will be possible to control the device low level 
via a **I2C**, **SPI** or **UART (serial)** interface from other microcontroller boards
(:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Microcontroller                   ATSAM3S4C (256kB Flash, 48k RAM)
--------------------------------  ------------------------------------------------------------
Device Current Consumption        53mA
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            12g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/master_brick_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__

.. _master_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Master Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: Connectivity of Master Brick
   :align: center
   :target: ../../_images/Bricks/servo_brick_anschluesse.jpg


.. _master_brick_test:

Test your Master Brick
----------------------

To test your Master Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes. 

Connect the Brick to the PC over USB. You should see a tab named
"Master Brick" in the Brick Viewer after you pressed "connect", select it.

.. image:: /Images/Bricks/master_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Master Brick
   :align: center
   :target: ../../_images/Bricks/master_brickv.jpg

You should see that the Master Brick isn't measuring any Stack voltages or 
currents. This is because you have not attached a
:ref:`Power-Supply Board <product_overview_powersupplies>`. When attaching
such a board you should see the voltage applied to your Stack and the current
flowing in.

After this small test you can go on with writing your own application.
See :ref:`Interface and Coding <master_brick_programming_interfaces>` section for 
the API of the Master Brick and examples in your programming language.

.. _master_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <master_brick_c_api>`", ":ref:`Examples <master_brick_c_examples>`", "Installation"
   "C#", ":ref:`API <master_brick_csharp_api>`", ":ref:`Examples <master_brick_csharp_examples>`", "Installation"
   "Java", ":ref:`API <master_brick_java_api>`", ":ref:`Examples <master_brick_java_examples>`", "Installation"
   "Python", ":ref:`API <master_brick_python_api>`", ":ref:`Examples <master_brick_python_examples>`", "Installation"


Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Comming soon! 

  Currently you have to modify the firmware to use this feature.
  SPI, I2C and UART interface are present and can be easily accessed with our
  :ref:`Breakout Board <breakout_brick>`. A special firmware is planned
  to control this brick over the different interfaces by transmitted commands.
  
..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "SPI", "API", "Examples", "Installation"
     "I2C", "API", "Examples", "Installation"
     "UART(serial)", "API", "Examples", "Installation"


On Device Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note:: Coming soon!

  Currently no API or special documentation exists for direct programming.
  You can use our firmware as startingpoint for your own modifications.

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"

