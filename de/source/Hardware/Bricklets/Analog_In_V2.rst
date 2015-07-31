
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Analog In Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/analog-in-v2-bricklet.html

.. include:: Analog_In_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_v2_bricklet:

Analog In Bricklet 2.0
======================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Misst elektrische Spannungen bis zu 42V (DC)
* Auflösung über den gesamten Messbereich von ~10mV


.. _analog_in_v2_bricklet_description:

Beschreibung
------------

Das Analog In :ref:`Bricklet <primer_bricklets>` 2.0 kann benutzt werden
um :ref:`Bricks <primer_bricks>` die Möglichkeit zu geben elektrische
Spannungen zu messen. Es ist der Nachfolger des :ref:`analog_in_bricklet`.
Die gemessene Spannung kann direkt in `Volt
<https://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.

Mit konfigurierbaren Events ist es möglich auf Spannungsänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    30mW (6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Elektrische Spannung              0V - 42V (DC) in 1mV Schritten, 12Bit Auflösung (~10mV)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           35 x 30 x 14mm (1,38 x 1,18 x 0,55")
Gewicht                           8g
================================  ============================================================

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/raw/master/hardware/analog_in-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/analog_in_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/analog-in-v2-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Analog In Bricklet 2.0 hat fünf Anschlussklemmen. Über diese sind folgende
Ausgangssignale verfügbar: 5V, 3,3V sowie GND. Zwischen der VIN Anschlussklemme
und GND kann die zu messende Spannung angelegt werden.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_horizontal_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 2.0 Anschlussklemmen
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_horizontal_1200.jpg


.. _analog_in_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Als nächstes muss eine zu messende Gleichspannungsquelle mit dem Bricklet
verbunden werden. Als Test kann z.B. die 5V oder 3,3V Anschlussklemme mit der
VIN Anschlussklemme verbunden werden. Die beiden GND Anschlussklemmen sind
intern schon verbunden.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_analog_in_v2_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_v2_brickv.jpg

|test_pi_ref|


.. _analog_in_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Analog In Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-analog-in-out-v2-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_analog_in_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_v2_case_built_up_1000.jpg

.. include:: Analog_In_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Analog In Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/analog_in_v2_exploded.png

|bricklet_case_hint|


.. _analog_in_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Analog_In_V2_hlpi.table
