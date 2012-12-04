.. include:: Industrial_Quad_Relay.substitutions


.. _industrial_quad_relay_bricklet:

Industrial Quad Relay Bricklet
==============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_quad_relay_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_quad_relay_tilted_600.jpg",
	               "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_vertical_600.jpg",
	             "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_horizontal_600.jpg",
	             "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_setup_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_setup_600.jpg",
	             "Industrial Quad Relay Bricklet Setup")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_brickv.jpg",
	             "Industrial Quad Relay Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_quad_relay_bricklet_dimensions_100.png",
	             "Dimensions/industrial_quad_relay_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 Solid State Relais
* Schaltet bis zu 30V mit 1,2A
* Galvanisch getrennt
* Gruppierbar


Beschreibung
------------

Das Industrial Quad Relay :ref:`Bricklet <product_overview_bricklets>` kann benutzt werden
um :ref:`Bricks <product_overview_bricks>` mit vier galvanisch getrennten Solid State Relais
zu erweitern. Jedes Relais kann bis zu 1,2 `Ampere <http://en.wikipedia.org/wiki/Ampere>`__
mit 30 `Volt <http://en.wikipedia.org/wiki/Volt>`__ schalten. 
Die Isolierung des Ausgangs erlaubt eine Nutzung one eine direkte elektrische Verbindung, 
so dass Masseschleifen vermieden werden können und eine zusätzliche Sicherheit gewährleistet wird.

Typische Anwendungen lassen sich in der Steuerung von industriellen Produkten,
wie z.B. SPS oder Frequenzumrichter, finden. Darüberhinaus ist eine Nutzung in Bereichen, 
bei denen verschiedene Massepotentiale nicht verbunden werden dürfen sinnvoll.

Wenn mehr als vier Relais benötigt werden kann ein weiteres Industrial Quad Relay
Bricklet mit angeschlossen und gruppiert werden. Anschließend ist es möglich
8 Relais simultan zu setzen anstatt zwei mal 4 Relais hintereinander zu setzen.
Die Gruppierung kann nur pro Brick erfolgen, so dass an einem Master Brick
maximal 4, an anderen Bricks 2 Industrial Bricklets gruppiert werden können.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Ausgangstyp                       Vier galvanisch getrennte Solid State Relais
Max. Schaltstrom                  1.2A
Max. Schaltspannung               30V
Isolation                         1500Vrms (Datenblattangabe)
Relais Typ                        CPC1020N
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/hardware/industrial-quad-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_quad_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Industrial Quad Relay Bricklet besitzt eine 8 Pol Anschlussklemme.
Das nachfolgende Bild erklärt die Pinbelegung:

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 Pinbelegung
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_caption_1200.jpg


.. _industrial_quad_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Für einen einfachen Test werden wir eine Batterie und eine LED anschließen (siehe nachfolgendes Bild).


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet Setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_setup_1200.jpg

|test_tab|

Anschließend sollte die LED über den Brick Viewer geschalten werden können.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg

|test_pi_ref|


.. _industrial_quad_relay_bricklet_programming_interfaces:

Programmierschnittstelle
------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte Beschreibung.

.. include:: Industrial_Quad_Relay_hlpi.table
