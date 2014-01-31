
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Blinkenlights
:shoplink: ../../../shop/kits/starter-kit-blinkenlights.html


.. _starter_kit_blinkenlights:

Starter Kit: Blinkenlights
==========================

.. note::
 This Starter Kit is currently in the prototype state and the software/hardware
 as well as the documentation is incomplete and may not represent the final
 version.

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/kit_blinkenlights_fire_350.jpg",
	               "Kits/kit_blinkenlights_fire_600.jpg",
	               "Blinkenlights: Fire Simulation")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_fire_daylight_100.jpg",
	             "Kits/kit_blinkenlights_fire_daylight_600.jpg",
	             "Blinkenlights: Fire Simulation in Daylight")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_on_wall_100.jpg",
	             "Kits/kit_blinkenlights_on_wall_600.jpg",
	             "Blinkenlights: On Wall")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_pong_100.jpg",
	             "Kits/kit_blinkenlights_pong_600.jpg",
	             "Blinkenlights: Pong")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_pong_daylight_100.jpg",
	             "Kits/kit_blinkenlights_pong_daylight_600.jpg",
	             "Blinkenlights: Pong in Daylight")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_tetris_100.jpg",
	             "Kits/kit_blinkenlights_tetris_600.jpg",
	             "Blinkenlights: Tetris")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_text_daylight_100.jpg",
	             "Kits/kit_blinkenlights_text_daylight_600.jpg",
	             "Blinkenlights: Text Display")
	}}
	{{
	    tfdocimg("Kits/kit_blinkenlights_rainbow_near_far_dark_100.jpg",
	             "Kits/kit_blinkenlights_rainbow_near_far_dark_600.jpg",
	             "Blinkenlights: Rainbow with different Front Panel Distances")
	}}
	{{ tfdocend() }}

Features
--------

* Giant 40x80cm 200 Pixel RGB Display with update rate up to 100Hz
* Develop Party Games, Exhibition Presentations and Customer Specific Displays
  of any kind
* Freely programmable, configurable and expandable
* Pixels: 12mm diameter, waterproof (IP65), full-color RGB with 1600mcd per pixel


Description
-----------

The *Starter Kit: Blinkenlights* is a huge, freely programmable display.
It consist of 200 independently controllable full-color RGB LED pixels that can
be changed up to 100 times per second. Possible applications are vast. The
kit can be used to create party games, exhibition presentations, fancy mood
lighting and custom displays of any kind.

The basic kit comes with one :ref:`Master Brick <master_brick>`, one :ref:`LED Strip
Bricklet <led_strip_bricklet>`, four 50 LED Pixel sets, one LED power supply,
four wall mounting plates, one perforated board, one front panel and all
necessary cables and mounting materials. The basic kit can be controlled over USB 
by any (Embedded-) PC (e.g. :ref:`Raspberry Pi <embedded_raspberry_pi>`), laptop, 
server or tablet.

The kit can be extended by other Tinkerforge products.
In game applications the :ref:`Multi Touch Bricklet <multi_touch_bricklet>`
can be useful when custom game controls are needed. With
:ref:`Master Brick Extensions <product_overview_master_extensions>` the USB
interface can be changed to :ref:`Wi-Fi <wifi_extension>` or
:ref:`Ethernet <ethernet_extension>` so smart phone or tablet
controlled applications are possible. A larger display can be created by
attaching more LED Pixels to the kit.

A :ref:`demo application <starter_kit_blinkenlights_demo_examples>` implements
clones of `Tetris <http://en.wikipedia.org/wiki/Tetris>`__ and
`Pong <http://en.wikipedia.org/wiki/Pong>`__ and includes different non-game
applications. For example, it can show customizable scrolling text in
different colors on the display, it shows rainbows, customizable image sets with
configurable durations and can warm your heart with a virtual fire.
The games can be controlled by a PC keyboard but can be also be controlled
by customizable touch pads when using the Multi Touch Bricklet or by Dual Button
Bricklet.

The kit name "Blinkenlights" is used in
`hacker jargon <http://en.wikipedia.org/wiki/Blinkenlights>`__
to describe blinking lights of network equipment. It is also known from the
`Project Blinkenlights <http://en.wikipedia.org/wiki/Project_Blinkenlights>`__.

Technical Specifications
------------------------

========================================  ============================================================
Property                                  Value
========================================  ============================================================
Maximum Update Rate (LED Strip Bricklet)  100Hz (per Pixel)
RGB resolution (LED Strip Bricklet)       3 x 8bit
Luminous Intensity                        1600mcd per pixel
----------------------------------------  ------------------------------------------------------------
----------------------------------------  ------------------------------------------------------------
Number of RGB Pixels                      10 x 20
Dimensions (W x D x H)                    | 40 x 80 x 7cm (without front panel)
                                          | 50 x 90 x > 7cm* (with front panel)
Weight                                    4kg (assembled kit)
========================================  ============================================================

\* depends on configured the distance between front and back panel

.. _starter_kit_blinkenlights_resources:

Resources
---------

* Example Source Code for :ref:`Tetris <starter_kit_blinkenlights_tetris>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Example Source Code for :ref:`Pong <starter_kit_blinkenlights_Pong>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__, `C# <https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__)
* Example Source Code for :ref:`Fire <starter_kit_blinkenlights_fire>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/python>`__, `Delphi <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/delphi>`__)
* Example Source Code for :ref:`Scrolling Text <starter_kit_blinkenlights_scrolling_text>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__, `PHP <https://github.com/Tinkerforge/blinkenlights/tree/master/text/php>`__)
* Example Source Code for :ref:`Display Images <starter_kit_blinkenlights_images>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/images/python>`__, `Java <https://github.com/Tinkerforge/blinkenlights/tree/master/images/java>`__)
* :ref:`Demo Application <starter_kit_blinkenlights_demo_examples>` (Download: Windows, Linux, Mac OS X, `Source Code <https://github.com/Tinkerforge/blinkenlights/tree/master/demo>`__)


Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect the LED Strip Bricklet 
to the Master Brick and connect it via USB to your PC. Afterwards use Brick 
Viewer to check if all of the firmwares are up to date (Updates / Flashing 
button). If not, you can :ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer too:

.. image:: /Images/Kits/kit_blinkenlights_update_350.jpg
   :scale: 100 %
   :alt: Blinkenlights update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_update.jpg

As the next step test the LED Strip Bricklet and the pixels as described
:ref:`here <led_strip_bricklet_test>`. After that you can start to assemble
the kit.


Construction
------------

.. image:: /Images/Kits/kit_blinkenlights_build_step9_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 40cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step9_1200.jpg

The construction is described
:ref:`here <starter_kit_blinkenlights_construction>` in detail.

.. toctree::
   :hidden:

   Construction


.. _starter_kit_blinkenlights_demo_examples:

Demo Application and Example Projects
-------------------------------------

.. image:: /Images/Kits/blinkenlights_demo_setup_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Setup
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_setup.jpg

The demo application shows possible applications for this kit. It
consists of 6 individual applications each also provided as individual project
(see below). Each project is represented by its own tab and will be
started by selecting the corresponding tab. The application supports the
additional usage of two Dual Button Bricklets or one Multi Touch Bricklet
to control the games. If a Piezo Speaker Bricklet and/or Segment Display 4x7
Bricklet is connected, these Bricklets will also be used by the games to give
acoustic feedback or to display the score.

Before starting you have to configure the host and port. If you use the standard
kit and have connected it directly to your PC via USB "localhost" and "4223" is
fine. If you extended the kit by
:ref:`Extensions <product_overview_master_extensions>` or
want to control the kit from another PC you have to enter the IP address or
hostname of the extension or the PC where the kit is connected to. Below the
input boxes is a table which shows you the connected Bricks and Bricklets.


.. _starter_kit_blinkenlights_tetris:

Tetris
^^^^^^
The demo application implements a typical
`Tetris <http://en.wikipedia.org/wiki/Tetris>`__ game with all specialties.
It can be played with:

.. image:: /Images/Kits/kit_blinkenlights_tetris_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

or without front panel:

.. image:: /Images/Kits/kit_blinkenlights_tetris_wo_frontpanel_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris
   :align: center

This Tetris clone can be controlled by three possible ways. Firstly, there
are buttons in the tab which can be used to control the game. Next you can use
your keyboard. The keys are defined in the tab (e.g. "a" is left). Finally a
connected Multi Touch Bricklet with attached electrodes can be used (e.g.
electrode 0 is left).

.. image:: /Images/Kits/blinkenlights_demo_tetris_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Tetris
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_tetris.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__.
This also incorporates the
:ref:`Pong <starter_kit_blinkenlights_pong>` project and consists of mainly
two files: ``tetris.py`` implements the game and ``config.py`` defines the
configuration (host, port, UIDs, LED matrix layout and keymaps).

Modify ``config.py`` according to your needs and run the application:

.. code-block:: python

   python tetris.py

There is also a :ref:`C# <api_bindings_csharp>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__.


.. _starter_kit_blinkenlights_pong:

Pong
^^^^

Like :ref:`Tetris <starter_kit_blinkenlights_tetris>` the
`Pong <http://en.wikipedia.org/wiki/Pong>`__ can be used with or without front 
panel.

The following images show pong with darkness and daylight.

.. image:: /Images/Kits/kit_blinkenlights_pong_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Pong
   :align: center


.. image:: /Images/Kits/kit_blinkenlights_pong_daylight_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Pong in Daylight
   :align: center

The game can be controlled
by buttons, keyboard or a Multi Touch Bricklet. Additionally it can be
controlled by two Dual Button Bricklets.

.. image:: /Images/Kits/blinkenlights_demo_pong_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Pong
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_pong.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/games/python>`__.
This also incorporates the
:ref:`Tetris <starter_kit_blinkenlights_tetris>` project and consists of mainly
two files: ``pong.py`` implements the game and ``config.py`` defines the
configuration (host, port, UIDs, LED matrix layout and keymaps).

Modify the ``config.py`` according to your needs and run the application:

.. code-block:: python

   python pong.py

There is also a :ref:`C# <api_bindings_csharp>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/games/csharp>`__.


.. _starter_kit_blinkenlights_fire:

Fire Simulation
^^^^^^^^^^^^^^^

When selecting the Fire tab you will see a fire simulation. It looks good
if you place the front panel in a distance of 42mm (2x9mm and 2x12mm standoff)
to the back panel. 

The following images show the fire simulation during darkness and daylight.

.. image:: /Images/Kits/kit_blinkenlights_fire_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Fire Demo
   :align: center


.. image:: /Images/Kits/kit_blinkenlights_fire_daylight_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Fire Demo in Daylight
   :align: center


The simulation is based on a particle system and can be 
configured by four sliders:

* **Frame Rate**:
  Defines the frame rate in Hz. The simulation is updated for each new frame.
  If you increase the frame rate you will see a faster burning fire.

* **Hue**:
  Defines the color of your fire.

* **Start**:
  Defines the starting point where the fire particles will start to rise.

* **End**:
  Defines the end point where the fire particles will extinguish.

Play with the sliders to configure your personal fire! With the "Default" button
you will set back all sliders to their default values.

.. image:: /Images/Kits/blinkenlights_demo_fire_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Fire
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_fire_1200.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/fire/python>`__.
It consists of mainly two files: ``fire.py`` implements the simulation and
``config.py`` defines the configuration (host, port, UID, LED matrix layout and
simulation parameters).

Modify the ``config.py`` according to your needs and run the application:

.. code-block:: python

   python fire.py

There is also a :ref:`Delphi <api_bindings_delphi>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/fire/delphi>`__.


.. _starter_kit_blinkenlights_scrolling_text:

Scrolling Text
^^^^^^^^^^^^^^

The "Text" demo will scroll the entered text with the given frame rate
on the display. 

.. image:: /Images/Kits/kit_blinkenlights_text_daylight_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Text Demo
   :align: center

The text moves one column per frame. A higher frame rate results
in faster moving text. You can set changing colors by selecting "Rainbow" or
select "Color" and pick the color you like by pressing the button.

.. image:: /Images/Kits/blinkenlights_demo_text_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Text
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_text.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/text/python>`__.
It consists of mainly two files: ``text.py`` implements the logic and
``config.py`` defines the configuration (host, port, UID, LED matrix layout and
color parameters).

Modify the ``config.py`` according to your needs and run the application with
some text to display:

.. code-block:: python

   python text.py Starter Kit: Blinkenlights

There is also a :ref:`PHP <api_bindings_php>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/text/php>`__.


.. _starter_kit_blinkenlights_images:

Display Images
^^^^^^^^^^^^^^

The "Images" demo can be used to display user specific images and whole
animations.

The following image

.. image:: /Images/Kits/kit_blinkenlights_heart_input.png
   :scale: 100 %
   :alt: Blinkenlights Heart Input
   :align: center

generates the following output

.. image:: /Images/Kits/kit_blinkenlights_heart_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Heart
   :align: center

Choose the images you want to display by pressing "Choose Images...". The
application will display the images with the given frame rate and switch to the
next image in the sequence each frame. This way you can create animations.
Each image is resized to 20x10 pixel (size of the display) and stretched if the
aspect ration does not  fit. Use an image editing tool if you are not satisfied
with the results.

.. image:: /Images/Kits/blinkenlights_demo_images_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Images
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_images.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/images/python>`__.
It consists of mainly two files: ``images.py`` implements the logic and
``config.py`` defines the configuration (host, port, UID, LED matrix layout).

Modify the ``config.py`` according to your needs and run the application with
some image files to display:

.. code-block:: python

   python text.py image1.jpg image2.jpg

There is also a :ref:`Java <api_bindings_java>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/text/java>`__.


.. _starter_kit_blinkenlights_scrolling_rainbow:

Moving Rainbow
^^^^^^^^^^^^^^

The "Rainbow" demo will display a moving rainbow with the given frame rate
and speed. The results depend on the distance to the front panel. 

The following image shows the rainbow demo with 12mm distance in daylight, 
42mm distance in daylight and with 42mm distance during darkness.

.. image:: /Images/Kits/kit_blinkenlights_rainbow_near_far_dark_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Rainbow Demo
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_rainbow_near_far_dark_1200.jpg

A higher frame rate and speed results in faster moving rainbow.

.. image:: /Images/Kits/blinkenlights_demo_rainbow_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Rainbow
   :align: center
   :target: ../../_images/Kits/blinkenlights_demo_rainbow.jpg

The standalone :ref:`Python <api_bindings_python>` project can be downloaded from
`GitHub <https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/python>`__.
It consists of mainly two files: ``rainbow.py`` implements the logic and
``config.py`` defines the configuration (host, port, UID, LED matrix layout and
speed parameter).

Modify the ``config.py`` according to your needs and run the application:

.. code-block:: python

   python rainbow.py

There is also a :ref:`C <api_bindings_c>` implementation that can be
downloaded from `GitHub
<https://github.com/Tinkerforge/blinkenlights/tree/master/rainbow/c>`__.


Further Enhancements
--------------------

If you modded, extended or improved your Blinkenlights installation in any way and you
have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!
