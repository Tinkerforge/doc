.. _temperature_bricklet:

Temperature
===========


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

* TMP102 Datasheet (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/datasheets/tmp102.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/hardware/temperature-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/temperature-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _temperature_bricklet_test:

Test your Temperature Bricklet
------------------------------

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
See :ref:`Interface and Coding <ambl_programming_interfaces>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _temperature_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <temperature_bricklet_c_api>`", ":ref:`Examples <temperature_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <temperature_bricklet_csharp_api>`", ":ref:`Examples <temperature_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <temperature_bricklet_java_api>`", ":ref:`Examples <temperature_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <temperature_bricklet_python_api>`", ":ref:`Examples <temperature_bricklet_python_examples>`", "Installation"


