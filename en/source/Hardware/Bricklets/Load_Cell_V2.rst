
:DISABLED_shoplink: ../../../shop/bricklets/load-cell-v2-bricklet.html

.. include:: Load_Cell_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _load_cell_v2_bricklet:

Load Cell Bricklet 2.0
======================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_load_cell_v2_tilted_[?|?].jpg           Load Cell Bricklet 2.0
	Bricklets/bricklet_load_cell_v2_horizontal_[?|?].jpg       Load Cell Bricklet 2.0
	Bricklets/bricklet_load_cell_v2_master_[100|600].jpg       Load Cell Bricklet 2.0 with Master Brick
	Cases/bricklet_load_cell_v2_case_[100|600].jpg             Load Cell Bricklet 2.0 with case
	Bricklets/bricklet_load_cell_v2_brickv_[100|].jpg          Load Cell Bricklet 2.0 in Brick Viewer
	Dimensions/load_cell_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures output of load cells
* 24bit ADC for high resolution
* Up to 80 weight measurements per second


.. _load_cell_v2_bricklet_description:

Description
-----------

The Load Cell :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure load cells.
Only a single known weight is required to calibrate the load cell.
It is possible to measure weight differences of few grams in objects that
weigh many kilograms.

Load cells with different maximum weights are available in the shop:

* `Load Cell 1kg CZL635
  <https://www.tinkerforge.com/en/shop/accessories/sensors/load-cell-1kg-czl635.html>`__
* `Load Cell 5kg CZL635
  <https://www.tinkerforge.com/en/shop/accessories/sensors/load-cell-5kg-czl635.html>`__
* `Load Cell 20kg CZL601
  <https://www.tinkerforge.com/en/shop/accessories/sensors/load-cell-20kg-czl601.html>`__
* `Load Cell 50kg CZL601
  <https://www.tinkerforge.com/en/shop/accessories/sensors/load-cell-50kg-czl601.html>`__

The Bricklet has the standard status LED and an additional info LED 
that can be turned on trough the API, e.g. to show that a weight
measurement is in range.

The Load Cell Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HX711
Current Consumption               54mW (10.8mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        24bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 14mm (1.18 x 1.18 x 0.55")
Weight                            7.3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/load-cell-v2-bricklet/raw/master/hardware/load-cell-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/load_cell_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/load-cell-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2IeyZE6>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/load_cell_v2/load-cell-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/load_cell_v2/load-cell-v2.FCStd>`__)


.. _load_cell_v2_bricklet_connectivity:

Connectivity
------------

The Load Cell Bricklet 2.0 has four terminals. The PWR and GND terminals are for
the excitation voltage and the IN+ and IN- terminals are for the signal
measurement.

TODO: Photo of new Bricklet

.. image:: /Images/Bricklets/bricklet_load_cell_horizontal_350.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet 2.0 terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_horizontal_1200.jpg

A typical load cell will have four or five wires. Check the specification of
your load cell for its pinout and connect it according to the table below.

============== ================ ================================================
Connection     Terminal         Possible Wire Colors
============== ================ ================================================
Excitation +   PWR              red
Excitation -   GND              black, yellow
Signal +       IN+              green, blue
Signal -       IN-              white
============== ================ ================================================


.. _load_cell_v2_bricklet_test:

Test your Load Cell Bricklet 2.0
--------------------------------

|test_intro|

|test_connect|.
Additionally :ref:`connect <load_cell_bricklet_connectivity>` and
:ref:`calibrate <load_cell_bricklet_calibration>` a load cell.

|test_tab|
If everything went as expected you can now see the weight in gram
and a graph that shows the weight over time.

.. image:: /Images/Bricklets/bricklet_load_cell_v2_brickv.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_v2_brickv.jpg

|test_pi_ref|


.. _load_cell_bricklet_v2_calibration:

Calibration
-----------

The Load Cell Bricklet 2.0 has to be calibrated for the connected load cell and the
specific setup.

TODO: New image?

.. image:: /Images/Screenshots/load_cell_bricklet_calibration.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet  2.0calibration in Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/load_cell_bricklet_calibration.jpg

Connect a load cell to the Bricklet as described :ref:`above
<load_cell_v2_bricklet_connectivity>`. Then start Brick Viewer and click the
"Calibration" button on the "Load Cell Bricklet 2.0" tab. With no weight on the
load cell, click the "Calibrate Zero" button. Now put a known weight on the
load cell, enter the known weight in gram as the "Current Weight", then click
the "Calibrate Weight" button.

Now the Load Cell Bricklet 2.0 is calibrated for the connected load cell and the
specific setup.

.. _load_cell_v2_bricklet_scale_kit:

Scale Kit
---------

The Scale Kit is build from `MakerBeam <https://www.tinkerforge.com/en/shop/makerbeam.html>`__, 
a `1kg Load Cell <https://www.tinkerforge.com/en/shop/accessories/sensors/load-cell-1kg-czl635.html>`__ 
and laser cut plastic parts. It is available in the 
`Tinkerforge shop <https://www.tinkerforge.com/en/shop/kits/scale-kit.html>`__, 
but you can also just use the description to 
get an idea on how to mount a load cell in general.

.. image:: /Images/Misc/scale_w_master_600.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet with Master Brick and Scale Kit
   :align: center
   :target: ../../_images/Misc/scale_w_master_1200.jpg

* Building up the Scale Kit is pretty easy. Start by removing the protective
  foil from the plastic parts (there is foil on both sides).

* Screw the 60mm MakerBeam and the load cell to the top plastic part. Ensure to
  screw the load cell with the arrow side to the plastic part and that the arrow
  is pointing away from the plastic part.

.. image:: /Images/Misc/scale_setup_part0_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 0
   :align: center
   :target: ../../_images/Misc/scale_setup_part0_1000.jpg

.. image:: /Images/Misc/scale_setup_part1_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 1
   :align: center
   :target: ../../_images/Misc/scale_setup_part1_1000.jpg

* Screw the 100mm MakerBeam and the load cell to the bottom plastic part.

.. image:: /Images/Misc/scale_setup_part2_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 2
   :align: center
   :target: ../../_images/Misc/scale_setup_part2_1000.jpg

.. image:: /Images/Misc/scale_setup_part3_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 3
   :align: center
   :target: ../../_images/Misc/scale_setup_part3_1000.jpg

.. image:: /Images/Misc/scale_setup_part4_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 4
   :align: center
   :target: ../../_images/Misc/scale_setup_part4_1000.jpg

* Use the double sided tape to attach the round plate to the 60mm MakerBeam.

.. image:: /Images/Misc/scale_setup_part5_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 5
   :align: center
   :target: ../../_images/Misc/scale_setup_part5_1000.jpg

.. image:: /Images/Misc/scale_setup_part6_350.jpg
   :scale: 100 %
   :alt: Scale Kit part 6
   :align: center
   :target: ../../_images/Misc/scale_setup_part6_1000.jpg

* Mechanical construction done! Finally, connect the load cell to the Bricklet
  as described in the :ref:`connectivity <load_cell_v2_bricklet_connectivity>`
  section.

.. image:: /Images/Misc/scale3_350.jpg
   :scale: 100 %
   :alt: Build up scale
   :align: center
   :target: ../../_images/Misc/scale3_1000.jpg


.. _load_cell_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the Load Cell Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-load-cell-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_load_cell_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Load Cell Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_load_cell_v2_case_1000.jpg

	.. include:: Load_Cell_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/load_cell_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Load Cell Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/load_cell_v2_exploded.png

	|bricklet_case_hint|


.. _load_cell_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Load_Cell_V2_hlpi.table
