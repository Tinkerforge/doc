
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Dust Detector Bricklet
:FIXME_shoplink: ../../../shop/bricklets/dust-detector-bricklet.html

.. include:: Dust_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dust_detector_bricklet:

Dust Detector Bricklet
======================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures dust density between 0 and 500µg/m³

.. _dust_detector_bricklet_description:

Description
-----------

The Dust Detector :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure dust density. The measured dust density can be read
out in µg/m³. With configurable events
it is possible to react on changing dust density without polling.

Typical applications are measurements of cigarette smoke, smog,
house dust, pollen, etc.


Technical Specifications
------------------------

=================================  ============================================================
Property                           Value
=================================  ============================================================
Sensor                             GP2Y1010AU
Current Consumption                TBDmA
---------------------------------  ------------------------------------------------------------
---------------------------------  ------------------------------------------------------------
Resolution                         1µg/m³
Measurement Range                  0-500µg/m³
---------------------------------  ------------------------------------------------------------
---------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)             60 x 50 x 20mm (2.36 x 1.97 x 0.79")
Weight                             26g
=================================  ============================================================


Resources
---------

* GP2Y1010AU datasheet (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/raw/master/datasheets/GP2Y1010AU.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/raw/master/hardware/dust-detector-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dust_detector_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/zipball/master>`__)


.. _dust_detector_bricklet_test:

Test your Dust Detector Bricklet
--------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the dust density in µg/m³ and a
graph that shows the dust density over time.

.. image:: /Images/Bricklets/bricklet_dust_detector_brickv.jpg
   :scale: 100 %
   :alt: Dust Detector in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dust_detector_brickv.jpg

|test_pi_ref|


.. _dust_detector_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Dust_Detector_hlpi.table
