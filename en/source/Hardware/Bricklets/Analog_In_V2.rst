
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Analog In Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/analog-in-v2-bricklet.html

.. include:: Analog_In_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_v2_bricklet:

Analog In Bricklet 2.0
======================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures voltages up to 42V (DC)
* Full-scale resolution of ~10mV

.. _analog_in_v2_bricklet_description:

Description
-----------

The Analog In :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the capability to
measure voltages. The voltage can be read out in `Volt
<https://en.wikipedia.org/wiki/Volt>`__ directly without conversions necessary.

With configurable events it is possible to react on changing
voltages without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 42V (DC) in 1mV steps, 12bit resolution (~10mV)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 14mm (1.38 x 1.18 x 0.55")
Weight                            TBDg
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/raw/master/hardware/analog-in-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_in_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/zipball/master>`__)


Connectivity
------------

The Analog In Bricklet 2.0 has five terminals. With these terminals you can
access the following output signals: 5V, 3.3V as well as GND. The voltage you
want to measure can be applied between the VIN and the GND terminal.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_vertical_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 2.0 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_vertical_1200.jpg


.. _analog_in_v2_bricklet_test:

Test your Analog In Bricklet 2.0
--------------------------------

|test_intro|

|test_connect|.
Additionally connect a DC voltage you want to measure to the Bricklet. For
testing purposes connect the 5V or 3.3V output terminal to the VIN terminal.
The GND terminals are already connected internally.

|test_tab|
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_brickv.jpg

|test_pi_ref|


.. _analog_in_v2_bricklet_case:

Case
----


.. _analog_in_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_In_V2_hlpi.table
