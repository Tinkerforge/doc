.. _analog_out_bricklet:

Analog Out Bricklet
===================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_analog_out_tilted_350.jpg",
	               "Bricklets/bricklet_analog_out_tilted_600.jpg",
	               "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_vertical_100.jpg",
	             "Bricklets/bricklet_analog_out_vertical_600.jpg",
	             "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_horizontal_100.jpg",
	             "Bricklets/bricklet_analog_out_horizontal_600.jpg",
	             "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_master_100.jpg",
	             "Bricklets/bricklet_analog_out_master_600.jpg",
	             "Analog Out Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_brickv_100.jpg",
	             "Bricklets/bricklet_analog_out_brickv.jpg",
	             "Analog Out Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/analog_out_bricklet_dimensions_100.png",
	             "Dimensions/analog_out_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Erzeugt konfigurierbare elektrische Spannungen bis zu 5V*
* Angabe in 1mV Schritten (12Bit Auflösung)
* Einstellbarer Lastwiderstand nach Masse


Beschreibung
------------

Das Analog Out :ref:`Bricklet <product_overview_bricklets>` kann genutzt werden
um Bricks mit einem `Digital-Analog-Wandler
<http://de.wikipedia.org/wiki/Digital-Analog-Umsetzer>`__ zu erweitern.
Mit diesem können elektrische Spannungen von 0V bis 5V* generiert werden.
Die Spannung kann direkt in `Volt <http://en.wikipedia.org/wiki/Volt>`__
angegeben werden. Anstatt eine Spannung zu erzeugen kann auch zwischen einem
1k, 100k oder 500k Ohm Lastwiderstand nach Masse (pull-down) gewählt werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
D/A-Wandler                       MCP4725
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Spannung                          0V - 5V* in 1mV Schritten, 12Bit Auflösung
Maximaler Strom                   24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 14mm (1,18 x 0,98 x 0,55")
Gewicht                           6g
================================  ============================================================

\* Die maximale Spannung hängt von der Versorgungsspannung des Bricks ab.
Wird dieses über USB versorgt, so kann es sein, dass 5V nicht erreicht werden
können. Der Grund für diesen Spannungsabfall um 0,5V sind Schutzdioden auf den
Bricks. Wenn 5V Ausgangsspannung benötigt werden kann der Stapel mit einer
zusätzlichen Stromversorgung, wie der :ref:`Step-Down Power Supply <step-down>`,
erweitert werden.


Ressourcen
----------

* MCP4725 Datenblatt (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/hardware/analog-out-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog-out_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-out-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Analog Out Bricklet hat vier Anschlussklemmen für Ausgangssignale.
Zwischen VOUT und GND liegt die einstellbare Ausgangsspannung an. 3,3V und 5V
sind zusätzliche Ausgangssignale mit festen Spannungen.

.. image:: /Images/Bricklets/bricklet_analog_out_vertical_350.jpg
    :scale: 100 %
    :alt: Analog Out Bricklet Anschlussklemmen
    :align: center
    :target: ../../_images/Bricklets/bricklet_analog_out_vertical_1200.jpg


.. _analog_out_bricklet_test:

Teste dein Analog Out Bricklet
------------------------------

Um das Analog Out Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the Analog Out Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable.
(see picture below).

.. image:: /Images/Bricklets/bricklet_analog_out_master_600.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Analog Out Bricklet" auftauchen.
Wähle diesen Tab aus.

In this tab you can configure the voltage on the output pin.
For test purposes, you can measure this voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

.. image:: /Images/Bricklets/bricklet_analog_out_brickv.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_brickv.jpg

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <analog_out_programming_interfaces>` über das
API des Analog Out Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _analog_out_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Analog_Out_hlpi.table
