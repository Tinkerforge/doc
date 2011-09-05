.. _voltage_bricklet:

Voltage
=======

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

With the Voltage :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the voltages. It is equipped with a terminal block which let you 
easily connect the voltage to be measured. The voltage can be readout in `Volt
<http://en.wikipedia.org/wiki/Volt>`_ directly. Events can be defined which
will be triggered when the voltages exceeds a specified value.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions
Weight
Sensor                            Voltage divider with factor 0.0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Voltage                   0V - 50V, unit: mV, resolution 12bit
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/voltage-bricklet/raw/master/hardware/voltage-bricklet-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/voltage-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


Test your Voltage Bricklet
--------------------------

For a simple test connect your Voltage Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable.
Additionally connect a voltage source to the Bricklet. 
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected Voltage Bricklet and Battery
   :align: center

After installing our software (Brickd, Brickv) you can see the connected 
Voltage Bricklet in the Brickv.

.. image:: /Images/Bricklets/voltage_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Voltage Bricklet
   :align: center

Click on the Voltage tab and see how the measured values change dependend 
on the applied voltage. 

You can now go on with writing your own application.
See :ref:`Interface and Coding <voltage_programming_interfaces>` section for the API of
the Voltage Bricklet and examples in your programming language.


.. _voltage_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <voltage_bricklet_python_api>`", ":ref:`Examples <voltage_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <voltage_bricklet_java_api>`", ":ref:`Examples <voltage_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <voltage_bricklet_c_api>`", ":ref:`Examples <voltage_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <voltage_bricklet_cpp_api>`", ":ref:`Examples <voltage_bricklet_cpp_examples>`", "Installation"

