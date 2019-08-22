
:shoplink: ../../../shop/bricklets/line-bricklet.html

.. include:: Line.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _line_bricklet:

Line Bricklet
=============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_line_tilted_[?|?].jpg           Line Bricklet
	Bricklets/bricklet_line_vertical_[?|?].jpg         Line Bricklet
	Bricklets/bricklet_line_horizontal_[?|?].jpg       Line Bricklet
	Bricklets/bricklet_line_tilted_back_[?|?].jpg      Line Bricklet
	Cases/bricklet_line_case1_tilted_[?|?].jpg         Line Bricklet Mounting Plate Version 1
	Cases/bricklet_line_case2_tilted1_[?|?].jpg        Line Bricklet Mounting Plate Version 2
	Bricklets/bricklet_line_brickv_[100|].jpg          Line Bricklet in Brick Viewer
	Dimensions/line_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Line Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`Color Bricklet 2.0 <color_v2_bricklet>` is the recommended
 replacement.


Features
--------

* Measures the reflectivity of a surface
* Can be used to detect/follow lines
* Can be used to measure distances of ca. 0-10mm


.. _line_bricklet_description:

Description
-----------

The Line :ref:`Bricklet <primer_bricklets>` can extend 
:ref:`Bricks <primer_bricks>` by a reflective optical sensor. 
The sensor consists of an infrared emitter and a
phototransistor. Output of the sensor is the reflectivity of a surface.

The reflectivity value can be used to detect and follow lines (e.g. a black
line has a different reflectivity then a white background). The Line Bricklet
can also be used to measure the distance to a surface, since the received light
decreases with increased distance.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            CNY70
Current Consumption               33mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        12bit
Emitter Wavelength                950nm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 9mm (0.98 x 0.59 x 0.35")
Weight                            2g
================================  ============================================================


Resources
---------

* CNY70 datasheet (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/datasheets/cny70.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/line-bricklet/raw/master/hardware/line-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/line_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/line-bricklet/zipball/master>`__)


.. _line_bricklet_test:

Test your Line Bricklet
-----------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the currently measured
reflectivity. To test it you can for example move the Bricklet over a
white paper with black stripes on it.

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
reflectiveness of the line and the underground. It can be found out by
trial and error.

There is a mounting Plate available for the Line Bricklet in the
`shop <https://www.tinkerforge.com/en/shop/mounting-plate-line-bricklet.html>`__
which simplifies the mounting. It consists of a mounting plate with fixed 
distance: 

.. image:: /Images/Cases/bricklet_line_case1_tilted_350.jpg
   :scale: 100 %
   :alt: Line Bricklet Mounting Plate Version 1
   :align: center
   :target: ../../_images/Cases/bricklet_line_case1_tilted_600.jpg

And a mounting plate with configurable distance:

.. image:: /Images/Cases/bricklet_line_case2_tilted1_350.jpg
   :scale: 100 %
   :alt: Line Bricklet Mounting Plate Version 2
   :align: center
   :target: ../../_images/Cases/bricklet_line_case2_tilted1_600.jpg


.. _line_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Line_hlpi.table
