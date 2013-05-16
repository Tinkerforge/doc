
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Python Wetterdaten auf Xively hochladen

.. _starter_kit_weather_station_python_to_xively:

Mit Python Wetterdaten auf Xively hochladen
===========================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

Folgende Ziele sind für dieses Projekt gesetzt:

* Die Wetterdaten sollen gesammelt und auf dem LCD 20x4 Bricklet
  angezeigt werden (siehe Projekt: :ref:`Mit Python auf das LCD 20x4 Bricklet schreiben
  <starter_kit_weather_station_python_to_lcd>`.
* Zusätzlich sollen die Messungen gespeichert und in 5 Minuten Intervallen 
  nach Xively hochgeladen werden.

Nachfolgend erklären wir Schritt für Schritt wie diese Ziele erreicht werden können.

Schritt 1: Erstelle und Konfiguriere einen Xively Account
---------------------------------------------------------

Um Xively benutzen zu können, muss zuerst ein Xively Account angelegt werden.
Dazu muss `xively.com <https://xively.com>`__ besucht werden und sich
eingeloggt werden.

Klicke auf "+ Device" und gebe eine Beschreibung des Devices ein.
Anschließend lege einen neuen Channel an ("+ Add Channel").
Für jeden Sensorwert muss nun ein neuer Channel angelegt werden:

.. image:: /Images/Kits/weather_station_xively_datastreams_600.jpg
   :scale: 100 %
   :alt: Xively Datastream Konfiguration
   :align: center
   :target: ../../_images/Kits/weather_station_xively_datastreams_orig.jpg

Die Channels bekommen die IDs AirPressure, AmbientLight, Humidity und 
Temperature. Diese IDs werden wir später nutzen um die Messwerte hochzuladen.


Schritt 2: Das Xively Protokoll verstehen
-----------------------------------------

Eine kurze Recherche in der Xively API Dokumentation zeigt, dass
ein Datastream über `JSON Pakete
<https://xively.com/docs/v2/datastream/update.html>`__
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

Als Basis für den Programmcode der Wetterstation kann das Projekt :ref:`Mit Python auf
das LCD 20x4 Bricklet schreiben <starter_kit_weather_station_python_to_lcd_step_5>`
dienen.

Wir müssen nun noch die put Funktion aufrufen wenn neue Messwerte ankommen:

.. code-block:: python

    class WeatherStation:
        # [...]
        def __init__(self):
            # [...]
            self.xively = Xively()
            # [...]

        # [...]
        def cb_illuminance(self, illuminance):
            if self.lcd is not None:
                text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
                self.lcd.write_line(0, 0, text)

                # Here we add illuminance to Xively with ID "AmbientLight"
                self.xively.put('AmbientLight', illuminance/10.0)
                log.info('Write to line 0: ' + text)
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
        FEED = '105813.json'
        API_KEY = 'WtXx2m6ItNZyFYoQyr5qnoN1GsOSAKxPMGdIaXRLYzY5ND0g'

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

Um alle 5 Minuten die Werte zu Aktualisieren, wird die ``update`` Funktion
in einem Thread gestartet:

.. code-block:: python

    def upload(self):
        while True:
            time.sleep(5*60) # Upload data every 5min
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

Wenn wir alles zusammenfügen erhalten wir eine Wetterstation die alle
Messwerte nach Xively hochlädt
(`download <https://raw.github.com/Tinkerforge/weather-station/master/xively/python/weather_xively.py>`__):

.. literalinclude:: ../../../../../weather-station/xively/python/weather_xively.py
 :language: python
 :tab-width: 4
