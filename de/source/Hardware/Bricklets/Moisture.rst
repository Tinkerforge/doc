
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Moisture Bricklet
:shoplink: ../../../shop/bricklets/moisture-bricklet.html

.. include:: Moisture.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _moisture_bricklet:

Moisture Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_moisture_v11_tilted1_350.jpg",
	               "Bricklets/bricklet_moisture_v11_tilted1_600.jpg",
	               "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_v11_horizontal_100.jpg",
	             "Bricklets/bricklet_moisture_v11_horizontal_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_v11_tilted2_100.jpg",
	             "Bricklets/bricklet_moisture_v11_tilted2_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_moisture_v11_case_built_up_100.jpg",
	             "Cases/bricklet_moisture_v11_case_built_up_600.jpg",
	             "Moisture Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_plant1_100.jpg",
	             "Bricklets/bricklet_moisture_plant1_600.jpg",
	             "Moisture Bricklet in Erde einer Pflanze")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_plant2_100.jpg",
	             "Bricklets/bricklet_moisture_plant2_600.jpg",
	             "Moisture Bricklet in Erde einer Pflanze")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_brickv_100.jpg",
	             "Bricklets/bricklet_moisture_brickv.jpg",
	             "Moisture Bricklet im Brick Viewer")
	}}
	{{ tfdocend() }}

..
	{{
	    tfdocimg("Dimensions/moisture_bricklet_v11_dimensions_100.png",
	             "Dimensions/moisture_bricklet_v11_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Erdfeuchtigkeit
* 12Bit Auflösung


.. _moisture_bricklet_description:

Beschreibung
------------

Das Moisture :ref:`Bricklet <primer_bricklets>` erweitert 
:ref:`Bricks <primer_bricks>` und ist dafür gedacht die Feuchtigkeit in Erde
zu ermitteln. Es kann aber auch zum Messen des Füllstands eines Wasserbehälters
genutzt werden.

Seit Hardwareversion 1.1 wird eine kapazitive Messmethode verwendet, da die
alte Messmethode im offenen Metallkontakten in Hardwareversion 1.0
:ref:`Korrosionsprobleme <moisture_bricklet_corrosion>` hatte.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    < 5mW (< 1mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Auflösung                         12Bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 86 x 5mm (0,99 x 3,39 x 0,2")
Gewicht                           5g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/moisture-bricklet/raw/master/hardware/moisture-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/moisture_bricklet_v11_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/moisture-bricklet/zipball/master>`__)


.. _moisture_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun die Änderung des
Feuchtegrades angezeigt.

.. image:: /Images/Bricklets/bricklet_moisture_brickv.jpg
   :scale: 100 %
   :alt: Moisture Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_brickv.jpg

|test_pi_ref|


.. _moisture_bricklet_corrosion:

Korrosionsprobleme bei Hardwareversion 1.0
------------------------------------------

Hardwareversion 1.0 des Moisture Bricklets verwendete eine Messmethode mit
offenen Metallkontakten, die bei einigen Kunden zu Korrosionsproblemen führte.
Daher wurde in Hardwareversion 1.1 auf eine kapazitive Messmethode gewechselt,
die keine offenen Metallkontakte verwendet und aher keine Korrosionsprobleme
habe kann.

.. image:: /Images/Bricklets/bricklet_moisture_tilted_350.jpg
   :scale: 100 %
   :alt: Moisture Bricklet Hardwareversion 1.0
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_tilted_1000.jpg


.. _moisture_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Moisture Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-moisture-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_moisture_v11_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Moisture Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_v11_case_built_up_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* baue Seitenteile auf mit Bricklet und Sensor in der Mitte,
* schraube Unterteil an untere Abstandshalter,
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Moisture Bricklet-Gehäuse:

.. image:: /Images/Exploded/moisture_v11_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Moisture Bricklet
   :align: center
   :target: ../../_images/Exploded/moisture_v11_exploded.png

|bricklet_case_hint|


.. _moisture_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Moisture_hlpi.table
