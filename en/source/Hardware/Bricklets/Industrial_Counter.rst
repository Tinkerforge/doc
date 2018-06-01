
:DISABLED_shoplink: ../../../shop/bricklets/industrial-counter-bricklet.html

.. include:: Industrial_Counter.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_counter_bricklet:

Industrial Counter Bricklet
===========================

.. note::
  This Bricklet is currently work-in-progress!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_counter_tilted_[?|?].jpg           Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_tilted2_[?|?].jpg          Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_side_[?|?].jpg             Industrial Counter Bricklet
	Bricklets/bricklet_industrial_counter_top_[?|?].jpg              Industrial Counter Bricklet
	Cases/bricklet_industrial_counter_case_[100|600].jpg             Industrial Counter Bricklet with case
	Bricklets/bricklet_industrial_counter_brickv_[100|].jpg          Industrial Counter Bricklet in Brick Viewer
	Dimensions/industrial_counter_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 channel galvanically isolated frequency counter 
* Configurable edge count per channel
* Measures duty cycle, period and frequency per channel
* Frequency range from 0.03Hz to 4MHz
* Time resolution up to 10.4ns and frequency resolution up to 0.03Hz

.. _industrial_counter_bricklet_description:

Description
-----------

The Industrial Counter :ref:`Bricklet <primer_bricklets>` can 
be used to extend :ref:`Bricks <primer_bricks>` by four frequency
counter channels.

The Bricklet has an integrated edge counter and it can measure 
duty cycle, period, frequency and value per channel. The frequency can 
be as high as 4MHz.

The edge counter can count rising edges, falling edges or both. The
direction of the count (up or down) is configurable. It is also possible
to use the value of one channel as the direction (e.g. high = up, low = down)
for another channel.

All 4 channels are galvanically isolated.

Example applications for the Bricklet are reading of a PWM signal and
reading of sensors that have edge counts or frequency as output.

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
Minimum Input Frequency           0.03Hz
Maximum Input Frequency           4Mhz
Time resolution                   up to 10.4ns (Duty Cycle Prescaler set to 1)
Frequency resolution              up to 0.03Hz (Frequency Integration Time set to 32768ms)
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
* 3D model (`View online <https://autode.sk/2rzxZ72>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_counter/industrial-counter.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_counter/industrial-counter.FCStd>`__)



.. _industrial_counter_bricklet_channel_status_led:

Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each channel).

By default the channel status LEDs are on if the corresponding channel
is high and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.


.. _industrial_counter_bricklet_duty_cycle_prescaler_and_frequency_integration_time:

Duty Cycle Prescaler and Frequency Integration Time
---------------------------------------------------

The Bricklet has two important configurations per channel:


**Duty Cycle Prescaler**: Prescaler for internal clock.

Internally the Bricklet uses a 96MHz clock. The prescaler is a divider for
this internal clock. If the input frequency is smaller than 1465Hz, the internal
counter can overflow and the frequency measurement becomes distorted. In this
case the prescaler needs to be increased.

If your frequency is above 1465Hz, you can always use a prescaler of 1. If your input frequency
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

The frequency is calculated by dividing the number of edges by the integration time.
Example: If the Frequency Integration Time
is set to 2048ms and the Bricklet sees 40960 edge changes in this time, the
resulting frequency is 20kHz (40960 edges divided by 2.048 seconds).

For the frequency integration to work, the frequency integration time
needs to be higher then the period of the measured frequency.

The update rate of the frequency corresponds to the Frequency Integration Time.
So a small integration time means that the value is updated more often. If
(for example) you change the Frequency Integration Time to 4096ms, it will take
~4 seconds until you get a proper frequency for the first time and the value
will be updated every 4 seconds.

The resolution of the measured frequency increases with increased integration time:

* 128ms: 7.81Hz
* 256ms: 3.90Hz
* 512ms: 1.95Hz
* 1024ms: 0.98Hz
* 2048ms: 0.49Hz
* 4096ms: 0.24Hz
* 8192ms: 0.12Hz
* 16384ms: 0.06Hz
* 32768ms: 0.03Hz


.. _industrial_counter_bricklet_count_duty_period_frequency:

Count, Duty Cycle, Period, Frequency, Value
-------------------------------------------

The Industrial Counter Bricklet has five different measurements:


**Count**: Is the number of counted edges. The Bricklet can count rising edges, falling edges
or both edges. The direction of the counting (up or down) can be configured. For
channel 0 and 3 it is also possible to use another channel as the input for counting
up or down.

**Duty Cycle**: Is the percentage that the signal is high in a cycle.

**Period**: Is the duration of one cycle.

**Frequency**: Is the frequency of the signal measured over a longer time period.

**Value**: Is the current state of the channel (either high or low).


Duty Cycle and Period are always given for the last cycle seen. The frequency is calculated
using the configured Frequency Integration Time. If the cycles have a bit of jitter,
the frequency will stay stable while the period and duty cycle will show the jitter.

If the resolution of the period is high enough, the frequency of the signal is
stable and there is no jitter, the frequency will be equal to 1/period.

Below you can find an oscilloscope screenshot that shows the different measurements of
a 12kHz signal with 60% duty cycle

.. image:: /Images/Bricklets/bricklet_industrial_counter_duty_period_freq.jpg
   :scale: 100 %
   :alt: Count, Duty Cycle, Period and Frequency shown on oscilloscope
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_duty_period_freq.jpg

and the corresponding Brick Viewer screenshot of the same signal connected to the
Industrial Counter Bricklet.

.. image:: /Images/Bricklets/bricklet_industrial_counter_duty_period_freq_brickv.jpg
   :scale: 100 %
   :alt: Count, Duty Cycle, Period and Frequency shown on Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_counter_duty_period_freq_brickv.jpg


.. _industrial_counter_bricklet_external_count_direction:

External Count Direction
------------------------

The count direction (up or down) can be configured and changed on-the-fly for each channel.
Channel 0 additionally supports to use the input of channel 2 as direction. You can configure
channel 0 to count up if the value of channel 2 is high and down if the value is low and the other
way around.

Additionally channel 3 can use channel 1 as direction input in the same manner.

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

A `laser-cut case for the Industrial Counter Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Counter Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Counter.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Counter Bricklet
   :align: center
   :target: ../../_images/Exploded/industria_exploded.png

|bricklet_case_hint|


.. _industrial_counter_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Counter_hlpi.table
