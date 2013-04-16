
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / Starter Kit: Weather Station

.. include:: WeatherStation.substitutions

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
bindings (|bindings|). Examples implementations for each language will
let you easily introduce in the programming.

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

TODO: Construction introduction: Different extension stages etc blabla

Basic Weather Station
^^^^^^^^^^^^^^^^^^^^^

The basic Weather Station Kit comes with Ambient Light, Barometer, 
Humidity and LCD 20x4 Bricklet, Master Brick, the Weather Station
case including a replacement side element for a DC Jack adapter,
Bricklet cables and USB cable as well as lots of screws, spacers,
nuts and washers.

.. image:: /Images/Kits/weather_station_content_350.jpg
   :scale: 100 %
   :alt: Weather Station content
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

If everything went as expected, the screws should be flsuh at the
bottom and the Bricklet connector should have about 1mm space to the top.
This way it is still easy to connect the Bricklet cable, and the sensor is
at a good position to give usefull measurements.

.. image:: /Images/Kits/weather_station_construction_top_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_top_1200.jpg

Humidity and Barometer Bricklet are attached to the front side of the case.
We screw them to the inside with the sensors facing to the outside. For that
we use the 10mm spacers and screws from the inside as well as the outside.

This way Weather Station case is open enough and there is enough space 
between the sensors and the case to again allow good measurements. If you intend
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
start by screwing the 10mm spacer to the Bricklet from the bottom. After that
we add a nut and washer between the case and the LCD circout board, to get a
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
and threads on both sides.

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
missing screws. Thats it, we are done!

.. image:: /Images/Kits/weather_station_construction_350.jpg
   :scale: 100 %
   :alt: Basic Weather Station construction step 8
   :align: center
   :target: ../../_images/Kits/weather_station_construction_1200.jpg


Wi-Fi Weather Station
^^^^^^^^^^^^^^^^^^^^^

.. image:: /Images/Kits/weather_station_construction_wifi_stack_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_stack_1200.jpg

.. image:: /Images/Kits/weather_station_construction_wifi_dc_jack_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_dc_jack_1200.jpg

.. image:: /Images/Kits/weather_station_construction_wifi_ready_350.jpg
   :scale: 100 %
   :alt: Wi-Fi Weather Station construction step 3
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_ready_1200.jpg


Raspberry Pi Weather Station
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

RS485, Ethernet, etc.
^^^^^^^^^^^^^^^^^^^^^

Same as Wi-Fi

Projects
--------

There are several applications for the Weather Station Starter Kit:

Display Environment Measurements on LCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most obvious application for the Weather Station Starter Kit is to display
the measurements of the environment on the LCD 20x4 Bricklet. This can be
done through three different paths:

* USB connection to PC: Install Brickd and application on PC, connect
  Master Brick of Weather Station to PC via USB.
* Wi-Fi connection to PC: Install application on PC, connect to
  Weather Station directly over Wi-Fi or through an access point.
* Raspberry Pi or other embedded board integrated in Weather Station:
  Install Brickd and application on embedded board, connect Master Brick of
  Weather Station to embedded board via USB.

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
