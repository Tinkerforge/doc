
:DISABLED_shoplink: ../../../shop/bricklets/industrial-analog-out-v2-bricklet.html

.. include:: Industrial_Analog_Out_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_analog_out_v2_bricklet:

Industrial Analog Out Bricklet 2.0
==================================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_analog_out_v2_tilted_[?|?].jpg           Industrial Analog Out Bricklet 2.0
	Bricklets/bricklet_industrial_analog_out_v2_horizontal_[?|?].jpg       Industrial Analog Out Bricklet 2.0
	Bricklets/bricklet_industrial_analog_out_v2_master_[100|600].jpg       Industrial Analog Out Bricklet 2.0 with Master Brick
	Cases/bricklet_industrial_analog_out_v2_case_[100|600].jpg             Industrial Analog Out Bricklet 2.0 with case
	Bricklets/bricklet_industrial_analog_out_v2_brickv_[100|].jpg          Industrial Analog Out Bricklet 2.0 in Brick Viewer
	Dimensions/industrial_analog_out_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Simultaneous programmable voltage and current output
* Outputs voltage between 0V and 10V (IEC 60381-1)
* Outputs current between 0mA and 24mA (IEC 60381-2)
* No external power supply necessary


.. _industrial_analog_out_v2_bricklet_description:

Description
-----------

The Industrial Analog Out :ref:`Bricklet <primer_bricklets>` 2.0
can be used to extend the features of :ref:`Bricks <primer_bricks>`
by the capability to output voltage and current simultaneous.
The voltage can be given in mV and the current in µA.
The device is equipped with a 12-bit `Digital-to-Analog Converter (DAC)
<https://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.

The Industrial Analog Out  Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               DAC7760
Current Consumption               90mW (18mA at 5V, without load)
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

* DAC7760 datasheet (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/raw/master/datasheets/dac7760.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/raw/master/hardware/industrial-analog-out-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_analog_out_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-analog-out-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2NYVTln>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out_v2/industrial-analog-out-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_analog_out_v2/industrial-analog-out-v2.FCStd>`__)


Connectivity
------------

TODO: Update image?

The Industrial Analog Out Bricklet 2.0 has an 8 pole terminal.
Please see the picture below for the pinout.

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_caption_1200.jpg

.. _industrial_analog_out_v2_bricklet_test:

Test your Industrial Analog Out Bricklet 2.0
--------------------------------------------

|test_intro|

|test_connect|.

|test_tab|
In this tab you can enable and configure the voltage on the VOUT terminal or
the current provided by the IOUT terminal.
For test purposes, you can measure this voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

.. image:: /Images/Bricklets/bricklet_industrial_analog_out_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Analog Out Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_analog_out_v2_brickv.jpg

|test_pi_ref|


.. _industrial_analog_out_v2_bricklet_case:

Case
----

A `laser-cut case for the Industrial Analog Out Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Analog_Out_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_analog_out_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Analog_Out_V2_hlpi.table
