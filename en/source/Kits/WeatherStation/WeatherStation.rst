
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Weather Station

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
	{{ tfdocend() }}

Features
--------

* Fully-fledged open source weather station.
* Measure Temperature, Humidity, Air Pressure and Illuminance.
* Control over USB, Wi-Fi or with Raspberry Pi.
* Modifiable with more buttons, more sensors and better software.

Description
-----------

The *Starter Kit: Weather Station* is a fully-fledged open source weather
station. It measures temperature, humidity, air pressure and illuminance
with high precision.

It can be controlled by a PC or a :ref:`Raspberry Pi <embedded_raspberry_pi>`
over USB or (if the :ref:`WIFI Extension <wifi_extension>` is added) over Wi-Fi.
The measurements can be displayed on the 20x4 character LCD, they can be shown on a
website or uploaded to `Cosm <https://cosm.com/>`__. With the four buttons of
the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` it is possible to control
different modes.

The kit allows it to modify soft- and hardware. The casing consists of
tinker-friendly PMMA which can be easily modified (e.g. drill new holes with 
simple wood drill). Additionally mounting holes for 
:ref:`Analog In <analog_in_bricklet>` and :ref:`IO-4 <io4_bricklet>` Bricklets
are provided, this gives the possibility to add more sensors (anemometer, 
pluviometer etc). 

Programming of the weather station can be done with all of the available
bindings (|bindings|). Example implementations for each of the languages are
available, this will give you a starting point into the programming with 
Tinkerforge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Air Pressure                      10mbar - 1200mbar in 0.012mbar steps
Illumination                      0lux - 900lux in 0.1lux steps, 12bit resolution
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
* Example source code *Write to LCD* (Download: `C <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/c>`__, `C# <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/csharp>`__, `Delphi <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/delphi>`__, `Java <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/java>`__, `PHP <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/php>`__, `Python <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/python>`__, `Ruby <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/ruby>`__, `Visual Basic .NET <https://github.com/Tinkerforge/weather-station/tree/master/write_to_lcd/vbnet>`__)
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

.. batti: screenshot brickv with all tabs?

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

Basic Weather Station
^^^^^^^^^^^^^^^^^^^^^

The basic Weather Station Kit comes with :ref:`Ambient Light
<ambient_light_bricklet>`, :ref:`Barometer <barometer_bricklet>`,
:ref:`Humidity <humidity_bricklet>` and :ref:`LCD 20x4 Bricklet
<lcd_20x4_bricklet>`, :ref:`Master Brick <master_brick>`, the Weather Station
case including a replacement side element for a :ref:`DC Jack Adapter
<dc_jack_adapter>`, Bricklet cables and USB cable as well as lots of screws,
spacers, nuts and washers.

.. image:: /Images/Kits/weather_station_content_350.jpg
   :scale: 100 %
   :alt: Weather Station kit content
   :align: center
   :target: ../../_images/Kits/weather_station_content_1200.jpg

There are several ways to mount the Bricks and Bricklets in the
case. In this construction tutorial we will show one way to
put everything together.

We will start by screwing the Master Brick on the back side. We use
screws from the top and bottom with 10mm spacers at the bottom inside
of the case. The USB connector of the Master Brick faces to the outside.

.. image:: /Images/Kits/weather_station_construction_back_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_back_1200.jpg

In the next step we attach the Ambient Light Bricklet to the top side
of the case. To make sure that it picks up as little light as possible
from the LCD backlight, we screw it directly to the top side of the case.
It is screwed to the inside with the sensor facing to the outside
through the case. We use a nut at the bottom and a nut as well as washer at
the top to get the correct height. The long 12mm screws are screwed in from
the top. 

If everything went as expected, the screws should be flush at the
bottom and the Bricklet connector should have about 1mm space to the top.
This way it is still easy to connect the Bricklet cable, and the sensor is
at a good position to give useful measurements.

.. image:: /Images/Kits/weather_station_construction_top_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_1200.jpg

Humidity and Barometer Bricklet will be attached to the front side of the case.
We screw them to the inside with the sensors facing to the outside. For that
we use the 10mm spacers and screws from the inside as well as the outside.

This way there is enough space between the sensors and the case 
to again allow good measurements. If you intend
to attach something big on the bottom side, you can attach the Humidity and
Barometer Bricklets the same way as the Ambient Light Bricklet to save space.

At this point you should already attach the Bricklet cables, otherwise it will 
become fiddly after the LCD Bricklet is inserted.

.. image:: /Images/Kits/weather_station_construction_front1_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 3
   :align: center
   :target: ../../_images/Kits/weather_station_construction_front1_1200.jpg

Now we mount the LCD 20x4 Bricklet to the case. It is probably easiest to
start by screwing the 10mm spacer to the black Bricklet board from the bottom. 
After that we put the LCD on it and add a nut and washer between 
the case and the LCD circuit board, to get a
nice distance between the board and the case. The whole thing is then screwed
together from the top with the long 12mm screws.

In this instruction we route the Bricklet cables below the LCD 20x4 Bricklet,
but it is also possible to route them between the two circuit boards of the
LCD 20x4 Bricklet to hide them a little bit more.

.. image:: /Images/Kits/weather_station_construction_front2_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 4
   :align: center
   :target: ../../_images/Kits/weather_station_construction_front2_1200.jpg

We start putting the parts of the case together by attaching the
top side to the back side. We can then also attach the Bricklet cable
between the Master Brick and the Ambient Light Bricklet.

.. image:: /Images/Kits/weather_station_construction_top_to_back_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 5
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_to_back_1200.jpg

After that we attach all of the other side parts as well as the big spacers
that hold everything together. The big spacers should have a height of 40mm
and threads on both sides trough front- and backside.
We achieve this by screwing two 9mm, one 12mm and one 10mm spacer together.
This long spacer is then attached to the inside of the back side by a screw
from the outside of the back side.

.. image:: /Images/Kits/weather_station_construction_top_back_spacer_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 6
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_back_spacer_1200.jpg

Now only the Bricklet cables of the three other Bricklets have to be connected.
We can do this while the back and the front part are lying side by side.

.. image:: /Images/Kits/weather_station_construction_cabling_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 7
   :align: center
   :target: ../../_images/Kits/weather_station_construction_cabling_1200.jpg

After that we just have to put the front side on the back side and add the four
missing screws. That's it, we are done!

.. image:: /Images/Kits/weather_station_construction_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 8
   :align: center
   :target: ../../_images/Kits/weather_station_construction_1200.jpg

.. _starter_kit_weather_station_construction_wifi:

Wi-Fi Weather Station
^^^^^^^^^^^^^^^^^^^^^

The Weather Station case is big enough to add a :ref:`WIFI Extension
<wifi_extension>` for wireless controlling. In this tutorial we will use
the :ref:`Step-Down Power Supply <step_down_power_supply>` together with
a :ref:`DC Jack Adapter <dc_jack_adapter>` to power the stack. It would also
be possible to power the stack with a USB Power Supply, in this case
Step-Down Power Supply and DC Jack Adapter are not needed.

We will start by mounting a stack consisting of Step-Down Power Supply,
Master Brick and WIFI Extension to the back side of the case. There is a 
slot in the case where solder bumps of the Step-Down Power Supply are,
so it is possible to mount the Step-Down Power Supply directly flush
to the case.

.. image:: /Images/Kits/weather_station_construction_wifi_stack_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_stack_1200.jpg

The DC Jack Adapter can be mounted to the back side of the case with a single
21mm long spacer. The 21mm long spacer can be constructed out of one 9mm spacer
and one 12mm spacer. It is screwed to the case on the bottom with a screw and
to the DC Jack Adapter with a nut.

If it is mounted correctly, the DC Jack Adapter should fit in the side part
of the case.

.. image:: /Images/Kits/weather_station_construction_wifi_dc_jack_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_dc_jack_1200.jpg

That's it! We can now again mount the front of the case to the back. If you
use an antenna from the Tinkerforge shop, you need to either use the large
or the external antenna. The small antenna does not fit.

.. image:: /Images/Kits/weather_station_construction_wifi_ready_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 3
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_ready_1200.jpg


Raspberry Pi Weather Station
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to control the Weather Station with an embedded board like
the Raspberry Pi. You can put the Raspberry Pi in the case, despite
it is a bit tricky to get everything in the case.

We will put a :ref:`Master Brick <master_brick>`, 
a :ref:`Step-Down Power Supply <step_down_power_supply>`, a :ref:`DC Jack
Adapter <dc_jack_adapter>` and 
the Rapsberry Pi in the case. The Raspberry Pi (and the Master Brick) will 
be powered over the DC Jack Adapter by the Step-Down Power Supply.

How to mount the DC Jack Adapter in the case can be seen above 
(:ref:`starter_kit_weather_station_construction_wifi`).

The Step-Down Power Supply (with Master Brick on top) is mounted on 10mm 
spacers. We can put the SD card below the Step-Down Power Supply,
the Micro USB connector goes left from the Step-Down Power Supply
spacers. There are slots in the back side of the case that can be used
to hold the Raspberry Pi with cable ties.

The green 5V output of the Step-Down Power Supply is connected to the Micro
USB input of the Raspberry Pi to power it. The black connector of the
Step-Down Power Supply is connected to the DC Jack Adapter and
the Mini USB connector of the Master Brick is connected to the USB connector
of the Raspberry Pi by a small Mini USB cable.

.. image:: /Images/Kits/weather_station_construction_rpi_front_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Weather Station construction step 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_front_1200.jpg

From the back side we can see how the Raspberry Pi fits in. 

.. image:: /Images/Kits/weather_station_construction_rpi_back_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_back_1200.jpg

The way the
Raspberry Pi is mounted in the images allows to easily connect an Ethernet
cable to the Raspberry Pi. You can also mount the Raspberry Pi the other
way around (turned 180°). Then you can use a smaller Mini USB cable, but
the Ethernet port is obstructed. 

Another possible mounting option is to put the Raspberry Pi on the outside of 
the back side of the case.

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

.. FIXME: Regenmesser, windgeschwindigkeit etc
