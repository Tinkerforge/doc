
:shoplink: ../../../shop/kits/starter-kit-weather-station.html

.. include:: WeatherStation.substitutions

.. _starter_kit_weather_station:

Starter Kit: Weather Station
============================

.. raw:: html

	{% tfgallery %}

	Kits/weather_station_table_[100|800].jpg               Weather Station: Basic Kit on table
	Kits/weather_station_black_table_[100|800].jpg         Weather Station (black): Basic Kit on table
	Kits/weather_station_wall_far_[100|800].jpg            Weather Station: With Wi-Fi on wall
	Kits/weather_station_wall_near_[100|800].jpg           Weather Station: With Wi-Fi on wall
	Kits/weather_station_construction_rpi_front_[?|?].jpg  Weather Station: With Raspberry Pi
	Kits/weather_station_demo_[100|].png                   Weather Station: Demo Application
	Kits/weather_station_lcd_all_[100|orig].jpg            Weather Station: Different Modes
	Kits/weather_station_website_[100|orig].jpg            Weather Station: Embedded in website
	Kits/weather_station_buttons_assembled_[100|800].jpg   Weather Station: With big buttons on the left side

	{% tfgalleryend %}

Features
--------

.. Einrueckung so beibehalten, da sonst kaputt

* Fully-fledged open source weather station
* Measures Temperature, Humidity, Air Pressure and Illuminance
* High Precision and Resolution

  * e.g. Air Pressure 0.012hPa and Temperature 0.01°C

* Control over USB, Wi-Fi and Ethernet or with RED Brick and Raspberry Pi
* Modifiable: more buttons, more sensors and customized software
* Demo Application available
* Internet of Things (IoT) capable

Description
-----------

The *Starter Kit: Weather Station* is a fully-fledged open source weather
station. It measures temperature, humidity, air pressure and illuminance
with high precision.

It can be controlled by an (Embedded-) PC.
Control via Wi-Fi is possible if a :ref:`WIFI Extension <wifi_extension>` is 
added. As alternative the weather station can be controlled over your local 
network when adding an :ref:`Ethernet Extension <ethernet_extension>`.
To use it standalone you can add a :ref:`RED Brick <red_brick>` or another
embedded board such as a
:ref:`Raspberry Pi <embedded_raspberry_pi>` which can be mounted in the case.
Thus Internet of Things applications are a possible with this kit.

There are several example projects available, e.g. the measurements can be 
displayed on the 20x4 character LCD or shown on a
website.
With the four buttons of the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` 
it is possible to control different modes.

A demo application, available for Windows, Linux and macOS, implements
some of these example projects and can be used to test the station.

The kit allows to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
:ref:`Analog In <analog_in_bricklet>` and :ref:`IO-4 <io4_bricklet>` Bricklets
are provided, this gives the possibility to add more sensors 
(`anemometer <https://en.wikipedia.org/wiki/Anemometer>`__, 
`pluviometer <https://en.wikipedia.org/wiki/Rain_gauge>`__ etc). 

Programming of the weather station can be done with all of the available
bindings (|bindings|). Example implementations for many supported programming languages
and a demo application are available. This will give you a starting point into the 
programming with Tinkerforge.

A small video that shows the construction and some applications 
is available on Youtube:

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/uwsseiiu_4A" frameborder="0" allowfullscreen></iframe>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Air Pressure                      10hPa - 1200hPa in 0.012hPa steps
Illumination                      0lx - 64000lx in 0.01lx steps
Relative Humidity                 0%RH - 100%RH in 0.1%RH steps
Temperature                       -40°C - 85°C in 0.01°C steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            240 x 46 x 100mm (9.45 x 1.81 x 3.94")
Weight                            376g
================================  ============================================================

.. _starter_kit_weather_station_resources:

Resources
---------

* Weather Station Case as FreeCAD CAD files (`Download <https://github.com/Tinkerforge/weather-station/tree/master/case>`__)
* Example Source Code for :ref:`starter_kit_weather_station_write_to_lcd` (Download: |write_to_lcd_examples_download|)
* Example Source Code for :ref:`starter_kit_weather_station_website` (Download: `PHP <https://github.com/Tinkerforge/weather-station/tree/master/website/php>`__)
* Example Source Code for :ref:`starter_kit_weather_station_button_control` (Download: `C# <https://github.com/Tinkerforge/weather-station/tree/master/button_control/csharp>`__)
* Example Configuration for :ref:`starter_kit_weather_station_openhab` (`Download <https://github.com/Tinkerforge/weather-station/tree/master/openhab>`__)
* :ref:`starter_kit_weather_station_demo` (Download: `Windows <https://download.tinkerforge.com/kits/weather_station/windows/starter_kit_weather_station_demo_windows_latest.exe>`__, `Linux <https://download.tinkerforge.com/kits/weather_station/linux/starter-kit-weather-station-demo_linux_latest.deb>`__, `macOS <https://download.tinkerforge.com/kits/weather_station/macos/starter_kit_weather_station_demo_macos_latest.dmg>`__, `Source Code <https://github.com/Tinkerforge/weather-station/tree/master/demo>`__)


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


.. _starter_kit_weather_station_demo:

Demo Application
----------------

If the hardware is running correctly you can also try the demo application for 
this Starter Kit: Weather Station. It implements two of the presented
:ref:`projects <starter_kit_weather_station_projects>` for demonstration
purposes:

1. :ref:`starter_kit_weather_station_write_to_lcd`
2. :ref:`starter_kit_weather_station_button_control`

Each project can be selected with its own tab. The first project only displays
the measured values. The second project is more complex and displays 
min, max and average values as well as graphs for these measurements.
The display mode can be changed by pressing the buttons at the LCD 20x4 
Bricklet or in the application. In some modes the buttons can be pressed
multiple times, such that other measurements will be shows. 


The download link is in the :ref:`resources
<starter_kit_weather_station_resources>` section.

.. image:: /Images/Kits/weather_station_demo_350.png
   :scale: 100 %
   :alt: Weather Station Demo Application Screenshot
   :align: center
   :target: ../../_images/Kits/weather_station_demo.png

Construction
------------

There is no singular way to build the Weather Station. In the
following we will show one way to build different variants.
The idea of the Weather Station Starter Kit is, that
it is easily extensible and modifiable. 

For example: You can put the Bricks and Bricklets on spacers
(as is mostly shown below), but you can also screw them directly
to the case to save space. There are several holes that allow
to mount addition Analog In, Temperature or IO-4 Bricklets to
read out more sensors. 

The utilized PMMA plastic is easy to work with, so you will be able
to add new holes or slots or similar if needed.

Here are four different construction variants:

* :ref:`Basic Weather Station <starter_kit_weather_station_construction_basic>`
* :ref:`Wi-Fi Weather Station <starter_kit_weather_station_construction_wifi>`
* :ref:`RED Brick Weather Station <starter_kit_weather_station_construction_red_brick>`
* :ref:`Raspberry Pi Weather Station <starter_kit_weather_station_construction_raspberry_pi>`

.. toctree::
   :hidden:

   Basic <Construction_Basic>
   With Wi-Fi <Construction_Wifi>
   With RED Brick <Construction_REDBrick>
   With Raspberry Pi <Construction_RaspberryPi>

We could also control the Weather Station with the RS485 or
Ethernet Extension. The setup in this case is the same as with the "Wi-Fi
Weather Station" described above, we just have to exchange the WIFI Extension 
with the RS485 or Ethernet Extension.

If the Ethernet Extension with PoE is used, the stack can also be powered by 
PoE. in this case the Step-Down Power Supply and the DC Jack Adapter are not 
needed.


.. _starter_kit_weather_station_projects:

Projects
--------

There are several applications for the Weather Station:


.. _starter_kit_weather_station_write_to_lcd:

Display Environment Measurements on LCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most obvious application for the Weather Station Starter Kit is to display
the measurements of the environment on the LCD 20x4 Bricklet. This can be
done through four different paths:

* USB connection to PC: Install Brick Daemon and application on PC, connect
  Master Brick of Weather Station to PC via USB.
* Wi-Fi connection to PC: Install application on PC, connect to
  Weather Station directly over Wi-Fi or through an access point.
* RED Brick: Use Brick Viewer to upload the application. How this works
  in detail is described in the :ref:`RED Brick documenation <red_brick_program_tab>`.
* Raspberry Pi or other embedded board integrated in Weather Station:
  Install Brick Daemon and application on embedded board, connect
  Master Brick of Weather Station to embedded board via USB.

.. batti: link to further enhancement section? how to use rasp with weather station etc.

All four possible solutions can use the same source code.

Example implementations with step-by-step instructions are available for: |write_to_lcd_examples|.

.. include:: WriteToLCD.toctree


.. _starter_kit_weather_station_website:

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
every 5 seconds, without the need to reload the website.

An example implementation is available
in :ref:`PHP <starter_kit_weather_station_website_php>`.

.. toctree::
   :hidden:

   PHPToWebsite


.. _starter_kit_weather_station_button_control:

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
in :ref:`C# <starter_kit_weather_station_button_control_csharp>`.

.. toctree::
   :hidden:

   CSharpToButtonControl


.. _starter_kit_weather_station_openhab:

Smart Home Integration using openHAB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Weather Station can be integrated into an `openHAB <https://www.openhab.org/>`__
managed smart home using the `openHAB Tinkerforge bindings
<https://github.com/openhab/openhab/wiki/Tinkerforge-Binding/>`__.

.. image:: /Images/Kits/weather_station_openhab_orig.jpg
   :scale: 100 %
   :alt: openHAB example sitemap
   :align: center
   :target: ../../_images/Kits/weather_station_openhab_orig.jpg

As an example the required :ref:`openHAB configuration steps
<starter_kit_weather_station_openhab_red_brick>` for the integration are
demonstrated using a RED Brick.

.. toctree::
   :hidden:

   OpenHABOnREDBrick


Further Enhancements
--------------------

If you modded, extended or improved your Weather Station in any way and you
have published your results on our `Wiki <https://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!


Bigger Push Buttons
^^^^^^^^^^^^^^^^^^^

The push buttons on the LCD 20x4 Bricklet are a bit fiddly. To extend
the Weather Station with bigger buttons we provide the
`Weather Station Push Button Extension
<https://www.tinkerforge.com/en/shop/kits/weather-station-push-button-add-on.html>`__.

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

To connect a button to the LCD 20x4 Bricklet you have to connect one pin of the button with
GND and the other with one input of the LCD 20x4 Bricklet (BTN0-BTN3). In the pictures 
above we have used a black wire to connect GND through and red wires to connect each button
with one input.

.. image:: /Images/Kits/weather_station_button_wiring_350.jpg
   :scale: 100 %
   :alt: Button Connect How-To
   :align: center
   :target: ../../_images/Kits/weather_station_button_wiring.jpg


As a fun example we have implemented a demonstrator for a game like Guitar Hero. 
It does not have much functions. The application basically shows bars which will 
be randomly rendered and moved to one side of the LCD.
With the four big push buttons you can make different sounds and you can choose
the used instrument from the 
`General MIDI <https://en.wikipedia.org/wiki/General_MIDI>`__ definition,
but the game logic is completely missing.

This demonstrator should show that it is possible to implement not only
weather station applications. 

.. image:: /Images/Kits/weather_station_guitar_350.jpg
   :scale: 100 %
   :alt: Game Application on Weather Station
   :align: center
   :target: ../../_images/Kits/weather_station_guitar_1200.jpg

The source code can be downloaded here: `Download
<https://raw.githubusercontent.com/Tinkerforge/weather-station/master/examples/GuitarStation.java>`__


.. FIXME: Regenmesser, windgeschwindigkeit etc
