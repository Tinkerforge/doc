
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Load Cell Bricklet
:FIXME_shoplink: ../../../shop/bricklets/load-cell-bricklet.html

.. include:: Load_Cell.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _load_cell_bricklet:

Load Cell Bricklet
==================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures output of load cells
* 24bit ADC for high resolution
* Up to 80 weight measurements per second


.. _load_cell_bricklet_description:

Description
-----------

The Load Cell :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure load cells.
Only a single known weight is required to calibrate the load cell.
It is possible to measure weight differences of few grams in objects that
weigh many kilograms.

Load cells with different maximum weights are available in the shop:

* `Load Cell 5kg <TBD>`
* `Load Cell 20kg <TBD>`
* `Load Cell 50kg <TBD>`

The Bricklet has an LED that can be turned on trough the API, e.g. to show
that a weight measurement is in range.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HX711
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        24bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 14mm (1.18 x 1.18 x 0.55")
Weight                            7g
================================  ============================================================

Resources
---------

* HX711 datasheet (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/datasheets/hx711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/hardware/load-cell-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/load_cell_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/load-cell-bricklet/zipball/master>`__)


.. _load_cell_bricklet_connectivity:

Connectivity
------------

The Load Cell Bricklet has four terminals. The PWR and GND terminals are for
the excitation voltage and the IN+ and IN- terminals are for the signal
measurement.

.. image:: /Images/Bricklets/bricklet_load_cell_vertical_350.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_vertical_1200.jpg

A typical load cell will have four or five wires. Check the specification of
your load cell for its pinout and connect it according to the table below.

============== ================ ================================================
Connection     Terminal         Possible Wire Colors
============== ================ ================================================
Excitation +   PWR              red
Excitation -   GND              black, yellow
Signal +       IN+              green, blue
Signal -       IN-              white
============== ================ ================================================

If you put weight onto the load cell on the end with the arrow facing down you
should get a positive weight reading. If you get a negative weight reading then
you need to switch the signal wires connected to the IN+ and IN- terminals.


.. _load_cell_bricklet_test:

Test your Load Cell Bricklet
----------------------------

|test_intro|

|test_connect|.
Additionally :ref:`connect <load_cell_bricklet_connectivity>` and
:ref:`calibrate <load_cell_bricklet_calibration>` a load cell.

|test_tab|
If everything went as expected you can now see the weight in gram
and a graph that shows the weight over time.

.. image:: /Images/Bricklets/bricklet_load_cell_brickv.jpg
   :scale: 100 %
   :alt: Load Cell Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_load_cell_brickv.jpg

|test_pi_ref|


.. _load_cell_bricklet_calibration:

Calibration
-----------

The Load Cell Bricklet has to be calibrated for the connected load cell and the
specific setup.

Connect a load cell to the Bricklet as described :ref:`above
<load_cell_bricklet_connectivity>`. Then start Brick Viewer and click the
"Calibration" button on the "Load Cell Bricklet" tab. With no weight on the
load cell, click the "Calibrate Zero" button. Now put a known weight on the
load cell, enter the known weight in gram as the "Current Weight", then click
the "Calibrate Weight" button.

Now the Load Cell Bricklet is calibrated for the connected load cell and the
specific setup.


.. _load_cell_bricklet_case:

Case
----


.. _load_cell_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Load_Cell_hlpi.table
