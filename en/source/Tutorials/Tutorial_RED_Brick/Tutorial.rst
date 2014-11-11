
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to develop software with the 
:ref:`RED Brick <red_brick>` together with :ref:`Bricks <primer_bricks>` 
and :ref:`Bricklets <primer_bricklets>`. A full step by step tutorial that
shows how to Bricks, Bricklets and Extensions are used can be found in the 
:ref:`first steps tutorial <tutorial_first_steps>`.

The RED Brick can be described as the brain of the building block system.
A program that controls Bricks and Bricklets can be uploaded to and 
executed on the RED Brick. 

In this tutorial we will demonstrate the different possibilities when 
working with the RED Brick. To keep it simple we will use a small setup
consisting of a RED Brick, a Master Brick and a Temperature Bricklet.
Later in the Tutorial will additionally add an Ethernet Extension to
get internet access.

We will show how to test a simple program that prints a temperature
on your PC and how to upload and execute it on the RED Brick after 
testing. Then we will extend the program to also show the current time,
to have a GUI (that is shown on an HDMI monitor) and to be shown as
a web interface.

If you develop your application, you might use other Bricks, Bricklets 
and programming languages, but the concepts and workflow will be the same.
	

Install necessary software
--------------------------

At first you need to :ref:`install the Brick Daemon <brickd_installation>` and 
you have to :ref:`install the Brick Viewer <brickv_installation>` software on 
your PC. Please follow the documented steps.

Test the RED Brick
------------------

TODO Image RED Brick

After you have installed the necessary software on your PC, we will test the 
RED Brick. At first put a micro SD card with an 
:ref:`RED Brick software image <red_brick_images>` in the micro SD card slot of
the Brick. It is located on the bottom side of the Brick. You can buy micro SD 
cards with preinstalled images in our shop. After that, connect the RED Brick 
with a micro USB cable to your PC.

TODO Image RED Brick connected with micro USB cable

Start the Brick Viewer software and click on **Connect**. A tab marked with 
**RED Brick** should show up. Click on it. You should see some status 
information about the state of the RED Brick. A full description of the Brick
Viewer representation of the RED Brick is documented 
:ref:`here <red_brick_brickv>`.

You have completed the test. The RED Brick is now ready to go.

Add Bricks and Bricklets
------------------------

After these tests we will add the other hardware modules to it. You should
only do this if the RED Brick is powered down. To shut it down click on 
**System** located in the right upper corner of the RED Brick tab and choose 
**shut down**. Wait until all leds turn off. After that stick a Master Brick on 
top of the RED Brick and connect a Temperature Bricklet 
Bricklet to it.

TODO Stack of RED + Master + Temperature Bricklet

After that reconnect the RED Brick stack to the PC, open the Brick Viewer
software and click on **Connect**. Now the RED Brick tab, a Master Brick and the
Temperature Bricklet will come up. You can
click through the tabs to test the connected hardware.

Run example program
-------------------

Before writing your first program you have to take a look in the API 
documentation of the used modules to see the supported functions. Each
documentation page starts with some examples. It is a good idea to run an 
example program first. We take the "Simple" example of the 
:ref:`Temperature Bricklet API documentation <temperature_bricklet_python>` and 
execute it. 

.. literalinclude:: ../Software/Bricklets/Temperature_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

To do this we download the **example_simple.py** Python program and
replace the UID in the line **UID = "XYZ"** with the UID of your Temperature 
Bricklet. You can find it in the **Setup** tab of the Brick Viewer or in the 
Temperature Bricklet tab.

Execute this program on your PC. If everything went as expected, you should see
the current temperature in the command line.

Execute the program on the RED Brick
------------------------------------

We have tested the example program and know that it is working correctly. In the
example program we wait for user input (we do this to prevent the command line on 
windows from closing immediately). On the RED Brick there won't be any user
interaction, so we will just remove the line.

`Download (example_simple_red.py) <https://github.com/Tinkerforge/doc/TODO/example_simple_red.py>`__

.. literalinclude:: example_simple_red.py
 :language: python
 :linenos:
 :tab-width: 4


Next we will execute it on the RED Brick. The procedure how to upload a program is 
generally described in the 
:ref:`RED Brick Brick Viewer description <red_brick_brickv_program>`. We will
only describe the necessary steps here:

First, open the RED Brick tab in the Brick Viewer and select the **Program** 
tab.

TODO: Screenshot Brick Viewer Program tab

The **New** button will open the **New Program** wizard. Enter "LCD Hello 
World" as name of the program, and select **Python** as language. Click on 
**Next**.

TODO: Screenshot first page of wizard

Click on **Add Files** and select the **example_simple_red.py** program. 
Click on **Next**.

TODO: Screenshot second page of wizard

In this case no changes are needed, so we can again click on **Next**.

TODO: Screenshot third page of wizard

We don't want to pass any arguments to our Python program, so we can again click
on the **Next** button.

TODO: Screenshot Arguments page

We use Pipe as Standard input and log all output (standard output and standard 
error) to a continuous log file. So no changes are required. Click on
**Next** again.

TODO: Screenshot Stdio

TODO describe schedule page
TODO: Screenshot Schedule

The summary page will summarize your configuration. Click on **Next**.
TODO: Screenshot summary

Click on the **Start Upload** Button to upload the file. After that click on
**Finish**. You should now see the text "Hello World" in the first line of your 
LCD20x4 Bricklet. 

Gain internet access
--------------------

To gain internet access we can either connect a USB WIFI/Ethernet dongle or
the Ethernet Extension. In this example we will add the Ethernet Extension:

TODO Stack of RED + Master + Temperature Bricklet + Ethernet Extension

Please shut the RED Brick down and remove the power before you add the
Extension.

The configuration of the network settings is 
:ref:`here <red_brick_brick_settings>`. 
If everything works as expected you can see a configured **tf0** 
interface in the **General** tab of the network settings after you
connected the Ethernet Extension to your network.

TODO: Screenshot Brickv Screenshot

Now that we have internet access, we can can easily do IoT and similar
applications. Another advantage of internet access is, that the RED Brick
will now automatically use NTP and thus have a correct system time.

This means that we can now add a time to each measured temperature.

`Download (example_time_red.py) <https://github.com/Tinkerforge/doc/TODO/example_time_red.py>`__

.. literalinclude:: example_time_red.py
 :language: python
 :linenos:
 :tab-width: 4

You can upload this program the same way as before


Develop a custom RED Brick GUI
------------------------------

TODO: pyqt program that shows temperature



Develop a custom RED Brick web interface
----------------------------------------

TODO: Web interface that shows temperature

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface_schedule.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick web interface scheduler configuration.
   :align: center

index.php
