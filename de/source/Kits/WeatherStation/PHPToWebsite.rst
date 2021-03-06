
.. _starter_kit_weather_station_website_php:

Mit PHP Messwerte live auf einer Webseite anzeigen
==================================================

.. include:: PHPCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Ziele
-----

Wir setzen die folgenden Ziele für dieses Projekt:

Die Wetterdaten sollen

* auf einer Webseite angezeigt werden,
* alle 5 Sekunden über AJAX aktualisiert werden und
* per kleinem PHP Skript verfügbar gemacht werden.

Nachfolgend werden wir Schritt-für-Schritt zeigen wie dieses Ziel erreicht 
werden kann.


Schritt 1: HTML und JavaScript
------------------------------

Da diese Projekt sich nicht darum dreht eine Webseite zu designen, werden wir 
eine einfache HTML Seite verwenden:

.. code-block:: html

    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Tinkerforge Weather Station</title>
      </head>
      <body>
        <p id="illuminance">TBD</p>
        <p id="humidity">TBD</p>
        <p id="air_pressure">TBD</p>
        <p id="temperature">TBD</p>
      </body>
    </html>

Der innere Text der vier Zeilen wird vom JavaScript durch die Daten vom PHP 
Script mittels AJAX ersetzt:

.. code-block:: html

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
    <script type="text/javascript">
      function updateMeasurements(){
        $.ajax({
          url: "WeatherStationWebsite.php",
          type: "POST",
          success: function(data) {
            var response = $.parseJSON(data);
            document.getElementById('illuminance').innerHTML = response.illuminance;
            document.getElementById('humidity').innerHTML = response.humidity;
            document.getElementById('air_pressure').innerHTML = response.air_pressure;
            document.getElementById('temperature').innerHTML = response.temperature;
          }
        });
      }

      updateMeasurements();
      setInterval(updateMeasurements, 5000);
    </script>

Wir nutzen jQuery um dies so einfach und lesbar wie möglich zu halten.
Die Funktion ``updateMeasurements`` ruft ``WeatherStationWebsite.php`` auf und
erwartet es ``illuminance``, ``humidity``, ``air_pressure`` und
``temperature`` im JSON Format zu erhalten.

Um die Messwerte direct nach dem Öffnen der Webseite angezeigt zu bekommen
wird ``updateMeasurements`` einmal direkt aufgerufen. Anschließend wird es
mit einem 5000ms (5s) Intervall aufgerufen, das zuvor per
``setInterval(updateMeasurements, 5000)`` konfiguriert wurde.


Schritt 2: PHP
--------------

Das PHP Skript selbst ist sehr einfach, es müssen nur die Bricklets 
initialisiert werden:

.. code-block:: php

    <?php

    require_once('Tinkerforge/IPConnection.php');
    require_once('Tinkerforge/BrickletAmbientLight.php');
    require_once('Tinkerforge/BrickletHumidity.php');
    require_once('Tinkerforge/BrickletBarometer.php');

    use Tinkerforge\IPConnection;
    use Tinkerforge\BrickletAmbientLight;
    use Tinkerforge\BrickletHumidity;
    use Tinkerforge\BrickletBarometer;

    $ipcon = new IPConnection();
    $brickletAmbientLight = new BrickletAmbientLight("apy", $ipcon);
    $brickletHumidity = new BrickletHumidity("7bA", $ipcon);
    $brickletBarometer = new BrickletBarometer("d99", $ipcon);

    $ipcon->connect("localhost", 4223);

    ?>


Hier müssen die UIDs (``apy``, ``7bA`` und ``d99``) durch die UIDs von den eigenen
Bricklets ersetzt werden.


Danach müssen die Werte abgerufen werden und in einem Array gespeichert werden.

.. code-block:: php

    <?php

    $illuminance = $brickletAmbientLight->getIlluminance()/10.0;
    $humidity = $brickletHumidity->getHumidity()/10.0;
    $air_pressure = $brickletBarometer->getAirPressure()/1000.0;
    $temperature = $brickletBarometer->getChipTemperature()/100.0;

    $response = array (
        "illuminance"  => "Illuminance: $illuminance Lux",
        "humidity"     => "Humidity: $humidity %RH",
        "air_pressure" => "Air Pressure: $air_pressure hPa",
        "temperature"  => "Temperature: $temperature &deg;C",
    );

    ?>


Zum Schluss muss nur noch die Antwort im JSON Format ausgegeben werden:

.. code-block:: php

    <?php

    print_r(json_encode($response));

    ?>


Schritt 3: Alles zusammenfügen
------------------------------

Das war's! Zum Schluss muss nur noch die HTML und PHP Datei in ein 
Verzeichnis gelegt werden, das von einem Webserver wie Apache bedient wird.

Wenn es hierbei Probleme gibt lohnt sich ein Blick in die
`PHP Installationsanleitung <https://php.net/manual/de/install.php>`__.

Wir haben dies auf einem Ubuntu Rechner getestet. Hier konnten wir
PHP und Apache einfach per apt-get installieren::

    apt-get install apache2 php5

und beide Dateien unter ``/var/www/`` speichern.

.. image:: /Images/Kits/weather_station_website_orig.jpg
   :scale: 100 %
   :alt: Messwerte live auf einer Webseite anzeigen
   :align: center
   :target: ../../_images/Kits/weather_station_website_orig.jpg

``weather.html`` (`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/website/php/weather.html>`__):

.. literalinclude:: ../../../../../weather-station/website/php/weather.html
 :language: html
 :tab-width: 4

``WeatherStationWebsite.php`` (`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/website/php/WeatherStationWebsite.php>`__):

.. literalinclude:: ../../../../../weather-station/website/php/WeatherStationWebsite.php
 :language: php
 :tab-width: 4
