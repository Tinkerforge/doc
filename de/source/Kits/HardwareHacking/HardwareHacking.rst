
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / Starterkit: Hardware Hacking
:shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starterkit: Hardware Hacking
============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/hardware_hacking_remote_finished_350.jpg",
	               "Kits/hardware_hacking_remote_finished_800.jpg",
	               "Hardware Hacking: Kit mit Funksteckdosenfernbedienung")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_smoke_detector_finished_100.jpg",
	             "Kits/hardware_hacking_smoke_detector_finished_800.jpg",
	             "Hardware Hacking: Kit mit Rauchmelder")
	}}
	{{
	    tfdocimg("Kits/hardware_hacking_garage_remote_finished_100.jpg",
	             "Kits/hardware_hacking_garage_remote_finished_800.jpg",
	             "Hardware Hacking: Kit Garagentorfernbedienung")
	}}
	{{ tfdocend() }}


Features
--------

* Elektrogeräte mit geringer Spannung hacken 

  * PC, Smartphone/Tablet oder über das Internet (Internet der Dinge).
  * Demo-Apps für Android, Windows Phone und iPhone* sind verfügbar.

* Direkt mit dem Hacken beginnen: Zwei Funksteckdosen im Kit enthalten

* Massenmarkt-Geräte auslesen und steuern,

  * z.B. Rauchmelder, Funkfernbedienungen, Garagentore und Türklingel.

* Interaktion über USB, WLAN und Ethernet möglich.




\*: Demo für iPhone folgt bald.

Beschreibung
------------

Das *Starterkit: Hardware Hacking* ermöglicht es Elektrogeräte mit niedriger
Spannung zu hacken und so mit Tinkerforge Modulen zu verbinden. Jeder
(Embedded-)PC und jedes Smartphone/Tablet kann genutzt werden um mit den
gehackten Geräten zu interagieren. Interaktion ist über USB sowie über
WLAN mit Hilfe der :ref:`WIFI Extension <wifi_extension>` möglich. Auch
eine Ethernetschnittstelle kann mit der 
:ref:`Ethernet Extension <ethernet_extension>` hinzugefügt werden.

Zwei Funksteckdosen sind in diesem Kit enthalten, so dass direkt mit dem Hacken
begonnen werden kann. Eine :ref:`Schritt-für-Schritt Anleitung
<starter_kit_hardware_hacking_remote_switch>` erklärt wie diese
gehackt werden können (Lötkolben, Lötzinn und Schraubendreher benötigt).

Es gibt zwei Gruppen von Anwendungen für dieses Kit: Steuern und Auslesen.
Für Steuerungsanwendungen wird ein :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` mitgeliefert. Dieses besteht aus vier
schaltbaren Solid-State-Relais. Für Ausleseanwendungen wird ein
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`
mitgeliefert. Dieses kann vier digitale Signale mit Spannungen bis zu
36V galvanisch getrennt auslesen.

Dokumentierte Beispielanwendungen sind:

* Rauchmelderalarm zum PC weiterleiten.
* Steckdosen über den PC fernsteuern.
* Garagentore über ein Smartphone/Tablet (Android, Windows Phone und iPhone)
  öffnen und schließen.
* Türklingel zum PC weiterleiten.

Eine Vielzahl weiterer Anwendungen sind möglich. Alles was über
eine Fernbedienung gesteuert wird oder digitale Signale ausgibt kann
mit diesem Kit kinderleicht gehackt werden. Die dokumentierten
Beispiele sollten ausreichen um auch ohne Vorkentnisse jedes Elektrogerät 
in dieser Kategorie zu hacken.

Die Programmierung kann über alle verfügbaren Bindings (|bindings|) 
stattfinden. Beispielimplementierungen für alle Programmiersprachen 
und Demo-Anwendungen erleichtern den Einstieg in die Programmierung mit
Tinkerforge.

Technische Spezifikation
------------------------

================================  ======================================
Eigenschaft                       Wert
================================  ======================================
Digitale Eingänge                 4
Spannungsbereich Low Pegel        0-2V
Spannungsbereich High Pegel       3-36V
--------------------------------  --------------------------------------
--------------------------------  --------------------------------------
Digitale Ausgänge                 4
Maximaler Schaltstrom             1,2A pro Relais
Maximale Schaltspannung           30V pro Relais
================================  ======================================

Resourcen
---------

* Beispielquelltexte für :ref:`Funksteckdosen fernsteuern <starter_kit_hardware_hacking_remote_switch>` (Download: |remote_switch_examples_download|)
* Beispielquelltext für :ref:`Funksteckdosen mit GUI fernsteuern <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `C# <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch_gui/csharp>`__)
* Beispielquelltexte für :ref:`Rauchmelder auslesen <starter_kit_hardware_hacking_smoke_detector>` (Download: |smoke_detector_examples_download|)
* Beispielquelltexte für :ref:`Garagentor mit Smartphone fernsteuern <starter_kit_hardware_hacking_garage_control>` (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/windows_phone>`__)
* Beispielquelltext für :ref:`Benachrichtigung durch Türklingel <starter_kit_hardware_hacking_doorbell_notifier>` (Download: `Python <https://github.com/Tinkerforge/hardware-hacking/tree/master/doorbell_notifier/python>`__)
* Demo-Anwendung :ref:`Funksteckdosen mit GUI fernsteuern <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `Windows, Linux, Mac OS X <https://github.com/Tinkerforge/hardware-hacking/raw/master/remote_switch_gui/csharp/RemoteSwitchGUI.exe>`__)
* Demo-Apps :ref:`Garagentor mit Smartphone fernsteuern <starter_kit_hardware_hacking_garage_control>` (Download: Android, Windows Phone, iPhone*) TODO

\*: Demo für iPhone folgt bald.


Benötigte Werkzeuge
-------------------

* Lötkolben
* Lötzinn
* Schraubendreher (um Gehäuse zu öffnen etc.)


Firmware aktualisieren und erste Tests
--------------------------------------

Im ersten Schritt sollten die Bricks und Bricklets ausprobiert
und die Firmwares ggf. aktualisiert werden.

Dazu müssen der :ref:`Brick Daemon <brickd_installation>` und der
:ref:`Brick Viewer <brickv_installation>` installiert werden. 
Schließe biede Bricklets an den Master Brick an und verbinde es per USB mit
dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_plugin>`):

.. image:: /Images/Kits/hardware_hacking_update_350.jpg
   :scale: 100 %
   :alt: Firmware update in Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_update.jpg

Danach sollten mit dem Brick Viewer alle Bricks und Bricklets überprüft 
werden. Dazu klickt man am besten durch die verschiedenen Tabs und 
überprüft, dass der Master Brick und die Bricklets korrekt angezeigt werden.


Funktionsweise
--------------

Es gibt zwei grundlegende Möglichkeiten dieses Kit zu nutzen: Spannungen messen
und Spannungen schalten. Eine detailierte Erklärung der Grundlagen befindet
sich im :ref:`Hardware Hacking für Anfänger
<starter_kit_hardware_hacking_for_beginners>` Tutorial.


Spannungen bis zu 36V messen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der aktuelle Zustand von Elektrogeräten wird oft irgendwo in Form
einer elektrischen Spannung repräsentiert. Wenn es sich um ein digitales Signal
handelt und dessen Spannung unter 36V liegt, dann kann ein :ref:`Industrial
Digital In 4 Bricklet <industrial_digital_in_4_bricklet>` damit verbunden und
der Zustand ausgelesen werden. Ein gutes Beispiel dafür sind LEDs. Eine LED die
den Zustand eines Systems anzeigt, kann problemlos ausgelesen werden.

Hierbei ist es wichtig zu beachten, dass die minimale Spannung, die als High
erkannt wird, bei 3V liegt. Die maximale Spannung die als Low erkannt wird liegt
bei 2V. Zwischen diesen Spannungen ist das Verhalten undefiniert.

Um ein Signal auszulesen muss dieses an einen der Eingänge des Industrial
Digital In 4 angeschlossen werden. Falls keine Reaktion des Eingangs im
Brick Viewer zu erkennen ist, kann es sein das die Belegung gedreht werden muss 
(verpolt). Die Belegung kann per Trial and Error getestet werden. Das
Industrial Digital In 4 ist verpolungsgeschützt.

Die nachfolgende Abbildung zeigt exemplarisch die notwendige Schaltung
zum Auslesen einer LED. Hierbei wurde der Vorwiderstand mit einbezogen
um ausreichende Pegel für die High/Low detektion zu erhalten.

.. image:: /Images/Kits/hardware_hacking_idi4_resistor_diode.jpg
   :scale: 100 %
   :alt: Beispielschaltung: Industrial Digital In 4 Bricklet misst LED state
   :align: center


Spannungen bis zu 30V schalten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mit dem :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
können Signal geschalten (kurz geschlossen)
werden. Viele Geräte verfügen über Taster oder Schalter die mit diesem Bricklet
gehackt werden können. Ein gutes Beispiel hierfür sind Fernbedienungen.

Die nachfolgende Abbildung zeigt exemplarisch einen möglichen Aufbau um einen
Taster/Schalter mit dem Industrial Quad Relay Bricklet zu steuern.

.. image:: /Images/Kits/hardware_hacking_idq_switch.jpg
   :scale: 100 %
   :alt: Beispielschaltung: Industrial Quad Relay Bricklet überbrickt Schalter
   :align: center


Hardware Hacking für Anfänger
-----------------------------

Um ein Industrial Digital In 4 oder Industrial Quad Relay Bricklet mit einem
Gerät zu verbinden müssen zuvor folgendes erledigt werden:

* Finde Löt-Pads die benutzt werden können um eine Spannung zu messen oder zu schalten
* Löte Drähte an diese Pads

In dem :ref:`Hardware Hacking für Anfänger
<starter_kit_hardware_hacking_for_beginners>` Tutorial werden diese Schritte
genauer erläutert.

.. toctree::
   :hidden:

   ForBeginners


Beispiele
---------

Es gibt viele Geräte die gehackt werden können. Hier sind ein paar Beispiele:


.. _starter_kit_hardware_hacking_remote_switch:

Funksteckdosen fernsteuern
^^^^^^^^^^^^^^^^^^^^^^^^^^

In diesem Kit ist das Funksteckdosenset `ELRO AB440WD/2
<http://www.elro.eu/de/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__
enthalten. Diese Funksteckdosen können als ersten Schritt in die 
Hausautomatisation genutzt werden. Wir werden die Fernbedienung dieser 
Funksteckdosen hacken, so dass wir die Steckdosen über den PC schalten können.

.. image:: /Images/Kits/hardware_hacking_remote_finished_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_1200.jpg

Dazu schließen wir ein :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` an die Taster der `ELRO AB440RA
<http://www.elro.eu/de/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
Fernbedienung. Es gibt eine große Anzahl an Funksteckdosen und 
Fernbedienungen auf dem Markt. 
Die meisten kommerziell erhältlichen Fernbedienungen nutzen einen HX2262 IC
mit identischem Hardwaredesign wie das der hier verwendeten ELRO Fernbedienung.
So kann diese Beschreibung auch für die meisten anderen Funksteckdosen-
Fernbedienungen genutzt werden.

Die vollständige Beschreibung des Hardware-Aufbaus ist
:ref:`hier <starter_kit_hardware_hacking_remote_switch_hardware_setup>`
zu finden.

Eine Beispielimplementierung mit GUI (kompatibel mit Windows (.NET),
Linux (Mono) und Mac OS X (Mono)) ist verfügbar in

* :ref:`C# <starter_kit_hardware_hacking_remote_switch_gui_csharp>`.

Minmalistische Beispiele sind verfügbar in

* |remote_switch_examples|.

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   RemoteSwitch_HardwareSetup
   RemoteSwitchGUI_CSharp


.. _starter_kit_hardware_hacking_smoke_detector:

Rauchmelder auslesen
^^^^^^^^^^^^^^^^^^^^

Über drahtlose Rauchmelder ist es möglich den Alarm eines ganzen 
Rauchmelder-Netzwerks an einem Punkt auszulesen. Wir werden uns dies zu nutze 
machen und eigene Aktionen ausführen wenn Rauch erkannt wird. Hierzu hacken
wir einen drahtlosen Rauchmelder. Als Beispiel könnten wir im Alarmfall eine 
Email oder Textnachricht verschicken.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

Für dieses Projekt nutzen wir das drahtlose Rauchmelderset `ELRO FA20RF/2
<http://www.elro.eu/de/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
und schließen ein :ref:`Industrial Digital In 4 Bricklet
<industrial_digital_in_4_bricklet>` an eine der LED die im Alarmfall aufleuchtet.

Eine ausführliche Beschreibung des Hardware-Aufbaus ist
:ref:`hier <starter_kit_hardware_hacking_smoke_detector_hardware_setup>` zu
finden.

Beispiel Implementierungen mit Schritt-für-Schritt Anleitungen sind verfügbar für:

|smoke_detector_examples|.

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   SmokeDetector_HardwareSetup


.. _starter_kit_hardware_hacking_garage_control:

Garagentor mit Smartphone fernsteuern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Garagentoröffner sind wirklich nützlich. Typischerweise besitzen diese eine 
Fernbedienung die wir in diesem Beispiel hacken werden. Anschließend werden
wir das Garagentor über eine kleine App mit dem Smartphone steuern können,
so dass die Fernbedienung nicht mehr mitgenommen werden muss.

Dieses Projekt basiert auf diesem
`Wiki-Projekt <http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg

Eine kurze Beschreibung des Hardware-Aufbaus kann
:ref:`hier <starter_kit_hardware_hacking_garage_control_hardware_setup>`
gefunden werden.

Beispiel Apps für
:ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`
und :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` sind verfügbar.

Eine Beispielanwendung für das iPhone folgt bald.

.. toctree::
   :hidden:

   GarageControl_HardwareSetup
   GarageControl_Android
   GarageControl_WindowsPhone


.. _starter_kit_hardware_hacking_doorbell_notifier:

Benachrichtigung durch die Türklingel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In diesem Projekt verbinden wir das Industrial Digital In 4 Bricklet mit einer
typischen, 12V betriebenen, Türklingel. Sobald jemand klingelt, wird unser
Python-Script "Ring Ring Ring!" ausgeben. Dieses Projekt kann natürlich
erweitert werden, so dass SMS versendet oder dein Telefon klingelt wenn jemand
and der Tür steht. Sei kreativ!

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Türklingel Benachrichtigung mit Industrial Digital In 4
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Eine Beschreibung des Hardwareaufbaus und mehr Fotos gibt es 
:ref:`hier <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.

Die Beispielanwendung in Python gibt es
:ref:`hier <starter_kit_hardware_hacking_doorbell_notifier_python>`.

.. toctree::
   :hidden:

   DoorbellNotifier_HardwareSetup
   DoorbellNotifier_Python
