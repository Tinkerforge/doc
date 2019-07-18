
:shoplink: ../../../shop/bricklets/industrial-dual-relay-bricklet.html

.. include:: Industrial_Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_relay_bricklet:

Industrial Dual Relay Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_relay_tilted_[?|?].jpg           Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_front_[?|?].jpg            Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_top_[?|?].jpg              Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_tilted2_[?|?].jpg          Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_side_[?|?].jpg             Industrial Dual Relay Bricklet
	Cases/bricklet_industrial_dual_relay_case_[100|600].jpg             Industrial Dual Relay Bricklet im Gehäuse
	Bricklets/bricklet_industrial_dual_relay_brickv_[100|].jpg          Industrial Dual Relay Bricklet im Brick Viewer
	Dimensions/industrial_dual_relay_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Zwei Relais um AC/DC Geräte zu schalten
* Schaltet bis zu 240VAC/10A und 30VDC/7A


.. _industrial_dual_relay_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual Relay :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um zwei
`Relais <https://de.wikipedia.org/wiki/Relais>`__ erweitert werden.
Jedes Relais besitzt drei Anschlüsse, der mittlere wird zwischen den beiden
äußeren umgeschaltet. Der Schaltzustand wird jeweils durch eine LED angezeigt.
Das Bricklet ist mit umfangreicher Schutzbeschaltung gegen
Störungen durch Schalten induktiver Lasten ausgestattet.

Dieses Bricklet kann benutzt werden um Stromversorgungen, Motoren, Lampen etc.
zu schalten.

Das Schalten induktiver Lasten kann besondere Vorkehrungen erfordern, siehe:
:ref:`Schalten Induktiver Lasten <dual_relay_inductive_load_switching>`.

.. warning::
 Anschlussklemmen und Kontakte sind nicht isoliert. Beim Schalten von hohen
 Spannungen sollte das Dual Relay Bricklet in ein Gehäuse verbaut werden.
 Das Berühren der Kontakte ist potentiell lebensgefährlich!

Das Industrial Dual Relay Bricklet hat einen 7 Pol Bricklet Stecker
und wird mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Relais                              Omron G5LE-1-36
Stromverbrauch                      | 27mw (5.4mA bei 5V) 
                                    | + 350mw (70mA bei 5V) pro aktiviertem Relais
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximale Spannung/Strom             | AC: 240V/10A
                                    | DC: 30V/7A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             40 x 40 x 25mm (1,57 x 1,57 x 0,98")
Gewicht                             29.4g
==================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-relay-bricklet/raw/master/hardware/industrial-dual-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-relay-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2ry2IS8>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_relay/industrial-dual-relay.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_relay/industrial-dual-relay.FCStd>`__)


Anschlussmöglichkeit
--------------------

Jedes Relais hat drei Anschlüsse: A, SW und B. SW ist mit A oder B verbunden
abhängig vom Schaltzustand des Relais.

* Wenn das Relais ausgeschaltet ist, dann ist SW mit B verbunden
* Wenn das Relais eingeschaltet ist, dann ist SW mit A verbunden

.. image:: /Images/Bricklets/bricklet_industrial_dual_relay_connectivity_350.jpg
   :scale: 100 %
   :alt: Industrial Dual Relay Bricklet Anschlussmöglichkeiten
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_relay_connectivity_800.jpg


.. _industrial_dual_relay_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_industrial_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_relay_brickv.jpg

Durch klicken der beiden Knöpfe werden die Relais umgeschaltet. Dies
ist durch ein Klickgeräusch hörbar und durch LEDs neben den Relais auch sichtbar.

|test_pi_ref|


.. _industrial_dual_relay_inductive_load_switching:

Schalten induktiver Lasten
--------------------------

Ohne externe Beschaltung kann das Schalten induktiver Lasten Störungen im
System verursachen, die zu Fehlfunktionen oder Schäden an Komponenten führen
können. Typische Beispiele für induktive Lasten sind Motoren und Spulen im
allgemeinen. Dieses Problem kann z.B. aber auch beim Schalten von
Leuchtstofflampen auftreten.

Um induktive Lasten sicher schalten zu können wird eine externe Beschaltung z.B. in
Form eines `Varistors <https://de.wikipedia.org/wiki/Varistor>`__ oder der
Kombination eines Widerstandes und eines Kondensators parallel zur Last empfohlen.

Weitere Informationen über Schutzbeschaltung ist
`hier <http://www.jkmicro.com/inductive_loads.pdf>`__ zu finden.

.. _industrial_dual_relay_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Dual Relay Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-dual-relay-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_1000.jpg

Das Gehäuse des Industrial Dual Relay Bricklet wird inklusive Kabelbinder für eine
Zugentlastung und WAGO Verbindungsklemmen zum Verbinden von Leitungen
ausgeliefert. Das Gehäuse ist groß genug um sowohl die Zugentlastung als
auch die WAGO Klemmen im Gehäuse unterzubringen. 

Der interne Aufbau kann wie folgt aussehen (mit einem bzw. beiden Relais
angeschlossen):

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual Relay Bricklet mit einem Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top1_1000.jpg

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top2_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual Relay Bricklet mit zwei Relais angeschlossen
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top2_1000.jpg

Der Außenleiter (braun) wird über das Industrial Dual Relay Bricklet geschaltet.
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
   :alt: Explosionszeichnung für Industrial Dual Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|



.. _industrial_dual_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_Relay_hlpi.table
