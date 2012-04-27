.. _current12_bricklet:

Current12 Bricklet
==================

.. raw:: html

    {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
    {{ 
		tfdocstart("Bricklets/bricklet_current_tilted_350.jpg", 
		         "Bricklets/bricklet_current_tilted_600.jpg", 
		         "Current12 Bricklet") 
	}}
	{{
		tfdocimg("Bricklets/bricklet_current_horizontal_100.jpg", 
		         "Bricklets/bricklet_current_horizontal_600.jpg", 
		         "Current12 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_vertical_100.jpg", 
		         "Bricklets/bricklet_current_vertical_600.jpg", 
		         "Current12 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_master_100.jpg", 
		         "Bricklets/bricklet_current_master_600.jpg", 
		         "Current12 Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_current12_brickv_100.jpg", 
	             "Bricklets/bricklet_current12_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/current12_bricklet_dimensions_100.png", 
	             "Dimensions/current12_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Measures currents up to 12 Ampere
 * Measures direction of current
 * Outputs current in Ampere
 * 12bit resolution


Description
-----------

The Current12 :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by 
bidirectional current flow measurments of up to 12.5 Ampere. 
Additionally events can be configured to receive signals when a specified 
current is exceeded.

Typical applications can be found in robotics. With the bidirectional current 
flow measurement it is possible distinguish between 
charge and discharge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight                            3.9g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            ACS711 12.5A Version
Output: Current                   -12.5A to 12.5A, unit 1mA, resolution 12bit
Max Input Voltage                 100VAC/100VDC (peak)
================================  ============================================================

Resources
---------

* ACS711 Datasheet (`Download <https://github.com/Tinkerforge/current12-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current12-bricklet/raw/master/hardware/current-12-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current12_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/current12-bricklet/zipball/master>`__)



.. _current12_bricklet_test:

Test your Current12 Bricklet
----------------------------

To test the Current12 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Now you can connect the Current12 Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. Connect a Motor
and a Battery to the Bricklet as displayed in the following image 
(or anything else connected in series to the Current12 Bricklet that 
produces a current).

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Current12 Bricklet, Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

If you connect the Brick to the PC over USB,
you should see a tab named "Current12 Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
If everything went as expected you can now see the current used by the 
motor and a graph that shows the current over time. 


.. image:: /Images/Bricklets/bricklet_current12_brickv.jpg
   :scale: 100 %
   :alt: Current12 Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

In the screenshot you can see a high current peak. This is caused by the
starting of the motor when the battery is connected. 

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <current12_programming_interfaces>` section for 
the API of the Current12 Bricklet and examples in different programming languages.


.. _current12_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <current12_bricklet_c_api>`", ":ref:`Examples <current12_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <current12_bricklet_csharp_api>`", ":ref:`Examples <current12_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <current12_bricklet_java_api>`", ":ref:`Examples <current12_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <current12_bricklet_python_api>`", ":ref:`Examples <current12_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"


