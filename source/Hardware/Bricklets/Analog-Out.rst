.. _analog_out_bricklet:

Analog Out
==========

.. note::
   Working in progress. Product will be available soon.

Features
--------

 * Supplies configurable voltages up to 5V\*
 * 12bit resolution
 * Configurable load in power down mode


Description
-----------

The Analog Out :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` by the 
capability to generate voltages between 0V and 5V.
The voltage can be configured directly in `Volt
<http://en.wikipedia.org/wiki/Volt>`_ without any conversion. 
The device is equipped with a 12bit `Digital to Analog Converter (DAC)
<http://en.wikipedia.org/wiki/Digital-to-analog_converter>`_. 
Instead of generating a voltage it is also possible to choose between a 1k, 
100k or 500k Ohm load resistor to ground (pull down).



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 30mm (0.98" x 1.18")
Weight                            TBD
DAC                               12bit DAC, MCP4725
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output: Voltage                   0V - 5V*, unit: mV, max 24mA
================================  ============================================================

.. note::
  \* Max output voltage depends on supply voltage. If the connected Brick is supplied 
  over USB, 5V may not be reached. The reason for this is a voltage drop of up to 0.7V 
  on our products caused by protection diodes. If your supply voltage has for example 4.7V
  then you can output voltages up to 4.5V in practical. If you need higher output voltages
  you have to change your powersupply: Use another USB supply or an Stack supply 
  for example the :ref:`Step Down Powersupply <step-down>`.

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/hardware/analog-out-schematic.pdf>`__)
* MCP4725 Datasheet (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog-out_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/analog-out-bricklet/zipball/master>`__)


Connectivity
------------

The Analog Out Bricklet has four screw terminals. All terminals are only outputs.
Applying an external voltage on them will destroy the connected devices.

.. warning::

  Todo Image

.. _analog_out_bricklet_test:

Test your Analog Out Bricklet
-----------------------------

To test the Analog Out Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Analog Out Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable.
(see picture below).

If you connect the Brick to the PC over USB,
you should see a tab named "Analog Out Bricklet" in the Brick Viewer after you
pressed "connect". Select this tab.
In this tab you can configure the voltage on the output pin.
For test purposes, you can measure this voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <analog_out_programming_interfaces>` section 
for the API of the Analog Out Bricklet and examples in different
programming languages.


.. _analog_out_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <analog_out_bricklet_c_api>`", ":ref:`Examples <analog_out_bricklet_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <analog_out_bricklet_csharp_api>`", ":ref:`Examples <analog_out_bricklet_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <analog_out_bricklet_java_api>`", ":ref:`Examples <analog_out_bricklet_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <analog_out_bricklet_python_api>`", ":ref:`Examples <analog_out_bricklet_python_examples>`", ":ref:`Installation <api_bindings_python>`"

