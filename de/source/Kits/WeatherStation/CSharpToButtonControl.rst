
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit C# verschiedene Wetterstatistiken anzeigen

.. _starter_kit_weather_station_button_control:

Mit C# verschiedene Wetterstatistiken anzeigen
===============================================

.. include:: CSharpCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

Das LCD Bricklet ist mit vier Tastern ausgestattet, die dazu genutzt werden 
sollen um zwischen der Anzeige von verschiedenen Wetterstatistiken 
umzuschalten.
Dazu gehören:

* Standard Wetteranzeige,
* 24h Min/Max/Durchschnitt,
* 24h Graph und
* Zeit und Datum.

Dieses Projekt baut auf dem 
:ref:`Mit C# auf das LCD 20x4 Bricklet schreiben <starter_kit_weather_station_csharp_to_lcd>`
Projekt auf. Im folgenden werden wir Schritt-für-Schritt erklären wie die 
oben genannten Funktionen implementiert werden können. Wir werden diesmal nur
das generelle Konzept erläutern, so dass das Programm einfach zu verstehen 
sein sollte. 

Schritt 1: Daten auslesen
-------------------------

Die Struktur des Programms ist identisch zu der aus dem
:ref:`Mit C# auf das LCD 20x4 Bricklet schreiben <starter_kit_weather_station_csharp_to_lcd>`
Projekt.

Die Wetterdaten erhalten wir über Callback mit 1s Intervall. Dieses mal
speichern wir allerdings die Messungen:

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

Um die letzten Messungen zu nutzen starten wir einen 1s Timer

.. code-block:: csharp

    Timer timer = new Timer(Update, null, TimeSpan.Zero, TimeSpan.FromSeconds(1));

und speichern die Messungen in einer Queue, so dass wir diese später analysieren 
können:

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

Auf den ersten Blick mag diese Programmiermethode etwas verwirrend wirken. 
Warum können wir nicht einfach Getter-Methoden in der Update Funktion aufrufen
oder die Messungen währen eines Callbacks speichern?

Es gibt zwei Gründe warum die Nutzung dieses Ansatzes Sinn macht:

1. Die Callbacks werden in 1s Intervallen aufgerufen aber auch nur, wenn sich 
   der aktuelle Callback-Wert ändert. Das heißt, wenn sich der Messwert für 
   10s nicht ändert wird auch der Callback erst nach diesen 10s aufgerufen.
   Das ist vorteilhaft, da so Bandbreite gespart werden kann. Die Messwerte
   werden gespeichert und können so für Statistiken genutzt werden.
2. Durch das Arbeiten mit Callbacks und einen separaten Timer mit einem 1s
   Intervall können auch kurze Verbindungsabbrüche oder ähnliches überbrückt
   werden. Zum Beispiel: Wenn die Wetterstation über Wi-Fi gesteuert wird und
   diese Verbindung für 30s unterbrochen ist, wird einfach der letzte Wert 
   benutzt der vor diesen 30s empfangen wurde. Hätten wir Getters hierfür 
   verwendet, so hätten wir Timeouts für jede Messung behandeln müssen. Da 
   die Standard Timeout Zeit bei 2.5s liegt und somit länger ist wie unser 1s 
   Intervall, hätte dies unsere Messungen verzerren können.

Schritt 2: Kontrolle über Taster
--------------------------------

Um über die LCD-Taster steuern zu können muss der ButtonPressed Callback zur
Initialisierung hinzugefügt werden:

.. code-block:: csharp

    brickletLCD.ButtonPressed += PressedCB;

In diesem Callback wird gespeichert welcher Taster zuletzt gedrückt wurde
und ein Zähler für den jeweiligen Taster inkrementiert, falls dieser
auch als letztes zuvor gedrückt wurde. Somit können wir zwischen 
verschiedenen Ansichten in einem Modus (z.B. Anzeige von 24h Graph) wechseln.

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

Um sofort auf den Tastendruck zu reagieren, löschen wir das Display und rufen
UpdateSwitch auf.

Die UpdateSwitch Methode wechselt zwischen den vier verschiedenen Modi.

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

Die vier Modi sind:

* Standard: Zeige alle 4 Messungen an.
* Graph: Zeige einen 24h Graphen von jeder Messung an. Durch mehrmaliges 
  drücken des Tasters kann zwischen den Messungen gewechselt werden.
* MinMaxAvg: Zeigt Minimums-, Maximums- und den Durchschnittswert jeder Messung
  an. Auch hierbei ist es möglich über einen erneuten Tasterdruck zwischen den
  Messwerten zu wechseln.
* Time: Zeigt die aktuelle Uhrzeit und das Datum an.



Schritt 3: Anzeige der vier Modi im Display
-------------------------------------------

Die Implementierung der vier Modi:

Standardmodus
^^^^^^^^^^^^^

Im Standard-Modus zeigen wir nur die Messwerte an:

.. code-block:: csharp

    static private void UpdateStandard()
    {
        string text = string.Format("Illuminanc {0,6:###.00} lx", latestIlluminance);
        brickletLCD.WriteLine(0, 0, text);

        text = string.Format("Humidity   {0,6:###.00} %", latestHumidity);
        brickletLCD.WriteLine(1, 0, text);

        text = string.Format("Air Press {0,7:####.00} mb", latestAirPressure);
        brickletLCD.WriteLine(2, 0, text);

        text = string.Format("Temperature {0,5:##.00} {1}C", latestTemperature, (char)0xDF);
        brickletLCD.WriteLine(3, 0, text);
    }

.. image:: /Images/Kits/weather_station_lcd_standard_350.jpg
   :scale: 100 %
   :alt: Standard Mode
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_standard_1000.jpg

Graphmodus
^^^^^^^^^^

Im Graph-Modus zeigen wir einen Balkengraphen der letzten 24 Stunden an:

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

Wir gehen hier nicht weiter ins Detail. Die Methoden wie die Graphen 
berechnet werden können zum Schluss im vollständigen Programm betrachtet 
werden. Für die Balkengraphen müssen allerdings ein paar Custom-Characters
bei der Initialisierung konfiguriert werden:

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

Dies konfiguriert die acht verfügbaren Custom-Characters als Balken mit Höhe
eins bis acht.

.. image:: /Images/Kits/weather_station_lcd_graph_350.jpg
   :scale: 100 %
   :alt: Graphmodus
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_graph_1000.jpg

MinMaxAvg-Modus
^^^^^^^^^^^^^^^

Im MinMaxAvg-Modus zeigen wir das Minimum, Maximum und den Durchschnittswert
der letzten 24h an:

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

Diese Werte werden in 4 Zeilen geschrieben, wobei die erste Zeile den Titel 
der jeweiligen Messungen anzeigt:

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
   :alt: MinMaxAvg-Modus
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_minmaxavg_1000.jpg

Time-Modus
^^^^^^^^^^

Im Time-Modus zeigt das Display die momentan Uhrzeit und das aktuelle Datum an:

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

Die UTF16ToKS0066U Methode encodiert Umlaute für den LCD Zeichensatz (ä, ö, ü, etc).
Dies wird benötigt, da C# die Daten in der momentanen Betriebssystem-Sprache übergibt.

.. image:: /Images/Kits/weather_station_lcd_time_350.jpg
   :scale: 100 %
   :alt: Time-Modus
   :align: center
   :target: ../../_images/Kits/weather_station_lcd_time_1000.jpg

Schritt 4: Alles zusammenfügen
------------------------------

Das war es! Nun haben wir eine Wetterstation mit vier Modi,
die über die LCD 20x4 Taster gesteuert werden kann.

Zugegeben ist dies alles noch ein wenig elementar. Es gibt
genügend Möglichkeiten Dinge zu verbessern. Zum Beispiel wäre
es Möglich die Einheit der Messwerte mit anzuzeigen sofern der Messwert
nicht zu groß ist. Oder es wäre besser die Graphenbeschriftungen
anstatt oben auf der linken Seite darzustellen.

Hier der komplette Quelltext (`download <https://raw.github.com/Tinkerforge/weather-station/master/button_control/csharp/WeatherStationButton.cs>`__):

.. literalinclude:: ../../../../../weather-station/button_control/csharp/WeatherStationButton.cs
 :language: csharp
 :tab-width: 4
