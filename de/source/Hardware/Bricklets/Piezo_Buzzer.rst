
.. include:: Piezo_Buzzer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _piezo_buzzer_bricklet:

Piezo Buzzer Bricklet
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_piezo_buzzer_tilted_[?|?].jpg           Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_vertical_[?|?].jpg         Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_horizontal_[?|?].jpg       Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_master_[100|600].jpg       Piezo Buzzer Bricklet mit Master Brick
	Bricklets/bricklet_piezo_buzzer_brickv_[100|].jpg          Piezo Buzzer Bricklet im Brick Viewer
	Dimensions/piezo_buzzer_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Piezo Buzzer Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Piezo Speaker Bricklet 2.0 <piezo_speaker_v2_bricklet>`
 empfohlen.


Features
--------

* Erzeugt 1kHz Piepton
* Konfigurierbare Piepdauer


.. _piezo_buzzer_bricklet_description:

Beschreibung
------------

Das `Piezo Buzzer <https://de.wikipedia.org/wiki/Summer_(Elektrik)>`__
:ref:`Bricklet <primer_bricklets>` ermöglicht es
einem :ref:`Bricks <primer_bricks>` akustische Signale abzugeben.
Es können 1kHz Pieptöne in verschiedenen Längen ausgegeben werden.
Die Ausgabe von `Morsezeichen <https://de.wikipedia.org/wiki/Morsezeichen>`__
ist ebenfalls möglich.

Zum Beispiel können mit dieser Platine Zustände signalisiert werden,
wie "E-Mail empfangen".


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Buzzer                            PS1420P02CT
Stromverbrauch                    1mA
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

Erster Test
-----------

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


.. _piezo_buzzer_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Piezo_Buzzer_hlpi.table
