.. _step-down:

Step-Down Power Supply
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Power_Supplies/powersupply11_tilted_350.jpg", 
	             "Power_Supplies/powersupply11_tilted_600.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply11_caption_100.jpg", 
	             "Power_Supplies/powersupply11_caption_600.jpg", 
	             "Power Supply with caption") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply11_horizontal_100.jpg", 
	             "Power_Supplies/powersupply11_horizontal_600.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Power_Supplies/powersupply11_connector_100.jpg", 
	             "Power_Supplies/powersupply11_connector_600.jpg", 
	             "Power Supply") 
	}}
	{{ 
	    tfdocimg("Dimensions/step_down_powersupply_dimensions_100.png", 
	             "Dimensions/step_down_powersupply_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Powers a stack of Bricks with 5V
 * Can power motors of driver Bricks, e.g. DC Brick
 * Input voltage 6V to 27V
 * Additional output voltage 5V (since version 1.1)

Description
-----------

The Step-Down Power Supply can be used to power a stack of 
:ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets <product_overview_bricklets>`. 
It is plugged in at the bottom of the stack and creates the
5V needed for Bricks/Bricklets. In addition the applied voltage is feed
into the power signals of the stack.

There are several possible applications. The Step-Down Power Supply allows
to create stacks powered by batteries. These stacks can then communicate
cable based or wireless with the help of Master Extensions.
Also, the Step-Down Power Supply can be used to power motors, stepper motors
or servos without the need to connect external power sources to the
corresponding Bricks. It is also possible to use the Step-Down Power Supply in cases
where huge stacks of Bricks with many Bricklets are needed and the maximum
current of 500mA given over the USB port is not sufficient. 

The possible voltage input range is 6V to 27V. A 
:ref:`Master Brick <master_brick>` can measure the voltage and current that
is drawn from the Step-Down Power Supply. The current measurement can be used to
measure the current consumption of a stack in case of driver bricks (stepper, dc etc.)
are used. Currents below 200mA are not adequate measureable.

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

.. image:: /Images/Power_Supplies/powersupply11_caption_600.jpg
   :scale: 100 %
   :alt: Step-Down Power Supply with caption
   :align: center
   :target: ../../_images/Power_Supplies/powersupply11_caption_800.jpg
