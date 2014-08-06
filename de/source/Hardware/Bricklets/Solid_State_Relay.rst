
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
	    tfdocstart("Bricklets/bricklet_ssr_w_ssr_350.jpg",
	               "Bricklets/bricklet_ssr_w_ssr_600.jpg",
	               "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ssr_vertical_100.jpg",
	             "Bricklets/bricklet_ssr_vertical_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ssr_tilted_100.jpg",
	             "Bricklets/bricklet_ssr_tilted_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ssr_w_cover_100.jpg",
	             "Bricklets/bricklet_ssr_w_cover_600.jpg",
	             "Solid State Relay Bricklet mit Abdeckung")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ssr_w_heatsink_tilted_low_100.jpg",
	             "Bricklets/bricklet_ssr_w_heatsink_tilted_low_600.jpg",
	             "Solid State Relay Bricklet mit Kühlkörper")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ssr_w_heatsink_tilted_100.jpg",
	             "Bricklets/bricklet_ssr_w_heatsink_tilted_600.jpg",
	             "Solid State Relay Bricklet mit Kühlkörper")
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


Features
--------

* Galvanisch getrenntes Schalten großer Wechselstrom- oder Gleichstrom-Lasten

  * zum Beispiel: Motoren, Pumpen und Lampen

* Bricklet steuert Solid State Relais (SSR)

  * Mit angebotenen SSRs bis zu 380V/25A AC oder 50V/80A DC schaltbar

* PWM möglich (Dimmen von Lampen, Geschindigkeit von Motoren steuern)


.. _solid_state_relay_bricklet_description:

Beschreibung
------------

Mittels Solid State Relais (SSR) können große Lasten, galvanisch getrennt 
geschaltet werden. Schaltfunken und damit verbundene Störungen, wie sie bei 
mechanischen Relais auftreten können, treten somit nicht auf. Zudem sind Solid 
State Relais verschleißfrei und ermöglichen deutlich höhere Schaltfrequenzen.

Die maximale Schaltleistung hängt von dem angeschlossenen Solid State Relais ab, 
das über das Solid State Relay Bricklet gesteuert wird. 


Im Shop bieten wir zwei passende Solid State Relais an:

* `AC (Wechselstrom) SSR mit einer maximalen Leistung von 380V bei 25A <https://www.tinkerforge.com/de/shop/solid-state-relay-ac-380v-25a.html>`__
* `DC (Gleichstrom) SSR mit einer maximalen Leistung von 50V bei 80A <https://www.tinkerforge.com/de/shop/solid-state-relay-dc-50v-80a.html>`__

Technische Spezifikation
------------------------

===========================================  ============================================================
Eigenschaft                                  Wert
===========================================  ============================================================
Stromverbrauch                               <20mA
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Notwendiger Kontaktabstand des SSR Eingangs   25,4mm (1")
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                      19 x 33,4 x 5mm (0,75 x 1,31 x 0,2")
Gewicht                                      1,6g
===========================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/raw/master/hardware/solid-state-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/solid_state_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/zipball/master>`__)
* Datenblatt SSR AC 380V/25A (KS15/D-38Z25-L) (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/blob/master/datasheets/ks15_ac.pdf?raw=true>`__)
* Datenblatt SSR DC 50V/80A (KS33/D-50D80-L) (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/blob/master/datasheets/ks33_dc.pdf?raw=true>`__)
* Datenblatt SSR Kühlkörper (HF92B-120) (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/blob/master/datasheets/hf92b_heatsink.pdf?raw=true>`__)
* Datenblatt SSR Abdeckung (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/blob/master/datasheets/ssr_cover.pdf?raw=true>`__)


Anschlussmöglichkeit
--------------------

Das Bricklet wird mit den Steuerkontakten (Input) des Solid State Relais 
verbunden. Dabei ist auf die Polung zu achten. Typischerweise ist auf dem Relais 
ein Kontakt mit einem "+" markiert, dieser Kontakt muss mit dem ebenfalls mit 
"+" markierten Kontakt des Bricklets verbunden werden.

Die Ausgangssseite des Solid State Relais weist bei Wechselstromrelais keine 
Polung auf. Typischerweise schaltet man mit dem Relais eine Phase 
(schwarzer Draht), indem man diesen Draht trennt und beide Enden mit dem Relais 
verbindet.

Bei Gleichstromrelais ist die Polung des Ausgangs zu berücksichtigen.
"+" Kennzeichnet hierbei die höhere Spannung. Soll zum Beispiel eine 
Stromversorgung geschaltet werden, so kann deren "+" Leitung getrennt werden.
Das Leitungsende, welches anschließend noch einen direkten Kontakt zur 
Stromversorgung besitzt muss anschließend mit dem "+" Pol des Solid State Relais 
verbunden werden. Die verbleibende Leitung wird mit dem "-" Pol des Relais 
verbunden.

.. warning:: Der Umgang mit Wechselspannungen, als auch mit hohen 
   Gleichspannungen, ist potentiell lebensgefährlich!

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

PWM / Dimmen / Geschwindigkeitssteuerung
----------------------------------------

Durch ein häufiges Ein-/ und Ausschalten des Solid State Relais können 
angeschlossene Lasten geregelt werden (Beispiel: Helligkeit einer Lampe,
Geschwindigkeit eines Motors). Das Verhältnis von eingeschalteter Zeit zur 
ausgeschalteter Zeit bestimmt dabei die Leistung der angeschlossenen Last. Die 
Frequenz sollte dabei konstant sein und nur die eingeschaltete Zeit variiert 
werden
(siehe `Pulsweitenmodulation <http://de.wikipedia.org/wiki/Pulsweitenmodulation>`__).

Beispiel:
Eine Heizung soll geregelt werden. Da eine Heizung sehr träge reagiert reicht 
eine Schaltfrequenz von 1Hz. Dazu schreibt man ein kleines Programm, welches 
mittels eines Timers 1 mal pro Sekunde die "set_monoflop" Methode des Solid 
State Relay Bricklets mit einer Zeitdauer von 0-1 Sekunde aufruft 
(0% - 100% Leistung).

.. warning::
   Hohe Schaltfrequenzen führen zu der Produktion von Wärme in einem Solid State 
   Relais. Zu hohe Frequenzen, bei nicht ausreichender Kühlung, können das 
   Relais zerstören. Frequenzen im Bereich von 20-30 Hz sollten nicht 
   überschritten werden.


.. _solid_state_relay_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Solid_State_Relay_hlpi.table
