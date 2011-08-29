.. _temperature_bricklet:

Temperature
===========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

With the Temperature :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the temperatures. 
The measured illuminance can be readout in `°C
<http://en.wikipedia.org/wiki/Degree_Celsius>`_ directly.
You can define events which will be triggered when a specified temperature
is exceeded.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight
Sensor                            TMP102 (Texas Instruments)
Temperature range                 -40°C to 125°C
Accuracy                          0.5°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Ambient temperature       -40°C to 125°C, unit 0.1°C, resolution 12bit 
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * TMP102 Datasheet (`Download <http://www.ti.com/lit/gpn/tmp102>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/temperature_dimensions.png
   :width: 300pt
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


.. _temperature_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <temperature_bricklet_python_api>`", ":ref:`Examples <temperature_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <temperature_bricklet_java_api>`", ":ref:`Examples <temperature_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <temperature_bricklet_c_api>`", ":ref:`Examples <temperature_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <temperature_bricklet_cpp_api>`", ":ref:`Examples <temperature_bricklet_cpp_examples>`", "Installation"


:ref:`Low Level Interfaces <concepts_llpi>`
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

