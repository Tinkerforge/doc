
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Blinkenlights
:shoplink: ../../../shop/kits/starter-kit-blinkenlights.html


.. _starter_kit_blinkenlights:

Starter Kit: Blinkenlights
==========================

.. note::
 This Starter Kit is currently in the prototype state and the software/hardware
 as well as the documentation is incomplete and may not represent the final
 version.

TODO: Images

Features
--------

* Giant 40x80cm 200 Pixel RGB Display with update rate up to 100Hz
* Develop Party Games, Exhibition Presentations and Customer Specific Displays 
  of any kind
* Freely programmable, configurable and expandable
* Pixels: 12mm diameter, waterproof (IP65), full-color RGB  with 1600mcd


Description
-----------

The Starter Kit: Blinkenlights is a huge, freely programmable display.
It consist of 200 independently controllable full-color RGB LED pixels that can
be changed up to 100 times per second. Possible applications are vast. The
kit can be used to create party games, exhibition presentations, fancy mood
lighting and custom displays of any kind.

The basic kit comes with one :ref:`Master Brick <master_brick>`, one :ref:`LED Strip
Bricklet <led_strip_bricklet>`, four 50 LED Pixel sets, two LED power supplies,
one mounting plate, one back plate and all necessary cables and mounting
materials. The basic kit can be controlled over USB by any (Embedded-) PC (e.g.
:ref:`Raspberry Pi <embedded_raspberry_pi>`), laptop, server or tablet.

The kit can be extended by other Tinkerforge products. 
In game applications the :ref:`Multi Touch Bricklet <multi_touch_bricklet>`
can be useful when custom game controls are needed. With 
:ref:`Master Brick Extensions <product_overview_master_extensions>` the USB 
interface can be changed to :ref:`WiFi <wifi_extension>` or 
:ref:`Ethernet <ethernet_extension>` so smart phone or tablet
controlled applications are imaginable. A larger display can be created by 
attaching more LED Pixels to it.

A demo application implements clones of
`Tetris <http://en.wikipedia.org/wiki/Tetris>`__ and 
`Pong <http://en.wikipedia.org/wiki/Pong>`__ and demonstrates different non game 
applications. For example it can scroll customizable text in different colors on 
the display, shows rainbows, shows customizable image sets with 
configurable durations and can warm your heart with a virtual fire.
The games can be controlled by a PC keyboard but can be also be controlled
by customizable touch pads when using the Multi Touch Bricklet.

The kit name "Blinkenlights" comes from the
`Project Blinkenlights <http://en.wikipedia.org/wiki/Project_Blinkenlights>`__.

Technical Specifications
------------------------

========================================  ============================================================
Property                                  Value
========================================  ============================================================
Maximum Update Rate (LED Strip Bricklet)  100Hz
RGB resolution (LED Strip Bricklet)       3 x 8Bit
Luminous Itensity                         1600cd
----------------------------------------  ------------------------------------------------------------
----------------------------------------  ------------------------------------------------------------
Number of RGB Pixels                      10 x 20
Dimensions (W x D x H)                    40 x 80 x TODO cm
Weight                                    TODO
========================================  ============================================================

.. _starter_kit_blinkenlights_resources:

Resources
---------

* Example source code :ref:`Tetris <starter_kit_blinkenlights_tetris>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games>`__)
* Example source code :ref:`Pong <starter_kit_blinkenlights_Pong>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games>`__)
* Example source code :ref:`Fire <starter_kit_blinkenlights_fire>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/fire>`__)
* Demo application :ref:`Starter Kit: Blinkenlights Demo <starter_kit_blinkenlights_demo_examples>` (Download: Windows, Linux, Mac OS X)




Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect all Bricklets to the Master 
Brick and connect it via USB to your PC. Afterwards use Brick Viewer to check
if all of the firmwares up to date (Updates / Flashing button). If not, you can
:ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer, too:

TODO: Image of Blinkenlights Bricks/Bricklets:

.. .. image:: /Images/Kits/blinkenlights_update_350.jpg
   :scale: 100 %
   :alt: Blinkenlights update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/blinkenlights_update_orig.jpg

As next step click through the tabs of the Brick Viewer
to see if all of the sensors are working correctly. Now you can be sure that 
the Bricks and Bricklets have versions that work together and that
everything will work if it is screwed together. 


Construction
------------

TODO

* Construction of standard kit
* Help for front plate extension


.. _starter_kit_blinkenlights_demo_examples:

Demo Application/ Example Projects
----------------------------------

TODO Screenshot

The demo application should demonstrate possible applications for this kit. It 
consists of five individual applications each also provided as single project 
(see below). Each projects is represented by its own tab and will be 
started by selecting the corresponding tab. The application supports the
additional usage of two Dual Button Bricklets or one Multi Touch Bricklet
to control the games. If a Piezo Speaker Bricklet and or Segment Display 4x7 
Bricklet is connected, these Bricklets will also be used by the games to give
acoustic feedback or to display the score.

Before starting you have to configure the host and port. If you use the standard
kit and have connected it directly to your PC via USB "localhost" and "4223" is 
fine. If you extended the kit by :ref:`Extensions <master_brick_extension>` or 
want to control the kit from another PC you have to enter the IP or hostname
of the extension or the PC where the kit is connected to. Below the 
input boxes is a table which shows you the connected Bricks and 
Bricklets. 


.. _starter_kit_blinkenlights_tetris:

Tetris
^^^^^^

TODO:

* Picture of Tetris 
* With/Without frontpanel?
* Example Image

The demo application implements a typical Tetris games with all defined
specialities. Tetris can be controlled by three possible ways. At first there 
are buttons in the tab which can be used to control the game. Next you can use 
your Keyboard. The keys are defined in the tab (e.g. "a" is left). Finally a 
connected Multi Touch Bricklet with attached electrodes can be used (e.g. 
electrode 0 is left).


.. _starter_kit_blinkenlights_pong:

Pong
^^^^

* Link to github, description how to configure/start
* Picture of Pong
* With/Without frontpanel?
* Example Image

Like :ref:`Tetris <starter_kit_blinkenlights_tetris>` the game can be controlled
by buttons, keyboard or a Multi Touch Bricklet. Additionally it can be 
controlled by two Dual Button Bricklets.


.. _starter_kit_blinkenlights_fire:

Fire Simulation
^^^^^^^^^^^^^^^

TODO:

* Distance to front panel
* Example Image

When selecting the Fire tab you will see a fire simulation. It looks good
if you place the front panel in a distance of TODO to the back panel.
The simulation is based on a particle system and can be configured by four 
sliders:

* Speed
  
  Defines the frame duration in milliseconds. After the duration time is 
  exceeded a new frame will be computed. So if you decrease the frame duration
  you will see a faster burning fire.

* Hue

  Defines the color of your fire.

* Start

  Defines the starting point where the fire particles will start to rise.

* End

  Defines the end point where the fire particles will extinguish.

Play with the sliders to configure your personal fire! With the "Default" button
you will set back all sliders to their defaults.


.. _starter_kit_blinkenlights_scrolling_text:

Scrolling Text
^^^^^^^^^^^^^^

TODO:

* Frontpanel?
* Example Image

The "Scrolling Text" demo will scroll the entered Text with the given speed
on the display. You can set changing colors by selecting "Rainbow" or select
"Color" and pick the color you like py pressing the button.


.. _starter_kit_blinkenlights_images:

Display Images
^^^^^^^^^^^^^^

TODO:

* Frontpanel? Distance?
* Example Image

The "Image" demo can be used to display user specific images and whole 
animations. 


Choose the images you want to display by pressing "Choose images...". The 
application will display each image for the given time ("Speed") and then switch
to the next image. This way you can create animations. Each image is resized to
20x10 pixels (size of the display) and stretched if the aspect ration does not 
fit. Use an image editing tool if you are not satisfied with the results.


Further Enhancements
--------------------

If you modded, extended or improved your Blinkenlights installation in any way and you
have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!
