
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using Python to upload weather data to Cosm

.. _starter_kit_weather_station_cosm:

Using Python to upload weather data to Cosm
===========================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

We are setting the following goals for this project:

* The weather measurements should be calculated and shown on the LCD20x4
  Bricklet, as in the :ref:`Display environment measurements on LCD project
  <starter_kit_weather_station_python_to_lcd>`.
* The measurements should additionally be stored and uploaded to Cosm in
  5 minute intervals.

In the following we will show step-by-step how this can be achieved.

Step 1: Create and configure Cosm account
-----------------------------------------

To use Cosm, we first have to create a Cosm account.
Go to `cosm.com <https://cosm.com>`__ and sign up.

Click on "+ Device/Feed" and as type choose "Something Else".
Choose "push data to Cosm", a title and tags and create the feed.

In the feed we have to add data streams for our weather measurements:

.. image:: /Images/Kits/weather_station_cosm_datastreams_600.jpg
   :scale: 100 %
   :alt: Cosm datastream configuration
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_datastreams_orig.jpg

The streams got the IDs AirPressure, AmbientLight, Humidity and Temperature.
Later we will need these IDs to upload measurements.

Step 2: Understanding Cosm protocol
-----------------------------------

A quick search in the Cosm API documentation reveals that we can update
a datastream by `just sending a small JSON package
<https://cosm.com/docs/v2/datastream/update.html>`__.

The given example is::

 {
  "current_value":"294",
  "max_value":"697.0",
  "min_value":"0.0",
  "id":"1"
 }

which can be send via HTTP PUT to ``http://api.cosm.com/v2/feeds/<ID>``. The
API key is put in the header of the HTTP request and the return consists of
an HTTP header only.

This seems quite straight forward. To not spam Cosm, we should limit the uploading
interval to once every 5 minutes. This means, that we need to store the
measurements and determine the corresponding
min and max values for each interval.

Step 3: Storing measurements
----------------------------

To start off, we create a simple value storage. To identify the
values, we use the ID that was configured in the Cosm account as
the Datastream ID:

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

We retrieve the old value, min_value and max_value, calculate the new
min/max and update it. If there aren't any values stored for a given
identifier, we catch the occurring exception and add the identifier
as a new key to the dict.

The Weather Station code itself we can base on the code from the
:ref:`Display environment measurements on LCD project <starter_kit_weather_station_python_to_lcd_step_5>`

We just have to use the put function whenever a new measurement arrives:

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
                text = 'Illuminanc %s lx' % self.fmt(illuminance/10.0, 3)
                self.lcd.write_line(0, 0, text)

                # Here we add illuminance to Cosm with ID "AmbientLight"
                self.cosm.put('AmbientLight', illuminance/10.0)
                log.info('Write to line 0: ' + text)
        # [...]

This has to be added for the other measurements accordingly.

Step 4: Uploading measurements
------------------------------

To upload our measurements we first have to define all of the names, URLs,
keys and so on:

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

You have to exchange the ``FEED`` and ``API_KEY`` values by your own Cosm
feed and key. Everything else is practically copied from the
Cosm documentation.

To make uploads in equidistant 5 minute intervals, we are starting the
upload function in a thread:

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

Here we take the data that was gathered, package it in the JSON format and
send a HTTP PUT request with the data and the header that was defined in
``__init__``. We also parse the response code and log it if something went wrong.

Step 5: Everything put together
-------------------------------

We are done! There is of course still room for improvement. For example the
uploading and adding of data could be protected by a mutex to ensure that we
don't add data while it is uploaded and thus remove the newly added data
after the uploading finished.

But if you put everything of the above together
(`download <https://raw.github.com/Tinkerforge/weather-station/master/cosm/python/weather_cosm.py>`__),
you have a working Weather Station that uploads the weather measurements to Cosm:

.. literalinclude:: ../../../../../weather-station/cosm/python/weather_cosm.py
 :language: python
 :tab-width: 4
