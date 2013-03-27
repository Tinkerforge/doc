
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / Brick Viewer (brickv)

.. _brickv:

Brick Viewer (brickv)
=====================

Der Brick Viewer bietet eine graphische Oberfläche um
:ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` zu testen. Jedes Gerät hat seine
eigenen Tab der die Hauptfunktionen abbildet und erlaubt diese zu steuern.

Darüber hinaus kann der Brick Viewer verwendet werden, um den
Analog-Digital-Wandler der Bricks zu :ref:`kalibrieren <brickv_adc_calibration>`
und so deren Messqualität zu verbessern, und um
:ref:`Brick Firmwares <brickv_flash_firmware>` und
:ref:`Bricklet Plugins <brickv_flash_plugin>` zu flashen.


.. _brickv_installation:

Installation
------------

* :ref:`Windows <brickv_install_windows>`
* :ref:`Linux <brickv_install_linux>`
* :ref:`Mac OS X <brickv_install_macosx>`


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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nach dem Start des Brick Viewers und dem Verbinden zu einem
Brick Daemon oder einer Master Extension kann überprüft werden ob
eine neuere Software für die angeschlossenen Geräte verfügbar ist.

Hierzu muss auf "Updates / Flashing" geklickt werden. Der Dialog
zeigt die angeschlossenen Geräte und deren Software stand. Orange
unterlegte Einträge können geupdated werden. Rot unterlegte Einträge
müssen geupdated werden damit sie korrekt funktionieren.

.. image:: /Images/Screenshots/brickv_auto_update_small.jpg
   :scale: 100 %
   :alt: Brickv (Updates)
   :align: center
   :target: ../_images/Screenshots/brickv_auto_update.jpg

Der Dialog ermöglicht es alle Bricklets gleichzeitig über den Knopf 
"Auto-Update All Bricklets" auf die neuste Softwareversion zu bringen.
Bricks können nicht automatisch auf den neusten Stand gebracht werden
(siehe :ref:`Brick Firmware Flashing <brickv_flash_firmware>`). 


.. _brickv_flash_firmware:

Brick Firmware Flashing
^^^^^^^^^^^^^^^^^^^^^^^

Seit Version 1.1.0 kann der Brick Viewer Firmwares auf Bricks flashen. Die
jeweils neuste Firmwareversion wird dabei automatisch vom Brick Viewer
ermittelt und heruntergeladen. Diese können aber auch manuell im
:ref:`Downloadbereich <downloads_firmwares_plugins>` heruntergeladen werden.

Um einen Brick flashen zu können, muss dieser per USB zu einem PC mit
Brick Viewer verbunden sein.

Bevor ein IMU Brick neu geflashed wird sollte dessen Kalibrierung exportiert
werden, da diese beim Flashen verloren geht. Dies ist allerdings nur dann
notwendig falls eine eigenen Kalibrierung vorgenommen wurde, da die
Werkskalibrierung seit Brick Viewer Version 1.1.13 automatisch wiederhergestellt
werden kann.

Zum Flashen muss der Brick in den Bootloader Modus versetzt werden. Dazu muss
der Erase Knopf am Brick gedrückt gehalten werden während der Brick startet.
Dazu denn Erase Knopf gedrückt halten und dabei den Reset Knopf 1x
drücken. Ist der Brick dann im Bootloader
Modus leuchtet die blaue LED neben der USB Buchse des Bricks nicht. Abhängig vom
Betriebssystems des PC sollte jetzt Atmel Gerät in Form einer seriellen
Schnittstelle auftauchen.

Als nächstes muss der Brick Viewer gestartet und "Flashing" Dialog geöffnet
werden:

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
richtig als serielle Schnittstelle erkannt.

.. note::
 Auf Windows kann es nötig sein den Atmel Treiber ``atm6124_cdc.inf`` aus dem
 drivers Unterordner der Brick Viewer Installation zu installieren, damit ein
 Brick im Bootloader Modus richtig als serielle Schnittstelle erkannt wird.

 Windows 7 erkennt einen Brick im Bootloader Modus von sich aus als "GPS Camera
 Detect" Gerät. Dies ist auch eine serielle Schnittstelle so dass Flashen
 dennoch möglich ist. Falls hier dennoch Probleme auftreten kann es helfen
 den Atmel Treiber ``atm6124_cdc.inf`` zu installieren.

.. note::
 Für alte Linux Kernel kann es notwendig sein diesen
 `SAM-BA Linux USB Kernel Treiber <http://www.embedded-it.de/en/microcontroller/eNet-sam7X.php>`__
 zu installieren, damit ein Brick im Bootloader Modus richtig funktioniert.

Wird die serielle Schnittstelle des Bricks richtig erkannt muss diese nun im
Brick Viewer ausgewählt werden, sowie die passende Firmware für den Brick.
Passend die Einstellungen kann das Flashen per Klick auf den "Save" Knopf
gestartet werden. Jetzt wird die aktuelle Firmware für den Brick heruntergeladen,
auf den Brick geschrieben und dann wieder zurück gelesen, um sicherzustellen,
dass das Schreiben der Firmware richtig funktioniert hat. Falls das Flashen
scheitert, sollte zunächst überprüft werden, ob die richtige serielle
Schnittstelle ausgewählt wurde.

Anstatt den Brick Viewer die jeweils neuste Firmware herunterladen zu lassen,
kann auch "Custom..." als Firmware gewählt werden und dann die zu flashende
Firmware als lokale Datei über den "Browse..." Knopf ausgewählt werden.


.. _brickv_flash_plugin:

Bricklet Plugin Flashing
^^^^^^^^^^^^^^^^^^^^^^^^

Der Brick Viewer kann auch Plugins auf Bricklets flashen.
Hierfür gibt es die Möglichkeit alle Bricklets auf die neuste Version zu 
bringen (siehe "Auto-Update All Bricklets" unter 
:ref:`Aktuellen Stand bestimmen <brickv_auto_update>`). Alternativ können
Bricklets auch einzeln geflasht werden. Die
jeweils neuste Pluginversion wird dabei automatisch vom Brick Viewer
ermittelt und heruntergeladen. Diese können aber auch manuell im
:ref:`Downloadbereich <downloads_firmwares_plugins>` heruntergeladen werden.

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


.. _brickv_adc_calibration:

Brick AD-Wandler Kalibrierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

