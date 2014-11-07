
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to develop software with the use of
a :ref:`RED Brick <red_brick>` and other :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>`.

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
temperature. A LCD 20x4 Bricklet will be used to display the measured values.
An Ethernet Extension is used to communicate with the web. 

We will show how to test written programs on your PC and how to upload and 
execute them on the RED Brick after testing. 

At the end we will write a small Python program which displays the measured
air pressure of the Barometer Bricklet together with other weather information
gain from the internet on the LCD20x4 Bricklet. In your application 
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
Brick and connect the Barometer Bricklet and the LCD 20x4 Bricklet to it. On top 
of this stack we plug the Ethernet Extension.

TODO Stack of RED + Master + Barometer Bricklet + LCD Bricklet + Ethernet Extension

After that we reconnect the RED Brick stack to the PC, open the Brick Viewer
software and press **Connect**. Now the RED Brick tab, a Master Brick,
Barometer Bricklet and LCD20x4 Bricklet tab should come up. You can click 
through the tabs to test them.

Run Example Program
-------------------

To write our first program we have to take a look in the API documentation of
the used modules to see what functions are offered. Each module documentation 
page starts with some examples. We take the "hello world" example of the 
:ref:`LCD 20x4 Bricklet API documentation <lcd_20x4_bricklet_python>` and 
execute it on the RED Brick. 

To do this we download the **example_hello_world.py** Python program. 
Enter the UID of your LCD20x4 Bricklet in line **UID = "XYZ"**. The UID is
shown in the **Setup** tab of the Brick Viewer or in the LCD20x4 Bricklet tab.

Run this program on your PC. If everything went as expected, you should see
"Hello World" in the first line of the LCD20x4 Bricklet.

Execute Program on RED Brick
----------------------------

We now know for certain that the program works as expected and want to execute
it on the RED Brick. The procedure how to upload a program is generally 
described in the 
:ref:`RED Brick Brick Viewer description <red_brick_brickv_program>`.

First we open the RED Brick tab in the Brick Viewer and select the **Program** 
tab.

TODO: Screenshot Brick Viewer Program tab

The **New** button will open the **New Program** wizard. Enter "LCD Hello 
World" as name, and select **Python** as language. Press **Next**.

TODO: Screenshot first page of wizard

Press **Add Files** and select the downloaded and modified 
**example_hello_world.py** program. Press **Next**.

TODO: Screenshot second page of wizard

In this case no changes are needed, so we can again press **Next**.

TODO: Screenshot third page of wizard

We don't want to pass any arguments to our Python program, so we can again press
the **Next** button.

TODO: Screenshot Arguments page

We use Pipe as Standard input and log all output (standard output and standard 
error) to a continuous log file. So no changes are required. Press again 
**Next**.

TODO: Screenshot Stdio

TODO describe schedule page
TODO: Screenshot Schedule

The summary page will summarize our configuration. Press **Next**.
TODO: Screenshot summary

Press the **Start Upload** Button to upload the file. After that press 
**Finish**. You should now see the text "Hello World" in the first line of your 
LCD20x4 Bricklet. 

Gain Internet Access
--------------------

TODO: Screenshot Brickv Screenshot

We need internet access for our example. The Ethernet Extension is already 
connected to the RED Brick, next we have to configure it. The procedure is 
described :ref:`here <red_brick_brick_settings>`. Connect it to your hub, router
or switch. If everything works as expected you can see a configured **tf0** 
interface in the **General** tab of the network settings.


Development of our own Program
------------------------------

Now it is time to write our own program. As mentioned we want to display weather
information gain from the internet together with the measured air pressure of
the Barometer Bricklet.

The programming will not be discussed here in detail. A air pressure callback
is registered with a period of two seconds. So every two seconds the 
**cb_airpressure** function is executed with the measured air pressure as
parameter. We use the `python weather API <https://code.google.com/p/python-weather-api/>`__
to get weather information from `weather.com <http://weather.com>`__. First we
have to get the location ID for our city (or a measurement station nearby).
We pass this location ID to weather.com and get the weather information back.
From this information we are writing the general weather condition and the 
received temperature to the first two lines of the LCD20x4 Bricklet. In the 
third line we display the measured air pressure. After each function call we
print "update lcd" to standard output.

.. literalinclude:: tutorial_red_weather.py
 :language: python
 :linenos:
 :tab-width: 4


We now execute this program again first on our PC to detect possible bugs and 
other problems (the python weather API is preinstalled on the RED Brick, if you 
want to execute this example on your PC you might have to install the weather 
API). If it 
works we will again upload it to the RED Brick. The configuration can be the 
same as mentioned before. After uploading the file you should see every two 
seconds an update of the weather data on your LCD20x4 Bricklet.
If you select your Program in the **Program** tab and scroll down you will come
to the **Logs** section. Click on **Refresh** above, select **Continous** and 
press **Download**. Open the saved log file and you should the output of all the
prints in the program.

You have now learned all necessary steps to develop with the RED Brick.

