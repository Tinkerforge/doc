.. _voltage_bricklet:

Voltage
=======

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_tilted_350.jpg", 
	             "Bricklets/bricklet_voltage_tilted_100.jpg", 
	             "Bricklets/bricklet_voltage_tilted_800.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_vertical_350.jpg", 
	             "Bricklets/bricklet_voltage_vertical_100.jpg", 
	             "Bricklets/bricklet_voltage_vertical_800.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_horizontal_350.jpg", 
	             "Bricklets/bricklet_voltage_horizontal_100.jpg", 
	             "Bricklets/bricklet_voltage_horizontal_800.jpg", 
	             "Voltage Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_master_350.jpg", 
	             "Bricklets/bricklet_voltage_master_100.jpg", 
	             "Bricklets/bricklet_voltage_master_1200.jpg", 
	             "Voltage Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_voltage_brickv_350.jpg", 
	             "Bricklets/bricklet_voltage_brickv_100.jpg", 
	             "Bricklets/bricklet_voltage_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/voltage_bricklet_dimensions_350.png", 
	             "Dimensions/voltage_bricklet_dimensions_100.png", 
	             "Dimensions/voltage_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
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
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight                            3.8g
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

.. _voltage_bricklet_test:

Test your Voltage Bricklet
--------------------------

To test your Voltage Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Voltage Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable.
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
pressed "connect", select this tab.
If everything went as expected you can now see the exact voltage in volt
and a graph that shows the voltage over time. 

.. image:: /Images/Bricklets/bricklet_voltage_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Voltage Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_brickv.jpg

In our test we have connected the battery not from beginning.
You can see the rising voltage after connecting the battery in the graph.

After this you can go on with writing your own application.
See :ref:`Interface and Coding <voltage_programming_interfaces>` section for 
the API of the Voltage Bricklet and examples in your programming language.


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

