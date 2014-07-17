
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Solid State Relay Bricklet
:shoplink: ../../../shop/bricklets/solid-state-relay-bricklet.html

.. include:: Solid_State_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _solid_state_relay_bricklet:

Solid State Relay Bricklet
==========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_solid_state_relay_tilted_350.jpg",
	               "Bricklets/bricklet_solid_state_relay_tilted_600.jpg",
	               "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_horizontal_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_horizontal_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_front_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_front_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_master_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_master_600.jpg",
	             "Solid State Relay Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_solid_state_relay_case_100.jpg",
	             "Cases/bricklet_solid_state_relay_case_600.jpg",
	             "Solid State Relay Bricklet Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_brickv_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_brickv.jpg",
	             "Solid State Relay Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/solid_state_relay_bricklet_dimensions_100.png",
	             "Dimensions/solid_state_relay_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


.. note::
  Diese Bricklet ist noch in Entwicklung!

Features
--------

* TODO


.. _solid_state_relay_bricklet_description:

Beschreibung
------------

TODO

Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Stromverbrauch                      TBDmA
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximale Spannung/Strom             TBD
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             TBD: 45 x 45 x 25mm (1,77 x 1,77 x 0,98")
Gewicht                             TBDg
==================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/raw/master/hardware/solid-state-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/solid_state_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

TODO


.. _solid_state_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_solid_state_relay_master_600.jpg
   :scale: 100 %
   :alt: Solid State Relay verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_solid_state_relay_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_solid_state_relay_brickv.jpg
   :scale: 100 %
   :alt: Solid State Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_solid_state_relay_brickv.jpg

Durch klicken der Knöpfe wird das Relais umgeschaltet, der Schaltzustand
kann anhand der LED des Relais nachvollzogen werden.

|test_pi_ref|


.. _solid_state_relay_bricklet_case:

Gehäuse
-------

TODO: FIXME

Ein `laser-geschnittenes Gehäuse für das Solid State Relay Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-solid-state-relay-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_solid_state_relay_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Solid State Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_1000.jpg

Das Gehäuse des Solid State Relay Bricklet wird inklusive Kabelbinder für eine
Zugentlastung und WAGO Verbindungsklemmen zum Verbinden von Leitungen
ausgeliefert. Das Gehäuse ist groß genug um sowohl die Zugentlastung als
auch die WAGO Klemmen im Gehäuse unterzubringen. 

Der interne Aufbau kann wie folgt aussehen (mit einem bzw. beiden Relais
angeschlossen):

.. image:: /Images/Cases/bricklet_solid_state_relay_case_top_open_1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Solid State Relay Bricklet mit einem Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_top_open_1_1000.jpg

.. image:: /Images/Cases/bricklet_solid_state_relay_case_top_open_2_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Solid State Relay Bricklet mit zwei Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_top_open_2_1000.jpg

Der Außenleiter (braun) wird über das Solid State Relay Bricklet geschaltet.
Der Schutzleiter (grün-gelb), sowie der Neutralleiter (blau), werden
mit den WAGO Klemmen durchgeschleift.

Dabei ist unbedingt zu beachten, dass der Schutzleiter länger als die anderen
beiden Leitungen seien sollte. So ist sichergestellt, das dieser bei
überbeanspruchter oder beschädigter Zugentlastung als letztes abreißt.
Wir empfehlen die folgenden Leitungs- bzw. Abisolier-Längen:

.. image:: /Images/Cases/bricklet_solid_state_relay_case_cables_350.jpg
   :scale: 100 %
   :alt: Empfohlene Kabellängen
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_cable_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Abstandshalter an Bricklet schrauben
* Bricklet an Unterteil mit Abstandshalter schrauben
* Seitenteile (inklusive Zugentlastung) aufbauen
* zusammengebaute Seitenteile in Unterteil stecken
* Verkabelung und WAGO Klemmen hinzufügen
* Kabel mit Kabelbinder für Zugentlastung festziehen
* Oberteil auf oberen Abstandshalter schrauben

.. warning:: Niemals im geöffneten Gehäuse unter Spannung arbeiten!


Die genaue Anordnung der Teile kann der folgenden Explosionszeichnung des Dual 
Relay Bricklet-Gehäuses entnommen werden:

.. image:: /Images/Exploded/solid_state_relay_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Solid State Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/solid_state_relay_exploded.png

|bricklet_case_hint|


.. _solid_state_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Solid_State_Relay_hlpi.table
