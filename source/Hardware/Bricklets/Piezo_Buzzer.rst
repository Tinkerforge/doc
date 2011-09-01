.. _piezo_buzzer_bricklet:

Piezo Buzzer
============


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #2") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #3") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #4") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #5") }}
	{{ tfdocend() }}


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

* Buzzer Datasheet (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/datasheets/ef532_ps.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/hardware/piezo-buzzer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/piezo_buzzer_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _piezo_buzzer_bricklet_test:

Test your Piezo Buzzer Bricklet
-------------------------------

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

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <piezo_buzzer_bricklet_c_api>`", ":ref:`Examples <piezo_buzzer_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <piezo_buzzer_bricklet_csharp_api>`", ":ref:`Examples <piezo_buzzer_bricklet_csharp_examples>`", "Installation"
   "Python", ":ref:`API <piezo_buzzer_bricklet_python_api>`", ":ref:`Examples <piezo_buzzer_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <piezo_buzzer_bricklet_java_api>`", ":ref:`Examples <piezo_buzzer_bricklet_java_examples>`", "Installation"


