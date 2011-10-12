.. _step-down:

Step-Down Powersupply
=====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_dc_tilted_front_350.jpg", 
	             "Power_Supplies/powersupply_dc_tilted_front_100.jpg", 
	             "Power_Supplies/powersupply_dc_tilted_front_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_dc_tilted_back_350.jpg", 
	             "Power_Supplies/powersupply_dc_tilted_back_100.jpg", 
	             "Power_Supplies/powersupply_dc_tilted_back_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_top_350.jpg", 
	             "Power_Supplies/powersupply_top_100.jpg", 
	             "Power_Supplies/powersupply_top_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_bottom_350.jpg", 
	             "Power_Supplies/powersupply_bottom_100.jpg", 
	             "Power_Supplies/powersupply_bottom_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Dimensions/step_down_powersupply_dimensions_350.png", 
	             "Dimensions/step_down_powersupply_dimensions_100.png", 
	             "Dimensions/step_down_powersupply_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

This powersupply can plugged below a stack to power it.
It is equipped with a high efficiency buck regulator.
You can connect an external power source (6V-27V)
like a battery to this device and it creates 5V for all
:ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets <product_overview_bricklets>`
of the stack.
Besides it connects the external power source with the
stack power signals, such that driver Bricks can use this power source
to power external motors. The :ref:`Master Brick <master_brick>`
which acts as master of the stack can measure the drawn current
and the voltage of the external power source.

The device is short circuit protected but an external fuse is recommended.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Minimum/Maximum Input Voltage     6V/27V
Device Current Consumption        20-30mA (depending on Input Voltage)
Maximum Input Current             TBD
Maximum Output Current 5V Supply  3A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            14g
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/step-down-powersupply/raw/master/hardware/step-down-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/step_down_powersupply_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/step-down-powersupply/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__

Connectivity
------------

The following picture depicts the different connection possibilities of the 
powersupply.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center
   :target: ../../_images/Bricks/servo_brick_anschluesse.jpg

Troubleshoot
------------

