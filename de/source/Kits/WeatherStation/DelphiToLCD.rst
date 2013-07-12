
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Delphi auf das LCD 20x4 Bricklet schreiben

.. |ref_CALLBACK_ENUMERATE| replace:: :delphi:func:`OnEnumerate <TIPConnection.OnEnumerate>`
.. |ref_CALLBACK_CONNECTED| replace:: :delphi:func:`OnConnected <TIPConnection.OnConnected>`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :delphi:func:`Enumerate <TIPConnection.Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``IPCON_ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``IPCON_ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``IlluminanceCB``
.. |cb_humidity| replace:: ``HumidityCB``
.. |cb_air_pressure| replace:: ``AirPressureCB``

.. include:: WriteToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_delphi_to_lcd:

Mit Delphi auf das LCD 20x4 Bricklet schreiben
==============================================

.. include:: DelphiCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: WriteToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

|step1_start_off|

.. code-block:: delphi

    const
      HOST = 'localhost';
      PORT = 4223;

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: delphi

    procedure TWeatherStation.Execute;
    begin
      ipcon := TIPConnection.Create;
      ipcon.Connect(HOST, PORT);
      ipcon.OnEnumerate := {$ifdef FPC}@{$endif}EnumerateCB;
      ipcon.OnConnected := {$ifdef FPC}@{$endif}ConnectedCB;
      ipcon.Enumerate;
    end;

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: delphi

    procedure TWeatherStation.ConnectedCB(sender: TIPConnection; const connectedReason: byte);
    begin
      if (connectedReason = IPCON_CONNECT_REASON_AUTO_RECONNECT) then begin
        ipcon.Enumerate;
      end;
    end;

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: delphi

    const
      HOST = 'localhost';
      PORT = 4223;

    type
      TWeatherStation = class
      private
        ipcon: TIPConnection;
      public
        procedure ConnectedCB(sender: TIPConnection; const connectedReason: byte);
        procedure Execute;
      end;

    procedure TWeatherStation.ConnectedCB(sender: TIPConnection; const connectedReason: byte);
    begin
      if (connectedReason = IPCON_CONNECT_REASON_AUTO_RECONNECT) then begin
        ipcon.Enumerate;
      end;
    end;

    procedure TWeatherStation.Execute;
    begin
      ipcon := TIPConnection.Create;
      ipcon.Connect(HOST, PORT);
      ipcon.OnEnumerate := {$ifdef FPC}@{$endif}EnumerateCB;
      ipcon.OnConnected := {$ifdef FPC}@{$endif}ConnectedCB;
      ipcon.Enumerate;
    end;


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: delphi

    procedure TWeatherStation.EnumerateCB(sender: TIPConnection; const uid: string;
                                          const connectedUid: string; const position: char;
                                          const hardwareVersion: TVersionNumber;
                                          const firmwareVersion: TVersionNumber;
                                          const deviceIdentifier: word; const enumerationType: byte);
    begin
      if ((enumerationType = IPCON_ENUMERATION_TYPE_CONNECTED) or
          (enumerationType = IPCON_ENUMERATION_TYPE_AVAILABLE)) then begin

|step2_lcd_config|

.. code-block:: delphi

    if (deviceIdentifier = BRICKLET_LCD_20X4_DEVICE_IDENTIFIER) then begin
      brickletLCD := TBrickletLCD20x4.Create(UID, ipcon);
      brickletLCD.ClearDisplay();
      brickletLCD.BacklightOn();
    end;

|step2_other_config1|

.. code-block:: delphi

    else if (deviceIdentifier = BRICKLET_AMBIENT_LIGHT_DEVICE_IDENTIFIER) then begin
      brickletAmbientLight := TBrickletAmbientLight.Create(uid, ipcon);
      brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
      brickletAmbientLight.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;
    end
    else if (deviceIdentifier = BRICKLET_HUMIDITY_DEVICE_IDENTIFIER) then begin
      brickletHumidity := TBrickletHumidity.Create(uid, ipcon);
      brickletHumidity.SetHumidityCallbackPeriod(1000);
      brickletHumidity.OnHumidity := {$ifdef FPC}@{$endif}HumidityCB;
    end
    else if (deviceIdentifier = BRICKLET_BAROMETER_DEVICE_IDENTIFIER) then begin
      brickletBarometer := TBrickletBarometer.Create(uid, ipcon);
      brickletBarometer.SetAirPressureCallbackPeriod(1000);
      brickletBarometer.OnAirPressure := {$ifdef FPC}@{$endif}AirPressureCB;
    end;

|step2_other_config2|

|step2_put_together|

.. code-block:: delphi

    procedure TWeatherStation.EnumerateCB(sender: TIPConnection; const uid: string;
                                          const connectedUid: string; const position: char;
                                          const hardwareVersion: TVersionNumber;
                                          const firmwareVersion: TVersionNumber;
                                          const deviceIdentifier: word; const enumerationType: byte);
    begin
      if ((enumerationType = IPCON_ENUMERATION_TYPE_CONNECTED) or
          (enumerationType = IPCON_ENUMERATION_TYPE_AVAILABLE)) then begin
        if (deviceIdentifier = BRICKLET_LCD_20X4_DEVICE_IDENTIFIER) then begin
          brickletLCD := TBrickletLCD20x4.Create(UID, ipcon);
          brickletLCD.ClearDisplay();
          brickletLCD.BacklightOn();
        end
        else if (deviceIdentifier = BRICKLET_AMBIENT_LIGHT_DEVICE_IDENTIFIER) then begin
          brickletAmbientLight := TBrickletAmbientLight.Create(uid, ipcon);
          brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
          brickletAmbientLight.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;
        end
        else if (deviceIdentifier = BRICKLET_HUMIDITY_DEVICE_IDENTIFIER) then begin
          brickletHumidity := TBrickletHumidity.Create(uid, ipcon);
          brickletHumidity.SetHumidityCallbackPeriod(1000);
          brickletHumidity.OnHumidity := {$ifdef FPC}@{$endif}HumidityCB;
        end
        else if (deviceIdentifier = BRICKLET_BAROMETER_DEVICE_IDENTIFIER) then begin
          brickletBarometer := TBrickletBarometer.Create(uid, ipcon);
          brickletBarometer.SetAirPressureCallbackPeriod(1000);
          brickletBarometer.OnAirPressure := {$ifdef FPC}@{$endif}AirPressureCB;
        end;
      end;
    end;


Schritt 3: Messwerte auf dem Display anzeigen
---------------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: delphi

    text := Format('%6.2f', [value])

|step3_printf|

.. code-block:: delphi

    procedure TWeatherStation.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
    var text: string;
    begin
      text := Format('Illuminanc %6.2f lx', [illuminance/10.0]);
      brickletLCD.WriteLine(0, 0, text);
    end;

    procedure TWeatherStation.HumidityCB(sender: TBrickletHumidity; const humidity: word);
    var text: string;
    begin
      text := Format('Humidity   %6.2f %%', [humidity/10.0]);
      brickletLCD.WriteLine(1, 0, text);
    end;

    procedure TWeatherStation.AirPressureCB(sender: TBrickletBarometer; const airPressure: longint);
    var text: string;
    begin
      text := Format('Air Press %7.2f mb', [airPressure/1000.0]);
      brickletLCD.WriteLine(2, 0, text);
    end;

|step3_temperature|

.. code-block:: delphi

    procedure TWeatherStation.AirPressureCB(sender: TBrickletBarometer; const airPressure: longint);
    var text: string; temperature: smallint;
    begin
      text := Format('Air Press %7.2f mb', [airPressure/1000.0]);
      brickletLCD.WriteLine(2, 0, text);

      temperature := brickletBarometer.GetChipTemperature;
      text := Format('Temperature %5.2f %sC', [temperature/100.0, '' + char($DF)]);
      brickletLCD.WriteLine(3, 0, text);
    end;

|step3_put_together|

.. code-block:: delphi

    procedure TWeatherStation.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
    var text: string;
    begin
      text := Format('Illuminanc %6.2f lx', [illuminance/10.0]);
      brickletLCD.WriteLine(0, 0, text);
    end;

    procedure TWeatherStation.HumidityCB(sender: TBrickletHumidity; const humidity: word);
    var text: string;
    begin
      text := Format('Humidity   %6.2f %%', [humidity/10.0]);
      brickletLCD.WriteLine(1, 0, text);
    end;

    procedure TWeatherStation.AirPressureCB(sender: TBrickletBarometer; const airPressure: longint);
    var text: string; temperature: smallint;
    begin
      text := Format('Air Press %7.2f mb', [airPressure/1000.0]);
      brickletLCD.WriteLine(2, 0, text);

      temperature := brickletBarometer.GetChipTemperature;
      { 0xDF == ° on LCD 20x4 charset }
      text := Format('Temperature %5.2f %sC', [temperature/100.0, '' + char($DF)]);
      brickletLCD.WriteLine(3, 0, text);
    end;

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

|step4_intro1|

.. code-block:: delphi

    while (true) do begin
      try
        ipcon.Connect(HOST, PORT);
        break;
      except
        on e: Exception do begin
          WriteLn('Connection Error: ' + e.Message);
          Sleep(1000);
        end;
      end;
    end;

|step4_intro2|

.. code-block:: delphi

    while (true) do begin
      try
        ipcon.Enumerate;
        break;
      except
        on e: Exception do begin
          WriteLn('Enumeration Error: ' + e.Message);
          Sleep(1000);
        end;
      end;
    end;

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: delphi

    procedure TWeatherStation.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
    var text: string;
    begin
      if (brickletLCD <> nil) then begin
        text := Format('Illuminanc %6.2f lx', [illuminance/10.0]);
        brickletLCD.WriteLine(0, 0, text);
        WriteLn('Write to line 0: ' + text);
      end;
    end;

|step4_lcd_initialized2|

.. code-block:: delphi

    if (deviceIdentifier = BRICKLET_AMBIENT_LIGHT_DEVICE_IDENTIFIER) then begin
      try
        brickletAmbientLight := TBrickletAmbientLight.Create(uid, ipcon);
        brickletAmbientLight.SetIlluminanceCallbackPeriod(1000);
        brickletAmbientLight.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;
        WriteLn('Ambient Light initialized');
      except
        on e: Exception do begin
          WriteLn('Ambient Light init failed: ' + e.Message);
          brickletAmbientLight := nil;
        end;
      end;
    end;

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/delphi/WeatherStation.pas>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/delphi/WeatherStation.pas
 :language: delphi
 :tab-width: 4
