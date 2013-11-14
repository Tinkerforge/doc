
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Hardware Hacking für Anfänger 

.. _starter_kit_hardware_hacking_for_beginners:

Hardware Hacking für Anfänger
=============================

Das Hardware Hacking Kit soll dazu ermutigen andere Geräte zu hacken und 
grundlegende Elektronik-Kenntnisse zu erlernen. Nachfolgend wird beschrieben
wie die im Kit enthaltene Hardware genutzt werden kann.

Grundsätzlich gibt es zwei verschiedene Anwendungen für dieses Kit. Jede 
Anwendung wird von einem Bricklet unterstützt.


.. _starter_kit_hardware_hacking_for_beginners_quad_relay:

Industrial Quad Relay Bricklet
------------------------------

Allgemeine Beschreibung
^^^^^^^^^^^^^^^^^^^^^^^

Das :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
besteht aus vier
`Solid State Relais <https://de.wikipedia.org/wiki/Solid_State_Relais>`__
(oder auch Halbleiterrelais).
Relais sind elektromechanisch betriebene Schalter. Das heißt das
andere Signale kurzgeschlossen werden können, ausgelöst durch ein anderes
elektrisches Signal. Im Gegensatz zu normalen Relais sind Solid State Relais 
nicht mechanisch, sie besitzen keine mechanischen Teile.

Wenn mit den Relais etwas geschaltet werden soll muss die maximal erlaubte
Spannung von 30V beachtet werden. Es darf also z.B. keine Netzspannung 
geschaltet werden! In den meisten Fällen ist die maximale Spannung in einer
Schaltung durch die Versorgungsspannung gegeben. Als Beispiel werden alle
Schaltkreise in einem batteriebetrieben Gerät höchstwahrscheinlich nicht
die Batteriespannung überschreiten. Selbiges gilt für ein Gerät welches über
ein Steckernetzteil versorgt wird. Aber natürlich gibt es Ausnahmen. Falls
man sich nicht sicher ist sollte man nachmessen.

Kurzfassung: Typische Anwendungen für dieses Bricklet ist das An- und
Abschalten von anderen Schaltungen. Wir nutzen ein einfaches Beispiel um diese
Anwendung zu erläutern. Die folgende Schaltung zeigt eine LED (mit dem 
typischem Vorwiderstand), die über einen Schalter an- bzw. ausgeschaltet
werden kann.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_off_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, Schalter und LED, ausgeschaltet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_off_1500.jpg

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_on_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, Schalter und LED, angeschaltet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_on_1500.jpg

Wenn wir einen zweiten Schalter parallel zu dem ersten einbauen und einen
der beiden schließen, leuchtet die LED. Wenn beide
Schalter geschlossen werden leuchtet die LED auch. Immer wenn ein Schalter
geschlossen ist, kann der andere den Zustand der LED nicht beeinflussen. Die LED
wird leuchten.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_two_switches_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, zwei Schalter und LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_two_switches_1500.jpg

Dies ist die grundsätzliche Idee um eine andere Schaltung mit dem Industrial 
Quad Relay steuerbar zu machen. Wir installieren ein Relais des Bricklets
parallel zu einem existierenden Schalters und können ihn so überbrücken.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, Schalter, LED und Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_1500.jpg

Anstatt andere Geräte zu hacken, kann das Industrial Quad Relay natürlich auch
in eigenen Schaltungen genutzt werden.

Wie benutzt man das Industrial Quad Relay Bricklet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Angenommen wir möchten ein Gerät hacken, welches über Taster verfügt um
verschiedene Aktionen auszulösen (Beispiel Fernbedienung). 
Diese Aktionen möchten wir auch extern 
auslösbar machen. Als erstes müssen wir uns diese Taster und ihre Verbindungen 
auf der Platine genauer ansehen. In den meisten Fällen sind die zwei 
Leiterbahnen, die überbrückt werden sollen, auf der Platine einfach erkennbar. 
Wenn diese Leiterbahnen identifiziert sind, müssen nur zwei Drähte angelötet 
werden, jeweils einen zu einer Leiterbahn, um das Industrial Quad Relay damit 
zu verbinden.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup2.jpg
   :scale: 100 %
   :alt: Nahaufnahme: Schalter auf einer Platine
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup2.jpg

Das obige Bild zeigt ein Taster auf einer Platine. Die verbundenen 
Leiterbahnen, einen in der oberen rechten und einen in der unteren linken Ecke,
sind mit diesem Taster verbunden. Wir haben nun die beiden Leiterbahnen 
identifiziert die der Taster schaltet (vgl. Beispielschaltung oben).
Um die Funktion des Tasters extern auslösbar
zu machen, muss jeweils ein Draht an das obere rechte und ein Draht an das
untere rechte Pad angelötet werden. Anschließend sollte die Schaltung wie folgt
aussehen:

.. image:: /Images/Kits/hardware_hacking_garage_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Nahaufnahme: Taster auf Leiterplatte mit abgelötete Drähte
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_soldered_1500.jpg

Beide Drähte werden mit einem Relais des Quad Relay Bricklets verbunden. 
Anschließend ist es möglich die Aktion die der Taster zuvor ausgelöst hat
auch über das Quad Relay Bricklet auszulösen.


Industrial Digital In 4 Bricklet
--------------------------------

Allgemeine Beschreibung
^^^^^^^^^^^^^^^^^^^^^^^

Das :ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>` 
ist mit vier `Optokopplern <http://de.wikipedia.org/wiki/Optokoppler>`__
ausgestattet. Technisch gesehen besteht ein Optokoppler aus einer LED die
wiederum einen Fototransistor über ihr Licht steuert. Auf diese Art gibt es
zwischen diesen beiden Bauteilen keine direkte elektrische Verbindung, sie sind
galvanisch getrennt. 

Weniger technisch formuliert ist das Industrial Digital In 4 Bricklet mit
vier internen LEDs ausgestattet. Leuchtet eine dieser LEDs wird der 
dazugehörende Ausgang auf High geschaltet. Leuchtet die LED nicht, so ist der
Ausgang logisch Low. Die Ausgänge sind mit dem Mikrocontroller des Bricks 
verbunden, so dass der Status über diesen ausgelesen werden kann.

Wenn das Industrial Digital In 4 Bricklet genutzt werden soll, um den Status
eines anderen Geräts auszulesen, muss es mit einem der Eingänge verbunden 
werden. Dies muss so gestaltet werden, dass die interne LED leuchtet wenn der
Zustand, der ausgelesen werden soll, elektrisch High ist. Wenn der Zustand
elektrisch Low ist darf die LED nicht leuchten. In der elektrischen 
Spezifikation des Industrial Digital In 4 Bricklet steht:
Elektrische Spannungen unter 2V werden als "Low" (LED aus) interpretiert.
Spannungen über 3V als "High" (LED an). Für Spannungen zwischen 2V und 3V
ist das Verhalten undefiniert. Daher sollte dieser Bereich vermieden werden.

Wie benutzt man das Industrial Digital In 4 Bricklet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In diesem Beispiel möchten wir den Zustand einer sehr einfachen Schaltung,
repräsentiert durch eine LED, auslesen: 
Die LED wird von etwas geschaltet, in diesem Fall
von einem einfachen Schalter. Es könnte aber genauso gut ein IC o.ä. sein.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_off_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, Schalter und LED, ausgeschaltet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_off_1500.jpg

Um den Zustand der Schaltung auszulesen nutzen wir die LED. Um diese auszulesen
verbinden wir einen Eingang des Industrial Digital In 4 Bricklets damit. Da die
minimale High Level Spannung bei 3V liegt reicht es typischerweise nicht aus
nur die LED mit dem Eingang zu verbinden. Die (Vorwärts-) Spannung einer roten
LED liegt typischerweise bei 1,7V, so dass diese nicht hoch genug ist um
als High Level detektiert zu werden. Um eine höhere Spannung am Eingang zu 
erreichen verbinden wir nicht nur die LED mit dem Bricklet sondern die LED und 
deren Vorwiderstand. Die Polarität, oder anders ausgedrückt, die Art wie die 
LED und der Vorwiderstand an das Bricklet angeschlossen sind, ist egal. Wenn
das Digital In 4 Bricklet keine Reaktion zeigt wenn die LED leuchtet, müssen
die Drähte am Eingang getauscht werden. Die Verdrahtung sollte wie folgt
aussehen:

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_350.jpg
   :scale: 100 %
   :alt: Beispielschaltung mit Batterie, Schalter, LED und Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_1500.jpg


.. _starter_kit_hardware_hacking_for_identify_series_resistor:

Den Vorwiderstand einer LED identifizieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es gibt viele verschiedene Gehäuse für Widerstände. Die bekanntesten sind
bedrahtete Gehäuse:

.. image:: /Images/Kits/hardware_hacking_for_beginner_tht_resistor_350.jpg
   :scale: 100 %
   :alt: Foto von THT Widerständen
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_tht_resistor_1500.jpg

Heutzutage nutzen viele Produkte sogenannte
`Surface-Mount Devices (SMD)
<http://en.wikipedia.org/wiki/Surface-mount_device>`__.
Diese Gehäuse können in ihrer Größe sehr stark abweichen. Es gibt sehr kleine
(z.B. Gehäuse 0201: 0.6mm x 0.3mm) oder große Gehäuse 
(Gehäuse 2920: 7.4mm x 5.1mm). Es gibt Widerstände, Kondensatoren, 
Induktivitäten und andere Bauteile die direkt auf die Platine gelötet werden.

.. image:: /Images/Kits/hardware_hacking_for_beginner_smd_resistor_350.jpg
   :scale: 100 %
   :alt: Foto von SMD Widerständen
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_smd_resistor_1500.jpg

Aber wie weiß man um welche Art von Bauteil es sich handelt?
Experten können Bauteile anhand ihrer Optik unterscheiden. Wenn das Bauteil
auch noch eine Markierung besitzt, so kann auch deren Wert (z.B. 1k Ohm 
Widerstand oder 22 Ohm Widerstand) bestimmt werden. Wenn das Bauteil keine
Markierung trägt und das Bauteil nicht optisch identifiziert werden kann, 
so kann es nur per Messung oder über Ermittlung der Funktion in der
Schaltung identifiziert werden.

Dies ist der Ansatzpunkt für dieses Kit. Wenn der Status einer LED ausgelesen
werden soll müssen nur deren Leiterbahnen verfolgt werden bis ein bedrahtetes
oder SMD Bauteil erreicht wird. Hierbei handelt es sich höchstwahrscheinlich
um den Vorwiderstand.

Das nächste Bild zeigt ein Beispiel (basiert auf dem
:ref:`starter_kit_hardware_hacking_garage_control` Beispiel).

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup3_350.jpg
   :scale: 100 %
   :alt: Nahaufname: LED Vorwiderstand
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup3.jpg

Abgebildet ist eine SMD LED markiert durch einen roten Pfeil. An diese sind
zwei Leiterbahnen angeschlossen. In der einen Leiterbahn findet sich ein 
kleiner SMD Widerstand (markiert durch einen blauen Pfeil).

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup4_350.jpg
   :scale: 100 %
   :alt: Nahaufnahme: LED mit Vorwiderstand
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup4.jpg

Soll also der Zustand einer LED ausgelesen werden, so muss ein Draht an die
LED (rote Kreis) und der andere nach dem Vorwiderstand angelötet werden (einer 
der blauen Kreise). Das war es!

.. _starter_kit_hardware_hacking_for_beginners_soldering:

Einen Draht an ein Pad anlöten
------------------------------

Um einen Draht an ein Pad anzulöten wird ein
`Lötkolben <https://de.wikipedia.org/wiki/L%C3%B6tkolben>`__ 
und `Lötzinn <https://de.wikipedia.org/wiki/Lot_%28Metall%29>`__ benötigt.

Löten ist kein Hexenwerk!
Für das Starterkit: Hardware Hacking müssen nur Drähte an Pads angelötet 
werden. 

Einen Draht an ein Pad anzulöten kann in fünf Schritten erfolgen:

* Erwärme das Pad mit dem Lötkolben
* Füge Lötzinn hinzu wenn es heiß ist, das Zinn sollte flüssig werden
* Lege den Draht an das Pad
* Entferne den Lötkolben (den Draht weiter festhalten)
* Warte bis das Zinn abgekühlt ist

Eine Vereinfachung kann es sein wenn man den Draht vorher verzinnt.
Bei `Youtube <http://www.youtube.com>`__ gibt es eine Menge an How-To Videos
zum Thema Löten.

Auch in unserem "Starter Kit: Hardware Hacking" How-To Video kann man erkennen
wie die Drähte an die Pads gelötet werden (löten startet bei 2:00):

.. raw:: html

 <iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/hHnhflS3260?start=120" frameborder="0" allowfullscreen></iframe>
