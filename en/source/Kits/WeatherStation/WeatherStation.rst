
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Weather Station

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
	    tfdocimg("Kits/weather_station_lcd_all_100.jpg",
	             "Kits/weather_station_lcd_all_orig.jpg",
	             "Weather Station: Different Modes")
	}}
	{{
	    tfdocimg("Kits/weather_station_website_100.jpg",
	             "Kits/weather_station_website_orig.jpg",
	             "Weather Station: Embedded in website")
	}}
	{{ tfdocend() }}

The *Starter Kit: Weather Station* is a fully-fledged open source weather
station. It measures temperature, humidity, air pressure and illuminance.

It can be controlled by a PC or a :ref:`Raspberry Pi <embedded_raspberry_pi>`
over USB or (if the :ref:`WIFI Extension <wifi_extension>` is added) over Wi-Fi.
The measurements can be displayed on the 20x4 LCD, they can be shown on a
website or uploaded to `Cosm <https://cosm.com/>`__. With the four buttons of
the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` it is possible to control
different modes.

Mounting holes for :ref:`Analog In <analog_in_bricklet>`
and :ref:`IO-4 <io4_bricklet>` Bricklets are provided, this gives the
possibility to add more sensors (anemometer, pluviometer etc). The plastic
is tinker-friendly PMMA, new drill holes and similar can be added with a
simple wood drill.

Programming of the weather station can be done with all of the available
bindings (C/C++, C#, Delphi, Java, PHP, Python, Ruby, VB.NET) and example
implementations with step-by-step instructions are available for all
of the languages.

Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.
For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Use Brick Viewer to find out
if all of the firmwares up to date (Updates / Flashing button). If not, you can
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

.. batti: screenshot brickv with all tabs?

Construction
------------

TODO: Images of construction and instructions

Projects
--------

There are several applications for the Weather Station Starter Kit.

Display Environment Measurements on LCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most obvious application for the Weather Station Starter Kit is to display
the measurements of the environment on the LCD 20x4 Bricklet. This can be
done through three different paths:

* USB connection to PC: Install brickd and application on PC, connect
  Master Brick of Weather Station to PC via USB.
* Wi-Fi connection to PC: Install application on PC, connect to
  Weather Station directly over Wi-Fi or through an access point.
* Raspberry Pi or other embedded board integrated in Weather Station:
  Install brickd and application on embedded board, connect Master Brick of
  Weather Station to embedded board via USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

All three possible solutions can use the same source code.

Example implementations with step-by-step instructions are available for:

:ref:`C/C++ <starter_kit_weather_station_c_to_lcd>`,
:ref:`C# <starter_kit_weather_station_csharp_to_lcd>`,
:ref:`Delphi <starter_kit_weather_station_delphi_to_lcd>`,
:ref:`Java <starter_kit_weather_station_java_to_lcd>`,
:ref:`PHP <starter_kit_weather_station_php_to_lcd>`,
:ref:`Python <starter_kit_weather_station_python_to_lcd>`,
:ref:`Ruby <starter_kit_weather_station_ruby_to_lcd>`,
:ref:`VB.NET <starter_kit_weather_station_vbnet_to_lcd>`.

Connect to Cosm
^^^^^^^^^^^^^^^

`Cosm <https://cosm.com/>`__ is a service that provides the possibility to
analyze and visualize the "Internet of Things". They can store a history of our
Weather Station data and we get pretty graphs:
Cosm is a service that provides the possibility to analyze and visualize
the "Internet of Things". They can store a history of our Weather Station
data and we get pretty graphs:

.. image:: /Images/Kits/weather_station_cosm_graphs_600.jpg
   :scale: 100 %
   :alt: Cosm datastreams shown as graph
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_graphs_orig.jpg

An example implementation with step-by-step instructions that shares the
weather data with Cosm is available
in :ref:`Python <starter_kit_weather_station_cosm>`.

Embed Live Measurements on Website
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another application for the Weather Station, is to embed the weather data
on a website:

.. image:: /Images/Kits/weather_station_website_orig.jpg
   :scale: 100 %
   :alt: Live Measurements on Website
   :align: center
   :target: ../../_images/Kits/weather_station_website_orig.jpg

In this project we will use JavaScript/AJAX to update the measurements
every 5 seconds, without the need to reload the webpage.

An example implementation is available
in :ref:`PHP <starter_kit_weather_station_website>`.

Show Statistics with Button Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` features four buttons,
we can enhance the first application by more data that can be switched with
the buttons.

.. image:: /Images/Kits/weather_station_lcd_all_orig.jpg
   :scale: 100 %
   :alt: Different modes of button control project
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_all_orig.jpg

The four buttons in this project will be used to switch through

* standard weather measurement,
* 24h min/max/average,
* 24h graph and
* time and date.

An example implementation is available
in :ref:`C# <starter_kit_weather_station_button_control>`.

Further Enhancements
--------------------

.. note::
 If you modded, extended or improved your Weather Station in any way and you
 have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
 on your blog or similar: Please give us a notice. We would love to add a link
 to your project here!

Regenmesser, windgeschwindigkeit etc
