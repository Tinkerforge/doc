
:breadcrumbs: <a href="index.html">Home</a> / <a href="index.html#tutorials-and-faq">Tutorials and FAQ</a> / FAQ

.. _faq:

FAQ
===

General information about Bricks, Bricklets and Master Extensions as well as how 
to use them can be found in the :ref:`Primer <primer>`.


My Program only works if Brick Viewer is running
------------------------------------------------

Your program is probably using callbacks, but is not activating them correctly.
Brick Viewer also uses callbacks and activates them if you select the tab of
a Brick or Bricklet. Because the callback configuration is global this activates
the callback for your program to.

To fix this problem you need to activate the callbacks you use in your program
properly. See the documentation of the callback it tells you how to activate
and configure it.


.. _faq_brick_hot:

My Brick gets hot
-----------------

Usually this means that there is some kind of short circuit. More often
than not this happens because of slightly bent pins in the Bricklet
connector:

.. image:: /Images/FAQ/bricklet_connector_short_circuit.jpg
   :scale: 100 %
   :alt: DON'T PANIC 
   :align: center

You can just bend them back again.


One of my Bricklets doesn't show up in the Brick Viewer
-------------------------------------------------------

**Broken Plugin**:

It is possible that there is a corrupted plugin or no plugin saved
on the EEPROM of the Bricklet.

In this case, you should reflash the Bricklet plugin. If a Brick doesn't
show up when the Bricklet is connected, you can connect the Bricklet
after the Brick has started. Then update the Brick as described 
:ref:`here <brickv_flash_plugin>`. 

If the flashing doesn't work: Have you tried a different Bricklet cable?

**Invalid UID**:

If the EEPROM on the Bricklet gets corrupted, it is also possible
that the UID is invalidated. A UID of "1" is invalid. If you can read
a UID of "1" with the Brick Viewer, you should set a new UID that
is unique in your System and in Base58.

**Short circuit in Bricklet connector**:

A short circuit can be caused by a slightly bent pin in the Bricklet
connector. See :ref:`above <faq_brick_hot>`. Please take a look
at the connector of the Brick and Bricklet.

**Defect Bricklet Cable**:

If possible please test with another Bricklet cable.


One of my Bricks doesn't show up in the Brick Viewer
----------------------------------------------------

**Brick in bootloader**:

It is possible that you accidentally brought your Brick in the
bootloader mode. You can recognize this by the fact, that the
LEDs aren't working anymore. In this case you need to 
:ref:`reflash the Brick firmware <brickv_flash_firmware>`.

**Short circuit in Bricklet connector**:

A short circuit can be caused by a slightly bent pin in the Bricklet
connector. See :ref:`above <faq_brick_hot>`.

**Brick Driver installation necessary**:

Bricks need a driver installation on older Windows versions
to work properly. Please see :ref:`here <brickd_install_windows_driver>`.

**Renesas/NEC USB 3.0 controller with old driver**:

If your Brick is connected to a Renesas/NEC USB 3.0 controller (µPD720200)
ensure that you have at least driver version 2.1.16 installed for this
controller. Older driver versions have a bug that hinders brickd from seeing
Bricks connected to such an USB controller.

Driver updates can be found on `usb3-drivers.com
<http://www.usb3-drivers.com/renesas-usb3-drivers.html>`__ and `computerbase.de
<http://www.computerbase.de/downloads/treiber/usb-3.0-host-controller-treiber/>`__.


An Extension does not show up in the Brick Viewer
-------------------------------------------------

**Extension is below Master Brick**:

Extensions have to be on top of the Master Brick. You can put other Bricks between
the Master Brick and the Extension, but the Master Brick have to be the lowermost Brick
(except of power supplies like Step-Down Power Supply).


**Extension is not configured**:

Connect a single Master Brick to your PC and open the Brick Viewer. 
After the Master Brick shows up in the Brick Viewer stick the Extension on it. 
Click on "Configure" and select Extension 0. Select the appropriate 
Extension Type and press "Save". Now restart the Master Brick, after restart
the Master Brick Tab should show the Extension now.

.. image:: /Images/Screenshots/brickv_configure_extension_type.jpg
   :scale: 60 %
   :alt: Screenshot of Brickv configure extension type dialogue 
   :align: center


I get timeouts when I call a function
-------------------------------------

**UID**:

Check the UID. You have to create the device object with the correct
UID of the device, otherwise it can't answer because it didn't
receive your request.

**Brick Daemon**:

Is the Brick Daemon running? You can check in the list of processes
if the Daemon is running (e.g. in the task manager on Windows).

If it isn't running but it is installed correctly, you can 
try to restart the service (Windows) or daemon (Mac OS X
and Linux). The service/daemon should also be started automatically 
on startup.

**WIFI Extension**:

Did you use the IP address of the WIFI Extension? If you want to
connect directly to the WIFI Extension, you have to use its
IP address instead of "localhost".


I don't get timeouts when I call a function
-------------------------------------------

If you expect to get a timeout (e.g. because a Brick or Bricklet is not
connected) but you don't get one, you are probably calling a 
"setter". Normally a function that doesn't return anything will not
wait for a response form a Brick or Bricklet.

It is however possible to configure it this way. See the 
``SetResponseExpected`` function in the API documentation of each
device.


The current measurement of my Step-Down Power Supply does not work
------------------------------------------------------------------

The measurement is designed for high currents. If only a single
Master Brick is connected to the Step-Down Power Supply it is
possible that the little current that is drawn by the Master Brick
doesn't get recognized at all (i.e. ``GetStackCurrent`` returns 0).


My Brick doesn't show up as serial port for flashing
----------------------------------------------------

**Brick not in bootloader**:

A Brick can only be flashed if it's in bootloader mode. To enter the bootloader
hold the Erase button, then press the Reset button 1x. The blue LED should be
off now.

**Driver not installed (on Windows)**:

On Windows you might need to install the Atmel driver ``atm6124_cdc.inf`` from
the ``drivers`` subfolder in the Brick Viewer installation folder to make Windows
detect a Brick in bootloader mode correctly.

Windows 7 and 8 typically auto detect a Brick as "GPS Camera Detect" serial
device. This works as well, just select "GPS Camera Detect" as serial port in
Brick Viewer.

**Master Brick 2.0 in stack with Master Extension**:

Master Brick hardware version 2.0 has a change in its PCB layout that interferes
with bootloader mode if a Master Extension such as RS485, WIFI or Ethernet is
present in the stack. In this case the Master Extension needs to be disconnected
from the stack to make the bootloader mode work correctly.

**/dev/ttyACM0 is not user-accessible (on Linux)**:

Serial devices might not be user-accessible on Linux. The device is listed in
Brick Viewer, but an error is reported if you try to flash the Brick. As
workaround start Brick Viewer as ``root``.


I updated something and now it doesn't work anymore
---------------------------------------------------

You probably have a version mismatch. On January 22nd 2013 we released a new 
protocol version, Protocol 2.0. This means that the way Bricks and Bricklets
communicate with each other and with the Brick Daemon has changed. Also
there are small changes in the API. You need to update your
language Bindings, the Brick Daemon, the Brick Viewer and the 
Firmwares/Plugins of your Bricks/Bricklets to a version starting with "2".

To do this you can use the :ref:`transitioning guide <transition_1to2>`. 
It also describes how to port already existing code to the new protocol. 
