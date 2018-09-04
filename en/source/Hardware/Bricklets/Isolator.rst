
:DISABLED_shoplink: ../../../shop/bricklets/isolator-bricklet.html

.. include:: Isolator.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _isolator_bricklet:

Isolator Bricklet
=================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_isolator_tilted_[?|?].jpg           Isolator Bricklet
	Bricklets/bricklet_isolator_horizontal_[?|?].jpg       Isolator Bricklet
	Bricklets/bricklet_isolator_master_[100|600].jpg       Isolator Bricklet with Master Brick
	Cases/bricklet_isolator_case_[100|600].jpg             Isolator Bricklet with case
	Bricklets/bricklet_isolator_brickv_[100|].jpg          Isolator Bricklet in Brick Viewer
	Dimensions/isolator_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Galvanically isolates the power and data lines
* Can be used between any Brick and any Bricklet with a 7 pole connector


.. _isolator_bricklet_description:

Description
-----------

The Isolator :ref:`Bricklet <primer_bricklets>` can
`galvanically isolate <https://en.wikipedia.org/wiki/Galvanic_isolation>`__ the
power and data lines between any Brick and any Bricklet with a 7 pole connector.

Any Bricklet that does analog/digital input/output may benefit from galvanic
isolation, for example:

* :ref:`Analog Out 3.0 <analog_out_v3_bricklet>`
* :ref:`CAN 2.0 <can_v2_bricklet>`
* :ref:`DMX <dmx_bricklet>`
* :ref:`Industrial Analog Out 2.0 <industrial_analog_out_v2_bricklet>`
* :ref:`Industrial Counter <industrial_counter_bricklet>`
* :ref:`Industrial Dual 0-20mA 2.0 <industrial_dual_0_20ma_v2_bricklet>`
* :ref:`Industrial Dual Analog In 2.0 <industrial_dual_analog_in_v2_bricklet>`
* :ref:`Industrial Dual Relay <industrial_dual_relay_bricklet>`
* :ref:`IO-16 2.0 <io16_v2_bricklet>`
* :ref:`IO-4 2.0 <io4_v2_bricklet>`
* :ref:`Load Cell 2.0 <load_cell_v2_bricklet>`
* :ref:`One Wire <one_wire_bricklet>`
* :ref:`PTC 2.0 <ptc_v2_bricklet>`
* :ref:`RS232 2.0 <rs232_v2_bricklet>`
* :ref:`RS485 <rs485_bricklet>`
* :ref:`Thermocouple 2.0 <thermocouple_v2_bricklet>`
* :ref:`Voltage/Current 2.0 <voltage_current_v2_bricklet>`

The Isolator Bricklet has two 7 pole Bricklet connectors. It is connected to a
Brick with a ``7p-10p`` Bricklet cable on one side and to a Bricklet with a
``7p-7p`` Bricklet cable on the other side.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               280mW (56mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Isolation Voltage Power Supply    3kV (1s), 60V (continous)*
Isolation Voltage Data            2.5kV (ESD), 600V (60s), 200V (continous)*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 40 x 15 (1.18 x 1.58 x 0.59")
Weight                            7.1g
================================  ============================================================

\*: See datasheet of MAX14850 for details of data isolation and of CRE1S0505S3C for details of power isolation.

Resources
---------

* MAX14850 datasheet (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/datasheets/MAX14850.pdf>`__)
* CRE1S0505S3C datasheet (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/datasheets/CRE1S0505S3C.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/isolator-bricklet/raw/master/hardware/isolator-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/isolator_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/isolator-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2NYVE9E>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/isolator/isolator.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/isolator/isolator.FCStd>`__)


Example
-------

TODO: Image of example application

.. _isolator_bricklet_test:

Test your Isolator Bricklet
---------------------------

|test_intro|

|test_connect| and the Bricklet that you want to isolate to the Isolator Bricklet.

|test_tab|
If everything went as expected you can now see the Isolator Bricklet
as well as the isolated Bricklet in Brick Viewer.

.. image:: /Images/Bricklets/bricklet_isolator_brickv.jpg
   :scale: 100 %
   :alt: Isolator Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_isolator_brickv.jpg

|test_pi_ref|


.. _isolator_bricklet_case:

Case
----

..
	A `laser-cut case for the Isolator Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-isolator-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_isolator_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Isolator Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_isolator_case_1000.jpg

	.. include:: Isolator.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/isolator_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Isolator Bricklet
	   :align: center
	   :target: ../../_images/Exploded/isolator_exploded.png

	|bricklet_case_hint|


.. _isolator_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Isolator_hlpi.table
