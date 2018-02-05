
.. _starter_kit_server_room_monitoring_upload_sensor_data_to_xively:

Sensordaten nach Xively hochladen
=================================

Bei `Xively <https://www.xively.com/>`__ handelt es sich um einen Dienst, der die
Möglichkeit bietet das "Internet der Dinge" zu analysieren und zu visualisieren.
Der Dienst kann dazu genutzt werden verschiedene Geräte über das Internet
miteinander zu verbinden. Er kann eine Historie von Messwerten speichern und
visualisieren.

Dieses Beispiel basiert hauptsächlich auf dem 
:ref:`Mit Python Wetterdaten auf Xively hochladen <starter_kit_weather_station_python_to_xively>` 
Beispiel.

.. include:: ../WeatherStation/PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Ziele
-----

In diesem Projekt sollten die Temperatur und die Helligkeit gemessen werden
und an Xively in 1 Minuten Intervallen übertragen werden. Nachfolgend erklärt
eine Schritt für Schritt Anleitung wie dies funktioniert.


Schritt 1: Erstelle und Konfiguriere einen Xively Account
---------------------------------------------------------

Um Xively benutzen zu können, muss zuerst ein Xively Account angelegt werden.
Dazu muss `xively.com <https://www.xively.com>`__ besucht werden und sich
eingeloggt werden.

Klicke auf "+ Device" und gebe eine Beschreibung des Devices ein.
Anschließend lege einen neuen Channel an ("+ Add Channel").
Für jeden Sensorwert muss nun ein neuer Channel angelegt werden:

.. image:: /Images/Kits/server_room_monitoring_xively_600.jpg
   :scale: 100 %
   :alt: Xively Datastream Konfiguration
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_xively_orig.jpg

Die Channels bekommen die IDs AmbientLight und Temperature.
Diese IDs werden wir später nutzen um die Messwerte hochzuladen.

Schritt 2: Das Xively Protokoll verstehen
-----------------------------------------

Eine kurze Recherche in der Xively API Dokumentation zeigt, dass
ein Datastream über `JSON Pakete
<https://personal.xively.com/dev/docs/api/communicating/>`__
aktualisiert werden können.

Das dort angegebene Beispiel::

 {
  "current_value":"294",
  "max_value":"697.0",
  "min_value":"0.0",
  "id":"1"
 }

wird über HTTP PUT zu ``http://api.xively.com/v2/feeds/<ID>`` gesendet. 
Der API Key ist im Header des HTTP Requests definiert und die Rückgabe besteht 
aus dem HTTP Header.

Um Xively nicht zu spammen sollten wir nur einmal alle 5 Minuten die Werte 
aktualisieren. Daher müssen wir die Messwerte speichern und die dazugehörigen
Werte (min/max) bestimmen.

Schritte 3: Messwerte speichern
-------------------------------

Als erstes erstellen wir eine einfache Datenhaltung. Die Werte werden wir mit
den IDs identifizieren, die wir bei Xively als Datastream ID hinterlegt haben:

.. code-block:: python

    class Xively:
        def __init__(self):
            self.items = {}

        def put(self, identifier, value):
            try:
                _, min_value, max_value = self.items[identifier]
                if value < min_value:
                    min_value = value
                if value > max_value:
                    max_value = value
                self.items[identifier] = (value, min_value, max_value)
            except:
                self.items[identifier] = (value, value, value)

Wir nutzen den letzten Wert, sowie das alte Minimum und Maximum und berechnen
daraus die neuen Werte. Wenn noch keine Werte zu der ID gespeichert sind,
fangen wir die Exception und legen einen neuen Key an.

Wir müssen nun noch die put Funktion aufrufen wenn neue Messwerte ankommen:

.. code-block:: python

    class ServerRoomMonitoring:
        # [...]
        def __init__(self):
            # [...]
            self.xively = Xively()
            # [...]

        # [...]
        def cb_illuminance(self, illuminance):
            # Here we add illuminance to Xively with ID "AmbientLight"
            self.xively.put('AmbientLight', illuminance/10.0)
            log.info('Ambient Light ' + str(illuminance/10.0))
        # [...]

Für alle anderen Messwerte muss dies ebenfalls entsprechend hinzugefügt werden.


Schritt 4: Messwerte hochladen
------------------------------

Um die Messwerte hochzuladen müssen wir zuerst alle Namen, URLs, Keys etc. 
definieren:

.. code-block:: python

    class Xively:
        HOST = 'api.xively.com'
        AGENT = "Tinkerforge xively 1.0"
        FEED = '196340443.json'
        API_KEY = 'SGpMEW3ZZ6yJVd9jZlaPgex06v1W00lA2UZkv5rgskwlVkr6'

        def __init__(self):
            self.items = {}
            self.headers = {
                "Content-Type"  : "application/x-www-form-urlencoded",
                "X-ApiKey"      : Xively.API_KEY,
                "User-Agent"    : Xively.AGENT,
            }
            self.params = "/v2/feeds/" + str(Xively.FEED)
            threading.Thread(target=self.upload).start()

Die Werte von ``FEED`` und ``API_KEY`` müssen durch die im eigenen Xively
Account erstellten Werte ersetzt werden. Der Rest ist praktisch aus
der Xively API Dokumentation kopiert.

Um alle 1 Minuten die Werte zu Aktualisieren, wird die ``update`` Funktion
in einem Thread gestartet:

.. code-block:: python

    def upload(self):
        while True:
            time.sleep(60) # Upload data every minute
            if len(self.items) == 0:
                continue

            stream_items = []
            for identifier, value in self.items.items():
                stream_items.append({'id': identifier,
                                     'current_value': value[0],
                                     'min_value': value[1],
                                     'max_value': value[2]})

            data = {'version' : '1.0.0',
                    'datastreams': stream_items}
            self.items = {}
            body = json.dumps(data)

            try:
                http = httplib.HTTPSConnection(Xively.HOST)
                http.request('PUT', self.params, body, self.headers)
                response = http.getresponse()
                http.close()

                if response.status != 200:
                    log.error('Could not upload to xively -> ' +
                              str(response.status) + ': ' + response.reason)
            except Exception as e:
                log.error('HTTP error: ' + str(e))

Diese nimmt die gesammelten Daten, verpackt sie im JSON Format und sendet 
diese per HTTP PUT Request mit Daten und Header die im 
``__init__`` definiert wurden. Zusätzlich parsen wir die Antwort
und loggen wenn etwas schief gegangen ist.

Schritt 5: Alles zusammenfügen
------------------------------

Das war's! Natürlich gibt es auch hierbei wieder einige Möglichkeiten der
Verbesserung. So kann z.B. das Aktualisieren und Hinzufügen der Daten mit 
einem Mutex geschützt werden, so dass sichergestellt wird, dass keine Daten 
hinzugefügt werden während andere hochgeladen werden.

Wenn wir alles zusammenfügen erhalten wir eine Serverraum-Überwachung die
die Messwerte nach Xively hochlädt:

(`download <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/xively/server_room_monitoring.py>`__)

.. literalinclude:: ../../../../../server-room-monitoring/xively/server_room_monitoring.py
 :language: python
 :tab-width: 4
