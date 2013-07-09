
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Rauchmelder mit Python auslesen

.. |ref_CALLBACK_ENUMERATE| replace:: :py:attr:`CALLBACK_ENUMERATE <IPConnection.CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :py:attr:`CALLBACK_CONNECTED <IPConnection.CALLBACK_CONNECTED>`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :py:func:`enumerate() <IPConnection.enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_interrupt| replace:: ``cb_interrupt``
.. |value_mask| replace:: ``value_mask``

.. include:: SmokeDetector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_python:

Rauchmelder mit Python auslesen
===============================

.. include:: PythonCommon.substitutions
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


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:

|step2_config|

.. code-block:: python

    if device_identifier == IndustrialDigitalIn4.DEVICE_IDENTIFIER:
        self.idi4 = IndustrialDigitalIn4(uid, self.ipcon)
        self.idi4.set_debounce_period(10000)
        self.idi4.set_interrupt(15)
        self.idi4.register_callback(IndustrialDigitalIn4.CALLBACK_INTERRUPT,
                                    self.cb_interrupt)

|step2_put_together|

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
            if device_identifier == IndustrialDigitalIn4.DEVICE_IDENTIFIER:
                self.idi4 = IndustrialDigitalIn4(uid, self.ipcon)
                self.idi4.set_debounce_period(10000)
                self.idi4.set_interrupt(15)
                self.idi4.register_callback(IndustrialDigitalIn4.CALLBACK_INTERRUPT,
                                            self.cb_interrupt)


Schritt 3: Auf Alarmsignal reagieren
------------------------------------

|step3_intro|

.. code-block:: python

    def cb_interrupt(self, interrupt_mask, value_mask):
        if value_mask > 0:
            log.warn('Fire! Fire!')

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

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

    if device_identifier == IndustrialDigitalIn4.DEVICE_IDENTIFIER:
        try:
            self.idi4 = IndustrialDigitalIn4(uid, self.ipcon)
            self.idi4.set_debounce_period(10000)
            self.idi4.set_interrupt(15)
            self.idi4.register_callback(IndustrialDigitalIn4.CALLBACK_INTERRUPT,
                                        self.cb_interrupt)
            log.info('Industrial Digital In 4 initialized')
        except Error as e:
            log.error('Industrial Digital In 4 init failed: ' + str(e.description))
            self.idi4 = None

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/python/smoke_detector.py>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/python/smoke_detector.py
 :language: python
 :tab-width: 4
