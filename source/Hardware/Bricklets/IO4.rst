.. _io4_bricklet:

IO4
===


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

With the IO4 :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by external digital inputs 
and outputs.

The bricklet features 1x4 pins which can be independently configured as
digital inputs or outputs. Each input pin can additionally be configured with
pullups or as interrupt source. 
Via terminal blocks all signals can be accessed.
A single terminal block deliver the switched output voltage and GND. 

Human interfaces are typical applications of this bricklet since switches, push-bottons and
LEDs can be easily connected.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of I/Os                    1x8
I/O voltages                      Fixed 3.3V
Update frequency                  
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

.. image:: /Images/Dimensions/io4_bricklet_dimensions.png
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


.. _io4_interface_coding:

Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <io4_bricklet_python_api>`", ":ref:`Examples <io4_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <io4_bricklet_java_api>`", ":ref:`Examples <io4_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <io4_bricklet_c_api>`", ":ref:`Examples <io4_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <io4_bricklet_cpp_api>`", ":ref:`Examples <io4_bricklet_cpp_examples>`", "Installation"


.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

