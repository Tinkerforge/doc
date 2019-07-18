
:shoplink: ../../../shop/bricklets/dual-relay-bricklet.html

.. include:: Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dual_relay_bricklet:

Dual Relay Bricklet
===================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_relay_12_tilted_[?|?].jpg        Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_12_horizontal_[?|?].jpg    Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_12_front_[?|?].jpg         Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_master_[100|600].jpg       Dual Relay Bricklet mit Master Brick
	Cases/bricklet_dual_relay_case_[100|600].jpg             Dual Relay Bricklet Gehäuse
	Bricklets/bricklet_dual_relay_brickv_[100|].jpg          Dual Relay Bricklet im Brick Viewer
	Dimensions/dual_relay_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Dual Relay Bricklet ist abgekündigt. Wir verkaufen noch unseren restlichen Lagerbestand.
 Als Ersatz wird das :ref:`Industrial Dual Relay Bricklet <industrial_dual_relay_bricklet>`
 empfohlen.


Features
--------

* Zwei Relais um AC/DC Geräte zu schalten
* Schaltet bis zu 240VAC/10A und 30VDC/7A


.. _dual_relay_bricklet_description:

Beschreibung
------------

Mit dem Dual Relay :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um zwei
`Relais <https://de.wikipedia.org/wiki/Relais>`__ erweitert werden.
Jedes Relais besitzt drei Anschlüsse, der mittlere wird zwischen den beiden
äußeren umgeschaltet. Der Schaltzustand wird jeweils durch eine LED angezeigt.
Die neue Hardwareversion 1.2 ist mit umfangreicher Schutzbeschaltung gegen
Störungen durch Schalten induktiver Lasten ausgestattet.

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
Relais                              AZ943-1CH-5DE
Stromverbrauch                      75mA (pro Relais)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximale Spannung/Strom             | AC: 240V/10A
                                    | DC: 30V/7A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             45 x 45 x 25mm (1,77 x 1,77 x 0,98")
Gewicht                             29g
==================================  ============================================================


Ressourcen
----------

* AZ943-1CH-5DE Datenblatt (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/az943.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2pLtx4b>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/dual_relay/dual-relay.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/dual_relay/dual-relay.FCStd>`__)



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
Form eines `Varistors <https://de.wikipedia.org/wiki/Varistor>`__ oder der
Kombination eines Widerstandes und eines Kondensators parallel zur Last empfohlen.

Weitere Informationen über Schutzbeschaltung ist
`hier <http://www.jkmicro.com/inductive_loads.pdf>`__ zu finden.


.. _dual_relay_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Dual Relay Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-dual-relay-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Dual Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_1000.jpg

Das Gehäuse des Dual Relay Bricklet wird inklusive Kabelbinder für eine
Zugentlastung und WAGO Verbindungsklemmen zum Verbinden von Leitungen
ausgeliefert. Das Gehäuse ist groß genug um sowohl die Zugentlastung als
auch die WAGO Klemmen im Gehäuse unterzubringen. 

Der interne Aufbau kann wie folgt aussehen (mit einem bzw. beiden Relais
angeschlossen):

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

Der Außenleiter (braun) wird über das Dual Relay Bricklet geschaltet.
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


Die genaue Anordnung der Teile kann der folgenden Explosionszeichnung des Dual 
Relay Bricklet-Gehäuses entnommen werden:

.. image:: /Images/Exploded/dual_relay_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Dual Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|


.. _dual_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Dual_Relay_hlpi.table
