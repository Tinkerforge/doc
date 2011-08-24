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

The Master :ref:`Brick <concepts_bricks>` is a microcontroller board 
used for two purposes. First of all it is equipped with four 
:ref:`Bricklet <concepts_bricklets>` ports and therefore ideally suited for 
applications where a great many of Bricklets are used.

Secondly, the Master Brick can be used for communication purposes.
When building a :ref:`Stack <concepts_stack>` the lowermost Master Brick
acts as the master of this Stack and routes all communication between the
boards of the Stack and the PC. Other Master Bricks in the Stack detect this 
and does not act as master. They are only provide their attached Bricklets.

In the simple case the communication with a Stack is routed 
over the USB connection of the master. This interface can be changed with 
:ref:`Master-Extensions <concepts_master-extensions>`. There are
Master-Extensions for cable based or wireless interfaces. Master-Extensions
will be plugged on the topside of the master. The master detect them
and use this additional interface.

Also it is possible to control the device low level via a **I2C**, **SPI** or
**UART (serial)** interface from other microcontroller boards
(:ref:`Low Level Concept <concepts_llpi>`). A direct interface for
Arduinos is provided by our :doc:`Tinkershield </Hardware/Tinkershield>`.
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <concepts_odpi>`).

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
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

.. image:: /Images/Dimensions/master_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


.. Powersupply
.. ^^^^^^^^^^^

.. Todo: Bildchen

Stacking
--------

Todo: Hier Plug/Play beschreiben
wann module erkannt
beispiel

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <master_brick_python_api>`", ":ref:`Examples <master_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <master_brick_java_api>`", ":ref:`Examples <master_brick_java_examples>`", "Installation"
   "C", ":ref:`API <master_brick_c_api>`", ":ref:`Examples <master_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <master_brick_cpp_api>`", ":ref:`Examples <master_brick_cpp_examples>`", "Installation"

Low Level Interfaces
^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI", "API", "Examples", "Installation"
   "I2C", "API", "Examples", "Installation"
   "UART(serial)", "API", "Examples", "Installation"


Direct on Device Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Programming", "API", "Examples", "Installation"


Troubleshoot
------------

