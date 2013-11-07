
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Segment Display 4x7 Bricklet
:FIXME_shoplink: ../../../shop/bricklets/segment-display-4x7-bricklet.html

.. include:: Segment_Display_4x7.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _segment_display_4x7_bricklet:

Segment Display 4x7 Bricklet
============================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_segment_display_4x7_tilted_350.jpg",
	               "Bricklets/bricklet_segment_display_4x7_tilted_600.jpg",
	               "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_vertical_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_vertical_600.jpg",
	             "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_horizontal_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_horizontal_600.jpg",
	             "Segment Display 4x7 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_master_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_master_600.jpg",
	             "Segment Display 4x7 Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_segment_display_4x7_brickv_100.jpg",
	             "Bricklets/bricklet_segment_display_4x7_brickv.jpg",
	             "Segment Display 4x7 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/segment_display_4x7_bricklet_dimensions_100.png",
	             "Dimensions/segment_display_4x7_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Four 7-segment displays with switchable colon
* Brightness of segments configurable
* Configurable counter functionality

Description
-----------

The Segment Display 4x7 Bricklet can be used to control four 7-segment 
displays and a colon. Each of the 29 segments can be controlled
independently. It is also possible to configure the brightness of the
segments. Besides the possibility of controlling each segment idependently,
the API offers a user configureable counter.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Segment Width                     6mm
Segment Height                    10mm
Brightness of Segments            Configurable, up to 70mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 65 x 9mm (0.98 x 2.56 x 0.35")
Weight                            11g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/hardware/segment-display-4x7-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/segment_display_4x7_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/zipball/master>`__)


.. _segment_display_4x7_bricklet_test:

Test your Segment Display 4x7 Bricklet
--------------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_segment_display_4x7_master_600.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_master_1200.jpg

|test_tab|
If everything went as expected you can now activate/deactivate the
individual segments.

.. image:: /Images/Bricklets/bricklet_segment_display_4x7_brickv.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_brickv.jpg

|test_pi_ref|

.. _segment_display_4x7_bricklet_case:

Case
----

A `laser-cut case for the Segment Display 4x7 Bricklet <https://www.tinkerforge.com/en/shop/cases/case-segment-display-4x7-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_segment_display_4x7_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_segment_display_4x7_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
* build up side plates,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the Segment Display 4x7 Bricklet case:

.. image:: /Images/Exploded/segment_display_4x7_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Exploded/segment_display_4x7_exploded.png

|bricklet_case_hint|


.. _segment_display_4x7_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Segment_Display_4x7_hlpi.table
