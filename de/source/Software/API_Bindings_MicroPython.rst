
.. _api_bindings_micropython:

MicroPython - API Bindings
==========================

Die MicroPython Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen MicroPython Skripten
heraus zu steuern, die auf Mikrocontroller-Boards wie ESP32, Raspberry Pi Pico
und anderen laufen. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``source/`` den Quelltext der Bindings als flache ``.py`` Dateien
* in ``examples/`` die Beispiele für alle Bricks und Bricklets
* in ``stubs/`` die ``.pyi`` Type-Stub-Dateien für IDE Code-Vervollständigung

Voraussetzungen
---------------

* `MicroPython <https://micropython.org/>`__ 1.17 oder neuer
* Ein MicroPython-fähiges Board mit WiFi oder Ethernet Netzwerkanbindung
  (z.B. ESP32, Raspberry Pi Pico W)

.. _api_bindings_micropython_install:

Installation
------------

Da MicroPython-Boards ein begrenztes Dateisystem haben und kein pip oder
setuptools unterstützen, gibt es keinen Paketmanager. Stattdessen werden die
Binding-Dateien direkt auf das Board kopiert.

Die ``.py`` Dateien aus dem ``source/`` Ordner der
:ref:`ZIP Datei <downloads_bindings_examples>` können mit einem Tool wie
`mpremote <https://docs.micropython.org/en/latest/reference/mpremote.html>`__,
`Thonny <https://thonny.org/>`__ oder
`ampy <https://github.com/scientificit/ampy>`__ auf das Board kopiert werden.
Zum Beispiel mit mpremote::

 mpremote cp source/ip_connection.py :
 mpremote cp source/bricklet_temperature_v2.py :

Es müssen nur die tatsächlich benötigten Bindings kopiert werden, um Platz auf
dem Board zu sparen. Mindestens werden immer ``ip_connection.py`` sowie die
Binding-Datei für jedes zu verwendende Gerät benötigt.

WiFi-Einrichtung
----------------

Für WiFi-fähige Boards (z.B. ESP32) muss die Netzwerkverbindung hergestellt
werden, bevor eine Verbindung zum Brick Daemon aufgebaut werden kann. Dies kann
mit dem ``network`` Modul von MicroPython durchgeführt werden:

.. code-block:: python

  import network

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect("YOUR_SSID", "YOUR_PASSWORD")

  while not wlan.isconnected():
      pass

  print("Connected:", wlan.ifconfig())

hmac-Modul (für Authentifizierung)
----------------------------------

Wenn Authentifizierung (``ipcon.authenticate()``) verwendet werden soll, wird
das ``hmac`` Modul benötigt. Die meisten MicroPython-Builds enthalten es nicht
standardmäßig. Es kann über MicroPythons Paketmanager installiert werden
(benötigt eine Netzwerkverbindung)::

 import mip
 mip.install("hmac")

Test eines Beispiels
--------------------

Um ein MicroPython Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür müssen die ``example_configuration.py`` Datei aus dem
``examples/brick/stepper/`` Ordner und die benötigten Binding-Dateien auf das
Board kopiert werden::

 board/
  -> ip_connection.py
  -> brick_stepper.py
  -> example_configuration.py

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Wenn das Beispiel auf
einem Mikrocontroller-Board ausgeführt wird, muss ``localhost`` durch die
IP-Adresse des Computers ersetzt werden, auf dem der Brick Daemon läuft. Als
``UID`` muss die UID des angeschlossen Stepper Bricks angegeben werden, diese
kann über den Brick Viewer ermittelt werden:

.. code-block:: python

  HOST = "192.168.1.100"
  PORT = 4223
  UID = "XXYYZZ" # Change XXYYZZ to the UID of your Stepper Brick

Dann ist auch schon alles bereit, um dieses Beispiel auf dem Board testen zu
können::

 mpremote run example_configuration.py

.. note::
 Anders als die regulären Python Bindings verwenden die MicroPython Bindings
 eine flache Modulstruktur. Imports verwenden die Form
 ``from ip_connection import IPConnection`` anstatt
 ``from tinkerforge.ip_connection import IPConnection``.

.. note::
 Die MicroPython Bindings verwenden eine synchrone/Polling Architektur. Es gibt
 keinen Hintergrund-Thread für die Callback-Auslieferung. Die Methode
 ``ipcon.dispatch_callbacks(seconds)`` muss periodisch aufgerufen werden, um
 eingehende Callbacks zu verarbeiten. Ein negativer Wert steht für
 unendliche Auslieferung: ``ipcon.dispatch_callbacks(-1)``.

.. note::
 Auto-Reconnect wird in den MicroPython Bindings nicht unterstützt, da dafür
 Hintergrund-Threads benötigt werden. Die Verbindungswiederherstellung muss
 explizit im eigenen Code behandelt werden.

Dateigröße reduzieren mit mpy-cross
------------------------------------

Die ``.py`` Binding-Dateien können mit dem ``mpy-cross`` Tool zu MicroPython
Bytecode (``.mpy`` Dateien) kompiliert werden, um die Dateigröße zu reduzieren
und die Importzeiten zu beschleunigen.

.. important::
 Die ``mpy-cross`` Version muss zur MicroPython Firmware-Version auf dem Board
 passen. Wenn auf dem Board zum Beispiel MicroPython 1.23.x läuft, wird
 ``mpy-cross`` aus dem 1.23 Release benötigt. Eine nicht passende Version führt
 zu Importfehlern auf dem Board.

``mpy-cross`` passend zur Firmware-Version installieren::

 pip install mpy-cross==1.23.0  # Version an eigene Firmware anpassen

Eine Binding-Datei kompilieren::

 mpy-cross bricklet_temperature_v2.py

Dies erzeugt ``bricklet_temperature_v2.mpy`` im selben Verzeichnis. Die
``.mpy`` Datei wird anstelle der ``.py`` Datei auf das Board kopiert. Alle
Imports funktionieren auf die gleiche Weise — MicroPython findet ``.mpy``
Dateien automatisch.

Alle Binding-Dateien auf einmal kompilieren::

 for f in source/*.py; do mpy-cross "$f"; done

Die typische Größenreduzierung beträgt ca. 70-80% im Vergleich zu den
originalen ``.py`` Dateien.

IDE-Unterstützung mit Type Stubs
--------------------------------

Die ZIP-Datei enthält einen ``stubs/`` Ordner mit ``.pyi`` Type-Stub-Dateien
für alle Bindings. Diese ermöglichen Code-Vervollständigung, Typprüfung und
Inline-Dokumentation in IDEs wie VS Code (mit Pylance) oder PyCharm.

Um die Stubs zu verwenden, muss die IDE so konfiguriert werden, dass der
``stubs/`` Ordner als zusätzlicher Analysepfad eingebunden wird. Für VS Code
wird folgendes in die ``.vscode/settings.json`` eingetragen:

.. code-block:: json

 {
   "python.analysis.extraPaths": ["path/to/stubs"]
 }

Die Stubs enthalten vollständige Typ-Annotationen und Docstrings für alle
Geräteklassen, Methoden und Konstanten. Sie werden nicht auf dem Board
benötigt — sie werden nur von der IDE während der Entwicklung verwendet.

API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_MicroPython_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MicroPython>
   Bricks <Bricks_MicroPython>
   Bricks (Abgekündigt) <Bricks_MicroPython_Discontinued>
   Bricklets <Bricklets_MicroPython>
   Bricklets (Abgekündigt) <Bricklets_MicroPython_Discontinued>
