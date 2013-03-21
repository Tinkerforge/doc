
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using C# to Control the Buttons for Statistics

.. _starter_kit_weather_station_button_control:

Using C# to Control the Buttons for Statistics
==============================================

For this project we are assuming, that you have a C# environment set up 
and that you have a rudimentary understanding of the C# language.

If you are totally new to either C# itself or to C# in the context of 
Tinkerforge, you should start :ref:`here <TODO>`.

Goals
-----

We are setting the following goals for this project:

The buttons should switch between

* standard weather measurement,
* 24h min/max/average,
* 24h graph and
* Time and date.

Additionally we will fulfill all of the goals that were present in the
:ref:`Display environment measurements on LCD project <starter_kit_weather_station_csharp_to_lcd>`. 

In the following we will show step-by-step how this can be achieved. This time
we will not go through each line of the code, since this would take too long.
But we will describe the general concept, so the program can be easily
understood.

Step 1: Retrieving data
-----------------------

The structure of the program is exactly the same as in the 
:ref:`Display environment measurements on LCD project <starter_kit_weather_station_csharp_to_lcd>`.

We get the data over callbacks with a 1s interval. But this time we just
save the measurements:

.. code-block:: csharp

    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        latestIlluminance = illuminance/10.0;
    }

    static void HumidityCB(BrickletHumidity sender, int humidity)
    {
        latestHumidity = humidity/10.0;
    }

    static void AirPressureCB(BrickletBarometer sender, int airPressure)
    {
        latestAirPressure = airPressure/1000.0;

        int temperature = sender.GetChipTemperature();
        latestTemperature = temperature/100.0;
    }

To use the latest measurements we start a 1s timer

.. code-block:: csharp

    Timer timer = new Timer(Update, null, TimeSpan.Zero, TimeSpan.FromSeconds(1));

and put the measurements in a queue so we can later analyze them:

.. code-block:: csharp

    static private void Update(object state)
    {
        // The measurements are initialized with NaN
        if(Double.IsNaN(latestIlluminance) ||
           Double.IsNaN(latestHumidity) ||
           Double.IsNaN(latestAirPressure) ||
           Double.IsNaN(latestTemperature))
        {
            return;
        }

        illuminanceQueue.Enqueue(latestIlluminance);
        if(illuminanceQueue.Count > 60*60*24) // Save max one day worth of measurements
        {
            illuminanceQueue.Dequeue();
        }

        humidityQueue.Enqueue(latestHumidity);
        if(humidityQueue.Count > 60*60*24)
        {
            humidityQueue.Dequeue();
        }

        airPressureQueue.Enqueue(latestAirPressure);
        if(airPressureQueue.Count > 60*60*24)
        {
            airPressureQueue.Dequeue();
        }

        temperatureQueue.Enqueue(latestTemperature);
        if(temperatureQueue.Count > 60*60*24)
        {
            temperatureQueue.Dequeue();
        }

        UpdateSwitch();
    }

At a first glance this approach seems convoluted, why can't we
just call the Getter methods in the Update function or put the measurements
in the queue during the callbacks?

There are two reasons why the utilized approach makes sense:

1. The callbacks only get called in 1s intervals if the actual callback
   value changed. That means, if a measurement doesn't change for 10s, the
   callback will only be triggered after this 10s. This is good since it
   saves bandwidth, but we want to have a measurement every second, so we
   can use the data for statistics.
2. By using callbacks with a 1s interval and a separate timer with a 1s
   interval, we can easily overcome short connection losses or similar.
   For example: If the Weather Station is controlled over Wi-Fi and the
   Wi-Fi connection is lost for 30s, we will just use the latest value that
   was retrieved for these 30s. If we would be using Getters for this, we would
   have to handle a timeout for each of the measurements. Since the standard
   timeout time of 2.5s is longer then our 1s interval, a timeout would
   actually distort the measurements.


Step 2: Button Control
----------------------

For the button control, we have to add the ButtonPressed callback
during the initialization:

.. code-block:: csharp

    brickletLCD.ButtonPressed += PressedCB;

In the callback we save the actual button that was pressed and
we also increase a counter for the specific button, if the
same button was pressed before. This allows us to cycle between
different views in a specific mode.

.. code-block:: csharp

    private static byte buttonPressed = 0;
    private static int[] buttonPressedCounter = {0, 0, 0, 0};

    // [...]

    static void PressedCB(BrickletLCD20x4 sender, byte button)
    {
        if(button == buttonPressed)
        {
            buttonPressedCounter[button]++;
        }
        else
        {
            buttonPressed = button;
        }

        brickletLCD.ClearDisplay();
        UpdateSwitch();
    }

To give instant feedback, we directly clear the display and call
UpdateSwitch.

The UpdateSwitch method switches between the four different modes:

.. code-block:: csharp

    static private void UpdateSwitch()
    {
        switch(buttonPressed)
        {
            case UPDATE_TYPE_STANDARD: UpdateStandard(); break;
            case UPDATE_TYPE_GRAPH: UpdateGraph(); break;
            case UPDATE_TYPE_MIN_MAX_AVG: UpdateMinMaxAvg(); break;
            case UPDATE_TYPE_TIME: UpdateTime(); break;
        }
    }

The four modes are:

* Standard: Displays all 4 measurements.
* Graph: Displays a 24h graph of one measurement. It is possible to cycle
  through the different measurements with repeated presses of the button.
* MinMaxAvg: Displays the minimum, maximum and average values of a measurement.
  It is also possible to cycle through the different measurements with repeated
  presses of the button.
* Time: Displays current time and date.

Step 3: Show four modes on display
----------------------------------

The implementation of the four modes.

Standard Mode
^^^^^^^^^^^^^

In standard mode we just show the measurements:

.. code-block:: csharp

    static private void UpdateStandard()
    {
        string text = string.Format("Illuminanc {0,6:###.00} lx", latestIlluminance);
        brickletLCD.WriteLine(0, 0, text);

        text = string.Format("Humidity   {0,6:###.00} %", latestHumidity);
        brickletLCD.WriteLine(1, 0, text);

        text = string.Format("Air Press {0,7:####.00} mb", latestAirPressure);
        brickletLCD.WriteLine(2, 0, text);

        text = string.Format("Temperature {0,2:##.00} {1}C", latestTemperature, (char)0xDF);
        brickletLCD.WriteLine(3, 0, text);
    }

.. image:: /Images/Kits/weather_station_lcd_standard_350.jpg
   :scale: 100 %
   :alt: Standard Mode
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_standard_1000.jpg

Graph Mode
^^^^^^^^^^

In graph mode we show a bar graph of the last 24 hours:

.. code-block:: csharp

    static private void UpdateGraph()
    {
        double barSumMin;
        double barSumMax;

        switch(buttonPressedCounter[1] % 4)
        {
            case MODE_ILLUMINANCE:
                UpdateGraphWriteBars(illuminanceQueue, out barSumMin, out barSumMax);
                UpdateGraphWriteTitle("I: ", barSumMin, barSumMax, illuminanceQueue.Count);
                break;

            case MODE_HUMIDITY:
                UpdateGraphWriteBars(humidityQueue, out barSumMin, out barSumMax);
                UpdateGraphWriteTitle("H: ", barSumMin, barSumMax, humidityQueue.Count);
                break;

            case MODE_AIR_PRESSURE:
                UpdateGraphWriteBars(airPressureQueue, out barSumMin, out barSumMax);
                UpdateGraphWriteTitle("A: ", barSumMin, barSumMax, airPressureQueue.Count);
                break;

            case MODE_TEMPERATURE:
                UpdateGraphWriteBars(temperatureQueue, out barSumMin, out barSumMax);
                UpdateGraphWriteTitle("T: ", barSumMin, barSumMax, temperatureQueue.Count);
                break;
        }
    }

We don't go into detail here. The exact method how the bars are calculated
can be seen in the final program. For the bar graph we have to configure
some custom characters during the initialization:

.. code-block:: csharp

    static private void ConfigureCustomChars(BrickletLCD20x4 lcd)
    {
        byte[][] c = new byte[8][];
        c[0] = new byte[8] {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff};
        c[1] = new byte[8] {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff};
        c[2] = new byte[8] {0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff};
        c[3] = new byte[8] {0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff};
        c[4] = new byte[8] {0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff};
        c[5] = new byte[8] {0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
        c[6] = new byte[8] {0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
        c[7] = new byte[8] {0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};

        for(byte i = 0; i < c.Length; i++)
        {
            lcd.SetCustomCharacter(i, c[i]);
        }
    }

This configures the eight available custom characters to bars with height
one to eight.

.. image:: /Images/Kits/weather_station_lcd_graph_350.jpg
   :scale: 100 %
   :alt: Graph Mode
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_graph_1000.jpg

MinMaxAvg Mode
^^^^^^^^^^^^^^

In MinMaxAvg mode we show minimum, maximum and average values of the last 24 hours:

.. code-block:: csharp

    static private void UpdateMinMaxAvg()
    {
        switch(buttonPressedCounter[2] % 4)
        {
            case MODE_ILLUMINANCE:
                UpdateMinMaxAvgWrite("Illuminance    " + TimeFromSeconds(illuminanceQueue.Count),
                                     "Lux",
                                     GetMinMaxAvg(illuminanceQueue));
                break;

            case MODE_HUMIDITY:
                UpdateMinMaxAvgWrite("Humidity       " + TimeFromSeconds(humidityQueue.Count),
                                     "%RH",
                                     GetMinMaxAvg(humidityQueue));
                break;

            case MODE_AIR_PRESSURE:
                UpdateMinMaxAvgWrite("Air Pressure   " + TimeFromSeconds(airPressureQueue.Count),
                                     "mbar",
                                     GetMinMaxAvg(airPressureQueue));
                break;

            case MODE_TEMPERATURE:
                UpdateMinMaxAvgWrite("Temperature    " + TimeFromSeconds(temperatureQueue.Count),
                                     ((char)0xDF) + "C",
                                     GetMinMaxAvg(temperatureQueue));
                break;
        }
    }

The values are written in 4 lines, whereby the first line is a title that
shows the names of the measurements:

.. code-block:: csharp

    static private void UpdateMinMaxAvgWrite(string title, string unit, double[] values)
    {
        String min = string.Format("Min: {0,2:##.00} {1}", values[0], unit);
        String max = string.Format("Max: {0,2:##.00} {1}", values[1], unit);
        String avg = string.Format("Avg: {0,2:##.00} {1}", values[2], unit);
        brickletLCD.WriteLine(0, 0, title);
        brickletLCD.WriteLine(1, 0, min);
        brickletLCD.WriteLine(2, 0, avg);
        brickletLCD.WriteLine(3, 0, max);
    }

.. image:: /Images/Kits/weather_station_lcd_minmaxavg_350.jpg
   :scale: 100 %
   :alt: MinMaxAvg Mode
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_minmaxavg_1000.jpg

Time Mode
^^^^^^^^^

In time mode we show the current time and date:

.. code-block:: csharp

    static private void UpdateTime()
    {
        string line0 = DateTime.Now.ToString("HH:MM:ss");
        string line1 = DateTime.Now.ToString("dddd");
        string line2 = DateTime.Now.ToString("D");
        brickletLCD.WriteLine((byte)0, (byte)((LINE_LENGTH-line0.Length)/2), line0);
        brickletLCD.WriteLine((byte)1, (byte)((LINE_LENGTH-line1.Length)/2), UTF16ToKS0066U(line1));
        brickletLCD.WriteLine((byte)2, (byte)((LINE_LENGTH-line2.Length)/2), UTF16ToKS0066U(line2));
    }

The UTF16ToKS0066U method encodes umlauts to the LCD charset (ä, ö, ü, etc).
This is needed, since C# gives the dates in the current operating system
language.

.. image:: /Images/Kits/weather_station_lcd_time_350.jpg
   :scale: 100 %
   :alt: Time Mode
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_time_1000.jpg

Step 4: Everything put together
-------------------------------

That's it! Now we have a Weather Station with four different modes
that can be controlled with the LCD20x4 Bricklet buttons.

This is of course still very elementary. There is lots of room
for improvement. For example it would be possible to show the unit in
graph mode whenever the shown values are not too big. Or perhaps it would
be better to show the top and bottom values of the graph on the left
side of the graph instead of the top.

All of the above put together (`download <https://raw.github.com/Tinkerforge/weather-station/master/button_control/csharp/WeatherStationButton.cs>`__):

.. literalinclude:: ../../../../../weather-station/button_control/csharp/WeatherStationButton.cs
 :language: csharp
 :linenos:
 :tab-width: 4
