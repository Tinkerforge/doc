
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
  * Demoapplikation für Android, Windows Phone und iPhone* sind verfügbar.

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

Es gibt zwei Gruppen von Anwendungen dieses Kits: Steuern und auslesen.
Für Steuerungsanwendungen wird ein :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` mitgeliefert. Dieses besteht aus vier
schaltbaren Solid-State-Relais. Für Ausleseanwendungen wird ein
:ref:`Analog In Bricklet <analog_in_bricklet>`, welches Spannungen
von 0V-45V messen kann.

Beispielanwendungen sind:

* Rauchmelderalarm zum PC weiterleiten.
* Steckdosen über den PC fernsteuern.
* Garagentore über ein Smartphone/Tablet (Android, Windows Phone und iPhone) öffnen und schließen.
* Türklingel zum PC weiterleiten.

Eine Vielzahl weiterer Anwendungen sind möglich. Alles was über
eine Fernbedienung gesteuert wird oder analoge Werte ausgibt kann
mit diesem Kit kinderleicht gehackt werden. Die dokumentierten
Beispiele sollten ausreichen um auch ohne Vorkentnisse jedes Elektrogerät 
in dieser Kategorie zu hacken.

Many more applications are possible, anything that is controlled by
a remote control or outputs analog voltages is easily hackable by this Kit.
The given examples applications should be enough to give you the power
to hack any electronic appliance in this category.

Die Programmierung kann über alle verfügbaren Bindings (|bindings|) 
stattfinden. Beispielimplementierungen für alle Programmiersprachen 
und Demoanwendungen erleichtern den Einstieg in die Programmierung mit 
Tinkerforge.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Spannungsmessung                  0V - 45V in 1mV-Schritten, 12Bit Auflösung
Max. Schaltstrom                  1,2A pro Relais
Max. Schaltspannung               30V pro Relais
================================  ============================================================

Resourcen
---------

* Beispielquelltexte *Rauchmelder* (Download: |smoke_detector_examples_download|)
* Beispielquelltext *Steckdosen fernsteuern* (Download: `C# <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch/csharp>`__)
* Beispielquelltexte *Garagentor fernsteuern* (Download: `Android (Java) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control/android>`__, `Windows Phone (C#) <https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control/windows_phone>`__)
* Beispielquelltext *Benachrichtigung durch die Türklingel* (Download: `Python <https://github.com/Tinkerforge/hardware-hacking/tree/master/doorbell_notifier/python>`__)

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

Wie es funktioniert
-------------------

Es gibt zwei grundlegende Möglichkeiten dieses Kit zu nutzen:

Spannungen bis zu 45V messen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der aktuelle Status von Elektrogeräten wird oft irgendwo in Form
einer analogen Spanung repräsentiert. Wenn diese Spannung unter
45V liegt kann sie mit dem Analog In Bricklet gemessen werden.

Ein gutes Beispiel dafür sind LEDs. Eine LED die den Zustand eines
Systems anzeigt, kann problemlos ausgelesen werden.

Um eine Spannungsquelle zu messen, muss sie an die VIN und GND
Eingänge des Analog In Bricklets angeschlossen werden.

.. warning:: Nicht mit 3.3V oder 5V verbinden! Dies sind Ausgänge.

Falls keine sinnvollen Messungen im Brick Viewer auftauchen muss
wahrscheinlich die Spannung umgepolt werden (VIN und GND tauschen).

.. image:: /Images/Kits/hardware_hacking_analog_in_diode_350.jpg
   :scale: 100 %
   :alt: Beispielschaltbild: Analog In Bricklet misst LED status.
   :align: center
   :target: ../../_images/Kits/hardware_hacking_analog_in_diode.jpg


Spannungen bis zu 30V schalten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Industrial Quad Relay Bricklet you can switch (short circuit) signals. 
Many devices have switches or push buttons that can be hacked by 
the Bricklet. Remote controls are good examples for it.

.. image:: /Images/Kits/hardware_hacking_industrial_quad_switch_350.jpg
   :scale: 100 %
   :alt: Example schematic: Industrial Quad Relay Bricklet bypassing switch
   :align: center
   :target: ../../_images/Kits/hardware_hacking_industrial_quad_switch.jpg


Beispiele
---------

There are many low voltage appliances that can be hacked. Here are some examples:

.. _starter_kit_hardware_hacking_smoke_detector:

Rauchmelder auslesen
^^^^^^^^^^^^^^^^^^^^

Wireless interconnectable smoke detectors allow to read out the alarm signal of
a whole smoke detector network at a single point. We are going to hack such a
smoke detector and utilized this feature to trigger actions if smoke is
detected. For example, notify someone with an email or a text message about the
alarm.

.. image:: /Images/Kits/hardware_hacking_smoke_detector_finished_350.jpg
   :scale: 100 %
   :alt: Smoke Detector with connected Analog In Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_smoke_detector_finished_1200.jpg

For this project we use the wireless smoke detector set `ELRO FA20RF/2
<http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
and connect an :ref:`Analog In Bricklet <analog_in_bricklet>` to one of its
LEDs that light up during an alarm.

The full hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_smoke_detector_hardware_setup>`.

Example implementations with step-by-step instructions are available for:

|smoke_detector_examples|.

.. include:: SmokeDetector.toctree

.. toctree::
   :hidden:

   SmokeDetector_HardwareSetup


.. _starter_kit_hardware_hacking_remote_switch:

Steckdose fernsteuern
^^^^^^^^^^^^^^^^^^^^^

Simple remote switches can be used as a first step towards home automation.
We are going to hack the remote control of such a switch and connect it to a PC
to create software controlled remote switches.

.. image:: /Images/Kits/hardware_hacking_remote_finished_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_finished_1200.jpg

For this project we use the remote switch set `ELRO AB440WD/2
<http://www.elro.eu/en/products/cat/home-automation/home-control/outdoor1/2-outdoor-switches-with-remote-control>`__
and connect an :ref:`Industrial Quad Relay Bricklet
<industrial_quad_relay_bricklet>` to the buttons of the `ELRO AB440RA
<http://www.elro.eu/en/products/cat/home-automation/home-control1/transmitters1/remote-control1>`__
remote control. There are a vast number of control remote switches available. 
Most of the commercially available remote controls use the HX2262 IC
with the same hardware design, so this guide can be used for most 
remote switches.

The full hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_remote_switch_hardware_setup>`.

An example implementation is available
in :ref:`C# <starter_kit_hardware_hacking_remote_switch_csharp>`.

.. toctree::
   :hidden:

   RemoteSwitch_HardwareSetup
   RemoteSwitch_CSharp


.. _starter_kit_hardware_hacking_garage_control:

Garagentor fernsteuern
^^^^^^^^^^^^^^^^^^^^^^

Garage door openers are quite useful. Typically they come with a remote control
and we are going to hack one. After the hack your smart phone can control the garage
door and you don't need to carry around the original remote control
anymore. This project is based on this
`project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garage Door Opener with Android Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg

A small hardware description can be found 
:ref:`here <starter_kit_hardware_hacking_garage_control_hardware_setup>`.

Example apps for :ref:`Android (Java)
<starter_kit_hardware_hacking_garage_control_android>`
and :ref:`Windows Phone (C#)
<starter_kit_hardware_hacking_garage_control_windows_phone>` are available.
The Android app is an improved version of this `project
<http://www.tinkerunity.org/wiki/index.php/EN/Projects/Android_Garagedoor_Control>`__
in the wiki.

A Demo app for iPhone is comming soon.

.. toctree::
   :hidden:

   GarageControl_HardwareSetup
   GarageControl_Android
   GarageControl_WindowsPhone


Benachrichtigung durch die Türklingel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this project the Analog In Bricklet is connected
to a 12V Doorbell. The python script prints "Ring Ring Ring!" if someone 
actuates the doorbell. You can extend this project such that it will 
send an SMS or let your phone ring if someone is at your door. Be creative! 

.. image:: /Images/Kits/hardware_hacking_doorbell_350.jpg
   :scale: 100 %
   :alt: Doorbell notifier
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell.jpg

Description of the hardware setup and more pictures can be found
:ref:`here <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.

An example application is available
in :ref:`Python <starter_kit_hardware_hacking_doorbell_notifier_python>`.

.. toctree::
   :hidden:

   DoorbellNotifier_HardwareSetup
   DoorbellNotifier_Python
