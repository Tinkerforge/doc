
:breadcrumbs: <a href="index.html">Startseite</a> / <a href="index.html#einstieg">Einstieg</a> / Einführung

.. _primer:

Einführung
==========

Die nachfolgende Beschreibung gibt einen Überblick über die verschiedenen
Produkte und Konzepte des Tinkerforge Baukastensystems. Detaillierte
Beschreibungen über die Funktion und die zur Verfügung stehende API befindet 
sich in der Dokumentation des jeweiligen Produktes.

.. _primer_products:

Produkte
--------

Unsere Produkte gliedern sich in fünf verschiedene Kategorien:

* :ref:`Bricks <primer_bricks>`:
  Stapelbare Module zum Messen und Steuern über USB.
* :ref:`Bricklets <primer_bricklets>`:
  Nicht stapelbare Sensor-/Aktormodule, die die Fähigkeiten von Bricks
  erweitern.
* :ref:`Master Extensions <primer_master_extensions>`:
  Module um Alternativen zur USB Schnittstelle des
  :ref:`Master Bricks <master_brick>` zu bieten (WIFI, Ethernet, RS485).
* :ref:`Stromversorgungen <primer_power_supplies>`:
  Module die einen Stapel von Bricks mit Strom versorgen.
* :ref:`Zubehör <primer_accessories>`

Dieses :ref:`Tutorial <tutorial_first_steps>` erklärt wie alles zusammen
funktioniert.


.. _primer_bricks:

Bricks
^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricks/brick_red_tilted_top_front_100.jpg
       :scale: 100 %
       :alt: RED Brick
       :align: center
       :target: _images/Bricks/brick_red_tilted_top_front_800.jpg

    - .. image:: /Images/Bricks/brick_master21_tilted_front_100.jpg
       :scale: 100 %
       :alt: Master Brick
       :align: center
       :target: _images/Bricks/brick_master21_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_dc_tilted_front_100.jpg
       :scale: 100 %
       :alt: DC Brick
       :align: center
       :target: _images/Bricks/brick_dc_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_stepper_tilted_front_100.jpg
       :scale: 100 %
       :alt: Stepper Brick
       :align: center
       :target: _images/Bricks/brick_stepper_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_servo_tilted_front_100.jpg
       :scale: 100 %
       :alt: Servo Brick
       :align: center
       :target: _images/Bricks/brick_servo_tilted_front_800.jpg

    - .. image:: /Images/Bricks/brick_imu_v2_tilted1_100.jpg
       :scale: 100 %
       :alt: IMU Brick 2.0
       :align: center
       :target: _images/Bricks/brick_imu_v2_tilted1_800.jpg


Bricks sind 4 x 4cm (1,57 x 1,57") große Module, die über einen Mini-USB 
Anschluss verfügen und über diesen von Geräten, wie zum Beispiel einem 
(Embedded-) PC, gesteuert werden können. Jedes Brick besitzt eine Aufgabe: Es 
gibt Bricks für Messaufgaben (z.B. :ref:`IMU Brick 2.0 <imu_v2_brick>`), zur 
Kommunikation (z.B. :ref:`Master Brick <master_brick>`) und um Motoren zu
steuern (z.B. :ref:`DC Brick <dc_brick>`).

Über :ref:`Bricklets <primer_bricklets>` können die Fähigkeiten von
Bricks erweitert werden. Abhängig vom Modell verfügt jeder Brick über zwei oder
vier Anschlüsse für Bricklets.

Bricks können gestapelt werden, siehe die 
:ref:`Beschreibung zum Stapelkonzept <primer_stack>`. Die USB
Schnittstelle eines Master Bricks kann mit 
:ref:`Master Extensions <primer_master_extensions>` durch
WLAN, Ethernet oder RS485 ersetzt werden. Zusammen mit dem Stapelkonzept können 
somit alle Bricks und Bricklets anstatt per USB auch per WLAN oder Ethernet 
gesteuert werden.


.. include:: Primer_bricks.table


.. _primer_bricklets:

Bricklets
^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricklets/bricklet_dual_relay_tilted_100.jpg
       :scale: 100 %
       :alt: Dual Relay Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_dual_relay_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_joystick_tilted_100.jpg
       :scale: 100 %
       :alt: Joystick Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_joystick_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_lcd_20x4_tilted_100.jpg
       :scale: 100 %
       :alt: LCD 20x4 Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_lcd_20x4_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_temperature_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Temperature IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_temperature_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_linear_poti_tilted_100.jpg
       :scale: 100 %
       :alt: Linear Poti Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_linear_poti_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_distance_ir_tilted_100.jpg
       :scale: 100 %
       :alt: Distance IR Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_distance_ir_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_analog_in_v2_tilted1_100.jpg
       :scale: 100 %
       :alt: Analog In Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_analog_in_v2_tilted1_800.jpg

Bricklets erweitern die Fähigkeiten von :ref:`Bricks <primer_bricks>`.
Es gibt Bricklets um physikalische Größen wie Rotation, elektrische Spannung,
elektrischen Strom, Umgebungshelligkeit oder Umgebungstemperatur zu messen.
Es gibt auch Bricklets für Steuerungsaufgaben wie Relais, digitale Ein- und
Ausgänge sowie alphanumerische Ausgaben auf LCDs.

Im Gegensatz zu Bricks haben Bricklets keine feste Größe. Jedes Bricklet hat
die kleinste mögliche Größe. Jeder Brick hat bis zu vier Anschlüsse für
Bricklets. Über seine USB Verbindung können diese gesteuert werden.

Bricklets verfügen über keinen eigenen Prozessor, verfügen aber über eine eigene 
API. Aus Sicht des Programmierers werden sie wie eigenständige Module behandelt. 
Beim Start erkennt ein Brick die angeschlossenen Bricklets. Die Bricklet Plugins 
sind auf einem 
`EEPROM <https://de.wikipedia.org/wiki/Electrically_Erasable_Programmable_Read-Only_Memory>`__
auf dem Bricklet gespeichert und werden zur Ausführung in den Flash des Bricks
geladen. Nach diesem Vorgang verarbeitet das Brick die API Aufrufe seiner 
angeschlossenen Bricklets und steuert die Bricklets.


.. include:: Primer_bricklets.table


.. _primer_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_chibi_tilted_100.jpg
       :scale: 100 %
       :alt: Chibi Extension
       :align: center
       :target: _images/Extensions/extension_chibi_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_ethernet_tilted_100.jpg
       :scale: 100 %
       :alt: Ethernet Extension
       :align: center
       :target: _images/Extensions/extension_ethernet_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_rs485_v11_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_v11_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_wifi2_tilted_100.jpg
       :scale: 100 %
       :alt: WIFI Extension 2.0
       :align: center
       :target: _images/Extensions/extension_wifi2_tilted_800.jpg

Wird ein :ref:`Master Brick <master_brick>` alleine oder im 
:ref:`Stapel <primer_stack>` eingesetzt, läuft die Kommunikation über
seine USB Schnittstelle. Master Extensions erweitern die 
Kommunikationsmöglichkeiten von Master Bricks. Es gibt kabelgebundene 
(:ref:`RS485 <rs485_extension>`,  :ref:`Ethernet <ethernet_extension>`) und 
drahtlose Master Extensions (:ref:`WIFI <wifi_v2_extension>`). Anstatt über USB 
können Bricks und Bricklets somit über WLAN (WIFI) oder Ethernet gesteuert 
werden. Über RS485 ist eine Vernetzung untereinander auch über größere Strecken 
möglich.

Aus Programmierersicht sind die verschiedenen Kommunikationsmöglichkeiten 
transparent. Ein Stapel mit Master Extension verhält sich so als wären alle 
Bricks einzeln per USB am PC angeschlossen.

Dies bedeutet: Programme können mit allen Bricks einzeln per USB am PC
angeschlossen entwickelt werden. Wenn später die Bricks gestapelt und über
eine Master Extension angebunden werden dann funktioniert das zuvor geschrieben
Programm ohne Änderungen weiter.

.. include:: Primer_extensions.table


.. _primer_power_supplies:

Stromversorgungen
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

:ref:`Bricks <primer_bricks>` und :ref:`Bricklets <primer_bricklets>` 
können über die USB Schnittstelle des Bricks mit Strom versorgt werden. 
:ref:`Stapel <primer_stack>` können ebenfalls über die USB Verbindung des 
Masters mit Strom versorgt werden. Diese Möglichkeit ist durch die USB 
Spezifikation auf 500mA beschränkt. Ein großer Stapel kann einen höheren 
Stromverbrauch aufweisen.

Die Stromversorgungsmodule können einen Stapel mit mehr als 500mA versorgen. 
Zusätzlich wird über den Stapel auch die Versorgungsspannung geleitet, so dass
Bricks im Stapel ihre angeschlossenen Motoren darüber direkt versorgen können
(z.B. :ref:`DC Brick <dc_brick>`). Stromversorgungsmodule haben die Größe von 
:ref:`Bricks <primer_bricks>` und werden unter einen Stapel gesteckt.

.. include:: Primer_power_supplies.table


.. _primer_accessories:

Zubehör
^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Accessories/dc_jack_adapter_tilted_100.jpg
       :scale: 100 %
       :alt: DC Jack Adapter
       :align: center
       :target: _images/Accessories/dc_jack_adapter_tilted_800.jpg

.. include:: Primer_accessories.table


Konzepte
--------

.. _primer_stack:

Stapel aus Bricks
^^^^^^^^^^^^^^^^^

.. image:: /Images/Bricks/brick_master_stack_front_big_350.jpg
    :scale: 100 %
    :alt: Bild eines Stacks von Bricks
    :align: center
    :target: _images/Bricks/brick_master_stack_front_big_800.jpg

:ref:`Bricks <primer_bricks>` können zu einem Stapel zusammengesteckt werden. 
Ein :ref:`Master Brick<master_brick>` (als unterstes Brick) kümmert sich 
um die Kommunikation aller anderen Teilnehmer im Stapel. Er routet Nachrichten 
zwischen den Teilnehmern und dem steuernden Gerät. Es ist also nur eine USB
Verbindung notwendig um die Bricks und Bricklets eines Stapels zu steuern.
Aus Benutzersicht verhält sich ein Stapel so, als wären alle Bricks einzeln
per USB am Gerät angeschlossen. Das :ref:`Stapel Tutorial
<tutorial_first_steps_build_stacks>` beinhaltet weitere Informationen über
Stapel.

Über :ref:`Master Extensions <primer_master_extensions>` kann die USB
Verbindung eines Stapels durch :ref:`Ethernet <ethernet_extension>`, 
:ref:`WLAN (WIFI) <wifi_extension>` oder 
:ref:`RS485 <rs485_extension>` ersetzt werden.
Reicht die USB Stromversorgung nicht aus, kann ein Stapel auch mit einer 
:ref:`Stromversorgung <primer_power_supplies>` versorgt werden.


.. _primer_programming:

Programmierung/API
^^^^^^^^^^^^^^^^^^

Eine generelle Beschreibung der Programmierschnittstelle kann 
:ref:`hier <programming_interface>` gefunden werden. Eine Übersicht der API 
Bindings für die jeweilige Programmiersprache befindet sich 
:ref:`hier <api_bindings>`. Die API eines Produkts ist auf der jeweiligen 
Produktseite dokumentiert. Hier lassen sich auch spezifische Programmbeispiele 
für jedes Produkt in jeder unterstützen Programmiersprache finden.

Die folgenden Tutorials bilden einen Einstieg in die Verwendung von Bricks und 
Bricklets:

* :ref:`Erste Schritte <tutorial_first_steps>`
* :ref:`Robuster Ansatz <tutorial_rugged_approach>`
* :ref:`Authentifizierung <tutorial_authentication>`
