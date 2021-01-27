
.. include:: Servo_Brick.substitutions


.. _servo_brick:

Servo Brick
===========

.. raw:: html

	{% tfgallery %}

	Bricks/brick_servo_tilted_front_[?|?].jpg        Servo Brick
	Bricks/brick_servo_tilted_back_[?|?].jpg         Servo Brick
	Bricks/brick_servo_setup_[?|?].jpg               Servo Brick mit Servo
	Bricks/brick_servo_setup_big_[?|?].jpg           Servo Brick mit Servos
	Bricks/brick_servo_caption_[?|?].jpg             Servo Brick mit Beschriftung
	Bricks/brick_servo_top_[?|?].jpg                 Servo Brick Oberseite
	Bricks/brick_servo_bottom_[?|?].jpg              Servo Brick Unterseite
	Dimensions/servo_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Der Servo Brick ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`Servo Bricklet 2.0 <servo_v2_bricklet>`
 empfohlen.

Features
--------

* Steuert bis zu **7** RC Servos mit max. **3A** über USB
* Brushless Motoren über externe ESCs ebenfalls steuerbar
* API für viele Programmiersprachen verfügbar
* Unterstützt TurboPWM
* Über API einstellbare Servospannung, Periode und Pulsweite
* Position, Geschwindigkeit und Beschleunigung steuerbar
* Erweiterbar über zwei Bricklet Anschlüsse


.. _servo_brick_description:

Beschreibung
------------

Der Servo :ref:`Brick <primer_bricks>` kann bis zu **7**
`RC Servos <https://de.wikipedia.org/wiki/Servo>`__ mit einem maximalen Strom
von **3A** per **USB** steuern. Eine API für
:ref:`viele Programmiersprachen <servo_brick_programming_interface>` ermöglichen 
das Steuern der Position, Geschwindigkeit und Beschleunigung der angeschlossenen
Servos. Die Ausgangsspannung ist ebenfalls per API einstellbar (max. **9V**), 
der Stromverbrauch jedes Servos kann einzeln gemessen werden. Zusätzlich kann die 
PWM jedes Servos einzeln konfiguriert werden.

Modellbau-Fahrtenregler (Electronic Speed Controller - ESC) können anstatt der
Servos angeschlossen werden und ermöglichen es andere Motoren, wie z.B. 
Brushless Motoren, zu steuern. Es muss nur der richtige ESC abhängig vom Motor
gewählt werden, so dass auch Motoren mit einem Stromverbrauch von 150A und 
mehr steuerbar sind.

Über zwei Anschlüsse können :ref:`Bricklets <primer_bricklets>` 
angeschlossen werden, die die Fähigkeiten des Bricks erweitern. Der Servo 
Brick kann mit anderen Bricks in einem :ref:`Stapel <primer_stack>` genutzt 
werden. Zum Beispiel
kann ein zusätzlicher :ref:`Master Brick <master_brick>` mit
:ref:`Master Extensions <primer_master_extensions>` genutzt werden,
um die USB Verbindung durch andere kabelgebundene Schnittstellen 
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
oder drahtlose Schnittstellen (:ref:`WLAN <wifi_extension>`) zu ersetzen.

Die Versorgung der Servos erfolgt entweder über eine externe Stromversorgung
(schwarze Stromversorgungsbuchse), die direkt an den Brick angeschlossen wird, 
oder über die interne Stromversorgung des Stapels. Der Brick schaltet 
automatisch auf externe Stromversorgung um, sobald eine angeschlossen wird.


Technische Spezifikation
------------------------

===================================== ================================================================
Eigenschaft                           Wert
===================================== ================================================================
Maximaler Motorstrom (Summe)          3A
Eingangsspannung                      5V - 25V (mindestens 1V höher als eingestellte Ausgangsspannung)
Ausgangsspannung                      2V - 9V (über Software einstellbar)
------------------------------------- ----------------------------------------------------------------
------------------------------------- ----------------------------------------------------------------
Ausgangsperiode*                      1µs - 65535µs
Pulsweite*                            1µs - 65535µs
Geschwindigkeit*                      0 - 65535 °/100s
Beschleunigung*                       1 - 65535 °/100s²
------------------------------------- ----------------------------------------------------------------
------------------------------------- ----------------------------------------------------------------
Bricklet Anschlüsse                   2
Abmessungen (B x T x H)               40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                               18g
Stromverbrauch                        60mA
===================================== ================================================================

\* einstellbar pro Servo


Ressourcen
----------

* MCP3008 Datenblatt (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/datasheets/MCP3008.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/hardware/servo-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/servo_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/servo-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BVF58T>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/servo/servo.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/servo/servo.FCStd>`__)


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
`PWM <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`__ Pulsweite
eingestellt und der Winkelbereich definiert werden. Zusätzlich wird der
Stromverbrauch des Servos angezeigt. Weiter unten finden sich vier Regler mit
denen Position, Geschwindigkeit und Beschleunigung des Servos kontrolliert
werden können. Der vierte Regler dient zur Einstellung der PWM Periode
(siehe :ref:`Servo PWM einstellen <servo_brick_configure_servo_pwm>` für
weiterführenden Information).

Auf der rechten Seite wird die externe und die Versorgungsspannung des Stapels
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
allen bisher getesteten Servos (20ms funktioniert mit einigen chinesischen
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
Ausgangsspannung für die Servos einzustellen. Die interne Stromversorgung
kann entweder über den schwarzen Stromversorgungsstecker auf der Platine
versorgt werden oder über eine :ref:`Stromversorgung
<primer_power_supplies>` die unter den Brick gesteckt wird.
Der Brick schaltet von selbst auf extern Versorgungen um, wenn am schwarzen
Stecker eine Spannung anliegt. Da die interne Stromversorgung einen Step-Down
Regler verwendet muss die Eingangsspannung am schwarzen Stromversorgungsstecker
1V höher sein als die eingestellt Ausgangsspannung für die Servos. Andernfalls
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
 der Servo Brick zerstört werden. Um die BEC abzuschalten darf das rote Kabel
 des ESC nicht an den Servo Brick angeschlossen werden
 (`externes Videotutorial <https://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

.. warning::
 Falls die gleiche Stromversorgung für den ESC und den Servo Brick
 verwendet wird, dann darf auch das schwarze Kabel (GND) nicht an den
 Servo Brick angeschlossen werden. Andernfalls kann der Motorstrom über das
 GND Kabel fließen und die Strommessschaltung auf dem Servo Brick zerstört
 werden.


Andere Hardware anschließen
---------------------------

Es können auch andere Geräte wie z.B. Lüfter mit PWM Eingang (nicht zu 
verwechseln mit Tachoausgang) gesteuert werden. Diese dürfen nur direkt über das 
Servo Brick mit Strom versorgt werden, wenn die normale Gerätespannung unter 9V 
liegt. 

Möchte man z.B. einen 12V Lüfter betreiben, so sollte dieser nicht über 
das Servo Brick versorgt werden! Auftretende Spannungsspitzen können dazu 
führen, dass die Maximalspannung von 10V (definiert durch einen verbauten 
Tantal-Kondensator) überschritten wird und der Tantal-Kondensator explodiert!
Um dies zu verhindern sollte der Lüfter extern über 12V versorgt werden 
(12V, Masse). Das PWM Signal kommt dann vom Servo Brick. 
Masse muss ebenfalls mit dem Servo Brick verbunden werden.


Fehler LED
----------

Die rote LED leuchtet wenn die Versorgungsspannung unter das einstellbaren
Minimum fällt.


.. _servo_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Servo_Brick_hlpi.table


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
