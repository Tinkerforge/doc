
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Dual Relay Bricklet
:shoplink: ../../../shop/bricklets/dual-relay-bricklet.html

.. include:: Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dual_relay_bricklet:

Dual Relay Bricklet
===================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_dual_relay_tilted_350.jpg",
	               "Bricklets/bricklet_dual_relay_tilted_600.jpg",
	               "Dual Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_horizontal_100.jpg",
	             "Bricklets/bricklet_dual_relay_horizontal_600.jpg",
	             "Dual Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_vertical_100.jpg",
	             "Bricklets/bricklet_dual_relay_vertical_600.jpg",
	             "Dual Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_front_100.jpg",
	             "Bricklets/bricklet_dual_relay_front_600.jpg",
	             "Dual Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_master_100.jpg",
	             "Bricklets/bricklet_dual_relay_master_600.jpg",
	             "Dual Relay Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_brickv_100.jpg",
	             "Bricklets/bricklet_dual_relay_brickv.jpg",
	             "Dual Relay Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dual_relay_bricklet_dimensions_100.png",
	             "Dimensions/dual_relay_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Zwei Relais um AC/DC Geräte zu schalten
* Schaltet bis zu 240VAC/10A und 24VDC/10A


Beschreibung
------------

Mit dem Dual Relay :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um zwei
`Relais <http://de.wikipedia.org/wiki/Relais>`__ erweitert werden.
Jedes Relais besitzt drei Anschlüsse, der mittlere wird zwischen den beiden
äußeren umgeschaltet. Der Schaltzustand wird jeweils durch eine LED angezeigt.

Dieses Bricklet kann benutzt werden um Stromversorgungen, Motoren, Lampen etc.
zu schalten.

Das Schalten induktiver Lasten kann besondere Vorkehrungen erfordern, siehe:
:ref:`Schalten Induktiver Lasten <dual_relay_inductive_load_switching>`.

.. warning::
 Anschlussklemmen und Kontakte sind nicht isoliert. Beim Schalten von hohen
 Spannungen sollte das Dual Relay Bricklet in ein Gehäuse verbaut werden.
 Das Berühren der Kontakte ist potentiell lebensgefährlich!


Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Stromverbrauch pro Relais           60mA
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Schalthäufigkeit                    360 pro Stunde
Maximale Spannung/Strom             | AC: 240V/10A
                                    | DC: 24V/10A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             45 x 45 x 25mm (1,77 x 1,77 x 0,98")
Gewicht                             37g
==================================  ============================================================


Ressourcen
----------

* T7CS5D-05 Datenblatt (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/T7CS5D-05.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Jedes Relais hat drei Anschlüsse: A, SW und B. SW ist mit A oder B verbunden
abhängig vom Schaltzustand des Relais.

* Wenn das Relais ausgeschaltet ist, dann ist SW mit B verbunden
* Wenn das Relais eingeschaltet ist, dann ist SW mit A verbunden

.. image:: /Images/Bricklets/bricklet_dual_relay_connection_350.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet Schaltzustand
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_connection_700.jpg


.. _dual_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_dual_relay_master_600.jpg
   :scale: 100 %
   :alt: Dual Relay verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_brickv.jpg

..
  FIXME: update screenshot and description for monoflop

Durch klicken der beiden Knöpfe werden die Relais umgeschaltet die
ist durch ein Klickgeräusch hörbar und durch LEDs neben den Relais auch sichtbar.

|test_pi_ref|



.. _dual_relay_inductive_load_switching:

Schalten Induktiver Lasten
--------------------------

Ohne externe Beschaltung kann das Schalten induktiver Lasten Störungen im
System verursachen die zu Fehlfunktionen oder Schäden an Komponenten führen
können. Typische Beispiele für induktive Lasten sind Motoren und Spulen im
allgemeinen. Dieses Problem kann z.B. aber auch beim Schalten von
Leuchtstofflampe auftreten.

Um induktive Lasten sicher schalten zu können wird externe Beschaltung z.B. in
Form eines `Varistors <http://de.wikipedia.org/wiki/Varistor>`__ oder der
Kombination eines Widerstandes und eines Kondensators parallel zur Last empfohlen.

Weitere Informationen über Schutzbeschaltung ist
`hier <http://www.jkmicro.com/inductive_loads.pdf>`__ zu finden.




.. _dual_relay_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Dual Relay Bricklet <https://www.tinkerforge.com/de/shop/cases/case-dual-relay-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_1000.jpg

Das Gehäuse des Dual Relay Bricklet wird inklusive Kabelbinder für eine
Zugentlastung und WAGO Verbindungsklemmen zum überbrücken von Leitungen
ausgeliefert. Das Gehäuse ist groß genug um sowohl die Zugentlastung als
auch die WAGO Klemmen im Gehäuse unterzubringen. 

Der interne Aufbau kann wie folgt aussehen (mit einem sowie beiden Relais
angeschlossen)

.. image:: /Images/Cases/bricklet_dual_relay_case_top_open_1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Relay Bricklet mit einem Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_top_open_1_1000.jpg

.. image:: /Images/Cases/bricklet_dual_relay_case_top_open_2_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Relay Bricklet mit zwei Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_top_open_2_1000.jpg

Der Aussenleiter (braun) wird mit dem Dual Relay Bricklet geschaltet 
und der Schutzleiter (grün-gelb) sowie der Neutralleiter (blau) werden
mit den WAGO Klemmen gebrückt.

Dabei ist unbedingt zu beachte, dass der Schutzleiter länger als die anderen
beiden Leitungen seien sollte. Wir empfehlen die folgenden Längen für die
Leitungen und die Abisolierungen:

.. image:: /Images/Cases/bricklet_dual_relay_case_cables_350.jpg
   :scale: 100 %
   :alt: Empfohlene Kabellängen
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_cable_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an Bricklet,
* schraube Bricklet an Unterteil mit Abstandshalter,
* baue Seitenteile (inklusive Zugentlastung) auf,
* stecke zusammengebaute Seitenteile in Unterteil,
* füge Verkabelung und WAGO Klemmen hinzu,
* ziehe Kabel mit Kabelbinder für Zugentlastung fest und
* schraube Oberteul auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Dual Relay Bricklet-Gehäuse:

.. image:: /Images/Exploded/dual_relay_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Dual Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|


.. _dual_relay_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Dual_Relay_hlpi.table
