.. _temperature_bricklet:

Temperature
===========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_temperature_tilted_350.jpg", 
	             "Bricklets/bricklet_temperature_tilted_100.jpg", 
	             "Bricklets/bricklet_temperature_tilted_800.jpg", 
	             "Temperature Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_temperature_vertical_350.jpg", 
	             "Bricklets/bricklet_temperature_vertical_100.jpg", 
	             "Bricklets/bricklet_temperature_vertical_800.jpg", 
	             "Temperature Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_temperature_horizontal_350.jpg", 
	             "Bricklets/bricklet_temperature_horizontal_100.jpg", 
	             "Bricklets/bricklet_temperature_horizontal_800.jpg", 
	             "Temperature Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_temperature_master_350.jpg", 
	             "Bricklets/bricklet_temperature_master_100.jpg", 
	             "Bricklets/bricklet_temperature_master_800.jpg", 
	             "Temperature Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_temperature_brickv_350.jpg", 
	             "Bricklets/bricklet_temperature_brickv_100.jpg", 
	             "Bricklets/bricklet_temperature_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/temperature_bricklet_dimensions_350.png", 
	             "Dimensions/temperature_bricklet_dimensions_100.png", 
	             "Dimensions/temperature_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Description
-----------

With the Temperature :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the temperatures. 
The measured temperature can be readout in `°C
<http://en.wikipedia.org/wiki/Degree_Celsius>`_ directly.
You can define events which will be triggered when a specified temperature
is exceeded.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight                            1.4g
Sensor                            TMP102
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

To test your Temperature Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Temperature Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected Temperature Bricklet
   :align: center
   :target: ../../_images/Bricklets/current12_brickv.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Temperature Bricklet" in the Brick Viewer after you pressed "connect", 
select it.
If everything went as expected you the Brick Viewer should look like
depicted below.

.. image:: /Images/Bricklets/temperature_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Temperature Bricklet
   :align: center
   :target: ../../_images/Bricklets/temperature_brickv.jpg

See how the measured values change dependend 
on the device temperature. For example put your finger on the sensor and see the 
temperature rising.

You can now go on with writing your own application.
See :ref:`Interface and Coding <temperature_programming_interfaces>` section for the API of
the Temperature Bricklet and examples in your programming language.


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


