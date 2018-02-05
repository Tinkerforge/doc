
.. _programming_interface:

Programming Interface
=====================

The Programming Interface uses preprogrammed devices
(:ref:`Bricks <primer_bricks>` and 
:ref:`Bricklets<primer_bricklets>`) that can be controlled by an 
(embedded-) PC, tablet or smart phone. Each device has its own unique
identifier (UID).

The user calls a function implemented in the :ref:`API Bindings <api_bindings>`
on a UID specified device. This function creates a TCP/IP data package 
which will be delivered to the :ref:`Brick <primer_bricks>` with the
corresponding UID. 

If this Brick is connected via USB to a computer, a 
program called :ref:`Brick Daemon <brickd>` has to be installed.
It acts as a translator between TCP/IP and USB. 
Some :ref:`Master Extensions <primer_master_extensions>` can be used
to create a direct TCP/IP connection without the need of another
computer in between. One example for it is the :ref:`WIFI Extension <wifi_extension>`.

After receiving a package, the Brick performs the task specified in the delivered 
data. For example in case of a ``getTemperature()`` call the Brick will read the
temperature and send it back. The initial function call blocks until the 
data package is received and returns the temperature.

In case of calling a :ref:`Bricklet <primer_bricklets>` function,
data is send to the Brick where the Bricklet is attached. The Brick
calls the corresponding function.

The Bricklet function called, is initially stored together with other data
e.g. UID (together called plugin), in the  
`EEPROM <https://en.wikipedia.org/wiki/EEPROM>`__ on the Bricklet.
At start up, this function (with other Bricklet functions if any) is loaded 
(as `position independent code <https://en.wikipedia.org/wiki/Position_independent_code>`__)
into the connected Brick Flash.
When the Brick calls the corresponding Bricklet function, this function is 
already loaded inside the Bricks Flash. 
This generic approach makes it possible to have compatibility between all 
Bricks and Bricklets, including future ones.

The Programming Interface is available for Windows, Linux and 
Mac OS X as well as mobile operating systems, such as Android,
iOS and Windows Phone.

.. note::
 See this :ref:`tutorial <tutorial_first_steps>` for more information on how to
 use it and an idea of the Brick and Bricklet concept.
