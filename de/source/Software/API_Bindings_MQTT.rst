
.. _api_bindings_mqtt:

MQTT - API Bindings
===================

Die MQTT-Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` mit dem MQTT Protokoll zu steuern.
Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``tinkerforge_mqtt`` ein Python Script, dass als Übersetzungs-Proxy zwischen
  einem MQTT-Broker und einem Brick Daemon agiert
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die MQTT-Bindings basieren auf den :ref:`Python Bindings <api_bindings_python>`.


Voraussetzungen
---------------

* Python 3.4 oder neuer
* Paho MQTT 1.3.1 oder neuer

.. _api_bindings_mqtt_install:

Installation
------------

Die MQTT Bindings können auf zwei Weisen installiert werden:
von unserem :ref:`APT Repository <api_bindings_mqtt_install_apt>` für Debian
basierte Linux Distributionen oder durch
:ref:`händisches <api_bindings_mqtt_install_manual>` Kopieren der Dateien an
die richtige Stelle. Die Bindings können aber auch ohne Installation genutzt werden.

.. _api_bindings_mqtt_install_apt:

Vom APT Repository
^^^^^^^^^^^^^^^^^^

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit. Zuerst das :ref:`APT Repository einrichten
<apt_repository_setup>` dann die Bindings installieren::

 sudo apt install tinkerforge-mqtt

Das Debian Package installiert und startet auch den systemd Service
``tinkerforge_mqtt`` der die MQTT Bindings ausführt.

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das Debian
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_mqtt_install_manual:

Händische Installation
^^^^^^^^^^^^^^^^^^^^^^

Die MQTT-Bindings können installiert werden, können aber auch ohne Installation
verwendet werden.

Zur Installation wird die ``tinkerforge_mqtt`` Datei in einen Ordner kopiert der
sich im PATH befindet. Das kann unter Linux und macOS folgender Ordner sein::

 /usr/local/bin/

Unter Windows bietet sich der ``Scripts/`` Ordner der Python Installation an::

 C:\Python\Scripts\

Damit die Bindings unter Windows direkt aufgerufen werden können muss noch eine
``tinkerforge_mqtt.bat`` Datei im ``Scripts/`` Ordner mit folgendem Inhalt angelegt
werden::

 @"C:\Python\python.exe" "C:\Python\Scripts\tinkerforge_mqtt" %*

Wenn sich die Python-Installation nicht im ``C:\Python\`` Ordner befindet,
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
die ein Teil des Mosquitto MQTT-Brokers sind, verwendet werden.

Die Beispiele bestehen aus einem setup- und einem cleanup-Block. Der setup-Block
konfiguriert die Geräte und Callbacks, der cleanup-Block hält sie an. Nicht jedes
Beispiel hat einen cleanup-Block.

Der Pseudocode zeichnet MQTT-Publish-Operationen als ``publish <PAYLOAD> to <TOPIC>``
sowie MQTT-Subscribe-Operationen als ``subscribe to <TOPIC>`` aus. Falls weitere Logik
ausgeführt werden soll, wenn eine Subscription eine Nachricht erhält, steht diese im
``subscribe``-Block, der mit ``endsubscribe`` beendet wird.

MQTT-Topics
^^^^^^^^^^^

Die Struktur der MQTT-Topics ist wie folgt: ``[<GLOBAL_PREFIX>/]<OPERATION>/<DEVICE>[/<UID>]/<FUNCTION>[/<SUFFIX>]``

``[<GLOBAL_PREFIX>/]`` ist der globale Präfix aller Topics (Standardeinstellung: ``tinkerforge/``).
Er kann mit dem ``--global-topic-prefix`` Kommandozeilenargument geändert werden. Der Präfix
kann verwendet werden um zwischen mehreren Instanzen der MQTT-Bindings zu unterscheiden. Außerdem
kann er mehrere Topic-Levels beinhalten, zum Beispiel ``tinkerforge/wohnzimmer/sensoren``. Wenn
der konfiguriere Präfix nicht mit einem ``/`` endet, wird es von den Bindings eingefügt, es sei denn
ein leerer Prefix wurde konfiguriert. Dann beginnen alle Topics mit der Operation. Dieses Vorgehen wird wegen
möglichen Namenskonflikten nicht empfohlen. Außerdem ist zu beachten, dass ``/`` ein gültiger Präfix ist.

``<OPERATION>`` ist der Typ der Anfrage. Dieser kann ``request``, ``response``, ``register`` oder ``callback`` sein.
Die Bindings subscriben auf ``request``- und ``register``-Topics und publishen Antworten auf ``request``- unter
``response``-Topics, Antworten auf ``register``- unter ``callback``-Topics.

``<DEVICE>`` ist der Typ des Gerätes mit dem interagiert werden soll. Dies kann der Name eines Bricks
oder Bricklets in snake_case, oder ``ip_connection`` sein. Siehe die Dokumentation der Geräte für die
genaue Schreibweise.

``[/<UID>]`` ist die UID des Gerätes. Wenn das Gerät die ``ip_connection`` ist, muss die UID leer und ohne ``/`` sein,
zum Beispiel ``.../ip_connection/enumerate``.

``<FUNCTION>`` ist die Funktion, die aufgerufen, oder das Callback, das registriert werden soll (in snake_case).

``</[SUFFIX]>`` ist der optionale Suffix der an Antworten angehangen wird. Dieser kann verwendet werden, um Nachrichten
zu filtern. Siehe :ref:`hier <mqtt_topic_suffixes>` für Details.

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

Callback-(De)registrierungen können entweder ``{"register": true/false}`` oder ``true/false`` als Payload haben.

Requests und Responses
^^^^^^^^^^^^^^^^^^^^^^

Um eine Funktion eines Bricks oder Bricklets aufzurufen, muss eine Nachricht im JSON-Format im entsprechenden
``request``-Topic gepublisht werden. Um zum Beispiel mit mosquitto_pub die Farbe des RGB LED Button Bricklets mit der UID Enx auf Gelb zu setzen,
kann folgender Befehl verwendet werden::

  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/set_color -m '{"red":255, "green":127, "blue":0}'

Funktionen geben Werte unter ``response``-Topics zurück. Folgendermaßen kann die aktuelle Farbe des selben Bricklets abgefragt werden::

  mosquitto_sub -t tinkerforge/response/rgb_led_button_bricklet/Enx/get_color
  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/get_color -m ''

Auch aufgetretene Fehler werden unter ``response``-Topics gepublisht, zum Beispiel wird, falls ein Parameter fehlt::

  mosquitto_sub -t tinkerforge/response/rgb_led_button_bricklet/Enx/set_color
  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/set_color -m '{"red":255, "blue":0}'

die Nachricht::

  {"_ERROR": "The arguments ['green'] where missing for a call of set_color of device Enx of type rgb_led_button_bricklet."}

auf dem Topic ``tinkerforge/response/rgb_led_button_bricklet/Enx/set_color`` zurückgegeben.
Fehler werden auch auf der Standardausgabe der Bindings ausgegeben.

Callbacks
^^^^^^^^^

Callbacks können auf ``register``-Topics registriert werden::

  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Enx/button_state_changed -m 'true'

und werden auf den entsprechenden ``callback``-Topics ausgelöst::

  mosquitto_sub -t tinkerforge/callback/rgb_led_button_bricklet/Enx/button_state_changed

gibt Nachrichten der Form::

  {"state": 0}
  {"state": 1}

zurück, wenn der Taster gedrückt und losgelassen wird.

Um ein Callback zu deregistrieren, kann als Payload ``false`` statt ``true`` verwendet werden.
Außerdem ist es möglich, stattdessen ``{"register":  true}`` und ``{"register": false}`` zu verwenden.

Die Callback-Konfiguration funktioniert analog zu den anderen Bindings. Wenn ein Callback aktiviert
und/oder konfiguriert werden muss, müssen folgende Schritte durchgeführt werden:

* Subscriben des ``callback``-Topics
* Publishen der Registrierung auf das ``register``-Topic
* Publishen der Konfiguration der Callback-Eigenschaften wie z.B. der Periode
* Publishen der Aktivierung des Callbacks über das ``request``-Topic

Um alle Callbacks der Devices und IP-Connection zu deregistrieren, kann folgendes Topic benutzt werden::

  mosquitto_pub -t tinkerforge/request/bindings/reset_callbacks -m ''

Laden initialer Nachrichten aus einer Datei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um die Konfiguration zu vereinfachen, können Nachrichten, die einmal beim Start der Bindings verarbeitet werden
sollen, aus einer Datei geladen werden. Hierzu wird das Kommandozeilenargument ``--init-file /pfad/zur/datei``
verwendet. Mit dieser Datei können z.B. Callbacks konfiguriert und registriert werden. Das Dateiformat entspricht
einem JSON-Objekt, dessen Attributsnamen MQTT-Topics sind. Die Attributswerte werden als weitere JSON-Objekte, die
dem MQTT-Payload entsprechen, behandelt. Folgendes Beispiel zeigt eine Datei, die das ``all_data``-Callback eines
IMU Brick 2.0 registriert und dessen Periode auf 100ms konfiguriert::

 {
     "tinkerforge/register/imu_v2_brick/XXYYZZ/all_data": {"register": true},
     "tinkerforge/request/imu_v2_brick/XXYYZZ/set_all_data_period": {"period": 100}
 }

Seit Version 2.0.8 kann zwischen Nachrichten, die vor oder nach dem Verbindungsaufbau
zum Brick Daemon, der Wifi oder der Ethernet Extension verarbeitet werden sollen,
unterschieden weden. Das erlaubt es, Callback zu registrieren, bevor eine Verbindung
besteht (zum Beispiel das connected-Callback der IP-Connection). Die Syntax ist wie folgt::

 {
     "pre_connect": {
         "tinkerforge/register/ip_connection/connected": {"register": true},
         "tinkerforge/register/ip_connection/enumerate": {"register": true}
     },
     "post_connect": {
         "tinkerforge/request/ip_connection/enumerate": ""
     }
 }

Diese Datei registriert das connected- und enumerate-Callback vor dem
Verbindungsaufbau und löst sofort danach eine Enumerierung aus.

Init-Dateien, die die alte Syntax ohne pre/post_connect verwenden, werden ausgeführt,
nachdem die Verbindung hergestellt wurde.

Topic-Präfixe
^^^^^^^^^^^^^

Die Bindings können mit dem ``--global-topic-prefix``-Parameter auf einen anderen globalen Präfix konfiguriert werden.
Der Präfix kann beispielsweise verwendet werden, um mehrere Binding-Instanzen die mit dem selben Broker verbunden sind zu trennen.
Der Präfix kann beliebig lang sein, zum Beispiel ``tf/instance/1/foo/bar``.

.. _mqtt_topic_suffixes:

Topic-Suffixe
^^^^^^^^^^^^^

Die Bindings unterstützen beliebige Suffixe pro Topic. Mit diesen können zum Beispiel alle Bricks/Bricklets
in einem Raum mit einer Raumnummer markiert werden::

  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Enx/button_state_changed/room/1 -m 'true'
  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/gBs/button_state_changed/room/2 -m 'true'
  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Dod/button_state_changed/room/1 -m 'true'

Um alle Callbacks von Bricks/Bricklets in Raum 1 zu empfangen, kann auf folgendes Topic subscribt werden::

  mosquitto_sub -t tinkerforge/callback/+/+/+/room/1

Es werden dann Callback-Nachrichten von ``Enx`` und ``Dod`` empfangen, aber nicht von ``gBs``.

Um alle Nachrichten zu erhalten kann sich auf::

  mosquitto_sub -t tinkerforge/callback/#
  mosquitto_sub -t tinkerforge/response/#

subscribt werden.

Start und Stop der Bindings
---------------------------

Die Bindings publishen beim Start, direkt nachdem sie zum MQTT-Broker verbunden sind, eine Nachricht auf ``tinkerforge/callback/bindings/restart`` mit ``null``
als Payload. Diese Nachricht kann als Neustart-Signal verwendet werden. Es müssen dann alle verwendeten Callbacks neugestartet werden.

Wenn die Bindungs normal beendet werden, publishen sie eine ``null``-Nachticht auf
``tinkerforge/callback/bindings/shutdown``, bevor die Verbindung zum MQTT-Broker
geschlossen wird.

Falls die Verbindung zum Broker unerwartet abbricht, wird durch den
Last-Will-Mechanismus von MQTT eine ``null``-Nachricht auf
``tinkerforge/callback/bindings/last_will`` gepublisht.

Diese Nachrichten werden gesendet, bevor die Verbindung zum Brick Daemon, der
WIFI- oder Ethernet-Extension besteht, beziehungsweise nachdem diese geschlossen
wurde. Falls auf Änderungen des Zustands dieser Verbindung reagiert werden soll,
können stattdessen die Callbacks der :ref:`IP-Connection <ip_connection_mqtt>`
verwendet werden.

Kommandozeilenargumente
-----------------------

* ``-h``, ``--help`` Listet die Kommandozeilenargumente auf
* ``-v``, ``--version`` Zeigt die Version an
* ``--cmdline-file <CMDLINE_FILE>`` Lädt Kommandozeilenargumente aus einer Datei
* ``--ipcon-host <IPCON_HOST>`` Hostname oder IP-Addresse des Brick Daemons, der WIFI- oder Ethernet-Extension (Standard: localhost)
* ``--ipcon-port <IPCON_PORT>`` Port des Brick Daemons, der WIFI- oder Ethernet-Extension (Standard: 4223)
* ``--ipcon-auth-secret <IPCON_AUTH_SECRET>`` Authentisierungsgeheimnis des Brick Daemons, der WIFI- oder Ethernet-Extension
* ``--ipcon-timeout <IPCON_TIMEOUT>`` Timeout in Millisekunden für Kommunikation mit dem Brick Daemons, der WIFI- oder Ethernet-Extension (Standard: 2500)
* ``--broker-host <BROKER_HOST>`` Hostname oder IP-Addresse des MQTT-Brokers (Standard: localhost)
* ``--broker-port <BROKER_PORT>`` Port des MQTT-Brokers (Standard: 1883)
* ``--broker-username <BROKER_USERNAME>`` Benutzername für die Verbindung zum MQTT-Broker
* ``--broker-password <BROKER_PASSWORD>`` Passwort für die Verbindung zum MQTT-Broker
* ``--broker-certificate <BROKER_CERTIFICATE>`` CA-Zertifikat für SSL/TLS-Verbindung zum Broker
* ``--broker-tls-secure`` Verifikation des Hostnames und Zertifikates für die Verbindung zum MQTT-Broker (standardmäßig aktiv)
* ``--broker-tls-insecure`` Deaktiviert Verifikation des Hostnames und Zertifikates für die Verbindung zum MQTT-Broker
* ``--global-topic-prefix <GLOBAL_TOPIC_PREFIX>`` Globaler Präfix für MQTT-Topics (Standard: tinkerforge/)
* ``--debug`` Zeigt die Debug-Ausgabe
* ``--no-debug`` Versteckt die Debug-Ausgabe (standardmäßig aktiv)
* ``--symbolic-response`` Übersetzung von Antwort-Konstanten in Strings (standardmäßig aktiv)
* ``--no-symbolic-response`` Keine Übersetzung von Antwort-Konstanten in Strings
* ``--int64-string-response`` Übersetzung von Antwort-[u]int64-Werten in Strings
* ``--no-int64-string-response`` ÜKeine bersetzung von Antwort-[u]int64-Werten in Strings (standardmäßig aktiv)
* ``--show-payload`` Empfangenen Payloads anzeigen falls das JSON-Parsing fehlschlägt
* ``--hide-payload`` Empfangenen Payloads nicht anzeigen falls das JSON-Parsing fehlschlägt (standardmäßig aktiv)
* ``--init-file <INIT_FILE>`` Lädt Nachrichten, die initial verarbeitet werden sollen, aus einer Datei
* ``--no-init-file`` Keine Nachrichten werden initial verarbeitet (standardmäßig aktiv)

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
