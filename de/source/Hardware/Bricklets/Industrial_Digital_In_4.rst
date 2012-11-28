.. include:: Industrial_Digital_In_4.substitutions


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
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_master_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_master_600.jpg",
	             "Industrial Digital In 4 Bricklet mit Master Brick")
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
* Eingangsspannung bis zu 36V
* Galvanisch getrennt


Beschreibung
------------

Das Industrial Digital In 4 :ref:`Bricklet <product_overview_bricklets>` kann benutzt werden
um :ref:`Bricks <product_overview_bricks>` um vier digitale Eingänge zu erweitern.
Die Eingangsspannung kann bis zu 36 `Volt <http://de.wikipedia.org/wiki/Volt>`__ hoch sein. 
Die galvanische Trennung der Eingänge erlaubt eine Benutzung ohne direkte elektrische
Verbindung, so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit
gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüberhinaus ist eine Nutzung in Bereichen, 
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Eingangstyp                       Vier Optokoppler Eingänge (4.7k Ohm Vorwiderstand enthalten)
Eingangsstrom                     Hängt von der Eingangsspannugn ab: ca. 1mA/5V, ca. 5m/24V
Max. Eingangsspannung             36V
Low Level Spannung                0-2V
High Level Spannung               3-36V
Isolation                         5000Vrms (Optokoppler Datenblattangabe)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  ============================================================


Resources
---------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/raw/master/hardware/industrial-digital-in-4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial-digital-in-4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Digital In 4 Bricklet besitzt eine 8 Pol Anschlussklemme. 
Diese führt die vier Eingänge nach außen. Jeder Eingang ist mit einer LED
innerhalb des Optokopplers verbunden. Um einen Eingang zu nutzen ist 
dieser wie folgt zu beschalten:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_vertical_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Steckerbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_vertical_1200.jpg


.. _industrial_digital_in_4_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Verbinde zusätzlich eine Spannungsquelle mit einem der Bricklet Eingänge
Wir haben eine Batterie für diesen Test genommen (siehe Bild unten).

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_master_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_master_1200.jpg

|test_tab|

Anschließend sollte der angezeigte Zustand des Eingangs durch An- und Abstecken
der Batterie geändert werden können.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg

|test_pi_ref|


.. _industrial_digital_in_4_bricklet_programming_interfaces:

Programmierschnittstelle
------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Digital_In_4_hlpi.table
