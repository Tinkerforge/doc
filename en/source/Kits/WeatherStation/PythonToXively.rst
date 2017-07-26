
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#starter-kits">Starter Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using Python to upload weather data to Xively

.. _starter_kit_weather_station_python_to_xively:

Using Python to upload weather data to Xively
=============================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

We are setting the following goals for this project:

* The weather data should be gathered and shown on the LCD 20x4
  Bricklet, as in the :ref:`Using Python to write to LCD 20x4 Bricklet project
  <starter_kit_weather_station_python_to_lcd>`.
* The measurements should additionally be stored and uploaded to Xively in
  5 minute intervals.

In the following we will show step-by-step how this can be achieved.

Step 1: Create and configure Xively account
-------------------------------------------

To use Xively, we first have to create a Xively account.
Go to `xively.com <https://www.xively.com>`__ and sign up.

Click on "+ Device" and add a description of your device.
Next add a new channel ("+ Add Channel").
For every sensor value we have to add a new channel:

.. image:: /Images/Kits/weather_station_xively_datastreams_600.jpg
   :scale: 100 %
   :alt: Xively datastream configuration
   :align: center
   :target: ../../_images/Kits/weather_station_xively_datastreams_orig.jpg

The channels got the IDs AirPressure, AmbientLight, Humidity and Temperature.
Later we will need these IDs to upload measurements.

Step 2: Understanding Xively protocol
-------------------------------------

A quick search in the Xively API documentation reveals that we can update
a datastream by `just sending a small JSON package
<https://personal.xively.com/dev/docs/api/communicating/>`__.

The given example is::

 {
  "current_value":"294",
  "max_value":"697.0",
  "min_value":"0.0",
  "id":"1"
 }

which can be send via HTTP PUT to ``http://api.xively.com/v2/feeds/<ID>``. The
API key is put in the header of the HTTP request and the return consists of
an HTTP header only.

This seems quite straight forward. To not spam Xively, we should limit the uploading
interval to once every 5 minutes. This means, that we need to store the
measurements and determine the corresponding
min and max values for each interval.

Step 3: Storing measurements
----------------------------

To start off, we create a simple value storage. To identify the
values, we use the ID that was configured in the Xively account as
the Datastream ID:

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

This has to be added for the other measurements accordingly.

Step 4: Uploading measurements
------------------------------

To upload our measurements we first have to define all of the names, URLs,
keys and so on:

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

You have to exchange the ``FEED`` and ``API_KEY`` values by your own Xively
feed and key. Everything else is practically copied from the
Xively documentation.

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
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/xively/python/weather_xively.py>`__),
you have a working Weather Station that uploads the weather measurements to Xively:

.. literalinclude:: ../../../../../weather-station/xively/python/weather_xively.py
 :language: python
 :tab-width: 4
