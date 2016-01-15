
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Analog In Bricklet

.. include:: Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_bricklet:

Analog In Bricklet
==================

.. raw:: html

    {% tfgallery %}

	Bricklets/bricklet_analog_in_tilted_[?|?].jpg           Analog In Bricklet
	Bricklets/bricklet_analog_in_vertical_[?|?].jpg         Analog In Bricklet
	Bricklets/bricklet_analog_in_horizontal_[?|?].jpg       Analog In Bricklet
	Bricklets/bricklet_analog_in_master_[100|600].jpg       Analog In Bricklet mit Master Brick
	Cases/bricklet_analog_in_case_build_up_[100|600].jpg    Analog In Bricklet im Gehäuse
	Bricklets/bricklet_analog_in_brickv_[100|].jpg          Analog In Bricklet im Brick Viewer
	Dimensions/analog_in_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Analog In Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Analog In Bricklet 2.0 <analog_in_v2_bricklet>`
 empfohlen.

Features
--------

* Misst elektrische Spannungen bis zu 45V (DC)
* Ausgabe in 1mV Schritten (12Bit Auflösung)
* Hohe Auflösung bis zu 1,48mV


.. _analog_in_bricklet_description:

Beschreibung
------------

Das Analog In :ref:`Bricklet <primer_bricklets>` kann benutzt werden
um :ref:`Bricks <primer_bricks>` die Möglichkeit zu geben elektrische
Spannungen zu messen.
Der Messbereich beträgt 0V bis 45V (DC) mit hoher Auflösung für kleine Spannungen.
Die gemessene Spannung kann direkt in `Volt
<https://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            Automatisch geschalteter Spannungsteiler
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Elektrische Spannung              0V - 45V (DC) in 1mV Schritten, 12Bit Auflösung
Messbereich                       Automatisch geschaltet

                                  * 0V - 6,05V, ~1,48mV Auflösung
                                  * 0V - 10,32V, ~2,52mV Auflösung
                                  * 0V - 36,30V, ~8,86mV Auflösung
                                  * 0V - 45,00V, ~11,25mV Auflösung

                                  Zusätzlich manuell auswählbar

                                  * 0V - 3,30V, ~0,81mV Auflösung
Maximaler Ausgangsstrom           150mA (3,3V), 150mA (5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           30 x 25 x 14mm (1,18 x 0,98 x 0,55")
Gewicht                           6g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/analog-in-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog_in_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-in-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Analog In Bricklet hat vier Anschlussklemmen. Über diese sind folgende
Ausgangssignale verfügbar: 5V, 3,3V sowie GND. Zwischen der VIN Anschlussklemme
und GND kann die zu messende Spannung angelegt werden. Das folgende Bild
zeigt die vier Anschlussklemmen.

.. image:: /Images/Bricklets/bricklet_analog_in_vertical_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_vertical_1200.jpg


.. _analog_in_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine zu messende Gleichspannungsquelle mit dem Bricklet
verbunden werden. Zum Beispiel kann der Pluspol einer Batterie mit der VIN
Anschlussklemme und der Minuspol mit der GND Anschlussklemme verbunden werden.

.. image:: /Images/Bricklets/bricklet_analog_in_master_600.jpg
   :scale: 100 %
   :alt: Analog In Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_brickv.jpg

|test_pi_ref|

.. _analog_in_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Analog In Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-analog-in-out-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_analog_in_case_build_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Analog In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_case_build_up_1000.jpg

.. include:: Analog_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Analog In Bricklet
   :align: center
   :target: ../../_images/Exploded/analog_in_exploded.png

|bricklet_case_hint|


.. _analog_in_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Analog_In_hlpi.table
