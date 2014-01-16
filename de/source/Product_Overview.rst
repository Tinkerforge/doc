
:breadcrumbs: <a href="index.html">Startseite</a> / Produktübersicht

.. _product_overview:

Produktübersicht
================

Unsere Produkte gliedern sich in fünf verschiedene Kategorien:

* :ref:`Bricks <product_overview_bricks>`:
  Stapelbare Mikrocontrollerplatinen zum Messen und Steuern.
* :ref:`Bricklets <product_overview_bricklets>`:
  Nicht stapelbare Sensor-/Aktorplatinen um die Fähigkeiten eines Bricks zu
  erweitern.
* :ref:`Master Extensions <product_overview_master_extensions>`:
  Platinen um die Kommunikationsmöglichkeiten des
  :ref:`Master Bricks <master_brick>` zu erweitern.
* :ref:`Stromversorgungen <product_overview_power_supplies>`:
  Platinen die einen Stapel von Bricks mit Strom versorgen; werden unter einen
  Stapel gesteckt.
* :ref:`Zubehör <product_overview_accessories>`

Diese :ref:`Tutorial <tutorial_first_steps>` erklärt wie alles zusammen
funktioniert.


.. _product_overview_bricks:

Bricks
------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricks/brick_master_tilted_front_100.jpg
       :scale: 100 %
       :alt: Master Brick
       :align: center
       :target: _images/Bricks/brick_master_tilted_front_800.jpg

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

    - .. image:: /Images/Bricks/brick_imu_tilted_front_100.jpg
       :scale: 100 %
       :alt: IMU Brick
       :align: center
       :target: _images/Bricks/brick_imu_tilted_front_800.jpg


Bricks sind 4 x 4cm (1,57 x 1,57") große Platinen die mit einem
vorprogrammierten 32-Bit ARM
Mikrocontroller, einem Mini-USB Abschluss, zwei Status LEDs, vier Steckern zur
Stapelbildung und bis zu vier Anschlüssen für :ref:`Bricklets
<product_overview_bricklets>` ausgestattet sind. Es gibt Bricks für Messaufgaben
(z.B. :ref:`IMU Brick <imu_brick>`), für Kommunikation (z.B. :ref:`Master Brick
<master_brick>`) und um Motoren zu steuern (z.B. :ref:`DC Brick <dc_brick>`).

Bricks können zu Stapeln zusammengesteckt werden. Ein Master kümmert sich um die
Kommunikation aller anderen Teilnehmer im Stapel. Er routet Nachrichten zwischen
den Teilnehmern und dem PC (:ref:`Programmierschnittstelle <programming_interface>`).
Aus Benutzersicht verhält sich solch ein Stapel so als wären alle Bricks einzeln
per USB am PC angeschlossen. Das :ref:`Stapel Tutorial
<tutorial_first_steps_build_stacks>` beinhaltet weitere Informationen über
Stapel.

.. include:: Product_Overview_bricks.table


.. _product_overview_bricklets:

Bricklets
---------

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

    - .. image:: /Images/Bricklets/bricklet_voltage_tilted_100.jpg
       :scale: 100 %
       :alt: Voltage Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_voltage_tilted_800.jpg

Bricklets erweitern die Fähigkeiten von :ref:`Bricks <product_overview_bricks>`.
Es gibt Bricklets um physikalische Größen wie Rotation, elektrische Spannung,
elektrischen Strom, Umgebungshelligkeit oder Umgebungstemperatur zu messen.
Es gibt auch Bricklets für Steuerungsaufgaben wie Relais, digitale Ein- und
Ausgänge sowie alphanumerische Ausgaben auf LCDs.

Im Gegensatz zu Bricks haben Bricklets keine feste Größe. Jedes Bricklet hat
die kleinste mögliche Größe. Jeder Brick hat bis zu vier Anschlüsse für
Bricklets.

Beim Start erkennt ein Brick die angeschlossenen Bricklets. Die Bricklet Plugins
sind auf einem `EEPROM <http://de.wikipedia.org/wiki/Electrically_Erasable_Programmable_Read-Only_Memory>`__
auf dem Bricklet gespeichert und werden zur Ausführung in den Flash des Bricks
geladen. Dies fügt dem Brick neue Funktionen hinzu die vom PC aus genutzt
werden können.

Siehe :ref:`Programmierschnittstelle <programming_interface>` für weitere
Information.

.. include:: Product_Overview_bricklets.table


.. _product_overview_master_extensions:

Master Extensions
-----------------

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

    - .. image:: /Images/Extensions/extension_rs485_tilted_100.jpg
       :scale: 100 %
       :alt: RS485 Extension
       :align: center
       :target: _images/Extensions/extension_rs485_tilted_800.jpg

    - .. image:: /Images/Extensions/extension_wifi_tilted_100.jpg
       :scale: 100 %
       :alt: WIFI Extension
       :align: center
       :target: _images/Extensions/extension_wifi_tilted_800.jpg

Für die :ref:`Programmierschnittstelle <programming_interface>`
routet der :ref:`Master Brick <master_brick>` Nachrichten zwischen den anderen
:ref:`Bricks <product_overview_bricks>` im Stapel und dem PC. Typischerweise
wird die Verbindung zwischen Master Brick und PC über den USB Anschluss des
Master Bricks hergestellt. Master Extensions erweitern die
Kommunikationsmöglichkeiten eines Master Bricks. Es gibt kabelgebundene und
drahtlose Master Extensions. Aus Programmierersicht sind die verschiedenen
Kommunikationsmöglichkeiten transparent. Ein Stapel mit Master Extension
verhält sich so als wären alle Bricks einzeln per USB am PC angeschlossen.

Dies bedeutet: Programme können mit allen Bricks einzeln per USB am PC
angeschlossen entwickelt werden. Wenn später die Bricks gestapelt und über
eine Master Extension angebunden werden dann funktioniert das zuvor geschrieben
Programm ohne Änderungen weiter.

.. include:: Product_Overview_extensions.table


.. _product_overview_power_supplies:

Stromversorgungen
-----------------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply_tilted_front_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply_tilted_front_800.jpg

Ein Stapel kann über den USB Anschluss des Masters mit Strom versorgt werden.
Diese Möglichkeit ist durch die USB Spezifikation auf 500mA beschränkt. Ein
großer Stapel kann mehr als 500mA Stromverbrauch aufweisen.

Eine Stromversorgung kann einen Stapel mit mehr als 500mA versorgen. Sie kann
auch an Bricks angeschlossen Motoren versorgen (z.B. :ref:`DC Brick <dc_brick>`).
Stromversorgungen haben die Größe von :ref:`Bricks <product_overview_bricks>`
und werden unter einen Stapel gesteckt.

.. include:: Product_Overview_power_supplies.table


.. _product_overview_accessories:

Zubehör
-------

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Accessories/dc_jack_adapter_tilted_100.jpg
       :scale: 100 %
       :alt: DC Jack Adapter
       :align: center
       :target: _images/Accessories/dc_jack_adapter_tilted_800.jpg

.. include:: Product_Overview_accessories.table
