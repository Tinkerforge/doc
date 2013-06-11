
:breadcrumbs: <a href="index.html">Home</a> / Programming Interfaces

.. _pi:

Programming Interfaces
======================


.. _pi_hlpi:

High Level Programming Interface (HLPI)
---------------------------------------

The High Level Programming Interface uses preprogrammed devices
(:ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets<product_overview_bricklets>`) that can be controlled by an 
(embedded-) PC, tablet or smart phone. Each device has its own unique
identifier (UID).

The user calls a function implemented in the :ref:`API Bindings <api_bindings>`
on a UID specified device. This function creates a TCP/IP data package 
which will be delivered to the :ref:`Brick <product_overview_bricks>` with the
corresponding UID. 

If this Brick is connected via USB to a computer, a 
program called :ref:`Brick Daemon <brickd>` has to be installed.
It acts as a translator between TCP/IP and USB. 
Some :ref:`Master Extensions <product_overview_master_extensions>` can be used
to create a direct TCP/IP connection without the need of another
computer in between. One example for it is the :ref:`WIFI Extension <wifi_extension>`.

After receiving a package, the Brick performs the task specified in the delivered 
data. For example in case of a ``getTemperature()`` call the Brick will read the
temperature and send it back. The initial function call blocks until the 
data package is received and returns the temperature.

In case of calling a :ref:`Bricklet <product_overview_bricklets>` function,
data is send to the Brick where the Bricklet is attached. The Brick
calls the corresponding function.

The Bricklet function called, is initially stored together with other data
e.g. UID (together called plugin), in the  
`EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ on the Bricklet. 
At start up, this function (with other Bricklet functions if any) is loaded 
(as `position independent code <http://en.wikipedia.org/wiki/Position_independent_code>`__) 
into the connected Brick Flash 
(see :ref:`Building a Bricklet plugin <building_bricklet_plugin>`).
When the Brick calls the corresponding Bricklet function, this function is 
already loaded inside the Bricks Flash. 
This generic approach makes it possible to have compatibility between all 
Bricks and Bricklets, including future ones.


The High Level Programming Interface is available for Windows, Linux and 
Mac OS as well as mobile operating systems, such as Android, 
iOS and Windows Mobile.

.. note::
 See the :ref:`tutorial` for more information on how to use it
 and an idea of the Brick and Bricklet concept.


.. _pi_odpi:

On Device Programming Interface (ODPI)
--------------------------------------

The On Device Programming Interface (ODPI) is an API to write your own
firmware for Bricks.

.. warning::
 Currently only the source code of the Bricks and Bricklets is
 `online <https://github.com/organizations/Tinkerforge>`__.
 If you have the skills to set up the compiler environment and can
 program C, you can adapt the code for your own purposes.

 We are working on a simple API to allow easy firmware development
 (comparable to the Arduino API).
