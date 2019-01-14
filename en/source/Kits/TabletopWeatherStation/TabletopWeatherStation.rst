
:shoplink: ../../../shop/kits/tabletop-weather-station.html

.. include:: TabletopWeatherStation.substitutions
   :start-after: >>>general
   :end-before: <<<general

.. _tabletop_weather_station:

Tabletop Weather Station
========================

.. raw:: html

	{% tfgallery %}

	Kits/tabletop_weather_station_transparent_right_titled_[?|?].jpg    Tabletop Weather Station
	Kits/tabletop_weather_station_content_[?|?].jpg                     Tabletop Weather Station
	Kits/tabletop_weather_station_transparent_back_[?|?].jpg            Tabletop Weather Station
	Kits/tabletop_weather_station_transparent_back_titled_[?|?].jpg     Tabletop Weather Station
	Kits/tabletop_weather_station_transparent_titled_[?|?].jpg          Tabletop Weather Station
	Kits/tabletop_weather_station_transparent_titled_pwr_[?|?].jpg      Tabletop Weather Station
	Kits/tabletop_weather_station_complete_transparent_back_[?|?].jpg   Tabletop Weather Station
	Kits/tabletop_weather_station_black_right_back_[?|?].jpg            Tabletop Weather Station
	Kits/tabletop_weather_station_black_right_titled_[?|?].jpg          Tabletop Weather Station
	Kits/tabletop_weather_station_blue_back_[?|?].jpg                   Tabletop Weather Station
	Kits/tabletop_weather_station_blue_left_back_[?|?].jpg              Tabletop Weather Station
	Kits/tabletop_weather_station_blue_right_titled_[?|?].jpg           Tabletop Weather Station
	Kits/tabletop_weather_station_colors_[?|?].jpg                      Tabletop Weather Station
	Kits/tabletop_weather_station_colors_side_by_side_[?|?].jpg         Tabletop Weather Station
	Kits/tabletop_weather_station_frosted_back_[?|?].jpg                Tabletop Weather Station
	Kits/tabletop_weather_station_frosted_right_titled_[?|?].jpg        Tabletop Weather Station
	Kits/tabletop_weather_station_frosted_titled_[?|?].jpg              Tabletop Weather Station
	Kits/tabletop_weather_station_screen_graph_[?|?].jpg                Tabletop Weather Station
	Kits/tabletop_weather_station_screen_main_[?|?].jpg                 Tabletop Weather Station
	Kits/tabletop_weather_station_screen_outdoor_[?|?].jpg              Tabletop Weather Station
	Kits/tabletop_weather_station_screen_sensor_[?|?].jpg               Tabletop Weather Station
	Kits/tabletop_weather_station_screen_settings_[?|?].jpg             Tabletop Weather Station

	{% tfgalleryend %}

Features
--------

* Open source touch-capable Tabletop Weather Station
* Measures Temperature, Humidity, Air Pressure and Air Quality Index
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
Mounting holes and an opening for the antenna are included in the Tabletop Weather 
Station enclosure. With this Bricklet you can receive data from the following
wireless outdoor weather station and sensor:

* `Outdoor Weather Station WS-6147 <https://www.tinkerforge.com/en/shop/outdoor-weather-station-ws-6147.html>`__
* `Temperature/Humidity Sensor TH-6148 <https://www.tinkerforge.com/en/shop/temperature-humidity-sensor-th-6148.html>`__

Both are supported by the demo application out-of-the-box.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/dz18cRKUvgA" frameborder="0" allowfullscreen></iframe>

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
Temperature Accuracy              ±0.5°C (at 25°C), ±1.0°C (0-65°C)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            110 x 125 x 65mm
Weight                            238g (basic), 288g (basic + RED Brick + Outdoor Weater Bricklet)
================================  ============================================================


.. _tabletop_weather_station_resources:

Resources
---------

* Tabletop Weather Station Case as FreeCAD CAD files (`Download <TODO>`__)
* Demo Application (Download: `Windows <http://download.tinkerforge.com/kits/tabletop_weather_station/windows/tabletop_weather_station_demo_windows_latest.exe>`__, `Linux <http://download.tinkerforge.com/kits/tabletop_weather_station/linux/tabletop-weather-station-demo-linux_latest.deb>`__, `macOS <http://download.tinkerforge.com/kits/tabletop_weather_station/macos/tabletop_weather_station_demo_macos_latest.dmg>`__, `Source Code <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo>`__)
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

.. image:: /Images/Kits/tabletop_weather_station_gui_600.jpg
   :scale: 100 %
   :alt: GUI on the LCD 128x64 Bricklet
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_gui_1000.jpg

The application is segmented in "screens". Each screen is shown as a tab that can
have a text-label or icon. The touch-click/gesture and GUI callbacks of the 
LCD 128x64 Bricklet are passed through to the screen if it is selected.

You can add your own screens in the 
`custom_screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/tabletop_weather_station_demo/custom_screens.py>`__.

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
`screens.py <https://github.com/Tinkerforge/tabletop-weather-station/blob/master/demo/tabletop_weather_station_demo/screens.py>`__.

The code above will create the following additional tab:

.. image:: /Images/Kits/tabletop_weather_station_screen_clock_600.jpg
   :scale: 100 %
   :alt: Clock Screen
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_screen_clock_1000.jpg


Pull requests for new screens are definitely welcome, we are looking forward to integrate
your fancy screens into the demo applications :-).


.. _tabletop_weather_station_construction:

Construction
------------

To assemble the Tabletop Weather Station we recommend that you first screw all
of the Bricks/Brickelts to the plastic parts and put the parts together afterwards.

.. image:: /Images/Exploded/tabletop_weather_station_explosion_master_700.png
   :scale: 100 %
   :alt: Exploded assembly drawing
   :align: center
   :target: ../../_images/Exploded/tabletop_weather_station_explosion_master.png

If you want to add a RED Brick and/or Outdoor Weather Bricklet, you can attach them
to the same plate as the Master Brick:

.. image:: /Images/Exploded/tabletop_weather_station_explosion_complete_700.png
   :scale: 100 %
   :alt: Exploded assembly drawing
   :align: center
   :target: ../../_images/Exploded/tabletop_weather_station_explosion_complete.png

As you can see in the exploded assembly drawings, we attach the
Air Quality Bricklet to the outside of the weather station. This ensures that the
heat comming from the other components (LCD 128x64 Bricklet, Master Brick, perhaps a
RED Brick) does not influence the temperature measurement of the Air Quality Bricklet.

You can also screw the Air Quality Bricklet to the inside. In this case we recommend
that you use the temperature calibration function of the Bricklet to correct it to
the temperature of the outside. This is important since the temperature is also used
to determine the correct Indoor Air Quality Index and Humidity.

Below you can find a sped-up video of the assembly. During crucial parts the speed
of the video is slowed down.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/-3BiX39U5_A" frameborder="0" allowfullscreen></iframe>


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

You can add a RED Brick to the Tabletop Weather Station below the
Master Brick. In this case the power is supplied through the USB
connector of the RED Brick.

.. image:: /Images/Kits/tabletop_weather_station_transparent_back2_600.jpg
   :scale: 100 %
   :alt: RED Brick in Tabletop Weather Station case
   :align: center
   :target: ../../_images/Kits/tabletop_weather_station_transparent_back2_1000.jpg

With the RED Brick you can upload your application and make the
Tabletop Weather Station standalone. To upload the demo application
go to the RED Brick tab in Brick Viewer and click on "Program" and "New".

Choose a name and Python as language.

.. image:: /Images/Kits/tabletop_weather_station_red1.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

Add the files of the demo application. You can find the files
`on GitHub <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/demo/tabletop_weather_station_demo>`__.
If you already had the weather station running before, you can also
upload the SQLite database (``.tabletop_weather_station_demo.db`` in your home
directory) to retain the data.

.. image:: /Images/Kits/tabletop_weather_station_red2.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

Choose ``main.py`` as script file.

.. image:: /Images/Kits/tabletop_weather_station_red3.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

There is no standard input for the demo, otherwise you can leave
the rest of the configurations as default.

.. image:: /Images/Kits/tabletop_weather_station_red4.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red5.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red6.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

.. image:: /Images/Kits/tabletop_weather_station_red7.jpg
   :scale: 100 %
   :alt: Upload demo application to RED Brick with Brick Viewer
   :align: center

After the upload is finished the demo application should be
able to automatically run on the RED Brick after power-up!

..
	.. _tabletop_weather_station_openhab:
	Smart Home Integration using openHAB
	------------------------------------
	TODO?
