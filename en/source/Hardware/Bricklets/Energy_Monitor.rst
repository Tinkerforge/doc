
:shoplink: ../../../shop/bricklets/energy-monitor-bricklet.html

.. include:: Energy_Monitor.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _energy_monitor_bricklet:

Energy Monitor Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_energy_monitor_tilted_[?|?].jpg                          Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_top_[?|?].jpg                             Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_w_transformer_[?|?].jpg                   Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_heater_brickv_[100|].jpg                  Energy Monitor Bricklet in Brick Viewer
	Bricklets/bricklet_energy_monitor_led_lamp_brickv_[100|].jpg                Energy Monitor Bricklet in Brick Viewer
	Bricklets/bricklet_energy_monitor_fan_brickv_[100|].jpg                     Energy Monitor Bricklet in Brick Viewer
	Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv_[100|].jpg Energy Monitor Bricklet in Brick Viewer
	Dimensions/energy_monitor_bricklet_dimensions_[100|600].png                 Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Enables energy monitoring of mains voltage (120V/230V AC)
* Measures voltage (V), current (A) and energy (Wh)
* Measures real/apparent/reactive power (W/VA/VAR)
* Measures power factor and frequency (Hz)
* Voltage and current waveform are provided


.. _energy_monitor_bricklet_description:

Description
-----------

The Energy Monitor :ref:`Bricklet <primer_bricklets>` is equipped with
a 3.5mm jack plug for a current transformer and a 3.5mm OD/1.35mm ID barrel
plug for a voltage transformer. The transformer voltages are used to calculate
voltage, current, energy, real/apparent/reactive power, power factor and
frequency of mains voltage of a single phase conductor. 
Additionally the waveform for voltage and current is provided.

The Energy Monitor Bricklet can do all of the measurements without the
need for any exposed mains voltage wiring!

To use the Bricklet you have to connect a current transformer clamp around 
a single phase conductor and connect an AC voltage transformer to the same power
line. The Energy Monitor Bricklet will use the low-level output voltages of the
transformers to make the measurements. This ensures that the Bricklet is safe to
handle, since no mains voltage has a direct connection to the Bricklet.

We offer a `230V voltage transformer <https://www.tinkerforge.com/en/shop/ac-ac-voltage-transformer.html>`__
as well as a `5A current transformer clamp <https://www.tinkerforge.com/en/shop/5a-1v-current-transformer-clamp.html>`__
or `30A current transformer clamp <https://www.tinkerforge.com/en/shop/30a-1v-current-transformer-clamp.html>`__.
The Bricklet comes factory-calibrated for these transformers.

The Energy Monitor Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               50mW (10mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Input Voltage                     Max 12V AC from voltage transformer
Input Current                     Max 1V AC from current transformer
Connector Voltage                 3.5mm jack plug (audio jack)
Connector Current                 3.5mm OD with 1.35mm ID barrel plug
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 5mm (1.57 x 1.57 x 0.2")
Weight                            7g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/energy-monitor-bricklet/raw/master/hardware/energy-monitor-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/energy_monitor_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/energy-monitor-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/31FfjlR>`__ | Download: `STEP <https://download.tinkerforge.com/3d/energy_monitor/energy_monitor.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/energy_monitor/energy_monitor.FCStd>`__)


.. _energy_monitor_bricklet_example_heater:

Example: Monitor Power Usage of Heater
--------------------------------------

.. warning::

 Never work on live mains electrical wiring. Remove the mains connection before you
 cut the wire or add the current transformer or similar!

As an example we want to monitor the power of a small electric heater.

To do this we have to connect the voltage transformer and the current transformer
clamp to the same circuit that the electric heater runs on.

A typical european mains power cable will have three wires:

* Neutral conductor (N)
* Protective earth (PE)
* Phase (L)

In case of three-phase power there are two more phases (L2 and L3). If you want to
measure the power for a three-phase system you have to use three Bricklets, for each phase one.
Each Bricklet has to be equipped with its own voltage and current transformer for its phase.

In our single phase example, the current transformer clamp has to be connected to L. For
that the wire has to be passed through the current transformer. You can open the current transformer
for that. It is absolutly important that only L is passed through the transformer.
If you for example pass N and L through it, you will not be able to measure the
current.

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_2_600.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet heater example
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_2_1200.jpg

On the Bricklet side you have to connect the clamp to the *AC Current* input.

Put the AC/AC voltage transformer into a socket that is as near to the load that you want
to monitor as possible.

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_3_600.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet heater example, photo 2
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_3_1200.jpg

On the Bricklet side you have to connect the transformer to the *AC Voltage* input.

The resulting setup will look like this:

.. image:: /Images/Bricklets/bricklet_energy_monitor_tutorial_1_800.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet heater example, photo 3
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_tutorial_1_1200.jpg

In the Brick Viewer this setup looks as follows:

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (heater)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg




Transformer Ratios
------------------

Both transformers (the voltage transformer and the current transformer) that
are connected to the Energy Monitor Bricklet have a ratio.

The current transformers that we sell are 5A:1V and 30A:1V, while the voltage
transformer delivers about 12V without load and 230V input. The voltage
is higher than specified (9V) since no current is flowing while connected
to the Bricklet. We measured an exact ratio of 19.23V:1V.

The Bricklet has a default current ratio of 30 and a default voltage ratio
of 19.23. You can change the ratios in Brick Viewer:

.. image:: /Images/Bricklets/bricklet_energy_monitor_brickv_ratios.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet ratio configuration
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_brickv_ratios.jpg

If you use the 5A:1V current transformer, change the current ratio to 5.

If you use your own current transformer or voltage transformer, you
have to measure the ratio and change it accordingly in Brick Viewer.


Increase Current Measurement Resolution
---------------------------------------

Current Transformer measure the current in a wire by measuring its
magnetic field (see 
`Wikipedia Current Transformer <https://en.wikipedia.org/wiki/Current_transformer>`__).
You can increase the resolution of the current measurement by passing
the wire through the current transformer multiple times.

.. image:: /Images/Bricklets/bricklet_energy_monitor_multiwire_600.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet with wires passed through multiple times
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_multiwire_1200.jpg

TODO Picture current transformer with multiple times passed trough wire 

The ratio changes accordingly:

* 2-times passed through: Ratio factor 2
* 3-times passed through: Ratio factor 3
* etc.

If the real current becomes too high, the measurement will be cut off.
The measurement is not correct anymore, but the Bricklet can not be damaged by
this. The same is true if the current transformer ratio is too high

Passing the wire multiple times through the transformer will 
increase the noise. If available, it is the better to choose a 
matching transformer.

.. _energy_monitor_bricklet_waveforms:

Waveforms
---------

The Energy Monitor Bricklet can deliver the voltage as well as the current
waveform. The voltage waveform should always look sinusoidal, while the
current waveform can heavily vary depending on the measured load. Below
you can see waveforms for four different loads.

Waveform 1: 1.7kW electric heater.

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (heater)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg

Waveform 2: 125W fan.

.. image:: /Images/Bricklets/bricklet_energy_monitor_fan_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (fan)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_fan_brickv.jpg

Waveform 3: 10W LED lamp. The conductor is threaded through the current transformer clamp eight
times to increase the resolution. This looks like a typical AC/DC power supply.

.. image:: /Images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (LED lamp)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg

Waveform 4: 12W energy saving lightbulb. The conductor is threaded through the current
transformer clamp eight times to increase the resolution. You can see that the energy saving
lightbulb only uses about 1/4 of the waveform.

.. image:: /Images/Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (energy saving lightbulb)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_energy_saving_lightbulb_brickv.jpg


.. _energy_monitor_bricklet_test:

Test your Energy Monitor Bricklet
---------------------------------

|test_intro|

|test_connect|.

|test_tab|
Connect the voltage and current transformer clamp.

You can now see the voltage/current waveforms as well as the voltage, current, power factor,
frequency, energy and real/apparent/Reactive power.

.. image:: /Images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_heater_brickv.jpg

The current waveform heavily depends on the measured load (see :ref:`energy_monitor_bricklet_waveforms`).

|test_pi_ref|


.. _energy_monitor_bricklet_case:

Case
----

..
	A `laser-cut case for the Energy Monitor Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-energy-monitor-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_energy_monitor_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Energy Monitor Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_energy_monitor_case_1000.jpg

	.. include:: Energy_Monitor.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/energy_monitor_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Energy Monitor Bricklet
	   :align: center
	   :target: ../../_images/Exploded/energy_monitor_exploded.png

	|bricklet_case_hint|


.. _energy_monitor_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Energy_Monitor_hlpi.table
