
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to use the 
:ref:`RED Brick <red_brick>` with other :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` with their 
:ref:`Programming Interfaces <programming_interface>`.

A full step by step tutorial in how to use Bricks, Bricklets and Extensions can
be found in the :ref:`First steps - Tutorial <tutoprial_first_steps>`.

The RED Brick can be described as brain of the building block system.
Your program will control other Bricks and Bricklets and can be uploaded and 
executed on the RED Brick. The RED Brick itself can't control 
motors and isn't equipped with sensors, so you have to plug other modules from
the building block system to it to get the necessary features.

In this tutorial we will demonstrate the different possibilities when 
working with the RED Brick. We will use the RED Brick together
with a Master Brick and a Barometer Bricklet to measure air pressure and 
temperature. An Ethernet Extension is used to communicate with the web. We will 
use Python as programming language to program the modules. In your application 
you can of course choose other Bricks and Bricklets and another programming 
language. The concepts are the same. 

Install necessary Software
--------------------------

At first you need to :ref:`install the Brick Daemon <brickd_installation>` and 
you have to :ref:`install the Brick Viewer <brickv_installation>` software on 
your PC. Please follow the documented steps.

Test the RED Brick
------------------

TODO Image RED Brick

After you have installed the necessary software on your PC we will test the 
RED Brick. At first put a micro SD card with an 
:ref:`RED Brick software image <red_brick_images>` in the micro SD card slot
located on the bottom side of the Brick. You can buy micro SD cards
with preinstalled images in our shop. After that, connect the RED Brick with
a micro USB cable to your PC.

TODO Image RED Brick connected with micro USB cable

Start the Brick Viewer software and press **Connect**. A tab marked with 
**RED Brick** should show up. Click on it. You should see some status 
information about the state of the RED Brick. A full description of the Brick
Viewer representation of the RED Brick is documented 
:ref:`here <red_brick_brickv>`.

You have completed the test. The RED Brick is now ready to go.

Add Bricks, Bricklets and Extension
-----------------------------------

After these tests we will shut down the RED Brick. To do this click on the right 
upper corner of the RED Brick tab on **System** and choose **shut down**. Wait 
until the leds turn off. Next we will stick a Master Brick on top of the RED 
Brick and connect the Barometer Bricklet to it. On top of this stack we plug
the Ethernet Extension.

TODO Stack of RED + Master + Barometer Bricklet + Ethernet Extension

After that we reconnect the RED Brick stack to the PC, open the Brick Viewer
software and press **Connect**. Now the RED Brick tab, a Master Brick and a
Baromter Bricklet tab should come up. You can click through the tabs to test 
them.

First Program Upload
--------------------

TODO: Screenshot Barometer API

TODO: API, Example Program upload and test


Gain Internet Access
--------------------

TODO: Screenshot Brickv Screenshot

For our example we need internet access. We have already connected the Ethernet
Extension to the RED Brick, next we have to configure it.The procedure is 
described :ref:`here <red_brick_brick_settings>`. Connect it to your hub, router
or switch.


Demo Program
------------

.. literalinclude:: tutorial_red_weather.py
 :language: python
 :linenos:
 :tab-width: 4

