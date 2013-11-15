
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Hardware-Aufbau: Funksteckdosen

.. _starter_kit_hardware_hacking_remote_switch_hardware_setup:

Hardware-Aufbau: Funksteckdosen
===============================

In diesem Kit sind zwei Funksteckdosen enthalten. Dieses Beispiel beschreibt wie
diese gehackt werden können. Es gibt viele verschiedene Funksteckdosen
mit identischen oder ähnlichen Fernbedienungen auf dem Mark, so dass diese
Beschreibung auch für diese gilt.

Die meisten Fernbedienungen für Funksteckdosen sind mit einem IC genannt
HX2262 ausgestattet. Dieser besitzt im wesentlichen sechs verschiedene 
Eingänge: Zwei um zu definieren ob es eine EIN oder AUS Kommando ist und vier
Eingänge um zu definieren was geschaltet werden soll (A, B, C oder D). Alle
Eingänge sind in einer Matrix verschaltet.

In diesem Beispiel werden wir das :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` mit seinen
vier Solid State Relais nutzen um die Eingänge EIN, AUS, A und B nach GND
zu schalten. Wenn zusätzlich auch C und D geschaltet werden soll muss ein
weiteres Industrial Quad Relay Bricklet genutzt werden.

Das Innenleben der Fernbedienung
--------------------------------

Im Gehäuse der Fernbedienung befindet sich höchst wahrscheinlich 
eine Leiterplatte wie diese (How-To Video `1:31 <http://www.youtube.com/watch?v=hHnhflS3260&t=91>`__):

.. image:: /Images/Kits/hardware_hacking_remote_open_350.jpg
   :scale: 100 %
   :alt: Fernbedienung geöffnet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_open_1200.jpg

Das große IC rechts neben dem roten DIP Schalter ist der HX2262. Wenn das 
Gehäuse komplett entfernt wurde und man einen Blick auf die Unterseite der
Leiterplatte wirft sollte diese wie folgt aussehen:

.. image:: /Images/Kits/hardware_hacking_remote_bottom_350.jpg
   :scale: 100 %
   :alt: Nahaufname: Fernbedienung Unterseite
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_bottom_1200.jpg


Drähte am IC anlöten
--------------------

Als nächstes müssen wir Drähte an den HX2262 anlöten um diese von außen 
steuern zu können. Wir werden fünf Drähte an den HX2262 anlöten
(:ref:`Kleines Löttutorial <starter_kit_hardware_hacking_for_beginners_soldering>`,
How-To Video `1:56 <http://www.youtube.com/watch?v=hHnhflS3260&t=116>`__):

========== ====== ===========
Pin Nummer Signal Draht Farbe
========== ====== ===========
6          A      blau
7          B      rot
8          C      /
9          GND    schwarz
10         D      /
11         /      /
12         ON     gelb
13         OFF    lila
========== ====== ===========

Das folgende Foto zeigt die Position des HX2262 und die Pin-Nummerierung:

.. image:: /Images/Kits/hardware_hacking_remote_bottom_labeled_350.jpg
   :scale: 100 %
   :alt: Nahaufnahme: Fernbedienung Unterseite beschriftet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_bottom_labeled_1200.jpg

Nachdem Löten sollte die Leiterplatte wie folgt aussehen:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_remote_350.jpg
   :scale: 100 %
   :alt: Nahaufname: Fernbedienung mit angelöteten Drähten
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_remote_1200.jpg


.. _starter_kit_hardware_hacking_remote_switch_hardware_setup_relay_matrix:

Drähte am Industrial Quad Relay Bricklet anschließen
----------------------------------------------------

Als nächstes werden wir diese Drähte an das Industrial Quad Relay Bricklet
anschließen. Jeder Eingang des HX2262 ist an ein Relais angeschlossen.
Im ersten Schritt wird jeder Draht (außer schwarz) an einen der zwei
Anschlüsse jedes Relais angeschlossen (How-To Video `4:30 <http://www.youtube.com/watch?v=hHnhflS3260&t=270>`__).

====== =========== ======
Signal Draht Farbe Relais
====== =========== ======
A      blau        0
B      rot         1
ON     gelb        2
OFF    lila        3
====== =========== ======

Nun ist jedes Relais mit einem Draht verbunden, aber es fehlt der zweite Draht.
Da wir gegen GND schalten wollen (mit GND kurzschließen) muss dieser zweite
Draht GND sein. Dazu verbinden wir den schwarzen Draht mit einem Relais und 
Brücken ihn weiter mit kurzen schwarzen Drahtstücken zu den anderen
(How-To Video `5:02 <http://www.youtube.com/watch?v=hHnhflS3260&t=302>`__).
Das nächste Bild zeigt das fertige Werk.

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_350.jpg
   :scale: 100 %
   :alt: Nahaufname: Industrial Quad Relay Bricklet Stecker
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_1200.jpg

Hiernach sind wir fertig. Der komplette Hardwareaufbau sieht wie folgt aus:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet mit verbundener Fernbedienung
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_1200.jpg

