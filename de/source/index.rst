.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############
Dokumentation
#############


.. _index_product_overview:

****************
Produktübersicht
****************

Unsere :ref:`Produkte <product_overview>` gliedern sich in fünf verschiedene
Kategorien:

* :ref:`product_overview_bricks`
* :ref:`product_overview_bricklets`
* :ref:`product_overview_master_extensions`
* :ref:`product_overview_power_supplies`
* :ref:`product_overview_accessories`

Die :ref:`Timeline <timeline>` gibt eine Übersicht über zukünftige Produkte und
Entwicklungen.

.. toctree::
   :hidden:

   Product_Overview
   Timeline

.. _index_tutorials:

*****************
Tutorials und FAQ
*****************

Diese Tutorials führen in die Verwendung von Bricks und Bricklets und deren
Konzepte ein:

* :ref:`Erste Schritte <tutorial_first_steps>`
* :ref:`Robuster Ansatz <tutorial_rugged_approach>`

Antworten auf häufig gestellte Fragen finden sich in den :ref:`FAQ <faq>`.

.. toctree::
   :hidden:

   Tutorials/Tutorial_Extending/Tutorial
   Tutorials/Tutorial_Rugged/Tutorial
   FAQ
.. _index_kits:

****
Kits
****

Für einen einfachen Einstieg bieten wir Kits in verschiedenen Themenbereichen an:

* :ref:`starter_kit_weather_station`

.. * :ref:`starter_kit_hardware_hacking`

.. toctree::
   :hidden:

   Kits/WeatherStation/WeatherStation
   Kits/HardwareHacking/HardwareHacking


.. _index_software:

********
Software
********

Die Software umfasst Dienst- und Testprogramme, die API zur Verwendung der
Bricks und Bricklets sowie deren Firmwares und Plugins:

* :ref:`brickd`
* :ref:`brickv`
* :ref:`api_bindings`
* :ref:`firmwares_and_plugins`

Diese können im :ref:`Downloadbereich <downloads>` heruntergeladen werden.
Die :ref:`Quelltexte und Links zu Bug Trackern <source_code>` befinden sich in
einem eigenen Bereich.

Die Grundlagen der verschiedenen Programmierschnittstellen werden
:ref:`hier <pi>` beschrieben.

Im `Januar 2013 <http://www.tinkerforge.com/de/blog/2013/1/15/protokoll-2-0-verfuegbar>`__
haben wir das Kommunikationsprotokoll der Bricks überarbeitet. Für Programme
die vor diesem Zeitpunkt entwickelt wurden gibt es eine Anleitung für den
:ref:`Übergang von Protokoll 1.0 auf Protokoll 2.0 <transition_1to2>`.

.. toctree::
   :hidden:

   Software/Brickd
   Software/Brickv
   Software/API_Bindings
   Software/Firmwares_And_Plugins
   Downloads
   Source_Code
   Programming_Interfaces
   Transitioning_Guide_1To2

.. toctree::
   :glob:
   :hidden:

   Software/*
   Software/Bricks/*
   Software/Bricklets/*


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

.. toctree::
   :hidden:

   Technical_Data
   Low_Level_Protocols/TCPIP
   Low_Level_Protocols/Modbus


.. _index_links:

*****
Links
*****

Die folgenden Tabelle fassen die Hardware und API Dokumentation für schnellen
Zugriff zusammen.

.. include:: index_links.table

.. toctree::
   :glob:
   :hidden:

   Hardware/Bricks/*
   Hardware/Bricklets/*
   Hardware/Master_Extensions/*
   Hardware/Power_Supplies/*
   Hardware/Accessories/*

Die Dokumentation für Protokoll 1.0 befindet sich
`hier <http://www.tinkerforge.com/de/doc_v1/index.html>`__.
