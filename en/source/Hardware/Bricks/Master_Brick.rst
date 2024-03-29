
:shoplink: ../../../shop/bricks/master-brick.html

.. include:: Master_Brick.substitutions


.. _master_brick:

Master Brick
============

.. raw:: html

	{% tfgallery %}

	Bricks/brick_master3_tilted_front_[?|?].jpg       Master Brick
	Bricks/brick_master3_tilted_back_[?|?].jpg        Master Brick
	Bricks/brick_master3_tilted_front2_[?|?].jpg      Master Brick
	Bricks/brick_master3_stack_front_big_[?|?].jpg    Master Brick in stack
	Bricks/brick_master3_stack_back_big_[?|?].jpg     Master Brick in stack
	Bricks/brick_master3_caption_[?|?].jpg            Master Brick with caption
	Bricks/brick_master3_top_[?|?].jpg                Master Brick top
	Bricks/brick_master3_bottom_[?|?].jpg             Master Brick bottom
	Dimensions/master_brick_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Up to **four** 7-pole Bricklets usable over USB-C
* Is the basis to build stacks
* Usable with cable based and wireless Master Extensions


.. _master_brick_description:

Description
-----------

The Master :ref:`Brick <primer_bricks>` can be used for two purposes:
First of all it has **four** :ref:`Bricklet <primer_bricklets>` ports (7-pole)
and therefore is ideally suited for applications where a many Bricklets are 
used. These can be directly controlled over the **USB-C** interface of the Master
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
1x Master Brick or 1x RED Brick, 8x arbitrary Bricks (excluding RED Brick),
2x Master Extensions. With all Bricks
being Master Bricks in a stack up to 9 Master Bricks x 4 Bricklets each = 36 
Bricklets can be connected to a single stack.

The current Master Brick has hardware version 3.1. The differences to
older version are described in the :ref:`legacy section <master_brick_lagecy>`.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                            12g
Current Consumption               410mW (82mA at 5V)
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/master-brick/raw/master/hardware/master-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/master_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/master-brick/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BbrUnt>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/master/master.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/master/master.FCStd>`__)


.. _master_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the
Master Brick.

.. image:: /Images/Bricks/brick_master3_caption_600.jpg
   :scale: 100 %
   :alt: Master Brick 3.1 with caption
   :align: center
   :target: ../../_images/Bricks/brick_master3_caption_800.jpg


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

.. _master_brick_legacy:

Legacy Master Bricks
--------------------

The Master Brick 3.1 (current version) has USB-C and four 7-pole Bricklet connectors.

.. image:: /Images/Bricks/brick_master3_tilted_front_350.jpg
   :scale: 100 %
   :alt: Master Brick 3.1
   :align: center
   :target: ../../_images/Bricks/brick_master3_tilted_front_800.jpg

Master Bricks with hardware version 1.0, 1.1, 2.0 and 2.1 have Mini-USB and four 10-pole Bricklet connectors.

The old Master Bricks can be used together with legacy 10-pole Bricklets as (10p-10p Bricklet cable
as well as new 7-pole Bricklets (7p-10 Bricklet cable). The new Master Brick is only compatible
to 7-pole Bricklets (with a 7p-7p Bricklet cable).

Master Brick 2.1 is still available in our shop.

.. image:: /Images/Bricks/brick_master21_tilted_front_350.jpg
   :scale: 100 %
   :alt: Master Brick 2.1
   :align: center
   :target: ../../_images/Bricks/brick_master21_tilted_front_800.jpg


Errata Hardware Version 3.1
---------------------------

Embarrassingly we introduced a hardware bug in hardware version 3.1.

In hardware version 3.1 we mixed up two pins on the stack connector that are used with the RS485 Extension.
This bug was introduced in a last-minute change that we did between version 3.0 and 3.1 (3.0 was just used internally and was never released).
Because of this error the RS485 Extension does not work with the Master Brick 3.1.

This will be fixed in the soon to be released Master Brick 3.2.


.. _master_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Master_Brick_hlpi.table
