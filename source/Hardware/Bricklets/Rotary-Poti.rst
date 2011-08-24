.. _rotary-poti_bricklet:

Rotary-Poti
===========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

This :ref:`Bricklet <concepts_bricklets>` is equipped with a 1-turn rotary 
`potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`_. 
After connecting it to a :ref:`Brick <concepts_bricks>` you
can readout the position of the potentiometer. Additionally you can configure 
different events triggered when the potentiometer reaches a specific position.

You can use this Bricklet for purposes like speed or volume control.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        30mm x 25mm (1.18" x 0.98")
Weight
Rotary potentiometer              1-turn, 300 degree
Output: Potentiometer position    -150 to 150 (left to right)
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/rotary-poti_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <concepts_bricks>` over the supplied cable (see picture below).

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


.. _rotary_poti_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <rotary_poti_bricklet_python_api>`", ":ref:`Examples <rotary_poti_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <rotary_poti_bricklet_java_api>`", ":ref:`Examples <rotary_poti_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <rotary_poti_bricklet_c_api>`", ":ref:`Examples <rotary_poti_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <rotary_poti_bricklet_cpp_api>`", ":ref:`Examples <rotary_poti_bricklet_cpp_examples>`", "Installation"

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

