.. _distance_ir_bricklet:

Distance IR
===========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The Distance IR :ref:`Bricklet <product_overview_bricklets>` can extend the features of
every :ref:`Brick <product_overview_bricks>` by the possibility to
measure distances. The Bricklet can be attached to `Sharp <http://www.sharpsma.com>`_ 
analog infrared proximity sensors. 
After configuring the attached sensor you can read out the measured distance 
directly in millimeters. You can configure events triggered when a specified distance
is exceeded, this supersede polling.

Typically these sensors are used in robotics to measure distances for mapping or 
localization purposes. But you can also use these sensors in other applications.
For example you may like to switch something when someone enters a room. 
You can install the sensor in the entrance in that way that if someone enters the room 
the measured distance will be smaller.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        13mm x 44.6mm (0.51" x 1.76") fitting on backside of sensor
Weight
Current Consumption
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor Range                      Depends on attached Sharp IR Sensor:

                                  * GP2D120XJ00F:   4- 30cm (1.57" - 11.81")
                                  * GP2Y0A21YK0F:  10- 80cm (3.94" - 31.50")
                                  * GP2Y0A02YK0F:  20-150cm (7.87" - 59.06")

                                  and others...
Output: Distance                  Distance range depends on sensor, unit mm, resolution 12bit.                     
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/distir_dimensions.png
   :height: 300pt
   :alt: alternate text
   :align: center


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_interface_coding>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _distir_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <pi_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <distance_ir_bricklet_python_api>`", ":ref:`Examples <distance_ir_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <distance_ir_bricklet_java_api>`", ":ref:`Examples <distance_ir_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <distance_ir_bricklet_c_api>`", ":ref:`Examples <distance_ir_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <distance_ir_bricklet_cpp_api>`", ":ref:`Examples <distance_ir_bricklet_cpp_examples>`", "Installation"


:ref:`Low Level Interfaces <pi_llpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI, over Brick", "API", "Example", "Installation"
   "I2C, over Brick", "API", "Example", "Installation"
   "UART(serial), over Brick", "API", "Example", "Installation"
   "Analog Voltage, directly", "\-", "Example", "\-"

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

