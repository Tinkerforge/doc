
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Current12 Bricklet

.. include:: Current12.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

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
	             "Current12 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/current12_bricklet_dimensions_100.png",
	             "Dimensions/current12_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures currents up to **12.5A**
* Measures direction of current
* Output in 1mA steps (12bit resolution)


Description
-----------

The Current12 :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by
bidirectional current flow measurements of up to **12.5A**.
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
Sensor                            ACS711 (12.5A version)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Current                           -12.5A to 12.5A in 1mA steps, 12bit resolution
Maximum Input Voltage             100VAC/100VDC (peak)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 14mm (0.98 x 0.98 x 0.55")
Weight                            4g
================================  ============================================================


Resources
---------

* ACS711 datasheet (`Download <https://github.com/Tinkerforge/current12-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current12-bricklet/raw/master/hardware/current-12-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current12_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/current12-bricklet/zipball/master>`__)


.. _current12_bricklet_test:

Test your Current12 Bricklet
----------------------------

|test_intro|

|test_connect|. Connect a motor
and a battery to the Bricklet as displayed in the following picture
(or anything else connected in series to the Current12 Bricklet that
produces a current).

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Current12 Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

|test_tab|
If everything went as expected you can now see the current used by the
motor and a graph that shows the current over time.

.. image:: /Images/Bricklets/bricklet_current12_brickv.jpg
   :scale: 100 %
   :alt: Current12 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

In the screenshot you can see a high current peak. This is caused by the
starting of the motor when the battery is connected.

|test_pi_ref|


.. _current12_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Current12_hlpi.table
