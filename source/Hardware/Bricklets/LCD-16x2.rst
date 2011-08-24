.. _LCD-16x2_bricklet:

LCD-16x2
========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

This LCD :ref:`Bricklet <concepts_bricklets>` is equipped with a
16x2 alphanummeric chars display with blue backlight and three push buttons. 
You can control it by connecting it to a :ref:`Brick <concepts_bricks>`.
The API lets you write chars or lines to the LCD, get the state of each button,
switch the backlight on or off and configure events for each button.

You can use this bricklet to display any information you like to.
For example you can use it to display song information on your PC or 
measured values from other bricklets.



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        80mm x 31mm (3.15" x 1.22")
Weight
LCD                               Alphanummeric, 16 chars per line, 2 lines
Backlight                         Blue, software switchable on/off
Contrast                          Contrast voltage adjustable with potentiometer
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * LCD Controller KS0066U Datasheet (`Download <http://www.asix.cz/download/pvk40/ks0066u.pdf>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/lcd-16x2_dimensions.png
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

Contrast



.. _lcd16x2_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <lcd_16x2_bricklet_python_api>`", ":ref:`Examples <lcd_16x2_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <lcd_16x2_bricklet_java_api>`", ":ref:`Examples <lcd_16x2_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <lcd_16x2_bricklet_c_api>`", ":ref:`Examples <lcd_16x2_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <lcd_16x2_bricklet_cpp_api>`", ":ref:`Examples <lcd_16x2_bricklet_cpp_examples>`", "Installation"


:ref:`Low Level Interfaces <concepts_llpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI, over Brick", "API", "Example", "Installation"
   "I2C, over Brick", "API", "Example", "Installation"
   "UART(serial), over Brick", "API", "Example", "Installation"
   "Analog Voltage, directly", "\-", "Example", "\-"


Troubleshoot
------------

I do not see anything on the display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Reason:** Maybe your contrast is to low

**Solution:**
  * Set contrast as described in TODODODODODO

