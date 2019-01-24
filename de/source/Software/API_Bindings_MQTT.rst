
.. _api_bindings_mqtt:

MQTT - API Bindings
===================

Die MQTT-Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` mit dem MQTT Protokoll zu steuern.
Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``tinkerforge_mqtt`` ein Pythonscript, dass als Übersetzungsproxy zwischen einem MQTT-Broker und einem Brick Daemon agiert
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die MQTT-Bindings basieren auf den :ref:`Python Bindings <api_bindings_python>`.


Voraussetzungen
---------------

* Python 2.7.9 oder neuer mit dem ``argparse`` Modul, Python 3.4 oder neuer wird auch unterstützt
* Die Python-Bibliothek von Paho, Version 1.3.1 oder neuer.


.. _api_bindings_mqtt_install:

Installation
------------

Die MQTT-Bindings können installiert werden, können aber auch ohne Installation
verwendet werden.

Zur Installation wird die ``tinkerforge_mqtt`` Datei in einen Ordner kopiert der
sich im PATH befindet. Das kann unter Linux und macOS folgender Ordner sein::

 /usr/local/bin/

Unter Windows bietet sich der ``Scripts/`` Ordner der Python Installation an::

 C:\Python27\Scripts\

Damit die Bindings unter Windows direkt aufgerufen werden können muss noch eine
``tinkerforge_mqtt.bat`` Datei im ``Scripts/`` Ordner mit folgendem Inhalt angelegt
werden::

 @"C:\Python27\python.exe" "C:\Python27\Scripts\tinkerforge_mqtt"

Wenn sich die Python-Installation nicht im ``C:\Python27\`` Ordner befindet,
dann ist natürlich der Inhalt der ``tinkerforge_mqtt.bat`` Datei entsprechend
abzuändern.

Test eines Beispiels
--------------------

Um ein MQTT-Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Dann muss das ``tinkerforge_mqtt``-Script so ausgeführt werden, dass es sich mit
dem Brick Daemon, sowie dem MQTT-Broker verbinden kann.

Alle Beispiele sind als Pseudocode geschrieben, der in eine Programmiersprache nach Wahl
übersetzt werden muss. Alternativ können die mosquitto_pub und mosquitto_sub Befehle,
die ein Teil des mosquitto MQTT-Brokers sind, verwendet werden.

Die Beispiele bestehen aus einem setup- und einem cleanup-Block. Der setup-Block
konfiguriert die Geräte und Callbacks, der cleanup-Block hält sie an. Nicht jedes
Beispiel hat einen cleanup-Block.

Der Pseudocode zeichnet MQTT-Publish-Operationen als ``publish [PAYLOAD] to [TOPIC]``
sowie MQTT-Subscribe-Operationen als ``subscribe to [TOPIC]`` aus. Falls weitere Logik
ausgeführt werden soll, wenn eine Subscription eine Nachricht erhält, steht diese im
``subscribe``-Block, der mit ``endsubscribe`` beendet wird.

MQTT-Topics
^^^^^^^^^^^

Die Struktur der MQTT-Topics ist wie folgt: ``[GLOBAL_PREFIX/][OPERATION]/[DEVICE][/UID/][FUNCTION][/SUFFIX]``

``[GLOBAL_PREFIX/]`` ist der globale Präfix aller Topics (Standardeinstellung: ``tinkerforge/``).
Er kann mit dem ``--global-topic-prefix`` Kommandozeilenargument geändert werden. Der Präfix
kann verwendet werden um zwischen mehreren Instanzen der MQTT-Bindings zu unterscheiden. Außerdem
kann er mehrere Topic-Levels beinhalten, zum Beispiel ``tinkerforge/wohnzimmer/sensoren``. Wenn
der konfiguriere Präfix nicht mit einem '/' endet, wird es von den Bindings eingefüht, es sei denn
ein leerer Prefix wurde konfiguriert. Dann beginnen alle Topics mit der Operation. Dieses Vorgehen wird wegen
möglichen Namenskonflikten nicht empfohlen. Außerdem ist zu beachten, dass '/' ein gültiger Präfix ist.

``[OPERATION]`` ist der Typ der Anfrage. Dieser kann ``request``, ``response``, ``register`` oder ``callback`` sein.
Die Bindings subscriben auf ``request``- und ``register``-Topics und publishen Antworten auf ``request``- unter
``response``-Topics, Antworten auf ``register``- unter ``callback``-Topics.

``[DEVICE]`` ist der Typ des Gerätes mit dem interagiert werden soll. Dies kann der Name eines Bricks
oder Bricklets in snake_case, oder ``ip_connection`` sein. Siehe die Dokumentation der Geräte für die
genaue Schreibweise.

``[/UID/]`` ist die UID des Gerätes. Wenn das Gerät die ``ip_connection`` ist, muss die UID leer und ohne '/' sein,
zum Beispiel ``.../ip_connection/enumerate``.

``[FUNCTION]`` ist die Funktion, die aufgerufen, oder das Callback, das registriert werden soll (in snake_case).

``[/SUFFIX]`` ist der optionale Suffix der an Antworten angehangen wird. Dieser kann verwendet werden, um Nachrichten
zu filtern. Zum Beispiel kann er für Requests oder Callback-Registrierungen, die Statusinformationen abfragen
auf ``/STATUS`` gesetzt werden. Ein anderer MQTT-Client kann sich dann auf ``[GLOBAL_PREFIX/]+/+/+/+/STATUS`` registrieren
um alle Statusmeldungen zu erhalten.

Ein typisches Request-Topic sieht aus wie folgt: ``tinkerforge/request/rgb_led_button_bricklet/Dod/get_color``.
Die Antwort auf diesen Request wird von den Bindungs unter
``tinkerforge/response/rgb_led_button_bricklet/Dod/get_color`` zurückgegeben.

Ein Callback-Registrierungs-Topic sieht aus wie folgt: ``tinkerforge/register/rgb_led_button_bricklet/Dod/button_state_changed``.
Durch subscriben von ``tinkerforge/callback/rgb_led_button_bricklet/Dod/button_state_changed`` wird jedes Mal, wenn
der Button gedrückt, oder losgelassen wird, eine Nachricht empfangen.

MQTT-Payload
^^^^^^^^^^^^

Jeglicher MQTT-Payload wird als JSON-Objekt enkodiert, dabei bildet fast jedes Feld
auf einen Parameter oder Rückgabewert der Python-Bindings ab. Aufgetretene Fehler werden
auf stdout geloggt, außerdem werden sie als ``_ERROR``-Feld im JSON-Objekt zurückgegeben.

Falls die symbolische Ausgabe nicht durch das ``--no-symbolic-response`` Kommandozeilenargument deaktiviert wurde,
werden Integer-Konstanten zu Strings übersetzt. Zum Beispiel gibt dann das button_state_changed-Callback des
RGB-LED-Button-Bricklets  ``{"state": "pressed"}`` anstelle von ``{"state:" 0}`` zurück.

Integer-Konstanten im Request-Payload können auch durch die zugehörigen Symbole ersetzt werden. Zum Beispiel
ist es äquivalent, ``{"config": "show_heartbeat"}`` oder ``{"config": 2}`` auf das Thema
``tinkerforge/request/rgb_led_button_bricklet/Dod/set_status_led_config`` zu publishen.

Symbole für Konstanten sind dokumentiert, wenn sie verfügbar sind.

Callback(de)registrierungen können entweder ``{"register": true/false}`` oder ``true/false`` als Payload haben.

API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_MQTT_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MQTT>
   Bricks <Bricks_MQTT>
   Bricks (Abgekündigt) <Bricks_MQTT_Discontinued>
   Bricklets <Bricklets_MQTT>
   Bricklets (Abgekündigt) <Bricklets_MQTT_Discontinued>
