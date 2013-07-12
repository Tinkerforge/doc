
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Rauchmelder mit C auslesen

.. |ref_CALLBACK_ENUMERATE| replace:: :c:data:`IPCON_CALLBACK_ENUMERATE`
.. |ref_CALLBACK_CONNECTED| replace:: :c:data:`IPCON_CALLBACK_CONNECTED`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :c:func:`ipcon_enumerate`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``IPCON_ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``IPCON_ENUMERATION_TYPE_AVAILABLE``
.. |cb_interrupt| replace:: ``cb_interrupt``
.. |value_mask| replace:: ``value_mask``

.. include:: SmokeDetector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_c:

Rauchmelder mit C auslesen
==========================

.. include:: CCommon.substitutions
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
        ipcon_create(&sd.ipcon);
        ipcon_connect(&sd.ipcon, HOST, PORT);

        ipcon_register_callback(&sd.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&sd);
        ipcon_register_callback(&sd.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&sd);

        ipcon_enumerate(&sd.ipcon);
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

        ipcon_register_callback(&sd.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&sd);
        ipcon_register_callback(&sd.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&sd);

        ipcon_enumerate(&sd.ipcon);
        return 0;
    }


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

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

|step2_config|

.. code-block:: c

    if(device_identifier == INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) {
        industrial_digital_in_4_create(&sd->idi4, uid, &sd->ipcon);
        industrial_digital_in_4_set_debounce_period(&sd->idi4, 10000);
        industrial_digital_in_4_register_callback(&sd->idi4,
                                                  INDUSTRIAL_DIGITAL_IN_4_CALLBACK_INTERRUPT,
                                                  (void *)cb_interrupt,
                                                  (void *)sd);
        industrial_digital_in_4_set_interrupt(&sd->idi4, 15);
    }

|step2_put_together|

.. code-block:: c

    void cb_enumerate(const char *uid, const char *connected_uid,
                      char position, uint8_t hardware_version[3],
                      uint8_t firmware_version[3], uint16_t device_identifier,
                      uint8_t enumeration_type, void *user_data) {
        SmokeDetector *sd = (SmokeDetector*)user_data;

        if(enumeration_type == IPCON_ENUMERATION_TYPE_CONNECTED ||
           enumeration_type == IPCON_ENUMERATION_TYPE_AVAILABLE) {
            if(device_identifier == INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) {
                industrial_digital_in_4_create(&sd->idi4, uid, &sd->ipcon);
                industrial_digital_in_4_set_debounce_period(&sd->idi4, 10000);
                industrial_digital_in_4_register_callback(&sd->idi4,
                                                          INDUSTRIAL_DIGITAL_IN_4_CALLBACK_INTERRUPT,
                                                          (void *)cb_interrupt,
                                                          (void *)sd);
                industrial_digital_in_4_set_interrupt(&sd->idi4, 15);
            }
        }
    }


Schritt 3: Auf Alarmsignal reagieren
------------------------------------

|step3_intro|

.. code-block:: c

    void cb_interrupt(uint16_t interrupt_mask, uint16_t value_mask, void *user_data) {
        if(value_mask > 0) {
            printf("Fire! Fire!\n");
        }
    }

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

|step4_intro1|

.. code-block:: c

    while(true) {
        int rc = ipcon_connect(&sd.ipcon, HOST, PORT);
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
        int rc = ipcon_enumerate(&sd.ipcon);
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

    if(device_identifier == INDUSTRIAL_DIGITAL_IN_4_DEVICE_IDENTIFIER) {
        industrial_digital_in_4_create(&sd->idi4, uid, &sd->ipcon);
        industrial_digital_in_4_set_debounce_period(&sd->idi4, 10000);
        industrial_digital_in_4_register_callback(&sd->idi4,
                                                  INDUSTRIAL_DIGITAL_IN_4_CALLBACK_INTERRUPT,
                                                  (void *)cb_interrupt,
                                                  (void *)sd);

        int rc = industrial_digital_in_4_set_interrupt(&sd->idi4, 15);
        if(rc < 0) {
            fprintf(stderr, "Industrial Digital In 4 init failed: %d\n", rc);
        } else {
            printf("Industrial Digital In 4 initialized\n");
        }
    }

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/c/smoke_detector.c>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/c/smoke_detector.c
 :language: c
 :tab-width: 4
