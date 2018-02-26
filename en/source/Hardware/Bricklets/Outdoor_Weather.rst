
:DISABLED_shoplink: ../../../shop/bricklets/outdoor-weather-bricklet.html

.. include:: Outdoor_Weather.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _outdoor_weather_bricklet:

Outdoor Weather Bricklet
========================

.. note::
  This Bricklet is currently work-in-progress!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_outdoor_weather_tilted_[?|?].jpg           Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_top_[?|?].jpg              Outdoor Weather Bricklet
	Bricklets/bricklet_outdoor_weather_front_[?|?].jpg            Outdoor Weather Bricklet with Master Brick
	Bricklets/bricklet_outdoor_weather_brickv_[100|].jpg          Outdoor Weather Bricklet in Brick Viewer
	Dimensions/outdoor_weather_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Receives data from outdoor weather station and indoor sensors
* Measures Temperature, Humidity, Wind/Gust speed, Wind direction and Rainfall
* Can use up to 255 weather stations/sensors simultaneously


.. _outdoor_weather_bricklet_description:

Description
-----------

The Outdoor Weather :ref:`Bricklet <primer_bricklets>` is equipped
with a 433MHz receiver capable of receiving data from outdoor weather stations.
It can be connected to a :ref:`Brick <primer_bricks>`.

It currently supports `Outdoor Weather Station WS-6147 <https://www.tinkerforge.com/en/shop/outdoor-weather-station-ws-6147>`__ which measures

* Temperature (°C)
* Humidity (%RH)
* Wind/Gust speed (m/s)
* Wind direction (16 directions)
* Rainfall (mm)

and `Temperature/Humidity Sensor TH-6148 <https://www.tinkerforge.com/en/shop/temperature-humidity-sensor-th-6148>`__ which measures

* Temperature (°C)
* Humidity (%RH)

The Outdoor Weather Station WS-6147 is meant to be put outside (somewhere where it can measure the rain/wind).
The TH-6148 sensor can be used inside or outside. You can use up to 255 Outdoor Weather Stations and up to
255 Sensors simultaneously.

The Outdoor Weather Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_outdoor_weather_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
P TBD                             V TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 35 x 5mm (1.58 x 1.38 x 0.2")
Weight                            TBDg
================================  ============================================================


Resources
---------

* Instruction manual WS-6147 (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/WS-6147.pdf>`__)
* 433MHz receiver RFM210LCF (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/datasheets/RFM210LCF.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/raw/master/hardware/outdoor-weather-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/outdoor_weather_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/outdoor-weather-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2E2p4U7>`__ | Download: `STEP <http://download.tinkerforge.com/3d/outdoor-weather/outdoor_weather_bricklet.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/outdoor-weather/outdoor_weather_bricklet.FCStd>`__)


.. _outdoor_weather_bricklet_test:

Test your Outdoor Weather Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the latest received data of your
weather stations and sensors. It takes about ~45 seconds until the first data
shows up when you start the weather station or Bricklet for the first time.

.. image:: /Images/Bricklets/bricklet_outdoor_weather_brickv.jpg
   :scale: 100 %
   :alt: Outdoor Weather Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_outdoor_weather_brickv.jpg

|test_pi_ref|


.. _outdoor_weather_bricklet_case:

Case
----

..
	A `laser-cut case for the Outdoor Weather Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-outdoor-weather-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_outdoor_weather_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Outdoor Weather Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_outdoor_weather_case_1000.jpg

	.. include:: Outdoor_Weather.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/outdoor_weather_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Outdoor Weather Bricklet
	   :align: center
	   :target: ../../_images/Exploded/outdoor_weather_exploded.png

	|bricklet_case_hint|


.. _outdoor_weather_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Outdoor_Weather_hlpi.table
