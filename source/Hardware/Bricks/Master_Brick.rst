.. _master_brick:

Master Brick
============

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The Master :ref:`Brick <product_overview_bricks>` is a microcontroller board 
used for two purposes. First of all it is equipped with **four** 
:ref:`Bricklet <product_overview_bricklets>` ports and therefore ideally 
suited for applications where a great many of Bricklets are used.

Secondly, the Master Brick can be used for communication purposes.
When building a stack the lowermost Master Brick
acts as the master of this stack and routes all communication between the
boards of the stack and the PC. Other Master Bricks in the stack detect this 
and does not act as master. They are only provide their attached Bricklets.

In the simple case the communication with a stack is routed 
over the USB connection of the master. This interface can be changed with 
:ref:`Master-Extensions <product_overview_master_extensions>`. There are
Master-Extensions for cable based or wireless interfaces. Master-Extensions
will be plugged on the topside of the master. The master detect them
and use this additional interface.

In the future it will be possible to control the device low level 
via a **I2C**, **SPI** or **UART (serial)** interface from other microcontroller boards
(:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            TBD
================================  ============================================================


Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Master Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/master_brick_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


.. Powersupply
.. ^^^^^^^^^^^

.. Todo: Bildchen

Stacking
--------

Auf Tutorial verweisen.
Todo: Hier Plug/Play beschreiben
wann module erkannt
beispiel

Programming Interfaces
----------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^
See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <master_brick_python_api>`", ":ref:`Examples <master_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <master_brick_java_api>`", ":ref:`Examples <master_brick_java_examples>`", "Installation"
   "C", ":ref:`API <master_brick_c_api>`", ":ref:`Examples <master_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <master_brick_cpp_api>`", ":ref:`Examples <master_brick_cpp_examples>`", "Installation"

Low Level Interfaces
^^^^^^^^^^^^^^^^^^^^
 .. note::  Comming soon! 

  Currently you have to modify the firmware to use this feature.
  SPI, I2C and UART interface are present and can be easily accessed with our
  :ref:`Breakout Board <breakout_brick>`. A special firmware is planned
  to control this brick over the different interfaces by transmitted commands.
  
..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "SPI", "API", "Examples", "Installation"
     "I2C", "API", "Examples", "Installation"
     "UART(serial)", "API", "Examples", "Installation"


Direct on Device Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note:: Coming soon!

  Currently no API or special documentation exists for direct programming.
  You can use our firmware as startingpoint for your own modifications.

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"

Troubleshoot
------------

