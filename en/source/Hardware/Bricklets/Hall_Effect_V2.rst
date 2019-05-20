
:shoplink: ../../../shop/bricklets/hall-effect-v2-bricklet.html

.. include:: Hall_Effect_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _hall_effect_v2_bricklet:

Hall Effect Bricklet 2.0
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_hall_effect_v2_tilted_[?|?].jpg           Hall Effect Bricklet 2.0
	Bricklets/bricklet_hall_effect_v2_top_[?|?].jpg              Hall Effect Bricklet 2.0
	Bricklets/bricklet_hall_effect_v2_brickv_[100|].jpg          Hall Effect Bricklet 2.0 in Brick Viewer
	Dimensions/hall_effect_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures magnetic flux density between -7mT and 7mT
* Counter with configurable thresholds, bipolar and unipolar
* Can count with a frequency of up to 10kHz


.. _hall_effect_v2_bricklet_description:

Description
-----------

The Hall Effect :ref:`Bricklet <primer_bricklets>` extends
:ref:`Bricks <primer_bricks>` and can
`magnetic flux density (magnetic induction) <https://en.wikipedia.org/wiki/Magnetic_flux>`__
from -7mT to 7mT (`milli Tesla <https://en.wikipedia.org/wiki/Tesla_(unit)>`__).
It can count the (dis-)appearances of magnetic fields
and can for example be used to measure the speed of a wheel with attached magnet
with a frequency of up to 10kHz.

The low/high threshold for the counter as well as a debounce time can
be configured and adjusted to a specific application.

Example applications are:

* Detect if a door is open or closed
* Reading out water/electricity meters
* Counting RPM of motors

The Hall Effect Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            DRV5053
Current Consumption               59mW (11.8mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Operation                         Omnipolar (North and South pole is detected)
Detection Range                   -7mT to 7mT
Counter Trigger Point             Configurable (unipolar and bipolar)
Counter Sampling Rate             10kHz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* DRV5053 datasheet (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/raw/master/datasheets/DRV5053.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/raw/master/hardware/hall-effect-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/hall_effect_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/hall-effect-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2VBKu39>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/hall_effect_v2/hall-effect-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/hall_effect_v2/hall-effect-v2.FCStd>`__)


.. _hall_effect_v2_bricklet_test:

Test your Hall Effect Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the measurement of the magnetic
flux density. You can move a magnet near the Bricklet to test it.

.. image:: /Images/Bricklets/bricklet_hall_effect_v2_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_v2_brickv.jpg

|test_pi_ref|



.. _hall_effect_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Hall_Effect_V2_hlpi.table
