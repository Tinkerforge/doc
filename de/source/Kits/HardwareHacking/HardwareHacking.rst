
:DISABLED_shoplink: ../../../shop/kits/starter-kit-hardware-hacking.html

.. include:: HardwareHacking.substitutions

.. _starter_kit_hardware_hacking:

Starterkit: Hardware Hacking
============================

.. raw:: html

	{% tfgallery %}

	Kits/hardware_hacking_kit_tilted_[?|?].jpg                          Hardware Hacking: Gelötetes Kit mit Steckdosen
	Kits/hardware_hacking_remote_finished_[100|800].jpg                 Hardware Hacking: Kit mit Funksteckdosenfernbedienung
	Kits/hardware_hacking_smoke_detector_finished_[100|800].jpg         Hardware Hacking: Kit mit Rauchmelder
	Kits/hardware_hacking_garage_remote_finished_[100|800].jpg          Hardware Hacking: Kit Garagentorfernbedienung
	Kits/hardware_hacking_smoke_detector_and_remote_new_[100|800].jpg   Hardware Hacking: Kit mit Funksteckdosenfernbedienung und Rauchmelder
	Kits/hardware_hacking_content_[100|800].jpg                         Hardware Hacking: Inhalte
	Kits/hardware_hacking_remote_soldered_closeup_remote_[100|800].jpg  Hardware Hacking: Gehackte Fernbedienung
	Kits/hardware_hacking_remote_soldered_closeup_iqr_top_[?|?].jpg     Hardware Hacking: Quad Relay Verdrahtung

	{% tfgalleryend %}

.. note::

 Das Starterkit: Hardware Hacking wird aktuell nicht mehr verkauft, da einfache
 Funksteckdosen nicht mehr verfügbar sind.

Features
--------

* Kleinstspannungs-Elektrogeräte hacken und über

  * PC, Smartphone/Tablet oder über das Internet (Internet der Dinge) steuern.
  * Demo-Apps für Android, Windows Phone und iOS sind verfügbar.

* Direkt mit dem Hacken beginnen: Zwei Funksteckdosen im Kit enthalten

* Massenmarkt-Geräte auslesen und steuern,

  * z.B. Rauchmelder, Funkfernbedienungen, Garagentore und Türklingel.

* Interaktion über USB, WLAN und Ethernet möglich.


Beschreibung
------------

Das *Starterkit: Hardware Hacking* ermöglicht es Kleinstspannungs-Elektrogeräte 
zu hacken und so mit Tinkerforge Modulen zu verbinden. Jeder
(Embedded-)PC und jedes Smartphone/Tablet kann genutzt werden um mit den
gehackten Geräten zu interagieren. Interaktion ist über USB sowie über
WLAN mit Hilfe der :ref:`WIFI Extension <wifi_extension>` möglich. Auch
eine Ethernet Schnittstelle kann mit der
:ref:`Ethernet Extension <ethernet_extension>` hinzugefügt werden.

Zwei Funksteckdosen sind in diesem Kit enthalten, so dass direkt mit dem Hacken
begonnen werden kann. Eine :ref:`Schritt-für-Schritt Anleitung
<starter_kit_hardware_hacking_remote_switch_hardware_setup>` erklärt wie diese
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
* Steckdosen über den PC uns über Smartphone/Tablet fernsteuern (Android, 
  Windows Phone und iOS).
* Garagentore über ein Smartphone/Tablet (Android, Windows Phone und iOS)
  öffnen und schließen.
* Türklingel zum PC weiterleiten.

Eine Vielzahl weiterer Anwendungen sind möglich. Alles was über
eine Fernbedienung gesteuert wird oder digitale Signale ausgibt kann
mit diesem Kit kinderleicht gehackt werden. Die dokumentierten
Beispiele sollten ausreichen um auch ohne Vorkenntnisse jedes Elektrogerät
in dieser Kategorie zu hacken.

Die Programmierung kann über alle verfügbaren Bindings (|bindings|) 
stattfinden. Beispielimplementierungen für viele Programmiersprachen
und Demo-Anwendungen erleichtern den Einstieg in die Programmierung mit
Tinkerforge.

Ein How-To-Video das zeigt wie man eine Funkfernbedienung hackt sowie
Anwendungen des Kits gibt es auf Youtube:

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/hHnhflS3260" frameborder="0" allowfullscreen></iframe>

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


Ressourcen
----------

* Beispielquelltexte für :ref:`Funksteckdosen fernsteuern <starter_kit_hardware_hacking_remote_switch>` (Download: |remote_switch_examples_download|)
* Beispielquelltext für :ref:`Funksteckdosen mit GUI fernsteuern <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `C# <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch_gui/csharp>`__)
* Beispielquelltexte für :ref:`Funksteckdosen mit Smartphone fernsteuern <starter_kit_hardware_hacking_remote_switch>` (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/power_outlet_control_smart_phone/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/power_outlet_control_smart_phone/windows_phone>`__, `iOS (ObjC) <https://github.com/Tinkerforge/hardware-hacking/tree/master/power_outlet_control_smart_phone/ios>`__)
* Beispielquelltexte für :ref:`Rauchmelder auslesen <starter_kit_hardware_hacking_smoke_detector>` (Download: |smoke_detector_examples_download|)
* Beispielquelltexte für :ref:`Garagentor mit Smartphone fernsteuern <starter_kit_hardware_hacking_garage_control>` (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/windows_phone>`__, `iOS (ObjC) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/ios>`__)
* Beispielquelltext für :ref:`Benachrichtigung durch Türklingel <starter_kit_hardware_hacking_doorbell_notifier>` (Download: `Python <https://github.com/Tinkerforge/hardware-hacking/tree/master/doorbell_notifier/python>`__)
* Demo-Anwendung für :ref:`Funksteckdosen mit GUI fernsteuern <starter_kit_hardware_hacking_remote_switch_gui_csharp>` (Download: `Windows (.NET), Linux (Mono), macOS (Mono) <https://github.com/Tinkerforge/hardware-hacking/raw/master/remote_switch_gui/csharp/RemoteSwitchGUI.exe>`__)
* Demo-Apps für :ref:`Funksteckdosen mit Smartphone fernsteuern <starter_kit_hardware_hacking_remote_switch>` (Download: `Android <https://play.google.com/store/apps/details?id=com.tinkerforge.poweroutletcontrol>`__, `Windows Phone <https://www.windowsphone.com/s?appid=52e1f6a9-707c-4961-9e68-5736e6d29b73>`__, `iOS <https://itunes.apple.com/de/app/power-outlet-control/id739029826?mt=8>`__)
* Demo-Apps für :ref:`Garagentor mit Smartphone fernsteuern <starter_kit_hardware_hacking_garage_control>` (Download: `Android <https://play.google.com/store/apps/details?id=com.tinkerforge.garagecontrol>`__, `Windows Phone <https://www.windowsphone.com/s?appid=4c9a8f61-d9ed-4fd2-b4e6-a332b617c596>`__, `iOS <https://itunes.apple.com/de/app/garage-control/id739047995?&mt=8>`__)


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
Schließe beide Bricklets an den Master Brick an und verbinde es per USB mit
dem PC. Anschließend kann über den Brick Viewer bestimmt werden, ob alle 
Firmwares aktuell sind. Falls nicht, so sollten diese aktualisiert werden
(:ref:`Bricks aktualisieren <brickv_flash_brick_firmware>`,
:ref:`Bricklets aktualisieren <brickv_flash_bricklet_plugin>`):

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
und Spannungen schalten. Eine detaillierte Erklärung der Grundlagen befindet
sich im :ref:`Hardware Hacking für Anfänger
<starter_kit_hardware_hacking_for_beginners>` Tutorial.

.. warning:: Die genannten Spannungsobergrenzen sind einzuhalten!
   Geräte die über eine potentiell gefährlich hohe Spannung
   versorgt werden (z.B. Netzspannung) dürfen nicht gehackt werden!

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
um ausreichende Pegel für die High/Low Detektion zu erhalten.

.. image:: /Images/Kits/hardware_hacking_idi4_resistor_diode.jpg
   :scale: 100 %
   :alt: Beispielschaltung: Industrial Digital In 4 Bricklet misst LED Zustand
   :align: center


Spannungen bis zu 30V schalten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mit dem :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
können Signal geschaltet (kurz geschlossen)
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
Gerät zu verbinden muss zuvor folgendes erledigt werden:

* Finde Löt-Pads die benutzt werden können um eine Spannung zu messen oder zu schalten.
* Löte Drähte an diese Pads.

Im :ref:`Hardware Hacking für Anfänger
<starter_kit_hardware_hacking_for_beginners>` Tutorial werden diese Schritte
genauer erläutert.

.. toctree::
   :hidden:

   Details <ForBeginners>


Beispiele
---------

Es gibt viele Geräte die gehackt werden können. Hier sind ein paar Beispiele:


.. _starter_kit_hardware_hacking_remote_switch:

Funksteckdosen fernsteuern
^^^^^^^^^^^^^^^^^^^^^^^^^^

In diesem Kit sind zwei Funksteckdosen enthalten die als erster Schritt in die
Hausautomatisierung genutzt werden können. Wir werden die Fernbedienung dieser
Funksteckdosen hacken, so dass wir die Steckdosen über den PC schalten können.

.. image:: /Images/Kits/hardware_hacking_remote_finished_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_1200.jpg

Dazu schließen wir ein :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` an die Taster der Fernbedienung an.
Es gibt eine große Anzahl an Funksteckdosen und Fernbedienungen auf dem Markt.
Die meisten kommerziell erhältlichen Fernbedienungen nutzen einen HX2262 IC
mit einem Hardwaredesign welches identisch zu der hier verwendeten ELRO 
Fernbedienung ist.
So kann diese Beschreibung auch für die meisten anderen Funksteckdosen-
Fernbedienungen genutzt werden.

Die vollständige Beschreibung des Hardware-Aufbaus ist
:ref:`hier <starter_kit_hardware_hacking_remote_switch_hardware_setup>`
zu finden.

.. toctree::
   :hidden:

   Hardware-Aufbau <RemoteSwitch_HardwareSetup>

Beispiel Apps für :ref:`Android (Java)
<starter_kit_hardware_hacking_power_outlet_control_android>`,
:ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_power_outlet_control_windows_phone>` und
:ref:`iOS (ObjC)
<starter_kit_hardware_hacking_power_outlet_control_ios>`
sind verfügbar.

.. toctree::
   :hidden:

   Mit Android <PowerOutletControl_Android>
   Mit Windows Phone <PowerOutletControl_WindowsPhone>
   Mit iOS <PowerOutletControl_iOS>

Eine Beispielimplementierung mit GUI (kompatibel mit Windows (.NET),
Linux (Mono) und macOS (Mono)) ist verfügbar in :ref:`C#
<starter_kit_hardware_hacking_remote_switch_gui_csharp>`.

.. toctree::
   :hidden:

   Mit C# und GUI <RemoteSwitchGUI_CSharp>

Minimalistische Beispiele sind verfügbar in:

|remote_switch_examples|

.. include:: RemoteSwitch.toctree


.. _starter_kit_hardware_hacking_smoke_detector:

Rauchmelder auslesen
^^^^^^^^^^^^^^^^^^^^

Über drahtlose Rauchmelder ist es möglich den Alarm eines ganzen 
Rauchmelder-Netzwerks an einem Punkt auszulesen. Wir werden uns dies zu nutze 
machen und eigene Aktionen ausführen wenn Rauch erkannt wird. Hierzu hacken
wir einen drahtlosen Rauchmelder. Als Beispiel könnten wir im Alarmfall eine 
E-Mail oder Textnachricht verschicken.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

Für dieses Projekt nutzen wir ein drahtlose Rauchmelderset
und schließen ein :ref:`Industrial Digital In 4 Bricklet
<industrial_digital_in_4_bricklet>` an eine der LEDs an, die im Alarmfall aufleuchtet.

Eine ausführliche Beschreibung des Hardware-Aufbaus ist
:ref:`hier <starter_kit_hardware_hacking_smoke_detector_hardware_setup>` zu
finden.

.. toctree::
   :hidden:

   Hardware-Aufbau <SmokeDetector_HardwareSetup>

Beispielimplementierungen mit Schritt-für-Schritt Anleitungen sind verfügbar für:

|smoke_detector_examples|

.. include:: SmokeDetector.toctree


.. _starter_kit_hardware_hacking_garage_control:

Garagentor mit Smartphone fernsteuern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Garagentoröffner besitzen typischerweise eine Fernbedienung. Eine solche 
Fernbedienung wollen wir in diesem Beispiel hacken. Anschließend werden
wir das Garagentor über eine kleine App mit dem Smartphone steuern können,
so dass die Fernbedienung nicht mehr mitgenommen werden muss.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg

Eine kurze Beschreibung des Hardware-Aufbaus kann
:ref:`hier <starter_kit_hardware_hacking_garage_control_hardware_setup>`
gefunden werden.

.. toctree::
   :hidden:

   Hardware-Aufbau <GarageControl_HardwareSetup>

Beispiel Apps für :ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`,
:ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` und
:ref:`iOS (ObjC) <starter_kit_hardware_hacking_garage_control_ios>`
sind verfügbar.

.. toctree::
   :hidden:

   Mit Android <GarageControl_Android>
   Mit Windows Phone <GarageControl_WindowsPhone>
   Mit iOS <GarageControl_iOS>


.. _starter_kit_hardware_hacking_doorbell_notifier:

Benachrichtigung durch die Türklingel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In diesem Projekt verbinden wir das Industrial Digital In 4 Bricklet mit einer
typischen, 12V betriebenen, Türklingel. Sobald jemand klingelt, wird unser
Python Skript "Ring Ring Ring!" ausgeben. Dieses Projekt kann natürlich
erweitert werden, so dass eine SMS versendet wird oder dein Telefon klingelt 
wenn jemand an der Tür ist. Sei kreativ!

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Türklingel Benachrichtigung mit Industrial Digital In 4
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Eine Beschreibung des Hardware-Aufbaus und mehr Fotos gibt es
:ref:`hier <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.

.. toctree::
   :hidden:

   Hardware-Aufbau <DoorbellNotifier_HardwareSetup>

Die Beispielanwendung in Python gibt es
:ref:`hier <starter_kit_hardware_hacking_doorbell_notifier_python>`.

.. toctree::
   :hidden:

   Mit Python <DoorbellNotifier_Python>
