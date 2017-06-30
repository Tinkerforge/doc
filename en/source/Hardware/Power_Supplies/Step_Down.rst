
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Step-Down Power Supply
:shoplink: ../../../shop/power-supplies/step-down-power-supply.html

.. _step_down_power_supply:

Step-Down Power Supply
======================

.. raw:: html

	{% tfgallery %}

	Power_Supplies/powersupply11_tilted_[?|?].jpg              Step-Down Power Supply
	Power_Supplies/powersupply11_caption_[?|?].jpg             Step-Down Power Supply with caption
	Power_Supplies/powersupply11_horizontal_[?|?].jpg          Step-Down Power Supply
	Power_Supplies/powersupply11_connector_[100|600].jpg       Step-Down Power Supply with connectors
	Dimensions/step_down_powersupply_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Powers a stack of Bricks with 5V
* Can power motors of driver Bricks (e.g. DC Brick)
* Input voltage 6V to 27V DC
* Additional output voltage 5V (since hardware version 1.1)


Description
-----------

The Step-Down Power Supply can be used to power a :ref:`stack <primer_stack>` 
of :ref:`Bricks <primer_bricks>` and :ref:`Bricklets <primer_bricklets>`.
It is equipped with an efficient step-down controller and can be plugged in
at the bottom of the stack where it provides the 5V needed for Bricks and
Bricklets. In addition it feeds the external voltage into the stack power signals.
It is not absolutely necessary if you only want to use a single Brick.
But is intended to be used with stacks.

There are several possible applications. The Step-Down Power Supply allows
to create stacks powered by batteries. These stacks can then communicate
cable based or wireless with the help of Master Extensions.
Also, the Step-Down Power Supply can be used to power DC motors, servos or
stepper motors (over the stack power signals with up to 27V DC) without the need
to connect external power sources to the corresponding Bricks. It is also
possible to use the Step-Down Power Supply in cases where huge stacks of Bricks
with many Bricklets are needed and the maximum current of 500mA given over the
USB port is not sufficient.

The possible input voltage range is 6V to 27V DC. A
:ref:`Master Brick <master_brick>` can measure the current consumption of the
stack and the voltage of the external power source. Currents below 200mA can
not be measured satisfactorily.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               20-30mA, depending on Input Voltage
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Minimum/Maximum Input Voltage     6V/27V DC
Maximum Output Current            | 5V Supply: 3A
                                  | Transit for Driver Bricks: 5A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                            14g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/step-down-powersupply/raw/master/hardware/step-down-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/step_down_powersupply_dimensions.png>`__)
* Project design files (`Download <https://github.com/Tinkerforge/step-down-powersupply/zipball/master>`__)
* 3D model (`View online <http://a360.co/2s95Th9>`__ | Download: `STEP <http://download.tinkerforge.com/3d/power_supplies/step_down/step-down.step>`__, `FreeCAD <http://download.tinkerforge.com/power_supplies/step_down/step-down.FCStd>`__)


Connectivity
------------

The following picture depicts the different connection possibilities of the
Step-Down Power Supply.

.. image:: /Images/Power_Supplies/powersupply11_caption_600.jpg
   :scale: 100 %
   :alt: Step-Down Power Supply with caption
   :align: center
   :target: ../../_images/Power_Supplies/powersupply11_caption_800.jpg
