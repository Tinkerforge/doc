.. _joystick_bricklet:

Joystick
========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

This :ref:`Bricklet <product_overview_bricklets>` can be connected to every 
:ref:`Brick <product_overview_bricks>` and can be used as input device. 
It is two directional moveable and equipped with a push button.
You can readout the position of the stick (X/Y coordinates) and
the state of the button. Additionally you can configure events triggered
when the stick is at a particular position or the button is pushed.

You can use this device to control robots, games etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        45mm x 25mm (1.77" x 0.98")
Weight
Joystick                          Two-axis with push button
Output: Joystick position         x/y axis position: -100/100, 0=center
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

.. image:: /Images/Dimensions/joystick_bricklet_dimensions.png
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


.. _joystick_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <pi_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <joystick_bricklet_python_api>`", ":ref:`Examples <joystick_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <joystick_bricklet_java_api>`", ":ref:`Examples <joystick_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <joystick_bricklet_c_api>`", ":ref:`Examples <joystick_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <joystick_bricklet_cpp_api>`", ":ref:`Examples <joystick_bricklet_cpp_examples>`", "Installation"

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

