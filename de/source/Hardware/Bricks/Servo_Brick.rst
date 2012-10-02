.. include:: Servo_Brick.substitutions


.. _servo_brick:

Servo Brick
===========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_servo_tilted_front_350.jpg",
	               "Bricks/brick_servo_tilted_front_600.jpg",
	               "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_tilted_back_100.jpg",
	             "Bricks/brick_servo_tilted_back_600.jpg",
	             "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_100.jpg",
	             "Bricks/brick_servo_setup_600.jpg",
	             "Servo Brick mit Servo")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_big_100.jpg",
	             "Bricks/brick_servo_setup_big_600.jpg",
	             "Servo Brick mit Servos")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_caption_100.jpg",
	             "Bricks/brick_servo_caption_600.jpg",
	             "Servo Brick mit Beschriftung")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_top_100.jpg",
	             "Bricks/brick_servo_top_600.jpg",
	             "Servo Brick Oberseite")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_bottom_100.jpg",
	             "Bricks/brick_servo_bottom_600.jpg",
	             "Servo Brick Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/servo_brick_dimensions_100.png",
	             "Dimensions/servo_brick_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Steuert bis zu **7** RC Servos mit max. **3A**
* Steuert Brushless Motoren (benötigt externe ESC)
* Unterstützt `TurboPWM <http://wiki.openpilot.org/display/Doc/TurboPWM>`__
* Software einstellbare Servospannung, Periode und Pulsweite
* Position, Geschwindigkeit und Beschleunigung steuerbar
* Eine USB und zwei Bricklet Schnittstellen


Beschreibung
------------

Der Servo :ref:`Brick <product_overview_bricks>` ist mit einem 32-Bit
ARM Mikrocontroller ausgestattet und kann bis zu **7**
`RC Servos <http://de.wikipedia.org/wiki/Servo>`__
mit einem maximalen Strom bis zu **3A** steuern.
Die Ausgangsspannung ist einstellbar bis zu **9V**, der Stromverbrauch jedes
Servos kann einzeln gemessen werden.
Zusätzlich kann die PWM jedes Servos einzeln konfiguriert werden.

Über einen zusätzlichen Modellbau Fahrtenregler (Electronic Speed
Controller - ESC) ist es möglich Brushless Motoren zu steuern.
Es muss nur der richtige ESC abhängig vom Motor gewählt werden, so dass auch
Motoren mit einem Stromverbrauch von 150A und mehr steuerbar sind.

Der Brick ist kompatibel zu anderen Tinkerforge
:ref:`Bricks <product_overview_bricks>`
und kann in einem Stapel benutzt werden.
Über zwei Anschlüsse können :ref:`Bricklet <product_overview_bricklets>`
angeschlossen werden.

Die Versorgung der Servos erfolgt entweder über eine externe Stromversorgung
die direkt an den Brick angeschlossen wird oder über die interne
Stromversorgung des Stapels.
Der Brick schaltet automatisch auf externe Stromversorgung um, sobald eine
angeschlossen wird.

Über eine **USB** Verbindung kann der Brick von einem PC gesteuert werden.
Über einen zusätzlichen Master Brick mit Master Extension ist es möglich diese
USB Verbindung durch kabelgebundene Schnittstellen (**RS485**, **Ethernet**)
oder drahtlose Schnittstellen (**WLAN**) zu ersetzen
(:ref:`High Level Konzept <pi_hlpi>`).

Da die Firmware Open Source ist, ist es natürlich auch möglich den Brick direkt
zu programmieren (:ref:`On Device Programmierung <pi_odpi>`).
Momentan bieten wir keine On Device API an.


Technische Spezifikation
------------------------

===================================== ============================================================
Eigenschaft                           Wert
===================================== ============================================================
Mikrocontroller                       ATSAM3S2B (128kB Flash, 32kB RAM)
Stromverbrauch                        60mA
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Maximaler Motorstrom (Summe)          3A
Minimale/Maximale Eingangsspannung    5V/25V
Ausgangsspannung                      Über Software einstellbar 2V - 9V
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Ausgangsperiode*                      1µs - 65535µs
Pulsweite*                            1µs - 65535µs
Geschwindigkeit*                      0 - 65535 °/100s
Beschleunigung*                       1 - 65535 °/100s²
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Bricklet Anschlüsse                   2
Abmessungen (B x T x H)               40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                               18g
===================================== ============================================================

\* einstellbar pro Servo


Ressourcen
----------

* MCP3008 Datenblatt (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/datasheets/MCP3008.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/hardware/servo-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/servo_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/servo-brick/zipball/master>`__)


.. _servo_brick_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Servo Bricks.

.. image:: /Images/Bricks/brick_servo_caption_600.jpg
   :scale: 100 %
   :alt: Servo Brick mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/brick_servo_caption_800.jpg


.. _servo_brick_test:

Erster Test
-----------

|test_intro|

Schließe einen RC Servo und eine passende Stromversorgung an den Brick an.
Der Aufbau sollte dem im folgenden Bild ähnlich sehen.

.. image:: /Images/Bricks/brick_servo_setup_600.jpg
   :scale: 100 %
   :alt: Servo Brick mit Servo
   :align: center
   :target: ../../_images/Bricks/brick_servo_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/servo_brickv.jpg
   :scale: 100 %
   :alt: Servo Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/servo_brickv.jpg

Auf der linke Seite des Tabs kann der einzustellende Servo ausgewählt werden.
Dieser kann ein- und ausgeschaltet, die zulässige
`PWM <http://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Pulsweite
eingestellt und der Winkelbereich definiert werden. Zusätzlich wird der
Stromverbrauch des Servos angezeigt. Weiter unten finden sich vier Regler mit
denen Position, Geschwindigkeit und Beschleunigung des Servors kontrolliert
werden können. Der vierte Regler dient zur Einstellung der PWM Periode
(siehe :ref:`Servo PWM einstellen <servo_brick_configure_servo_pwm>` für
weiterführenden Information).

Auf der rechten Seite wird die externe und die Versorgungsspannung des Staples
angezeigt. Darunter findet sich eine graphische Darstellung des Zustandes jedes
Servos. Ganz unten können die Mindesteingangsspannung und die Ausgangsspannung
eingestellt werden. Wird die Mindesteingangsspannung unterschritten wird der
Undervoltage Callback ausgelöst.

.. warning::
 Eine zu hohe Ausgangsspannung kann den Servo beschädigen!

Unten rechts ist der "Start Test" Knopf, dieser startet eine Testsequenz bei der
alle Servos zufällige Bewegungen ausführen.

|test_pi_ref|


.. _servo_brick_configure_servo_pwm:

Servo PWM einstellen
--------------------

Typischerweise wird ein RC Servo über ein PWM Signal mit 20ms Periode und
1ms bis 2ms Pulsweite gesteuert. Dabei definiert die Pulsweite die gewünschte
Position. Es gibt aber auch Servos die nicht diesem Standard entsprechen, daher
erlaubt der Servo Brick alle Parameter des PWM Signals zu konfigurieren.

Der Standardwert für die Periode ist 19,5ms. Diese Periode funktioniert mit
allen bisher getesteten Servors (20ms funktioniert mit einigen chinesischen
Servos nicht zuverlässig). Falls im Datenblatt des Servos eine Periode angeben
ist sollte dieser Wert auch eingestellt werden. Es ist allerdings eher
unwahrscheinlich, dass dieser Wert verändert werden muss.

Eher interessant ist die minimale und maximale Pulsweite. Der Standardbereich
ist 1ms bis 2ms. Die meisten Servos können aber auch einen größeren Winkelbereich
fahren wenn der Bereich der Pulsweite vergrößert wird. Falls im Datenblatt des
Servos eine Angabe über die zulässige Pulsweite gemacht ist sollte diese
entsprechend eingestellt werden. Falls der zulässige Bereich der Pulsweite unbekannt
ist können die richtigen Werte durch Ausprobieren angenähert werden. Dazu muss
der Bereich solange vergrößert werden bis der Servo anfängt zu stottern. Der
zulässige Bereich sind dann der nächste kleiner, bei dem der Servo noch nicht
stottert.

.. warning::
 Einen Servo über längere Zeit mit einer falsch eingestellten PWM zu betreiben
 kann den Servo beschädigen.


Stromversorgung
---------------

Der Servo Brick hat eine interne Stromversorgung, die es ermögliche die
Ausgangsspannung für die Servors einzustellen. Die interne Stromversorgung
kann entweder über den schwarzen Stromversorgungsstecker auf der Platine
versorgt werden oder über eine :ref:`Stromversorgung
<product_overview_power_supplies>` die unter den Brick gesteckt wird.
Der Brick schaltet von selbst auf extern Versorgungen um, wenn am schwarzen
Stecker eine Spannung anliegt. Da die interne Stromversorgung einen Step-Down
Regler verwendet muss die Eingangsspannung am schwarzen Stromversorgungsstecker
1V höher sein als die eingestellt Ausgangsspannung für die Servors. Andernfalls
ist ein stabiler Betrieb nicht gewährleistet.

.. warning::
 Eine zu hohe Ausgangsspannung kann den Servo beschädigen!


Brushless Motoren mit ESCs verwenden
------------------------------------

Mit dem Servo Brick können bis zu 7 Brushless Motoren mittels externen
Electronic Speed Controllern (ESC) gesteuert werden. Dazu muss einfach der
Brushless Motor an den ESC und der ESC an den Servo Brick angeschlossen werden.
Mit diesem Aufbau ist der maximale Motorstrom nur durch den verwendeten ESC
beschränkt.

.. warning::
 Viele ESCs haben eingebaute Battery Eliminator Circuits (BEC) die verwendet
 werde können um RC Empfänger zu versorgen. Falls ein ESC mit BEC verwendet wird
 dann muss diese unbedingt abgeschaltet werden. Andernfalls kann der ESC oder
 der Servo Brick zerstört werden. Um die BEC abzuschalten darf das rote Kakel
 des ESC nicht an den Servo Brick angeschlossen werden
 (`externes Videotutorial <http://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

.. warning::
 Falls die gleiche Stromversorgungen für den ESC und den Servo Brick
 verwendet wird, dann darf auch das schwarze Kabel (GND) nicht an den
 Servo Brick angeschlossen werden. Es scheint so, dass die meisten ESCs ihren
 Strom nicht über deren eigene Stromversorgungen, sondern über den GND Pin des
 Servo Bricks beziehen. Dies kann zur Zerstörung des Servo Bricks führen. Daher
 sollte beim ersten Test die Strommessung im Brick Viewer im Auge behalten werden.


Fehler LED
----------

Die rote LED leuchtet wenn die Versorgungsspannung unter das einstellbaren
Minimum fällt.


.. _servo_brick_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Servo_Brick_hlpi.table


On Device Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
 In Kürze!

 Eine API und Dokumentation um direkt auf dem Mikrocontroller zu programmieren
 (vergleichbar mit Arduino) ist geplant.
 Bis es soweit ist kann unsere Firmware als Grundlage für eigene Modifikationen
 verwendet werden (C Kenntnisse vorausgesetzt).

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"


FAQ
---

Die Servos stottern
^^^^^^^^^^^^^^^^^^^

Die häufigste Ursache ist ein Spannungsabfall, verursacht durch wiederholte
Spitzen im Stromverbrauch der angeschlossenen Servos. Als erstes sollte
sichergestellt werden, dass die Eingangspannung des Servo Bricks um mindestens
1V höher liegt als die eingestellte Ausgangsspannung.

Üblicherweise tritt diese Problem auf, wenn die Stromversorgung Spitzen im
Stromverbrauch nicht verträgt. Um die Stromversorgung als Ursache
auszuschließen können testweise Batterien als Stromversorgung verwendet werden.
Diese haben normalerweise kein Problem mit Spitzen im Stromverbrauch.

Falls schon Batterien verwendet werden und das Problem weiterhin auftritt, dann
sollte als nächstes sichergestellt werden, dass die Batterien voll geladen sind.
Falls die Batterien zu schwach sind fällt deren Spannung ab.

Wenn die Servos nur anfangen zu stottern wenn sie den minimalen oder maximalen
Winkel erreichen, dann ist der Bereich der zulässigen Pulsweite zu groß
eingestellt. In diesem Fall musst der Bereich der Pulsweite verringert werden.
Anderenfalls können deine Servos beschädigt werden, wenn dieser Zustand längere
Zeit anhält.
