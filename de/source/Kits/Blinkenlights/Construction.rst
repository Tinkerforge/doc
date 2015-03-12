
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/Blinkenlights/Blinkenlights.html">Starterkit: Blinkenlights</a> / Aufbau des Starterkits: Blinkenlights


.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white

.. role:: power-red

.. role:: power-black

.. role:: power-white


.. _starter_kit_blinkenlights_construction:

Aufbau des Starterkits: Blinkenlights
=====================================

Das Starterkit: Blinkenlights besteht aus:

* 1x :ref:`Master Brick <master_brick>`,
* 1x :ref:`LED Strip Bricklet <led_strip_bricklet>`,
* 4x LED Pixel (jeweils 50 Stück),
* 1x Gelochte Rückplatte 80x40cm (schwarz)
* 1x Frontplatte 90x50cm (weiß)
* 4x Wandbefestigungsplatte (für Wandhaken)
* 1x 5V/8A Stromversorgung
* 1x Bricklet Kabel 15cm
* 1x 2x2.5mm² Litze (5m)
* 2x Dübel und Wandhaken
* 4x 2-Draht Klemmen
* 6x 3-Draht Klemmen
* 4x 5-Draht Klemmen

sowie Kabelbinder, Schrauben, Abstandshalter und andere Teile.

.. image:: /Images/Kits/kit_blinkenlights_content_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Inhalt
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_content_1200.jpg


Benötigte Werkzeuge
-------------------

Ein Kreuzschlitz-Schraubendreher, etwas zum Abisolieren von Drähten (Messer
oder Abisolierzange) und ein Maßband sind notwendig. Es sollte sich genügend
Zeit zum Aufbau des Kits genommen werden.

Erster Schritt
--------------

Überprüfe ob alles vorhanden und unbeschädigt ist. Anschließend
sollte die Schutzfolien von Frontplatte (weiß) und Rückplatte (schwarz) 
abgezogen werden. Jeweils auf Vorder- und Rückseite befindet sich eine Folie.

.. image:: /Images/Kits/kit_blinkenlights_remove_protective_foil_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Aufbau Folien entfernen
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_remove_protective_foil_1200.jpg


Pixel in die Rückplatte einsetzen
---------------------------------

Als nächstes werden die Pixel in die Rückplatte gesteckt. Es ist wichtig
mit dem korrekten Pixel an der korrekten Position zu beginnen. Falls falsch 
begonnen wird ist es möglich, dass die Pixel nicht verbunden werden können
oder die Kabel unglücklich verlegt werden müssen.

Nimm das erste Bündel Pixel und stecken das Pixel an dem ein Stecker befestigt
ist (das Ende, dass mit dem LED Strip Bricklet verbunden wird) in das erste
Loch. 

.. image:: /Images/Kits/kit_blinkenlights_build_step1_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Schritt 1
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step1_1200.jpg

Die Vorder- und Rückseite der Rückplatte sind unterschiedlich, zu erkennen an
der Anordnung der kleinen Befestigungslöcher.
Die folgende Grafik zeigt die Rückseite der Rückplatte. Die Pixel werden von
dieser Seite eingesteckt, so dass die Köpfe der Pixel auf der Vorderseite sind.
Beachte die Startposition der
ersten LED. Nach dem Einstecken der ersten LED werden die Folgenden im
rot markierten Muster eingesteckt.

.. image:: /Images/Kits/kit_blinkenlights_led_wiring_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Verdrahtungsbeschreibung
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_led_wiring_1200.jpg

Nachdem die ersten 50 Pixel eingesteckt wurden, wird mit den nächsten 50
fortgefahren. Das erste Pixel des nächsten Bündel wird mit dem letzten Pixel
der bereits eingesteckten Pixel verbunden.

.. image:: /Images/Kits/kit_blinkenlights_build_step4_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau alle Pixel eingesteckt
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step4_1200.jpg


Stromversorgungskabel und Pixelverkabelung
------------------------------------------

Im nächsten Schritt werden die Stromversorgungskabel zugeschnitten und 
eingebaut. 5m von 2x2.5mm² Litze liegt dem Kit bei. Folgende Längen müssen
davon geschnitten werden:

* 1x 95cm
* 1x 80cm
* 1x 55cm
* 1x 40cm
* 1x 20cm
* 1x 10cm

10mm von beiden Enden müssen abisoliert werden.

.. image:: /Images/Kits/kit_blinkenlights_wire_stripped_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Abisolierte Drähte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wire_stripped_1200.jpg

Zusätzlich müssen 8mm der Stromversorgungsdrähte der LED Pixel
(:led-pixel-blue:`blaue` und :led-pixel-red:`rote` Drähte) abisoliert werden.


Drähte verbinden
----------------

Es muss darauf geachtet werden, dass die Verdrahtung korrekt ist. Eine 
inkorrekte Verdrahtung kann zu Kurzschlüssen und zerstörter Hardware führen!

Wir beginnen die Verdrahtung mit dem 95cm Abschnitt. Mit diesem wird 
das letzte Pixel mit der späteren Stromversorgung verbunden. Dazu nehmen werden
zwei 2-Draht Klemmen jeweils mit dem :led-pixel-red:`roten` LED Pixel 
Draht bzw. dem :led-pixel-blue:`blauen` Draht verbunden.
Der :led-pixel-blue:`blaue` Draht wird mit dem :power-black:`schwarzen` 
Stromversorgungsdraht verbunden. Der :led-pixel-red:`rote` Draht des Pixels
wird mit dem :power-red:`roten` Stromversorgungsdraht verbunden.
Das fertig installierte 95cm Stromversorgungskabel ist nachfolgend abgebildet.

.. image:: /Images/Kits/kit_blinkenlights_wago_2x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Drahtklemmen
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_2x_connected_1200.jpg

.. image:: /Images/Kits/kit_blinkenlights_build_step6_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Schritt 95cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step6_1200.jpg

Danach wird das 80cm Kabel installiert. Dieses wird mit dem vorletzten 
Versorgungspunkt verbunden. Dazu nehmen werden zwei 3-Draht Klemmen genommen
um die zwei :led-pixel-blue:`blauen` Drähte der Pixel mit dem
:power-black:`schwarzen` Stromversorgungsdraht zu verbinden. Anschließend
werden zwei :led-pixel-red:`roten` Drähte mit dem :power-red:`roten` Draht der
Stromversorgung verbunden. Das Kabel wird wie unten abgebildet verlegt.

.. image:: /Images/Kits/kit_blinkenlights_wago_3x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbauschritt Klemmen
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_3x_connected_1200.jpg


.. image:: /Images/Kits/kit_blinkenlights_build_step7_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbauschritt mit 80cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step7_1200.jpg

Danach wird das 55cm Kabel für zwei 3-Draht Klemmen verbunden.

.. image:: /Images/Kits/kit_blinkenlights_build_step8_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbauschritt mit 55cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step8_1200.jpg

Diesen Schritt wiederholen sich mit dem 40cm Kabel.
   
.. image:: /Images/Kits/kit_blinkenlights_build_step9_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbauschritt mit 40cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step9_1200.jpg

Im letzten Verdrahtungsschritt  wird mit 2-Draht Klemmen
der letzten Versorgungspunkt mit dem 20cm Kabel verbunden. 
Dies sieht wie folgt aus:

.. image:: /Images/Kits/kit_blinkenlights_build_step10_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbauschritt mit 20cm Kabel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step10_1200.jpg


5V Stromversorgung vorbereiten
------------------------------

Nun müssen die Stromversorgungskabel verbunden werden.
Dazu wird die 5V Stromversorgung mit zwei 5-Draht Klemmen wie
nachfolgend abgebildet verbunden:

.. image:: /Images/Kits/kit_blinkenlights_wago_power_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Stromversorgungsverbindung
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_power_1200.jpg

Der weiße Draht der Stromversorgung ist der :power-white:`5V` Anschluss und wird
später mit den :power-red:`roten` Drähten verbunden. Der schwarze Draht ist
:power-black:`Masse` und wird mit den :power-black:`schwarzen` Drähten 
verbunden.

Als nächstes werden zwei weitere 5-Draht Klemmen mit diesen Klemmen verbunden.
Dazu wird der zuvor erstellten 10cm Draht verwendet.

.. image:: /Images/Kits/kit_blinkenlights_wago_5x_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Stromversorgungsverdrahtung
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_5x_1200.jpg

Alles verbinden
---------------

Verbinde die zuvor installierten Stromversorgungskabel mit den Klemmen.
Das nachfolgende Foto zeigt den abgeschlossenen Schritt.

.. image:: /Images/Kits/kit_blinkenlights_wago_5x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Stromversorgung verdrahtet
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_5x_connected_1200.jpg


LED Strip Bricklet und Master Brick einbauen
--------------------------------------------

Verbinde das LED Strip Bricklet mit dem Master Brick. Das mitgelieferte 
LED Pixel Verbindungskabel muss abisoliert werden und kann dann
dem LED Strip Bricklet verbunden werden. 7mm reichen aus.

.. image:: /Images/Kits/kit_blinkenlights_master_led_strip_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Master Brick mit LED Strip Bricklet
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_master_led_strip_1200.jpg

Danach wird dieser Aufbau mit dem ersten Pixel verbunden und wie nachfolgend
 dargestellt befestigt:

.. image:: /Images/Kits/kit_blinkenlights_build_step13_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau mit installiertem Master Brick
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step13_1200.jpg


Wandhalterungen montieren
-------------------------

Um die Wandhalterungen an die Rückplatte zu befestigen werden zwei 10mm 
Abstandsbolzen (Innen/Innengewinde) mit zwei M3 schrauben an jede 
Befestigungsplatte geschraubt:

.. image:: /Images/Kits/kit_blinkenlights_holder_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Befestigungsplatte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_holder_1200.jpg

Diese Befestigungsplatten werden wiederum mit M3 Schrauben an die Rückplatte
geschraubt:

.. image:: /Images/Kits/kit_blinkenlights_holder_on_board_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Befestigungsplatte an Rückplatte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_holder_on_board_1200.jpg

Danach sieht die Platte wie folgt aus:

.. image:: /Images/Kits/kit_blinkenlights_on_wall_wo_frontpanel_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit an der Wand ohne Frontplatte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_on_wall_wo_frontpanel_1200.jpg

Der Abstand zwischen den Befestigungshaltern ist 32cm für vertikale
als auch horizontale Montage.

Frontplatte befestigen (Optional)
---------------------------------

Dieser Schritt ist optional. Abhängig von der Anwendung kann die Frontplatte
befestigt werden. Ohne Frontplatte sind die Pixel **sehr hell**.

Das folgende Foto aus dem Tetris Beispiel zeigt das Kit ohne Frontplatte:

.. image:: /Images/Kits/kit_blinkenlights_tetris_wo_frontpanel_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris ohne Frontplatte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_tetris_wo_frontpanel_1200.jpg

Um die Frontplatte zu montieren werden 12mm Abstandsbolzen (Außen-/Innengewinde)
an sechs Stellen montiert. An zwei Stellen sind die Löcher schon durch die
M3 Schrauben der Wandhalterungen belegt. Hier werden die M3 Schrauben einfach
durch die Außengewinde der 12mm Abstandsbolzen ersetzt. An den anderen vier
Stellen wird der Abstandsbolzen mit dem Außengewinde durch die Rückplatte
gesteckt und mit einer Mutter fixiert.

.. image:: /Images/Kits/kit_blinkenlights_mounting_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Aufbau Montage Frontplatte
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_mounting_1200.jpg

Anschließend wird die Frontplatte mit Schrauben an den sechs Abstandsbolzen
befestigt:

.. image:: /Images/Kits/kit_blinkenlights_on_wall_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit an der Wand
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_on_wall_1200.jpg

Wenn das Kit dazu genutzt werden soll um pixelbasierte Anwendungen wie Text
oder Spiele anzuzeigen kann die Frontplatte direkt an die sechs 12mm 
Abstandshalter montiert werden. Für diffuse Anwendungen, wie unser 
Feuerbeispiel, ist ein größerer Abstand zwischen den Pixeln und der Platte 
notwendig. Dazu werden zusätzliche Abstandshalter genutzt. In unseren Beispielen
nutzen wir zwei 9mm Abstandshalter und ein 12mm Abstandshalter zusätzlich zu dem
bereits installierten 12mm Abstandshalter an jeder der sechs Positionen.

Das nachfolgende Regenbogenbeispiel wurde einmal mit 12mm Abstandshaltern im
Tageslicht, mit 2x12mm und 2x9mm Abstandshaltern im Tageslicht und mit
2x12mm und 2x9mm Abstandshaltern in Dunkelheit aufgenommen:

.. image:: /Images/Kits/kit_blinkenlights_rainbow_near_far_dark_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Regenbogen
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_rainbow_near_far_dark_1200.jpg
