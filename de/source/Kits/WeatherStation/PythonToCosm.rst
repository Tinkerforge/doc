
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Python Wetterdaten auf Cosm hochladen

.. _starter_kit_weather_station_cosm:

Mit Python Wetterdaten auf Cosm hochladen
=========================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

Folgende Ziele sind für dieses Projekt gesetzt:

* Die Wetterdaten sollen gesammelt und auf dem LCD 20x4 Bricklet
  angezeigt werden (siehe :ref:`Mit Python auf das LCD 20x4 Bricklet schreiben Projekt
  <starter_kit_weather_station_python_to_lcd>`.
* Zusätzlich sollen die Messungen gespeichert und in 5 Minuten Intervallen 
  nach Cosm hochgeladen werden.

Nachfolgend erklären wir Schritt für Schritt wie diese Ziele erreicht werden können.

Schritt 1: Erstelle und Konfiguriere einen Cosm Account
-------------------------------------------------------

Um Cosm benutzen zu können muss zuerst ein Cosm Account angelegt werden.
Dazu muss `cosm.com <https://cosm.com>`__ besucht werden und sich
eingeloggt werden.

Klicke auf "+ Device/Feed" und wähle "Something Else" als Typ.
Wähle "push data to Cosm", einen Titel und Tags und erzeuge einen Feed.

In diesem Feed müssen Data Streams für unsere Wetterdaten hinzugefügt werden:

.. image:: /Images/Kits/weather_station_cosm_datastreams_600.jpg
   :scale: 100 %
   :alt: Cosm Datastream Konfiguration
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_datastreams_orig.jpg

Die Streams bekommen die IDs AirPressure, AmbientLight, Humidity und 
Temperature. Diese IDs werden wir später nutzen um die Messwerte hochzuladen.


Schritt 2: Das Cosm Protokoll verstehen
---------------------------------------

Eine kurze Recherche in der Cosm API Dokumentation zeigt, dass
ein Datastream über `JSON Pakete
<https://cosm.com/docs/v2/datastream/update.html>`__
aktualisiert werden können.

Das angegebene Beispiel::

 {
  "current_value":"294",
  "max_value":"697.0",
  "min_value":"0.0",
  "id":"1"
 }

wird über HTTP PUT zu ``http://api.cosm.com/v2/feeds/<ID>`` gesendet. 
Der API Key ist im Header des HTTP Requests definiert und die Rückgabe besteht 
aus dem HTTP Header.

Um Cosm nicht zu spammen sollten wir nur alle 5 Minuten einmal die Werte 
aktualisieren. Daher müssen wir die Messwerte speichern und die dazugehörigen
Werte (min/max) bestimmen.

Schritte 3: Messwerte speichern
-------------------------------

Als erstes erstellen wir eine einfache Datenhaltung, wobei wir die Werte mit
den IDs identifizieren, die wir bei Cosm als Datastream ID hinterlegt haben:

.. code-block:: python

    class Cosm:
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

Wir nutzen den letzten Wert, das alte Minimum und Maximum und berechnen
daraus die neuen Werte. Wenn noch keine Werte zu der ID gespeichert sind,
fangen wir die Exception und legen einen neuen Key an.

Als Basis für den Programmcode der Wetterstation kann das :ref:`Mit Python auf
das LCD 20x4 Bricklet schreiben Projekt <starter_kit_weather_station_python_to_lcd_step_5>`
dienen.

Wir müssen nur noch die put Funktion aufrufen wenn neue Messwerte ankommen:

.. code-block:: python

    class WeatherStation:
        # [...]
        def __init__(self):
            # [...]
            self.cosm = Cosm()
            # [...]

        # [...]
        def cb_illuminance(self, illuminance):
            if self.lcd is not None:
                text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
                self.lcd.write_line(0, 0, text)

                # Here we add illuminance to Cosm with ID "AmbientLight"
                self.cosm.put('AmbientLight', illuminance/10.0)
                log.info('Write to line 0: ' + text)
        # [...]

Dies muss für die anderen Messwerte ebenfalls entsprechend hinzugefügt werden.

Schritt 4: Messwerte hochladen
------------------------------

Um die Messwerte hochzuladen müssen wir zuerst alle Namen, URLs, Keys und so 
weiter definieren:

.. code-block:: python

    class Cosm:
        HOST = 'api.cosm.com'
        AGENT = "Tinkerforge cosm 1.0"
        FEED = '105813.json'
        API_KEY = 'WtXx2m6ItNZyFYoQyr5qnoN1GsOSAKxPMGdIaXRLYzY5ND0g'

        def __init__(self):
            self.items = {}
            self.headers = {
                "Content-Type"  : "application/x-www-form-urlencoded",
                "X-ApiKey"      : Cosm.API_KEY,
                "User-Agent"    : Cosm.AGENT,
            }
            self.params = "/v2/feeds/" + str(Cosm.FEED)
            threading.Thread(target=self.upload).start()

``FEED`` und ``API_KEY`` Werte müssen durch die im eigenen Cosm
Account erstellten Werte ersetzt werden. Der Rest ist praktisch aus
der Cosm API Dokumentation kopiert.

Um alle 5 Minuten die Werte zu Aktualisieren wird die ``update`` Funktion
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

            data = {
              'version' : '1.0.0',
              'datastreams': stream_items,
            }
            self.items = {}
            body = json.dumps(data)

            http = httplib.HTTPSConnection(Cosm.HOST)
            http.request('PUT', self.params, body, self.headers)
            response = http.getresponse()
            http.close()

            if response.status != 200:
                log.error('Could not upload to cosm -> ' +
                          str(response.status) + ': ' + response.reason)

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
Messwerte nach Cosm hochlädt
(`download <https://raw.github.com/Tinkerforge/weather-station/master/cosm/python/weather_cosm.py>`__):

.. literalinclude:: ../../../../../weather-station/cosm/python/weather_cosm.py
 :language: python
 :tab-width: 4
