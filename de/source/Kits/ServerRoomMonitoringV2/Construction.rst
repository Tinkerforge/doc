
.. _starter_kit_server_room_monitoring_v2_construction:

Aufbau des Starterkits: Serverraum-Überwachung 2.0
==================================================

Das Starterkit: Serverraum-Überwachung 2.0 wird mit 

* :ref:`1x Ambient Light Bricklet 3.0 <ambient_light_v3_bricklet>`,
* :ref:`1x PTC Bricklet 2.0 <ptc_v2_bricklet>`,
* :ref:`1x Temperature Bricklet 2.0 <temperature_v2_bricklet>`,
* :ref:`1x Humidity Bricklet 2.0 <humidity_v2_bricklet>`,
* :ref:`1x Segment Display 4x7 Bricklet 2.0 <segment_display_4x7_v2_bricklet>`,
* :ref:`1x E-Paper 296x128 Bricklet (schwarz/weiß/rot) <e_paper_296x128_bricklet>`,
* :ref:`2x Master Brick <master_brick>`,
* :ref:`1x Ethernet Extension (with PoE) <ethernet_extension>`

sowie notwendigen Bricklet Kabeln, Schrauben, Abstandshalter, Muttern und 
Unterlegscheiben ausgeliefert.

Schrauben, Abstandshalter, Muttern und Unterlegscheiben sind in einzelnen
Befestigungskits verpackt. Die benötigten Teile für jeden Arbeitsschritt 
müssen aus den Befestigungskits zusammengesucht werden. Das übrige 
Befestigungsmaterial kann für eigene Modifikationen verwendet werden.

.. image:: /Images/Kits/server_room_monitoring_v2_exploded_600.jpg
   :scale: 100 %
   :alt: Explosionszeichnung Starterkit: Serverraum-Überwachung
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_exploded_1500.jpg

Schutzfolien entfernen
----------------------

Als erstes müssen die Schutzfolien von allen Gehäuseteilen entfernt werden. 
Jeweils auf Front- und Rückseite der Kunstoffteile befinden sich Schutzfolien. 
Ein Messer kann bei der Entfernung der Folien helfen, sollten sich diese 
schwer entfernen lassen.

Winkel mit den Seitenteilen verbinden
-------------------------------------

Im nächsten Schritt werden die Winkel mit den Seitenteilen verbunden.
Dazu wird der Winkel, wie im nachfolgenden Bild abgebildet, in das Seitenteil 
gesteckt. Anschließend wird eine Mutter in die vorgesehene Aussparung gesteckt
und mittels einer 12mm langen Schraube mit dem Seitenteil verbunden. Falls diese 
Mutter nicht in die Aussparung zu passen scheint, muss diese etwas gedreht 
werden.

Das Ergebnis dieses Arbeitsschritts ist im folgenden Bild abgebildet:

.. image:: /Images/Kits/server_room_monitoring_v2_construction_1_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 1
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_1_1000.jpg

Seitenteile mit dem Frontteil verbinden
---------------------------------------

Die zuvor verbundenen Seitenteile werden in das Frontteil gesteckt und 
ebenfalls mit jeweils einer Mutter und 12mm Schraube befestigt. Wichtig 
ist das Frontteil wie im nachfolgenden Bild zu befestigen und darauf zu 
achten dass das Tinkerforge Logo richtig herum ist.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_2_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 2
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_2_1000.jpg

Rückseite befestigen
--------------------

Als nächstes werden acht 10mm Abstandshalter (Innen-/Innengewinde) mittels 
kurzen Schrauben an die Positionen für das Temperature Bricklet 2.0 und 
Humidity Bricklet 2.0 auf das Rückseitenteil geschraubt.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_3_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 3
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_3_1000.jpg

Anschließend wird die Rückseite auf die Seitenteile gesteckt und ebenfalls 
mittels zwei 12mm langen Schrauben und zwei Muttern befestigt. Zusätzlich 
wird ein Winkel in der Mitte der Rückseite mit Schraube und Mutter befestigt. 
Darauf achten dass die Bodenplatte wie im nächsten Schritt daran befestigt 
werden kann. 

.. image:: /Images/Kits/server_room_monitoring_v2_construction_4_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 4
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_4_1000.jpg
   
Boden befestigen
----------------

Im Anschluss wird die Bodenplatte an das bereits zusammngeschraubte Gehäuse 
befestigt. Dafür wird die Bodenplatte wie im Bild an die Unterseite der 
Seitenteile gedrückt und wie gehabt mit 12mm Schrauben und Muttern fixiert. 
Danach vier 10mm Abstandshalter (Innen-/Innengewinde) für das PTC Bricklet 2.0 
mittels kurzen Schrauben an die gewünschte Positionen auf der Lochrasterplatte schrauben.
Im nächsten Schritt werden die Bricks und Bricklets angebracht.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_5_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 5
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_5_1000.jpg

Bricks und Bricklets einbauen
-----------------------------

Jetzt werden die Bricks und Bricklets ans Gehäuse geschraubt.

Master Brick und Ethernet Extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Ethernet Extension wird auf die zwei Master Bricks gesteckt wobei jeweils 
ein 12mm Abstandshalter (Innen-/Außengewinde) und eine Unterlegscheibe 
dazwischen gesteckt wird. Anschließend wird jeweils ein 10mm Abstandshalter 
(Innen-/Innengewinde) unten den untersten Master Brick geschraubt und die 
Master Extension auf den obersten Master Brick von oben mittels Schrauben 
befestigt. 

Dieser Stapel wird an das gewünschte Seitenteil mit vier kurzen 
Schrauben angebracht. Wenn die Anschlüsse nach vorne schauen sollen muss 
der Stapel an das linke Seitenteil geschraubt werden. Bei einer Nutzung 
bei der die Kabelführung nach hinten erfolgen soll muss der Stapel 
dementsprechend an das rechte Seitenteil befestigt werden.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_6_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 6
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_6_1000.jpg

RED Brick (optional)
^^^^^^^^^^^^^^^^^^^^

Wenn das Kit inklusive RED Brick gebaut wird, sollte der RED Brick unter
der Ethernet Extension sein und der Master Brick auf der Ethernet Extension 
gesteckt werden. Beide können mit 12mm Abstandshaltern (Innen-/Außengewinde) 
und Unterlegscheiben befestigt werden.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_7_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 7
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_7_1000.jpg

Raspberry Pi und HAT Brick (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sollte das Kit mir einem Raspberry Pi genutzt werden wird dieser zusammen 
mit dem HAT Brick in der Mitte der Bodenplatte an die dafür vorgesehene 
Platzierung verschraubt. Dafür die entsprechenden Abstandbolzen und 
Schrauben des Raspberry Pi Befestigungskits verwenden. Zur Montage gibt es
zwei Stege die an den Raspberry Pi geschraubt werden. Danach kann dies an
den Boden verschraubt werden. Für die richtige Platzierung sind Lächer 
vorgesehen an die der Aufbau aufgelegt und anschließend mit den langen Schrauben
und jeweils einer Mutter verschraubt wird. Hier ist es auch möglich den 
Raspberry Pi nach vorne oder nach hinten auszurichten.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_8_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 8
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_8_1000.jpg

.. image:: /Images/Kits/server_room_monitoring_v2_construction_9_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 9
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_9_1000.jpg

.. image:: /Images/Kits/server_room_monitoring_v2_construction_10_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 10
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_10_1000.jpg

PTC, Temperature und Humidity Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Als nächstes werden Temperature Bricklet 2.0 und Humidity Bricklet 2.0 
auf die zuvor positionierten 10mm Abstandshalter auf dem Rückseitenteil 
sowie das PTC Bricklet 2.0 auf der Bodenplatte aufgeschraubt.

Vor der ersten Benutzung muss das PTC Bricklet 2.0 konfiguriert werden 
und der Temperaturfühler (2-Leiter) angeschlossen werden. Wie dies funktioniert 
ist
:ref:`hier <ptc_v2_bricklet_jumper_configuration>` und
:ref:`hier <ptc_v2_bricklet_connectivity>` dokumentiert.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_11_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 11
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_11_1000.jpg

.. image:: /Images/Kits/server_room_monitoring_v2_construction_12_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 12
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_12_1000.jpg

E-Paper, Segment Display, Ambient Light Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Im letzten Schritt wird das Ambient Light Bricklet 3.0, Segment Display 
4x7 Bricklet 2.0 und das E-Paper 296x128 Bricklet (schwarz/weiß/rot) an 
die Frontseite geschraubt. Dazu werden jeweils vier 12mm lange Schrauben 
durch die Frontseite gesteckt und von hinten jeweils mit zwei Muttern fixiert. 
Beim E-Paper Bricklet werden die vier Schrauben mit nur jeweils einer Mutter 
gekontert. Anschließend werden die 50cm Bricklet Kabel (7p-10p) an die 
Bricklets angeschlossen. Im Anschluss dann die drei Bricklets auf die 
Schrauben setzten und erneut mit jeweils einer weiteren Mutter befestigen.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_13_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 13
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_13_1000.jpg

Verkabeln, Deckel drauf, Fertig
-------------------------------

Die Bricklet Kabel müssen nun noch zum Master Brick geführt und dort
angeschlossen werden. Ein Kabelbinder kann zur Ordnung der Verkablung
genutzt werden.

Sobald alles verkabelt und verlegt ist wird der Deckel mit dem TF-Logo 
aufgesetzt. Zuvor sollte relativ nah an der Frontplatte im mittleren 
Bereich ein Stapel aus 3 Abstandbolzen an der Bodenplatte verschraubt 
werden. Danach kann der Deckel aufgelegt werden. Dieser wird dann lediglich 
mit einer Schraube mit dem zuvor positionierten Abstandsbolzenstapel 
verschraubt.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_14_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 14
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_14_1000.jpg

Das nachfolgende Bild zeigt das fertig aufgebaute Kit.

.. image:: /Images/Kits/server_room_monitoring_v2_construction_15_600.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 15
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_v2_construction_15_1000.jpg

