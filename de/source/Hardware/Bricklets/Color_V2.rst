
:DISABLED_shoplink: ../../../shop/bricklets/color-v2-bricklet.html

.. include:: Color_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _color_v2_bricklet:

Color Bricklet 2.0
==================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_color_v2_tilted_[?|?].jpg           Color Bricklet 2.0
	Bricklets/bricklet_color_v2_top_[?|?].jpg              Color Bricklet 2.0
	Bricklets/bricklet_color_v2_brickv_[100|].jpg          Color Bricklet 2.0 im Brick Viewer
	Dimensions/color_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Farbe (RGB), Farbtemperatur und Beleuchtungsstärke (jeweils 16Bit Auflösung)
* Ausgestattet mit einer schaltbaren LED zur gleichmäßigen Beleuchtung mit definierter Farbtemperatur


.. _color_v2_bricklet_description:

Beschreibung
------------

Mit dem Color :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` die 
`Farbe <https://de.wikipedia.org/wiki/Farbe>`__,
`Farbtemperatur <https://de.wikipedia.org/wiki/Farbtemperatur>`__ und die
`Beleuchtungsstärke <https://de.wikipedia.org/wiki/Beleuchtungsst%C3%A4rke>`__ einer
Lichtquelle messen.
Mit dem Bricklet kann somit die Farbe eines Gegenstandes über dessen
reflektiertes Licht gemessen werden.
Um eine gleichmäßige Beleuchtung mit einer definierter Farbtemperatur zu
erhalten, ist das Bricklet mit einer API-schaltbaren LED ausgestattet.

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

Das Color Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_color_v2_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_color_v2_button_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_color_v2_button_video.webm" type="video/webm">
	</video>


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            TCS34725
Stromverbrauch                    LED aus: 30mW (6mA bei 5V), LED an 50mW (10mA bei 5V)
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
* Schaltplan (`Download <https://github.com/Tinkerforge/color-v2-bricklet/raw/master/hardware/color-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/color_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/color-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2z3hIux>`__ | Download: `STEP <https://download.tinkerforge.com/3d/color_v2/color_v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/color_v2/color_v2.FCStd>`__)


.. _color_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert können nun die gemessenen Werte, 
abhängig von der Helligkeit betrachtet werden.

	.. image:: /Images/Bricklets/bricklet_color_v2_brickv.jpg
	   :scale: 100 %
	   :alt: Color Bricklet 2.0 im Brick Viewer
	   :align: center
	   :target: ../../_images/Bricklets/bricklet_color_v2_brickv.jpg

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


.. _color_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Color_V2_hlpi.table
