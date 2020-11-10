
:DISABLED_shoplink: ../../../shop/bricklets/servo-v2-bricklet.html

.. include:: Servo_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _servo_v2_bricklet:

Servo Bricklet 2.0
==================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_servo_v2_tilted_[?|?].jpg           Servo Bricklet 2.0
	Bricklets/bricklet_servo_v2_horizontal_[?|?].jpg       Servo Bricklet 2.0
	Bricklets/bricklet_servo_v2_master_[100|600].jpg       Servo Bricklet 2.0 mit Master Brick
	Cases/bricklet_servo_v2_case_[100|600].jpg             Servo Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_servo_v2_brickv_[100|].jpg          Servo Bricklet 2.0 im Brick Viewer
	Dimensions/servo_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Steuert bis zu **10** RC Servos
* Brushless Motoren über externe ESCs ebenfalls steuerbar
* Einstellbare Periode und Pulsweite
* Benutzt Motion Planning für ruckelfreie Bewegungen
* Position und Geschwindigkeit/Verzögerung können konfiguriert werden
* Strommessung auf jedem individuellen Servo-Kanal


.. _servo_v2_bricklet_description:

Beschreibung
------------

Das Servo :ref:`Bricklet <primer_bricklets>` 2.0 kann bis zu **10**
`RC Servos <https://de.wikipedia.org/wiki/Servo>`__ steuern. Eine API für
:ref:`viele Programmiersprachen <servo_brick_programming_interface>` ermöglichen 
das Steuern der Position, Geschwindigkeit und Beschleunigung/Verzögerng der angeschlossenen
Servos. Motion Planning wird genutzt um neue Positionen ruckelfrei anzufahren. 
Zusätzlich kann die PWM (Pulsweite und Preiod) jedes Servos einzeln konfiguriert werden.

Modellbau-Fahrtenregler (Electronic Speed Controller - ESC) können anstatt der
Servos angeschlossen werden und ermöglichen es andere Motoren, wie z.B. 
Brushless Motoren, zu steuern. Es muss nur der richtige ESC abhängig vom Motor
gewählt werden, so dass auch Motoren mit einem Stromverbrauch von 150A und 
mehr steuerbar sind.

Die Versorgung der Servos erfolgt entweder eine externe Stromversorgung
(schwarze Stromversorgungsbuchse). Die Eingangsspannung wird direkt mit
den Servos verbunde.


Technische Spezifikation
------------------------

===================================== ================================================================
Eigenschaft                           Wert
===================================== ================================================================
Stromverbrauch                        75mW (15mA at 5V)
Eingangsspannung                      5V-24V (wird direkt mit den Servos verbunden)
------------------------------------- ----------------------------------------------------------------
------------------------------------- ----------------------------------------------------------------
Ausgangsperiode*                      1µs - 65535µs
Pulsweite*                            1µs - 65535µs
Geschwindigkeit*                      0 - 500000 °/100s
Beschleunigung*                       0 - 500000 °/100s²
Verzötgerung*                         0 - 500000 °/100s²
------------------------------------- ----------------------------------------------------------------
------------------------------------- ----------------------------------------------------------------
Abmessungen (B x T x H)               40 x 40 x 10mm (1,57 x 1,57 x 0,39")
Gewicht                               9g
===================================== ================================================================

\* einstellbar pro Servo


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/servo-v2-bricklet/raw/master/hardware/servo-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/servo_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/servo-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _servo_v2_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit des
Servo Bricklet 2.0.

.. image:: /Images/Bricks/bricklet_servo_v2_caption_600.jpg
   :scale: 100 %
   :alt: Servo Bricklet 2.0 mit Beschriftung
   :align: center
   :target: ../../_images/Bricks/bricklet_servo_v2_caption_800.jpg

.. _servo_v2_bricklet_test:


Erster Test
-----------

|test_intro|

Schließe einen RC Servo und eine passende Stromversorgung an den Brick an.
Der Aufbau sollte dem im folgenden Bild ähnlich sehen.

.. image:: /Images/Bricks/bricklet_servo_v2_setup_600.jpg
   :scale: 100 %
   :alt: Servo Bricklet 2.0 mit Servo
   :align: center
   :target: ../../_images/Bricks/bricklet_servo_v2_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricklets/bricklet_servo_v2_brickv.jpg
   :scale: 100 %
   :alt: Servo Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_servo_v2_brickv.jpg

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


.. _servo_v2_bricklet_configure_servo_pwm:

Servo PWM einstellen
--------------------

Typischerweise wird ein RC Servo über ein PWM Signal mit 20ms Periode und
1ms bis 2ms Pulsweite gesteuert. Dabei definiert die Pulsweite die gewünschte
Position. Es gibt aber auch Servos die nicht diesem Standard entsprechen, daher
erlaubt das Servo Bricklet 2.0 alle Parameter des PWM Signals zu konfigurieren.

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


Brushless Motoren mit ESCs verwenden
------------------------------------

Mit dem Servo Bricklet 2.0 können bis zu 10 Brushless Motoren mittels externen
Electronic Speed Controllern (ESC) gesteuert werden. Dazu muss einfach der
Brushless Motor an den ESC und der ESC an den Servo Bricklet 2.0 angeschlossen werden.
Mit diesem Aufbau ist der maximale Motorstrom nur durch den verwendeten ESC
beschränkt.

.. warning::
 Viele ESCs haben eingebaute Battery Eliminator Circuits (BEC) die verwendet
 werde können um RC Empfänger zu versorgen. Falls ein ESC mit BEC verwendet wird
 dann muss diese unbedingt abgeschaltet werden. Andernfalls kann der ESC oder
 den Servo Bricklet 2.0 zerstört werden. Um die BEC abzuschalten darf das rote Kabel
 des ESC nicht an den Servo Bricklet 2.0 angeschlossen werden
 (`externes Videotutorial <https://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

.. warning::
 Falls die gleiche Stromversorgung für den ESC und den Servo Bricklet 2.0
 verwendet wird, dann darf auch das schwarze Kabel (GND) nicht an den
 Servo Bricklet 2.0 angeschlossen werden. Andernfalls kann der Motorstrom über das
 GND Kabel fließen und die Strommessschaltung auf dem Servo Bricklet 2.0 zerstört
 werden.


Andere Hardware anschließen
---------------------------

Es können auch andere Geräte wie z.B. Lüfter mit PWM Eingang (nicht zu 
verwechseln mit Tachoausgang) gesteuert werden.

Zur Verwendung eines 12V/24V Lüfters muss ein 12V/24V Netzteil am
Schwarzen Spannungseingangsstecker angeschlossen werden. Die Kontroll-PWM
des Lüfters muss allerdings einen High-Pegel von 5V und einen Low-Pegel von 0V
unterstützen. Die meisten PWM-kontrollierbaren Lüfter unterstützen dies,
allerdings sollte das vorher im Datenblatt des Lüfters überprüft werden.

TODO: Bild/Vide + Beispielkonfiguriation

.. _servo_v2_bricklet_case:

Gehäuse
-------

TBD

..
	Ein `laser-geschnittenes Gehäuse für das Servo Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-servo-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_servo_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Servo Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_servo_v2_case_1000.jpg

	.. include:: Servo_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/servo_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Servo Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/servo_v2_exploded.png

	|bricklet_case_hint|


.. _servo_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Servo_V2_hlpi.table


FAQ
---

Die Servos stottern
^^^^^^^^^^^^^^^^^^^

Die häufigste Ursache ist ein Spannungsabfall, verursacht durch wiederholte
Spitzen im Stromverbrauch der angeschlossenen Servos.

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
