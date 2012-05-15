.. _master_brick:

Master Brick
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricks/brick_master_tilted_front_350.jpg", 
	             "Bricks/brick_master_tilted_front_600.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_tilted_back_100.jpg", 
	             "Bricks/brick_master_tilted_back_600.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_stack_front_big_100.jpg", 
	             "Bricks/brick_master_stack_front_big_600.jpg", 
                     "Master Brick in stack")
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_stack_back_big_100.jpg", 
	             "Bricks/brick_master_stack_back_big_600.jpg", 
                     "Master Brick in stack")
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_caption_100.jpg", 
	             "Bricks/brick_master_caption_600.jpg", 
	             "Master Brick with caption") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_top_100.jpg", 
	             "Bricks/brick_master_top_600.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_master_bottom_100.jpg", 
	             "Bricks/brick_master_bottom_600.jpg", 
	             "Master Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/master_brick_dimensions_100.png", 
	             "Dimensions/master_brick_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}

Features
--------

 * Can be used to to build stacks
 * Usable with cable based and wireless extensions
 * One USB port and four Bricklet ports


Description
-----------

The Master :ref:`Brick <product_overview_bricks>`
is equipped with a 32-bit ARM microcontroller and can be
used for two purposes. First of all it has **four** 
:ref:`Bricklet <product_overview_bricklets>` ports and therefore is ideally 
suited for applications where a many Bricklets are used.

Secondly, the Master Brick can be used for communication purposes.
When building a stack the lowermost Master Brick
acts as the master of this stack and routes all communication between the
boards of the stack and the PC. Other Master Bricks in the stack provide their 
attached Bricklets.

Normally the communication with a stack is routed 
over the USB connection of the master. This can be changed with 
:ref:`Master-Extensions <product_overview_master_extensions>`. There are
Master-Extensions for cable based interfaces (RS485, Ethernet) and wireless 
interfaces (Zigbee, WLAN). Extensions are plugged on the topside of the master. 

In the future it will be possible to control the device low level 
via a **I2C**, **SPI** or **UART (serial)** interface from other
microcontroller boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is open source it is possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).
Currently we are not offering an on device API.

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
* Project source code and design files (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)

.. _master_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Master Brick.

.. image:: /Images/Bricks/brick_master_caption_600.jpg
   :scale: 100 %
   :alt: Master Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_master_caption_800.jpg


.. _master_brick_test:

Test your Master Brick
----------------------

To test the Master Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes. 

Connect the Brick to the PC over USB. You should see a tab named
"Master Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/master_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Master Brick
   :align: center
   :target: ../../_images/Bricks/master_brickv.jpg

You should see that the Master Brick isn't measuring any stack voltages or
currents. This is because you have not attached a
:ref:`Power Supply Board <product_overview_powersupplies>`. When attaching
such a board you should see the voltage applied to your stack and the current
flowing in.

After this small test you can go on with writing your own application.
See the :ref:`Programming Interface <master_brick_programming_interfaces>` section 
for  the API of the Master Brick and examples in different programming languages.

.. _master_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Master_Brick_hlpi.table

Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Coming soon! 

  A special firmware is planned to control the Master Brick over 
  SPI, I2C and UART.
  
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

  An API and documentation for direct on device programming (comparable
  to arduino) is planned.
  You can however already use our firmware as a starting point for your 
  own modifications (C knowledge required).

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"

