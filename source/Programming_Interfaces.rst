.. _pi:

Programming Interfaces
======================


.. _pi_hlpi:

High Level Programming Interface (HLPI)
---------------------------------------

The High Level Programming Interface uses preprogrammed devices
(Bricks/Bricklets) that are controlled by a PC. Each device has its 
own unique identifier (UID).

The user calls a method implemented in the :ref:`API Bindings <api_bindings>` 
on a device specified by a UID. 
This method creates a data package which will be delivered to the
:ref:`Brick <product_overview_bricks>` with the corresponding UID.
The Brick performs the task specified in the delivered data. 
For example in case of a "getTemperature()" call the Brick will read the
temperature and send it back. The method call blocks until the data package 
is received and returns the temperature.

In case of calling a :ref:`Bricklet <product_overview_bricklets>` method,
data is send to the Brick where the Bricklet is attached. The Brick 
calls the corresponding method stored in the 
`EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ on the Bricklet.
This method performs the task and sends back the requested data.

This interface is available for Windows, Linux and Mac OS as well
as mobile operating systems, such as Android, iOS and Windows Mobile.


.. note::

   See the :ref:`tutorial` for more information on how to use it
   and an idea of the Brick/Bricklet concept.


.. _pi_llpi:

Low Level Programming Interface (LLPI)
--------------------------------------

If you have a microcontroller board (such as Arduino) and you want to use 
Bricks/Bricklets, the Low Level Programming Interface can be used. You can
access every :ref:`Brick <product_overview_bricks>` over a 
**SPI**, **I2C** or **serial** connection. 
:ref:`Bricklets <product_overview_bricklets>` can be accesses by these
interfaces over the connected Brick. 

Additionally it is possible to use Bricklets as breakout boards
and read the equipped sensor directly (e.g. the analog voltage of a light
sensor).

.. warning::

   Currently only the direct access to Bricklets is supported.
   See the particular Bricklet documentation for more information.

   The LLPI support for Bricks is not yet implemented.


.. _pi_odpi:

On Device Programming Interface (ODPI)
--------------------------------------

The On Device Programming Interface (ODPI) is an API to write your own 
firmware for Bricks.

.. warning::

   Currently only the source code of the Bricks is
   `online <https://github.com/organizations/Tinkerforge>`__. 
   If you have the skills to set up the compiler environment and can
   program c, you can adapt the code for your own purposes. 
   
   We are working on a simple API to allow easy firmware development
   (comparable to the Arduino API). 
