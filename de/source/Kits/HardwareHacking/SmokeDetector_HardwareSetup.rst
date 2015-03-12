
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Hardware-Aufbau: Rauchmelder

.. _starter_kit_hardware_hacking_smoke_detector_hardware_setup:

Hardware-Aufbau: Rauchmelder
============================

Typischerweise ist ein Rauchmelder mit einer oder mehreren LEDs ausgestattet,
die den Zustand repräsentieren. Die Anzahl und das Verhalten der LEDs hängt
vom Modell ab.

In diesem Beispiel nutzen wir einen 
`ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
Rauchmelder. Dieser Rauchmelder ist drahtlos vernetzbar. Das heißt, dass
Rauchmelder in verschiedenen Räumen installiert werden können und alle auslösen
wenn ein Melder Rauch detektiert.
Wir können einen Rauchmelder hacken und diesen in der Nähe eines PCs 
installieren, so dass dieser von anderen Rauchmeldern im Haus ausgelöst 
werden kann. Auf diesem Wege können wir mitlesen ob die Rauchmelder ausgelöst 
wurden.

Das Innenleben des Rauchmelders
-------------------------------

Der ELRO FA20RF/2 besitzt zwei LEDs in der Nähe der "TEST" und "LEARN" 
Taster.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_leds_closeup_350.jpg
   :scale: 100 %
   :alt: Rauchmelder LEDs
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_600.jpg

Wenn wir einen Testalarm auslösen können wir sehen das die LED auf der rechten
Seite grün blinkt wenn der Alarm ausgelöst wurde.

Nachdem wir nun die LED ausfindig gemacht haben die den Zustand abbildet, 
wollen wir diese auslesen. Dazu öffnen wir das Gehäuse:

.. image:: /Images/Kits/hardware_hacking_smoke_detector_open_350.jpg
   :scale: 100 %
   :alt: Rauchmelder geöffnet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_open_1200.jpg

Die besagte LED ist die transparente LED oben rechts. Es ist eine zwei-farbige
LED, sie kann grün sowie rot blinken. Wir müssen als nächstes die Pins ausfindig 
machen die die LED grün blinken lässt.

Da die LED bedrahtet ist (nicht SMD) befinden sich die Kontakte an der 
Unterseite.

Um an die Unterseite zu gelangen müssen wir die Schrauben entfernen.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_inside_350.jpg
   :scale: 100 %
   :alt: Rauchmelder Unterseite geöffnet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_inside_1200.jpg

Die drei Pads oben im Bild, links neben dem roten Aufkleber gehören zur LED.
An diese müssen wir Drähte anlöten.

Drähte an die LED und dessen Vorwiderstand anlöten
--------------------------------------------------

:ref:`Hier <starter_kit_hardware_hacking_for_beginners_soldering>`
gibt es ein kleines Löt-Tutorial und 
:ref:`hier <starter_kit_hardware_hacking_for_identify_series_resistor>` 
Anweisungen wie die korrekten Pins einer LED und dessen Vorwiderstand gefunden 
werden können.

Die transparente LED des ELRO FA20RF/2 besteht aus zwei LEDs (grün, rot) die
in einem gemeinsamen Gehäuse untergebracht sind. Beide LEDs besitzen einen 
gemeinsamen Pin (der mittlere) und jeweils einen eigenen (Pin rechts, links).
Um die grüne LED leuchten zu lassen wird der linke Pin benutzt.


.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_350.jpg
   :scale: 100 %
   :alt: Geöffneter Rauchmelder mit angelöteten Drähten
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_1200.jpg

Wir löten einen Draht an den mittleren Pin an und verfolgen die Leiterbahn des 
linken Pads bis zu einem Widerstand (in rot
markiert). An dessen Ende löten wir den anderen Draht an.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_350.jpg
   :scale: 100 %
   :alt: Nahaufnahme: Geöffneter Rauchmelder mit angelöteten Drähten
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_soldered_closeup_w_trace_1200.jpg

Anschließend können wir die Leiterplatte wieder in das Gehäuse schrauben.
Die beiden Drähte werden an + und - von Eingang 0 des Industrial Digital In 4
Bricklets angeschlossen. Ob die Polarität stimmt können wir später mit dem
Brick Viewer überprüfen.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Geöffneter Rauchmelder mit angelöteten Drähten und verbundenem Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

Als nächstes können wir den gehackten Rauchmelder testen. Um dies zu tun 
drücken wir den Test-Knopf woraufhin die Reaktion der LED im Brick Viewer
angezeigt werden sollte.

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: Brick Viwer: Industrial Digital In 4
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

Wenn sich der Zustand des Eingangs im Brick Viewer nicht verändert müssen
die beiden Drähte getauscht werden.

