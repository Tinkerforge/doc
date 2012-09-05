.. include:: Piezo_Buzzer.substitutions


.. _piezo_buzzer_bricklet:

Piezo Buzzer Bricklet
=====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_piezo_buzzer_tilted_350.jpg",
	               "Bricklets/bricklet_piezo_buzzer_tilted_600.jpg",
	               "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_vertical_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_vertical_600.jpg",
	             "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_horizontal_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_horizontal_600.jpg",
	             "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_master_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_master_600.jpg",
	             "Piezo Buzzer Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_brickv_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_brickv.jpg",
	             "Piezo Buzzer Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/piezo_buzzer_bricklet_dimensions_100.png",
	             "Dimensions/piezo_buzzer_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Erzeugt 1kHz Piepton
* Konfigurierbare Piepdauer


Beschreibung
------------

Das Piezo Buzzer :ref:`Bricklet <product_overview_bricklets>` ermöglicht es
einem :ref:`Bricks <product_overview_bricks>` akustische Signale abzugeben.
Es können 1kHz Pieptöne in verschiedenen Längen ausgegeben werden.
Die Ausgabe von Morse Codes ist ebenfalls möglich.

Zum Beispiel können mit dieser Platine Zustände signalisiert werden,
wie "Email empfangen".


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Buzzer                            PS1420P02CT
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Piepton                           Frequenz 1kHz, konfigurierbare Dauer
Lautstärke                        63 dB/10cm (laut Datenblatt)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 14mm (0,98 x 0,98 x 0,55")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* PS1420P02CT Datenblatt (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/datasheets/ef532_ps.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/hardware/piezo-buzzer-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/piezo_buzzer_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/zipball/master>`__)


.. _piezo_buzzer_bricklet_test:

Teste dein Piezo Buzzer Bricklet
--------------------------------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_master_600.jpg
   :scale: 100 %
   :alt: Piezo Buzzer Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_brickv.jpg
   :scale: 100 %
   :alt: Piezo Buzzer Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_brickv.jpg

Ein Klick auf den "Send Beep" Knopf erzeugt einen Piepton mit der eingestellten
Dauer.

|test_pi_ref|


.. _piezo_buzzer_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Piezo_Buzzer_hlpi.table
