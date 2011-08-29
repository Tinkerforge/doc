.. _humidity_bricklet:

Humidity
========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

With the Humidity :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the `relative humidity <http://en.wikipedia.org/wiki/Relative_humidity>`_. 
The measured humidity can be readout in percent directly, no conversions are 
necessary. You can configure events triggered when a particular humidity threshold 
is reached so that no polling is necessary.

A weather station is a typical application for this sensor, but it can be also
used in drying applications, environment monitoring etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight
Power Consumption                 
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            HIH-5030 (Honeywell)
Output: Relative Humidity (RH)    0-100% RH, unit 0.1% RH, resolution 12bit
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * HIH-5030 Datasheet (`Download <http://sensing.honeywell.com/index.cfm?ci_id=155943>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/humidity_bricklet_dimensions.png
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


.. _humidity_interface_coding:

Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <humidity_bricklet_python_api>`", ":ref:`Examples <humidity_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <humidity_bricklet_java_api>`", ":ref:`Examples <humidity_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <humidity_bricklet_c_api>`", ":ref:`Examples <humidity_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <humidity_bricklet_cpp_api>`", ":ref:`Examples <humidity_bricklet_cpp_examples>`", "Installation"   

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

