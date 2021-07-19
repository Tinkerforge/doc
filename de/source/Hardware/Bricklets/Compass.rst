
:shoplink: ../../../shop/bricklets/compass-bricklet.html

.. include:: Compass.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _compass_bricklet:

Compass Bricklet
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_compass_tilted_[?|?].jpg           Compass Bricklet
	Bricklets/bricklet_compass_top_[?|?].jpg              Compass Bricklet
	Bricklets/bricklet_compass_brickv_[100|].jpg          Compass Bricklet im Brick Viewer
	Dimensions/compass_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* 3-Achsen Kompass
* Misst die Himmelsrichtung (0,1° Auflösung / bis zu 1° Genauigkeit)
* Misst die magnetische Flussdichte (Auflösung 0,01µT / Mikrotesla)
* Messfrequenz von bis zu 600Hz


.. _compass_bricklet_description:

Beschreibung
------------

Das Compass :ref:`Bricklet <primer_bricklets>` ist mit einem 3-Achsen ±8 Gauß Magnetsensor
ausgestattet. Der Sensor kann die magnetische Flussdichte für alle drei Achsen messen.
Die Himmelsrichtung wird mit einer Auflösung von 0.1° und einer Genauigkeit von bis zu 1° 
gemessen.

Die Updaterate ist einstellbar und beträgt bis zu 600Hz.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_compass_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_compass_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_compass_video.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

===================================  ============================================================
Eigenschaft                          Wert
===================================  ============================================================
Sensor                               MMC5883MA
Stromverbrauch                       40mW (8mA bei 5V)
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Magnetische Flussdichte Messbereich  -800µT bis 800µT (Mikrotesla)
Magnetische Flussdichte Auflösung    0,01µG (Mikrotesla)
Himmelsrichtung Messbereich          0° bis 360°
Himmelsrichtung Auflösung            0,1°
Himmelsrichtung Genauigkeit          Bis zu 1° bei 100Hz Updaterate*
Updaterate                           100Hz-600Hz (einstellbar)
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)              25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                              2g
===================================  ============================================================

\*: Hängt von der Qualität der Kalibrierung für die spezifische Umgebung des Bricklets ab.


Ressourcen
----------

* MMC5883MA Datenblatt (`Download <https://github.com/Tinkerforge/compass-bricklet/raw/master/datasheets/MMC5883MA-RevC.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/compass-bricklet/raw/master/hardware/compass-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/compass_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/compass-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/33AQJo8>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/compass/compass.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/compass/compass.FCStd>`__)


.. _compass_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun die gemessene magnetische Flussdichte,
der Kurs und die Neigung angezeigt.

.. image:: /Images/Bricklets/bricklet_compass_brickv.jpg
   :scale: 100 %
   :alt: Compass Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_compass_brickv.jpg

|test_pi_ref|


.. _compass_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Compass Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-accelerometer-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Compass Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Compass.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Compass Bricklet
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _compass_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Compass_hlpi.table
