
:shoplink: ../../../shop/bricklets/industrial-analog-out-bricklet.html

.. include:: Industrial_Analog_Out.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_analog_out_bricklet:

Industrial Analog Out Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_analog_out_tilted_[?|?].jpg           Industrial Analog Out Bricklet
	Bricklets/bricklet_industrial_analog_out_horizontal_[?|?].jpg       Industrial Analog Out Bricklet
	Bricklets/bricklet_industrial_analog_out_brickv_[100|].jpg          Industrial Analog Out Bricklet in Brick Viewer
	Dimensions/industrial_analog_out_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Simultaneous programmable voltage and current output
* Outputs voltage between 0V and 10V (IEC 60381-1)
* Outputs current between 0mA and 24mA (IEC 60381-2)
* No external power supply necessary


.. _industrial_analog_out_bricklet_description:

Description
-----------

The Industrial Analog Out :ref:`Bricklet <primer_bricklets>`
can be used to extend the features of :ref:`Bricks <primer_bricks>`
by the capability to output voltage and current simultaneous.
The voltage can be given in mV and the current in µA.
The device is equipped with a 12-bit `Digital-to-Analog Converter (DAC)
<https://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               DAC7760
Current Consumption               65mW (13mA at 5V, without load)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        up to 1.2mV / 4.8µA

Voltage Ranges                    * 0V - 5V
                                  * 0V - 10V

Current Ranges                    * 4mA - 20mA
                                  * 0mA - 20mA
                                  * 0mA - 24mA

VOUT Output                       up to 30mA
12V Supply Output                 up to 100mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            9g
================================  ============================================================


Resources
---------

* DAC7760 datasheet (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/datasheets/dac7760.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/hardware/industrial-analog-out-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_analog_out_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2iW0W8F>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out/industrial-analog-out.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out/industrial-analog-out.FCStd>`__)

Connectivity
------------

The Industrial Analog Out Bricklet has an 8 pole terminal.
Please see the picture below for the pinout.

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_caption_1200.jpg


.. _industrial_analog_out_bricklet_test:

Test your Industrial Analog Out Bricklet
----------------------------------------

|test_intro|

|test_connect|.

|test_tab|
In this tab you can enable and configure the voltage on the VOUT terminal or
the current provided by the IOUT terminal.
For test purposes, you can measure this voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_brickv.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_brickv.jpg

|test_pi_ref|


.. _industrial_analog_out_bricklet_case:

Case
----

A `laser-cut case for the Industrial Analog Out Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Analog Out Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Analog_Out.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Analog Out Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_analog_out_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Analog_Out_hlpi.table
