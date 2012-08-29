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
	             "Current25 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/current25_bricklet_dimensions_100.png",
	             "Dimensions/current25_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures currents up to **25A**
* Measures direction of current
* Output in 1mA steps (12bit resolution)


Description
-----------

The Current25 :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by
bidirectional current flow measurements of up to **25A**.
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
Sensor                            ACS711 (25A version)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Current                           -25A to 25A in 1mA steps, 12bit resolution
Maximum Input Voltage             100VAC/100VDC (peak)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 14mm (0.98 x 0.98 x 0.55")
Weight                            4g
================================  ============================================================


Resources
---------

* ACS711 datasheet (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)


.. _current25_bricklet_test:

Test your Current25 Bricklet
----------------------------

To test the Current25 Bricklet you need to have the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
(for installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
to the Brick Daemon.

Connect the Current25 Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable. Connect a motor
and a battery to the Bricklet as displayed in the following image
(or anything else connected in series to the Current25 Bricklet that
produces a current).

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Current25 Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

If you connect the Brick to the PC over USB, you should see a new tab named
"Current25 Bricklet" in the Brick Viewer after a moment. Select this tab.

If everything went as expected you can now see the current used by the
motor and a graph that shows the current over time.

.. image:: /Images/Bricklets/bricklet_current25_brickv.jpg
   :scale: 100 %
   :alt: Current25 Bricklet in Brick Viewer
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
