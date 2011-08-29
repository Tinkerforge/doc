.. _step-down:

Step-Down Powersupply
=====================

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


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
Maximum Input Current             TBD
Maximum Output Current 5V Supply  3A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            TBD
================================  ============================================================

Resources
---------

 * AOZ1212 Datasheet (`Download <http://www.aosmd.com/res/data_sheets/AOZ1212AI.pdf>`_)
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

.. image:: /Images/Dimensions/step_down_powersupply_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center

Usage
-----
 * explain usage with images


Troubleshoot
------------

