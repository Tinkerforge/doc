
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Hardware-Aufbau: Garagentor

.. _starter_kit_hardware_hacking_garage_control_hardware_setup:

Hardware-Aufbau: Garagentor
===========================

Die Hardware von Garagentoröffnern kann wirklich komplex sein. Neben dem
Funktransmitter gibt es zum Beispiel komplexe Elektronik für die 
Verschlüsselung so dass wir diese nicht näher betrachten wollen. Dies müssen
wir aber auch nicht, da wir nur die Aktionen auslösen wollen die normalerweise
vom Taster der Fernbedienung ausgelöst werden.

Anstatt den Taster selber auszulösen werden wir diesen überbrücken
wie zuvor schon :ref:`hier <starter_kit_hardware_hacking_for_beginners_quad_relay>` 
beschrieben.

Gehäuse öffnen
--------------

Im ersten Schritt öffnen wir dazu das Gehäuse der Fernbedienung
mit einem Schraubendreher.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_350.jpg
   :scale: 100 %
   :alt: Fernbedienung mit entfertem Gehäuse
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_1200.jpg

Nachdem das Gehäuse entfernt ist können wir einen genaueren Blick auf die
fünf Taster werfen. Wir sind nur an dem linken Taster interessiert, da dieser,
bei diesem Modell, das Garagentor öffnet bzw. schließt.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup.jpg
   :scale: 100 %
   :alt: Nahaufname: Fernbedienung Taster
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup.jpg

Drähte anlöten
--------------

Wenn wir diesen Taster näher betrachten stellen wir fest, dass nur zwei der
vier Pads mit Leiterbahnen verbunden sind. Wir haben also die Stellen 
identifiziert an denen wir unsere Drähte anlöten müssen.

.. image:: /Images/Kits/hardware_hacking_garage_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Fernbedienung mit angelöteten Drähten
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_soldered_1200.jpg

Die Enden der Drähte verbinden wir mit einem Relais des Quad Relay Bricklets
auf dem 8 Pol Stecker. Anschließend können wir unser Werk mit der Brick Viewer
Software Testen. Dazu öffnen wir das Industrial Quad Relay Bricklet Tab
und schalten das Relais. Die Fernbedienung sollte sich darüber steuern lassen.

Nach diesem Test können wir das Gehäuse der Fernbedienung schließen und
sind mit unserer Arbeit fertig.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_350.jpg
   :scale: 100 %
   :alt: Garagentorfernbedienung mit angeschlossenem Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_1200.jpg


