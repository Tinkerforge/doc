
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
 This Brick is currently work-in-progress.


Features
--------


.. _red_brick_description:

Description
-----------


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
================================  ============================================================


Resources
---------


FAQ
---

* Q: I connected the RED Brick to my Linux PC. Why is there no ``/dev/ttyACM0``
  device to access its serial console?
* A: The ``cdc_acm`` driver has to be loaded for this to work.


.. _red_brick_connectivity:

Connectivity
------------


.. _red_brick_test:

Test your RED Brick
-------------------

.. _red_brick_leds:

LEDs
----

TODO: Image of RED Brick with arrows to LEDs

The RED Brick has a blue, a red and a green LED.

The blue LED is directly connected to the power supply and is on if the 
RED Brick is powered.

The red LED shows if an error is present. If the red LED is on at startup, no 
image could be found. There may be no sd card inserted or there is no 
valid image on the sd card.

The green LED shows the current state. If on startup the red LED is off
and the green LED does not turn on, Linux could start booting. During 
boottime the green LED turns on. After the RED Brick has booted up
and all of the services are available the green led starts showing a
heartbeat.

You can change the function of the green LED after bootup to `show
cpu or sd card usage <TODO>`__ instead of a heartbeat.


.. _red_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RED_Brick_hlpi.table
