
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Visual Basic .NET auf das LCD 20x4 Bricklet schreiben

.. |ref_CALLBACK_ENUMERATE| replace:: :vbnet:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_CALLBACK_CONNECTED| replace:: :vbnet:func:`Connected <IPConnection::Connected>`
.. |callback| replace:: Callback
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``IlluminanceCB``
.. |cb_humidity| replace:: ``HumidityCB``
.. |cb_air_pressure| replace:: ``AirPressureCB``

.. include:: VBNETToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_vbnet_to_lcd:

Mit Visual Basic .NET auf das LCD 20x4 Bricklet schreiben
=========================================================

.. include:: VBNETCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: VBNETToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

|step1_start_off|

.. code-block:: vbnet

    Const HOST As String = "localhost"
    Const PORT As Integer = 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: vbnet

    Sub Main()
        ipcon = New IPConnection()
        ipcon.Connect(HOST, PORT)

        AddHandler ipcon.EnumerateCallback, AddressOf EnumerateCB
        AddHandler ipcon.Connected, AddressOf ConnectedCB

        ipcon.Enumerate()
    End Sub

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: vbnet

    Sub ConnectedCB(ByVal sender As IPConnection, ByVal connectedReason as Short)
        If connectedReason = IPConnection.CONNECT_REASON_AUTO_RECONNECT Then
            ipcon.Enumerate()
        End If
    End Sub

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: vbnet

    Module WeatherStation
        Const HOST As String = "localhost"
        Const PORT As Integer = 4223

        Sub ConnectedCB(ByVal sender As IPConnection, ByVal connectedReason as Short)
            If connectedReason = IPConnection.CONNECT_REASON_AUTO_RECONNECT Then
                ipcon.Enumerate()
            End If
        End Sub

        Sub Main()
            ipcon = New IPConnection()
            ipcon.Connect(HOST, PORT)

            AddHandler ipcon.EnumerateCallback, AddressOf EnumerateCB
            AddHandler ipcon.Connected, AddressOf ConnectedCB

            ipcon.Enumerate()
        End Sub
    End Module


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: vbnet

    Sub EnumerateCB(ByVal sender As IPConnection, ByVal uid As String, _
                    ByVal connectedUid As String, ByVal position As Char, _
                    ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, _
                    ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)
        If enumerationType = IPConnection.ENUMERATION_TYPE_CONNECTED Or _
           enumerationType = IPConnection.ENUMERATION_TYPE_AVAILABLE Then

|step2_lcd_config|

.. code-block:: vbnet

    If deviceIdentifier = BrickletLCD20x4.DEVICE_IDENTIFIER Then
        brickletLCD = New BrickletLCD20x4(UID, ipcon)
        brickletLCD.ClearDisplay()
        brickletLCD.BacklightOn()

|step2_other_config1|

.. code-block:: vbnet

    Else If deviceIdentifier = BrickletAmbientLight.DEVICE_IDENTIFIER Then
        brickletAmbientLight = New BrickletAmbientLight(UID, ipcon)
        brickletAmbientLight.SetIlluminanceCallbackPeriod(1000)
        AddHandler brickletAmbientLight.Illuminance, AddressOf IlluminanceCB
    Else If deviceIdentifier = BrickletHumidity.DEVICE_IDENTIFIER Then
        brickletHumidity = New BrickletHumidity(UID, ipcon)
        brickletHumidity.SetHumidityCallbackPeriod(1000)
        AddHandler brickletHumidity.Humidity, AddressOf HumidityCB
    Else If deviceIdentifier = BrickletBarometer.DEVICE_IDENTIFIER Then
        brickletBarometer = New BrickletBarometer(UID, ipcon)
        brickletBarometer.SetAirPressureCallbackPeriod(1000)
        AddHandler brickletBarometer.AirPressure, AddressOf AirPressureCB
    End If

|step2_other_config2|

|step2_put_together|

.. code-block:: vbnet

    Sub EnumerateCB(ByVal sender As IPConnection, ByVal uid As String, _
                    ByVal connectedUid As String, ByVal position As Char, _
                    ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, _
                    ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)
        If enumerationType = IPConnection.ENUMERATION_TYPE_CONNECTED Or _
           enumerationType = IPConnection.ENUMERATION_TYPE_AVAILABLE Then
            If deviceIdentifier = BrickletLCD20x4.DEVICE_IDENTIFIER Then
                brickletLCD = New BrickletLCD20x4(UID, ipcon)
                brickletLCD.ClearDisplay()
                brickletLCD.BacklightOn()
            Else If deviceIdentifier = BrickletAmbientLight.DEVICE_IDENTIFIER Then
                brickletAmbientLight = New BrickletAmbientLight(UID, ipcon)
                brickletAmbientLight.SetIlluminanceCallbackPeriod(1000)
                AddHandler brickletAmbientLight.Illuminance, AddressOf IlluminanceCB
            Else If deviceIdentifier = BrickletHumidity.DEVICE_IDENTIFIER Then
                brickletHumidity = New BrickletHumidity(UID, ipcon)
                brickletHumidity.SetHumidityCallbackPeriod(1000)
                AddHandler brickletHumidity.Humidity, AddressOf HumidityCB
            Else If deviceIdentifier = BrickletBarometer.DEVICE_IDENTIFIER Then
                brickletBarometer = New BrickletBarometer(UID, ipcon)
                brickletBarometer.SetAirPressureCallbackPeriod(1000)
                AddHandler brickletBarometer.AirPressure, AddressOf AirPressureCB
            End If
        End If
    End Sub


Schritt 3: Messwerte auf dem Display anzeigen
---------------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: vbnet

    Dim text As String = String.Format("{0,6:###.00}", value)

|step3_printf|

.. code-block:: vbnet

    Sub IlluminanceCB(ByVal sender As BrickletAmbientLight, ByVal illuminance As Integer)
        Dim text As String = String.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0)
        brickletLCD.WriteLine(0, 0, text)
    End Sub

    Sub HumidityCB(ByVal sender As BrickletHumidity, ByVal humidity As Integer)
        Dim text As String = String.Format("Humidity   {0,6:###.00} %", humidity/10.0)
        brickletLCD.WriteLine(1, 0, text)
    End Sub

    Sub AirPressureCB(ByVal sender As BrickletBarometer, ByVal airPressure As Integer)
        Dim text As String = String.Format("Air Press {0,7:####.00} mb", airPressure/1000.0)
        brickletLCD.WriteLine(2, 0, text)
    End Sub

|step3_temperature|

.. code-block:: vbnet

    Sub AirPressureCB(ByVal sender As BrickletBarometer, ByVal airPressure As Integer)
        Dim text As String = String.Format("Air Press {0,7:####.00} mb", airPressure/1000.0)
        brickletLCD.WriteLine(2, 0, text)

        Dim temperature As Integer = sender.GetChipTemperature()
        text = String.Format("Temperature {0,5:##.00} {1}C", temperature/100.0, Chr(&HDF))
        brickletLCD.WriteLine(3, 0, text)
    End Sub

|step3_put_together|

.. code-block:: vbnet

    Sub IlluminanceCB(ByVal sender As BrickletAmbientLight, ByVal illuminance As Integer)
        Dim text As String = String.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0)
        brickletLCD.WriteLine(0, 0, text)
    End Sub

    Sub HumidityCB(ByVal sender As BrickletHumidity, ByVal humidity As Integer)
        Dim text As String = String.Format("Humidity   {0,6:###.00} %", humidity/10.0)
        brickletLCD.WriteLine(1, 0, text)
    End Sub

    Sub AirPressureCB(ByVal sender As BrickletBarometer, ByVal airPressure As Integer)
        Dim text As String = String.Format("Air Press {0,7:####.00} mb", airPressure/1000.0)
        brickletLCD.WriteLine(2, 0, text)

        Dim temperature As Integer = sender.GetChipTemperature()
        ' &HDF == ° on LCD 20x4 charset
        text = String.Format("Temperature {0,5:##.00} {1}C", temperature/100.0, Chr(&HDF))
        brickletLCD.WriteLine(3, 0, text)
    End Sub

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

|step4_intro1|

.. code-block:: vbnet

    while True
        Try
            ipcon.Connect(HOST, PORT)
            Exit While
        Catch e As System.Net.Sockets.SocketException
            System.Console.WriteLine("Connection Error: " + e.Message)
            System.Threading.Thread.Sleep(1000)
        End Try
    End While

|step4_intro2|

.. code-block:: vbnet

    while True
        try
            ipcon.Enumerate()
            Exit While
        Catch e As NotConnectedException
            System.Console.WriteLine("Enumeration Error: " + e.Message)
            System.Threading.Thread.Sleep(1000)
        End Try
    End While

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: vbnet

    Sub IlluminanceCB(ByVal sender As BrickletAmbientLight, ByVal illuminance As Integer)
        If brickletLCD IsNot Nothing Then
            Dim text As String = String.Format("Illuminanc {0,6:###.00} lx", illuminance/10.0)
            brickletLCD.WriteLine(0, 0, text)
            System.Console.WriteLine("Write to line 0: " + text)
        End If
    End Sub

|step4_lcd_initialized2|

.. code-block:: vbnet

    If deviceIdentifier = BrickletAmbientLight.DEVICE_IDENTIFIER Then
        Try
            brickletAmbientLight = New BrickletAmbientLight(UID, ipcon)
            brickletAmbientLight.SetIlluminanceCallbackPeriod(1000)
            AddHandler brickletAmbientLight.Illuminance, AddressOf IlluminanceCB
            System.Console.WriteLine("AmbientLight initialized")
        Catch e As TinkerforgeException
            System.Console.WriteLine("AmbientLight init failed: " + e.Message)
            brickletAmbientLight = Nothing
        End Try
    End If

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/vbnet/WeatherStation.vb>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/vbnet/WeatherStation.vb
 :language: vbnet
 :tab-width: 4
