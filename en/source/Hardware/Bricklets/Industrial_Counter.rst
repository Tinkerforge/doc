
:DISABLED_shoplink: ../../../shop/bricklets/industrial-counter-bricklet.html

.. include:: Industrial_Counter.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_counter_bricklet:

Industrial Counter Bricklet
===========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_counter_tilted_[?|?].jpg           Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_horizontal_[?|?].jpg       Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_master_[100|600].jpg       Industrial Counter Bricklet with Master Brick
	Cases/bricklet_industrial_counter_case_[100|600].jpg             Industrial Counter Bricklet with case
	Bricklets/bricklet_industrial_counter_brickv_[100|].jpg          Industrial Counter Bricklet in Brick Viewer
	Dimensions/industrial_counter_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 channel frequency counter 
* Count, duty cycle, period and frequency per channel
* Frequency range from 0.05Hz to 4MHz


.. _industrial_counter_bricklet_description:

Description
-----------

TBD

The Industrial Counter Bricklet has a 7 pole Bricklet connector and
is connected to a Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               100mW (20mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Input Type                        Four optocoupled inputs (including 2.7kΩ series resistor)
Input Current                     Depending on input voltage, ca. 3.85mA/12V, ca. 8.3mA/24V
Maximum Input Voltage             26V (DC)
Low Level Voltage                 0-2V
High Level Voltage                10-26V
Isolation                         3750Vrms (optocoupler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Minimum Input Frequency           0.05Hz
Maximum Input Frequency           4Mhz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8.4g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-counter-bricklet/raw/master/hardware/industrial-counter-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_counter_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-counter-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each channel).

By default the channel status LEDs are on if the corresponding channel
is high and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.


Duty Cycle Prescaler and Frequency Integration Time
---------------------------------------------------

The Bricklet has two important configurations per channel:


**Duty Cycle Prescaler**: Prescaler for internal clock.

Internally the Bricklet uses a 96MHz clock. The prescaler is a divider for
this internal clock. If the input frequency is too small, the internal
counter can overflow and the frequency measurement becomes distorted. In this
case the prescaler needs to be increased.

If your frequency is above 1465Hz, you can always use a prescaler of 1. If your frequency
is below 1465Hz, you can look at the list below for the prescaler that gives you the
highest resolution for a given frequency.

* 1: minimum frequency 1465Hz, resolution 10.4ns
* 2: minimum frequency 733Hz, resolution 20.8ns
* 4: minimum frequency 367Hz, resolution 41.6ns
* 8: minimum frequency 184Hz, resolution 83.3ns
* 16: minimum frequency 92Hz, resolution 166.6ns
* 32: minimum frequency 46Hz, resolution 333.3ns
* 64: minimum frequency 23Hz, resolution 0.66us
* 12: minimum frequency 12Hz, resolution 1.33us
* 256: minimum frequency 6Hz, resolution 2.66us
* 512: minimum frequency 3Hz, resolution 5.33us
* 1024: minimum frequency 2Hz, resolution 10.66us
* 2048: minimum frequency 0.7Hz, resolution 21.33us
* 4096: minimum frequency 0.36Hz, resolution 42.66us
* 8192: minimum frequency 0.18Hz, resolution 85.33us
* 16384: minimum frequency 0.09Hz, resolution 170.66us
* 32768: minimum frequency 0.045Hz, resolution 341.33us


**Frequency Integration Time**: Time that is used to calculate the frequency.

The frequency is calculated by dividing the integration tine with the
number of edges seen in this time. Example: If the Frequency Integration Time
is set to 2048ms and the Bricklet sees 40960 edge changes in this time, the
resulting frequency is 20kHz (40960 edges divided by 2.048 seconds).

For the frequency integration to work, the frequency integration time
needs to be higher then the period of the measured frequency.

The update rate of the frequency correponds to the Frequency Integration Time.
So a small integration time means that the value is udated more often. If
(for example) you change the Frequency Integration Time to 4096ms, it will take
~4 seconds until you get a proper frequency for the first time and the value
will be updated every 4 seconds.

The resolution of the measured frequency increases with increased integration time:

* 128ms: 7.81 Hz
* 256ms: 3.90 Hz
* 512ms: 1.95 Hz
* 1024ms: 0.98 Hz
* 2048ms: 0.49 Hz
* 4096ms: 0.24 Hz
* 8192ms: 0.12 Hz
* 16384ms: 0.06 Hz
* 32768ms: 0.03 Hz


Count, Duty Cycle, Period, Frequency, Value
-------------------------------------------

The Industrial Counter Bricklet has five different measurements:


**Count**: Is the number of counted edges. The Bricklet can count rising edges, falling edges
or both edges. The direction of the counting (up or down) can be configured. For
channel 0 and 3 it is also possible to use another channel as the input for counting
up or down.

**Duty Cycle**: Is the percentage of time that the signal is high in a cycle.

**Period**: Is the duration of time for one cycle.

**Frequency**: Is the frequency of the signal measured over a longer time period.

**Value**: Is the current value of the channel (either high or low).


Duty Cycle and Period are always given for the last cycle seen. The frequency is calculated
using the configured Frequency Integration Time. If the cycles have a bit of jitter,
the frequency will stay stable while the period and duty cycle will show the jitter.

If the resolution of the period is high enough, the frequency of the signal is
stable and there is no jitter, the frequency will be equal to 1/period.


External Count Direction
------------------------

TBD

.. _industrial_counter_bricklet_test:

Test your Industrial Counter Bricklet
-------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now configure the channels and
see the counter values.

.. image:: /Images/Bricklets/bricklet_industrial_counter_brickv.jpg
   :scale: 100 %
   :alt: Industrial Counter Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_brickv.jpg

|test_pi_ref|


.. _industrial_counter_bricklet_case:

Case
----

..
	A `laser-cut case for the Industrial Counter Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-industrial-counter-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_industrial_counter_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Industrial Counter Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_industrial_counter_case_1000.jpg

	.. include:: Industrial_Counter.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/industrial_counter_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Industrial Counter Bricklet
	   :align: center
	   :target: ../../_images/Exploded/industrial_counter_exploded.png

	|bricklet_case_hint|


.. _industrial_counter_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Counter_hlpi.table
