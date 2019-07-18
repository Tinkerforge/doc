
:shoplink: ../../../shop/bricklets/segment-display-4x7-bricklet.html

.. include:: Segment_Display_4x7.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _segment_display_4x7_bricklet:

Segment Display 4x7 Bricklet
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_segment_display_4x7_tilted_[?|?].jpg           Segment Display 4x7 Bricklet
	Bricklets/bricklet_segment_display_4x7_horizontal_[?|?].jpg       Segment Display 4x7 Bricklet
	Cases/bricklet_segment_display_4x7_case_tilted_[?|?].jpg          Segment Display 4x7 Bricklet in Case
	Bricklets/bricklet_segment_display_4x7_leds_on_[100|600].jpg      Segment Display 4x7 Bricklet active
	Bricklets/bricklet_segment_display_4x7_brickv_[100|].jpg          Segment Display 4x7 Bricklet in Brick Viewer
	Dimensions/segment_display_4x7_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Segment Display 4x7 Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`Segment Display 4x7 Bricklet 2.0 <segment_display_4x7_v2_bricklet>` is the recommended
 replacement.


Features
--------

* Four 7-segment displays with switchable colon
* Brightness of segments configurable
* Configurable counter functionality


.. _segment_display_4x7_bricklet_description:

Description
-----------

The Segment Display 4x7 :ref:`Bricklet <primer_bricklets>` can be
used to control four 7-segment displays and a colon by a 
:ref:`Brick <primer_bricks>`. Each of the 29 segments
can be controlled independently. It is also possible to configure the
brightness of the segments. Besides the possibility of controlling each segment
independently, the API offers a user configurable counter.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               | 1mA (all segments off)
                                  | 6mA (all segments on at minimum brightness)
                                  | 62mA (all segments on at maximum brightness)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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

* TM1637 datasheet (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/datasheets/TM1637.pdf>`__)
* KHN40392ASR1D-2 datasheet (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/datasheets/KHN40392ASR1D-2.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/raw/master/hardware/segment-display-4x7-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/segment_display_4x7_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/segment-display-4x7-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2iV9qNf>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/segment_display_4x7/segment-display-4x7.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/segment_display_4x7/segment-display-4x7.FCStd>`__)


.. _segment_display_4x7_bricklet_test:

Test your Segment Display 4x7 Bricklet
--------------------------------------

|test_intro|

|test_connect|.

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

A `laser-cut case for the Segment Display 4x7 Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-segment-display-4x7-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_segment_display_4x7_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Segment Display 4x7 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_segment_display_4x7_case_tilted_1000.jpg

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


.. _segment_display_4x7_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Segment_Display_4x7_hlpi.table


Known Bugs
----------

When connecting the Segment Display 4x7 Bricklet (version 1.0) to a Master 
Brick, try to connect it to port A or B (not C or D). The reason for that is, 
that the Segment Display 4x7 Bricklet might interfere with the Analog-to-digital 
converter of the microcontroller due to a voltage feedback.

This will be fixed in the next product version.
