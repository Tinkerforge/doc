
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit PHP Messwerte live auf einer Webseite anzeigen

.. _starter_kit_weather_station_website:

Mit PHP Messwerte live auf einer Webseite anzeigen
==================================================

.. include:: PHPCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

We are setting the following goals for this project:

The weather measurements should be

* shown on a website,
* updated every 5 seconds over AJAX and
* provided by a small PHP script.

In the following we will show step-by-step how this can be achieved.


Step 1: HTML and JavaScript
---------------------------

Since this project is not about designing an actual website, we will
leave the HTML as plain as possible:

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

The inner text of the four paragraphs will be replaced by JavaScript with
data that is provided by a PHP script over AJAX:

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

We use jQuery to keep it as simple and readable as possible.
The function ``updateMeasurements`` calls ``WeatherStationWebsite.php`` and
expects to get ``illuminance``, ``humidity``, ``air_pressure`` and
``temperature`` as a return in the JSON format.

To show the measurements directly upon opening the website,
``updateMeasurements`` is called once directly. After that it is called with
an interval of 5000ms (5s), configured with
``setInterval(updateMeasurements, 5000)``.


Step 2: PHP
-----------

The PHP script itself is quite simple, we just need to initialize the
Bricklets:

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

Then get the values and package them in a response array:

.. code-block:: php

    <?php

    $illuminance = $brickletAmbientLight->getIlluminance()/10.0;
    $humidity = $brickletHumidity->getHumidity()/10.0;
    $air_pressure = $brickletBarometer->getAirPressure()/1000.0;
    $temperature = $brickletBarometer->getChipTemperature()/100.0;

    $response = array (
        "illuminance"  => "Illuminance: $illuminance Lux",
        "humidity"     => "Humidity: $humidity %RH",
        "air_pressure" => "Air Pressure: $air_pressure mbar",
        "temperature"  => "Temperature: $temperature °C",
    );

    ?>

Here you have to change the UIDs ("apy", "7bA" and "d99") by the UIDs
of your own Bricklets.

Lastly, we print the response in JSON format:

.. code-block:: php

    <?php

    print_r(json_encode($response));

    ?>


Step 3: Everything put together
-------------------------------

That's it! Now we have to put the HTML and the PHP file in a directory
that is served by a webserver, such as Apache.

If you haven't done anything like this, you should take a look at the
`PHP installation guide <http://php.net/manual/en/install.php>`__.

This was tested on a Ubuntu machine, so we have simply installed PHP
and apache via apt-get::

    apt-get install apache2 php5

and put both of the files in ``/var/www/``.

.. image:: /Images/Kits/weather_station_website_orig.jpg
   :scale: 100 %
   :alt: Live Measurements on Website
   :align: center
   :target: ../../_images/Kits/weather_station_website_orig.jpg

``weather.html`` (`download <https://raw.github.com/Tinkerforge/weather-station/master/website/php/weather.html>`__):

.. literalinclude:: ../../../../../weather-station/website/php/weather.html
 :language: html
 :tab-width: 4

``WeatherStationWebsite.php`` (`download <https://raw.github.com/Tinkerforge/weather-station/master/website/php/WeatherStationWebsite.php>`__):

.. literalinclude:: ../../../../../weather-station/website/php/WeatherStationWebsite.php
 :language: php
 :tab-width: 4
