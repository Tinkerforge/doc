
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to develop software with the 
:ref:`RED Brick <red_brick>` together with :ref:`Bricks <primer_bricks>` 
and :ref:`Bricklets <primer_bricklets>`. A full step by step tutorial that
shows how Bricks, Bricklets and Extensions are used can be found in the 
:ref:`first steps tutorial <tutorial_first_steps>`.

The RED Brick is the brain of the Tinkerforge building block system.
A program that controls Bricks and Bricklets can be uploaded to and 
executed on the RED Brick. 

In this tutorial we will demonstrate the different capabilities
of the RED Brick. To keep it simple we will use a small setup
consisting of a RED Brick, a Master Brick and a Temperature Bricklet.
Later in the Tutorial will additionally add an Ethernet Extension to
get internet access.

We will test a simple program that prints a temperature
on your PC and upload and execute it on the RED Brick after that. 
Then we will extend the program to also show the current time,
to utilize a GUI (that is shown on an HDMI monitor) and we will add
a web interface for our temperature measurements.

If you build your application, you might use other Bricks, Bricklets 
and programming languages, but the concepts and the workflow will be the same.
	

Install necessary software
--------------------------

At first you need to install the :ref:`Brick Daemon <brickd_installation>` and 
the :ref:`Brick Viewer <brickv_installation>` software on 
your PC/Mac. Please follow the documented steps.

Test the RED Brick
------------------

TODO Image RED Brick

After you have installed the necessary software on your PC, you can test the 
RED Brick. At first you need to put a micro SD card with an 
:ref:`RED Brick software image <red_brick_images>` in the micro SD card slot of
the Brick. It is located on the bottom side. A `micro SD card with a pre-installed image <TODO>`__
can be found in our shop. After that, you can connect the RED Brick 
with a mini USB cable to your PC.

TODO Image RED Brick connected with mini USB cable

Start the Brick Viewer software and click on **Connect**. A tab marked with 
**RED Brick** will show up. Click on it. You should see some status 
information about the state of the RED Brick. A full description of the 
RED Brick tab of the Brick Viewer is documented :ref:`here <red_brick_brickv>`.

The RED Brick is now ready to go!

Add Bricks and Bricklets
------------------------

Know we can be sure that your RED Brick works. Before adding Bricks/Bricklets,
you should power the RED Brick down. To shut it down click on 
**System** located in the right upper corner of the RED Brick tab and choose 
**shut down**. Wait until all LEDs turn off. After that plug a Master Brick on 
top of the RED Brick and connect a Temperature Bricklet 
Bricklet to it.

TODO Stack of RED + Master + Temperature Bricklet

After that reconnect the RED Brick to the PC, open the Brick Viewer
software and click on **Connect**. Now the RED Brick tab, a Master Brick and the
Temperature Bricklet will come up. You can
click through the tabs to try out the connected hardware.

Run example program
-------------------

Before writing your first program you should to take a look at the API 
documentation of the used modules to see the supported functions. Each
documentation page starts with some examples. It is a good idea to run an 
example program first. We take the "Simple" example of the 
:ref:`Temperature Bricklet API documentation <temperature_bricklet_python>` and 
execute it. 

.. literalinclude:: ../Software/Bricklets/Temperature_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

To do this you download the **example_simple.py** Python program and
replace the UID in the line **UID = "XYZ"** with the UID of your Temperature 
Bricklet. You can find it in the **Setup** tab of the Brick Viewer or in the 
Temperature Bricklet tab.

Execute this program on your PC. If everything went as expected, you should see
the current temperature in the command line.

Execute the program on the RED Brick
------------------------------------

Now you have tried out the example and you know that it is working 
correctly. In the example program we wait for user input::
 
 raw_input('Press key to exit\n')

We do this to prevent the command line on windows from closing immediately. 
On the RED Brick there won't be any user interaction, so you need to remove 
this line.

`Download (example_simple_red.py) <https://github.com/Tinkerforge/doc/TODO/example_simple_red.py>`__

.. literalinclude:: example_simple_red.py
 :language: python
 :linenos:
 :tab-width: 4


Now you can execute it on the RED Brick. The general program uploading procedure
can be found in the :ref:`RED Brick Brick Viewer description <red_brick_brickv_program>`.
We will only describe the necessary steps here:

First, open the RED Brick tab in the Brick Viewer and select the **Program** 
tab.

TODO: Screenshot Brick Viewer Program tab

The **New** button will open the **New Program** wizard. Enter 
"Temperature Logger" as name of the program, and select **Python** as 
language. Click on **Next**.

TODO: Screenshot first page of wizard

Click on **Add Files** and select the **example_simple_red.py** program. 
Click on **Next**.

TODO: Screenshot second page of wizard

In this case no changes are needed, so we can again click on **Next**.

TODO: Screenshot third page of wizard

We don't want to pass any arguments to our Python program, so we can again 
click on the **Next** button.

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
**Finish**. You should now be able to take a look at the log file
and see the logged temperatures

Gain internet access
--------------------

To gain internet access on the RED Brick we can either connect a 
USB WIFI/Ethernet dongle or the Ethernet Extension. In this example we 
will add the Ethernet Extension:

TODO Stack of RED + Master + Temperature Bricklet + Ethernet Extension

Shut the RED Brick down and remove the power before you add the
Extension.

After the enhanced stack has booted click on "Settings", "Network", 
"Wired" in the RED Brick tab of the Brick Viewer.
Choose **tf0** as interface either use DHCP or enter a static
configuration. Then click on **Save**.

Now you can see the configured **tf0** interface in the **General** 
tab of the network settings. If you use DHCP you may have to click
**Refresh** a few times until the RED Brick received an IP.

.. image:: /Images/Screenshots/red_brick_tutorial_network_general.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick network settings.
   :align: center

Now that you have internet access, you can can easily do IoT and similar
applications. Another advantage of internet access is, that the RED Brick
will automatically use `NTP <http://en.wikipedia.org/wiki/Network_Time_Protocol>`__ 
and thus have a correct system time.

This means that you can now add a time to each measured temperature.

`Download (example_time_red.py) <https://github.com/Tinkerforge/doc/TODO/example_time_red.py>`__

.. literalinclude:: example_time_red.py
 :language: python
 :linenos:
 :tab-width: 4

You can upload this program the same way as before.


Develop a custom RED Brick GUI
------------------------------

.. note::
    GUI on the RED Brick only works with the full image.

Another type of program that the RED Brick can execute is a GUI program
that is shown on the HDMI output.
In this example we will add a Qt GUI to the simple Temperature Bricklet
program.

`Download (example_gui_red.py) <https://github.com/Tinkerforge/doc/TODO/example_gui_red.py>`__

.. literalinclude:: example_gui_red.py
 :language: python
 :linenos:
 :tab-width: 4

The GUI has a label that is refreshed with the current temperature
every second. Additionally there is a *Refresh* button that forces
a refresh of the label. 

You can upload this program the same way as the other Python programs
before, with two small differences:

.. image:: /Images/Screenshots/red_brick_tutorial_gui_environment.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick GUI environment.
   :align: center

In step 4 you need to add the environment variable **DISPLAY** with
a value of **:0**. With this configuration the GUI will be shown on
the RED Brick desktop that is running on the full image. Adding this
variable is necessary, the program will not be able to start otherwise.

.. image:: /Images/Screenshots/red_brick_tutorial_gui_schedule.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick GUI schedule.
   :align: center

For the scheduler you may want to choose **Always** and tick off
**Continue After Error**. With this configuration your GUI will be
automatically restarted if is closed and also if it fails with
an error.

On the RED Brick desktop the simple GUI looks as follows:

.. image:: /Images/Screenshots/red_brick_tutorial_gui.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick Temperature GUI.
   :align: center

Develop a custom RED Brick web interface
----------------------------------------

If your RED Brick has a network interface (WIFI dongle or Ethernet Extension),
you can also use it to display a dynamic web page. Currently we support
HTML/JavaScript, PHP and Python for this purpose.

Please look at the :ref:`RED Brick web interface documentation <red_brick_web_interface>`
for more information about the web interface. Basically you can call
your start point index.html, index.php or index.py and it will automatically
be used as a directory index.

Our simple Temperature Bicklet program as a web interface looks as follows
(Python and PHP):

`Download (index.py) <https://github.com/Tinkerforge/doc/TODO/index.py>`__

.. literalinclude:: index.py
 :language: python
 :linenos:
 :tab-width: 4

`Download (index.php) <https://github.com/Tinkerforge/doc/TODO/index.php>`__

.. literalinclude:: index.php
 :language: php
 :linenos:
 :tab-width: 4

If your program is used as a web interface, you don't need to configure
your executable, arguments, environment and working directory. The steps
4-6 will actually be skipped if you choose **Web Interface** in Step 3:

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface_execution.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick web interface execution configuration.
   :align: center

To take a look at your web interface go to the IP address or hostname of
your RED Brick with a browser and click on the **Bin** button of your
program. Your index file will be used automatically:

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick web interface.
   :align: center

