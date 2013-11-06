
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Line Bricklet
:FIXME_shoplink: ../../../shop/bricklets/line-bricklet.html

.. include:: Line.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _line_bricklet:

Line Bricklet
=============

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_line_tilted_350.jpg",
	               "Bricklets/bricklet_line_tilted_600.jpg",
	               "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_vertical_100.jpg",
	             "Bricklets/bricklet_line_vertical_600.jpg",
	             "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_horizontal_100.jpg",
	             "Bricklets/bricklet_line_horizontal_600.jpg",
	             "Line Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_master_100.jpg",
	             "Bricklets/bricklet_line_master_600.jpg",
	             "Line Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_line_brickv_100.jpg",
	             "Bricklets/bricklet_line_brickv.jpg",
	             "Line Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/line_bricklet_dimensions_100.png",
	             "Dimensions/line_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures the reflectivity of a surface
* Can be used to detect/follow lines
* Can be used to measure distances of ~0-10mm

Description
-----------

The Line Bricklet is equipped with a reflective optical sensor. The sensor 
consists of an infrared emitter and a phototransistor. Output of the sensor is 
the reflectivity of a surface. 

The reflectivity value can be used to detect
and follow lines (e.g. a black line has a different reflectivity then
a white background). The Line Bricklet can also be used to measure the distance 
to a surface, since the reflectivity decreases with increased distance.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Resolution                        12bit
Emitter Wavelength                950nm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 9mm (0.98 x 0.59 x 0.35")
Weight                            2g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/hardware/line-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/line_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/line-bricklet/zipball/master>`__)


.. _line_bricklet_test:

Test your Line Bricklet
-----------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_line_master_600.jpg
   :scale: 100 %
   :alt: Line Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_line_master_1200.jpg

|test_tab|
If everything went as expected you can now see the currently measured
reflectivity.

.. image:: /Images/Bricklets/bricklet_line_brickv.jpg
   :scale: 100 %
   :alt: Line Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_line_brickv.jpg

|test_pi_ref|

Mounting of the Line Bricklet
-----------------------------

To be used as a line detector the Bricklet has to be mounted with
a fixed distance to the line. The mounting distance depends on the 
reflectiveness of the line and the underground and has to be found out by
trail and error.

.. _line_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Line_hlpi.table
