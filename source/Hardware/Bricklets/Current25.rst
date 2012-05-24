.. _current25_bricklet:

Current25 Bricklet
==================

.. raw:: html

    {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
    {{ 
		tfdocstart("Bricklets/bricklet_current_tilted_350.jpg", 
		         "Bricklets/bricklet_current_tilted_600.jpg", 
		         "Current25 Bricklet") 
	}}
	{{
		tfdocimg("Bricklets/bricklet_current_horizontal_100.jpg", 
		         "Bricklets/bricklet_current_horizontal_600.jpg", 
		         "Current25 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_vertical_100.jpg", 
		         "Bricklets/bricklet_current_vertical_600.jpg", 
		         "Current25 Bricklet") 
	}}
	{{ 
		tfdocimg("Bricklets/bricklet_current_master_100.jpg", 
		         "Bricklets/bricklet_current_master_600.jpg", 
		         "Current25 Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_current25_brickv_100.jpg", 
	             "Bricklets/bricklet_current25_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/current25_bricklet_dimensions_100.png", 
	             "Dimensions/current25_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Measures currents up to 25 Ampere
 * Measures direction of current
 * Outputs current in Ampere
 * 12bit resolution


Description
-----------

The Current25 :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by 
bidirectional current flow measurements of up to 25 Ampere.
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
Sensor                            ACS711 25A Version
Output: Current                   -25A to 25A, unit 1mA, resolution 12bit
Max Input Voltage                 100VAC/100VDC (peak)
================================  ============================================================

Resources
---------

* ACS711 Datasheet (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)



.. _current25_bricklet_test:

Test your Current25 Bricklet
----------------------------

To test the Current25 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Now you can connect the Current25 Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. Connect a Motor
and a Battery to the Bricklet as displayed in the following image
(or anything else connected in series to the Current25 Bricklet that 
produces a current).

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Current25 Bricklet, Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

If you connect the Brick to the PC over USB,
you should see a tab named "Current25 Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
If everything went as expected you can now see the current used by the 
motor and a graph that shows the current over time. 


.. image:: /Images/Bricklets/bricklet_current25_brickv.jpg
   :scale: 100 %
   :alt: Current25 Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current25_brickv.jpg

In the screenshot you can see a high current peak. This is caused by the
starting of the motor when the battery is connected. 

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <current25_programming_interfaces>` section for 
the API of the Current25 Bricklet and examples in different programming languages.


.. _current25_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Current25_hlpi.table
