.. _dual-relay_bricklet:

Dual-Relay
===========


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

With the Dual Relay :ref:`Bricklet <concepts_bricklets>` the features of
every :ref:`Brick <concepts_bricks>` can be extended by two 
`relays <http://en.wikipedia.org/wiki/Relay>`_. Each relay has three
terminals such that the terminal in the middle is electrically connected to 
the terminal left or right depending on the state. 
The state is visualized by a LED.

You can use this Bricklet to switch power-supplies, motors, lamps, etc.
Consider the maximum voltage and current.

.. warning::

   Be aware that handling of higher voltages is potentially dangerous!

   Note that terminals and contacts are not insulated. 
   Do not touch when switching higher voltages. 
   Doing so might cause electric shock.

Technical Specifications
------------------------

=================================  ============================================================
Property                           Value
=================================  ============================================================
Dimensions                         45mm x 45mm (1.77" x 1.77")
Weight
Current Consumption (per Channel)
---------------------------------  ------------------------------------------------------------
---------------------------------  ------------------------------------------------------------
Maximum Voltage/Current            250V/10A or 125V/15A
=================================  ============================================================

Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/dual-relay_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <concepts_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_interface_coding>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _dualrelay_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <dual_relay_bricklet_python_api>`", ":ref:`Examples <dual_relay_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <dual_relay_bricklet_java_api>`", ":ref:`Examples <dual_relay_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <dual_relay_bricklet_c_api>`", ":ref:`Examples <dual_relay_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <dual_relay_bricklet_cpp_api>`", ":ref:`Examples <dual_relay_bricklet_cpp_examples>`", "Installation"

   "Python", "API", "Example", "Installation"
   "Java", "API", "Example", "Installation"
   "C", "API", "Example", "Installation"
   "C++", "API", "Example", "Installation"


:ref:`Low Level Interfaces <concepts_llpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI, over Brick", "API", "Example", "Installation"
   "I2C, over Brick", "API", "Example", "Installation"
   "UART(serial), over Brick", "API", "Example", "Installation"
   "Analog Voltage, directly", "\-", "Example", "\-"

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

