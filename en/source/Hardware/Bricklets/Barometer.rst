
:shoplink: ../../../shop/bricklets/barometer-bricklet.html

.. include:: Barometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _barometer_bricklet:

Barometer Bricklet
==================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_barometer_tilted_[?|?].jpg           Barometer Bricklet
	Bricklets/bricklet_barometer_vertical_[?|?].jpg         Barometer Bricklet
	Bricklets/bricklet_barometer_horizontal_[?|?].jpg       Barometer Bricklet
	Cases/bricklet_ambient_light_case_built_up_[?|?].jpg    Barometer Bricklet in case
	Bricklets/bricklet_barometer_brickv_[100|].jpg          Barometer Bricklet in Brick Viewer
	Dimensions/barometer_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Barometer Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`Barometer Bricklet 2.0 <barometer_v2_bricklet>` is the recommended
 replacement.

Features
--------

* Measures air pressure and altitude changes
* Resolution 0.012hPa / 0.1m
* Range 10 to 1200hPa


.. _barometer_bricklet_description:

Description
-----------

The Barometer :ref:`Bricklet <primer_bricklets>` can be used to extend the 
features of :ref:`Bricks <primer_bricks>` by the
capability to measure air pressure in range of 10 to 1200hPa with a resolution
of 0.012hPa. The measurement is temperature compensated internally.

The Bricklet is equipped with a MS5611-01BA01 sensor which is designed to be
used as an altimeter, too. But since the air pressure is changing significantly
even over a short period time the achievable accuracy is limited. One possible
solution to achieve higher accuracy and stability of the altitude measurement is
to perform sensor fusion with the sensor data of an :ref:`IMU Brick <imu_brick>`
(see `Youtube video <https://www.youtube.com/watch?v=TaqtzG7lyp0>`__).


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MS5611-01BA01
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Pressure Range                    10 - 1200hPa
Resolution                        0.012hPa / 0.1m
Accuracy (25°C, 750hPa)           ± 1.5hPa
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* MS5611 datasheet (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/datasheets/ms5611-01ba01.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/hardware/barometer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/barometer_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/barometer-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2iT7sNj>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/barometer/barometer.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/barometer/barometer.FCStd>`__)


.. _barometer_bricklet_test:

Test your Barometer Bricklet
----------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the air pressure in hPa
and a graph that shows the air pressure over time.

.. image:: /Images/Bricklets/bricklet_barometer_brickv.jpg
   :scale: 100 %
   :alt: Barometer Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_brickv.jpg

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
  is 0.0065°C/m)
* ``Tfe`` is the temperature at the measuring location in °C
* ``H`` is the altitude of the measuring location in Meters

`Here <https://keisan.casio.com/exec/system/1224575267>`__ is an online
calculator for this formula. The altitude of the measuring location can be found
with `Google Maps <https://www.mapcoordinates.net/en>`__.

Altitude Reading
^^^^^^^^^^^^^^^^

The altitude value for the Barometer Bricklets is by default calculated for a
reference air pressure of 1013.25hPa using an approximation of the
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


.. _barometer_bricklet_case:

Case
----

A `laser-cut case for the Barometer Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Barometer Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Barometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Barometer Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _barometer_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Barometer_hlpi.table
