
.. _starter_kit_weather_station_openhab_red_brick:

Smart Home Integration using openHAB and RED Brick
==================================================

For this project we are assuming, that you have build a
:ref:`RED Brick Weather Station <starter_kit_weather_station_construction_red_brick>`,
that your RED Brick is using at least Image version 1.6 and that you have
at least Brick Viewer 2.2.3 installed.

The openHAB configuration used in this project is based on an example created
by an openHAB developer. The original example is available on
`GitHub <https://github.com/theoweiss/tinkerforge-RED-Brick>`__.

Goals
-----

We are setting the following goals for this project:

* Temperature, ambient light, humidity and air pressure should be shown on
  the LCD 20x4 Bricklet,
* the measured values should be updated automatically when they change and
* button 0 on the LCD 20x4 Bricklet should toggle the backlight of the display.

Additionally, if the RED Brick has network connectivity:

* Temperature, ambient light, humidity and air pressure should be shown on
  openHAB sitemap in the RED Brick web interface.

In the following we will show step-by-step how openHAB has to be configured to
achieve this.

Step 1: Enable openHAB service
------------------------------

The `openHAB <https://www.openhab.org/>`__ service is disabled by default on the
RED Brick because it takes quite some time to start and slows down the boot
process. Before we can configure openHAB we have to enable it first. The
:ref:`RED Brick services documentation <red_brick_brickv_settings_services>`
explains how to do this..

Step 2: Define Bricklet items
-----------------------------

Bricks and Bricklets are represented in openHAB as
`items <https://github.com/openhab/openhab/wiki/Explanation-of-items>`__. Such
items are defined in ``.items`` config files stored on the RED Brick.
Brick Viewer allows to edit these files. See the
:ref:`RED Brick openHAB documentation <red_brick_brickv_settings_openhab>`
for details.

1. Open the openHAB settings tab in Brick Viewer and click the *New* button.
2. Enter ``weather-station.items`` as name and click the *Create* button.
3. Copy and paste the ``.items`` template from below into the empty text field.
4. Replace the UID placeholders (e.g. ``<HUMIDITY_UID>``) with the corresponding
   UIDs of your Bricklets.
5. Click the *Apply Changes* button to save the file.

This is the ``.items`` template
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.items>`__)
used in step 3:

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.items
 :tab-width: 4

Step 3: Define rules
--------------------

`Rules <https://github.com/openhab/openhab/wiki/Rules>`__ allow to connect
events to actions in an when-then fashion. We use this rules to update the
currently measured values on the LCD 20x4 Bricklet when they change.

Create a new config file (as described in step 1) named
``weather-station.rules`` and copy and paste following rules
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.rules>`__)
into it:

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.rules
 :tab-width: 4

* The "Weather Station LCD Init From Backlight" rule writes the static part of
  the text to the display and turns the LCD backlight on.
* The "Weather Station LCD Update \*" rules update the displayed values when
  they change.
* The "Weather Station LCD Backlight" rule toggles the LCD backlight when
  button 0 is pressed.

Step 4: Define the sitemap
--------------------------

A `sitemap <https://github.com/openhab/openhab/wiki/Explanation-of-Sitemaps>`__
defines the elements of the openHAB user interface. We use it to display the
measured values in the :ref:`RED Brick web interface <red_brick_web_interface>`.

Create a new config file (as described in step 1) named
``weather-station.sitemap`` and copy and paste following sitemap definition
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.sitemap>`__)
into it:

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.sitemap
 :tab-width: 4

Now this sitemap's web interface is available at::

 http://<RED_BRICK_IP_ADDRESS>:8080/openhab.app?sitemap=weather-station

.. image:: /Images/Kits/weather_station_openhab_orig.jpg
   :scale: 100 %
   :alt: openHAB example sitemap
   :align: center
   :target: ../../_images/Kits/weather_station_openhab_orig.jpg

You can also go to the main RED Brick web interface where all available sitemaps
are listed::

 http://<RED_BRICK_IP_ADDRESS>
