.. _temperature_ir_bricklet:

Temperature IR
==============


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The Temperature IR :ref:`Bricklet <product_overview_bricklets>` is equipped with a
`infrared thermometer <http://en.wikipedia.org/wiki/Infrared_thermometer>`_.
It uses thermal radiation emitted by the measured object. The
`emmissivity <http://en.wikipedia.org/wiki/Emissivity>`_ of an object is
material specific, a good list can be found 
`here <http://www.infrared-thermography.com/material.htm>`_.
Many infrared thermometers have a fixed emmissivity of 0.95 or 1.0
and measure wrong temperatures depending of the material.

The API of the Bricklet let you readout the object temperature and the
ambient temperature in degree Celsius.You can define the emmissivity dependend 
of your measurement or use the default value of 1.0. Additionally you can
configure events triggered when a specified temperature is exceeded.



Technical Specifications
------------------------

===================================  =====================================================================
Property                             Value
===================================  =====================================================================
Dimensions                           20mm x 25mm (0.79" x 0.98")
Weight
Sensor                               MLX90614ESF-BAA (Melexis)
Temperature range                    * -40 to +85°C ambient temperature

                                     * -70 to 380°C object temperature
Accurracy                            0.5°C over wide temperature range
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Output: Object/Ambient Temperature   Output in °C, unit 0.1°C, resolution 12bit
===================================  =====================================================================

Resources
---------

 * Schematic (Download)
 * MLX90614 Datasheet (`Download <http://www.melexis.com/Asset/IR-sensor-thermometer-MLX90614-Datasheet-DownloadLink-5152.aspx>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/temperature_ir_bricklet_dimensions.png
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


.. _temperatureir_interface_coding:

Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <temperature_ir_bricklet_python_api>`", ":ref:`Examples <temperature_ir_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <temperature_ir_bricklet_java_api>`", ":ref:`Examples <temperature_ir_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <temperature_ir_bricklet_c_api>`", ":ref:`Examples <temperature_ir_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <temperature_ir_bricklet_cpp_api>`", ":ref:`Examples <temperature_ir_bricklet_cpp_examples>`", "Installation"

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

