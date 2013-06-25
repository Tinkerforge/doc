
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Readout Smoke Detectors using C#

.. |ref_CALLBACK_ENUMERATE| replace:: :csharp:func:`EnumerateCallback <IPConnection::EnumerateCallback>`
.. |ref_CALLBACK_CONNECTED| replace:: :csharp:func:`Connected <IPConnection::Connected>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :csharp:func:`Enumerate() <IPConnection::Enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``VoltageReachedCB``

.. include:: SmokeDetector_CSharp.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_csharp:

Read out Smoke Detectors using C#
=================================

.. include:: CSharpCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_CSharp.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_CSharp.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


.. _starter_kit_hardware_hacking_smoke_detector_csharp_step1:

Step 1: Discover Bricks and Bricklets
-------------------------------------

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

    class SmokeDetector
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


.. _starter_kit_hardware_hacking_smoke_detector_csharp_step2:

Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: csharp

    static void EnumerateCB(IPConnection sender, string UID, string connectedUID, char position,
                            short[] hardwareVersion, short[] firmwareVersion,
                            int deviceIdentifier, short enumerationType)
    {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)

|step2_config1|

.. code-block:: csharp

    if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER)
    {
        brickletAnalogIn = new BrickletAnalogIn(UID, ipcon);
        brickletAnalogIn.SetRange(1);
        brickletAnalogIn.SetDebouncePeriod(10000);
        brickletAnalogIn.SetVoltageCallbackThreshold('>', 1200, 0);
        brickletAnalogIn.VoltageReached += VoltageReachedCB;
    }

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: csharp

    static void EnumerateCB(IPConnection sender, string UID, string connectedUID, char position,
                            short[] hardwareVersion, short[] firmwareVersion,
                            int deviceIdentifier, short enumerationType)
    {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)
        {
            if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER)
            {
                brickletAnalogIn = new BrickletAnalogIn(UID, ipcon);
                brickletAnalogIn.SetRange(1);
                brickletAnalogIn.SetDebouncePeriod(10000);
                brickletAnalogIn.SetVoltageCallbackThreshold('>', 1200, 0);
                brickletAnalogIn.VoltageReached += VoltageReachedCB;
            }
        }
    }


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: csharp

    static void VoltageReachedCB(BrickletAnalogIn sender, int voltage)
    {
        System.Console.WriteLine("Fire! Fire!");
    }

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


.. _starter_kit_hardware_hacking_smoke_detector_csharp_step4:

Step 4: Error handling and Logging
----------------------------------

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

|step4_initialization|

.. code-block:: csharp

    if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER)
    {
        try
        {
            brickletAnalogIn = new BrickletAnalogIn(UID, ipcon);
            brickletAnalogIn.SetRange(1);
            brickletAnalogIn.SetDebouncePeriod(10000);
            brickletAnalogIn.SetVoltageCallbackThreshold('>', 1200, 0);
            brickletAnalogIn.VoltageReached += VoltageReachedCB;
            System.Console.WriteLine("Analog In initialized");
        }
        catch(TinkerforgeException e)
        {
            System.Console.WriteLine("Analog In init failed: " + e.Message);
            brickletAnalogIn = null;
        }
    }

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/csharp/SmokeDetector.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/csharp/SmokeDetector.cs
 :language: csharp
 :tab-width: 4
