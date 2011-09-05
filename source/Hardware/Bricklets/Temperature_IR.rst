.. _temperature_ir_bricklet:

Temperature IR
==============


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #2") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #3") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #4") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #5") }}
	{{ tfdocend() }}


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

* MLX90614 Datasheet (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/blob/master/datasheets/MLX90614.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/hardware/temperature-ir-bricklet-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_ir_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__

.. _temperature_ir_bricklet_test:

Test your Temperature IR Bricklet
---------------------------------

For a simple test connect your Temperature IR Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected Temperature IR Bricklet
   :align: center

After installing our software (Brickd, Brickv) you can see the connected 
Temperature IR Bricklet in the Brickv.

.. image:: /Images/Bricklets/temperature_ir_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Temperature IR Bricklet
   :align: center

Click on the Temperature IR Bricklet tab and point the device in different
directions. The Brick Viewer will show you the ambient temperature (the 
temperature of the device) and the object temperature you point at.

Since the emmissivity depends on the material you can configure it.
Enter 0xFFFF = 65535 for an emmissivity of 1.0.
The default is an emmisivity of 0.98 (0.98 * 0xFFFF = 64224).

After this you can go on with writing your own application.
See :ref:`Interface and Coding <temperatureir_programming_interfaces>` 
section for the API of the Ambient Light Bricklet and examples in your 
programming language.


.. _temperatureir_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <temperature_ir_bricklet_c_api>`", ":ref:`Examples <temperature_ir_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <temperature_ir_bricklet_csharp_api>`", ":ref:`Examples <temperature_ir_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <temperature_ir_bricklet_java_api>`", ":ref:`Examples <temperature_ir_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <temperature_ir_bricklet_python_api>`", ":ref:`Examples <temperature_ir_bricklet_python_examples>`", "Installation"


