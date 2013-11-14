
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Tilt Bricklet
:FIXME_shoplink: ../../../shop/bricklets/tilt-bricklet.html

.. include:: Tilt.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _tilt_bricklet:

Tilt Bricklet
=============

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_tilt_tilted_350.jpg",
	               "Bricklets/bricklet_tilt_tilted_600.jpg",
	               "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_vertical_100.jpg",
	             "Bricklets/bricklet_tilt_vertical_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_horizontal_100.jpg",
	             "Bricklets/bricklet_tilt_horizontal_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_master_100.jpg",
	             "Bricklets/bricklet_tilt_master_600.jpg",
	             "Tilt Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_brickv_100.jpg",
	             "Bricklets/bricklet_tilt_brickv.jpg",
	             "Tilt Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/tilt_bricklet_dimensions_100.png",
	             "Dimensions/tilt_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Detects inclination of Bricklet (tilt switch open/closed)
* Detects if Bricklet is vibrating

Description
-----------

The Tilt Bricklet is equipped with a tilt switch. It can detect if the
Bricklet is tilted or if the Bricklet is vibrating.

It is possible to configure events that are triggered if the state of
the Tilt Bricklet changes.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (W x D x H)            25 x 15 x 15mm (0.98 x 0.59 x 0.59")
Weight                            3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/tilt-bricklet/raw/master/hardware/tilt-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/tilt_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/tilt-bricklet/zipball/master>`__)


.. _tilt_bricklet_test:

Test your Tilt Bricklet
-----------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_tilt_master_600.jpg
   :scale: 100 %
   :alt: Tilt Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_master_1200.jpg

|test_tab|
If everything went as expected you can now see the current
state of the Tilt Bricklet.

.. image:: /Images/Bricklets/bricklet_tilt_brickv.jpg
   :scale: 100 %
   :alt: Tilt Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_brickv.jpg

|test_pi_ref|

.. _tilt_bricklet_case:

Case
----

A `laser-cut case for the Tilt Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-tilt-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_tilt_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Tilt Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_tilt_case_built_up_1000.jpg

.. include:: Tilt.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/tilt_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Tilt Bricklet
   :align: center
   :target: ../../_images/Exploded/tilt_exploded.png

|bricklet_case_hint|


.. _tilt_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Tilt_hlpi.table
