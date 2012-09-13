.. _pi:

Programming Interfaces
======================


.. _pi_hlpi:

High Level Programming Interface (HLPI)
---------------------------------------

The High Level Programming Interface uses preprogrammed devices
(Bricks and Bricklets) that are controlled by a PC. Each device has its
own unique identifier (UID).

The user calls a function implemented in the :ref:`API Bindings <api_bindings>`
on a device specified by a UID.  This function creates a data package which
will be delivered to the :ref:`Brick <product_overview_bricks>` with the
corresponding UID. The Brick performs the task specified in the delivered data.
For example in case of a "getTemperature()" call the Brick will read the
temperature and send it back. The function call blocks until the data package
is received and returns the temperature.

In case of calling a :ref:`Bricklet <product_overview_bricklets>` function,
data is send to the Brick where the Bricklet is attached. The Brick
calls the corresponding function stored in the
`EEPROM <http://en.wikipedia.org/wiki/EEPROM>`__ on the Bricklet.

This interface is available for Windows, Linux and Mac OS as well
as mobile operating systems, such as Android, iOS and Windows Mobile.

.. note::
 See the :ref:`tutorial` for more information on how to use it
 and an idea of the Brick and Bricklet concept.


.. _pi_odpi:

On Device Programming Interface (ODPI)
--------------------------------------

The On Device Programming Interface (ODPI) is an API to write your own
firmware for Bricks.

.. warning::
 Currently only the source code of the Bricks is
 `online <https://github.com/organizations/Tinkerforge>`__.
 If you have the skills to set up the compiler environment and can
 program C, you can adapt the code for your own purposes.

 We are working on a simple API to allow easy firmware development
 (comparable to the Arduino API).
