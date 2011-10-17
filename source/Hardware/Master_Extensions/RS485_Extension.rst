.. _rs485_extension:

RS485 Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Extensions/extension_rs485_tilted_front_350.jpg", 
	             "Extensions/extension_rs485_tilted_front_100.jpg", 
	             "Extensions/extension_rs485_tilted_front_800.jpg", 
	             "RS485 Extension") 
	}}
	{{ tfdocend() }}

Description
-----------

The RS485 Extension can be used for long range cable based
inter-stack communication. It uses the RS485 differential interface
standard to achieve ranges of **up to 1200m**.

To establish a RS485 bus with Bricks, two RS485 Extensions and two
Master Bricks are needed. Both Master Bricks can be connected to a
full stack of Bricks and Bricklets, whereas one Master Brick is Battery
powered and one is connected with USB. From a programming perspective
the RS485 bus is completely transparent, i.e. the two stacks can
be used exactly the same way as if they were both connected via USB.

It is also possible to create a bus with several RS485 Extension where
only one is connected via USB (many-to-one routing).


.. note:: Coming soon! 
   The RS485 Extension is not yet available to buy.

..
	Technical Specifications
	------------------------

	================================  ============================================================
	Property                          Value
	================================  ============================================================
	Device Current Consumption        TBD
	Maximum Baud Rate                 TBD
	--------------------------------  ------------------------------------------------------------
	--------------------------------  ------------------------------------------------------------
	Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
	Weight                            13g
	================================  ============================================================


	Resources
	---------

	* Schematic (Download)
	* Outline and drilling plan (`Download <../../_images/Dimensions/rs485_extension_dimensions.png>`__)
	* Project source code and design files (Download)


.. RS485 Bus Assembly
  ------------------
  * Picture Bus
  * explain termination


.. Connectivity
  ------------
  The following picture depicts the different connection possibilities of the 
  485-Extension.
  .. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

.. Troubleshoot
   ------------

