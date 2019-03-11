
:DISABLED_shoplink: ../../../shop/bricklets/e-paper-296x128-bricklet.html

.. include:: EPaper_296x128.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _e_paper_296x128_bricklet:

E-Paper 296x128 Bricklet
========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_e_paper_296x128_tilted_[?|?].jpg           E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_horizontal_[?|?].jpg       E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_master_[100|600].jpg       E-Paper 296x128 Bricklet with Master Brick
	Cases/bricklet_e_paper_296x128_case_[100|600].jpg             E-Paper 296x128 Bricklet with case
	Bricklets/bricklet_e_paper_296x128_brickv_[100|].jpg          E-Paper 296x128 Bricklet in Brick Viewer
	Dimensions/e_paper_296x128_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 7.4cm (2.9") e-paper display with a resolution of 296x128 pixel
* two three-color displays available: black/white/red and black/white/gray
* Embedded font for easy text drawing


.. _e_paper_296x128_bricklet_description:

Description
-----------

The E-Paper 296x128 :ref:`Bricklet <primer_bricklets>` is an e-paper display
with a resolution of 296x128 pixel.

Each pixel can be set individually, so the display can show graphics. The content
of the display will stay after the Bricklet is powered off.

A three-color refresh of the display takes about 7.5 seconds. With different update
modes it is possible to reach update rates of up 1Hz if only black and white
are used.

The E-Paper 296x128 Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               TBDmW (TBDmA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Display Resolution                296x128 pixel
Display Size                      7.4cm (2.9")
Display Colors                    black/white/red or black/white/gray
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            100 x 40 x 6mm (3.93 x 1.57 x 0.24")
Weight                            TBDg
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/raw/master/hardware/e-paper-296x128-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/e_paper_296x128_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _e_paper_296x128_bricklet_test:

Test your E-Paper 296x128 Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

You can draw and write text to the display.

Note: On startup the Bricklet can not read back the content of the screen.
So the Brick Viewer will show a black screen even if something is one the display.
If you write to the display afterwards, the Brick Viewer will be able to read it back
and show it until the Bricklet is powered down again.

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_brickv.jpg
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_brickv.jpg

|test_pi_ref|


.. _e_paper_296x128_bricklet_case:

Case
----

..
	A `laser-cut case for the E-Paper 296x128 Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-e-paper-296x128-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_e_paper_296x128_case_350.jpg
	   :scale: 100 %
	   :alt: Case for E-Paper 296x128 Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_e_paper_296x128_case_1000.jpg

	.. include:: EPaper_296x128.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/e_paper_296x128_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for E-Paper 296x128 Bricklet
	   :align: center
	   :target: ../../_images/Exploded/e_paper_296x128_exploded.png

	|bricklet_case_hint|


.. _e_paper_296x128_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: EPaper_296x128_hlpi.table
