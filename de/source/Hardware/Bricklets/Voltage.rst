.. _voltage_bricklet:

Voltage Bricklet
================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_voltage_tilted_350.jpg",
	               "Bricklets/bricklet_voltage_tilted_600.jpg",
	               "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_vertical_100.jpg",
	             "Bricklets/bricklet_voltage_vertical_600.jpg",
	             "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_horizontal_100.jpg",
	             "Bricklets/bricklet_voltage_horizontal_600.jpg",
	             "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_master_100.jpg",
	             "Bricklets/bricklet_voltage_master_600.jpg",
	             "Voltage Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_brickv_100.jpg",
	             "Bricklets/bricklet_voltage_brickv.jpg",
	             "Voltage Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_bricklet_dimensions_100.png",
	             "Dimensions/voltage_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Spannungen bis zu 50V
* Ausgabe in 1mV Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Voltage :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Spannungen messen.
Über eine Schraubklemme wird das Bricklet mit der zu messenden Spannung
verbunden. Der Messbereicht beträgt 0-50V. Die gemessene Spannung kann direkt
in `Volt <http://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.
Zusätzlich können Events definiert werden die ausgelöst werden wenn eine
bestimmte Spannung über- oder unterschritten wird.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            Spannungsteiler mit Faktor 0,0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Spannung                          0V - 50V in 1mV Schritten, 12Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 14mm (0,98 x 0,98 x 0,55")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/voltage-bricklet/raw/master/hardware/voltage-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/voltage_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/voltage-bricklet/zipball/master>`__)


.. _voltage_bricklet_test:

Teste dein Voltage Bricklet
---------------------------

Um das Voltage Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the Voltage Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable.
Additionally connect a voltage source to the Bricklet.
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricklets/bricklet_voltage_master_600.jpg
   :scale: 100 %
   :alt: Voltage Bricklet mit Batterie verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Voltage Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected you can now see the voltage in volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_voltage_brickv.jpg
   :scale: 100 %
   :alt: Voltage Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_brickv.jpg

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <voltage_programming_interfaces>` über das
API des Voltage Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _voltage_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Voltage_hlpi.table
