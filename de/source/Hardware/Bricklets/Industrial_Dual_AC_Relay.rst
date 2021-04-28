
:shoplink: ../../../shop/bricklets/industrial-dual-ac-relay-bricklet.html

.. include:: Industrial_Dual_AC_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_ac_relay_bricklet:

Industrial Dual AC Relay Bricklet
=================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_ac_relay_tilted_[?|?].jpg           Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_front_[?|?].jpg            Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_top_[?|?].jpg              Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_tilted2_[?|?].jpg          Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_side_[?|?].jpg             Industrial Dual AC Relay Bricklet
	Cases/bricklet_industrial_dual_ac_relay_case_[100|600].jpg             Industrial Dual AC Relay Bricklet im Gehäuse
	Bricklets/bricklet_industrial_dual_ac_relay_brickv_[100|].jpg          Industrial Dual AC Relay Bricklet im Brick Viewer
	Dimensions/industrial_dual_ac_relay_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Zwei Solid State Relais um AC Geräte zu schalten
* Schaltet bis zu 240VAC/1,2A (mit max 12A Spitzenstrom)
* Schwingungspaketsteuerung (Schaltung während zero-crossing)


.. _industrial_dual_ac_relay_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual AC Relay :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um zwei 
`Solid State Relais (SSR) <https://de.wikipedia.org/wiki/Relais#Halbleiterrelais>`__
erweitert werden.
Jedes Relais besitzt zwei Anschlüsse. Der Schaltzustand wird jeweils durch eine LED angezeigt.

Dieses Bricklet kann benutzt werden um Stromversorgungen, Motoren, Lampen etc.
zu schalten.

.. warning::
 Anschlussklemmen und Kontakte sind nicht isoliert. Beim Schalten von hohen
 Spannungen sollte das Dual AC Relay Bricklet in ein Gehäuse verbaut werden.
 Das Berühren der Kontakte ist potentiell lebensgefährlich!

Das Industrial Dual AC Relay Bricklet hat einen 7 Pol Bricklet Stecker
und wird mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Relais                              Panasonic AQH3213A
Stromverbrauch                      | 25mW (5mA bei 5V)
                                    | + 60mW (12mA bei 5V) pro aktiviertem Relais
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximale Spannung/Strom             AC: 240V/1,2A (mit max 12A Spitzenstrom)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                             11g
==================================  ============================================================


Ressourcen
----------

* AQH3213A Solid State Relay (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/raw/master/hardware/industrial-dual-ac-relay-schematic.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/raw/master/hardware/industrial-dual-ac-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_ac_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2ry2IS8>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_relay/industrial-dual-ac-relay.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_relay/industrial-dual-ac-relay.FCStd>`__)


Anschlussmöglichkeit
--------------------

TODO

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_relay_connectivity_350.jpg
   :scale: 100 %
   :alt: Industrial Dual AC Relay Bricklet Anschlussmöglichkeiten
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_relay_connectivity_800.jpg


.. _industrial_dual_ac_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual AC Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_relay_brickv.jpg

Durch klicken der beiden Knöpfe werden die Relais umgeschaltet. Dies
ist durch die LEDs neben dem Bricklet ersichtbar.

|test_pi_ref|


.. _industrial_dual_ac_relay_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Dual Relay Bricklet und Industria Dual AC Relay Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-dual-ac-relay-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual AC Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_1000.jpg

Das Gehäuse des Industrial Dual AC Relay Bricklet wird inklusive Kabelbinder für eine
Zugentlastung und WAGO Verbindungsklemmen zum Verbinden von Leitungen
ausgeliefert. Das Gehäuse ist groß genug um sowohl die Zugentlastung als
auch die WAGO Klemmen im Gehäuse unterzubringen. 

Der interne Aufbau kann wie folgt aussehen (mit einem bzw. beiden Relais
angeschlossen):

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual AC Relay Bricklet mit einem Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top1_1000.jpg

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top2_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual AC Relay Bricklet mit zwei Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top2_1000.jpg

Der Außenleiter (braun) wird über das Industrial Dual AC Relay Bricklet geschaltet.
Der Schutzleiter (grün-gelb), sowie der Neutralleiter (blau), werden
mit den WAGO Klemmen durchgeschleift.

Dabei ist unbedingt zu beachten, dass der Schutzleiter länger als die anderen
beiden Leitungen seien sollte. So ist sichergestellt, das dieser bei
überbeanspruchter oder beschädigter Zugentlastung als letztes abreißt.
Wir empfehlen die folgenden Leitungs- bzw. Abisolier-Längen:

.. image:: /Images/Cases/bricklet_dual_relay_case_cables_350.jpg
   :scale: 100 %
   :alt: Empfohlene Kabellängen
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_cables_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Abstandshalter an Bricklet schrauben
* Bricklet an Unterteil mit Abstandshalter schrauben
* Seitenteile (inklusive Zugentlastung) aufbauen
* zusammengebaute Seitenteile in Unterteil stecken
* Verkabelung und WAGO Klemmen hinzufügen
* Kabel mit Kabelbinder für Zugentlastung festziehen
* Oberteil auf oberen Abstandshalter schrauben

.. warning:: Niemals im geöffneten Gehäuse unter Spannung arbeiten!


Die genaue Anordnung der Teile kann der folgenden Explosionszeichnung des Industrial Dual 
Relay Bricklet-Gehäuses entnommen werden:

.. image:: /Images/Exploded/dual_relay_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Dual AC Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|



.. _industrial_dual_ac_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_AC_Relay_hlpi.table
