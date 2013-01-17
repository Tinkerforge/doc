.. _rs485_extension:

RS485 Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_rs485_tilted_350.jpg",
	               "Extensions/extension_rs485_tilted_600.jpg",
	               "RS485 Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_rs485_top_100.jpg",
	             "Extensions/extension_rs485_top_600.jpg",
	             "RS485 Extension Oberseite")
	}}
	{{
	    tfdocimg("Extensions/extension_rs485_bottom_100.jpg",
	             "Extensions/extension_rs485_bottom_600.jpg",
	             "RS485 Extension Unterseite")
	}}
	{{ tfdocend() }}


Features
--------

* Lange Verbindungen möglich (bis zu 1200m)
* Erlaubt kabelgebundene Verbindungen zwischen Stapeln
* Konfigurierbare Baudrate, Parität und Stoppbits
* Kann in existierenden RS485 Netzwerken genutzt
  werden (:ref:`Modbus RTU <llproto_modbus>`)


Beschreibung
------------

Die RS485 Extension kann für lange kabelgebundene Kommunikation zwischen
Stapeln genutzt werden. Es wird der differentielle RS485 Standard verwendet
um Längen von **bis zu 1200m** zu erreichen.

Für einen RS485 Bus mit Bricks werden zwei RS485 Extension und zwei Master
Bricks benötigt. Beide Master Bricks können mit einem vollen Stapel aus Bricks
und Bricklets verbunden sein. Dabei muss ein Master per USB mit dem PC
verbunden sein. Aus Programmierer-Sicht ist der RS485 Bus vollkommen
transparent, d.h. alle Bricks und Bricklets können genauso benutzt werden
als wenn sie einzeln per USB angeschlossen wären.

Es ist möglich einen Bus mit mehreren RS485 Extension zu betreiben, dabei
muss einer per USB verbunden sein (Many-to-One Routing).

:ref:`Modbus RTU <llproto_modbus>` wird als Protokoll auf der RS485
Schnittstelle genutzt. Dadurch ist es möglich Stapel aus Bricks und Bricklets
mit RS485 Extension in ein vorhandenes Modbus Netzwerk zu integrieren. Es ist
auch möglich direkt mit einem Stapel über Modbus zu kommunizieren, z.B. über
ein eingebettetes Gerät oder über einen Modbus Gateway.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich:

* RS485 Master oben / WIFI unten
* RS485 Master oben / Chibi Slave unten
* RS485 Master unten / WIFI oben
* RS485 Master unten / Chibi Slave oben
* RS485 Slave oben / Chibi Master unten
* RS485 Slave unten / Chibi Master oben

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    8mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Distanz                  1200m
Maximale Baudrate                 2Mbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Gewicht                           13g
================================  ============================================================


Ressourcen
----------

* ADM3485 Datenblatt (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/datasheets/ADM3485.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/hardware/rs485-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rs485_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rs485-extension>`__)


.. _rs485_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der RS485 Extension.

.. image:: /Images/Extensions/extension_rs485_caption_600.jpg
   :scale: 100 %
   :alt: RS485 Extension mit Beschriftung
   :align: center
   :target: ../../_images/Extensions/extension_rs485_caption_800.jpg


RS485 Busaufbau
---------------

Ein RS485 Bus besteht aus einem Master und mehreren Slaves. Der RS485
Master ist der Master Brick der per USB an den PC angeschlossen ist auf dem
der Brick Daemon läuft. Alle anderen Master Bricks mit RS485 Extension dürfen
keine USB Verbindung haben (sie können allerdings seit Master Brick Firmware
1.1.3 eine USB Power Supply verwenden). Jede RS485 Extension hat eine eigene
Adresse. Diese Adressen müssen innerhalb des Buses eindeutig sein.

Um einen RS485 Bus aufzubauen muss zuerst die RS485 Extension auf einen
Master Brick gesteck werden und der Master Brick über USB mit dem PC verbunden
werden. Im Brick Viewer sollte jetzt ein Master Brick mit erkannter RS485
Extension angezeigt werden. Die RS485 Extension muss jetzt als Master oder
Slave konfiguriert werden wie :ref:`hier <rs485_configuration>` beschrieben.

Wenn alle RS485 Extensions konfiguriert sind kann das Gesamtsystem
zusammengebaut werden. Verbinde die benötigten Bricks und Bricklets zu Stapeln.
Der Master jedes Stapels muss der unterste Brick sein (außer ganz
unten steckt eine Stromversorgung). Die RS485 Extension kann an einem beliebigen
Platz oberhalb des Masters gesteckt werden. Verbinde nun die RS485 Extensions
und setzen den Termination Schalter der ersten und letzten RS485 Extension am
Bus auf "on".

.. image:: /Images/Extensions/extension_rs485_assembly.jpg
   :scale: 90 %
   :alt: RS485 Extension Busaufbau
   :align: center
   :target: ../../_images/Extensions/extension_rs485_assembly.jpg

Nachdem alles zusammen gesteckt ist kann das System gestartet werden. Dabei
müssen zuerst alle RS485 Slaves gestartet werden bevor der RS485 Master
gestartet wird, da der RS485 Master nur direkt nach dem Start nach den Slaves
sucht. Jetzt sollten alle Bricks und Bricklets des RS485 Buses im Brick Viewer
angezeigt werden.


.. _rs485_configuration:

RS485 Konfiguration
^^^^^^^^^^^^^^^^^^^

Um eine RS485 Extension zu konfigurieren muss zuerst eine eindeutige Adresse
für jeden RS485 Slave festgelegt sowie die Baudrate, Parität und Anzahl
Stoppbits für das gesamte RS485 Netzwerk bestimmt werden.

.. image:: /Images/Extensions/extension_rs485_config.jpg
   :scale: 100 %
   :alt: RS485 Extension Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_rs485_config.jpg

Wenn der Bus nicht wirklich riesig ist sollte für "Speed" 2000000 (2Mbit/s),
für "Parity" None und für "Stop bits" 1 gewählt werden. Falls allerdings Timeouts
auftreten und der CRC Fehlerzähler rapide steigt dann sollte eine niedrigere
Baudrate getestet werden. Für die Verwendung der RS485 Extension in einem
bestehenden Modbus Netzwerk müssen diese Einstellungen mit denen der anderen
Netzwerkteilnehmer übereinstimmen.

Um eine RS485 Extension als Slave zu konfigurieren muss zuerst "Slave" als
Typ ausgewählt und dann eine Adresse (1-255) festgelegt werden.

.. image:: /Images/Extensions/extension_rs485_slave.jpg
   :scale: 100 %
   :alt: RS485 Konfiguration für Slave Modus
   :align: center
   :target: ../../_images/Extensions/extension_rs485_slave.jpg

Um eine RS485 Extension als Master zu konfigurieren muss zuerst "Master" als
Typ ausgewählt und dann eine Liste (getrennt mit Komma) an Adressen von RS485
Slaves angegeben werden, mit denen der RS485 Master kommunizieren soll.

.. image:: /Images/Extensions/extension_rs485_master.jpg
   :scale: 100 %
   :alt: RS485 Konfiguration für Master Modus
   :align: center
   :target: ../../_images/Extensions/extension_rs485_master.jpg


RS485 Busmodifikation
^^^^^^^^^^^^^^^^^^^^^

Wenn etwas am Bus verändert werden soll, z.B. neue Bricks oder Bricklets
hinzufügen, dann muss der betroffene Stapel zuerst von seiner
Stromversorgung trennen. Nachdem die Änderungen vorgenommen wurden kann der Stapel
wieder an seine Stromversorgung angeschlossen. Falls der Stapel ein RS485
Slave ist, dann muss auch der dazugehörige RS485 Master neugestartet werden,
da dieser nur beim Start seine zugehörigen RS485 Slaves sucht und die
Kommunikation mit ihnen aufnimmt. Den Neustart des RS485 Masters kann
durch Drücken seines Reset Knopfes erreicht werden, bzw. durch ein kurzes Trennen
seiner USB Verbindung.

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interfaces>`.

