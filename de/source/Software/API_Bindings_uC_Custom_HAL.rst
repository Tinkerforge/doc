
.. _api_bindings_uc_custom_hal:

C/C++ für Mikrocontroller - Eigener HAL
=======================================

Um die C/C++ für Mikrocontroller verwenden zu können
ist ein hardware-spezifischer HAL notwendig.
Falls für die Zielplattform kein HAL verfügbar ist,
kann mittels dieser Anleitung ein eigener geschrieben werden.

.. note::
  Falls Du einen HAL für eine neue Hardware-Plattform geschrieben hast
  und es möglich ist diesen unter der CC0-Lizenz zu veröffentlichen,
  bitten wir um eine Mail an info@tinkerforge.com. Wir haben immer
  Interesse daran, HALs für weitere Plattformen in die Bindings aufzunehmen.

Hardware-Anforderungen
----------------------

Um die Bindings auszuführen, wird ein Mikrocontroller benötigt,
der in etwa vergleichbar zum, oder besser als der ATmega328 ist.
Der Bindings-Code benötigt mindestens 2k RAM und 16k Flash. Außerdem
muss die Host-Hardware SPI mit mindestens 400 kHz kommunizieren können.
Für maximale Performance wird eine SPI-Taktfrequenz von 2 MHz empfohlen.

Übersicht
---------

Ein HAL ist für die Initialisierung und Kontrolle der SPI-Hardware
der Zielplattform verantwortlich. Außerdem abstrahiert er andere hardwarespezifische
Funktionen wie Zeitmessung und Logging.

Um einen HAL zu implementieren müssen die folgenden Schritte durchgeführt werden:

* Definition der ``TF_HAL``- und ``TF_Port``-Strukturen
* Implementierung der ``tf_hal_create`` und ``tf_hal_destroy``-Funktionen für die definierte Struktur
* Implementierung der notwendigen HAL-Funktionen

Die folgenden Funktionen aus :file:`bindings/hal_common.h` werden verwendet:

.. c:function:: int tf_hal_common_create(TF_HAL *hal)

 Initialisiert die ``TF_HALCommon``-Instanz die zum übergebenen ``TF_HAL`` gehört.
 Diese Funktion muss bei der HAL-Initialisierung so früh wie möglich aufgerufen werden.

.. c:function:: int tf_hal_common_prepare(TF_HAL *hal, uint8_t port_count, uint32_t port_discovery_timeout_us)

 Schließt die Initialisierung der ``TF_HALCommon``-Instanz, die zum übergebenen ``TF_HAL`` gehört,
 ab. Das ist typischerweise der letzte Schritt der HAL-Initialisierung. SPI-Kommunikation muss hier bereits
 möglich sein. Diese Funktion erwartet die Anzahl verwendbarer Ports, sowie einen Timeout in Mikrosekunden,
 der angibt, wie lange die Bindings versuchen sollen, ein Gerät an einem der Ports zu erreichen.
 :c:func:`tf_hal_common_prepare` baut dann eine Liste der erreichbaren Geräte und speichert diese in der ``TF_HALCommon``-Instanz.

Definition einer ``TF_HAL``-Struktur
------------------------------------

Die ``TF_HAL``-Struktur hält alle Informationen, die für die SPI-Kommunikation
notwendig sind. Sie speichert außerdem eine Instanz von ``TF_HALCommon``,
einem internen Typen, der pro HAL-Instanz einmal von den Bindings benötigt wird,
sowie einen Pointer auf ein Array von Port-Mapping-Informationen (``TF_Port``).

Die ``TF_Port``-Struktur kann komplett auf den HAL angepasst werden,
um zum Beispiel den Chip-Select-Pin eines Ports, sowie dessen Namen, zu verwendende
SPI-Einheit usw. abzuspeichern. Beispiele finden sich in :file:`hal_arduino_esp32/hal_arduino_esp32.h`
und :file:`hal_linux/hal_linux.h`.

Bricklets werden anhand ihrer UID und des Ports unter dem sie erreichbar sind identifiziert.
Ein Port mappt typischerweise auf den Chip-Select-Pin der gesetzt werden muss, damit Daten über SPI
an das Bricklet übertragen werden. Manche HAL-Funktionen bekommen eine Port-ID übergeben.
Diese ist typischerweise der Index in ein ``TF_Port``-Array.


Implemetierung der ``tf_hal_create`` und ``tf_hal_destroy``-Funktionen
----------------------------------------------------------------------

Nachdem die ``TF_HAL``-Funktion definiert wurde, muss deren Initialisierungsfunktion
``tf_hal_create`` implementiert werden. Sie hat folgende Aufgaben:

* Die ``TF_HAL``-Struktur in einen definierten Zustand bringen

* Die ``TF_HALCommon``-Instanz mit :c:func:`tf_hal_common_create` initialisieren

* Vorbereiten der SPI-Kommunikation
  Wenn die Initialisierungs-Funktion beendet ist, muss die SPI-Kommunikation mit allen angeschlossenen
  Geräten möglich sein. Alle Chip-Select-Pins müssen auf HIGH (also deaktiviert) stehen.
  :ref:`Siehe hier <api_bindings_uc_custom_hal_spi_details>` für Details über die SPI-Kommunikation.

* Aufrufen von :c:func:`tf_hal_common_prepare`
  Das ist typischerweise der letzte Initialisierungsschritt. SPI-Kommunikation muss hier möglich sein.

Nach Konvention gibt ``tf_hal_create`` einen int zurück, der bei Erfolg auf ``TF_E_OK``
gesetzt ist. Falls die Initialisierung fehlschlägt, kann ein anderer Fehlercode aus
:file:`bindings/errors.h` zurückgegeben werden. Es ist außerdem möglich eigene Fehlercodes
für den HAL in dessen Header zu definieren. Die Fehlercodes von -99 bis -1 sind allerdings für die
Bindings reserviert. Der erste valide Fehlercode ist also -100.

Nachdem ``tf_hal_create`` implementiert wurde, kann jetzt ``tf_hal_destroy`` implementiert werden.
Es sollte möglich sein, einen HAL mit ``tf_hal_create`` zu erstellen, zu verwenden,
ihn dann mit ``tf_hal_destroy`` zu zerstören und danach mit ``tf_hal_create`` wieder zu erstellen.
Der neu erstellte HAL muss dann wieder funktionsfähig sein.

Implementierung der benötigten HAL-Funktionen
---------------------------------------------

Als letzter Schritt müssen die folgenden Funktionen implementiert werden,
die in :file:`bindings/hal_common.h` zwischen
``// BEGIN - To be implemented by the specific HAL``
und
``// END - To be implemented by the specific HAL``
definiert sind.
Alle Funktionen, die einen int zurückgeben, sollten ``TF_E_OK`` zurückgeben, wenn
kein Fehler aufgetreten ist.

.. c:function:: int tf_hal_chip_select(TF_HAL *hal, uint8_t port_id, bool enable)

 Wenn ``enable`` true ist, wählt diese Funktion den Port mit der übergebenen ID für die folgende
 SPI-Kommunikation aus. Wenn ``enable`` false ist, wird der Port nicht mehr ausgewählt.

 .. note:
  ``enable`` ist true wenn der Chip-Select-Pin des Ports auf LOW gesetzt werden soll.
  :ref:`Siehe hier <api_bindings_uc_custom_hal_spi_details>` für Details über die SPI-Kommunikation.

 Abhängig von der Plattform müssen hier mehrere Schritte durchgeführt werden.
 Zum Beispiel muss auf einem Arduino ``begin/endTransaction`` aufgerufen werden
 um sicherzustellen, dass die SPI-Konfiguration angewendet wird.

 Die Bindings stellen sicher, dass immer nur ein Port gleichzeitig ausgewählt wird.

.. c:function:: int tf_hal_transceive(TF_HAL *hal, uint8_t port_id, const uint8_t *write_buffer, uint8_t *read_buffer, uint32_t length)

 Überträgt ``length`` Bytes an Daten aus dem ``write_buffer`` zum Bricklet und empfängt währenddessen
 die selbe Menge an Bytes vom Bricklet in den ``read_buffer`` (da SPI bidirektional ist). Die übergebenen
 Buffer sind immer groß genug um ``length`` Bytes zu lesen oder zu schreiben.

 Diese Funktion wird nur aufgerufen, wenn zuvor :c:func:`tf_hal_chip_select` mit der selben Port-ID
 und ``enable=true`` aufgerufen wurde.

 Falls die Zielplattform DMA unterstützt, kann hier ein Transfer initiiert werden, es muss aber blockiert
 werden bis die Daten übertragen wurden.

 Falls die Zielplattform kooperatives Multitasking unterstützt, kann, nachdem ein Transfer initiiert wurde,
 ``yield`` o.Ä. aufgerufen werden. Um sicherzustellen, dass während die Bindings während des Transfers nicht
 verwendet werden, sollten sie wie folgt gesperrt werden:

 .. code-block:: c

  TF_HALCommon *common = tf_hal_get_common(hal);
  common->locked = true

 Nachdem der Transfer abgeschlossen ist, sollten die Bindings wieder entsperrt werden, damit sie weiter
 verwendet werden können.

 .. note:
  Wenn nur ein Byte übertragen wird, sollte auch bei Einsatz von DMA nicht ``yield`` o.Ä. aufgerufen werden,
  da Ein-Byte-Transfers typischerweise von der Callback-Poll-Logik ausgeführt werden. Damit ein Pollen
  nach Callbacks mit Timeout 0 möglichst schnell ist sollte hier auf das ``yield`` verzichtet werden.
  Falls ein größerer Timeout verwendet wird, wird ``tf_hal_callback_tick`` nach dem Pollen :c:func:`tf_hal_sleep_us`
  aufrufen. Dort kann dann ``yield`` aufgerufen werden.

.. c:function:: uint32_t tf_hal_current_time_us(TF_HAL *hal)

 Gibt die aktuelle Zeit in Mikrosekunden zurück. Diese Zeit muss keine Relation zu einer "echten" Zeit haben,
 aber monoton außer bei Überläufen sein.

.. c:function:: void tf_hal_sleep_us(TF_HAL *hal, uint32_t us)

 Blockiert für die übergebene Zeit in Mikrosekunden. Falls die Plattform kooperatives
 Multitasking unterstützt, können die Bindings hier gesperrt und danach durch ``yield``
 pausiert werden. Siehe :c:func:`tf_hal_transceive` für Details.

 .. note:
  Die Zeit muss nur ungefähr eingehalten werden, falls deutlich länger als die übergebene Zeit
  blockiert wird, kann die Performance allerdings schlechter ausfallen.

.. c:function:: TF_HALCommon *tf_hal_get_common(TF_HAL *hal)

 Gibt die ``TF_HALCommon``-Instanz zurück, die zum übergebenen ``TF_HAL`` gehört.

.. c:function:: char tf_hal_get_port_name(TF_HAL *hal, uint8_t port_id)

 Gibt den Port-Namen (typischerweise ein Buchstabe zwischen 'A' and 'Z') für die übergebene Port-ID zurück.
 Der Name wird in ``get_identity``-Rückgaben eingefügt, falls das Gerät direkt mit dem Host
 verbunden ist.

.. c:function:: void tf_hal_log_message(const char *msg, size_t len)

 Loggt die übergebene Nachricht. Die Nachricht hat eine Länge von ``len`` und ist **nicht** null-terminiert.
 Abhängig von der Plattform kann hier z.B. eine serielle Konsole (Arduino) oder die Standardausgabe (Linux)
 verwendet werden. Es kann auch in eine Log-Datei geschrieben werden.

 .. note:
  Diese Funktion darf nicht annehmen, dass die HAL-Initialisierung erfolgreich war,
  damit auch Fehler die während dieser auftreten geloggt werden können.

.. c:function:: void tf_hal_log_newline()

 Loggt das/die plattformspezifischen Zeilenumbruchszeichen.

.. c:function:: const char *tf_hal_strerror(int e_code)

 Gibt eine Fehlerbeschreibung für den übergebenen Fehlercode zurück.
 Um so platzeffizient wie möglich zu sein, kann diese Funktion komplett entfernt werden,
 falls ``TF_IMPLEMENT_STRERROR`` nicht in :file:`bindings/config.h` definiert ist.

 Fehlercodes die von den Bindings verwendet werden können durch Einbinden von :file:`bindings/error_cases.h`
 behandelt werden.

 Zur Implementierung kann die folgende Vorlage verwendet werden:

 .. code-block:: c

  #ifdef TF_IMPLEMENT_STRERROR
  const char *tf_hal_strerror(int e_code) {
      switch(e_code) {
          #include "../bindings/error_cases.h"
          /* Add HAL specific error codes here, for example:
          case TF_E_OPEN_GPIO_FAILED:
              return "failed to open GPIO";
          */
          default:
              return "unknown error";
      }
  }
  #endif

.. _api_bindings_uc_custom_hal_spi_details:

Details über die SPI-Kommunikation
----------------------------------

Die Kommunikation zwischen dem Host und den Bricks/Bricklets verwendet SPI Modus 3:

 * CPOL=1: Clock-Polarität ist invertiert, HIGH wenn inaktiv
 * CPHA=1: Clock-Phase ist verschoben: Daten werden zur fallenden Taktflanke gelesen

Daten werden mit dem MSB (most significant bit) zuerst übertragen.
Die Standardtaktfrequenz ist 1,4 MHz, Bricks und Bricklets unterstützen aber
Taktfrequenzen zwischen 400 kHz und 2 MHz. Der Logikpegel aller Signale beträgt 3,3V.

Aufgrund eines Bugs des auf den Bricklets verwendeten XMC-Mikrocontrollers von
Infineon trennt das Bricklets sich nicht korrekt vom SPI-Bus, wenn das
Chip-Select-Signal deaktiviert wird. Es treibt dann weiterhin auf MISO einen
Wert, was dazu führt, dass sich mehrere Bricklets am selben SPI-Bus gegenseitig
stören. Falls mehrere Bricklets eingesetzt werden sollen, müssen deshalb vom
Chip-Select-Signal kontrollierte Trenner-Chips eingesetzt werden.
