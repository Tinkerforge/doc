
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Sound Intensity Bricklet
:FIXME_shoplink: ../../../shop/bricklets/sound-intensity-bricklet.html

.. include:: Sound_Intensity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _sound_intensity_bricklet:

Sound Intensity Bricklet
========================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_sound_intensity_tilted_350.jpg",
	               "Bricklets/bricklet_sound_intensity_tilted_600.jpg",
	               "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_vertical_100.jpg",
	             "Bricklets/bricklet_sound_intensity_vertical_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_horizontal_100.jpg",
	             "Bricklets/bricklet_sound_intensity_horizontal_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_master_100.jpg",
	             "Bricklets/bricklet_sound_intensity_master_600.jpg",
	             "Sound Intensity Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_brickv_100.jpg",
	             "Bricklets/bricklet_sound_intensity_brickv.jpg",
	             "Sound Intensity Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/sound_intensity_bricklet_dimensions_100.png",
	             "Dimensions/sound_intensity_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Schallintensität
* 12Bit Auflösung
* Einsetzbar als Klatschschalter, Alarmanlagen-Sensor, u.v.m.

Beschreibung
------------

Das Sound Intensity :ref:`Bricklet <product_overview_bricklets>` ist mit einer
Mikrofonkapsel ausgestattet und es kann genutzt werden um Lautstärke zu messen.
Der zurückgegebene Wert entspricht der `Hüllkurve
<http://de.wikipedia.org/wiki/Hüllkurvendemodulator>`__ des Signals der
Mikrofonkapsel.

Es ist möglich Events zu konfigurieren die ausgelöst werden wenn eine
spezifizierte Lautstärkenschwelle überschritten wird.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Auflösung                         12Bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 30 x 9mm (0,98 x 1,18 x 0,35")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/raw/master/hardware/sound-intensity-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/sound_intensity_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/zipball/master>`__)


.. _sound_intensity_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_sound_intensity_master_600.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird nun die aktuelle Lautstärke
angezeigt.

.. image:: /Images/Bricklets/bricklet_sound_intensity_brickv.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_brickv.jpg

|test_pi_ref|

.. _sound_intensity_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Sound Intensity Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-sound-intensity-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_sound_intensity_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_intensity_case_built_up_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Bricklet an Oberteil mit Abstandshalter von unten und den langen Schrauben von oben,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Oberteil und
* schraube Unterteil auf unteren Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Sound Intensity Bricklet-Gehäuse:

.. image:: /Images/Exploded/sound_intensity_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Exploded/sound_intensity_exploded.png

|bricklet_case_hint|


.. _sound_intensity_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Sound_Intensity_hlpi.table
