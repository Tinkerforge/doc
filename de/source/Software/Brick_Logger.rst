
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Brick Logger

.. _brick_logger:

Brick Logger
============

Der Brick Logger kann Sensordaten von Bricks und Bricklets sammeln und in einer
`CSV <https://de.wikipedia.org/wiki/CSV_(Dateiformat)>`__ Datei zu späteren
Auswertung speichern. Welche Daten, von welchen Bricklets, in welchem Intervall
und mit welchen Einstellungen gesammelt werden soll, kann individuell
eingestellt werden.

Der Brick Logger ist seit Version 2.3.0 Teil von Brick Viewer und kann mit dem
"Data Logger" Knopf aufgerufen werden. Hier kann der Brick Logger konfiguriert
und auch ausgeführt werden. Es gibt auch eine :ref:`Standalone Version
<brick_logger_standalone>` die von der Kommandozeile aus ausgeführt werden kann.

Konfiguration
-------------

.. image:: /Images/Screenshots/brick_logger_setup.jpg
   :scale: 100 %
   :alt: Brick Logger (Setup Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_setup.jpg

Alle gesammelten Sensordaten und Debug-Nachrichten sind mit einem Zeitstempel
versehen. Das Format diese Zeitstempels kann eingestellt werden.

Standardmäßig werden die Sensordaten und Debug-Nachrichten nur auf den "Data"
und "Debug" Tabs angezeigt. Diese Tabs zeigen jeweils die letzten 1000 Einträge
an. Zusätzlich werden die Daten und Nachrichten auch in Dateien geschrieben,
wenn die entsprechenden Häkchen gesetzt sind.

.. image:: /Images/Screenshots/brick_logger_devices.jpg
   :scale: 100 %
   :alt: Brick Logger (Devices Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_devices.jpg

Auf dem "Devices" Tab kann eingestellt werden, welche Sensordaten gesammelt
werden sollen. Als erstes muss die UID des Bricks oder Bricklets angegeben
werden. Der "Add Device" Dialog schlägt verbundenen Geräte, samt UID vor.

Jedes unterstützte Gerät bietet mindestens einen Sensorwert im "Values"
Abschnitt an, der geloggt werden kann. Standardmäßig ist das Intervall für alle
Sensorwerte auf 0 Sekunden eingestellt. Dies bedeutet, dass dieser Sensorwert
nicht geloggt werden wird. Bei einem Intervall von X Sekunden (mit X größer
als 0) wird der entsprechende Sensorwert alle X Sekunden abgefragt und
aufgezeichnet.

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
<http://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.zip>`__
zur Verfügung. Um es verwenden zu können, müssen die :ref:`Python API Bindings
<api_bindings_python>` installiert werden und in Brick Viewer eine Konfiguration
erstellt und gespeichert werden. Dann kann der Brick Logger so gestartet werden
(``config.json`` ist die gespeicherte Konfiguration):

.. code-block:: bash

  python brick-logger.py config.json

RED Brick
^^^^^^^^^

Der Brick Logger ist auch als `vorkonfiguriertes RED Brick Program
<http://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.tfrba>`__
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
