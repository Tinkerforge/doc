
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Read out Smoke Detectors using Java

.. |ref_CALLBACK_ENUMERATE| replace:: :java:func:`EnumerateListener <IPConnection.EnumerateListener>`
.. |ref_CALLBACK_CONNECTED| replace:: :java:func:`ConnectedListener <IPConnection.ConnectedListener>`
.. |callback| replace:: listener
.. |ref_enumerate| replace:: :java:func:`enumerate() <IPConnection::enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``voltageReached``

.. include:: SmokeDetector_Java.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_java:

Read out Smoke Detectors using Java
===================================

.. include:: JavaCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_Java.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_Java.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


.. _starter_kit_hardware_hacking_smoke_detector_java_step1:

Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: java

    private static final String host = "localhost";
    private static final int port = 4223;

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: java

    public static void main(String args[]) {
        ipcon = new IPConnection();
        ipcon.connect(host, port);

        smokeListener = new SmokeListener(ipcon);
        ipcon.addEnumerateListener(smokeListener);
        ipcon.addConnectedListener(smokeListener);

        ipcon.enumerate();
    }

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: java

    class SmokeListener implements IPConnection.EnumerateListener,
                                   IPConnection.ConnectedListener {
        public void connected(short connectedReason) {
            if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT) {
                ipcon.enumerate();
            }
        }
    }

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: java

    class SmokeListener implements IPConnection.EnumerateListener,
                                   IPConnection.ConnectedListener {
        private IPConnection ipcon = null;

        public SmokeListener(IPConnection ipcon) {
            this.ipcon = ipcon;
        }

        public void connected(short connectedReason) {
            if(connectedReason == IPConnection.CONNECT_REASON_AUTO_RECONNECT) {
                ipcon.enumerate();
            }
        }
    }

    public class SmokeDetector {
        private static final String host = "localhost";
        private static final int port = 4223;
        private static IPConnection ipcon = null;
        private static SmokeListener smokeListener = null;

        public static void main(String args[]) {
            ipcon = new IPConnection();
            ipcon.connect(host, port);

            smokeListener = new SmokeListener(ipcon);
            ipcon.addEnumerateListener(smokeListener);
            ipcon.addConnectedListener(smokeListener);

            ipcon.enumerate();
        }
    }

Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: java

    public void enumerate(String uid, String connectedUid, char position,
                          short[] hardwareVersion, short[] firmwareVersion,
                          int deviceIdentifier, short enumerationType) {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE) {

|step2_config1|

.. code-block:: java

    if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER) {
        brickletAnalogIn = new BrickletAnalogIn(uid, ipcon);
        brickletAnalogIn.setRange((short)1);
        brickletAnalogIn.setDebouncePeriod(10000);
        brickletAnalogIn.setVoltageCallbackThreshold('>', (short)1200, (short)0);
        brickletAnalogIn.addVoltageReachedListener(this);
    }

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: java

    public void enumerate(String uid, String connectedUid, char position,
                          short[] hardwareVersion, short[] firmwareVersion,
                          int deviceIdentifier, short enumerationType) {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE) {
            if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER) {
                brickletAnalogIn = new BrickletAnalogIn(uid, ipcon);
                brickletAnalogIn.setRange((short)1);
                brickletAnalogIn.setDebouncePeriod(10000);
                brickletAnalogIn.setVoltageCallbackThreshold('>', (short)1200, (short)0);
                brickletAnalogIn.addVoltageReachedListener(this);
            }
        }
    }


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: java

    public void voltageReached(int illuminance) {
        System.out.println("Fire! Fire!");
    }

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


.. _starter_kit_hardware_hacking_smoke_detector_java_step4:

Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: java

    while(true) {
        try {
            ipcon.connect(host, port);
            break;
        } catch(java.net.UnknownHostException e) {
        } catch(java.io.IOException e) {
        } catch(com.tinkerforge.AlreadyConnectedException e) {
        }

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ei) {
        }
    }

|step4_intro2|

.. code-block:: java

    while(true) {
        try {
            ipcon.enumerate();
            break;
        } catch(com.tinkerforge.NotConnectedException e) {
        }

        try {
            Thread.sleep(1000);
        } catch(InterruptedException ei) {
        }
    }

|step4_connect_afterwards|

|step4_initialization|

.. code-block:: java

    if(deviceIdentifier == BrickletAnalogIn.DEVICE_IDENTIFIER) {
        try {
            brickletAnalogIn = new BrickletAnalogIn(uid, ipcon);
            brickletAnalogIn.setRange((short)1);
            brickletAnalogIn.setDebouncePeriod(10000);
            brickletAnalogIn.setVoltageCallbackThreshold('>', (short)1200, (short)0);
            brickletAnalogIn.addVoltageReachedListener(this);
            System.out.println("Analog In initialized");
        } catch(com.tinkerforge.TinkerforgeException e) {
            brickletAnalogIn = null;
            System.out.println("Analog In init failed: " + e);
        }
    }

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/java/SmokeDetector.java>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/java/SmokeDetector.java
 :language: java
 :tab-width: 4
