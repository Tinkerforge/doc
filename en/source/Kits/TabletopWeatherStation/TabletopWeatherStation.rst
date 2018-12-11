
:shoplink: ../../../shop/kits/tabletop-weather-station.html

.. include:: TabletopWeatherStation.substitutions
   :start-after: >>>general
   :end-before: <<<general

.. _tabletop_weather_station:

Tabletop Weather Station
========================

..
	.. raw:: html

		{% tfgallery %}

		Kits/weather_station_table_[100|800].jpg               Weather Station: Basic Kit on table
		Kits/weather_station_black_table_[100|800].jpg         Weather Station (black): Basic Kit on table
		Kits/weather_station_wall_far_[100|800].jpg            Weather Station: With Wi-Fi on wall
		Kits/weather_station_wall_near_[100|800].jpg           Weather Station: With Wi-Fi on wall
		Kits/weather_station_construction_rpi_front_[?|?].jpg  Weather Station: With Raspberry Pi
		Kits/weather_station_demo_[100|].jpg                   Weather Station: Demo Application
		Kits/weather_station_xively_graphs_[100|800].jpg       Weather Station: Xively graphs
		Kits/weather_station_lcd_all_[100|orig].jpg            Weather Station: Different Modes
		Kits/weather_station_website_[100|orig].jpg            Weather Station: Embedded in website
		Kits/weather_station_buttons_assembled_[100|800].jpg   Weather Station: With big buttons on the left side

		{% tfgalleryend %}

Features
--------

* Open source touch-capable Tabletop Weather Station
* Measures Temperature, Humidity, Air Pressure and Air Quaility Index
* Demo Application available (touch-capable, with graphs, database logging)
* Control over USB, Wi-Fi, Ethernet or with RED Brick
* Internet of Things (IoT) capable

Description
-----------

The *Tabletop Weather Station* is an open source touch-capable 
weather station. It measures temperature, humidity, air pressure and air quality
index with high precision. The basic kit consists of

* :ref:`Master Brick <master_brick>`,
* :ref:`Air Quality Bricklet <air_quality_bricklet>` and
* `Tabletop Weather Station case <TBD>`__.

It can be controlled by an (Embedded-) PC.
Control via Wi-Fi is possible if a :ref:`WIFI Extension 2.0 <wifi_v2_extension>` is 
added. Alternatively the weather station can be controlled over your local 
network when adding an :ref:`Ethernet Extension <ethernet_extension>`.
To use it standalone you can add a :ref:`RED Brick <red_brick>` or another
embedded board such as a :ref:`Raspberry Pi <embedded_raspberry_pi>`.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for other sensor Bricklets are 
available.

Programming of the weather station can be done with all of the available
bindings (|bindings|). Example implementations for many supported programming languages
and a demo application are available. The demo application offers 
graphs, logging to database, control via touch, etc. It is written in Python
and available for Windows, Linux and macOS.

The kit can be extended by an :ref:`Outdoor Weather Bricklet <outdoor_weather_bricklet>`.
Mounting holes and and an opening for the antenna are included in the Tabletop Weather 
Station enclosure. With this Bricklet you can receive data from the following
wireless outdoor weather station and sensor:

* `Outdoor Weather Station WS-6147 <https://www.tinkerforge.com/en/shop/outdoor-weather-station-ws-6147.html>`__
* `Temperature/Humidity Sensor TH-6148 <https://www.tinkerforge.com/en/shop/temperature-humidity-sensor-th-6148.html>`__

Both are supported by the demo application out-of-the-box.

TODO: Video

..
	.. raw:: html

	 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/uwsseiiu_4A" frameborder="0" allowfullscreen></iframe>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
IAQ Index Resolution              1
Air Pressure Resolution           0.0018mbar
Humidity Resolution               0.008%RH
Temperature Resolution            0.01°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
IAQ Index Accuracy                ±15 and ±15% of reading
Air Pressure Accuracy             ±0.12mbar (700-900mbar at 25-40°C), ±0.6mbar (full scale)
Humidity Accuracy                 ±3%RH (20-80%RH at 25°C)
Temperature Accuracy              ±0.5°C (at 25°C), ±1.0°C (0-65°C)*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            110 x 125 x 65mm
Weight                            TBDg 
================================  ============================================================

\* This is the temperature at the exact position of the sensor. If the Air Quality Bricklet is 
used inside of an enclosure, the air around the Bricklet may heat up more than the ambient air. 
The Bricklet does have API to calibrate this kind of offset. On the Tabletop Weather Station 
the Air Quality Bricklet is mounted outside of the enclosure to minimize self-heating.

.. _tabletop_weather_station_resources:

Resources
---------

* Tabletop Weather Station Case as FreeCAD CAD files (`Download <TODO>`__)
* TODO: Demo Application Download
* Simple examples: |examples_download|


Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect all Bricklets to the Master 
Brick and connect it via USB to your PC. Afterwards use Brick Viewer to check
if all of the firmwares up to date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_brick_firmware>` and
:ref:`update the Bricklets <brickv_flash_bricklet_plugin>` with the Brick
Viewer, too:

.. image:: /Images/Kits/tabletop_weather_station_update.jpg
   :scale: 100 %
   :alt: Tabletop Weather Station update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_update.jpg

As next step click through the tabs of the Brick Viewer
to see if all of the sensors are working correctly. Now you can be sure that 
the Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together in the weather station
enclosure.


.. _tabletop_weather_station_demo:

Demo Application
----------------

The demo application for the Tabletop Weather Station is written in Python. You
can find the source code `here <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo>`__ 
and executables for Linux, macOS and Windows are available 
`here <TBD>`__.

It shows the data of the Air Quality Bricklet as well as the Outdoor Weather Station.
Graphs can be drawn for different time frames, the data is logged in a sqlite database
with a configuratable period and the settings are configurable through the touch-interface
of the weather station itself.

TODO: Photos?

The application is segmented in "screens". Each screen is shown as a tab that can
have a text-label or icon. The touch-click/gesture and GUI callbacks of the 
LCD 128x64 Bricklet are passed through to the screen if it is selected.

You can add your own screens in the 
`custom_screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/custom_screens.py>`__.

A simple screen that displays the curent time looks as follows::

	class ClockScreen(Screen):
		# text/icon: Text is taken if no icon is available
		text = "Clock" # Text shown on tab
		icon = None    # Icon shown on tab (see icons.py and data/ sub-directory)

		# Called when tab is selected
		def draw_init(self):
			self.lcd.draw_text(40, 5, self.lcd.FONT_12X16, self.lcd.COLOR_BLACK, 'Time')
			self.draw_update()
		
		# Called when new data is available (usually once per second)
		def draw_update(self):
			# Get current time in HH:MM:SS format
			current_time = time.strftime("%H:%M:%S")
			self.lcd.draw_text(16, 30, self.lcd.FONT_12X16, self.lcd.COLOR_BLACK, current_time)


As a minimum you have to define a text (or optionally an icon) and a ``draw_init`` as well
ass ``draw_update`` function. For examples on how to react to touch-gestures and similar
you can take a look at the already implemented screens in
`screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/screens.py>`__.

The code above will create the following additional tab:

Pull request for new screens are definitely welcome, we are looking forward to integrate
your fancy screens into the demo applications :-).


.. _tabletop_weather_station_construction:

Construction
------------

TODO


.. _tabletop_weather_station_examples:

Examples
--------

If you don't want to use Python or you want to write your own program that does not use the
:ref:`Demo Application <tabletop_weather_station_demo>` as a starting point, you can take
a look at the following examples:

.. include:: TabletopWeatherStation.substitutions
   :start-after: >>>example_list
   :end-before: <<<example_list

These examples will write the measured data to the display in an one second interval. They
are written to be as simple as possible, but with a robust approach. They will wait
for the Brick Daemon to be available, automatically reconnect if necessary, automatically
discover UIDs and support hotplug.

Thus they are a good starting point for the foundation of your own custom application.

.. _tabletop_weather_station_red:

Standalone with RED Brick
-------------------------

TODO?


.. _tabletop_weather_station_openhab:

Smart Home Integration using openHAB
------------------------------------

TODO?
