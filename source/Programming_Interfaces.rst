.. _pi:

Programming Interfaces
======================


.. _pi_hlpi:

High Level Programming Interface (HLPI)
---------------------------------------

This interfaces uses preprogrammed devices which are controlled
by an PC. Each device has its own unique identifier (UID).

The user calls a method implemented in our :ref:`API Bindings <api_bindings>` 
on a device specified by a UID. 
This method creates a data package which will be delivered to the
:ref:`Brick <product_overview_bricks>` with the according UID.
The Brick performs the task specified in the delivered data. 
For example in case of an "getTemperature()" call the Brick will readout the
temperature and sends an data package back which contains it. The method 
call blocks until the data package is received and final returns 
the temperature.

In case of calling a :ref:`Bricklet <product_overview_bricklets>` method,
data is send to the Brick at which the Bricklet is attached. The Brick 
calls the according method stored in the 
`EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ on the Bricklet.
This method performs the according task and can send back data.

This interface is available for Windows, Linux and Mac OS systems.


.. note::

   See our :ref:`tutorial` for more information how to use it
   and an idea of the Brick/Bricklet concept.


.. _pi_llpi:

Low Level Programming Interface (LLPI)
--------------------------------------

If you have an microcontroller board and want to use our products, 
the Low Level Programming Interface may hit the spot. You can
access every :ref:`Brick <product_overview_bricks>` over a **SPI**, **I2C** or **serial**
connection. :ref:`Bricklets <product_overview_bricklets>` can be accesses by these
interfaces over the connected Brick. 

Additionally it is possible to use our Bricklets as breakout boards
and read the equipped sensor directly (e.g. the analog voltage of an light
sensor).

.. note::

   | Currently only the direct access on Bricklets is supported.
   | See particular documentation for more information.

   Support of Bricks will coming soon...


.. _pi_odpi:

On Device Programming Interface (ODPI)
--------------------------------------

On Device Programming Interface (ODPI) is an API to write your own firmware on our
devices.

.. note::

   Currently only the source-code of our devices is online (Todo Link). You are
   free to adapt the code for your own purposes. We are working on a
   special API to assist easy firmware development.

   Comming soon...

