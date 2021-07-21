
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
  Basismodule des Tinkerforge Systems mit eigenen Funktionen.
* :ref:`Bricklets <primer_bricklets>`:
  Sensor-/Aktormodule, die die Fähigkeiten von Bricks
  erweitern und per Kabel an Bricks angeschlossen werden.
* :ref:`Master Extensions <primer_master_extensions>`:
  Module, die Alternativen zur USB-Schnittstelle des
  :ref:`Master Bricks <master_brick>` bieten (WIFI, Ethernet, RS485).
* :ref:`Stromversorgungen <primer_power_supplies>`:
  Module, die einen Stapel aus Bricks mit Strom versorgen.

Die Verwendung von Bricks und Bricklets demonstriert :ref:`dieses Tutorial <tutorial_first_steps>`.


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

    - .. image:: /Images/Bricks/brick_hat_tilted_top_100.jpg
       :scale: 100 %
       :alt: HAT Brick
       :align: center
       :target: _images/Bricks/brick_hat_tilted_top_800.jpg

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

.. include:: Primer_bricks.content

.. include:: Primer_bricks.table


.. _primer_bricklets:

Bricklets
^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Bricklets/bricklet_lcd_128x64_tilted_100.jpg
       :scale: 100 %
       :alt: LCD 128x64 Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_lcd_128x64_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_nfc_tilted_100.jpg
       :scale: 100 %
       :alt: NFC Brickelt
       :align: center
       :target: _images/Bricklets/bricklet_nfc_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_rotary_encoder_v2_tilted_100.jpg
       :scale: 100 %
       :alt: Rotary Encoder Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_rotary_encoder_v2_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_tilted_100.jpg
       :scale: 100 %
       :alt: Piezo Speaker Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_piezo_speaker_v2_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_industrial_quad_relay_v2_tilted2_100.jpg
       :scale: 100 %
       :alt: Industrial Quad Relay Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_industrial_quad_relay_v2_tilted2_800.jpg

    - .. image:: /Images/Bricklets/bricklet_laser_range_finder_v2_tilted_100.jpg
       :scale: 100 %
       :alt: Laser Range Finder Bricklet 2.0
       :align: center
       :target: _images/Bricklets/bricklet_laser_range_finder_v2_tilted_800.jpg

    - .. image:: /Images/Bricklets/bricklet_thermal_imaging_tilted_100.jpg
       :scale: 100 %
       :alt: Thermal Imaging Bricklet
       :align: center
       :target: _images/Bricklets/bricklet_thermal_imaging_tilted_800.jpg

.. include:: Primer_bricklets.content

.. include:: Primer_bricklets.table


.. _primer_master_extensions:

Master Extensions
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Extensions/extension_ethernet_tilted_100.jpg
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

.. include:: Primer_extensions.content

.. include:: Primer_extensions.table


.. _primer_power_supplies:

Stromversorgungen
^^^^^^^^^^^^^^^^^

.. container:: tfdocimages

 .. list-table::

  * - .. image:: /Images/Power_Supplies/powersupply11_tilted_100.jpg
       :scale: 100 %
       :alt: Step-Down Power Supply
       :align: center
       :target: _images/Power_Supplies/powersupply11_tilted_800.jpg

.. include:: Primer_power_supplies.content

.. include:: Primer_power_supplies.table


Konzepte
--------

.. _primer_stack:

Stapel aus Master Bricks
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /Images/Bricks/brick_master_stack_front_big_350.jpg
    :scale: 100 %
    :alt: Bild eines Stacks von Bricks
    :align: center
    :target: _images/Bricks/brick_master_stack_front_big_800.jpg

Ein spezieller Brick ist der :ref:`Master Brick<master_brick>`. Dieser 4x4cm Brick verfügt
über eine USB-C Schnittstelle über die er und seine angeschlossenen Bricklets gesteuert
werden können. Master Bricks können gestapelt werden, so dass mehr Anschlüsse für Bricklets
zur Verfügung stehen.

Der unterste Master Brick kümmert sich 
um die Kommunikation aller anderen Teilnehmer im Stapel: Er routet Nachrichten 
zwischen den Teilnehmern und dem steuernden Gerät. Es ist also nur eine
USB-Verbindung notwendig, um die Bricks und Bricklets eines Stapels zu steuern.
Aus Benutzersicht verhält sich ein Stapel so, als wären alle Bricks einzeln
per USB am Gerät angeschlossen. Das :ref:`Stapel-Tutorial
<tutorial_first_steps_build_stacks>` beinhaltet weitere Informationen über
Stapel.

Über :ref:`Master Extensions <primer_master_extensions>` kann die
USB-Verbindung eines Stapels durch :ref:`Ethernet <ethernet_extension>`, 
:ref:`WLAN (Wi-Fi) <wifi_extension>` oder 
:ref:`RS485 <rs485_extension>` ersetzt werden.
Reicht die Stromzufuhr über USB nicht aus, kann ein Stapel auch mit einer 
:ref:`Stromversorgung <primer_power_supplies>` betrieben werden.


.. _primer_programming:

Programmierung/API
^^^^^^^^^^^^^^^^^^

Eine generelle Beschreibung der Programmierschnittstelle kann 
:ref:`hier <programming_interface>` gefunden werden. Eine Übersicht der API 
Bindings für die jeweilige Programmiersprache befindet sich 
:ref:`hier <api_bindings>`. Die API eines Produkts ist auf der jeweiligen 
Produktseite dokumentiert. Dort finden sich auch spezifische Programmbeispiele 
für jedes Produkt in jeder unterstützen Programmiersprache.

Die folgenden Tutorials bilden einen Einstieg in die Verwendung von Bricks und 
Bricklets:

* :ref:`Erste Schritte <tutorial_first_steps>`
* :ref:`Robuster Ansatz <tutorial_rugged_approach>`
* :ref:`Authentifizierung <tutorial_authentication>`
