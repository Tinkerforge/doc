
:DISABLED_shoplink: ../../../shop/bricklets/one-wire-bricklet.html

.. include:: One_Wire.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _one_wire_bricklet:

One Wire Bricklet
=================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_one_wire_tilted_[?|?].jpg           One Wire Bricklet
	Bricklets/bricklet_one_wire_horizontal_[?|?].jpg       One Wire Bricklet
	Bricklets/bricklet_one_wire_master_[100|600].jpg       One Wire Bricklet with Master Brick
	Cases/bricklet_one_wire_case_[100|600].jpg             One Wire Bricklet with case
	Bricklets/bricklet_one_wire_brickv_[100|].jpg          One Wire Bricklet in Brick Viewer
	Dimensions/one_wire_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 1-wire communication with any 1-wire capable device
* Uses high-level commands (bus search, reset, write, read)
* Supports 3.3V, 5V and external supply voltage
* Supports up to 64 1-wire devices simultaneously


.. _one_wire_bricklet_description:

Description
-----------

The One-Wire Bricklet can be used to communicate with any `1-wire <https://en.wikipedia.org/wiki/1-Wire>`__
capable device. 

The API uses a set of high-level commands (bus search, reset, write, read, write command). Each
command will give immediat status feedback for easy error detection

Up to 64 devices can be connected to the bus and used at the same time.

A jumper can be used to switch between 3.3V, 5V or an external supply voltage for the
connected 1-wire devices.

An example application would be to read the temperature of a MAX31820
1-wire ambient temperature sensor.

The One Wire Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               35mW (7mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of simultaneous devices    64
Supported voltage                 3.3V, 5V and external supply
Commands                          bus search, reset, write, read, write command
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 14mm (1.18 x 1.18 x 0.55")
Weight                            6.5g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/one-wire-bricklet/raw/master/hardware/one-wire-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/one_wire_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/one-wire-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2KdKuf1>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/one_wire/one-wire.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/one_wire/one-wire.FCStd>`__)



Connectivity
------------

TODO


Example: MAX31820
-----------------

The following example uses Python to read the temperature of a MAX31820
with the API of the One Wire Bricklet::

	ow.write_command(0, 0x4E)     # WRITE SCRATCHPAD
	ow.write(0x00)                # ALARM H (unused)
	ow.write(0x00)                # ALARM L (unused)
	ow.write(0x7F)                # COFIGURATION: 12 bit mode

	while True:
	    ow.write_command(0, 0x44) # CONVERT T (start temperature conversion)
	    time.sleep(1)             # Wait for conversion to finish

	    ow.write_command(0, 0xBE) # READ SCRATCHPAD

	    t_low = ow.read().data    # Read LSB
	    t_high = ow.read().data   # Read MSB
	    print('Temperature: {0} °C'.format((t_low | (t_high << 8))/16.0))


.. _one_wire_bricklet_test:

Test your One Wire Bricklet
---------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now use the
Brick Viewer to communicate with a connected 1-wire device.

.. image:: /Images/Bricklets/bricklet_one_wire_brickv.jpg
   :scale: 100 %
   :alt: One Wire Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_one_wire_brickv.jpg

|test_pi_ref|


.. _one_wire_bricklet_case:

Case
----

..
	A `laser-cut case for the One Wire Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-one-wire-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_one_wire_case_350.jpg
	   :scale: 100 %
	   :alt: Case for One Wire Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_one_wire_case_1000.jpg

	.. include:: One_Wire.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/one_wire_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for One Wire Bricklet
	   :align: center
	   :target: ../../_images/Exploded/one_wire_exploded.png

	|bricklet_case_hint|


.. _one_wire_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: One_Wire_hlpi.table
