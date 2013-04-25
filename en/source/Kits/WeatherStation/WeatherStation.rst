
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Weather Station
:shoplink: ../../../shop/kits/starter-kit-weather-station.html

.. include:: WeatherStation.substitutions

.. _starter_kit_weather_station:

Starter Kit: Weather Station
============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/weather_station_table_350.jpg",
	               "Kits/weather_station_table_800.jpg",
	               "Weather Station: Basic Kit on table")
	}}
	{{
	    tfdocimg("Kits/weather_station_black_table_100.jpg",
	             "Kits/weather_station_black_table_800.jpg",
	             "Weather Station (black): Basic Kit on table")
	}}
	{{
	    tfdocimg("Kits/weather_station_wall_far_100.jpg",
	             "Kits/weather_station_wall_far_800.jpg",
	             "Weather Station: With Wi-Fi on wall")
	}}
	{{
	    tfdocimg("Kits/weather_station_wall_near_100.jpg",
	             "Kits/weather_station_wall_near_800.jpg",
	             "Weather Station: With Wi-Fi on wall")
	}}
	{{
	    tfdocimg("Kits/weather_station_construction_rpi_front_100.jpg",
	             "Kits/weather_station_construction_rpi_front_800.jpg",
	             "Weather Station: With Raspberry Pi")
	}}
	{{
	    tfdocimg("Kits/weather_station_cosm_graphs_100.jpg",
	             "Kits/weather_station_cosm_graphs_800.jpg",
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
	{{
	    tfdocimg("Kits/weather_station_buttons_assembled_100.jpg",
	             "Kits/weather_station_buttons_assembled_800.jpg",
	             "Weather Station: With big buttons on the left side")
	}}
	{{ tfdocend() }}

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

* Fully-fledged open source weather station.
* Measures Temperature, Humidity, Air Pressure and Illuminance.
* High Precision and Resolution

  * e.g. Air Pressure 0.012mbar and Temperature 0.01°C

* Control over USB, Wi-Fi or with Raspberry Pi.
* Modifiable with more buttons, more sensors and changed software.

Description
-----------

The *Starter Kit: Weather Station* is a fully-fledged open source weather
station. It measures temperature, humidity, air pressure and illuminance
with high precision.

It can be controlled by an (Embedded-) PC.
Control via Wi-Fi is possible if a :ref:`WIFI Extension <wifi_extension>` is 
added. To use it standalone you can add an embedded board such as the
:ref:`Raspberry Pi <embedded_raspberry_pi>` which can be mounted in the casing.
The measurements can be displayed on the 20x4 character LCD, they can be shown on a
website or uploaded to `Cosm <https://cosm.com/>`__. With the four buttons of
the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` it is possible to control
different modes.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
:ref:`Analog In <analog_in_bricklet>` and :ref:`IO-4 <io4_bricklet>` Bricklets
are provided, this gives the possibility to add more sensors 
(`anemometer <https://en.wikipedia.org/wiki/Anemometer>`__, 
`pluviometer <https://en.wikipedia.org/wiki/Rain_gauge>`__ etc). 

Programming of the weather station can be done with all of the available
bindings (|bindings|). Example implementations for each of the languages are
available. This will give you a starting point into the programming with 
Tinkerforge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Air Pressure                      10mbar - 1200mbar in 0.012mbar steps
Illumination                      0lux - 900lux in 0.1lux steps
Relative Humidity                 0% RH - 10% RH in 0.1% RH steps
Temperature                       -40°C - 85°C in 0.01°C steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            240 x 46 x 100mm (9.45 x 1.81 x 3.94")
Weight                            376g
================================  ============================================================


Resources
---------

* Weather Station case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/weather-station/tree/master/case>`__)
* Example source code *Write to LCD* (Download: |write_to_lcd_examples_download|)
* Example source code *Cosm* (Download: `Python <https://github.com/Tinkerforge/weather-station/tree/master/cosm/python>`__)
* Example source code *Website* (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
* Example source code *Button Control* (Download: `C# <https://github.com/Tinkerforge/weather-station/tree/master/button_control/csharp>`__)

Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect all Bricklets to the Master 
Brick and connect it via USB to your PC. Afterwards use Brick Viewer to find out
if all of the firmwares up to date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer, too:

.. image:: /Images/Kits/weather_station_update_350.jpg
   :scale: 100 %
   :alt: Weather Station update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/weather_station_update_orig.jpg

As next step click through the tabs of the Brick Viewer
to see if all of the sensors are working correctly. Now you can be sure that 
the Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together in the weather station
enclosure.

Construction
------------

There is no singular way to build the Weather Station. In the
following we will show one way to build different extension
stages. The idea of the Weather Station Starter Kit is, that
it is easily extensible and modifiable. 

For example: You can put the Bricks and Bricklets on spacers
(as is mostly shown below), but you can also screw them directly
to the case to save space. There are several holes that allow
to mount addition Analog In, Temperature or IO-4 Bricklets to
read out more sensors. 

The utilized PMMA plastic is easy to work with, so you will be able
to add new holes or slots or similar if needed.

Three extension stages
^^^^^^^^^^^^^^^^^^^^^^

* :ref:`Basic Weather Station <starter_kit_weather_station_construction_basic>`
* :ref:`Wi-Fi Weather Station <starter_kit_weather_station_construction_wifi>`
* :ref:`Raspberry Pi Weather Station <starter_kit_weather_station_construction_rpi>`

RS485, Ethernet, etc.
^^^^^^^^^^^^^^^^^^^^^

We could also control the Weather Station with the RS485 or
Ethernet Extension. The setup in this case is the same as with the Wi-Fi
Weather Station, we just have to exchange the WIFI Extension with the
RS485 or Ethernet Extension.

If the Ethernet Extension is used, the stack can also be powered by PoE.
in this case the Step-Down Power Supply and the DC Jack Adapter are
not needed.

Projects
--------

There are several applications for the Weather Station:

Display Environment Measurements on LCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most obvious application for the Weather Station Starter Kit is to display
the measurements of the environment on the LCD 20x4 Bricklet. This can be
done through three different paths:

* USB connection to PC: Install Brick Daemon and application on PC, connect
  Master Brick of Weather Station to PC via USB.
* Wi-Fi connection to PC: Install application on PC, connect to
  Weather Station directly over Wi-Fi or through an access point.
* Raspberry Pi or other embedded board integrated in Weather Station:
  Install Brick Daemon and application on embedded board, connect
  Master Brick of Weather Station to embedded board via USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

All three possible solutions can use the same source code.

Example implementations with step-by-step instructions are available for:

|write_to_lcd_examples|.

Connect to Cosm
^^^^^^^^^^^^^^^

`Cosm <https://cosm.com/>`__ is a service that provides the possibility to
analyze and visualize the "Internet of Things". They can store a history of our
Weather Station data and we get pretty graphs:

.. image:: /Images/Kits/weather_station_cosm_graphs_600.jpg
   :scale: 100 %
   :alt: Cosm datastreams shown as graph
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_graphs_orig.jpg

An example implementation with step-by-step instructions that shares the
weather data with Cosm is available
in :ref:`Python <starter_kit_weather_station_cosm>`.

The Weather Station in our laboratory has the Cosm feed 
`125881 <https://cosm.com/feeds/125881>`__.

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

If you modded, extended or improved your Weather Station in any way and you
have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!


Bigger Push Buttons
^^^^^^^^^^^^^^^^^^^

The push buttons on the LCD 20x4 Bricklet are a bit fiddly. To extend
the Weather Station with bigger buttons we provide the
`Weather Station Push Button Extension
<https://www.tinkerforge.com/en/shop/kits/weather-station-push-button-extension.html>`__.

.. image:: /Images/Kits/weather_station_buttons_assembled_600.jpg
   :scale: 100 %
   :alt: Weather Station with big push buttons
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_assembled_1200.jpg

The extension consists of four big push buttons, a replacement wall for the left
side of the Weather station case and a right angle 2x3 pin header.

We can connect the push buttons to the LCD 20x4 Bricklet with a little bit
of soldering and some wires.

.. image:: /Images/Kits/weather_station_buttons_soldered_350.jpg
   :scale: 100 %
   :alt: Push buttons wired up
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_soldered_1200.jpg

.. image:: /Images/Kits/weather_station_buttons_and_lcd_350.jpg
   :scale: 100 %
   :alt: Push buttons connected to LCD 20x4
   :align: center
   :target: ../../_images/Kits/weather_station_buttons_and_lcd_1200.jpg

Changes in software are not needed.

As a fun example we have implemented a demonstrator for a game like Guitar Hero. 
It does not have much functions. The application basically shows bars which will 
be randomly rendered and moved to one side of the LCD.
With the four big push buttons you can make different sounds and you can choose
the used instrument from the 
`General MIDI <http://en.wikipedia.org/wiki/General_MIDI>`__ definition, 
but the game logic is completely missing.

This demonstrator should show that it is possible to implement not only
weather station applications. 

.. image:: /Images/Kits/weather_station_guitar_350.jpg
   :scale: 100 %
   :alt: Game Application on Weather Station
   :align: center
   :target: ../../_images/Kits/weather_station_guitar_1200.jpg

The source code can be downloaded here: `Download
<https://raw.github.com/Tinkerforge/weather-station/master/examples/GuitarStation.java>`__


.. FIXME: Regenmesser, windgeschwindigkeit etc
