.. _voltage_bricklet:

Voltage
=======


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

With the Voltage :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the voltages. It is equipped with a terminal block which let you 
easily connect the voltage to be measured. The voltage can be readout in `Volt
<http://en.wikipedia.org/wiki/Volt>`_ directly. Events can be defined which
will be triggered when the voltages exceeds a specified value.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions
Weight
Sensor                            Voltage divider with factor 0.0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Voltage                   0V - 50V, unit: mV, resolution 12bit
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

.. image:: /Images/Dimensions/voltage_dimensions.png
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


.. _voltage_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <pi_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <voltage_bricklet_python_api>`", ":ref:`Examples <voltage_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <voltage_bricklet_java_api>`", ":ref:`Examples <voltage_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <voltage_bricklet_c_api>`", ":ref:`Examples <voltage_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <voltage_bricklet_cpp_api>`", ":ref:`Examples <voltage_bricklet_cpp_examples>`", "Installation"


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

