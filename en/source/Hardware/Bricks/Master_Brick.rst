
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Master Brick
:shoplink: ../../../shop/bricks/master-brick.html

.. include:: Master_Brick.substitutions


.. _master_brick:

Master Brick
============

.. raw:: html

	{% tfgallery %}

	Bricks/brick_master21_tilted_front_[?|?].jpg      Master Brick
	Bricks/brick_master_stack_front_big_[?|?].jpg     Master Brick in stack
	Bricks/brick_master_stack_back_big_[?|?].jpg      Master Brick in stack
	Bricks/brick_master_caption_[?|?].jpg             Master Brick with caption
	Bricks/brick_master21_top_[?|?].jpg               Master Brick top
	Bricks/brick_master21_bottom_[?|?].jpg            Master Brick bottom
	Dimensions/master_brick_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Up to **four** Bricklets usable over USB
* Is the basis to build stacks
* Usable with cable based and wireless Master Extensions


.. _master_brick_description:

Description
-----------

The Master :ref:`Brick <primer_bricks>` can be used for two purposes:
First of all it has **four** :ref:`Bricklet <primer_bricklets>` ports
and therefore is ideally suited for applications where a many Bricklets are 
used. These can be directly controlled over the **USB** interface of the Master
Brick. This way USB sensors, like temperature or humidity sensors, or USB 
actors, like relays, can be created according to your individual needs.

Secondly, the Master Brick can be used for communication purposes. When 
building a :ref:`stack <primer_stack>` the lowermost Master Brick acts as the 
master of the stack and routes all communication between the boards of the stack 
and the controlling device. Other Master Bricks in the stack detect that are not 
the lowermost Master and will only provide their attached Bricklets. This way 
only one USB connection, the one to the lowermost Master Brick, is necessary.

The USB connection of the Master Brick can be changed with :ref:`Master 
Extensions <primer_master_extensions>`. There are Master Extensions 
for cable based interfaces 
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
or wireless interfaces (:ref:`WIFI <wifi_extension>`). Master Extensions 
have to be plugged on top of a Master Brick and will be detected as new 
interfaces. This way Bricks and Bricklets can be directly controlled from 
devices inside a network (WIFI or Ethernet) or can be interconnected over
large distances (RS485).

The maximum stack consists of (bottom to top): 1x Step-Down Power Supply,
1x Master Brick, 8x arbitrary Bricks, 2x Master Extensions. With all Bricks 
being Master Bricks in a stack up to 9 Master Bricks x 4 Bricklets each = 36 
Bricklets can be connected to a single stack.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 19mm (1.57 x 1.57 x 0.75")
Weight                            12g
Current Consumption               410mW (82mA at 5V)
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/master_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)
* 3D model (`View online <http://a360.co/2spaP0V>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricks/master/master.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricks/master/master.FCStd>`__)


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
:ref:`Power Supply <primer_power_supplies>`. When attaching
such a board you should see the voltage applied to your stack and the current
flowing in.

|test_pi_ref|


.. _master_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Master_Brick_hlpi.table
