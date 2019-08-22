
:shoplink: ../../../shop/bricklets/color-bricklet.html

.. include:: Color.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _color_bricklet:

Color Bricklet
==============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_color_tilted_[?|?].jpg           Color Bricklet
	Bricklets/bricklet_color_w_master_[100|600].jpg     Color Bricklet mit Master Brick
	Bricklets/bricklet_color_horizontal_[?|?].jpg       Color Bricklet
	Bricklets/bricklet_color_in_action_[100|600].jpg    Color Bricklet in Aktion
	Bricklets/bricklet_color_brickv_[100|].jpg          Color Bricklet im Brick Viewer
	Dimensions/color_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Color Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`Color Bricklet 2.0 <color_v2_bricklet>`
 empfohlen.


Features
--------

* Misst Farbe (RGB), Farbtemperatur und Beleuchtungsstärke (jeweils 16Bit Auflösung)
* Ausgestattet mit einer schaltbaren LED zur gleichmäßigen Beleuchtung mit definierter Farbtemperatur


.. _color_bricklet_description:

Beschreibung
------------

Mit dem Color :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die 
`Farbe <https://de.wikipedia.org/wiki/Farbe>`__,
`Farbtemperatur <https://de.wikipedia.org/wiki/Farbtemperatur>`__ und die
`Beleuchtungsstärke <https://de.wikipedia.org/wiki/Beleuchtungsst%C3%A4rke>`__ einer
Lichtquelle messen.
Mit dem Bricklet kann somit die Farbe eines Gegenstandes über dessen
reflektiertes Licht gemessen werden.
Um eine gleichmäßige Beleuchtung mit einer definierter Farbtemperatur zu
erhalten ist das Bricklet mit einer API-schaltbaren LED ausgestattet.

Das Bricklet kann für viele Anwendungen genutzt werden, z.B. für das Sortieren
von Objekten nach deren Farbe.

.. image:: /Images/Bricklets/bricklet_color_wavelength_chart_350.jpg
   :scale: 100 %
   :alt: Diagramm Empfindlichkeit / Wellenlängen
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_wavelength_chart_600.jpg

Der Sensor verfügt über interne Farbfilter zur Messung der Farben Rot, Grün und 
Blau (RGB). Die obige Grafik stellt die Empfindlichkeit des Sensors für den 
jeweiligen Farbbereich dar. Neben der Farbinformation (RGB) gibt der Sensor eine
zusätzliche Information aus, genannt "Clear" (C). Dies ist der Sensormesswert 
ohne einen Farbfilter. R,G,B und C sind jeweils 16Bit Werte. Aus diesen 
Informationen berechnet das Bricklet die Helligkeit und die Farbtemperatur 
(ebenfalls jeweils 16Bit).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            TCS34725
Stromverbrauch                    0,2mA (LED aus), 5mA (LED an)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dynamikbereich                    3800000:1
Auflösung Farbe (R,G,B,C)         jeweils 16Bit (0-65535)
Auflösung Farbtemperatur          16Bit (0-65535)
Auflösung Helligkeit              16Bit (0-65535)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 20 x 5mm (0,98 x 0,79 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* TCS3472 Datenblatt (`Download <https://github.com/Tinkerforge/color-bricklet/raw/master/datasheets/TCS34725.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/color-bricklet/raw/master/hardware/color-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/color_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/color-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2kpfpdx>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/color/color.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/color/color.FCStd>`__)



.. _color_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_color_w_master_600.jpg
   :scale: 100 %
   :alt: Color Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_w_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert, sollte das Bricklet auf die jeweilige
Beleuchtung reagieren.

.. image:: /Images/Bricklets/bricklet_color_brickv.jpg
   :scale: 100 %
   :alt: Color Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_brickv.jpg

|test_pi_ref|


Nutzung und Konfiguration
-------------------------

Der Sensor des Bricklets kann konfiguriert werden. Sowohl die Verstärkung 
(Gain) als auch die Integrationszeit (Integration Time) kann eingestellt werden.
Dunkle Umgebungen erfordern eine hohe Verstärkung und/oder eine lange 
Integrationszeit. Durch lange Integrationszeiten wird der Sensor träger, so dass
für schnelle Messungen eine kurze Integrationszeit genutzt werden sollte.

Die einzustellenden Werte hängen von der jeweiligen Anwendung ab. Je nach 
Beleuchtung und Entfernung zum Objekt muss eine andere Parametrierung 
vorgenommen werden. Diese kann über den Brick Viewer erprobt werden.

Für Sortieraufgaben sollte das Bricklet mit einer festen Distanz zum messenden 
Objekt verbaut werden, eine definierte Lichtquelle besitzen (z.B. über 
eingebaute LED) und gegen Fremdlicht geschützt sein.



.. _color_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Color_hlpi.table
