
:breadcrumbs: <a href="index.html">Startseite</a> / <a href="index.html#spezifikationen">Spezifikationen</a> / Technische Daten

.. _technical_data:

Technische Daten
================

Diese Seite gibt eine kurze Beschreibung aller Stecker. Weitere Informationen
sind in den Schaltplänen für jedes Produkt und den KiCad Bibliotheken zu finden.


Stapelstecker
-------------

Jeder :ref:`Brick <product_overview_bricks>` hat zwei Arten von Stapelsteckern:

* **Stapeldatenstecker:** Verwendet für den Datenaustausch zwischen Bricks.
* **Stapelstromversorgungsstecker:** Versorgt Bricks und angeschlossene Bricklets, Motoren, Servos usw.


.. _connector_stack_data:

Stapeldatenstecker
^^^^^^^^^^^^^^^^^^

.. csv-table:: 
   :header: "Beschreibung", "Signal", "Pin", "Pin", "Signal", "Beschreibung"
   :widths: 200, 150, 25, 25, 150, 200

   "Stack SPI: MasterIn SlaveOut",                "SPI-MISO",        "**01**", "**02**", "I2C-SDA/TDI", "Stack I2C: Serial Data/ JTAG-TDI"
   "Stack SPI: MasterOut SlaveIn",                "SPI-MOSI",        "**03**", "**04**", "I2C-SCL/TDO", "Stack I2C: Serial Clock/ JTAG-TDO"
   "Stack SPI: Clock",                            "SPI-SCLK",        "**05**", "**06**", "SEL-0",       "Stack Select 0"
   "Reset Signal",                                "RESET",           "**07**", "**08**", "SEL-1",       "Stack Select 1"
   "Stack Detect/JTAG-TMS",                       "DETECT/TMS",      "**09**", "**10**", "SEL-2",       "Stack Select 2"
   "Stack Synchronization/ JTAG-TCK",             "SYNC/GP/TCK",     "**11**", "**12**", "SEL-3",       "Stack Select 3"
   "Extension SPI: MasterIn SlaveOut",            "EX-SPI-MISO",     "**13**", "**14**", "SEL-4",       "Stack Select 4"
   "Extension SPI: MasterOut SlaveIn",            "EX-SPI-MOSI",     "**15**", "**16**", "SEL-5",       "Stack Select 5"
   "Extension SPI: Clock",                        "EX-SPI-SCLK",     "**17**", "**18**", "SEL-6",       "Stack Select 6"
   "Extension 0: General Purpose 0/ Interrupt 0", "EX-0-GP-0/nINT0", "**19**", "**20**", "SEL-7",       "Stack Select 7"
   "Extension 0: General Purpose 1/ Interrupt 1", "EX-0-GP-1/nINT1", "**21**", "**22**", "EX-SEL-0",    "Extension Select 0"
   "Extension 0: General Purpose 2/ Interrupt 2", "EX-0-GP-2/nINT2", "**23**", "**24**", "EX-SEL-1",    "Extension Select 1"
   "Extension 1: General Purpose 0",              "EX-1-GP-0",       "**25**", "**26**", "EX-SER-RXD",  "Extension Serial Interface: RXD"
   "Extension 1: General Purpose 1",              "EX-1-GP-1",       "**27**", "**28**", "EX-SER-TXD",  "Extension Serial Interface: TXD"
   "Extension 1: General Purpose 2",              "EX-1-GP-2",       "**29**", "**30**", "EX-SER-RTS",  "Extension Serial Interface: RTS"

Alle Signale sind 3,3V basiert.


Beschreibung
""""""""""""

* **Stack SPI**: Der SPI Bus für Kommunikation zwischen
  :ref:`Brick <product_overview_bricks>` und Master Brick.
* **JTAG**: Debug-Schnittstelle, überschneidet sich mit anderen Signals. JTAG
  darf nicht verwendet werden, wenn der Brick Teil eines Stapels ist.
* **Reset**: Signal um eine Brick zurückzusetzen, durch den Stapel
  durchgeschleift so dass alle Bricks gleichzeitig zurückgesetzt werden.
* **Stack Detect**: Signal um die Anwesenheit eines
  :ref:`Master Bricks <master_brick>` zu erkennen.
  Alle Bricks außer dem Master Brick haben dieses Signal durchverbunden und
  prüfen es auf logisch 1 um Stapelteilnahme zu erkennen. Der Master Brick
  hat dieses Signal nicht durchverbunden, sondern setzt es im oberen
  Stapeldatenstecker auf Ausgang mit logisch 1 und im unteren Stapeldatenstecker
  auf Eingang mit Pull-Down. Dadurch kann der Master an einem logisch 0 Signal
  im unteren Stapeldatenstecker erkennen ob er der unterste Teilnehmer im Stapel
  und somit Master des Stapels ist.
* **Stack Synchronization**: Dieses Signal wird vom Master Brick verendet um
  Aktionen andere Bricks im Stapel zu synchronisieren.
* **Extension SPI** Der SPI Bus für Kommunikation zwischen Master Brick und
  Master Extensions.
* **Extension General Purpose 0,1 mit 0,1,2**: Drei General Purpose Signal pro
  Master Extension können vom Master Brick verwendet werden um die Master
  Extensions zu steuern. Die Verwendung hängt von der aufgesteckten Master
  Extension ab.
* **Interrupt 0,1,2**: Interrupt Ausgänge, die Verwendung hängt von der
  Konfiguration ab.
* **Stack I2C**: Der I2C Bus für Kommunikation zwischen Master Brick und Master
  Extensions sowie anderer Bricks im Stapel.
* **Select 0-7**: Bis zu acht Adressleitungen über die der Master des Stapels
  bis zu acht Teilnehmer im Stapel auswählen kann. Ein Brick darf nur dann auf
  Nachrichten antworten, wenn seine Adressleitungen gewählt ist
  (Select = logisch 0). Jeder Brick verwendet das erste Select Signal in seinem
  unteren Stapeldatenstecker als seine Adressleitung. Die anderen
  Adressleitungen sind im Stecker versetzt durchverbunden, so dass die zweite
  Adressleitung im unteren Stapeldatenstecker mit der ersten Adressleitung im
  oberen Stapeldatenstecker verbunden ist. Dadurch haben die ersten acht Bricks
  über dem Master des Stapels ihre eigenen Adressleitungen. Alle Bricks darüber
  können nicht mehr adressiert werden und somit nicht mit dem Master des Stapels
  kommunizieren.
* **Extension Select 0,1**: Wird vom Master des Stapels verwendet um Master
  im Stapel auszuwählen. Die Funktion und Aufbau ist gleich den Adressleitungen
  für Bricks. Dadurch können die ersten zwei Master Extensions im Stapel mit dem
  Master des Stapels kommunizieren.
* **Extension Serial Interface**: Serielle Schnittstelle zwischen Master Brick
  und Master Extension.


.. _connector_stack_power:

Stapelstromversorgungsstecker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabularcolumns: |C|C|C|C|

.. csv-table:: 
   :header: "Funktion", "Pin", "Pin", "Funktion"
   :widths: 60, 25, 25, 60

   "PGND",		"01",		"02", "PVCC"
   "PGND",		"03",		"04", "PVCC"
   "PGND",		"05",		"06", "PVCC"
   "PGND",		"07",		"08", "PVCC"
   "PGND",		"09",		"10", "PVCC"
   "PGND",		"11",		"12", "PVCC"
   "PGND",		"13",		"14", "PVCC"
   "PGND",		"15",		"16", "PVCC"
   "PGND",		"17",		"18", "PVCC"
   "PGND",		"19",		"20", "PVCC"
   "GND",		"21",		"22", "5V"
   "GND",		"23",		"24", "5V"
   "GND",		"25",		"26", "5V"
   "GND",		"27",		"28", "3V3"
   "Current",	"29",		"28", "Voltage"


Beschreibung
""""""""""""

* **PGND**: Stapelmassesignal.
* **PVCC**: Stapelstromversorgung (max. 27V, 0,5A per Pin, 5A gesamt), durch
  :ref:`Stromversorgung <product_overview_power_supplies>` bereitgestellt.
* **GND**: Gemeinsames Massesignal.
* **5V**: 5V Stromversorgung (max. 0,5A per Pin, 1,5A gesamt),
  bereitgestellt durch jeden Brick (per USB) oder Stromversorgungen.
  Da die USB Spannung vom verwendeten PC/USB Hub abhängt
  können die 5V an diesem Pin nicht garantiert werden bei Versorgung über USB.
* **3V3**: Bereitgestellt durch jeden Brick. Wird durch einen DC/DC Wandler
  (5V -> 3V3) auf der Platine erzeugt.
* **Current**: Signal zur Messung des Stromverbrauchs über die
  :ref:`Stromversorgung <product_overview_power_supplies>` (max. 3,3V). Kann
  von Master Bricks verwendet wird.
* **Voltage**: Signal zur Messung der externen Versorgungsspannung der
  :ref:`Stromversorgung <product_overview_power_supplies>` (max. 3,3V). Kann
  von Master Bricks verwendet wird.


.. _connector_bricklet:

Bricklet Stecker
----------------

.. csv-table:: 
   :header: "Pin", "Funktion", "Beschreibung"
   :widths: 25, 100, 200

   "01", "5V",			"5V Signal, verbunden mit 5V des Stapels"
   "02", "GND",			"Masse"
   "03", "3V3",			"3,3V bereitgestellt vom Brick"
   "04", "SCL",			"I2C Serial Clock"
   "05", "SDA",			"I2C Serial Data"
   "06", "ADDR",		"Adressleitung (logisch 0 oder 1) um Bricklets für I2C Kommunikation auszuwählen"
   "07", "IO_1/AD",		"I/O 1 mit Analog-Digital-Wandler Fähigkeit"
   "08", "IO_2/DA",		"I/O 2 mit Digital-Analog-Wandler Fähigkeit"
   "09", "IO_3/PWM",	"I/O 3 mit Pulsweitenmodulationsfähigkeit"
   "10", "IO_4",		"I/O 4"

Falls nicht anders angegeben, sind alle Signale 3,3V basiert.


.. _connector_usb:

USB Stecker
-----------

.. csv-table::
   :header: "Pin", "Funktion", "Beschreibung"
   :widths: 25, 100, 200

   "1", "VCC",        "5V"
   "2", "D-",         "Data -"
   "3", "D+",         "Data +"
   "4", "GND",        "Masse"

Die 5V Versorgung über USB muss zwischen 4,8V und 5,7V liegen.
