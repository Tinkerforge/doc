.. _starter_kit_weather_station:

Starter Kit: Weather Station
============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/weather_station_cosm_graphs_350.jpg",
	               "Kits/weather_station_cosm_graphs_600.jpg",
	               "Weather Station: Cosm graphs")
	}}
	{{
	    tfdocimg("Kits/weather_station_website_350.jpg",
	             "Kits/weather_station_website_orig.jpg",
	             "Weather Station: Embedded in website)
	}}
	{{ tfdocend() }}

The Starter Kit: Weather Station is... TODO

Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.
For that you need to install the :ref:`Brick Daemon <brickd_installation>` and 
the :ref:`Brick Viewer <brickv_installation>`. Use Brick Viewer to find out
if all of the firmwares up to date (Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_firmware>` and 
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick 
Viewer too:

.. image:: /Images/Kits/weather_station_update_350.jpg
   :scale: 100 %
   :alt: Weather Station update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/weather_station_update_orig.jpg


After that you can click through the tabs of the Brick Viewer to see if
all of the sensors are working correctly. Now you can be sure that the
Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together in the weather station
enclosure.


Construction
------------

TODO: Images of construction and instructions

Projects
--------

Write Environment Measurements to LCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most obvious application of the Weather Station Starter Kit is to write
the measurements of the environment to the LCD20x4 Bricklet. This can be 
done through three different paths:

* USB connection to PC: Install brickd and application on PC, connect Master Brick of Weather Station to PC via USB.
* WIFI connection to PC: Install application on PC, connect Weather Station directly over WiFi or through AP.
* Raspberry PI or other embedded board integrated in Weather Station: Install brickd and application on embedded board, connect Master Brick of Weather Station to embedded board via USB.

All three possible solutions can use the same source code.

Example implementations with step-by-step instructions are available for

:ref:`C/C++ <starter_kit_weather_station_c_to_lcd>`, :ref:`C# <starter_kit_weather_station_csharp_to_lcd>`, :ref:`Delphi <starter_kit_weather_station_delphi_to_lcd>`, :ref:`Java <starter_kit_weather_station_java_to_lcd>`, :ref:`PHP <starter_kit_weather_station_php_to_lcd>`, :ref:`Python <starter_kit_weather_station_python_to_lcd>`, :ref:`Ruby <starter_kit_weather_station_ruby_to_lcd>`, :ref:`VB.NET <starter_kit_weather_station_vbnet_to_lcd>`.


Connect to Cosm
^^^^^^^^^^^^^^^

Cosm is a service that provides the possibility to analyze and visualize
the "Internet of Things". They can store a history of our Weather Station
data and we get a neat graphs:

.. image:: /Images/Kits/weather_station_cosm_graphs_600.jpg
   :scale: 100 %
   :alt: Cosm datastreams shown as graph
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_graphs_orig.jpg

An example implementation with step-by-step instructions that shares the 
weather data with cosm is available in :ref:`Python <starter_kit_weather_station_cosm>`.

Embed Live Measurements on Website
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another application for the Weather Station, is to embed the weather data
on a website:

.. image:: /Images/Kits/weather_station_website_orig.jpg
   :scale: 100 %
   :alt: Cosm datastreams shown as graph
   :align: center
   :target: ../../_images/Kits/weather_station_website_orig.jpg

In this project we will use JavaScript/AJAX to update the measurements
every 5 seconds, without the need to relaod the webpage.

An example implementation is available in :ref:`PHP <starter_kit_weather_station_website>`.


Further Enhancements
--------------------

.. note::
 If you modded, extended or improved your Weather Station in any way and you
 have published your results on our wiki, on your blog or similar: Please give
 us a notice. We would love to add a link to your project here!

Regenmesser, windgeschwindigkeit etc
