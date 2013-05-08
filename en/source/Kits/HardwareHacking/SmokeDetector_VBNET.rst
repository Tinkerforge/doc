
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Readout Smoke Detectors using Visual Basic .NET

.. |ref_CALLBACK_ENUMERATE| replace:: :vbnet:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_CALLBACK_CONNECTED| replace:: :vbnet:func:`Connected <IPConnection::Connected>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :vbnet:func:`Enumerate <IPConnection::Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``VoltageReachedCB``

.. include:: SmokeDetector_VBNET.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_vbnet:

Readout Smoke Detectors using Visual Basic .NET
===============================================

.. include:: VBNETCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_VBNET.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_VBNET.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

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


Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: vbnet

    Sub EnumerateCB(ByVal sender As IPConnection, ByVal uid As String, _
                    ByVal connectedUid As String, ByVal position As Char, _
                    ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, _
                    ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)
        If enumerationType = IPConnection.ENUMERATION_TYPE_CONNECTED Or _
           enumerationType = IPConnection.ENUMERATION_TYPE_AVAILABLE Then

|step2_config1|

.. code-block:: vbnet

    If deviceIdentifier = BrickletAnalogIn.DEVICE_IDENTIFIER Then
        brickletAnalogIn = New BrickletAnalogIn(UID, ipcon)
        brickletAnalogIn.SetRange(1)
        brickletAnalogIn.SetDebouncePeriod(10000)
        brickletAnalogIn.SetVoltageCallbackThreshold(">"C, 1200, 0)
        AddHandler brickletAnalogIn.VoltageReached, AddressOf VoltageReachedCB
    End If

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: vbnet

    Sub EnumerateCB(ByVal sender As IPConnection, ByVal uid As String, _
                    ByVal connectedUid As String, ByVal position As Char, _
                    ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, _
                    ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)
        If enumerationType = IPConnection.ENUMERATION_TYPE_CONNECTED Or _
           enumerationType = IPConnection.ENUMERATION_TYPE_AVAILABLE Then
            If deviceIdentifier = BrickletAnalogIn.DEVICE_IDENTIFIER Then
                brickletAnalogIn = New BrickletAnalogIn(UID, ipcon)
                brickletAnalogIn.SetRange(1)
                brickletAnalogIn.SetDebouncePeriod(10000)
                brickletAnalogIn.SetVoltageCallbackThreshold(">"C, 1200, 0)
                AddHandler brickletAnalogIn.VoltageReached, AddressOf VoltageReachedCB
            End If
        End If
    End Sub


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: vbnet

    Sub VoltageReachedCB(ByVal sender As BrickletAnalogIn, ByVal voltage As Integer)
        System.Console.WriteLine("Fire! Fire!")
    End Sub

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

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

    If deviceIdentifier = BrickletAnalogIn.DEVICE_IDENTIFIER Then
        Try
            brickletAnalogIn = New BrickletAnalogIn(UID, ipcon)
            brickletAnalogIn.SetRange(1)
            brickletAnalogIn.SetDebouncePeriod(10000)
            brickletAnalogIn.SetVoltageCallbackThreshold(">"C, 1200, 0)
            AddHandler brickletAnalogIn.VoltageReached, AddressOf VoltageReachedCB
            System.Console.WriteLine("Analog In initialized")
        Catch e As TinkerforgeException
            System.Console.WriteLine("Analog In init failed: " + e.Message)
            brickletAnalogIn = Nothing
        End Try
    End If

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/vbnet/SmokeDetector.vb>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/vbnet/SmokeDetector.vb
 :language: vbnet
 :tab-width: 4
