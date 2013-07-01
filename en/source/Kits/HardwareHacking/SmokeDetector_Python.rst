
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Read out Smoke Detectors using Python

.. |ref_CALLBACK_ENUMERATE| replace:: :py:attr:`CALLBACK_ENUMERATE <IPConnection.CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :py:attr:`CALLBACK_CONNECTED <IPConnection.CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :py:func:`enumerate <IPConnection.enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``cb_voltage_reached``

.. include:: SmokeDetector_Python.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_python:

Read out Smoke Detectors with Python
====================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_Python.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_Python.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: python

    HOST = "localhost"
    PORT = 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: python

    def __init__(self):
        self.ipcon = IPConnection()
        self.ipcon.connect(SmokeDetector.HOST, SmokeDetector.PORT)

        self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE,
                                     self.cb_enumerate)
        self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED,
                                     self.cb_connected)

        self.ipcon.enumerate()

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: python

    def cb_connected(self, connected_reason):
        if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
            self.ipcon.enumerate()

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: python

    class SmokeDetector:
        HOST = "localhost"
        PORT = 4223

        def __init__(self):
            self.ipcon = IPConnection()
            self.ipcon.connect(SmokeDetector.HOST, SmokeDetector.PORT)

            self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE,
                                         self.cb_enumerate)
            self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED,
                                         self.cb_connected)

            self.ipcon.enumerate()

        def cb_connected(self, connected_reason):
            if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
                self.ipcon.enumerate()


Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:

|step2_config1|

.. code-block:: python

    if device_identifier == Barometer.DEVICE_IDENTIFIER:
        self.ai = AnalogIn(uid, self.ipcon)
        self.ai.set_range(1)
        self.ai.set_debounce_period(10000)
        self.ai.register_callback(AnalogIn.CALLBACK_VOLTAGE_REACHED,
                                  self.cb_voltage_reached)
        self.ai.set_voltage_callback_threshold('>', 1200, 0)

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
            if device_identifier == Barometer.DEVICE_IDENTIFIER:
                self.ai = AnalogIn(uid, self.ipcon)
                self.ai.set_range(1)
                self.ai.set_debounce_period(10000)
                self.ai.register_callback(AnalogIn.CALLBACK_VOLTAGE_REACHED,
                                          self.cb_voltage_reached)
                self.ai.set_voltage_callback_threshold('>', 1200, 0)


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: python

    def cb_voltage_reached(self, voltage):
        log.warn('Fire! Fire!')

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: python

    while True:
        try:
            self.ipcon.connect(SmokeDetector.HOST, SmokeDetector.PORT)
            break
        except Error as e:
            log.error('Connection Error: ' + str(e.description))
            time.sleep(1)
        except socket.error as e:
            log.error('Socket error: ' + str(e))
            time.sleep(1)

|step4_intro2|

.. code-block:: python

    while True:
        try:
            self.ipcon.enumerate()
            break
        except Error as e:
            log.error('Enumerate Error: ' + str(e.description))
            time.sleep(1)

|step4_connect_afterwards|

|step4_initialization|

.. code-block:: python

    if device_identifier == AnalogIn.DEVICE_IDENTIFIER:
        try:
            self.ai = AnalogIn(uid, self.ipcon)
            self.ai.set_range(1)
            self.ai.set_debounce_period(10000)
            self.ai.register_callback(AnalogIn.CALLBACK_VOLTAGE_REACHED,
                                      self.cb_voltage_reached)
            self.ai.set_voltage_callback_threshold('>', 1200, 0)
            log.info('Analog In initialized')
        except Error as e:
            log.error('Analog In init failed: ' + str(e.description))
            self.ai = None

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/python/smoke_detector.py>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/python/smoke_detector.py
 :language: python
 :tab-width: 4
