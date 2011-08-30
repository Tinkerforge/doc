.. _piezo_buzzer_bricklet:

Piezo Buzzer
============


.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The `Piezo-Buzzer <http://en.wikipedia.org/wiki/Buzzer>`_
:ref:`Bricklet <product_overview_bricklets>` let
extend you the features of every :ref:`Brick <product_overview_bricks>` by 
audio signaling. The device can output 1kHz beeps in different
lengths. It is possible to beep a specified time or to transmit a
`Morse Code <http://en.wikipedia.org/wiki/Morse_code>`_ string.

It is applicable different signaling applications like signal events
("email received") or to localize a lost R/C model.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight
Buzzer                            PS1420P02CT (TDK Corporation)
Output: Beep                      Frequency 1kHz, definable duration
Sound Pressure                    63 dB/10cm (according to datasheet)
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * PS1420P02CT Datasheet (`Download <http://media.digikey.com/pdf/Data%20Sheets/TDK%20PDFs/PS%20Series%20Rev2008.pdf>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/piezo_buzzer_bricklet_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

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
See :ref:`Interface and Coding <ambl_programming_interfaces>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _piezobuzzer_programming_interfaces:

Programming Interfaces
----------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <piezo_buzzer_bricklet_python_api>`", ":ref:`Examples <piezo_buzzer_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <piezo_buzzer_bricklet_java_api>`", ":ref:`Examples <piezo_buzzer_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <piezo_buzzer_bricklet_c_api>`", ":ref:`Examples <piezo_buzzer_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <piezo_buzzer_bricklet_cpp_api>`", ":ref:`Examples <piezo_buzzer_bricklet_cpp_examples>`", "Installation"

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

