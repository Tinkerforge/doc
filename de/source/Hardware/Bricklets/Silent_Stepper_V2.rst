
:DISABLED_shoplink: ../../../shop/bricklets/silent-stepper-v2-bricklet.html

.. include:: Silent_Stepper_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _silent_stepper_v2_bricklet:

Silent Stepper Bricklet 2.0
===========================


.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_silent_stepper_v2_tilted_[?|?].jpg           Silent Stepper Bricklet 2.0
	Bricklets/bricklet_silent_stepper_v2_horizontal_[?|?].jpg       Silent Stepper Bricklet 2.0
	Bricklets/bricklet_silent_stepper_v2_master_[100|600].jpg       Silent Stepper Bricklet 2.0 mit Master Brick
	Cases/bricklet_silent_stepper_v2_case_[100|600].jpg             Silent Stepper Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_silent_stepper_v2_brickv_[100|].jpg          Silent Stepper Bricklet 2.0 im Brick Viewer
	Dimensions/silent_stepper_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Steuert einen bipolaren Schrittmotor über USB (max. **46V**, **1,6A** pro Phase)
* Lautloser Betrieb von Schrittmotoren
* Position, Geschwindigkeit und Beschleunigung sind steuerbar
* Schrittmotor-Auflösung von Vollschritt bis zu 1/256-Schritt


.. _silent_stepper_v2_bricklet_description:

Beschreibung
------------

Das Silent Stepper :ref:`Bricklet <primer_bricklets>` 2.0 kann einen bipolaren
`Schrittmotor <https://de.wikipedia.org/wiki/Schrittmotor>`__ mit einem 
maximalen Phasenstrom von **1,6A** und einer maximalen Spannung von **46V**
steuern. Die API des Bricks ist für verschiedene  
:ref:`Programmiersprachen <silent_stepper_brick_programming_interface>` verfügbar und kann
Richtung, Geschwindigkeit und Beschleunigung des angeschlossenen Schrittmotors steuern.
Die Schrittweite kann zwischen Vollschritt und 1/256-Schrittmodus gewählt werden.

Das Silent Stepper Bricklet 2.0 kann in verschiedenen Modi betrieben werden. Im Stealth Modus 
ist der Motor vollständig lautlos, im Coolstep Modus wird Energie gespart und im Classic Modus
bietet der Motor maximalen Drehmoment. Das Silent Stepper Bricklet 2.0 kann konfiguriert werden,
abhängig von der Motorgeschwindigkeit, automatisch zwischen diesen Modi zu wechseln.

Das Performance DC Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    100mW (20mA bei 5V) ohne Motor
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximaler Motorstrom pro Phase    1.6A
Minimum/Maximum Eingangsspannung  8V/46V
Schrittauflösung                  1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/256
Maximale Geschwindigkeit          0 bis 65535, einstellbares Limit, in Schritte/s
Maximale Beschleunigung           0 bis 65535, einstellbares Limit, in Schritte/s²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 15mm (1,57 x 1,57 x 0,59")
Gewicht                           12g
================================  ============================================================


Ressourcen
----------

* TMC2130 datasheet (`Download <https://github.com/Tinkerforge/silent-stepper-v2-bricklet/raw/master/datasheets/TMC2130_datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/silent-stepper-v2-bricklet/raw/master/hardware/silent-stepper-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/silent_stepper_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/silent-stepper-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _silent_stepper_v2_bricklet_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeiten des Silent Stepper Bricklet 2.0.

.. image:: /Images/Bricklets/bricklet_silent_stepper_v2_caption_600.jpg
   :scale: 100 %
   :alt: Silent Stepper Bricklet 2.0 mit Beschreibung
   :align: center
   :target: ../../_images/Bricklets/bricklet_silent_stepper_v2_caption_800.jpg


.. _silent_stepper_v2_bricklet_test:

Erster Test
-----------

|test_intro|

Verbinde einen Schrittmotor mit dem Bricklet und eine passende Stromversorgung an
das Bricklet an (siehe :ref:`here <silent_stepper_brick_connectivity>`).
Der Aufbau sollte dem im folgenden Bild ähnlich sehen.

.. image:: /Images/Bricklets/bricklet_silent_stepper_v2_motor_setup_600.jpg
   :scale: 100 %
   :alt: Silent Stepper Bricklet 2.0 mit motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_silent_stepper_v2_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricklets/bricklet_silent_stepper_v2_brickv.jpg
   :scale: 100 %
   :alt: Silent Stepper Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_silent_stepper_v2_brickv.jpg

Auf der linken Seite des Tabs kann die Treiberstufe ein- und ausgeschaltet,
sowie die maximale Geschwindigkeit, Beschleunigung und Verzögerung eingestellt werden.
Darunter sind drei Knöpfe um die Drehrichtung des Schrittmotors zu kontrollieren
sowie diesen zu stoppen. Wenn der "Forward" Kopf geklickt wird, dann wird die
Geschwindigkeit des Schrittmotors bis zur "Max Velocity" mit der eingestellten
Beschleunigung erhöht. Ein Klick auf den "Stop" Knopf verringert die
Geschwindigkeit auf "0" mit der eingestellten Verzögerung.

Weiter unten kann die Schrittmodus (Voll- bis 1/256 Schritt)
eingestellt sowie eine Vollbremsung ausgelöst werden, die den Motor sofort
anhält.

Alternativ kann der Schrittmotor auch zu einer bestimmten Position (gemessen
in Schritten) gefahren werden. Dazu einfach bei "Drive To" die Position eingeben
und "Go" klicken. Der Schrittmotor kann ebenfalls eine bestimmte Anzahl Schritte
gefahren werden. Bei diesen beiden Fahrweisen werden auch die Einstellungen für
die maximale Geschwindigkeit, Beschleunigung und Verzögerung berücksichtigt.

Auf der rechten Seite werden die aktuelle Position, die noch zu fahrenden
Schritte sowie die Versorgungsspannung des Stapels und die externe
Versorgungsspannung angezeigt. Darunter befindet sich eine Tachometer zur
Darstellung der Motorgeschwindigkeit. Ganz unten kann die Mindestspannung des
Motors eingestellt werden. Wird diese unterschritten wird der Undervoltage
Callback ausgelöst. Zusätzlich kann auch noch der Motorstrom entsprechend des
angeschlossenen Motors eingestellt werden.

Ganz unten können Basic, Stealth, Coolstep, Spreadcycle und andere Einstellungen
gesetzt werden. Der letzte Tab zeigt den aktuellen Status des Treibers an.

|test_pi_ref|


Error LED
---------

Die rote Error-LED hat vier unterschiedliche Zustände:

* Aus: Es liegt kein Fehler vor.
* 250ms Intervall-Blinken: Übertemperaturwarnung.
* 1s Intervall-Blinken: Eingangsspannung zu gering.
* Durchgängig rot: Motor deaktiviert auf Grund von Kurzschluss mit Ground in Phase A oder B oder auf Grund von zu hoher temperatur.


Wenn ein Überttemperatur- oder Kurzschluss-Event eintritt hört
der Motor auf zu laufen und der treiber wird deaktiviert.
Um den Treiber wieder zu starten muss dieser explizit mit
der Enable-Funktion wieder aktiviert werden.


Modi und deren Eigenschaften
-----------------------------

Basic Configuration (Grundeinstellungen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Für die meisten Anwendungen können alle anderen Einstellungen beibehalten werden.
Nur diese Einstellungen müssen meist angepasst werden:

* **Standstill Current**: Mit diesem Wert kann der Phasenstrom im Stillstand 
  reduziert werden. Dies ist zum Beispiel sinnvoll um das Aufheizen des Motors 
  zu verringern. Wenn der Motor steht wird dieser mit dem eingestellte 
  Phasenstrom betrieben bis die eingestellte Power Down Time um ist. Danach 
  wird der Phasenstrom schrittweise bis zum Standstill Current reduziert. Die 
  dafür benötigte Zeit wird mittels Power Down Time eingestellt. Die Einheit ist
  mA und der eingestellte Phasenstrom ist das Maximum für diesen Wert.

* **Motor Run Current**: Dieser Wert setzt den Phasenstrom, wenn der Motor sich dreht.
  Ein Wert von mindestens der Hälfte des maximalen Phasenstrom sollte für gute 
  Ergebnisse im Mikroschrittbetrieb gesetzt werden. Die Einheit ist mA und der maximal 
  zulässige Wert ist der maximale Phasenstrom. Der eingegebene Wert wird von der API intern
  in einen Faktor im Bereich von 1/32 ... 32/32 umgerechnet, mit dem der Phasenstrom 
  begrenzt wird. Der maximale Phasenstrom sollte im laufenden Betrieb nicht geändert werden. 
  Für eine Änderung im laufenden Betrieb ist dieser Wert da.

* **Standstill Delay Time**: Steuert die Zeit für das Verringern des Motorstroms bis zum 
  Standstill Current. Eine hohe Standstill Delay Time führt zu einem ruhigen und 
  ruckelfreien Übergang. Der Wertebereich ist 0 bis 307ms.

* **Power Down Time**: Setzt die Wartezeit nach dem Stehenbleiben. Der Wertebereich ist 0 bis 5222ms.

* **Stealth Threshold**: Setzt den oberen Grenzwert für den Stealth Modus in Schritte/s.
  Der Wertebereich ist 0-65536 Schritte/s. Wenn die Geschwindigkeit des Motors über diesen Wert liegt wird
  der Stealth Modus abgeschaltet. Ansonsten angeschaltet. Im Stealth Modus nimmt das Drehmoment mit 
  steigender Geschwindigkeit ab.

* **Coolstep Threshold**: Setzt den unteren Grenzwert für den Coolstep Modus Schritte/s. Der Wertebereich
  ist 0-65536 Schritte/s. Der Coolstep Grenzwert muss über dem Stealth Grenzwert liegen.

* **Classic Threshold**: Sets den unteren Grenzwert für den Classic Modus. Der Wertebereich ist
  0-65536 Schritte/s. Im Classic Modus wird der Schrittmotor geräuschvoll aber das Drehmoment wird 
  maximiert.

* **High Velocity Shopper Mode**: Wenn der High Velocity Shopper Mode aktiviert wird, optimiert der 
  Schrittmotortreiber die Ansteuerung des Motors für hohe Geschwindigkeiten.


Stealth Mode
^^^^^^^^^^^^

Im Stealth Modus bewegt sich der Schrittmotor sehr leise mit wenig Vibration. Dieser Modus ist
gut einsetzbar für niedrige und mittlere Geschwindigkeiten.

Coolstep Mode
^^^^^^^^^^^^^

Im Coolstep Modus wird der Schrittmotor mit Energie-Optimierungen betrieben.
Für Anwendungen mit sich ändernden Lasten wird der Strom des Motors automatisch verringert,
wenn niedrige Lasten bewegt werden. Dadurch wird weniger Wärme erzeugt und weniger Kühlung
ist notwendig.

Classic Mode
^^^^^^^^^^^^

Im Classic Modus sind Stealth und Coolstep Modus deaktiviert. Der Schrittmotor wird ganz klassisch 
angesteuert, bietet aber ein maximales Drehmoment.

Spreadcycle
^^^^^^^^^^^

Spreadcycle kann zusammen mit dem Coolstep Modus verwendet werden. Es handelt sich dabei um eine
andere Art der Stromregelung die eine schnellere Reaktionszeit auf sich ändernde Motorlasten und
Geschwindigkeiten besitzt.

Stallguard
^^^^^^^^^^
Mittels Stallguard können Motorlast und ein Abwürgen des Motors erkannt werden.
Im Coolstep Modus wird diese Messung intern genutzt um den Motorstrom an die Motorlast
anzupassen.

Hilfe! Ich verstehe die Hälfte der Wörter nicht
-----------------------------------------------

Der verwendete TMC2130 ist ein sehr mächtiger Motortreiber. Leider besitzt dieser 
daher auch viele Modi, Features und Einstellungsmöglichkeiten. In den meisten 
Anwendungen sollte es ausreichen nur die Grundeinstellungen (Basic Configuration,
erster Tab im Brick Viewer) anzupassen. 

Wenn alle Eigenschaften des Treibers im Detail verstanden werden sollen empfehlen 
wir einen Blick in das
`TMC2130 Datenblatt <https://github.com/Tinkerforge/silent-stepper-brick/raw/master/datasheets/TMC2130_datasheet.pdf>`__.

Um unsere API besser mit den Registern des TMC2130 vergleichen zu können haben wir folgende Tabelle erstellt:

.. |nbsp| unicode:: 0xA0
   :trim:

============================== ==================================== ============================= =================================================
Function                       Parameter                            Register Name @Address[bits]  Note
============================== ==================================== ============================= =================================================
SetBasicConfiguration          Standstill Current                   ihold @0x10[4..0]             Wert wird umgewandelt in 0-31
|nbsp|                         Motor Run Current                    irun @0x10[12..8]             Wert wird umgewandelt in 0-31
|nbsp|                         Standstill Delay Time                iholddelay @0x10[19..16]      Wert wird umgewandelt in 2^18 Takte
|nbsp|                         Power Down Time                      tpowerdown @0x11              Wert wird umgewandelt in 2^18 Takte
|nbsp|                         Stealth Threshold                    tpwmthrs @0x13                Wert wird umgewandelt in Zeit zwischen zwei Takte
|nbsp|                         Coolstep Threshold                   tcoolthrs @0x14               Wert wird umgewandelt in Zeit zwischen zwei Takte
|nbsp|                         Classic Threshold                    thigh @0x15                   Wert wird umgewandelt in Zeit zwischen zwei Takte
|nbsp|                         High Velocity Chopper Mode           vhighchm @0x6C[19]            |nbsp|
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
SetSpreadcycleConfiguration    Slow Decay Duration                  toff @0x6C[3..0]              |nbsp|
|nbsp|                         Enable Random Slow Decay             rndtf @0x6C[13]               |nbsp|
|nbsp|                         Fast Decay Duration                  fd3/hstrt @0x6C[11/6..4]      wird genutzt wenn chm=1, sonst ignoriert
|nbsp|                         Hysteresis Start Value               hstrt @0x6C[6..4]             wird genutzt wenn chm=0, sonst ignoriert
|nbsp|                         Hysteresis End Value                 hend @0x6C[10..7]             wird genutzt wenn chm=0, sonst ignoriert
|nbsp|                         Sinewave Offset                      hend @0x6C[10..7]             wird genutzt wenn chm=1, sonst ignoriert
|nbsp|                         Chopper Mode                         chm @0x6C[14]                 |nbsp|
|nbsp|                         Comperator Blank Time                tbl @0x6C[16..15]             |nbsp|
|nbsp|                         Fast Decay Without Comperator        disfdcc @0x6C[12]             |nbsp|
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
SetStealthConfiguration        Enable Stealth                       en_pwm_mode @0x00[2]          |nbsp|
|nbsp|                         Amplitude                            pwm_ampl @0x70[7..0]          |nbsp|
|nbsp|                         Gradient                             pwm_grad @0x70[15..8]         |nbsp|
|nbsp|                         Enable Autoscale                     pwm_autoscale @0x70[18]       |nbsp|
|nbsp|                         Force Symmetric                      pwm_symmetric @0x70[19]       |nbsp|
|nbsp|                         Freewheel Mode                       freewheel @0x70[21..20]       |nbsp|
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
SetCoolstepConfiguration       Minimum Stallguard Value             semin @0x6D[3..0]             |nbsp|
|nbsp|                         Maximum Stallguard Value             semax @0x6D[11..8]            |nbsp|
|nbsp|                         Current Up Step Width                seup @0x6D[7..4]              |nbsp|
|nbsp|                         Current Down Step Width              sedn @0x6D[14..13]            |nbsp|
|nbsp|                         Minimum Current                      seimin @0x6D[15]              |nbsp|
|nbsp|                         Stallguard Threshold Value           sgt @0x6D[22..16]             |nbsp|
|nbsp|                         Stallguard Mode                      sfilt 0x6D@[24]               |nbsp|
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -------------------------------------------------
SetMiscConfiguration           Disable Short To Ground Protection   diss2g @0x6C[30]              |nbsp|
|nbsp|                         Synchronize Phase Frequency          sync @0x6C[23..20]            |nbsp|
============================== ==================================== ============================= =================================================



.. _silent_stepper_v2_bricklet_case:

Gehäuse
-------

TBD

..
	Ein `laser-geschnittenes Gehäuse für das Silent Stepper Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-silent-stepper-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_silent_stepper_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Silent Stepper Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_silent_stepper_v2_case_1000.jpg

	.. include:: Silent_Stepper_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/silent_stepper_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Silent Stepper Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/silent_stepper_v2_exploded.png

	|bricklet_case_hint|


.. _silent_stepper_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Silent_Stepper_V2_hlpi.table
