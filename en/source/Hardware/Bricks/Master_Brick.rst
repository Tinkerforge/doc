
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Master Brick
:shoplink: ../../../shop/bricks/master-brick.html

.. include:: Master_Brick.substitutions


.. _master_brick:

Master Brick
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_master20_tilted_front_350.jpg",
	               "Bricks/brick_master20_tilted_front_600.jpg",
	               "Master Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_master20_tilted_back_100.jpg",
	             "Bricks/brick_master20_tilted_back_600.jpg",
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
	    tfdocimg("Bricks/brick_master20_top_100.jpg",
	             "Bricks/brick_master20_top_600.jpg",
	             "Master Brick top")
	}}
	{{
	    tfdocimg("Bricks/brick_master20_bottom_100.jpg",
	             "Bricks/brick_master20_bottom_600.jpg",
	             "Master Brick bottom")
	}}
	{{
	    tfdocimg("Dimensions/master_brick_dimensions_100.png",
	             "Dimensions/master_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

Features
--------

* Up to **four** Bricklets useable over USB
* Is the basis to build stacks
* Usable with cable based and wireless Master Extensions


Description
-----------

The Master :ref:`Brick <product_overview_bricks>` can be used for two purposes:
First of all it has **four** :ref:`Bricklet <product_overview_bricklets>` ports
and therefore is ideally suited for applications where a many Bricklets are 
used. These can be directly controlled over the **USB** interface of the Master
Brick. This way USB sensors, like temperature or humidity sensors, or USB 
actors, like relais, can be created according to your individual needs.

Secondly, the Master Brick can be used for communication purposes. When 
building a stack the lowermost Master Brick acts as the master of this stack 
and routes all communication between the boards of the stack and the controlling
device. Other Master Bricks in the stack detect that they do not act as a 
master and will only provide their attached Bricklets. This way only one USB
connection, the to the lowermost Master Brick, is necessary.

The USB connection of the Master Brick can be changed with :ref:`Master 
Extensions <product_overview_master_extensions>`. There are Master Extensions 
for cable based interfaces (**RS485**, **Ethernet**) and wireless interfaces 
(**WIFI**). This way Bricks and Bricklets can be directly controlled from 
devices inside a network (WIFI or Ethernet) or can be interconnected over
large distances (RS485).

The maximum stack consists of (bottom to top): 1x Step-Down Power Supply,
1x Master Brick, 8x arbitrarily Bricks, 2x Master Extensions. With all Bricks 
being Master Bricks in a stack up to 9 Master Bricks x 4 Bricklets each = 36 
Bricklets can be connected to a single stack.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                            12g
Current Consumption               68mA
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/master_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)


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

|test_intro|

|test_tab|

.. image:: /Images/Bricks/master_brickv.jpg
   :scale: 100 %
   :alt: Master Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/master_brickv.jpg

You should see that the Master Brick isn't measuring any stack voltages or
currents. This is because you have not attached a
:ref:`Power Supply <product_overview_power_supplies>`. When attaching
such a board you should see the voltage applied to your stack and the current
flowing in.

|test_pi_ref|


.. _master_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Master_Brick_hlpi.table
