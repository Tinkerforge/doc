
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Rauchmelder mit Visual Basic .NET auslesen

.. |ref_CALLBACK_ENUMERATE| replace:: :vbnet:func:`EnumerateCallback <IPConnection.EnumerateCallback>`
.. |ref_CALLBACK_CONNECTED| replace:: :vbnet:func:`Connected <IPConnection.Connected>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :vbnet:func:`Enumerate() <IPConnection.Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_interrupt| replace:: ``InterruptCB``
.. |value_mask| replace:: ``valueMask``

.. include:: SmokeDetector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_vbnet:

Rauchmelder mit Visual Basic .NET auslesen
==========================================

.. include:: VBNETCommon.substitutions
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

    Module SmokeDetector
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

|step2_config|

.. code-block:: vbnet

    If deviceIdentifier = BrickletIndustrialDigitalIn4.DEVICE_IDENTIFIER Then
        brickletIndustrialDigitalIn4 = New BrickletIndustrialDigitalIn4(UID, ipcon)
        brickletIndustrialDigitalIn4.SetDebouncePeriod(10000)
        brickletIndustrialDigitalIn4.SetInterrupt(15)
        AddHandler brickletIndustrialDigitalIn4.Interrupt, AddressOf InterruptCB
    End If

|step2_put_together|

.. code-block:: vbnet

    Sub EnumerateCB(ByVal sender As IPConnection, ByVal uid As String, _
                    ByVal connectedUid As String, ByVal position As Char, _
                    ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, _
                    ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)
        If enumerationType = IPConnection.ENUMERATION_TYPE_CONNECTED Or _
           enumerationType = IPConnection.ENUMERATION_TYPE_AVAILABLE Then
            If deviceIdentifier = BrickletIndustrialDigitalIn4.DEVICE_IDENTIFIER Then
                brickletIndustrialDigitalIn4 = New BrickletIndustrialDigitalIn4(UID, ipcon)
                brickletIndustrialDigitalIn4.SetDebouncePeriod(10000)
                brickletIndustrialDigitalIn4.SetInterrupt(15)
                AddHandler brickletIndustrialDigitalIn4.Interrupt, AddressOf InterruptCB
            End If
        End If
    End Sub


Schritt 3: Auf Alarmsignal reagieren
------------------------------------

|step3_intro|

.. code-block:: vbnet

    Sub InterruptCB(ByVal sender As BrickletIndustrialDigitalIn4, _
                    ByVal interruptMask As Integer, ByVal valueMask As Integer)
        If valueMask > 0 Then
            System.Console.WriteLine("Fire! Fire!")
        End If
    End Sub

|step3_complete|

|step3_suggestions|

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

|step4_initialization|

.. code-block:: vbnet

    If deviceIdentifier = BrickletIndustrialDigitalIn4.DEVICE_IDENTIFIER Then
        Try
            brickletIndustrialDigitalIn4 = New BrickletIndustrialDigitalIn4(UID, ipcon)
            brickletIndustrialDigitalIn4.SetDebouncePeriod(10000)
            brickletIndustrialDigitalIn4.SetInterrupt(15)
            AddHandler brickletIndustrialDigitalIn4.Interrupt, AddressOf InterruptCB
            System.Console.WriteLine("Industrial Digital In 4 initialized")
        Catch e As TinkerforgeException
            System.Console.WriteLine("Industrial Digital In 4 init failed: " + e.Message)
            brickletIndustrialDigitalIn4 = Nothing
        End Try
    End If

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/vbnet/SmokeDetector.vb>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/vbnet/SmokeDetector.vb
 :language: vbnet
 :tab-width: 4
