
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to develop software with the 
:ref:`RED Brick <red_brick>` together with other :ref:`Bricks <primer_bricks>` 
and :ref:`Bricklets <primer_bricklets>`. A full step by step tutorial in how to 
use Bricks, Bricklets and Extensions can be found in the 
:ref:`First steps - Tutorial <tutorial_first_steps>`.

The RED Brick can be described as brain of the building block system.
Your program will control other Bricks and Bricklets and can be uploaded and 
executed on the RED Brick. The RED Brick itself can't control 
motors and isn't equipped with sensors, so you have to plug other modules from
the building block system to it to get the necessary features.

In this tutorial we will demonstrate the different possibilities when 
working with the RED Brick. We will use the RED Brick together
with a Master Brick and a Barometer Bricklet to measure the air pressure A 
LCD20x4 Bricklet will be used to display the measured values. An Ethernet 
Extension is used to gain data from the web. 

We will show how to test written programs on your PC and how to upload and 
execute them on the RED Brick after testing. At the end of this tutorial we will 
write a small Python program which displays the measured air pressure of the 
Barometer Bricklet together with other weather information on the LCD20x4 
Bricklet. If you develop your application, you might use other Bricks, Bricklets 
and programming language, but the concepts and workflow stays the same.
	

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

Add Bricks, Bricklets and Extensions
------------------------------------

After these tests we will add the other hardware modules to it. You should
only do this if the RED Brick is powered down. To shut it down click on 
**System** located in the right upper corner of the RED Brick tab and choose 
**shut down**. Wait until all leds turn off. After that stick a Master Brick on 
top of the RED Brick and connect the Barometer Bricklet and the LCD 20x4 
Bricklet to it. On top of this stack we plug the Ethernet Extension.

TODO Stack of RED + Master + Barometer Bricklet + LCD Bricklet + Ethernet Extension

After that reconnect the RED Brick stack to the PC, open the Brick Viewer
software and click on **Connect**. Now the RED Brick tab, a Master Brick,
Barometer Bricklet and LCD20x4 Bricklet tab should come up. You might want to
click through the tabs to test the connected hardware.

Run example program
-------------------

Before writing your first program you have to take a look in the API 
documentation of the used modules to see the supported functions. Each
documentation page starts with some examples. It is a good idea to run an 
example program first. We take the "hello world" example of the 
:ref:`LCD 20x4 Bricklet API documentation <lcd_20x4_bricklet_python>` and 
execute it. 

To do this we download the **example_hello_world.py** Python program and
replace the UID in the line **UID = "XYZ"** with the UID of your LCD20x4 
Bricklet. You can find it in the **Setup** tab of the Brick Viewer or in the 
LCD20x4 Bricklet tab.

Execute this program on your PC. If everything went as expected, you should see
"Hello World" in the first line of the LCD20x4 Bricklet.

Execute the program on the RED Brick
------------------------------------

We have tested the example program and know that it is working correctly. Next 
we will execute it on the RED Brick. The procedure how to upload a program is 
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

Click on **Add Files** and select the downloaded and modified 
**example_hello_world.py** program. Click on **Next**.

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

TODO: Screenshot Brickv Screenshot

We need internet access for the following example. The Ethernet Extension is already 
connected to the RED Brick, next we have to configure it. The procedure is 
described :ref:`here <red_brick_brick_settings>`. Connect it to your hub, router
or switch. If everything works as expected you can see a configured **tf0** 
interface in the **General** tab of the network settings.


TODO: Screenshot Brickv configured interface


Develop a custom program
------------------------

Now it is time to write your own program. As mentioned we want to display 
weather information gained from the web together with the measured air pressure 
of the Barometer Bricklet.

The program will not be discussed here in detail. A air pressure callback
is registered with a period of two seconds. So every two seconds the 
**cb_airpressure** function is executed with the measured air pressure as
parameter. The `python weather API <https://code.google.com/p/python-weather-api/>`__
is used to get weather information from `weather.com <http://weather.com>`__. 
At first the location ID for your city (or a measurement station nearby) had to
be determined. This location ID is passed to weather.com to get the weather 
information back. From this information the general weather condition and the 
received temperature is written to the first two lines of the LCD20x4 Bricklet. 
In the third line the measured air pressure is displayed. After each function 
call "update lcd" is printed to standard output.

.. literalinclude:: tutorial_red_weather.py
 :language: python
 :linenos:
 :tab-width: 4


You should execute this program again first on your PC to detect possible bugs 
and other problems (the python weather API is preinstalled on the RED Brick, if 
you execute this example on your PC you might have to install the weather 
API first). If it works you can upload it to the RED Brick. The configuration 
can be the same as mentioned before. After uploading the file you should see 
every two seconds an update of the weather data on your LCD20x4 Bricklet.

If you select your Program in the **Program** tab and scroll down you will come
to the **Logs** section. Click on **Refresh** above, select **Continous** and 
click on **Download**. Open the saved log file and you should the output of all 
the prints in the program. This way you can log measured values or determine 
problems during execution.

You have now learned all necessary steps to develop with the RED Brick.

Develop a custom GUI
--------------------

pyqt



Develop a custom web interface
------------------------------

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface_schedule.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick web interface scheduler configuration.
   :align: center

index.php
