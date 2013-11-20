
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

The Starter Kit: Blinkenlights implements (besser: realize?) a giant, 
freely programmable display. It consits of 200 independently controllable, 
full-color, 12mm diameter, waterproof (IP65) RGB color pixels updatable up to 
100 times per second. Possible applications depend on your creativity: The 
kit is useable to create party games, exhibition presentations and custom 
displays of any kind.

TODO Video

Basic kit comes with one :ref:`Master Brick <master_brick>`, one :ref:`LED Strip
Bricklet <led_strip_bricklet>`, four 50 LED Pixels sets, two led power supplies, 
one mounting plate, one back plate and all necessary cables and mouting 
materials. The basic kit can be controlled over USB by any (Embedded-) PC (e.g.
:ref:`Raspberry Pi <embedded_raspberry_pi>`), Laptop, Server or Tablet.

The kit can be extended by other Tinkerforge products. 
In game applications the :ref:`Multi Touch Bricklet <multi_touch_bricklet>`
can be useful when custom game controls are needed. With 
:ref:`Master Brick Extensions <product_overview_master_extensions>` the USB 
interface can be changed to :ref:`WiFi <wifi_extension>` or 
:ref:`Ethernet <ethernet_extension>` so Smartphone or Tablet
controlled applications are imaginable. A larger display can be created by 
attaching more LED Pixels to it.

A free application implements clones of
`Tetris <http://en.wikipedia.org/wiki/Tetris>`__ and 
`Pong <http://en.wikipedia.org/wiki/Pong>`__.
The games can be controlled by a PC keyboard but can be also be controlled
by customizable touch pads when using the Multi Touch Bricklet.

The kit name "Blinkenlights" relies on the 
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

* TODO


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


.. _starter_kit_blinkenlights_demo:

Demo Application
^^^^^^^^^^^^^^^^

TODO


Construction
------------

TODO

* Construction of standard kit
* Help for front plate extension

Projects
--------

TODO: Description of types of projects

Tetris
^^^^^^

TODO:

* Link to github, description how to configure/start
* Picture of Tetris 

Pong
^^^^

* Link to github, description how to configure/start
* Picture of Pong


Further Enhancements
--------------------

If you modded, extended or improved your Blinkenlights installation in any way and you
have published your results on our `Wiki <http://www.tinkerunity.org/wiki/>`__,
on your blog or similar: Please give us a notice. We would love to add a link
to your project here!
