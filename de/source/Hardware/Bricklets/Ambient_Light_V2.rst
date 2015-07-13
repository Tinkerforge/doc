
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Ambient Light Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/ambient-light-v2-bricklet.html

.. include:: Ambient_Light_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ambient_light_v2_bricklet:

Ambient Light Bricklet 2.0
==========================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Misst Umgebungslicht bis zu 64000Lux
* Voller Dynamikumfang von 0,01Lux bis 64000Lux
* Ausgabe in 0,01Lux Schritten (16Bit effektive Auflösung)


.. _ambient_light_v2_bricklet_description:

Beschreibung
------------

Mit dem Ambient Light :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` die Umgebungshelligkeit messen.
Es ist der Nachfolger des :ref:`ambient_light_bricklet` mit einem etwa 70x
größeren Messbereich.
Die gemessene Helligkeit kann in `Lux <http://de.wikipedia.org/wiki/Lux>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
Helligkeitsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Bricklet kann genutzt werden um z.B. helligkeitsabhängig Beleuchtungen
oder Motoren zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            LTR329ALS
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beleuchtungsstärke                0Lux - 64000Lux in 0,01Lux Schritten, 16Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           TBDg
================================  ============================================================


Ressourcen
----------

* LTR329ALS Datenblatt (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/raw/master/datasheets/LTR329ALS.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/raw/master/hardware/ambient-light-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ambient_light_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/zipball/master>`__)


.. _ambient_light_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Beleuchtungsstärke in Lux
angezeigt. Der Graph gibt den zeitlichen Verlauf der Beleuchtungsstärke wieder.

Ein guter Test für den Sensor ist es den Raum abzudunkeln und eine Taschenlampe
langsam über den Sensor hinweg zu bewegen. Der resultierende Graph sollte
ungefähr so aussehen wie auf dem folgenden Screenshot.

.. image:: /Images/Bricklets/bricklet_ambient_light_v2_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_v2_brickv.jpg

|test_pi_ref|


.. _ambient_light_v2_bricklet_case:

Gehäuse
-------


.. _ambient_light_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Ambient_Light_V2_hlpi.table
