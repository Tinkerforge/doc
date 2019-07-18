
:shoplink: ../../../shop/bricklets/segment-display-4x7-v2-bricklet.html

.. include:: Segment_Display_4x7_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _segment_display_4x7_v2_bricklet:

Segment Display 4x7 Bricklet 2.0
================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_segment_display_4x7_v2_tilted_[?|?].jpg           Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_tilted2_[?|?].jpg          Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_top_[?|?].jpg              Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_side_[?|?].jpg             Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_active_bright_[?|?].jpg    Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_active_dark_[?|?].jpg      Segment Display 4x7 Bricklet 2.0
	Bricklets/bricklet_segment_display_4x7_v2_brickv_[100|].jpg          Segment Display 4x7 Bricklet 2.0 in Brick Viewer
	Dimensions/segment_display_4x7_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Four 7-segment digits
* Switchable dots per digit, colon and tick mark
* Brightness of segments configurable
* Configurable counter functionality


.. _segment_display_4x7_v2_bricklet_description:

Description
-----------

The Segment Display 4x7 :ref:`Bricklet <primer_bricklets>` 2.0 can be
used to control four 7-segment displays, four dots, two colon dots and
a tick mark by a :ref:`Brick <primer_bricks>`. Each of the 35 segments
can be controlled independently. 

It is also possible to configure the brightness of the segments. 
Besides the possibility of controlling each segment
independently, the API offers a user configurable counter.

The Segment Display 4x7 Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="600px" height="auto" controls loop>
	  <source src="../../_images/Videos/bricklet_segment_display_4x7_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_segment_display_4x7_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_segment_display_4x7_v2_video.webm" type="video/webm">
	</video>


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               | 30mW  (6mA at 5V)  all segments off
                                  | 60mW  (12mA at 5V) all segments on at minimum brightness
                                  | 400mW (80mA at 5V) all segments on at maximum brightness
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Segment Width                     6mm
Segment Height                    10mm
Brightness of Segments            Configurable in 8 steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 65 x 9mm (0.98 x 2.56 x 0.35")
Weight                            11g
================================  ============================================================


Resources
---------

* TM1637 datasheet (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/datasheets/TM1637.pdf>`__)
* LTC-4627JR datasheet (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/datasheets/LTC-4627JR.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/raw/master/hardware/segment-display-4x7-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/segment_display_4x7_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/segment-display-4x7-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2WFOtYT>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/segment_display_4x7_v2/segment-display-4x7-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/segment_display_4x7_v2/segment-display-4x7-v2.FCStd>`__)


.. _segment_display_4x7_v2_bricklet_test:

Test your Segment Display 4x7 Bricklet 2.0
------------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now activate/deactivate the
individual segments.

.. image:: /Images/Bricklets/bricklet_segment_display_4x7_v2_brickv.jpg
   :scale: 100 %
   :alt: Segment Display 4x7 Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_segment_display_4x7_v2_brickv.jpg

|test_pi_ref|


.. _segment_display_4x7_v2_bricklet_case:

Case
----

A `laser-cut case for the Segment Display 4x7 Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-segment-display-4x7-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_segment_display_4x7_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Segment Display 4x7 Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_segment_display_4x7_case_tilted_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
* build up side plates,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the Segment Display 4x7 Bricklet 2.0 case:

.. image:: /Images/Exploded/segment_display_4x7_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Segment Display 4x7 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/segment_display_4x7_exploded.png

|bricklet_case_hint|


.. _segment_display_4x7_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Segment_Display_4x7_V2_hlpi.table
