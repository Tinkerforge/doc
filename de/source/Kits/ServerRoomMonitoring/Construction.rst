
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Starterkit: Serverraum-Überwachung</a> / Aufbau des Starterkits: Serverraum-Überwachung

.. _starter_kit_server_room_monitoring_construction:

Aufbau des Starterkits: Serverraum-Überwachung
==============================================

Das Starterkit: Serverraum-Überwachung wird mit einem :ref:`Ambient Light 
Bricklet <ambient_light_bricklet>`, :ref:`PTC Bricklet <ptc_bricklet>`,
:ref:`Temperature Bricklet<temperature_bricklet>`, 
:ref:`Master Brick <master_brick>`,
:ref:`Ethernet Extension <ethernet_extension>` sowie
Bricklet Kabel, Schrauben, Abstandshalter, Muttern und Unterlegscheiben.

Schrauben, Abstandshalter, Muttern und Unterlegscheiben sind in einzelnen
Befestigungskits verpackt. Diese sind Standard-Befestigungskits und nicht 
speziell für dieses Starterkit zusammengestellt. Die benötigten Teile für jeden 
Arbeitsschritt müssen aus den Befestigungskits selektiert werden. Für eigene 
Modifikationen sind mehr Befestigungsteile enthalten als notwendig.

.. image:: /Images/Kits/server_room_monitoring_exploded_guided_small.png
   :scale: 100 %
   :alt: Explosionszeichnung Starterkit: Serverraum-Überwachung
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_exploded_guided.png

Schutzfolien entfernen
----------------------

Als erstes müssen die Schutzfolien von allen Gehäuseteilen entfernt werden. 
Jeweils auf Front- und Rückseite befindet sich eine Schutzfolie. Ein Messer kann
bei der Entfernung der Folien helfen, sollten sich diese schwer entfernen 
lassen.

Winkel mit den Seitenteilen verbinden
-------------------------------------

Im nächsten Schritt werden die Winkel mit den Seitenteilen verbunden.
Dazu wird der Winkel, wie im nachfolgenden Bild abgebildet, in das Seitenteil 
gesteckt. Anschließend wird eine Mutter in die vorgesehene Aussparung gesteckt
und mittels einer 12mm langen Schraube mit dem Seitenteil verbunden. Falls diese 
Mutter nicht in die Aussparung zu passen scheint, muss diese etwas gedreht 
werden.

Das Ergebnis dieses Arbeitsschritts ist in dem folgenden Bild abgebildet:

.. image:: /Images/Kits/server_room_monitoring_construction_step1_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 1
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step1.png

Seitenteile mit dem Frontteil verbinden
---------------------------------------

Die zuvor hergestellten Seitenteile werden in das Frontteil gesteckt und 
ebenfalls mit jeweils einer Mutter und 12mm Schraube befestigt. Wichtig ist das 
Frontteil wie im nachfolgenden Bild zu befestigen. Das Frontteil ist korrekt
befestigt, wenn die Position des Ausschnitts für die Ethernet Extension 
übereinstimmt.

.. image:: /Images/Kits/server_room_monitoring_construction_step2_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 2
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step2.png

Rückseite befestigen
--------------------

Als nächstes werden acht 10mm Abstandshalter (Innen-/Innengewinde) mittels 
kurzen Schrauben an die Positionen für das PTC und das Temperature Bricklet auf 
das Rückseitenteil geschraubt.

.. image:: /Images/Kits/server_room_monitoring_construction_step3_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 3
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step3.png

Anschließend wird die Rückseite auf die Seitenteile gesteckt und ebenfalls
mittels zwei 12mm langen Schrauben und zwei Muttern befestigt. Anschließend ist 
das Gehäuse fertiggestellt. Im nächsten Schritt werden die Bricks und Bricklets 
eingebaut.

.. image:: /Images/Kits/server_room_monitoring_construction_step4_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 4
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step4.png

Bricks und Bricklets einbauen
-----------------------------

Die Ethernet Extension wird auf das Master Brick gesteckt wobei
jeweils ein 9mm Abstandshalter (Innen-/Außengewinde) dazwischen gesteckt wird. 
Anschließend wird jeweils ein 10mm Abstandshalter (Innen-/Innengewinde)
unten aufgeschraubt und die Master Extension mittels Schrauben befestigt.

.. image:: /Images/Kits/server_room_monitoring_construction_step5_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 5
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step5.png

Dieser Stapel wird an ein Seitenteil mittels vier Schrauben geschraubt.

.. image:: /Images/Kits/server_room_monitoring_construction_step6_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 6
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step6.png

Als nächstes werden PTC und Temperature
Bricklet auf die zuvor installierten 10mm Abstandshalter auf
dem Rückseitenteil aufgeschraubt. 

Es ist einfacher wenn hier vor dem aufschrauben die 15cm Bricklet Kabel
an die Bricklets angeschlossen werden.

Vor der ersten Benutzung muss das PTC Bricklet konfiguriert werden und der 
Temperatursensor (2-Leiter) angeschlossen werden. Wie dies funktioniert ist
:ref:`hier <ptc_bricklet_jumper_configuration>` und
:ref:`hier <ptc_bricklet_connectivity>` dokumentiert.

.. image:: /Images/Kits/server_room_monitoring_construction_step7_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 7
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step7.png

Im letzten Schritt wird das Ambient Light Bricklet an die Frontseite geschraubt.
Dazu werden vier 12mm lange Schrauben durch die Frontseite gesteckt und von 
hinten jeweils mittels einer Unterlegscheibe und einer Mutter fixiert. 
Anschließend wird das 50cm Brickletkabel an das Ambient Light Bricklet 
angeschlossen und dieses auf die vier Schrauben gesteckt. Fixiert wird es über 
jeweils eine Mutter. 

.. image:: /Images/Kits/server_room_monitoring_construction_step8_350.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 8
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step8.png

Die Brickletkabel müssen nun noch zum Master Brick geführt und dort
angeschlossen werden. Ein Kabelbinder kann genutzt werden um die
Verkabelung ordnen.

Das nachfolgende Bild zeigt das fertig aufgebaute Kit.

.. image:: /Images/Kits/server_room_monitoring_construction_step9_600.jpg
   :scale: 100 %
   :alt: Arbeitsschritt 9
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_construction_step9.png

.. image:: /Images/Kits/server_room_monitoring_cabling_600.jpg
   :scale: 100 %
   :alt: Serverraum-Überwachungskit: Verkabelung
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_cabling_1000.jpg
