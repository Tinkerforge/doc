
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

The following tutorial will demonstrate how to develop software with the
:ref:`RED Brick <red_brick>` together with :ref:`Bricks <primer_bricks>`
and :ref:`Bricklets <primer_bricklets>`. A full step-by-step tutorial that
shows how Bricks, Bricklets and Extensions are used is also available:
:ref:`first steps tutorial <tutorial_first_steps>`.

The RED Brick is the brain of the Tinkerforge building block system.
A program that controls Bricks and Bricklets can be uploaded to and
executed on the RED Brick.

In this tutorial we will demonstrate the different capabilities
of the RED Brick. To keep it simple we will use a small setup
consisting of a RED Brick, a :ref:`Master Brick <master_brick>` and a
:ref:`Temperature Bricklet <temperature_bricklet>`.
Later in the Tutorial will additionally add an Ethernet Extension to
get Internet access.

At first we will test a simple program that prints the temperature
on your PC and upload and execute it on the RED Brick after that.
Then we will extend the program by a GUI to also show the current time
on an HDMI monitor. After that we will add
a web interface for our temperature measurements. The features of this example
are not very useful, but it shows some of the important possibilities of the RED
Brick.

If you build your application, you might use other Bricks, Bricklets
or programming languages, than those used in this example. But the presented
concepts and the workflow will be the same.


Install necessary software
--------------------------

At first you need to install the :ref:`Brick Daemon <brickd>`
and the :ref:`Brick Viewer <brickv>` on your PC or Mac.
Follow the documented steps:

 * :ref:`Brick Daemon Installation <brickd_installation>`
 * :ref:`Brick Viewer Installation <brickv_installation>`

Test the RED Brick
------------------

After you have installed the necessary software, you can test the
RED Brick. At first you need to put a Micro-SD card with an
:ref:`RED Brick software image <red_brick_images>` in the Micro-SD card slot of
the Brick. It is located on the bottom side
(a `Micro-SD card with a pre-installed image <https://www.tinkerforge.com/en/shop/accessories/red-brick.html>`__
can be found in our shop). After that, you can connect the RED Brick
with a mini USB cable to your PC.

.. image:: /Images/Bricks/brick_red_mini_usb_600.jpg
   :scale: 100 %
   :alt: RED Brick with Mini-USB cable
   :align: center
   :target: ../../_images/Bricks/brick_red_mini_usb_800.jpg

Start the Brick Viewer software and click on **Connect**. A tab marked with
**RED Brick** will show up. Click on it. You should see some status
information about the state of the RED Brick. A full description of the
RED Brick tab of the Brick Viewer is documented :ref:`here <red_brick_brickv>`.

The RED Brick is now ready to go!

Add Bricks and Bricklets
------------------------

Now we can be sure that your RED Brick works. Before adding Bricks/Bricklets,
you should power the RED Brick down. To shut it down click on
**System** located in the right upper corner of the RED Brick tab and choose
**Shutdown**. Wait until all LEDs turn off. After that plug a Master Brick on
top of the RED Brick and connect a Temperature Bricklet
Bricklet to it.

.. image:: /Images/Bricks/brick_red_master_temp_600.jpg
   :scale: 100 %
   :alt: RED Brick with Master Brick and Temperature Bricklet
   :align: center
   :target: ../../_images/Bricks/brick_red_master_temp_800.jpg

After that reconnect the RED Brick to the PC, open the Brick Viewer
software and click on **Connect**. Now the RED Brick tab, a Master Brick and the
Temperature Bricklet will come up. You can
click through the tabs to try out the connected hardware.

Run example program
-------------------

Before writing your first program you should to take a look at the API
documentation of the used Bricks/Bricklet to see their supported functions.
Each documentation page starts with some examples. It is a good idea to run an
example program first. We take the "Simple" example of the
:ref:`Temperature Bricklet API documentation <temperature_bricklet_python>` and
execute it.

`Download (example_simple.py) <https://github.com/Tinkerforge/temperature-bricklet/raw/master/software/examples/python/example_simple.py>`__

.. literalinclude:: ../../Software/Bricklets/Temperature_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

To do this you download the ``example_simple.py`` Python program and
replace the UID in the line ``UID = "XYZ"`` with the UID of your Temperature
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
On the RED Brick there won't be any user interaction. We want the program
to print the measured temperature one time and end the program afterwards. So
we need to remove this line.

`Download (example_simple_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_simple_red.py>`__

.. literalinclude:: example_simple_red.py
 :language: python
 :linenos:
 :tab-width: 4

Now you can execute it on the RED Brick. The general program uploading procedure
can be found in the :ref:`RED Brick Brick Viewer description <red_brick_brickv_program>`.
We will only describe the necessary steps here:

.. image:: /Images/Screenshots/red_brick_tutorial_upload_1.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 1.
   :align: center

First, open the RED Brick tab in the Brick Viewer and select the **Program**
tab.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_2.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 2.
   :align: center

The **New** button will open the **New Program** wizard. Enter
"Temperature Logger" as name of the program, and select **Python** as
language. Click on **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_3.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 3.
   :align: center

Click on **Add Files** and select the ``example_simple_red.py`` program.
Click on **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_4.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 4.
   :align: center

We will use Python version **2.7.3**, **Script File** as start mode and
our single file as script file. All of these settings are already
the default, so we can again click on **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_5.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 5.
   :align: center

Our simple Python program does not need any arguments or environment
variable, so we can again click on the **Next** button.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_6.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 6.
   :align: center

We use Pipe as standard input and log all output (standard output and standard
error) to a continuous log file. So no changes are required. Click on
**Next** again.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_7.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 7.
   :align: center

There are many options for scheduling, one of the easiest option is to
schedule a program with a given time interval. Will will choose
**Interval** as mode with an interval time of 10 minutes (**600 seconds**).
This means that our program will be scheduled every 10 minutes, i.e.
the temperature will be logged every 10 minutes.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_8.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 8.
   :align: center

The summary page will show your configuration. Click on **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_9.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick program upload step 9.
   :align: center

Click on the **Start Upload** Button to upload the file. After that click on
**Finish**. You should now be able to take a look at the log file
and see the logged temperatures.

.. image:: /Images/Screenshots/red_brick_tutorial_view_log.jpg
   :scale: 50 %
   :alt: Screenshot Log Files
   :align: center

You can select log files in the browser view and downloading them to your PC by
clicking on **Download**. By the **View** button you can directly take a look
inside the log. With the **Delete** button you can delete the log file from the
RED Brick.

Gain Internet Access
--------------------

To gain Internet access on the RED Brick we can either connect a
USB Wi-Fi/Ethernet dongle or the Ethernet Extension. In this example we
will add the :ref:`Ethernet Extension <ethernet_extension>`:

.. image:: /Images/Bricks/brick_red_master_temp_eth_600.jpg
   :scale: 100 %
   :alt: RED Brick with Master Brick, Temperature Bricklet and Ethernet Extension
   :align: center
   :target: ../../_images/Bricks/brick_red_master_temp_eth_800.jpg

Shut the RED Brick down and remove the power before you stack the
Extension on top of the stack.

After that reconnect power and wait until the enhanced stack has booted.
Click on "Settings". The **Network** section should be opened
and **tfX: Wired** should be selected (X is a number). Select between DHCP or
a static IP and press **Connect**. After a few seconds the **Current Network
Status** should change to **Connected**.


.. image:: /Images/Screenshots/red_brick_tutorial_network.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick network settings.
   :align: center

Now that you have Internet access, you can easily do Internet-of-Things and
similar applications. Another advantage of Internet access is, that the RED Brick
will automatically use `NTP <http://en.wikipedia.org/wiki/Network_Time_Protocol>`__
and thus have a correct system time.

This means that you can now add a time to each measured temperature.

`Download (example_time_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_time_red.py>`__

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
In this example we will add a `PyQt <http://sourceforge.net/projects/pyqt/>`__
GUI to the simple Temperature Bricklet program.

`Download (example_gui_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_gui_red.py>`__

.. literalinclude:: example_gui_red.py
 :language: python
 :linenos:
 :tab-width: 4

The GUI has a label that is refreshed with the current temperature
every second. Additionally there is a **Refresh** button that forces
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

If your RED Brick has a network interface (Wi-Fi dongle or Ethernet Extension),
you can also use it to display a dynamic web page. Currently we support
HTML/JavaScript, PHP and Python for this purpose.

Please look at the :ref:`RED Brick web interface documentation <red_brick_web_interface>`
for more information about the web interface. Basically you can call
your start point ``index.html``, ``index.php`` or ``index.py`` and it will
automatically be used as a directory index.

Our simple Temperature Bricklet program as a web interface looks as follows
(Python and PHP):

`Download (index.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/index.py>`__

.. literalinclude:: index.py
 :language: python
 :linenos:
 :tab-width: 4

`Download (index.php) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/index.php>`__

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
program. It will redirect you to your program path for which your index file
will be executed automatically:

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick web interface.
   :align: center
