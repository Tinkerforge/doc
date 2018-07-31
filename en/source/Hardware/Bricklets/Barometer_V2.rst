
:DISABLED_shoplink: ../../../shop/bricklets/barometer-v2-bricklet.html

.. include:: Barometer_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _barometer_v2_bricklet:

Barometer Bricklet 2.0
======================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_barometer_v2_tilted_[?|?].jpg           Barometer Bricklet 2.0
	Bricklets/bricklet_barometer_v2_horizontal_[?|?].jpg       Barometer Bricklet 2.0
	Bricklets/bricklet_barometer_v2_master_[100|600].jpg       Barometer Bricklet 2.0 with Master Brick
	Cases/bricklet_barometer_v2_case_[100|600].jpg             Barometer Bricklet 2.0 with case
	Bricklets/bricklet_barometer_v2_brickv_[100|].jpg          Barometer Bricklet 2.0 in Brick Viewer
	Dimensions/barometer_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures air pressure, temperature and altitude
* Resolution 0.0075mbar / 6.25cm
* Range 260 to 1260mbar


.. _barometer_v2_bricklet_description:

Description
-----------

The Barometer :ref:`Bricklet <primer_bricklets>` 2.0 can be used to extend the 
features of :ref:`Bricks <primer_bricks>` by the
capability to measure air pressure in range of 260 to 1260mbar with a resolution
of 0.0065mbar. The measurement is temperature compensated internally.

The Bricklet is equipped with a LPS22HB sensor which can be used
as an altimeter. Since the air pressure is changing significantly
even over a short period of time the achievable accuracy is limited. One possible
solution to achieve higher accuracy and stability of the altitude measurement is
to perform sensor fusion with the sensor data of an :ref:`IMU Brick <imu_brick>`
(see `Youtube video <https://www.youtube.com/watch?v=TaqtzG7lyp0>`__).

The Barometer Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LPS22HB
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Pressure Range                    260 - 1260mbar
Resolution                        0.0075mbar / 6.25cm
Accuracy (0-65°C before OPC*)     ± 1.1mbar
Accuracy (0-65°C after OPC*)      ± 0.2mbar

Temperature Range                 -40 - 85°C
Resolution                        0.01°C
Accuracy                          ± 1.5°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            1.6g
================================  ============================================================

\* OPC = One-Point Calibration, see TODO

Resources
---------

* LPS22HB datasheet (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/datasheets/LPS22HB.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/hardware/barometer-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/barometer_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2NYG7XC>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/barometer_v2/barometer-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/barometer_v2/barometer-v2.FCStd>`__)


.. _barometer_v2_bricklet_test:

Test your Barometer Bricklet 2.0
--------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the air pressure in mbar
and a graph that shows the air pressure over time.

TODO: Make screenshot

.. image:: /Images/Bricklets/bricklet_barometer_v2_brickv.jpg
   :scale: 100 %
   :alt: Barometer Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_v2_brickv.jpg

|test_pi_ref|


Understanding Air Pressure
--------------------------

Air pressure is a complex topic. Two frequently asked questions are: Why does
the air pressure value of the Barometer Bricklet differs from the value in the
weather forecast and why does the altitude value differ from the actual altitude
of the measuring location?

Air Pressure Reading
^^^^^^^^^^^^^^^^^^^^

The Barometer Bricklet outputs the air pressure in relation to the altitude of
the measuring location, known as `QFE <https://en.wikipedia.org/wiki/QFE>`__
value in aviation. The weather forecast reports air pressure in relation to mean
sea level (the value is also temperature-corrected in a special way), known as
`QFF <https://en.wikipedia.org/wiki/QFF>`__ value in aviation.

With the `barometric formula <https://en.wikipedia.org/wiki/Barometric_formula>`__
the QFF value can be approximated based on the the QFE value::

 QFF = QFE / [1 - Tg * H / (273.15 + Tfe + Tg * H)] ^ (0.034163 / Tg)

* ``Tg`` is the temperature lapse rate, that specifies how fast the temperature
  drops with increasing altitude (a common approximation under normal conditions
  is 0.0065 °C/Meter)
* ``Tfe`` is the temperature at the measuring location in °C
* ``H`` is the altitude of the measuring location in Meters

`Here <http://keisan.casio.com/exec/system/1224575267>`__ is an online
calculator for this formula. The altitude of the measuring location can be found
with `Google Maps <http://www.mapcoordinates.net/en>`__.

Altitude Reading
^^^^^^^^^^^^^^^^

The altitude value for the Barometer Bricklets is by default calculated for a
reference air pressure of 1013.25 mbar using an approximation of the
`International Standard Atmosphere <https://en.wikipedia.org/wiki/International_Standard_Atmosphere>`__
model. An altitude value calculated like this is known as `QNE
<https://en.wikipedia.org/wiki/Pressure_altitude>`__ value in aviation.

For a more exact altitude value in relation to mean sea level the reference air
pressure for the measuring location has to be specified. In aviation the `QNH
<https://en.wikipedia.org/wiki/QNH>`__ value is used for this purpose. Therefore,
this value if often available at airfields. Instead of the QNH value the QFF
value can be used also. The QFF value has a different temperature-correction
applied to it compared to the QNH, but the values are similar under normal
conditions.


.. _barometer_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the Barometer Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-barometer-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_barometer_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Barometer Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_barometer_v2_case_1000.jpg

	.. include:: Barometer_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/barometer_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Barometer Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/barometer_v2_exploded.png

	|bricklet_case_hint|


.. _barometer_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Barometer_V2_hlpi.table
