
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Digital In 4 Bricklet
:shoplink: ../../../shop/bricklets/industrial-digital-in-4-bricklet.html

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_in_4_bricklet:

Industrial Digital In 4 Bricklet
================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_digital_in_4_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_digital_in_4_tilted_600.jpg",
	               "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_vertical_600.jpg",
	             "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_horizontal_600.jpg",
	             "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_setup_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_setup_600.jpg",
	             "Industrial Digital In 4 Bricklet Setup")
	}}
	{{
	    tfdocimg("Cases/bricklet_industrial_case_100.jpg",
	             "Cases/bricklet_industrial_case_600.jpg",
	             "Industrial Digital In 4 Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_brickv.jpg",
	             "Industrial Digital In 4 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_digital_in_4_bricklet_dimensions_100.png",
	             "Dimensions/industrial_digital_in_4_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 digitale Eingänge 
* Eingangsspannung bis zu 36V (DC)
* Galvanisch getrennt
* Gruppierbar


.. _industrial_digital_in_4_bricklet_description:

Beschreibung
------------

Das Industrial Digital In 4 :ref:`Bricklet <primer_bricklets>` kann benutzt werden
um :ref:`Bricks <primer_bricks>` mit vier digitale Eingängen zu erweitern.
Die Eingangsspannung kann bis zu 36 `Volt <http://de.wikipedia.org/wiki/Volt>`__ (DC) betragen.
Die galvanische Trennung der Eingänge erlaubt eine Benutzung ohne direkte elektrische
Verbindung, so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit
gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüber hinaus ist eine Nutzung in Bereichen,
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

Wenn mehr als vier Eingänge benötigt werden kann ein weiteres Industrial Digital In 4
Bricklet mit angeschlossen und gruppiert werden. Anschließend ist es möglich
8 Eingänge simultan zu lesen anstatt zwei mal 4 Eingänge hintereinander zu lesen.
Die Gruppierung kann nur pro Brick erfolgen, so dass an einem Master Brick
maximal 4, an anderen Bricks 2 Industrial Bricklets gruppiert werden können.


Technische Spezifikation
------------------------

================================  =================================================================
Eigenschaft                       Wert
================================  =================================================================
Stromverbrauch                    1mA
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Eingangstyp                       Vier opto-gekoppelte Eingänge (4,7kΩ Vorwiderstand enthalten)
Eingangsstrom                     Abhängig von der Eingangsspannung: ca. 1mA/5V, ca. 5mA/24V
Maximale Eingangsspannung         36V (DC)
Low Level Spannung                0-2V
High Level Spannung               3-36V
Isolation                         5000Vrms (Optokoppler Datenblattangabe)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  =================================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/raw/master/hardware/industrial-digital-in-4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_digital_in_4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Digital In 4 Bricklet besitzt eine 8 Pol Anschlussklemme. 
Diese führt die vier Eingänge nach außen. Jeder Eingang ist mit einer LED
innerhalb des Optokopplers verbunden. Um einen Eingang zu nutzen ist 
dieser wie folgt zu beschalten:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_caption_1200.jpg


.. _industrial_digital_in_4_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Verbinde zusätzlich eine Spannungsquelle mit einem der Bricklet Eingänge
Wir haben eine Batterie für diesen Test genommen (siehe Bild unten).

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet Setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_setup_1200.jpg

|test_tab|

Anschließend sollte der angezeigte Zustand des Eingangs durch An- und Abstecken
der Batterie geändert werden können.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg

|test_pi_ref|

.. _industrial_digital_in_4_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Digital In 4 Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_in_4_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Digital_In_4_hlpi.table
