
:shoplink: ../../../shop/bricklets/sound-intensity-bricklet.html

.. include:: Sound_Intensity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _sound_intensity_bricklet:

Sound Intensity Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_sound_intensity_tilted_[?|?].jpg           Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_vertical_[?|?].jpg         Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_horizontal_[?|?].jpg       Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_tilted_back_[?|?].jpg      Sound Intensity Bricklet
	Cases/bricklet_sound_intensity_case_tilted_[?|?].jpg          Sound Intensity Bricklet im Gehäuse
	Bricklets/bricklet_sound_intensity_brickv_[100|].jpg          Sound Intensity Bricklet im Brick Viewer
	Dimensions/sound_intensity_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Sound Intensity Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`Sound Pressure Level Bricklet <sound_pressure_level_bricklet>`
 empfohlen.


Features
--------

* Misst Schallintensität
* 12Bit Auflösung
* Einsetzbar als Klatschschalter, Alarmanlagen-Sensor, u.v.m.


.. _sound_intensity_bricklet_description:

Beschreibung
------------

Das Sound Intensity :ref:`Bricklet <primer_bricklets>` ist mit einer
Mikrofonkapsel ausgestattet und es kann genutzt werden um die Lautstärke 
mit :ref:`Bricks <primer_bricks>` zu messen.
Der zurückgegebene Wert entspricht der `Hüllkurve
<https://de.wikipedia.org/wiki/H%C3%BCllkurvendemodulator>`__ des Signals der
Mikrofonkapsel.

Es ist möglich Events zu konfigurieren die ausgelöst werden, wenn eine
spezifizierte Lautstärkeschwelle überschritten wird.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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

|test_connect|.

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

.. image:: /Images/Cases/bricklet_sound_intensity_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_intensity_case_tilted_1000.jpg

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


.. _sound_intensity_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Sound_Intensity_hlpi.table
