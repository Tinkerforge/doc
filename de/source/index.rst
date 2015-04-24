.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############
Dokumentation
#############


.. _index_tutorials:

***************************
Einstieg, Tutorials und FAQ
***************************

Eine allgemeine Beschreibung zu Bricks, Master Extensions Bricklets und den 
Konzepten befindet sich in der :ref:`Allgemeinen Beschreibung <primer>`.

Tutorials führen in die Verwendung von Bricks und Bricklets und deren
Konzepte ein:

* :ref:`Erste Schritte <tutorial_first_steps>`
* :ref:`Robuster Ansatz <tutorial_rugged_approach>`
* :ref:`Authentifizierung <tutorial_authentication>`
* :ref:`RED Brick <tutorial_red_brick>`

Antworten auf häufig gestellte Fragen finden sich in den :ref:`FAQ <faq>`.

.. toctree::
   :hidden:

   Tutorials/Tutorial_Extending/Tutorial
   Tutorials/Tutorial_Rugged/Tutorial
   Tutorials/Tutorial_Authentication/Tutorial
   Tutorials/Tutorial_RED_Brick/Tutorial
   FAQ


.. _index_hardware:

********
Hardware
********

Unsere :ref:`Produkte <primer_products>` gliedern sich in fünf verschiedene
Kategorien:

* :ref:`primer_bricks`
* :ref:`primer_bricklets`
* :ref:`primer_master_extensions`
* :ref:`primer_power_supplies`
* :ref:`primer_accessories`

Die :ref:`Timeline <timeline>` gibt eine Übersicht über die Historie
veröffentlichter Hardware und gemachter Entwicklungen.


.. raw:: html
   :file: index_hardware.html

.. toctree::
   :hidden:

   Primer
   Timeline

.. toctree::
   :glob:
   :hidden:

   Hardware/Bricks/*
   Hardware/Bricklets/*
   Hardware/Master_Extensions/*
   Hardware/Power_Supplies/*
   Hardware/Accessories/*


.. _index_software:

********
Software
********

Die Software umfasst Dienst- und Testprogramme, die API Bindings zur Verwendung
der Bricks und Bricklets sowie deren Firmwares und Plugins:

* :ref:`brickd`
* :ref:`brickv`
* :ref:`api_bindings`
* :ref:`firmwares_and_plugins`

Diese können im :ref:`Downloadbereich <downloads>` heruntergeladen werden.
Die :ref:`Quelltexte und Links zu Bug Trackern <source_code>` befinden sich in
einem eigenen Bereich.

Die Grundlagen der Programmierschnittstelle werden :ref:`hier
<programming_interface>` beschrieben.

.. raw:: html
   :file: index_api.html

.. toctree::
   :hidden:

   Software/Brickd
   Software/Brickv
   Software/API_Bindings
   Software/Firmwares_And_Plugins
   Downloads
   Source_Code
   Programming_Interface
   Transitioning_Guide_1To2

.. toctree::
   :glob:
   :hidden:

   Software/*

.. include:: Software/Bricks.toctree

.. include:: Software/Bricklets.toctree


.. _index_kits:

***********
Starterkits
***********

Für einen einfachen Einstieg bieten wir Kits in verschiedenen Themenbereichen an:

* :ref:`starter_kit_weather_station`
* :ref:`starter_kit_hardware_hacking`
* :ref:`starter_kit_server_room_monitoring`
* :ref:`starter_kit_blinkenlights`
* :ref:`starter_kit_iot`

..
  * :ref:`starter_kit_camera_slider`

.. toctree::
   :hidden:

   Kits/WeatherStation/WeatherStation
   Kits/HardwareHacking/HardwareHacking
   Kits/ServerRoomMonitoring/ServerRoomMonitoring
   Kits/Blinkenlights/Blinkenlights
   Kits/InternetOfThings/InternetOfThings
   Kits/CameraSlider/CameraSlider


.. _index_embedded_boards:

***************
Embedded Boards
***************

Bricks und Bricklets können einfach mit verschiedenen Embedded Boards kombiniert
werden:

.. toctree::
   :maxdepth: 1
   :glob:

   Embedded/*


.. _index_spec:

***************
Spezifikationen
***************

Diese Spezifikationen umfassen die :ref:`technischen Daten <technical_data>`
der verwendeten Steckverbindungen sowie die verschiedenen verwendeten Low-Level
Protokolle:

* :ref:`llproto_tcpip`
* :ref:`llproto_modbus`

Ein :ref:`Wireshark Dissector <wireshark_dissector>` für TFP
(Tinkerforge Protokoll) ist verfügbar.

.. toctree::
   :hidden:

   Technical_Data
   Low_Level_Protocols/TCPIP
   Low_Level_Protocols/Modbus
   Low_Level_Protocols/Wireshark_Dissector
