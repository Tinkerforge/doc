
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Rauchmelder mit Delphi auslesen

.. |ref_CALLBACK_ENUMERATE| replace:: :delphi:func:`OnEnumerate <TIPConnection.OnEnumerate>`
.. |ref_CALLBACK_CONNECTED| replace:: :delphi:func:`OnConnected <TIPConnection.OnConnected>`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :delphi:func:`Enumerate <TIPConnection.Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``IPCON_ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``IPCON_ENUMERATION_TYPE_AVAILABLE``
.. |cb_interrupt| replace:: ``InterruptCB``
.. |value_mask| replace:: ``valueMask``

.. include:: SmokeDetector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_delphi:

Rauchmelder mit Delphi auslesen
===============================

.. include:: DelphiCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: SmokeDetector.substitutions
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

    procedure TSmokeDetector.Execute;
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

    procedure TSmokeDetector.ConnectedCB(sender: TIPConnection; const connectedReason: byte);
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
      TSmokeDetector = class
      private
        ipcon: TIPConnection;
      public
        procedure ConnectedCB(sender: TIPConnection; const connectedReason: byte);
        procedure Execute;
      end;

    procedure TSmokeDetector.ConnectedCB(sender: TIPConnection; const connectedReason: byte);
    begin
      if (connectedReason = IPCON_CONNECT_REASON_AUTO_RECONNECT) then begin
        ipcon.Enumerate;
      end;
    end;

    procedure TSmokeDetector.Execute;
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

    procedure TSmokeDetector.EnumerateCB(sender: TIPConnection; const uid: string;
                                         const connectedUid: string; const position: char;
                                         const hardwareVersion: TVersionNumber;
                                         const firmwareVersion: TVersionNumber;
                                         const deviceIdentifier: word; const enumerationType: byte);
    begin
      if ((enumerationType = IPCON_ENUMERATION_TYPE_CONNECTED) or
          (enumerationType = IPCON_ENUMERATION_TYPE_AVAILABLE)) then begin

|step2_config|

.. code-block:: delphi

    if (deviceIdentifier = BRICKLET_INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) then begin
      brickletIndustrialDigitalIn4 := TBrickletIndustrialDigitalIn4.Create(uid, ipcon);
      brickletIndustrialDigitalIn4.SetDebouncePeriod(10000);
      brickletIndustrialDigitalIn4.SetInterrupt(15);
      brickletIndustrialDigitalIn4.OnInterrupt := {$ifdef FPC}@{$endif}InterruptCB;
    end;

|step2_put_together|

.. code-block:: delphi

    procedure TSmokeDetector.EnumerateCB(sender: TIPConnection; const uid: string;
                                         const connectedUid: string; const position: char;
                                         const hardwareVersion: TVersionNumber;
                                         const firmwareVersion: TVersionNumber;
                                         const deviceIdentifier: word; const enumerationType: byte);
    begin
      if ((enumerationType = IPCON_ENUMERATION_TYPE_CONNECTED) or
          (enumerationType = IPCON_ENUMERATION_TYPE_AVAILABLE)) then begin
        if (deviceIdentifier = BRICKLET_INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) then begin
          brickletIndustrialDigitalIn4 := TBrickletIndustrialDigitalIn4.Create(uid, ipcon);
          brickletIndustrialDigitalIn4.SetDebouncePeriod(10000);
          brickletIndustrialDigitalIn4.SetInterrupt(15);
          brickletIndustrialDigitalIn4.OnInterrupt := {$ifdef FPC}@{$endif}InterruptCB;
        end;
      end;
    end;


Schritt 3: Auf Alarmsignal reagieren
------------------------------------

|step3_intro|

.. code-block:: delphi

    procedure TSmokeDetector.InterruptCB(sender: TBrickletIndustrialDigitalIn4; const interruptMask: word; const valueMask: word);
    begin
      if (valueMask > 0) then begin
        WriteLn('Fire! Fire!');
      end;
    end;

|step3_complete|

|step3_suggestions|

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

|step4_initialization|

.. code-block:: delphi

    if (deviceIdentifier = BRICKLET_INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) then begin
      try
        brickletIndustrialDigitalIn4 := TBrickletIndustrialDigitalIn4.Create(uid, ipcon);
        brickletIndustrialDigitalIn4.SetDebouncePeriod(10000);
        brickletIndustrialDigitalIn4.SetInterrupt(15);
        brickletIndustrialDigitalIn4.OnInterrupt := {$ifdef FPC}@{$endif}InterruptCB;
        WriteLn('Industrial Digital In 4 initialized');
      except
        on e: Exception do begin
          WriteLn('Industrial Digital In 4 init failed: ' + e.Message);
          brickletIndustrialDigitalIn4 := nil;
        end;
      end;
    end;

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/delphi/SmokeDetector.pas>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/delphi/SmokeDetector.pas
 :language: delphi
 :tab-width: 4
