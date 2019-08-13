
:shoplink: ../../../shop/bricklets/e-paper-296x128-bricklet-bwr.html

.. include:: EPaper_296x128.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _e_paper_296x128_bricklet:

E-Paper 296x128 Bricklet
========================


.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_e_paper_296x128_tilted_red_[?|?].jpg       E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_tilted_gray_[?|?].jpg      E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_top_red_[?|?].jpg          E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_top_gray_[?|?].jpg         E-Paper 296x128 Bricklet
	Bricklets/bricklet_e_paper_296x128_tilted_bottom_[?|?].jpg    E-Paper 296x128 Bricklet
	Cases/bricklet_e_paper_296x128_case_front_[?|?].jpg           E-Paper 296x128 Bricklet in Case
	Bricklets/bricklet_e_paper_296x128_brickv_[100|].jpg          E-Paper 296x128 Bricklet in Brick Viewer
	Dimensions/e_paper_296x128_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 7.4cm (2.9") e-paper display with a resolution of 296x128 pixel
* Two three-color displays available: black/white/red and black/white/gray
* Embedded font for easy text drawing


.. _e_paper_296x128_bricklet_description:

Description
-----------

The E-Paper 296x128 :ref:`Bricklet <primer_bricklets>` is an e-paper display
with a resolution of 296x128 pixel.

Each pixel can be set individually, so the display can show graphics. The content
of the display will stay after the Bricklet is powered off.

The E-Paper 296x128 Bricklet is available with two different three-color display
options: Black/white/red and black/white/gray.

A three-color refresh of the display takes about 7.5 seconds. With different update
modes it is possible to reach update rates of up 1Hz if only black and white
are used.

The E-Paper 296x128 Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_e_paper_296x128_video.webm" type="video/webm">
	</video>


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               | 45mW (9mA at 5V) idle
                                  | 95mW (19mA at 5V) during draw
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Display Resolution                296x128 pixel
Display Size                      7.4cm (2.9")
Display Colors                    black/white/red or black/white/gray
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            100 x 40 x 6mm (3.93 x 1.57 x 0.24")
Weight                            20g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/raw/master/hardware/e-paper-296x128-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/e_paper_296x128_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/e-paper-296x128-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2VyGhgF>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/e_paper_296x128/e-paper-296x128.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/e_paper_296x128/e-paper-296x128.FCStd>`__)


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
So the Brick Viewer will show a black screen even if something is on the display.
If you write to the display afterwards, the Brick Viewer will be able to read it back
and show it until the Bricklet is powered down again.

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_brickv.jpg
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_brickv.jpg

|test_pi_ref|


Usage
-----

To draw to the display we recommend that you use an image library that is
native to your programming language (for example PIL for Python). This
way you can use all of the available drawing primitives and fonts of the
library and then copy the image buffer to the Bricklet.

We provide examples for:

* `C/C++ <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/c/example_load_image.c>`__
  (with `libgd <https://libgd.github.io/>`__),
* `C# <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/csharp/ExampleLoadImage.cs>`__,
* `Go <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/go/example_load_image.go>`__,
* `Java <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/java/ExampleLoadImage.java>`__,
* `Perl <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/perl/example_load_image.pl>`__
  (with `GD <https://search.cpan.org/~lds/GD-2.56/lib/GD.pm>`__),
* `PHP <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/php/ExampleLoadImage.php>`__
  (with `GD <https://php.net/manual/en/book.image.php>`__),
* `Python <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/python/example_load_image.py>`__
  (with `PIL <https://python-pillow.org/>`__),
* `Rust <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/rust/example_load_image.rs>`__,
  (with `image <https://docs.rs/image/0.21.1/image/>`__)
* `Visual Basic .NET <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/vbnet/ExampleLoadImage.vb>`__.

In the example we load the image `tf_red.png <https://raw.githubusercontent.com/Tinkerforge/e-paper-296x128-bricklet/master/software/examples/tf_red.png>`__
and write it to the display:

TODO: tf_red image


Update Modes
------------

.. note::
 The default update mode corresponds to the default e-paper display
 manufacturer settings. All of the other modes are experimental and
 will result in increased ghosting and possibly other long-term
 side effects.

 If you want to know more about the inner workings of an e-paper display
 take a look at this excellent video from Ben Krasnow:
 `https://www.youtube.com/watch?v=MsbiO8EAsGw <https://www.youtube.com/watch?v=MsbiO8EAsGw>`__.

 If you are not sure about this option, leave the update mode at default.

Currently there are three update modes available:

* **Default**: Settings as given by the manufacturer. An update will take about
  7.5 seconds and during the update the screen will flicker several times.
* **Black/White**: This will only update the black/white pixel. It uses the manufacturer
  settings for black/white and ignores the red or gray pixel buffer. With this mode the
  display will flicker once and it takes about 2.5 seconds. Compared to the default settings
  there is more ghosting.
* **Delta**: This will only update the black/white pixel. It uses an aggressive method where
  the changes are not applied for a whole buffer but only for the delta between the last
  and the next buffer. With this mode the display will not flicker during an update and
  it takes about 900-950ms. Compared to the other two settings there is more ghosting. This
  mode can be used for something like a flicker-free live update of a text.

With the black/white/red display if you use either the black/white or the delta mode,
after a while of going back and forth between black and white the white color will
start to appear red-ish or pink-ish.

If you use the aggressive delta mode and rapidly change the content, we recommend that you
change back to the default mode every few hours and in the default mode cycle between the
three available colors a few times. This will get rid of the ghosting and after that you can
go back to the delta mode with flicker-free updates.

.. _e_paper_296x128_bricklet_font:

Font
----

The Bricklet has an embedded font (ASCII subset in green) that allows fast and
easy text rendering:

.. image:: /Images/Bricklets/bricklet_e_paper_296x128_font.png
   :scale: 100 %
   :alt: E-Paper 296x128 Bricklet font
   :align: center
   :target: ../../_images/Bricklets/bricklet_e_paper_296x128_font.png


.. _e_paper_296x128_bricklet_case:

Case
----

Comming soon...

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
