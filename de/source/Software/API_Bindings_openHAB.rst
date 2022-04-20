
.. _api_bindings_openhab:

openHAB - API Bindings
======================

.. note::
 Die openHAB-Dokumentation ist nur auf Englisch verfügbar.

.. warning::
 The openHAB bindings are still in beta, but the development was stopped.

The openHAB bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your openHAB installation. The
`ZIP file <https://www.tinkerunity.org/topic/4901-betaversion-der-openhab-bindings/>`__ for the bindings contains:

* ``org.openhab.binding.tinkerforge-[version].jar``, a precompiled version of the bindings
* in ``org.openhab.binding.tinkerforge/`` the source code of the bindings
* in ``examples/`` example DSL rules for some Bricks and Bricklets
* ``tinkerforge-2.1.26.jar``, the currently required version of the Java bindings

Requirements
------------

* openHAB 2.5.0 or newer, openHAB 3 is currently not supported. openHAB 3 support will be added in the future.


.. _api_bindings_openhab_install:

Installation
------------

.. note::
 Currently the bindings also require installation of the Java bindings version 2.1.26 or higher.
 They are available in in the zip file or alternatively in the
 `Central Maven Repository <https://search.maven.org/search?q=a:tinkerforge>`__.
 Put the jar into the addons directory, next to the openHAB bindings jar.

To install the bindings, just copy the JAR into the addons directory
of your installation. openHAB will then load the bindings.

Usage
-----

To control Tinkerforge hardware with the openHAB bindings, :ref:`Brick Daemon <brickd>` has
to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the bindings. You can then connect the bindings
by adding a Brick Daemon thing in openHAB's Paper UI.

Attached devices are automatically put into the inbox after adding the
Brick Daemon thing.

Devices and channels can be configured: Channels typically allow changing
the update rate. The configuration of some things can show or hide channels, for
example the IO-4/16 pin configuration will dynamically create input or
output channels. Sometimes PaperUI needs to be refreshed by pressing F5
to show new channels.

Changing device configuration is only supported, if it is stored in the RAM of the device.
Persistent configuration has to be set externally (e.g. by using Brick Viewer),
because openHAB will often reconfigure devices, for example on startup or when
reconnected to a Brick Daemon. Writing persistent configuration every time would use up
too many write-cycles.

Actions
^^^^^^^

There are actions available for each thing. To use
actions of a thing in a rule, first the actions have to be loaded with:
``var devActions = getActions("tinkerforge", "tinkerforge:[devicetype]:[Device UID]")``
Then they can be used with ``devActions.[actionname]([parameters])``.
The following example shows how to show a GUI on an LCD 128x64 Bricklet
with the UID "HQ6":

.. code-block:: none

    rule "GUI example"
    when
        System started
    then
        var lcdActions = getActions("tinkerforge", "tinkerforge:brickletlcd128x64:HQ6")
        lcdActions.brickletLCD128x64ClearDisplay()
        lcdActions.brickletLCD128x64RemoveAllGUI();
        lcdActions.brickletLCD128x64SetGUIButton(0, 0, 0, 60, 20, "button");
        lcdActions.brickletLCD128x64SetGUISlider(0, 0, 30, 60, 0, 50);
        lcdActions.brickletLCD128x64SetGUIGraphConfiguration(0, 1, 62, 0, 60, 52, "X", "Y");
        lcdActions.brickletLCD128x64SetGUIGraphData(0, newArrayList(0, 10, 20, 40, 20, 15));
        lcdActions.brickletLCD128x64SetGUITabConfiguration(3, false);
        lcdActions.brickletLCD128x64SetGUITabText(0, "Tab A");
        lcdActions.brickletLCD128x64SetGUITabText(1, "Tab B");
    end

The parameters and return values typically correspond to those of the respective
function in the Java Bindings.
Functions that expect arrays as parameters can also
be called with lists, as shown in the call of setGUIGraphData in the example.
Results are returned as a Map<String, Object>, that can be used as follows:

.. code-block:: none

    rule "invert image"
    when
        Item Enx_Button changed to OFF
    then
        val lcdActions = getActions("tinkerforge", "tinkerforge:brickletlcd128x64:HQ6")
        pixels = lcdActions.brickletLCD128x64ReadPixels(0, 0, 127, 63).get("pixels")
        val inverted = pixels.map[p | !p]
        lcdActions.brickletLCD128x64WritePixels(0, 0, 127, 63, inverted)        
    end

This rule is triggered if the Item Enx_Button changes to OFF (i.e. if the
corresponding RGB LED Button is released). It will then read the pixels
currently shown on the LCD Bricklet, invert them and draw the inverted
pixels back on the LCD.

Nearly the complete API of devices can be used as actions. Functions that
change the state of a channel will refresh it automatically. Alternatively
you can use items associated to the channels with .sendCommand to change those.
Not supported are operations, that would write EEPROM or Flash Storage, to
avoid unnecessary write-cycles.

API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_openHAB_links.table

.. toctree::
   :hidden:

   Bricks <Bricks_openHAB>
   Bricks (Discontinued) <Bricks_openHAB_Discontinued>
   Bricklets <Bricklets_openHAB>
   Bricklets (Discontinued) <Bricklets_openHAB_Discontinued>
