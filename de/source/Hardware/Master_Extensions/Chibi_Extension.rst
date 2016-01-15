
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Chibi Master Extension

.. _chibi_extension:

Chibi Master Extension
======================

.. raw:: html

	{% tfgallery %}

	Extensions/extension_chibi_tilted_[?|?].jpg           Chibi Extension
	Extensions/extension_chibi_tilted_complete_[?|?].jpg  Chibi Extension
	Extensions/extension_chibi_top_[?|?].jpg              Chibi Extension Oberseite
	Extensions/extension_chibi_bottom_[?|?].jpg           Chibi Extension Unterseite

	{% tfgalleryend %}

.. note::

 Die Chibi Extension ist abgekündigt und wird nicht mehr verkauft.
 Abhängig vom Einsatzzweck kann die :ref:`WIFI Extension <wifi_extension>`
 als Ersatz verwendet werden.


Features
--------

* 700/800/900MHz Funk Transceiver
* Erlaubt drahtlose Verbindungen zwischen Stapeln
* Konfigurierbare Frequenz und Kanal
* Integrierte Signalstärkemessung


Beschreibung
------------

Die Chibi Extension ist mit einem 700/800/900MHz Funk Transceiver ausgestattet.
Typischerweise wird dieser für weitreichende `Zigbee
<https://de.wikipedia.org/wiki/ZigBee>`__ Netzwerke eingesetzt.
Leider verbieten es die Zigbee Bedingungen eine GPL Implementierung des Zigbee
Protokoll Stacks (klicke `hier
<http://www.freaklabs.org/index.php/blog/zigbee/zigbee-linux-and-the-gpl.html>`__
für weitere Informationen).

Daher haben wir uns dazu entschlossen den Open Source `Chibi Wireless Stack
<http://www.freaklabs.org/index.php/blog/embedded/introducingchibi-a-simple-small-wireless-stack-for-open-hardware-hackers-and-enthusiasts.html>`__
für diese Extension zu portieren. Es ist ein einfacher und kleiner Protokoll
Stack der perfekt geeignet ist für unsere Anwendungen.

Bei guten Bedingungen können Reichweiten **bis zu 2km** draußen erreicht werden.

Um ein Chibi Netzwerk aufzubauen sind mindestens zwei Chibi Extensions und zwei
Master Bricks notwendig. Jeder dieser Master Bricks kann in einem Stapel aus
Bricks und Bricklets stecken, wobei einer der Master Bricks per USB und der
andere über eine externe Stromversorgung versorgt wird. Aus Programmierersicht
ist das Chibi Netzwerk vollkommen transparent, d.h. alle Bricks und Bricklets
können genauso benutzt werden als wenn sie einzeln per USB angeschlossen wären.

Es ist auch möglich ein Netzwerk mit mehr als zwei Chibi Extensions aufzubauen,
wobei immer nur ein Stapel per USB verbunden sein darf (Many-to-One Routing).

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich.
Die Reihenfolge im Stapel ist dabei nicht relevant:

* Chibi Master / RS485 Slave
* Chibi Slave / RS485 Master

.. note::
 Nach der Konfiguration verhalten sich alle Module des Netzwerks als wenn sie
 einzeln per USB mit dem PC verbunden wären. Daher sind keine
 Programmcodeänderungen notwendig. Allerdings ist die
 Übertragungsgeschwindigkeit von USB höher als die von Chibi, so dass mit
 einem geringeren Durchsatz gerechnet werden muss.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    10mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Reichweite (Freifeld)    2km
Maximale Baudrate                 250kBit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           13g
================================  ============================================================


Ressourcen
----------

* AT86RF212 Datenblatt (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/datasheets/at86rf212.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/hardware/chibi-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/chibi_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/chibi-extension/zipball/master>`__)


Chibi Netzwerkaufbau
--------------------

Ein Chibi Netzwerk besteht aus einem Master und mehreren Slaves. Der Chibi
Master ist der Master Brick der per USB an den PC angeschlossen ist auf dem
der Brick Daemon läuft. Alle anderen Master Bricks mit Chibi Extension dürfen
keine USB Verbindung haben (sie können allerdings seit Master Brick Firmware
1.1.3 eine USB Power Supply verwenden). Jede Chibi Extension hat eine eigene
Adresse. Diese Adressen müssen innerhalb der Sendereichweite eindeutig sein.

.. note::
 Falls mehrere Netzwerke mit gleichen Kanal und Frequenzeinstellungen
 nebeneinander betrieben werden sollen, dann muss sichergestellt sein, dass
 die einzelnen Adressen innerhalb der Sendereichweite eindeutig sein und nicht
 in mehreren Netzwerken gleichzeitig benutzt werden.

Um ein Chibi Netzwerk aufzubauen muss zuerst die Chibi Extension auf einen
Master Brick gesteckt werden und der Master Brick über USB mit dem PC verbunden
werden. Im Brick Viewer sollte jetzt ein Master Brick mit erkannter Chibi
Extension angezeigt werden. Die Chibi Extension muss jetzt als Master oder
Slave konfiguriert werden wie :ref:`hier <chibi_configuration>` beschrieben.

Wenn alle Chibi Extensions konfiguriert sind kann das Gesamtsystem
zusammengebaut werden. Verbinde die benötigten Bricks und Bricklets zu Stapeln.
Der Master jedes Stapels muss der unterste Brick sein (außer ganz
unten steckt eine Stromversorgung). Die Chibi Extension kann an einem beliebigen
Platz oberhalb des Masters gesteckt werden.

Nachdem alles zusammen gesteckt ist kann das System gestartet werden. Dabei
müssen zuerst alle Chibi Slaves gestartet werden bevor der Chibi Master
gestartet wird, da der Chibi Master nur direkt nach dem Start nach den Slaves
sucht. Jetzt sollten alle Bricks und Bricklets des Chibi Netzwerkes im Brick
Viewer angezeigt werden.


.. _chibi_configuration:

Chibi Konfiguration
^^^^^^^^^^^^^^^^^^^

.. note::
 Die Chibi Konfiguration wurde in Brick Viewer 1.0.6 geändert. In vorherigen
 Versionen war es nicht notwendig anzugeben ob einen Chibi Extension als
 Master oder Slave arbeiten soll (dies wurde auf anderem Wege ermittelt).

 Es stellte sich aber heraus, dass dies für die meisten Benutzer sehr verwirrend
 war. Daher empfehlen wird auf die neuste Brick Viewer Version zu aktualisieren
 bevor das Chibi Netzwerk konfiguriert wird.

Um eine Chibi Extension zu konfigurieren muss zuerst eine eindeutige Adresse
für jede Chibi Extension festgelegt werden sowie eine Frequenz und einen Kanal
für das gesamte Chibi Netzwerk bestimmt werden.

.. image:: /Images/Extensions/extension_chibi.jpg
   :scale: 100 %
   :alt: Konfiguration der Chibi Adresse, Frequenz und Kanal
   :align: center
   :target: ../../_images/Extensions/extension_chibi.jpg

Um eine Chibi Extension als Slave zu konfigurieren muss zuerst "Slave" als
Typ ausgewählt und dann die Adresse des Chibi Masters angegeben werden.

.. image:: /Images/Extensions/extension_chibi_slave.jpg
   :scale: 100 %
   :alt: Konfiguration einer Chibi Extension für Slave Modus
   :align: center
   :target: ../../_images/Extensions/extension_chibi_slave.jpg

Um eine Chibi Extension als Master zu konfigurieren muss zuerst "Master" als
Typ ausgewählt und dann eine Liste (getrennt mit Komma) an Adresse von Chibi
Slaves angegeben werden, mit denen der Chibi Master kommunizieren soll.

.. image:: /Images/Extensions/extension_chibi_master.jpg
   :scale: 100 %
   :alt: Konfiguration einer Chibi Extension für Master Modus
   :align: center
   :target: ../../_images/Extensions/extension_chibi_master.jpg

Zum Schluss muss auf "Save Chibi Configuration" geklickt werden um die
Konfiguration dauerhaft auf der Chibi Extension zu speichern.
Dann muss der Master Brick neu gestartet werden um die neue Konfiguration zu
übernehmen.


Chibi Netzwerkmodifikation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn etwas am Netzwerk verändert werden soll, z.B. neue Bricks oder Bricklets
hinzufügen, dann muss der betroffene Stapel zuerst von seiner
Stromversorgung getrennt werden. Nachdem die Änderungen vorgenommen wurde kann
der Stapel wieder an seine Stromversorgung angeschlossen werden. Falls der Stapel ein Chibi
Slave ist, dann muss auch der dazugehörige Chibi Master neu gestartet werden,
da dieser nur beim Start seine zugehörigen Chibi Slaves sucht und die
Kommunikation mit ihnen aufnimmt. Den Neustart des Chibi Masters kann
durch Drücken seines Reset Knopfes erreicht werden, bzw. durch ein kurzes Trennen
seiner USB Verbindung.


Chibi Frequenz und Kanal
^^^^^^^^^^^^^^^^^^^^^^^^

Die Chibi Extension unterstützt verschiedene Frequenzen mit mehrere Kanälen. In
verschiedenen Teilen der Welt sind jeweils verschiedene Frequenzen und Kanäle
zur Nutzung freigeben.

Hier ist eine Liste von Frequenzen und zugehörigen Kanälen:

.. csv-table::
 :header: "Frequenz", "Mögliche Kanäle"
 :widths: 40, 60

 "OQPSK 868MHz (Europa)", "0"
 "OQPSK 915MHz (US)", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
 "OQPSK 780MHz (China)", "0, 1, 2, 3"
 "BPSK40 915MHz", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

.. warning::
 Die Chibi Extension wird als elektronisches Bauteil verkauft. Es liegt in der
 Verantwortung des Nutzers sicherzustellen, dass das aufgebaute System den
 jeweiligen lokalen gesetzlichen Bestimmungen entspricht. Dazu gehört auch
 sicherzustellen, dass die konfigurierte Frequenz am jeweiligen Standort für die
 Nutzung freigegeben ist!


Programmierschnittstelle
------------------------

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interface>`.
