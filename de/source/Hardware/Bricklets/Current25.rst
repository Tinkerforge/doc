
.. include:: Current25.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _current25_bricklet:

Current25 Bricklet
==================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_current_tilted_[?|?].jpg             Current25 Bricklet
	Bricklets/bricklet_current_horizontal_[?|?].jpg         Current25 Bricklet
	Bricklets/bricklet_current_vertical_[?|?].jpg           Current25 Bricklet
	Bricklets/bricklet_current_master_[100|600].jpg         Current25 Bricklet mit Master Brick
	Bricklets/bricklet_current25_brickv_[100|].jpg          Current25 Bricklet im Brick Viewer
	Dimensions/current25_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Current25 Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Voltage/Current Bricklet <voltage_current_bricklet>`
 empfohlen.


Features
--------

* Misst elektrische Ströme bis zu **25A**
* Misst die Stromrichtung
* Ausgabe in 1mA Schritten (12Bit Auflösung)


.. _current25_bricklet_description:

Beschreibung
------------

Mit dem Current25 :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` bidirektional Ströme bis zu **25A**
messen. Der gemessene Strom kann direkt in `Ampere
<https://de.wikipedia.org/wiki/Ampere>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Stromänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Mittels einer bidirektionale Strommessungen kann z.B. zwischen Laden und
Entladen eines Akkus unterschieden werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            ACS711 (25A Version)
Stromverbrauch                    5mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Strom                             -25A bis 25A in 1mA Schritten, 12Bit Auflösung
Maximale Eingangsspannung         100VAC/100VDC (Spitzenbelastung)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 14mm (0,98 x 0,98 x 0,55")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* ACS711 Datenblatt (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/datasheets/ACS711.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/current25-bricklet/raw/master/hardware/current-25-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/current25_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/current25-bricklet/zipball/master>`__)


.. _current25_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss noch ein Verbraucher und eine Stromquelle in Reihe mit der
Bricklet in Reihe verbunden werden. Zum Beispiel einen Motor und eine Batterie
wie im folgenden Bild.

.. image:: /Images/Bricklets/bricklet_current_master_600.jpg
   :scale: 100 %
   :alt: Current25 Bricklet mit Batterie und Motor verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_current_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die Stromaufnahme des Motors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Stromaufnahme wieder.

.. image:: /Images/Bricklets/bricklet_current25_brickv.jpg
   :scale: 100 %
   :alt: Current25 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current25_brickv.jpg

Der Screenshot zeigt eine hohe Spitze. Diese wird durch das Anfahren des Motors
beim Anschließen der Batterie verursacht.

|test_pi_ref|


.. _current25_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Current25_hlpi.table
