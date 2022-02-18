.. cpp:function:: void tf_hal_set_timeout(TF_HAL *hal, uint32_t timeout_us)

 Setzt den Timeout in Mikrosekunden für Getter und Setter für die das Response-Expected-Flag
 gesetzt ist.

 Der Standard-Timeout ist 2500000 (2,5 Sekunden).

.. cpp:function:: uint32_t tf_hal_get_timeout(TF_HAL *hal)

 Gibt den Timeout zurück, der von :cpp:func:`tf_hal_set_timeout` gesetzt wurde.

.. cpp:function:: int tf_hal_get_device_info(TF_HAL *hal, size_t index, char ret_uid[7], char *ret_port_name, uint16_t *ret_device_id)

 Gibt die UID, den Port und den :ref:`Device-Identifier <device_identifier>` für das n-te (=index)
 gefundene Gerät zurück. Diese Funktion gibt ``TF_E_DEVICE_NOT_FOUND`` zurück, wenn der index größer
 oder gleich der Anzahl gefundener Geräte ist. Damit alle Geräte aufgelistet werden, kann diese Funktion
 in einer Schleife mit wachsendem index aufgerufen werden, bis einmal ``TF_E_DEVICE_NOT_FOUND`` zurückgegeben wird.

.. cpp:function:: int tf_hal_callback_tick(TF_HAL *hal, uint32_t timeout_us)

 Pollt auf allen Geräten mit registriertem Callback-Handler nach Callbacks. Blockiert für
 die übergebene Zeit in Mikrosekunden.

 Diese Funktion kann nicht-blockierend verwendet werden, indem sie mit einem Timeout von 0 aufgerufen wird.
 Die Bindings pollen dann ein einziges Gerät nach einem Callback, indem sie ein Byte über SPI
 senden und empfangen. Falls kein Callback verfügbar ist, wird die Funktion sofort beendet.
 Wenn das Gerät beginnt ein Callback zu schicken, wird es empfangen, bestätigt und der Callback-Handler
 wird ausgeführt.

 Diese Funktion pollt mit einem Round-Robin-Scheduler über mehrere Aufrufe. Das heißt dass selbst
 wenn immer mit einem Timeout von 0 gepollt wird, alle Geräte so fair wie möglich abgefragt werden.

.. cpp:function:: bool tf_hal_deadline_elapsed(TF_HAL *hal, uint32_t deadline_us)

 Gibt true zurück, wenn die übergebene Deadline in Mikrosekunden abgelaufen ist, ansonsten false.
 Robust gegen Überläufe bis zu ``UINT32_MAX / 2``.

.. cpp:function:: int tf_hal_get_error_counters(TF_HAL *hal, char port_name, uint32_t *ret_spitfp_error_count_checksum, uint32_t *ret_spitfp_error_count_frame, uint32_t *ret_tfp_error_count_frame, uint32_t *ret_tfp_error_count_unexpected)

 Gibt die Fehlerzähler für den übergebenen Port zurück. Folgende Fehler werden gezählt:

 * ``spitfp_error_count_checksum``: Empfangene SPITFP-Pakete die wegen falscher Checksumme ignoriert wurden
 * ``spitfp_error_count_frame``: Empfangene SPITFP-Pakete mit invalider Länge
 * ``tfp_error_count_frame``: Empfangene TFP-Pakete mit invalider Länge
 * ``tfp_error_count_unexpected``: Empfangene TFP-Pakete die unerwartet waren, da sie auf unbekannte Anfragen antworten

.. cpp:function:: void tf_hal_log_error(const char *format, ...)

 Loggt einen Fehler, falls das Log-Level in :file:`bindings/config.h` ``TF_LOG_LEVEL_ERROR`` oder höher ist.
 Unterstützt eine Teilmenge der normalen printf-Syntax. Siehe :cpp:func:`tf_hal_printf` für Details.

.. cpp:function:: void tf_hal_log_info(const char *format, ...)

 Loggt eine Information, falls das Log-Level in :file:`bindings/config.h` ``TF_LOG_LEVEL_INFO`` oder höher ist.
 Unterstützt eine Teilmenge der normalen printf-Syntax. Siehe :cpp:func:`tf_hal_printf` für Details.

.. cpp:function:: void tf_hal_log_debug(const char *format, ...)

 Loggt eine Debug-Meldung, falls das Log-Level in :file:`bindings/config.h` ``TF_LOG_LEVEL_DEBUG`` oder höher ist.
 Unterstützt eine Teilmenge der normalen printf-Syntax. Siehe :cpp:func:`tf_hal_printf` für Details.

.. cpp:function:: void tf_hal_printf(const char *format, ...)

 Diese Funktion ist eine minimalistische printf-Implementierung.
 Die folgenden Platzhalter werden unterstützt:

 * ``%[präfix]u``: Eine vorzeichenlose Ganzzahl in Basis 10
 * ``%[präfix]d``: EIne vorzeichenbehaftete Ganzzahl in Basis 10
 * ``%[präfix]b``: Eine vorzeichenlose Ganzzahl in Basis 2
 * ``%[präfix]x`` and ``%[präfix]X``: Eine vorzeichenlose Ganzzahl in Basis 16, in beiden Fällen mit Kleinbuchstaben.
 * ``%c``: Ein einzelnes Zeichen
 * ``%s``: Ein null-terminierter String
 * ``%%``: Ein Prozentzeichen

 Mit den Präfixen kann die Breite von Ganzzahlen kontrolliert werden.
 Valide Präfixe sind ``I8``, ``I16``, ``I32`` und ``I64``.
 Zum Beispiel kann ``%I16x`` als Platzhalter verwendet werden um eine 16-Bit Zahl hexadezimal auszugeben.

 Padding, gruppierungen, l-Modifikatoren oder ähnliches, oder Floats werden nicht unterstützt.

 Der Zeilenumbruch ``\n`` wird in den oder die plattformspezifischen Zeilenumbruchs-Zeichen übersetzt.

.. cpp:function:: const char *tf_hal_strerror(int e_code)

 Gibt eine Beschreibung für den übergebenen Fehlercode zurück.
