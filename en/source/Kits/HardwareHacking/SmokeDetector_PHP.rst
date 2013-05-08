
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Readout Smoke Detectors using PHP

.. |ref_CALLBACK_ENUMERATE| replace:: :php:member:`CALLBACK_ENUMERATE <IPConnection::CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :php:member:`CALLBACK_CONNECTED <IPConnection::CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :php:func:`enumerate <IPConnection::enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``voltageReachedCB``

.. include:: SmokeDetector_PHP.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_php:

Readout Smoke Detectors using PHP
=================================

.. include:: PHPCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_PHP.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_PHP.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: php

    <?php

    const HOST = 'localhost';
    const PORT = 4223;

    ?>

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: php

    <?php

    public function __construct()
    {
        $this->ipcon = new IPConnection();
        $this->ipcon->connect(self::HOST, self::PORT);

        $this->ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE,
                                       array($this, 'enumerateCB'));
        $this->ipcon->registerCallback(IPConnection::CALLBACK_CONNECTED,
                                       array($this, 'connectedCB'));

        $this->ipcon->enumerate();
    }

    ?>

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: php

    <?php

    function connectedCB($connectedReason)
    {
        if($connectedReason == IPConnection::CONNECT_REASON_AUTO_RECONNECT) {
            $this->ipcon->enumerate();
        }
    }

    ?>

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: php

    <?php

    class SmokeDetector
    {
        const HOST = 'localhost';
        const PORT = 4223;

        public function __construct()
        {
            $this->ipcon = new IPConnection();
            $this->ipcon->connect(self::HOST, self::PORT);

            $this->ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE,
                                           array($this, 'enumerateCB'));
            $this->ipcon->registerCallback(IPConnection::CALLBACK_CONNECTED,
                                           array($this, 'connectedCB'));

            $this->ipcon->enumerate();
        }

        function connectedCB($connectedReason)
        {
            if($connectedReason == IPConnection::CONNECT_REASON_AUTO_RECONNECT) {
                $this->ipcon->enumerate();
            }
        }
    }

    ?>


Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: php

    <?php

    function enumerateCB($uid, $connectedUid, $position, $hardwareVersion,
                         $firmwareVersion, $deviceIdentifier, $enumerationType)
    {
        if($enumerationType == IPConnection::ENUMERATION_TYPE_CONNECTED ||
           $enumerationType == IPConnection::ENUMERATION_TYPE_AVAILABLE) {

    ?>

|step2_config1|

.. code-block:: php

    <?php

    if($deviceIdentifier == BrickletAnalogIn::DEVICE_IDENTIFIER) {
        $this->brickletAnalogIn = new BrickletAnalogIn($uid, $this->ipcon);
        $this->brickletAnalogIn->setRange(1);
        $this->brickletAnalogIn->setDebouncePeriod(10000);
        $this->brickletAnalogIn->setVoltageCallbackThreshold('>', 1200, 0);
        $this->brickletAnalogIn->registerCallback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED,
                                                  array($this, 'voltageReachedCB'));
    }

    ?>

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: php

    <?php

    function enumerateCB($uid, $connectedUid, $position, $hardwareVersion,
                         $firmwareVersion, $deviceIdentifier, $enumerationType)
    {
        if($deviceIdentifier == BrickletAnalogIn::DEVICE_IDENTIFIER) {
            $this->brickletAnalogIn = new BrickletAnalogIn($uid, $this->ipcon);
            $this->brickletAnalogIn->setRange(1);
            $this->brickletAnalogIn->setDebouncePeriod(10000);
            $this->brickletAnalogIn->setVoltageCallbackThreshold('>', 1200, 0);
            $this->brickletAnalogIn->registerCallback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED,
                                                      array($this, 'voltageReachedCB'));
        }
    }

    ?>


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: php

    <?php

    function voltageReachedCB($voltage)
    {
        echo "Fire! Fire!\n";
    }

    ?>

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: php

    <?php

    while(true) {
        try {
            $this->ipcon->connect(self::HOST, self::PORT);
            break;
        } catch(Exception $e) {
            sleep(1);
        }
    }

    ?>

|step4_intro2|

.. code-block:: php

    <?php

    while(true) {
        try {
            $this->ipcon->enumerate();
            break;
        } catch(Exception $e) {
            sleep(1);
        }
    }

    ?>

|step4_connect_afterwards|

|step4_initialization|

.. code-block:: php

    <?php

    if($deviceIdentifier == BrickletAnalogIn::DEVICE_IDENTIFIER) {
        try {
            $this->brickletAnalogIn = new BrickletAnalogIn($uid, $this->ipcon);
            $this->brickletAnalogIn->setRange(1);
            $this->brickletAnalogIn->setDebouncePeriod(10000);
            $this->brickletAnalogIn->setVoltageCallbackThreshold('>', 1200, 0);
            $this->brickletAnalogIn->registerCallback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED,
                                                      array($this, 'voltageReachedCB'));
            echo "Analog In initialized\n";
        } catch(Exception $e) {
            $this->brickletAnalogIn = null;
            echo "Analog In init failed: $e\n";
        }
    }

    ?>

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/php/SmokeDetector.php>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/php/SmokeDetector.php
 :language: php
 :tab-width: 4
