.. _io4_bricklet:

IO-4 Bricklet
=============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_io4_11_tilted_350.jpg",
	               "Bricklets/bricklet_io4_11_tilted_600.jpg",
	               "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_vertical_100.jpg",
	             "Bricklets/bricklet_io4_11_vertical_600.jpg",
	             "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_horizontal_100.jpg",
	             "Bricklets/bricklet_io4_11_horizontal_600.jpg",
	             "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_master_100.jpg",
	             "Bricklets/bricklet_io4_11_master_600.jpg",
	             "IO-4 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_brickv_100.jpg",
	             "Bricklets/bricklet_io4_brickv.jpg",
	             "IO-4 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/io4_bricklet_dimensions_100.png",
	             "Dimensions/io4_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 digitale Ein- und Ausgänge
* 3,3V Logikspannung
* Konfigurierbare Pull-Ups und Interrupts


Beschreibung
------------

Mit dem IO-4 :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um externe digitale Ein- und Ausgänge
(I/Os) erweitert werden.

Das Bricklet besitzt 4 I/Os die unabhängig voneinander als Ein- oder Ausgänge
konfiguriert werden können. Jeder I/O kann zusätzlich mit Pull-Ups oder als
Interrupt konfiguriert werden. Die I/Os sind über Schraubklemmen nach außen
geführt. Zwei zusätzliche Schraubklemmen führen 3,3V und GND nach außen.

In typischen Anwendungen können Schalter, Taster und LEDs angeschlossen werden

Seit Hardwareversion 1.1 führt eine zusätzliche Schraubklemme 3,3V und GND
nach außen.


Technische Spezifikation
------------------------

================================  =================================================================
Eigenschaft                       Wert
================================  =================================================================
Anzahl I/Os                       4
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
I/O Spannung                      3,3V
Maximaler Ausgangsstrom           6mA
Maximale API Aufrufe*             ``set_value`` (1kHz), ``get_value`` (0,5kHz), Callbacks (1kHz)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Abmessungen (B x T x H)           35 x 35 x 14mm (1,38 x 1,38 x 0,55")
Gewicht                           14g
================================  =================================================================

\* abhängig vom jeweiligen System (Betriebssystem, CPU etc.)


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/io4-bricklet/raw/master/hardware/io-4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/io4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/io4-bricklet/zipball/master>`__)


.. _io4_bricklet_test:

Teste dein IO-4 Bricklet
------------------------

To test the IO-4 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the IO-4 Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable.
In our test we connected an LED with series resistor to the board
by attaching the anode to pin 3 and the cathode to a GND pin.
Additionally we connected a button that can short pin 0 to GND
(see picture below). Starting from hardware version 1.1 you can also
use the GND pins directly beside the data pins.

.. image:: /Images/Bricklets/bricklet_io4_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected IO-4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named
"IO-4 Bricklet" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricklets/bricklet_io4_brickv.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_brickv.jpg

In this tab you can change the "Debounce Period",
it is the debounce time for interrupt callbacks.
For example: If you set this value to 100, you will get interrupts
maximal every 100ms. This is necessary if something that bounces is
connected to the IO-4 Bricklet, such as a button. You can test the optimal
value in the Brick Viewer and use it later in your own program.

Below the debounce period configuration you can configure the pins.
Each pin can be configured as input/output and in case of an input pin
as pull-up. The current state is depicted in the tabular below.

To test the LED we configure pin 3 as output and change
the value. When the pin is high the LED should light up. To test the button
configure pin 0 as input pull-up. We need the pull-up to define a stable
state when the button is not pressed. Now look in the tabular, you should
see that you can change the value of the pin by toggling the button.

If you don't have a button or a LED you can try to measure voltages with
a voltage meter or connect a pin with GND or VCC to see changes in the
Brick Viewer.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <io4_programming_interfaces>` section for
the API of the IO-4 Bricklet and examples in different programming languages.


.. _io4_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: IO4_hlpi.table
