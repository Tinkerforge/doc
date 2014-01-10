
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

The *Starter Kit: Blinkenlights* is a huge, freely programmable display.
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
by customizable touch pads when using the Multi Touch Bricklet.

The kit name "Blinkenlights" is used in
`hacker jargon <http://en.wikipedia.org/wiki/Blinkenlights>`__
to describe blinking lights. It is also known from the
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

* Example Source Code for :ref:`Tetris <starter_kit_blinkenlights_tetris>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games>`__)
* Example Source Code for :ref:`Pong <starter_kit_blinkenlights_Pong>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/games>`__)
* Example source Code for :ref:`Fire <starter_kit_blinkenlights_fire>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/fire>`__)
* Example Source Code for :ref:`Scrolling Text <starter_kit_blinkenlights_scrolling_text>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/text>`__)
* Example Source Code for :ref:`Display Images <starter_kit_blinkenlights_images>` (Download: `Python <https://github.com/Tinkerforge/blinkenlights/tree/master/images>`__)
* :ref:`Demo Application <starter_kit_blinkenlights_demo_examples>` (Download: Windows, Linux, Mac OS X, `Source Code <https://github.com/Tinkerforge/blinkenlights/tree/master/demo>`__)


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

Demo Application and Example Projects
-------------------------------------

TODO Screenshot

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

TODO:

* Picture of Tetris
* With/Without frontpanel?
* Example Image

The demo application implements a typical
`Tetris <http://en.wikipedia.org/wiki/Tetris>`__ game with all specialities.
This Tetris clone can be controlled by three possible ways. Firstly, there
are buttons in the tab which can be used to control the game. Next you can use
your keyboard. The keys are defined in the tab (e.g. "a" is left). Finally a
connected Multi Touch Bricklet with attached electrodes can be used (e.g.
electrode 0 is left).

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

TODO:

* Picture of Pong
* With/Without frontpanel?
* Example Image

Like :ref:`Tetris <starter_kit_blinkenlights_tetris>` the
`Pong <http://en.wikipedia.org/wiki/Pong>`__ game can be controlled
by buttons, keyboard or a Multi Touch Bricklet. Additionally it can be
controlled by two Dual Button Bricklets.

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

TODO:

* Distance to front panel
* Example Image

When selecting the Fire tab you will see a fire simulation. It looks good
if you place the front panel in a distance of TODO to the back panel.
The simulation is based on a particle system and can be configured by four
sliders:

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

TODO:

* Frontpanel?
* Example Image

The "Text" demo will scroll the entered text with the given frame rate
on the display. The text moved one column per frame. A higher frame rate results
in faster moving text. You can set changing colors by selecting "Rainbow" or
select "Color" and pick the color you like by pressing the button.

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

TODO:

* Frontpanel? Distance?
* Example Image

The "Images" demo can be used to display user specific images and whole
animations.

Choose the images you want to display by pressing "Choose images...". The
application will display the images with the given frame rate and switch to the
next image in the sequence each frame. This way you can create animations.
Each image is resized to 20x10 pixel (size of the display) and stretched if the
aspect ration does not  fit. Use an image editing tool if you are not satisfied
with the results.

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

Rainbow
^^^^^^^

TODO:

* Frontpanel?
* Example Image

The "Rainbow" demo will display a moving rainbow with the given frame rate
and speed. A higher frame rate and speed results in faster moving rainbow.

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
