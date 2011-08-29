.. _rs485_extension:

RS485 Extension
===============

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

Two or more of this 
:ref:`Master Extension <product_overview_master_extensions>` with one
:ref:`Master Bricks <master_brick>` each
can be used to create a `RS-485 bus <http://en.wikipedia.org/wiki/RS-485>`_
between them. 
Each Master Brick can be a master of a stack. Using our
:ref:`High Level Concept <pi_hlpi>` this bus
is completely transparent, which means that each device in this bus
is usable like it would be connected to the PC with its own USB connection.
You can write the same programming code.

Since RS485 is differental interface standard, information can be communicated
over large distances. Therefore this interface is better suited to connect a
stack cable-based to a PC than USB when it is further away.

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
Weight                            TBD
================================  ============================================================


RS485 Bus Assembly
------------------
 * Picture Bus
 * explain termination

Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Connectivity
------------

The following picture depicts the different connection possibilities of the 
485-Extension.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/rs485-extension_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


.. Powersupply
.. ^^^^^^^^^^^

.. Todo: Bildchen


Usage
-----

 * Explain usage

Troubleshoot
------------

