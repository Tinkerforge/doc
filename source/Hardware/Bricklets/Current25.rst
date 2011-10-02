.. _current25_bricklet:

Current25
=========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
    {{ 
		tfdocimg("Bricklets/bricklet_current_tilted_350.jpg", 
		         "Bricklets/bricklet_current_tilted_100.jpg", 
		         "Bricklets/bricklet_current_tilted_800.jpg", 
		         "Current25 Bricklet") 
	}}
	{{
		tfdocimg("Bricklets/bricklet_current_horizontal_350.jpg", 
		         "Bricklets/bricklet_current_horizontal_100.jpg", 
		         "Bricklets/bricklet_current_horizontal_800.jpg", 
		         "Current25 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_vertical_350.jpg", 
		         "Bricklets/bricklet_current_vertical_100.jpg", 
		         "Bricklets/bricklet_current_vertical_800.jpg", 
		         "Current25 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_master_350.jpg", 
		         "Bricklets/bricklet_current_master_100.jpg", 
		         "Bricklets/bricklet_current_master_1200.jpg", 
		         "Current25 Bricklet with connected Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_current25_brickv_350.jpg", 
	             "Bricklets/bricklet_current25_brickv_100.jpg", 
	             "Bricklets/bricklet_current25_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/current25_bricklet_dimensions_350.png", 
	             "Dimensions/current25_bricklet_dimensions_100.png", 
	             "Dimensions/current25_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}

Description
-----------

The Current25 :ref:`Bricklet <product_overview_bricklets>` extend the features
of an :ref:`Brick <product_overview_bricks>` by bidirectional current flow
measurments up to 25 Ampere. 
The measured current can be readout in `Ampere <http://en.wikipedia.org/wiki/Ampere>`_ 
directly. Additionally events can be configured, triggered when a specified current is 
exceeded.

Typical applications can be found in robotics. The bidirectional current 
flow measurement is advantageous since you can distinguish between charge and discharge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight                            3.9g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            ACS711 25A Version
Output: Current                   -25A to 25A, unit 10mA, resolution 12bit
================================  ============================================================

Resources
---------

* ACS711 Datasheet (`Download <https://github.com/Tinkerforge/current25-bricklet/blob/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _current25_bricklet_test:

Test your Current25 Bricklet
----------------------------

To test your Current25 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Now you can connect your Current25 Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. If you like you can connect a Motor
and a Battery to the Bricklet as displayed in the following image.

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Current25 Bricklet, Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

If you connect the Brick to the PC over USB,
you should see a tab named "Current25 Bricklet" in the Brick Viewer after you
pressed "connect", select this tab.
If everything went as expected you can now see the exact current in Ampere 
and a graph that shows the current over time. 


.. image:: /Images/Bricklets/bricklet_current25_brickv.jpg
   :scale: 100 %
   :alt: Current25 Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current25_brickv.jpg

In our test we have connected the battery not from beginning. 
When connecting the battery, you
can see the high current peak caused by the motor when start running.
   
After this test you can go on with writing your own application.
See :ref:`Interface and Coding <current25_programming_interfaces>` section for 
the API of the Current25 Bricklet and examples in your programming language.

.. _current25_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <current25_bricklet_c_api>`", ":ref:`Examples <current25_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <current25_bricklet_csharp_api>`", ":ref:`Examples <current25_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <current25_bricklet_java_api>`", ":ref:`Examples <current25_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <current25_bricklet_python_api>`", ":ref:`Examples <current25_bricklet_python_examples>`", "Installation"

