
:DISABLED_shoplink: ../../../shop/bricklets/energy-monitor-bricklet.html

.. include:: Energy_Monitor.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _energy_monitor_bricklet:

Energy Monitor Bricklet
=======================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_energy_monitor_tilted_[?|?].jpg           Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_horizontal_[?|?].jpg       Energy Monitor Bricklet
	Bricklets/bricklet_energy_monitor_master_[100|600].jpg       Energy Monitor Bricklet with Master Brick
	Cases/bricklet_energy_monitor_case_[100|600].jpg             Energy Monitor Bricklet with case
	Bricklets/bricklet_energy_monitor_brickv_[100|].jpg          Energy Monitor Bricklet in Brick Viewer
	Dimensions/energy_monitor_bricklet_dimensions_[100|600].png  Outline and drilling plan

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
frequency of mains voltage. Additionally the waveform for voltage and
current is provided.

To use the Bricklet you have to connect a current clamp around a single
phase conductor and connect an AC voltage transformer to the same power
line. The Energy Monitor Bricklet will use the low-level voltages
to make the measurements.

The Energy Monitor Bricklet can do all of the measurements without the
need for any exposed mains voltage wiring!

We offer a `230V voltage transformer <TBD>`__ as well as a `5A <TBD>`__ and
`30A current clamp <TBD>`__. The Bricklet comes factory-calibrated for these
transformers.


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
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _energy_monitor_bricklet_connectivity:

Connectivity
------------

TODO: Photos of simple setup with instructions.


.. _energy_monitor_bricklet_waveforms:

Waveforms
---------

The Energy Monitor Bricklet can show the voltage as well as the current
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

Waveform 3: 10W LED lamp. The conductor is threaded through the current clamp eight
times to increase the resolution. This looks like a typical AC/DC power supply.

.. image:: /Images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg
   :scale: 100 %
   :alt: Energy Monitor Bricklet in Brick Viewer (led lamp)
   :align: center
   :target: ../../_images/Bricklets/bricklet_energy_monitor_led_lamp_brickv.jpg

Waveform 3: 12W energy saving lightbulb. The conductor is threaded through the current
clamp eight times to increase the resolution. You can see that the energy saving
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
Connect the voltage and current clamp (see :ref:`energy_monitor_bricklet_connectivity`).

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
