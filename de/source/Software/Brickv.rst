
.. _brickv:

Brick Viewer (brickv)
=====================

Der Brick Viewer bietet eine graphische Oberfläche um
:ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` zu testen. Jedes Gerät hat seine
eigenen Tab der die Hauptfunktionen abbildet und erlaubt diese zu steuern.

Darüber hinaus kann der Brick Viewer verwendet werden, um den
Analog-Digital-Wandler der Bricks zu :ref:`kalibrieren <brickv_adc_calibration>`
und so deren Messqualität zu verbessern, und um
:ref:`Brick Firmwares <brickv_flash_brick_firmware>` und
:ref:`Bricklet Plugins <brickv_flash_bricklet_plugin>` zu flashen.


.. _brickv_installation:

Installation
------------

* :ref:`Windows <brickv_install_windows>`
* :ref:`Linux <brickv_install_linux>`
* :ref:`macOS <brickv_install_macos>`

.. toctree::
   :hidden:

   Windows <Brickv_Install_Windows>
   Linux <Brickv_Install_Linux>
   macOS <Brickv_Install_MacOSX>


Verwendung
----------

Zuerst muss der Brick Viewer mit dem :ref:`Brick Daemon <brickd>` oder z.B. einer
:ref:`WIFI Extension <wifi_extension>` verbunden werden. Dabei kann der Brick
Daemon auf dem gleichen oder einem anderen PC als der Brick Viewer laufen.
Dazu zuerst die IP Adresse des PCs auf dem der Brick Daemons läuft oder die IP
Adresse einer WIFI Extension als Host angeben. Falls Brick Daemon und Viewer
auf dem gleichen PC laufen kann der Standardwert ``localhost`` beibehalten werden.
Nach einem Klick auf den "Connect" Knopf werden die verbunden Bricks und
Bricklets auf je einem eigenen Tab angezeigt und können getestet werden.

.. image:: /Images/Screenshots/brickv_setup_tab_small.jpg
   :scale: 100 %
   :alt: Brickv (Setup Tab)
   :align: center
   :target: ../_images/Screenshots/brickv_setup_tab.jpg

Ein Klick auf den "Updates / Flashing" öffnen einen Dialog mit Informationen
über verfügbare Updates und der Möglichkeit Bricks und Bricklets
neu zu flashen. Der "Advanced Functions" Knopf öffnet einen Dialog zur
Kalibrierung des Analog-Digital-Wandler eines Bricks.


.. _brickv_auto_update:

Aktuellen Stand bestimmen / Nach Updates suchen
-----------------------------------------------

Nach dem Start des Brick Viewers und dem Verbinden zu einem
Brick Daemon oder einer Master Extension kann überprüft werden ob
eine neuere Software für die angeschlossenen Geräte verfügbar ist.

Hierzu muss auf "Updates / Flashing" geklickt werden. Der Dialog
zeigt die angeschlossenen Geräte und deren Software stand. Orange
unterlegte Einträge können geupdatet werden. Rot unterlegte Einträge
müssen geupdatet werden damit sie korrekt funktionieren.

.. image:: /Images/Screenshots/brickv_auto_update_small.jpg
   :scale: 100 %
   :alt: Brickv (Updates)
   :align: center
   :target: ../_images/Screenshots/brickv_auto_update.jpg

Der Dialog ermöglicht es alle Bricklets gleichzeitig über den Knopf
"Auto-Update All Bricklets" auf die neuste Softwareversion zu bringen.
Bricks können nicht automatisch auf den neusten Stand gebracht werden
(siehe :ref:`Brick Firmware Flashing <brickv_flash_brick_firmware>`).


.. _brickv_flash_brick_firmware:

Brick Firmware Flashing
-----------------------

Wir empfehlen Brick Viewer zum Flashen von Firmwares zu verwenden. Für
Linux System ohne graphische Benutzeroberfläche steht aber auch
``brick-flash`` zur Verfügung.

Mit Brick Viewer
^^^^^^^^^^^^^^^^

Seit Version 1.1.0 kann der Brick Viewer Firmwares auf Bricks flashen. Die
jeweils neuste Firmwareversion wird dabei automatisch vom Brick Viewer
ermittelt und heruntergeladen. Diese können aber auch manuell im
:ref:`Downloadbereich <downloads_brick_firmwares>` heruntergeladen werden.

Vorbereitung
""""""""""""

Um einen Brick flashen zu können, muss dieser per USB zu einem PC mit
Brick Viewer verbunden sein. Abhängig vom Typ des Brick ist noch Folgendes
zu beachten:

* Bevor ein **IMU Brick** neu geflasht wird sollte dessen Kalibrierung
  exportiert werden, da diese beim Flashen verloren geht. Dies ist allerdings
  nur dann notwendig, falls eine eigenen Kalibrierung vorgenommen wurde, da
  die Werkskalibrierung seit Brick Viewer Version 1.1.13 automatisch
  wiederhergestellt werden kann.

* Die Hardware Version 2.0 des **Master Bricks** hat eine Änderung im
  Leiterplattenlayout, die den Bootloader Modus stört, wenn eine Master Extension
  wie WIFI, RS485 oder Ethernet im Stack vorhanden ist. In diesem Fall muss die
  Master Extension aus dem Stack entfernt werden, damit der Bootloader Modus
  richtig funktioniert. Diese Problem wurde in Hardware Version 2.1 korrigiert.

Zum Flashen einer neuen Firmware muss der Brick in den Bootloader Modus
versetzt werden. Dazu folgende Schritte anwenden:

1. Brick per USB an PC anschließen.
2. Erase Knopf drücken und gedrückt halten.
3. Reset Knopf drücken und wieder loslassen.
4. Erase Knopf wieder loslassen.

Jetzt sollten alle LEDs am Brick aus sein, der Brick sich im Bootloader
Modus befinden und am PC sollte eine neue seriellen Schnittstelle auftauchen.

Serielle Schnittstelle
""""""""""""""""""""""

Als nächstes muss der Brick Viewer gestartet und der "Updates / Flashing"
Dialog geöffnet werden:

.. image:: /Images/Screenshots/brickv_flashing_firmware_small.jpg
   :scale: 100 %
   :alt: Brickv (Brick Firmware)
   :align: center
   :target: ../_images/Screenshots/brickv_flashing_firmware.jpg

Die "Serial Port" Dropdown-Box zeigt alle verfügbaren seriellen Schnittstellen
des PCs an. Diese kann mittels des "Refresh" Knopfes aktualisiert werden, falls
keine oder nicht die richtige serielle Schnittstelle aufgelistet wird. Falls
der Brick nicht als serielle Schnittstelle auftaucht, befindet sich der Brick
entweder nicht im Bootloader Modus, oder das Betriebssystem hat ihn nicht
richtig als serielle Schnittstelle erkannt:

* Auf **Windows** XP und Vista kann es nötig sein den Atmel Treiber
  ``atm6124_cdc.inf`` aus dem ``drivers`` Unterordner der Brick Viewer
  Installation zu installieren, damit ein Brick im Bootloader Modus richtig
  als serielle Schnittstelle erkannt wird. Windows 7, 8, 8.1 und 10 erkennt
  einen Brick im Bootloader Modus von sich aus als "GPS Camera  Detect" oder
  "Bossa Program Port" Gerät. Dies ist auch eine serielle Schnittstelle so
  das Flashen dennoch möglich ist.

* Für **alte Linux** Kernel Versionen kann es notwendig sein diesen
  `SAM-BA Linux USB Kernel Treiber
  <http://www.embedded-it.de/en/microcontroller/eNet-sam7X.php>`__
  zu installieren, damit ein Brick im Bootloader Modus richtig funktioniert.

* Auf **macOS** kann einen Brick im Bootloader Modus als DVB-T Stick erkannt
  und automatisch EyeTV oder ein ähnliches Programm gestartet werden. Dann
  einfach EyeTV schließen und mit dem Flash-Vorgang fortfahren.

Wird die serielle Schnittstelle des Bricks richtig erkannt muss diese nun im
Brick Viewer ausgewählt werden, typische Namen sind:

* Windows: "AT91 USB to Serial Converter" oder "GPS Camera Detect" oder
  "Bossa Program Port"
* Linux: ``/dev/ttyACM0`` oder ``/dev/ttyUSB0``
* macOS: ``/dev/tty.usbmodemfd131``

Flashen
"""""""

Jetzt noch die richtige Firmware für den Brick auswählen.
Passend die Einstellungen kann das Flashen per Klick auf den "Save" Knopf
gestartet werden. Die aktuelle Firmware für den Brick wird heruntergeladen,
auf den Brick geschrieben und dann wieder zurück gelesen, um sicherzustellen,
dass das Schreiben der Firmware richtig funktioniert hat.

Falls das Flashen fehlschlägt, sollte zunächst überprüft werden, ob die
richtige serielle Schnittstelle ausgewählt wurde. Wenn Brick Viewer auf Linux
"No permission to open serial port" meldet, dann liegt dies normalerweise
daran, dass der Nutzer nicht der Gruppe ``dialout`` angehört. Um dieses Problem
zu beheben kann entweder der Nutzer der Gruppe ``dialout`` hinzugefügt oder
Brick Viewer als root gestartet werden (``sudo brickv``).

Anstatt den Brick Viewer die jeweils neuste Firmware herunterladen zu lassen,
kann auch "Custom..." als Firmware gewählt werden und dann die zu flashende
Firmware als lokale Datei über den "Browse..." Knopf ausgewählt werden.

Mit brick-flash auf Linux
^^^^^^^^^^^^^^^^^^^^^^^^^

Brick Viewer benötigt eine graphische Benutzeroberfläche. Falls Bricks an
Linux Rechnern ohne graphische Benutzeroberfläche geflasht werden sollen kann
``brick-flash`` verwendet werden. Es steht als `Debian Packet
<http://download.tinkerforge.com/tools/brick_flash/linux/brick-flash_linux_latest.deb>`__
zum Download bereit::

 wget http://download.tinkerforge.com/tools/brick_flash/linux/brick-flash_linux_latest.deb
 sudo dpkg -i brick-flash_linux_latest.deb

Im Gegensatz zum Brick Viewer lädt ``brick-flash`` die Firmware nicht
automatisch herunter. Die jeweils neusten Firmwares sind :ref:`hier
<downloads_brick_firmwares>` zu finden. Lade die zu flashende Firmware
herunter, z.B. die neuste Master Brick Firmware::

 wget http://download.tinkerforge.com/firmwares/bricks/master/brick_master_firmware_latest.bin

Stelle sicher, dass sich der Brick im Bootloader Modus befindet (siehe Brick
Viewer Abschnitt weiter oben) und bestimme die serielle Schnittstelle des
Bricks. Typischerweise ist dies ``/dev/ttyACM0`` oder ``/dev/ttyUSB0``.

Jetzt kann ``brick-flash`` mit dem Namen der serielle Schnittstelle und dem
Dateinamen der Firmware ausgeführt werden::

 brick-flash -p /dev/ttyACM0 -f brick_master_firmware_latest.bin

Nach dem Flash-Vorgang startet der Brick automatisch neu und verwendet die
neue Firmware.


.. _brickv_flash_bricklet_plugin:

Bricklet Plugin Flashing
------------------------

Der Brick Viewer kann auch Plugins auf Bricklets flashen.
Hierfür gibt es die Möglichkeit alle Bricklets auf die neuste Version zu
bringen (siehe "Auto-Update All Bricklets" unter
:ref:`Aktuellen Stand bestimmen <brickv_auto_update>`). Alternativ können
Bricklets auch einzeln geflasht werden. Die
jeweils neuste Plugin-Version wird dabei automatisch vom Brick Viewer
ermittelt und heruntergeladen. Diese können aber auch manuell im
:ref:`Downloadbereich <downloads_bricklet_plugins>` heruntergeladen werden.

Um ein Bricklet flashen zu können, muss es an einem Brick angeschlossen sein,
der im Brick Viewer aufgelistet ist. Ein Klick auf den "Flashing" Knopf im
lässt den passenden Dialog erscheinen:

.. image:: /Images/Screenshots/brickv_flashing_plugin_small.jpg
   :scale: 100 %
   :alt: Brickv (Bricklet Plugin)
   :align: center
   :target: ../_images/Screenshots/brickv_flashing_plugin.jpg

Als nächstes muss der Brick und dessen Port ausgewählt werden, an dem das zu
flashende Bricklet angeschlossen ist, sowie das passenden Plugin für das
Bricklet. Passend die Einstellungen kann das Flashen per Klick auf den "Save" Knopf
gestartet werden. Jetzt wird das aktuelle Plugin für das Bricklet heruntergeladen,
auf das Bricklet geschrieben und dann wieder zurück gelesen, um sicherzustellen,
dass das Schreiben des Plugin richtig funktioniert hat. Falls das Flashen
scheitert, sollte zunächst überprüft werden, ob der richtige Brick und der
richtige Port ausgewählt wurde und ob das Bricklet auch richtig angeschlossen ist.

Anstatt den Brick Viewer das jeweils neuste Plugin herunterladen zu lassen,
kann auch "Custom..." als Plugin gewählt werden und dann die zu flashende
Plugin als lokale Datei über den "Browse..." Knopf ausgewählt werden.

Darüber hinaus kann die UID des Bricklets ausgelesen und auch neu geschrieben
werden. Die UID ist Base58 kodiert, die erlaubten Zeichen umfassen
0-9, a-z und A-Z ohne 0 (Null), I (groß i), O (groß o) und l (klein L).
Die einzige weitere Einschränkung ist, dass die UIDs aller Bricklets eindeutig
sind.


.. _brickv_flash_extension_firmware:

Master Extension Firmware Flashing
----------------------------------

.. note::
  Coming soon!


.. _brickv_adc_calibration:

Brick AD-Wandler Kalibrierung
-----------------------------

Bei Problemen mit ungenauen Messungen (z.B. erreicht das Linear Poti Bricklet
nicht den Maximalwert oder die Spannungsmessung im Stapel ist ungenau) kann
die Kalibrierung des AD-Wandlers Schuld sein.

Der Mikrocontroller auf den Bricks verwendet einen Analog-Digital-Wandler um
analoge Spannungen zu messen. Da der AD-Wandler nicht perfekt kalibriert ist
kann dieser über den Brick Viewer nachkalibriert werden.

Für die Kalibrierung wird eines der Potentiometer Bricklets (Rotary Poti
oder Linear Poti) benötigt. Verbinde es mit dem Brick und rufe den
"Advanced Functions" Dialog im Brick Viewer auf:

.. image:: /Images/Screenshots/brickv_advanced_functions_calibrate_small.jpg
   :scale: 100 %
   :alt: Brickv (AD-Wandler Kalibrierung)
   :align: center
   :target: ../_images/Screenshots/brickv_advanced_functions_calibrate.jpg

Wähle den Port aus an dem das Poti Bricklet angeschlossen ist (A-D).
Stelle dann das Poti Bricklet ganz nach links und klicke den "Calibrate" Knopf.
Stelle das Poti Bricklet ganz nach rechts und klicke wieder den "Calibrate"
Knopf. Falls der AD-Wandler nicht passend kalibriert war, dann weichen jetzt der
Gain und Offset Wert von den Standardwerten ab (4095 und 0).

Ob die Kalibrierung grundsätzlich funktioniert kann dadurch getestet werden,
dass das Poti Bricklet in Mittelstellung gebracht und dann "Calibrate" geklickt
wird. Dabei muss sich Gain oder Offset ändern (danach muss der AD-Wandler
natürlich wieder korrekt kalibriert werden).


Brick Logger
------------

Seit Version 2.3.0 ist ein Logger Teil vom Brick Viewer.
:ref:`Brick Logger <brick_logger>` kann auch eigenständig betrieben werden.
Die Dokumentation befindet sich :ref:`hier <brick_logger>`.
