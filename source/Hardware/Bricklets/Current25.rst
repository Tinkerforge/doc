.. _current25_bricklet:

Current25
=========


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

The Current25 :ref:`Bricklet <product_overview_bricklets>` extend the features
of an :ref:`Brick <product_overview_bricks>` by bidirectional current flow
measurments up to 25 Ampere. 
The measured current can be readout in `Ampere <http://en.wikipedia.org/wiki/Ampere>`_ 
directly. Additionally events can be configured, triggered when a specified current is 
exceeded.

Typical applications can be found in robotics. The bidirectional current 
flow measurement is advantageous since you can distinguish between charge and discharge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight
Current Consumption
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            ACS711 25A Version (Allegro Microsystems)
Output: Current                   -25A to 25A, unit 10mA, resolution 12bit
================================  ============================================================

Resources
---------

* ACS711 Datasheet (`Download <https://github.com/Tinkerforge/current25-bricklet/blob/master/datasheets/ACS711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _current25_bricklet_test:

Test your Current25 Bricklet
----------------------------

To test your Current25 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Now you can connect your Current25 Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet.


.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Current25 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg


Additionally connect a circuit to the Bricklet as displayed
in the following image:

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Current25 Bricklet with connected circuit
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg

If you then connect the Brick to the PC over USB,
you should see a tab named "Current25" in the Brick Viewer after you
pressed "connect". 
If everything went as expected you can now see the exact current in ampere 
and a graph that shows the current over time. 


.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Current25 Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg

Click on the Current25 tab and see how the measured values change dependend 
on the current flow through the bricklet. 
You can now go on with writing your own application.
See :ref:`Interface and Coding <current25_programming_interfaces>` section for the API of
the Current25 Bricklet and examples in your programming language.


.. _current25_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <current25_bricklet_c_api>`", ":ref:`Examples <current25_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <current25_bricklet_csharp_api>`", ":ref:`Examples <current25_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <current25_bricklet_java_api>`", ":ref:`Examples <current25_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <current25_bricklet_python_api>`", ":ref:`Examples <current25_bricklet_python_examples>`", "Installation"

