:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Humidity Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/humidity-v2-bricklet.html

.. include:: Humidity_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _humidity_v2_bricklet:

Humidity Bricklet 2.0
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_humidity_v2_tilted_[?|?].jpg           Humidity Bricklet 2.0
	Bricklets/bricklet_humidity_v2_horizontal_[?|?].jpg       Humidity Bricklet 2.0
	Bricklets/bricklet_humidity_v2_brickv_[100|].jpg          Humidity Bricklet 2.0 im Brick Viewer
	Dimensions/humidity_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst relative Luftfeuchtigkeit und Temperatur
* Ausgabe in 0,01%RH / 0,01°C Schritten (14Bit Auflösung)
* Internes Heizelement, interne Kompensation


.. _humidity_v2_bricklet_description:

Beschreibung
------------

Mit dem Humidity :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` die `relative Luftfeuchtigkeit
<https://de.wikipedia.org/wiki/Relative_Luftfeuchtigkeit>`__ und 
die `Temperatur <https://de.wikipedia.org/wiki/Temperatur>`__ messen.
Die gemessene Luftfeuchtigkeit kann in Prozent, die Temperatur direkt in °C
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf eine 
veränderte Luftfeuchtigkeit oder Temperatur zu reagieren ohne die Werte 
laufend abzufragen (kein Polling notwendig).

Der Sensor kompensiert die gemessene Luftfeuchtigkeit intern mit dem 
Temperatursensor. Ein per API schaltbares Heizelement, welches direkt im Sensor 
integriert ist, kann dazu genutzt werden um bei extremer Feuchtigkeit den Sensor 
zu trocknen.

Typische Anwendungen sind der Aufbau einer Wetterstation oder in
Umweltmessungen.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            HDC1080
Stromverbrauch                    TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Relative Luftfeuchtigkeit (RH)    0% RH - 100%RH in 0,01%RH Schritten, 14Bit Auflösung
Temperatur                        -20°C- 85°C in 0,01°C Schritten, 14Bit Auflösung
Genauigkeiten                     +-2% (typisch) für Luftfeuchtigkeitsmessung
                                  +-0,2°C (typisch) für Temperaturmessung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           3g
================================  ============================================================


Ressourcen
----------

* HDC1080 Datenblatt (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/raw/master/datasheets/hdc1080.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/raw/master/hardware/humidity-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/humidity_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2yBMQ5P>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/humidity_v2/humidity.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/humidity_v2/humidity.FCStd>`__)

.. _humidity_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessen relative
Luftfeuchtigkeit des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Luftfeuchtigkeit wieder.
Das folgende Bild entstand durch Ausatmen auf den Sensor. Die Luftfeuchtigkeit
steigt durch die feuchte Atemluft und fällt dann wieder ab.

.. image:: /Images/Bricklets/bricklet_humidity_v2_brickv.jpg
   :scale: 100 %
   :alt: Humidity Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_v2_brickv.jpg

|test_pi_ref|


.. _humidity_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Humidity Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Humidity Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Humidity Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png


Troubleshooting
---------------
Bei extremer Feuchtigkeit kann es sein, dass die Messwerte über einen 
längeren Zeitraum verfälscht ausgegeben werden. In diesem Fall kann über 
Aktivierung des internen Heizelements der Sensor getrocknet werden.

Allgemein sollte der Sensor vor direkter Feuchtigkeit geschützt verbaut werden.



.. _humidity_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Humidity_V2_hlpi.table
