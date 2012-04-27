.. _voltage_bricklet:

Voltage Bricklet
================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_voltage_tilted_350.jpg", 
	             "Bricklets/bricklet_voltage_tilted_600.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_vertical_100.jpg", 
	             "Bricklets/bricklet_voltage_vertical_600.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_horizontal_100.jpg", 
	             "Bricklets/bricklet_voltage_horizontal_600.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_master_100.jpg", 
	             "Bricklets/bricklet_voltage_master_600.jpg", 
	             "Voltage Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_brickv_100.jpg", 
	             "Bricklets/bricklet_voltage_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/voltage_bricklet_dimensions_100.png", 
	             "Dimensions/voltage_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Measures voltages up to 50V
 * Outputs voltage in mV, resolution 12bit
 * Configurable events


Description
-----------

The Voltage :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by the 
capability to measure voltages. The measurement range is 0-50V.
The voltage can be read out directly in `Volt
<http://en.wikipedia.org/wiki/Volt>`_ without conversion. 
With configurable events it is possible to react on changing
voltages without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight                            3.8g
Sensor                            Voltage divider with factor 0.0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Voltage                   0V - 50V, unit: mV, resolution 12bit
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/voltage-bricklet/raw/master/hardware/voltage-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/voltage-bricklet/zipball/master>`__)


.. _voltage_bricklet_test:

Test your Voltage Bricklet
--------------------------

To test the Voltage Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Voltage Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable.
Additionally connect a voltage source to the Bricklet. 
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricklets/bricklet_voltage_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Voltage Bricklet and Battery
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_master_1200.jpg

If you connect the Brick to the PC over USB,
you should see a tab named "Voltage Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
If everything went as expected you can now see the voltage in volt
and a graph that shows the voltage over time. 

.. image:: /Images/Bricklets/bricklet_voltage_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Voltage Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_brickv.jpg

After this you can go on with writing your own application.
See the :ref:`Programming Interface <voltage_programming_interfaces>` section 
for the API of the Voltage Bricklet and examples in different
programming languages.


.. _voltage_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <voltage_bricklet_c_api>`", ":ref:`Examples <voltage_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <voltage_bricklet_csharp_api>`", ":ref:`Examples <voltage_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <voltage_bricklet_java_api>`", ":ref:`Examples <voltage_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <voltage_bricklet_python_api>`", ":ref:`Examples <voltage_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"

