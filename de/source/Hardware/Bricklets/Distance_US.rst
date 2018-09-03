
:shoplink: ../../../shop/bricklets/distance-us-bricklet.html

.. include:: Distance_US.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_us_bricklet:

Distance US Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_us_tilted_[?|?].jpg           Distance US Bricklet
	Bricklets/bricklet_distance_us_vertical_[?|?].jpg         Distance US Bricklet
	Bricklets/bricklet_distance_us_horizontal_[?|?].jpg       Distance US Bricklet
	Bricklets/bricklet_distance_us_tilted_back_[?|?].jpg      Distance US Bricklet
	Bricklets/bricklet_distance_us_w_sensor_[100|600].jpg     Distance US Bricklet mit Sensor
	Cases/bricklet_distance_us_case_front_[?|?].jpg           Distance US Bricklet im Gehäuse
	Bricklets/bricklet_distance_us_brickv_[100|].jpg          Distance US Bricklet im Brick Viewer
	Dimensions/distance_us_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Distance US Bricklet ist abgekündigt und wird nicht mehr verkauft. Das
 Distance US Bricklet 2.0 befindet sich aktuell noch in der Entwicklung.
 Bis dahin werden als möglicher Ersatz das :ref:`Distance IR Bricklet <distance_ir_bricklet>`
 und das :ref:`Laser Range Finder Bricklet <laser_range_finder_bricklet>`
 empfohlen.


Features
--------

* Misst Entfernungen von 2cm bis 400cm mit Ultraschall
* 12Bit Auflösung


.. _distance_us_bricklet_description:

Beschreibung
------------

Das Distance US :ref:`Bricklet <primer_bricklets>` ist mit einem
`Ultraschall-Entfernungsmesser
<https://de.wikipedia.org/wiki/Entfernungsmessung#Laufzeitmessung>`__
ausgestattet. :ref:`Bricks <primer_bricks>` können hiermit Entfernungen zwischen 
2cm und 400cm messen. Die gemessene Entfernung wird als einheitenloser Wert 
ausgegeben, nicht in mm. Dies liegt daran, dass das Verhältnis von gemessenem 
Entfernungswert zu wirklicher Entfernung vom exakten Wert der 5V 
Versorgungsspannung abhängt. Abweichungen in der Versorgungsspannung führen zu 
Abweichungen in den gemessenen Entfernungswerten.
Mit konfigurierbaren Events ist es möglich auf veränderte Distanzmessung
zu reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            HC-SR04
Stromverbrauch                    8mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Entfernungen                      2cm - 400cm, 12Bit Auflösung
Messwinkel                        15°
Aktualisierungsrate               40Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 20 x 30mm (1,78 x 0,78 x 1,18")
Gewicht                           13g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/distance-us-bricklet/raw/master/hardware/distance-us-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/distance_us_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/distance-us-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2Ie3TvY>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/distance_us/distance_us.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/distance_us/distance_us.FCStd>`__)


.. _distance_us_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Entfernungsmessung angezeigt.

.. image:: /Images/Bricklets/bricklet_distance_us_brickv.jpg
   :scale: 100 %
   :alt: Distance US Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_brickv.jpg

|test_pi_ref|


.. _distance_us_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Distance US Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-distance-us-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_distance_us_case_front_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Distance US Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_distance_us_case_front_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet (jeder lange Abstandshalter besteht aus 2x 9mm und 1x 12mm Stücken),
* baue Seitenteile auf mit Bricklet und Sensor in der Mitte (das Vorderteil ist asymmetrisch, der breitere Rand gehört von außen gesehen nach rechts),
* schraube Unterteil an untere Abstandshalter,
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Distance US Bricklet-Gehäuse:

.. image:: /Images/Exploded/distance_us_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Distance US Bricklet
   :align: center
   :target: ../../_images/Exploded/distance_us_exploded.png

|bricklet_case_hint|


.. _distance_us_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Distance_US_hlpi.table
