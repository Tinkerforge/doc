
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Readout Smoke Detectors using C

.. |ref_CALLBACK_ENUMERATE| replace:: :c:data:`IPCON_CALLBACK_ENUMERATE`
.. |ref_CALLBACK_CONNECTED| replace:: :c:data:`IPCON_CALLBACK_CONNECTED`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :c:func:`ipcon_enumerate <ipcon_enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``IPCON_ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``IPCON_ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``cb_voltage_reached``

.. include:: SmokeDetector_C.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_c:

Read out Smoke Detectors using C
================================

.. include:: CCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_C.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_C.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: c

    #define HOST "localhost"
    #define PORT 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: c

    typedef struct {
        IPConnection ipcon;
    } SmokeDetector;

    int main() {
        SmokeDetector sd;
        ipcon_create(&ws.ipcon);
        ipcon_connect(&ws.ipcon, HOST, PORT);

        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&ws);
        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&ws);

        ipcon_enumerate(&ws.ipcon);
        return 0;
    }

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: c

    void cb_connected(uint8_t connected_reason, void *user_data) {
        SmokeDetector *sd = (SmokeDetector *)user_data;

        if(connected_reason == IPCON_CONNECT_REASON_AUTO_RECONNECT) {
            ipcon_enumerate(&sd->ipcon);
        }
    }

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: c

    typedef struct {
        IPConnection ipcon;
    } SmokeDetector;

    void cb_connected(uint8_t connected_reason, void *user_data) {
        SmokeDetector *sd = (SmokeDetector *)user_data;

        if(connected_reason == IPCON_CONNECT_REASON_AUTO_RECONNECT) {
            ipcon_enumerate(&sd->ipcon);
        }
    }

    int main() {
        SmokeDetector sd;
        ipcon_create(&sd.ipcon);
        ipcon_connect(&sd.ipcon, HOST, PORT);

        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&sd);
        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&sd);

        ipcon_enumerate(&sd.ipcon);
        return 0;
    }


Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: c

    void cb_enumerate(const char *uid, const char *connected_uid,
                      char position, uint8_t hardware_version[3],
                      uint8_t firmware_version[3], uint16_t device_identifier,
                      uint8_t enumeration_type, void *user_data) {
        SmokeDetector *sd = (SmokeDetector*)user_data;

        if(enumeration_type == IPCON_ENUMERATION_TYPE_CONNECTED ||
           enumeration_type == IPCON_ENUMERATION_TYPE_AVAILABLE) {

|step2_config1|

.. code-block:: c

    if(device_identifier == ANALOG_IN_DEVICE_IDENTIFIER) {
        analog_in_create(&sd->analog_in, uid, &sd->ipcon);
        analog_in_set_range(&sd->analog_in, 1);
        analog_in_set_debounce_period(&sd->analog_in, 10000);
        analog_in_register_callback(&sd->analog_in,
                                    ANALOG_IN_CALLBACK_VOLTAGE_REACHED,
                                    (void *)cb_voltage_reached,
                                    (void *)sd);
        analog_in_set_voltage_callback_threshold(&sd->analog_in, '>', 1200, 0);
    }

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: c

    void cb_enumerate(const char *uid, const char *connected_uid,
                      char position, uint8_t hardware_version[3],
                      uint8_t firmware_version[3], uint16_t device_identifier,
                      uint8_t enumeration_type, void *user_data) {
        SmokeDetector *sd = (SmokeDetector*)user_data;

        if(enumeration_type == IPCON_ENUMERATION_TYPE_CONNECTED ||
           enumeration_type == IPCON_ENUMERATION_TYPE_AVAILABLE) {
            if(device_identifier == ANALOG_IN_DEVICE_IDENTIFIER) {
                analog_in_create(&sd->analog_in, uid, &sd->ipcon);
                analog_in_set_range(&sd->analog_in, 1);
                analog_in_set_debounce_period(&sd->analog_in, 10000);
                analog_in_register_callback(&sd->analog_in,
                                            ANALOG_IN_CALLBACK_VOLTAGE_REACHED,
                                            (void *)cb_voltage_reached,
                                            (void *)sd);
                analog_in_set_voltage_callback_threshold(&sd->analog_in, '>', 1200, 0);
            }
        }
    }


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: c

    void cb_voltage_reached(uint16_t voltage, void *user_data) {
        printf("Fire! Fire!\n");
    }

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: c

    while(true) {
        int rc = ipcon_connect(&ws.ipcon, HOST, PORT);
        if(rc < 0) {
            fprintf(stderr, "Could not connect to brickd: %d\n", rc);
            // TODO: sleep 1s
            continue;
        }
        break;
    }

|step4_intro2|

.. code-block:: c

    while(true) {
        int rc = ipcon_enumerate(&ws.ipcon);
        if(rc < 0) {
            fprintf(stderr, "Could not enumerate: %d\n", rc);
            // TODO: sleep 1s
            continue;
        }
        break;
    }

|step4_sleep_in_c|

|step4_connect_afterwards|

|step4_initialization|

.. code-block:: c

    if(device_identifier == ANALOG_IN_DEVICE_IDENTIFIER) {
        analog_in_create(&sd->analog_in, uid, &sd->ipcon);
        analog_in_set_range(&sd->analog_in, 1);
        analog_in_set_debounce_period(&sd->analog_in, 10000);
        analog_in_register_callback(&sd->analog_in,
                                    ANALOG_IN_CALLBACK_VOLTAGE_REACHED,
                                    (void *)cb_voltage_reached,
                                    (void *)sd);

        int rc = analog_in_set_voltage_callback_threshold(&sd->analog_in, '>', 1200, 0);
        if(rc < 0) {
            fprintf(stderr, "Analog In init failed: %d\n", rc);
        } else {
            printf("Analog In initialized\n");
        }
    }

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/c/smoke_detector.c>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/c/smoke_detector.c
 :language: c
 :tab-width: 4
