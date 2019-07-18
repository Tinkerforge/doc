
:shoplink: ../../../shop/master-extensions/rs485-master-extension.html

.. _rs485_extension:

RS485 Master Extension
======================

.. raw:: html

	{% tfgallery %}

	Extensions/extension_rs485_v11_tilted_[?|?].jpg  RS485 Extension
	Extensions/extension_rs485_v11_top_[?|?].jpg     RS485 Extension Oberseite
	Extensions/extension_rs485_v11_bottom_[?|?].jpg  RS485 Extension Unterseite

	{% tfgalleryend %}


Features
--------

* Erlaubt kabelgebundene Verbindungen zwischen Stapeln aus Bricks
* Lange Verbindungen möglich (bis zu 1200m)
* Konfigurierbare Baudrate, Parität und Stoppbits
* Kann in existierenden RS485 Netzwerken genutzt
  werden (:ref:`Modbus RTU <llproto_modbus>`)


Beschreibung
------------

Die RS485 Extension kann für lange kabelgebundene Kommunikation zwischen
:ref:`Stapeln <primer_stack>` genutzt werden. Es wird der differentielle RS485 
Standard verwendet um Längen von **bis zu 1200m** zu erreichen.

Für einen RS485 Bus mit :ref:`Bricks <primer_bricks>` werden zwei RS485 
Extension und zwei :ref:`Master Bricks <master_brick>` benötigt. Beide Master 
Bricks können mit einem vollen Stapel aus Bricks und 
:ref:`Bricklets <primer_bricklets>` verbunden sein. Dabei muss ein 
Master per USB, Ethernet oder WLAN mit dem PC verbunden sein. Aus
Programmierer-Sicht ist der RS485
Bus vollkommen transparent, d.h. alle Bricks und Bricklets können genauso 
benutzt werden als wenn sie einzeln per USB angeschlossen wären.

Es ist möglich einen Bus mit mehreren RS485 Extension zu betreiben, dabei
muss einer per USB, Ethernet oder WLAN verbunden sein (Many-to-One Routing).

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich.
Die Reihenfolge im Stapel ist dabei nicht relevant:

* RS485 Master / Ethernet
* RS485 Master / WIFI
* RS485 Master / WIFI 2.0
* RS485 Master / Chibi Slave [abgekündigt]
* RS485 Slave / Chibi Master [abgekündigt]

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
* 3D Modell (`Online ansehen <https://autode.sk/2iTPXMM>`__ | Download: `STEP <https://download.tinkerforge.com/3d/extensions/rs485/rs485-extension.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/extensions/rs485/rs485_extension.FCStd>`__)


Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der RS485 Extension.

.. image:: /Images/Extensions/extension_rs485_v11_caption_600.jpg
   :scale: 100 %
   :alt: RS485 Extension mit Beschriftung
   :align: center
   :target: ../../_images/Extensions/extension_rs485_v11_caption_800.jpg


RS485 Busaufbau
---------------

Ein RS485 Bus besteht aus einem Master und mehreren Slaves. Der RS485
Master ist der Master Brick der per USB, Ethernet oder WLAN an den PC
angeschlossen ist auf dem
der Brick Daemon läuft. Alle anderen Master Bricks mit RS485 Extension dürfen
keine USB, Ethernet or WIFI Verbindung haben (sie können allerdings seit
Master Brick Firmware
1.1.3 eine USB Power Supply verwenden). Jede RS485 Extension hat eine eigene
Adresse. Diese Adressen müssen innerhalb des Buses eindeutig sein.

Um einen RS485 Bus aufzubauen muss zuerst die RS485 Extension auf einen
Master Brick gesteckt werden und der Master Brick über USB, Ethernet oder WLAN
mit dem PC verbunden
werden. Im Brick Viewer sollte jetzt ein Master Brick mit erkannter RS485
Extension angezeigt werden. Die RS485 Extension muss jetzt als Master oder
Slave konfiguriert werden wie :ref:`hier <rs485_extension_configuration>`
beschrieben.

Wenn alle RS485 Extensions konfiguriert sind kann das Gesamtsystem
zusammengebaut werden. Verbinde die benötigten Bricks und Bricklets zu Stapeln.
Der Master jedes Stapels muss der unterste Brick sein (außer ganz
unten steckt eine Stromversorgung). Die RS485 Extension kann an einem beliebigen
Platz oberhalb des Masters gesteckt werden. Verkabele nun die RS485 Extensions
und setzen den Termination Schalter der ersten und letzten RS485 Extension am
Bus auf "on".

.. image:: /Images/Extensions/extension_rs485_assembly.jpg
   :scale: 90 %
   :alt: RS485 Extension Busaufbau
   :align: center
   :target: ../../_images/Extensions/extension_rs485_assembly.jpg

Wenn der Bus nur ein paar Meter lang ist spielt das verwendete Kabel
normalerweise keine Rolle. Wenn der Bus länger als ein paar Meter ist, dann
sollte eine Form von `Twisted Pair
<https://de.wikipedia.org/wiki/Twisted-Pair-Kabel>`__ Kabel verwendet werden.
Normales Telefonkabel hat häufig verdrillte Aderpaare. Noch besser ist
Ethernetkabel, da es verdrillt und normalerweise auch geschirmt ist. Wenn
ein Kabel mit verdrillten Aderpaaren verwendet wird, dann sollte das gleiche
Aderpaar für A und B verwendet werden und eine anderes Aderpaar für GND.

Nachdem alles zusammengesteckt ist kann das System gestartet werden. Dabei
müssen zuerst alle RS485 Slaves gestartet werden bevor der RS485 Master
gestartet wird, da der RS485 Master nur direkt nach dem Start nach den Slaves
sucht. Jetzt sollten alle Bricks und Bricklets des RS485 Buses im Brick Viewer
angezeigt werden.


.. _rs485_extension_configuration:

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

Zum Schluss muss auf "Save RS485 Configuration" geklickt werden um die
Konfiguration dauerhaft auf der RS485 Extension zu speichern.
Dann muss der Master Brick neu gestartet werden um die neue Konfiguration zu
übernehmen.


RS485 Busmodifikation
^^^^^^^^^^^^^^^^^^^^^

Wenn etwas am Bus verändert werden soll, z.B. neue Bricks oder Bricklets
hinzufügen, dann muss der betroffene Stapel zuerst von seiner
Stromversorgung getrennt werden. Nachdem die Änderung vorgenommen wurde kann der Stapel
wieder an seine Stromversorgung angeschlossen werden. 

Seit Master Brick Firmware Version 2.4.6 ist das Verhalten nach einem
Neustart wie folgt:

* Wenn der Stapel eines RS485-Masters neugestartet wird, senden alle Bricks/Bricklets
  des RS485-Netzwerkes nochmal ihre initiale Enumerierung.

* Wenn der Stapel eines RS485-Slaves neugestartet wird, senden nur die Bricks/Bricklets
  im Stapel des Slaves ihre initiale Enumerierung nochmal.


Programmierschnittstelle
------------------------

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interface>`.
