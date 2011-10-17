.. _step-down:

Step-Down Power Supply
=====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_tilted_front_350.jpg", 
	             "Power_Supplies/powersupply_tilted_front_100.jpg", 
	             "Power_Supplies/powersupply_tilted_front_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_tilted_back_350.jpg", 
	             "Power_Supplies/powersupply_tilted_back_100.jpg", 
	             "Power_Supplies/powersupply_tilted_back_800.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply_caption_350.jpg", 
	             "Power_Supplies/powersupply_caption_100.jpg", 
	             "Power_Supplies/powersupply_caption_800.jpg", 
	             "Power Supply with caption") 
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

The Step-Down Power Supply can be used to power a stack of 
:ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets <product_overview_bricklets>`. 
It is plugged in at the bottom of the stack and creates the
5V needed for Bricks/Bricklets. In addition the applied voltage is feed
into the power signals of the Stack.

There are several possible applications. The Power Supply allows
to create Stacks powered by batteries. These Stacks can then communicate
cable based or wireless with the help of Master Extensions.
Also, the Power Supply can be used to power Motors, Stepper Motors
or Servos without the need to connect external power sources to the
corresponding Bricks. It is also possible to use the power supply in cases
where huge Stacks of Bricks with many Bricklets are needed and the maximum
current of 500mA given over the USB port is not sufficient. 

The possible voltage input range is 6V to 27V. A 
:ref:`Master Brick <master_brick>` can measure the voltage and current that
is drawn from the Power Supply.

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
* Project design files (`Download <https://github.com/Tinkerforge/step-down-powersupply/zipball/master>`__)


Connectivity
------------

The following picture depicts the different connection possibilities of the 
Step-Down Power Supply.

.. image:: /Images/Power_Supplies/powersupply_caption_600.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center
   :target: ../../_images/Power_Supplies/powersupply_caption_800.jpg
