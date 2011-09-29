.. _humidity_bricklet:

Humidity
========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
	{{ tfdocimg("Bricklets/humidity_with_master_s.jpg", "Bricklets/humidity_with_master_t.jpg", "Bricklets/humidity_with_master_b.jpg", "Title #1") }}
	{{ tfdocend() }}


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
Weight                            1.6g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            HIH-5030
Output: Relative Humidity (RH)    0-100% RH, unit 0.1% RH, resolution 12bit
================================  ============================================================

Resources
---------

* HIH-5030 Datasheet (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/datasheets/hih-5030.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/hardware/humidity-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/humidity_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/humidity-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _humidity_bricklet_test:


Test your Humidity Bricklet
---------------------------

To test your Humidity Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Humidity Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected Humidity Bricklet
   :align: center
   :target: ../../_images/Bricklets/current12_brickv.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Humidity Bricklet" in the Brick Viewer after you pressed “connect”.
Select it.
If everything went as expected you can now see the measured relative humidity
and a graph that shows the humidity over time.

.. image:: /Images/Bricklets/humidity_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Humidity Bricklet
   :align: center
   :target: ../../_images/Bricklets/humidity_brickv.jpg

To test the sensor breath over the sensor and see the relative humidity rising.
It will fall again when you stop breathing over the sensor.

After this test you can go on with writing your own application.
See :ref:`Interface and Coding <humidity_programming_interfaces>` section for the API of
the Humidity Bricklet and examples in your programming language.


.. _humidity_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <humidity_bricklet_c_api>`", ":ref:`Examples <humidity_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <humidity_bricklet_csharp_api>`", ":ref:`Examples <humidity_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <humidity_bricklet_java_api>`", ":ref:`Examples <humidity_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <humidity_bricklet_python_api>`", ":ref:`Examples <humidity_bricklet_python_examples>`", "Installation"


