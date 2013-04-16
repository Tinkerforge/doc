
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit C# auf das LCD 20x4 Bricklet schreiben

.. |ref_CALLBACK_ENUMERATE| replace:: :csharp:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_CALLBACK_CONNECTED| replace:: :csharp:func:`Connected <IPConnection::Connected>`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :csharp:func:`Enumerate <IPConnection::Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``IlluminanceCB``
.. |cb_humidity| replace:: ``HumidityCB``
.. |cb_air_pressure| replace:: ``AirPressureCB``

.. include:: CSharpToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_csharp_to_lcd:

Mit C# auf das LCD 20x4 Bricklet schreiben
==========================================

.. include:: CSharpCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: CSharpToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

|step1_start_off|

.. code-block:: csharp

    private static string HOST = "localhost";
    private static int PORT = 4223;

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: csharp

    static void Main()
    {
        ipcon = new IPConnection();
        ipcon.Connect(HOST, PORT);

        ipcon.EnumerateCallback += EnumerateCB;
        ipcon.Connected += ConnectedCB;

        ipcon.Enumerate();
    }

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: csharp

    static void ConnectedCB(IPConnection sender, short connectedReason)
    {
        if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT)
        {
            ipcon.Enumerate();
        }
    }

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: csharp

    class WeatherStation
    {
        private static string HOST = "localhost";
        private static int PORT = 4223;

        static void ConnectedCB(IPConnection sender, short connectedReason)
        {
            if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT)
            {
                ipcon.Enumerate();
            }
        }

        static void Main()
        {
            ipcon = new IPConnection();
            ipcon.Connect(HOST, PORT);

            ipcon.EnumerateCallback += EnumerateCB;
            ipcon.Connected += ConnectedCB;

            ipcon.Enumerate();
        }
    }


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: csharp

    static void EnumerateCB(IPConnection sender, string UID, string connectedUID, char position,
                            short[] hardwareVersion, short[] firmwareVersion,
                            int deviceIdentifier, short enumerationType)
    {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)

|step2_lcd_config|

.. code-block:: csharp

    if(deviceIdentifier == BrickletLCD20x4.DEVICE_IDENTIFIER)
    {
        brickletLCD = new BrickletLCD20x4(UID, ipcon);
        brickletLCD.ClearDisplay();
        brickletLCD.BacklightOn();
    }

|step2_other_config1|

.. code-block:: csharp

    else if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER)
    {
        brickletAmbientLight = new BrickletAmbientLight(UID, ipcon);
        brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
        brickletAmbientLight.Illuminance += IlluminanceCB;
    }
    else if(deviceIdentifier == BrickletHumidity.DEVICE_IDENTIFIER)
    {
        brickletHumidity = new BrickletHumidity(UID, ipcon);
        brickletHumidity.SetHumidityCallbackPeriod(1000);
        brickletHumidity.Humidity += HumidityCB;
    }
    else if(deviceIdentifier == BrickletBarometer.DEVICE_IDENTIFIER)
    {
        brickletBarometer = new BrickletBarometer(UID, ipcon);
        brickletBarometer.SetAirPressureCallbackPeriod(1000);
        brickletBarometer.AirPressure += AirPressureCB;
    }

|step2_other_config2|

|step2_put_together|

.. code-block:: csharp

    static void EnumerateCB(IPConnection sender, string UID, string connectedUID, char position,
                            short[] hardwareVersion, short[] firmwareVersion,
                            int deviceIdentifier, short enumerationType)
    {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)
        {
            if(deviceIdentifier == BrickletLCD20x4.DEVICE_IDENTIFIER)
            {
                brickletLCD = new BrickletLCD20x4(UID, ipcon);
                brickletLCD.ClearDisplay();
                brickletLCD.BacklightOn();
            }
            else if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER)
            {
                brickletAmbientLight = new BrickletAmbientLight(UID, ipcon);
                brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
                brickletAmbientLight.Illuminance += IlluminanceCB;
            }
            else if(deviceIdentifier == BrickletHumidity.DEVICE_IDENTIFIER)
            {
                brickletHumidity = new BrickletHumidity(UID, ipcon);
                brickletHumidity.SetHumidityCallbackPeriod(1000);
                brickletHumidity.Humidity += HumidityCB;
            }
            else if(deviceIdentifier == BrickletBarometer.DEVICE_IDENTIFIER)
            {
                brickletBarometer = new BrickletBarometer(UID, ipcon);
                brickletBarometer.SetAirPressureCallbackPeriod(1000);
                brickletBarometer.AirPressure += AirPressureCB;
            }
        }
    }


Schritt 3: Messwerte auf dem Display anzeigen
---------------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: csharp

    string text = string.Format("{0,6:###.00}", value);

|step3_printf|

.. code-block:: csharp

    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        string text = string.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0);
        brickletLCD.WriteLine(0, 0, text);
    }

    static void HumidityCB(BrickletHumidity sender, int humidity)
    {
        string text = string.Format("Humidity   {0,6:###.00} %", humidity/10.0);
        brickletLCD.WriteLine(1, 0, text);
    }

    static void AirPressureCB(BrickletBarometer sender, int airPressure)
    {
        string text = string.Format("Air Press {0,7:####.00} mb", airPressure/1000.0);
        brickletLCD.WriteLine(2, 0, text);
    }

|step3_temperature|

.. code-block:: csharp

    static void AirPressureCB(BrickletBarometer sender, int airPressure)
    {
        string text = string.Format("Air Press {0,7:####.00} mb", airPressure/1000.0);
        brickletLCD.WriteLine(2, 0, text);

        int temperature = sender.GetChipTemperature();
        text = string.Format("Temperature {0,5:##.00} {1}C", temperature/100.0, (char)0xDF);
        brickletLCD.WriteLine(3, 0, text);
    }

|step3_put_together|

.. code-block:: csharp

    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        string text = string.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0);
        brickletLCD.WriteLine(0, 0, text);
    }

    static void HumidityCB(BrickletHumidity sender, int humidity)
    {
        string text = string.Format("Humidity   {0,6:###.00} %", humidity/10.0);
        brickletLCD.WriteLine(1, 0, text);
    }

    static void AirPressureCB(BrickletBarometer sender, int airPressure)
    {
        string text = string.Format("Air Press {0,7:####.00} mb", airPressure/1000.0);
        brickletLCD.WriteLine(2, 0, text);

        int temperature = sender.GetChipTemperature();
        // 0xDF == ° on LCD 20x4 charset
        text = string.Format("Temperature {0,5:##.00} {1}C", temperature/100.0, (char)0xDF);
        brickletLCD.WriteLine(3, 0, text);
    }

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

|step4_intro1|

.. code-block:: csharp

    while(true)
    {
        try
        {
            ipcon.Connect(HOST, PORT);
            break;
        }
        catch(System.Net.Sockets.SocketException e)
        {
            System.Console.WriteLine("Connection Error: " + e.Message);
            System.Threading.Thread.Sleep(1000);
        }
    }


|step4_intro2|

.. code-block:: csharp

    while(true)
    {
        try
        {
            ipcon.Enumerate();
            break;
        }
        catch(NotConnectedException e)
        {
            System.Console.WriteLine("Enumeration Error: " + e.Message);
            System.Threading.Thread.Sleep(1000);
        }
    }

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: csharp

    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        if(brickletLCD != null)
        {
            string text = string.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0);
            brickletLCD.WriteLine(0, 0, text);
            System.Console.WriteLine("Write to line 0: " + text);
        }
    }

|step4_lcd_initialized2|

.. code-block:: csharp

    if(deviceIdentifier == BrickletAmbientLight.DEVICE_IDENTIFIER)
    {
        try
        {
            brickletAmbientLight = new BrickletAmbientLight(UID, ipcon);
            brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
            brickletAmbientLight.Illuminance += IlluminanceCB;
            System.Console.WriteLine("AmbientLight initialized");
        }
        catch(TinkerforgeException e)
        {
            System.Console.WriteLine("AmbientLight init failed: " + e.Message);
            brickletAmbientLight = null;
        }
    }

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/csharp/WeatherStation.cs>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/csharp/WeatherStation.cs
 :language: csharp
 :tab-width: 4
