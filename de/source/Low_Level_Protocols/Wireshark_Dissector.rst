
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#specifications">Spezifikationen</a> / Wireshark Dissector

.. _wireshark_dissector:

Wireshark Dissector
===================

`Wireshark <http://www.wireshark.org>`__ ist ein freies Programm zur Analyse
von Netzwerk-Kommunikationsverbindungen.

Das Werkzeug stellt entweder während oder nach der Aufzeichnung 
von Datenverkehr einer Netzwerk-Schnittstelle die Daten in Form einzelner 
Pakete dar. Dabei werden die Daten übersichtlich und für den Menschen 
nachvollziehbar analysiert. So kann der Inhalt der mitgeschnittenen Pakete
betrachtet oder nach Inhalten gefiltert werden.

Ein Wireshark Dissector ist ein Plugin für ein spezifisches Protokoll. Mit
dem TFP (Tinkerforge Protocol) Dissector ist es möglich sowohl das Protokoll
welches zwischen :ref:`Bindings <api_bindings>` und 
:ref:`Brick Daemon <brickd>` (TCP/IP) als auch das Protokoll welches
zwischen Brick Daemon und :ref:`Bricks <primer_bricks>` (USB)
genutzt wird zu analysieren.

Der Dissector kann nützlich sein um Bugs in den Bindings und in brickd zu
debuggen. Er ist auch sehr hilfreich beim erstellen neuer Bindings.

.. image:: /Images/Screenshots/wireshark_dissector.jpg
   :scale: 100 %
   :alt: Wireshark Dissector
   :align: center
   :target: ../_images/Screenshots/wireshark_dissector.jpg

Installation
------------

Der TFP Dissector ist im Wireshark SVN trunk seit
`November 2013 <https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9324>`__. 
Er ist noch nicht in der letzten "stable" Veröffentlichung. Die folgenden
Schritte sind notwendig um Wireshark aus dem Quellcode zu installieren::

 svn co http://anonsvn.wireshark.org/wireshark/trunk/ wireshark
 cd wireshark/
 ./autogen.sh
 ./configure
 make

Wireshark kann nun direkt gestartet werden::

 ./wireshark

Oder auch installiert werden::

 make install

Wireshark hat viele Abhängigkeiten. Das Configure-Script gibt die
fehlenden Abhängigkeiten aus. Auf Debian basierten System können
alle notwendigen Abhängigkeiten wie folgt installiert werden::

 apt-get build-dep wireshark

Der Dissector selbst ist auch auf
`GibHub verfügbar <https://github.com/Tinkerforge/tf-wireshark-dissector>`__.

Display Filter
--------------

Display Filter sind für alle Felder der TFP Pakete vorhanden.

Nützliche Beispiele:

Zeige nur TFP Pakete::

 tfp

Zeige nur Pakete die von oder zur UID "XYZ" gehen::

 tfp.uid == "XYZ"

Zeige nur Pakete mit einem Fehlercode::

 tfp.e != 0

Zeige nur spezifische Funktionsaufrufe (in diesem Fall Function ID 4)::

 tfp.fid == 4
