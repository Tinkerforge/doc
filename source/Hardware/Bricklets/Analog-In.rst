.. _analog_in_bricklet:

Analog In
=========

.. raw:: html

    {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
    {{ 
        tfdocstart("Bricklets/bricklet_analog_in_tilted_350.jpg", 
                 "Bricklets/bricklet_analog_in_tilted_600.jpg", 
                 "Ambient Light Bricklet") 
    }}
    {{ 
        tfdocimg("Bricklets/bricklet_analog_in_vertical_100.jpg", 
                 "Bricklets/bricklet_analog_in_vertical_600.jpg", 
                 "Ambient Light Bricklet") 
    }}
    {{ 
        tfdocimg("Bricklets/bricklet_analog_in_horizontal_100.jpg", 
                 "Bricklets/bricklet_analog_in_horizontal_600.jpg", 
                 "Ambient Light Bricklet") 
    }}
    {{ 
        tfdocimg("Bricklets/bricklet_analog_in_master_100.jpg", 
                 "Bricklets/bricklet_analog_in_master_600.jpg", 
                 "Ambient Light Bricklet with Master Brick") 
    }}
    {{ 
        tfdocimg("Bricklets/bricklet_analog_in_brickv_100.jpg", 
                 "Bricklets/bricklet_analog_in_brickv.jpg", 
                 "Brick Viewer screenshot") 
    }}
    {{ 
        tfdocimg("Dimensions/analog_in_bricklet_dimensions_100.png", 
                 "Dimensions/analog_in_bricklet_dimensions_600.png", 
                 "Outline and drilling plan") 
    }}
    {{ tfdocend() }}


Features
--------

 * Measures voltages of up to 45V
 * Read out measured voltage in mV
 * High resolution up to 1.48mV
 * Configurable events


Description
-----------

The Analog In :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by the 
capability to measure voltages.
The voltage can be read out in `Volt
<http://en.wikipedia.org/wiki/Volt>`_ directly without conversions necessary. 
The device has 4 different measurement ranges.
Each range is measured with 12bit resolution such that lower voltages can be 
measured more accurate than larger voltages (see technical specifications below). 
The device switches between these ranges automatically.
With configurable events it is possible to react on changing
voltages without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 30mm (0.98" x 1.18")
Weight                            TBD
Sensor                            Switchable Voltage Divider
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Voltage                   0V - 45V, unit: mV
Measurement Range:                Switched Automatically

                                  * 0V -  6.05V, Resolution ~1.48mV
                                  * 0V - 10.32V, Resolution ~2.52mV
                                  * 0V - 36.30V, Resolution ~8.86mV
                                  * 0V - 45.00V, Resolution ~11.25mV
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/analog-in-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog-in_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/analog-in-bricklet/zipball/master>`__)



Connectivity
------------

The Analog In Bricklet has 4 terminals. With these terminals you can access
ground, 3.3V, 5V (only output) and you can apply the voltage you want to 
measure (VIN). See picture below.

.. image:: /Images/Bricklets/bricklet_analog_in_vertical_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_vertical_1200.jpg


.. _analog_in_bricklet_test:

Test your Analog In Bricklet
----------------------------

To test the Analog In Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Analog In Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable.
Additionally connect a voltage source to the Bricklet. 
For testing purposes we have connected a battery.

.. image:: /Images/Bricklets/bricklet_analog_in_master_600.jpg
   :scale: 100 %
   :alt: Analog In Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_master_1200.jpg


If you connect the Brick to the PC over USB,
you should see a tab named "Analog In Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time. 

.. image:: /Images/Bricklets/bricklet_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_brickv.jpg

After this you can go on with writing your own application.
See the :ref:`Programming Interface <analog_in_programming_interfaces>` section 
for the API of the Analog In Bricklet and examples in different
programming languages.


.. _analog_in_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <analog_in_bricklet_c_api>`", ":ref:`Examples <analog_in_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <analog_in_bricklet_csharp_api>`", ":ref:`Examples <analog_in_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <analog_in_bricklet_java_api>`", ":ref:`Examples <analog_in_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <analog_in_bricklet_python_api>`", ":ref:`Examples <analog_in_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"

