
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Color Bricklet
:shoplink: ../../../shop/bricklets/color-bricklet.html

.. include:: Color.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _color_bricklet:

Color Bricklet
==============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_color_tilted_350.jpg",
	               "Bricklets/bricklet_color_tilted_600.jpg",
	               "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_vertical_100.jpg",
	             "Bricklets/bricklet_color_vertical_600.jpg",
	             "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_horizontal_100.jpg",
	             "Bricklets/bricklet_color_horizontal_600.jpg",
	             "Color Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_master_100.jpg",
	             "Bricklets/bricklet_color_master_600.jpg",
	             "Color Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_color_case_built_up_100.jpg",
	             "Cases/bricklet_color_case_built_up_600.jpg",
	             "Color Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_color_brickv_100.jpg",
	             "Bricklets/bricklet_color_brickv.jpg",
	             "Color Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/color_bricklet_dimensions_100.png",
	             "Dimensions/color_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


.. note::
  Diese Bricklet ist noch in Entwicklung!

Features
--------

* Misst Farbe (RGB), Farbtemperatur und Beleuchtungsstärke (jeweils 16Bit Auflösung)
* Ausgestattet mit einer schaltbaren LED zur gleichmäßigen Beleuchtung mit definierter Farbtemperatur


.. _color_bricklet_description:

Beschreibung
------------

Mit dem Color :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die 
`Farbe <http://de.wikipedia.org/wiki/Farbe>`__ , 
`Farbtemperatur <http://de.wikipedia.org/wiki/Farbtemperatur>`__ und die 
`Beleuchtungsstärke <http://de.wikipedia.org/wiki/Beleuchtungsstärke>`__ von Licht messen. 
Mit dem Bricklet kann somit die Farbe des reflektierten Lichts von
Gegenständen gemessen werden.
Um eine gleichmäßige Beleuchtung mit definierter Farbtemperatur zu schaffen
ist das Bricklet mit einer per API schaltbaren LED ausgestattet. 

Das Bricklet kann für viele Anwendungen genutzt werden, z.B. für das Sortieren
von Objekten.

.. image:: /Images/Bricklets/bricklet_color_wavelength_chart_350.jpg
   :scale: 100 %
   :alt: Diagramm Empfindlichkeit / Wellenlängen
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_wavelength_chart_600.jpg

Der Sensor verfügt über interne Farbfilter zur Messung der Farben Rot, Grün und 
Blau (RGB). Die obige Grafik stellt die Empfindlichkeit des Sensors für den 
jeweiligen Farbbereich dar. Neben der Farbinformaton (RGB) gibt der Sensor eine 
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
Stromverbrauch                    TBDmA
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


.. _color_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_color_master_600.jpg
   :scale: 100 %
   :alt: Color Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_master_1200.jpg

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

.. _color_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Color Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-color-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_color_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Color Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_color_case_built_up_1000.jpg

.. include:: Color.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/color_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Color Bricklet
   :align: center
   :target: ../../_images/Exploded/color_exploded.png

|bricklet_case_hint|


.. _color_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Color_hlpi.table
