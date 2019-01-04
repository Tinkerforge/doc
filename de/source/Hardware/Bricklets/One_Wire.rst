
:shoplink: ../../../shop/bricklets/one-wire-bricklet.html

.. include:: One_Wire.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _one_wire_bricklet:

One Wire Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_one_wire_tilted_[?|?].jpg           One Wire Bricklet
	Bricklets/bricklet_one_wire_tilted2_[?|?].jpg          One Wire Bricklet
	Bricklets/bricklet_one_wire_top_[?|?].jpg              One Wire Bricklet
	Bricklets/bricklet_one_wire_brickv_[100|].jpg          One Wire Bricklet im Brick Viewer
	Dimensions/one_wire_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 1-Wire Kommunikation mit allen 1-wire kompatiblen Geräten
* Bietet High-Level-Befehle (Bus Search, Reset, Write, Read, Write Command)
* Unterstützt 3,3V, 5V und externe Versorgungsspannung
* Bis zu 64 1-Wire Geräte gleichzeitig anschließbar


.. _one_wire_bricklet_description:

Beschreibung
------------

Das One-Wire Bricklet ermöglicht die Kommunikation mit
`1-wire <https://de.wikipedia.org/wiki/1-Wire>`__ kompatiblen Geräten .

Die API stellt verschiedene High-Level-Befehle (Bus Search, Reset, Write, Read,
Write Command) bereit, die direkt den Status zurückmelden und einfache
Fehlererkennung ermöglichen.

Bis zu 64 1-Wire Geräte können gleichzeitig angeschlossen und genutzt werden.

Ein Jumper kann genutzt werden um zwischen 3,3V, 5V und einer externen
Stromversorgung für das 1-Wire Gerät zu wechseln.

Eine Beispielanwendung für das Bricklet wäre z.B. das Bestimmen der
Temperatur mit einem MAX31820 1-Wire Temperatursensors.

Das Bricklet verfügt über keine galvanische Trennung zum Tinkerforge System. 
Das heißt es gibt eine direkte elektrische Verbindung zwischen den 
Anschlussklemmen des Bricklets und dem restlichen System. Sollte dies in der 
jeweiligen Anwendung zu ungewollten Verbindungen, Masseschleifen oder 
Kurzschlüssen führen, so ist der Einsatz zusammen mit einem :ref:`Isolator Bricklet <isolator_bricklet>` ratsam.

Das One Wire Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    35mW (7mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Busgröße                 64
Unterstüzte Spannungen            3,3V, 5V und externe Versorgung
Befehle                           Bus Search, Reset, Write, Read, Write Command
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 30 x 14mm (1,18 x 1,18 x 0,55")
Gewicht                           6,5g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/one-wire-bricklet/raw/master/hardware/one-wire-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/one_wire_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/one-wire-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2KdKuf1>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/one_wire/one-wire.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/one_wire/one-wire.FCStd>`__)


Anschlussmöglichkeit
--------------------

Ein 1-Wire Gerät kann mit VCC/DAT/GND (Spannung, Daten, Masse) verbunden werden

Der Jumper kann genutzt werden um die Stromversorgung auf der VCC-Klemme zwischen 3,3
und 5V zu wechseln. Wenn der Jumper auf NC gesetzt wird, kann eine externe Stromversorgung
an VCC angeschlossen werden. Wenn eine externe Stromversorgung verwendet wird darf
der Jumper nicht auf 3,3V/5V gesetzt werden.

.. image:: /Images/Bricklets/bricklet_one_wire_top_350.jpg
   :scale: 100 %
   :alt: One Wire Bricklet Anschlussmöglichkeiten
   :align: center
   :target: ../../_images/Bricklets/bricklet_one_wire_top_1200.jpg


Beispiel: MAX31820
------------------

Das folgende Python Beispiel ließt über das One Wire Bricklet die Temperatur
eines angeschlossenen MAX31820 Temperatursensors aus:

.. code-block:: python

    ow.write_command(0, 0x4E)     # WRITE SCRATCH PAD
    ow.write(0x00)                # ALARM H (unused)
    ow.write(0x00)                # ALARM L (unused)
    ow.write(0x7F)                # CONFIGURATION: 12 bit mode

    while True:
        ow.write_command(0, 0x44) # CONVERT T (start temperature conversion)
        time.sleep(1)             # Wait for conversion to finish

        ow.write_command(0, 0xBE) # READ SCRATCH PAD

        t_low = ow.read().data    # Read LSB
        t_high = ow.read().data   # Read MSB

        print('Temperature: {0} °C'.format((t_low | (t_high << 8)) / 16.0))


.. _one_wire_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| und ein 1-Wire Gerät an das Bricklet angeschlossen werden.

|test_tab|
Wenn alles wie erwartet funktioniert kann jetzt mit dem angeschlossenen
1-Wire Gerät kommuniziert werden.

.. image:: /Images/Bricklets/bricklet_one_wire_brickv.jpg
   :scale: 100 %
   :alt: One Wire Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_one_wire_brickv.jpg

|test_pi_ref|


.. _one_wire_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das One Wire Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-load-cell-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_load_cell_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für One Wire Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_load_cell_case_built_up1_1000.jpg

.. include:: One_Wire.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/one_wire_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für One Wire Bricklet
   :align: center
   :target: ../../_images/Exploded/one_wire_exploded.png

|bricklet_case_hint|


.. _one_wire_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: One_Wire_hlpi.table
