
.. _brick_logger:

Brick Logger
============

Der Brick Logger kann Sensordaten von :ref:`Bricks <primer_bricks>`
und :ref:`Bricklets <primer_bricklets>` sammeln und in einer
`CSV <https://de.wikipedia.org/wiki/CSV_(Dateiformat)>`__ Datei zu späteren
Auswertung speichern. Welche Daten, von welchen Bricklets, in welchem Intervall
und mit welchen Einstellungen gesammelt werden soll, kann individuell
eingestellt werden.
Der Brick Logger ist seit Version 2.3.0 Teil von :ref:`Brick Viewer <brickv>`
und kann mit dem
"Data Logger" Knopf aufgerufen werden. Hier kann der Brick Logger konfiguriert
und auch ausgeführt werden. Es gibt auch eine :ref:`Standalone Version
<brick_logger_standalone>` die von der Kommandozeile aus ausgeführt werden kann.

Konfiguration
-------------

.. image:: /Images/Screenshots/brick_logger_setup_v2_small.jpg
   :scale: 100 %
   :alt: Brick Logger (Setup Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_setup_v2.jpg

Alle gesammelten Sensordaten und Debug-Nachrichten sind mit einem Zeitstempel
versehen. Das Format dieses Zeitstempels kann eingestellt werden. Der Brick
Logger bietet verschiedenen Format zur Auswahl:

* **DD.MM.YYYY HH:MM:SS** ist ein typisches deutsches Format, dass automatisch
  von LibreOffice und Microsoft Office verstanden wird.
* **DD.MM.YYYY HH:MM:SS,000** ist das gleiche deutsche Format, aber mit
  Millisekundenauflösung.
* **MM/DD/YYYY HH:MM:SS** ist ein typisches US-englisches Format, dass
  automatisch von LibreOffice und Microsoft Office verstanden wird.
* **MM/DD/YYYY HH:MM:SS.000** ist das gleiche US-englische Format, aber mit
  Millisekundenauflösung.
* **ISO 8601** folgt dem `ISO 8601 <https://de.wikipedia.org/wiki/ISO_8601>`__
  Standard for die Darstellung von Datum und Uhrzeit.
* **ISO 8601 + Milliseconds** folgt auch dem ISO 8601 Standard, aber mit
  Millisekundenauflösung.
* **Unix** `zählt die Sekunden, die seit 1970-01-01T00:00:00Z vergangen sind
  <https://de.wikipedia.org/wiki/Unixzeit>`__.
* **Unix + Milliseconds** zählt auch Sekunden, aber mit Millisekundenauflösung.
* **strftime** ermöglich es ein eigenes Zeitstempelformat mit Pythons `strftime
  <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`__
  Syntax zu definieren.

Wenn nicht klar ist, welches Format hier am besten ausgewählt werden sollte,
dann empfehlen wir entweder **DD.MM.YYYY HH:MM:SS** oder **MM/DD/YYYY HH:MM:SS**
auszuwählen.

Standardmäßig werden die Sensordaten und Debug-Nachrichten nur auf den "Data"
und "Debug" Tabs angezeigt. Diese Tabs zeigen jeweils die letzten 1000 Einträge
an. Zusätzlich werden die Daten und Nachrichten auch in Dateien geschrieben,
wenn die entsprechenden Häkchen gesetzt sind.

.. image:: /Images/Screenshots/brick_logger_devices_v2.jpg
   :scale: 100 %
   :alt: Brick Logger (Devices Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_devices_v2.jpg

Auf dem "Devices" Tab kann eingestellt werden, welche Sensordaten gesammelt
werden sollen. Als erstes muss die UID des Bricks oder Bricklets angegeben
werden. Der "Add Device" Dialog schlägt verbundenen Geräte, samt UID vor.

Jedes unterstützte Gerät bietet mindestens einen Sensorwert im "Values"
Abschnitt an, der geloggt werden kann. Standardmäßig ist das Intervall für alle
Sensorwerte auf 0 eingestellt. Dies bedeutet, dass dieser Sensorwert
nicht geloggt werden wird. Bei einem Intervall von X Sekunden oder Millisekunden
(mit X größer als 0) wird der entsprechende Sensorwert alle X Sekunden oder
Millisekunden abgefragt und aufgezeichnet. Wenn ein Intervall in Millisekunden
eingestellt wird sollte auch ein Zeitstempelformat mit Millisekundenauflösung
auf dem "Setup" Tab ausgewählt werden.

Wenn ein Gerät Optionen besitzt, dann werden diesem im "Options" Abschnitt
aufgelistet. Der Brick Logger kümmert sich automatisch darum, die
eingestellten Options vorzunehmen.

Sobald die Konfiguration komplett ist kann der Logging-Vorgang mittels des
"Start Logging" Knopfes gestartet werden. Der Logging-Vorgang läuft, bis er
über den "Stop Logging" Knopf beendet oder Brick Viewer geschlossen wird.

Über die "Load Config" und "Save Config" Knöpfe kann die aktuelle Konfiguration
geladen und gespeichert werden.

.. _brick_logger_standalone:

Standalone
----------

Der Brick Logger kann auch außerhalb von Brick Viewer verwendet werden. Dazu
steht der Brick Logger auch einzeln als `Python Skript
<https://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.zip>`__
zur Verfügung. Um es verwenden zu können, müssen die :ref:`Python API Bindings
<api_bindings_python>` installiert werden und in Brick Viewer eine Konfiguration
erstellt und gespeichert werden. Dann kann der Brick Logger so gestartet werden
(``config.json`` ist eine zuvor händisch gespeicherte Konfiguration):

.. code-block:: bash

  python brick-logger.py config.json

RED Brick
^^^^^^^^^

Der Brick Logger ist auch als `vorkonfiguriertes RED Brick Program
<https://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.tfrba>`__
verfügbar. Siehe die :ref:`RED Brick Dokumentation
<red_brick_brickv_import_export_tab>` für Details.

Nach dem Import des Programs muss die Konfiguration als ``config.json``
zum Program hochgeladen werden. Dabei muss die existierende Konfigurationsdatei
ersetzt werden. Nach erfolgreichem Upload muss der Brick Logger über den "Exit"
Knopf des Programs im Brick Viewer beendet werden. Der RED Brick startet den
Brick Logger dann automatisch mit der neuen Konfiguration neu.

.. image:: /Images/Screenshots/brick_logger_red_brick.jpg
   :scale: 100 %
   :alt: Brick Logger Program on RED Brick
   :align: center
   :target: ../_images/Screenshots/brick_logger_red_brick.jpg
