
:DISABLED_shoplink: ../../../shop/bricks/hat-brick.html

.. include:: HAT_Brick.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _hat_brick:

HAT Brick
=========

.. note::
  Dieses Brick befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricks/brick_hat_tilted_[?|?].jpg              HAT Brick
	Bricks/brick_hat_horizontal_[?|?].jpg          HAT Brick
	Bricks/brick_hat_brickv_[100|].jpg             HAT Brick im Brick Viewer
	Dimensions/hat_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Raspberry Pi HAT im standard RPi HAT Formfaktor
* Besitzt **acht** Anschlüsse für Bricklets
* Integrierte 5.3V Stromversorgung (5V-28V Eingang, bis zu 4A)
* Misst USB und DC Spannungsversorgung
* Bietet eine Realtimeclock für das Raspberry Pi
* Bietet Schlafmodus (low power) und RPi Watchdog


.. _hat_brick_description:

Beschreibung
------------

Der HAT Brick ist ein `Raspberry Pi HAT <https://www.raspberrypi.org/blog/introducing-raspberry-pi-hats/>`__
im standard RPi HAT Formfaktor. Der Brick ist zur HAT Spezifikation konform und funktioniert automatisch
mit Raspbian ohne irgendwelche Änderungen.

Mit dem HAT Brick können bis zu **acht** :ref:`Bricklets <primer_bricklets>` an ein Raspberry Pi
angeschlossen werden.

Das Raspberry Pi kann über den HAT mit einer externen 5V-28V DC Stromversorgung betrieben werden.
Die integrierte Stromversorgung liefert stabile 5V für den RPi, auch unter großer Last. Somit können
der Raspberry Pi, angeschlossene Bricklets und mit dem Raspberry Pi verbundene USB Geräte versorgt 
werden. Schwierigkeiten mit der Stromversorgung des RPi's gehören mit dem HAT der Vergangenheit an,
da das HAT den Spannungsabfall kompensiert und eine etwas erhöhte Spannungsversorgung liefert (5,3V).

Alternativ kann der HAT/RPi auch über Micro-USB versorgt werden. In diesem Fall muss allerdings sichergestellt 
werden, dass die Stromversorgung stable 5V bietet. Dies ist zum Beispiel mit der offiziellen Raspberry Pi
Universal Stromversorgung möglich.
Die USB/DC Versorgungsspannungen werden vom HAT gemessen und sind über die API zugänglich.

Zusätzlich bietet der hat eine :ref:`Real-Time Clock mit Batteriebackup <hat_brick_real_time_clock>`,
welche direkt mit dem Raspberry Pi verbunden ist. Der HAT kann :ref:`den RPi für eine angegebene Zeit
ausschalten <hat_brick_low_power_sleep_mode>`. Somit kann der Raspberry PI auch in batteriebetriebenen
Anwendungen eingesetzt werden. Als Beispiel in einer Anwendung, in der Sensorinformationen jede Stunde
in die Cloud geschickt werden sollen.

Ein :ref:`Watchdog <hat_brick_watchdog>` kann ebenfalls mit dem HAT implementiert werden, so dass der
RPi neugestartet wird wenn dieser sich aufhängt oder das eigene Programm steckenbleibt.

Der HAT Brick ist elektronisch kompatibel zu den Raspberry Pi 2B, 3B, 3B+, 4B, Zero und Zero W. Die
Befestigungslöcher sind kompatibel zum Raspberry Pi 2/3/4. Zusätzlich bieten wir mit dem 
:ref:`HAT Zero Brick <hat_zero_brick>` eine kleinere Version, deren Befestigungslöcher zum Raspberry
Pi Zero kompatibel sind.

.. note::
  Das HAT Brick besitzt Bricklet 7 polige Anschlüsse. Über ein 7 pol <-> 7 pol Kabel können Bricklets
  an das Brick angeschlossen werden. Es werden nur Bricklets unterstützt die über einen 7 poligen Anschluss verfügen. 

Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Stromverbrauch                        100mW (20mA bei 5V)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse                   8
DC Eingangsspannunsbereich            5-28V
DC Ausgang                            5,3V, max. 4A
Stromverbrauch im Sleepmodus (≤1.4)*  70mW (14mA bei 5V) + 1.5mW wenn Sleep Anzeigeled aktiv ist
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               65 x 56 x 25mm (2,56 x 2,20 x 0,98")
Gewicht                               30g 
====================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/hat-brick/raw/master/hardware/hat-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hat_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hat-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _hat_brick_erste_schritte:

Erste Schritte
--------------

Um mit dem HAT Brick zu beginnen muss zuerst der :ref:`Brick Daemon <brickd>`
auf dem Raspberry Pi installiert werden. Der Brick Daemon agiert als proxy zwischen 
den Brickletanschlüssen des HATs und den API Bindings. Er kümmert sich auch um die
Real-Time Clock.

Der Brick Daemon kann auf dem Raspberry Pi im Terminal mit folgenden Kommandos 
installiert werden:

.. code-block:: shell

	sudo apt-get install libusb-1.0-0 libudev0 pm-utils
	wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
	sudo dpkg -i brickd_linux_latest_armhf.deb

Nachdem der Brick Daemon installiert ist, kann der HAT auf den Raspberry Pi gesteckt
und dieser neugestartet werden.

Anschließend kann der :ref:`Brick Viewer <brickv>` genutzt werden um sich mit dem HAT Brick 
und den angeschlossenen Bricklets zu verbinden. 
Der Brick Viewer kann entweder direkt auf dem Raspberry Pi oder aber auf einem externen PC,
der Zugriff auf den RPi besitzt (über Ethernet oder WLAN) installiert werden. Von einem
externen PC muss sich auf die IP des Raspberry Pis verbunden werden. Ansonste auf localhost.

Im Brick Viewer sollte ein Tab (Reiter) namens "HAT Brick" und für jedes angeschlossene Bricklet
ein weiteres Tab angezeigt werden.

.. image:: /Images/Bricks/hat_brickv.jpg
   :scale: 100 %
   :alt: HAT Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/hat_brickv.jpg

Im HAT Brick Tab des Brick Viewers können der Schlafmodus getestet und die gemessenen Spannungen
betrachtet werden.

Sollte unklar sein, ob der HAT Brick korrekt erkannt wurden kann ein Blick in den Ordner
``/proc/device-tree/hat/`` auf dem Raspberry Pi helfen:

.. code-block:: shell

	cd /proc/device-tree/hat/
	echo Name: "$(tr -d '\0'<name)", Product: "$(tr -d '\0'<product)",  Product ID: "$(tr -d '\0'<product_id)", Vendor: "$(tr -d '\0'<vendor)"

Dies sollte etwa das folgende ausgeben::

	Name: hat, Product: HAT Brick, Product ID: 0x084e, Vendor: Tinkerforge GmbH

Falls der Order nicht exisitiert, oder die Ausgabe nicht korrekt ist war die Installation nicht erfolgreich.
Dann sollte geprüft werden ob der HAT Brick korrekt verbunden wurde und ob der Raspberry Pi nach dem aufstecken
neugestartet wurde.


.. _hat_brick_low_power_sleep_mode:

Low Power Sleep Modus
---------------------

Der HAT Brick kann das Raspberry Pi aus-/ und einschalten mit einer konfigurierbaren Ausschaltzeit.

Es kann auch konfiguriert werden ob die Bricklets ebenfalls mit abgeschaltet werden sollen. Zusätzlich
kann die blaue Status-LED entweder ebenfalls ausgeschaltet oder aber mit einem 1 Sekunden Blink-Intervall
konfiguriert werden.

Während das RPi ausgeschaltet ist, läuft die Real-Time Clock weiter und die Uhrzeit wird beim Neustart
wieder korrekt gesetzt.

Zum Thema Sleep Modus bietet die API eine genauere Beschreibung in der ``SetSleepMode`` Funktion.


.. _hat_brick_watchdog:

Watchdog
--------

Der HAT Brick kann als Watchdog für den Raspberry Pi genutzt werden. Er kann
den RPi neustarten, wenn dieser sich aufhängt oder das eigene Programm festhängt.

Um einen Watchdog zu implementieren können die ``Sleep Delay`` und ``Sleep Duration`` Parameter der 
``SetSleepMode`` Funktion genutzt werden.

Watchdog Implementierungsbeispiel (Python):

.. code-block:: python

	while True:
		hat.set_sleep_mode(10, 2, True, False, False)
		time.sleep(1)

Der Beispielcode teilt dem HAT Brick in jedem Schleifendurchlauf mit, das Raspberry Pi in 10 
Sekunden neuzustarten. Dies erfolgt einmal pro sekunde. Jeden Schleifendurchlauf wird der Neustart
somit auf 10 Sekunden zurückgesetzt. Wenn der Raspberry Pi sich aufhängt, erfolgt dieser reset nicht mehr 
und der Raspberry Pi wird neugestartet.

Diese Schleife kann als eigenständiges Programm implementiert werden. Alternativ kann der  ``SetSleepMode``
Aufruf irgendwo in der Hauptschleife der eigenen Anwendung, die auf dem Raspberry Pi läuft, eingebaut werden.
call somewhere in the main loop of your application that runs on the
Im Falle, dass der Raspberry Pi hängt, erfolgt also der neustart.


.. _hat_brick_real_time_clock:

Real-Time Clock
---------------

Der HAT Brick bietet eine I2C Real-Time Clock (Echtzeituhr), welche direkt mit 
dem Raspberry Pi verbunden ist. Die Uhr wird automatisch vom RPi erkannt. Mit dmesg 
kann überprüft werden ob die Uhr korrekt erkannt wurde. Es sollte ein Eintrag
wie der folgende existieren::

	[    3.850299] rtc-pcf8523 1-0068: rtc core: registered rtc-pcf8523 as rtc0

Falls NTP nicht zur Verfügung steht muss das Datum und Uhrzeit anfangs einmal händisch gesetzt
werden. Anschließend kann mit folgenden Kommando:

.. code-block:: shell

	hwclock --systohc

die Uhrzeit des RPi auf die Real-Time Clock übertragen werden. Dies ist nur einmal notwendig.

Steht NTP zur Verfügung, so wird die Real-Time Clock automatisch aktualisiert.

Der Brick Daemon stellt sicher, dass Datum und Uhrzeit automatisch nach einem Neustart von der
Real-Time Clock übernommen werden.

Ohne Brick Daemon kann dies händisch mit folgenden Kommando durchgeführt werden:

.. code-block:: shell

	hwclock --hctosys


Kompatibilität zu anderen Boards und Images
-------------------------------------------

Wird Raspbian genutzt, so wird der HAT Brick automatisch erkannt und genutzt. 
Die Pins werden dann automatisch für eine Kommunikation mit den Bricklets konfiguriert.

Dies erfolgt über das Auslesen der gespeicherten HAT Konfiguration aus dem EEPROM des HAT.

Wird ein Linux Image genutzt, welches das raspi-config Framework nicht bietet,
oder aber ein anderes Board mit Raspberry Pi kompatiblen GPIO Pinheader aber anderen Prozessor genutzt,
so funktioniert dies nicht automatisch.

In diesem Fall kann der Brick Daemon die notwendige SPI und GPIO Pinkonfiguration vornehmen.
Dazu muss in der ``/etc/brickd.conf`` Datei die Konfiguration angegeben werden.

Für ein standard Raspberry Pi wäre dies::

	bricklet.group0.spidev = /dev/spidev0.0

	bricklet.group0.cs0.driver = gpio
	bricklet.group0.cs0.name = gpio23
	bricklet.group0.cs0.num = 23

	bricklet.group0.cs1.driver = gpio
	bricklet.group0.cs1.name = gpio22
	bricklet.group0.cs1.num = 22

	bricklet.group0.cs2.driver = gpio
	bricklet.group0.cs2.name = gpio25
	bricklet.group0.cs2.num = 25

	bricklet.group0.cs3.driver = gpio
	bricklet.group0.cs3.name = gpio26
	bricklet.group0.cs3.num = 26

	bricklet.group0.cs4.driver = gpio
	bricklet.group0.cs4.name = gpio27
	bricklet.group0.cs4.num = 27

	bricklet.group0.cs5.driver = gpio
	bricklet.group0.cs5.name = gpio24
	bricklet.group0.cs5.num = 24

	bricklet.group0.cs6.driver = gpio
	bricklet.group0.cs6.name = gpio7
	bricklet.group0.cs6.num = 7

	bricklet.group0.cs7.driver = gpio
	bricklet.group0.cs7.name = gpio6
	bricklet.group0.cs7.num = 6

	bricklet.group0.cs8.driver = gpio
	bricklet.group0.cs8.name = gpio5
	bricklet.group0.cs8.num = 5

Als erstes muss das SPI Device, das genutzt werden soll konfiguriert werden 
(``/dev/spidev0.0`` für den Raspberry Pi). Anschließend muss ein GPIO Treiber,
und Name und Nummer des GPIO für jedes Chip Selects definiert werden.
Es gibt acht Chip Selects für die acht Bricklet Anschlüsse und ein Chip Select für
den HAT Brick selbst.

Wird ein komplett verschiedenes Board genutzt, so kann der Schaltplan zu dem Board
Aufschlüsse bieten, wie die Konfiguration angepasst werden muss. Sollte Hilfe 
notwendig sein, bietet `tinkerunity.org <https://www.tinkerunity.org>`__
eine Möglichkeit Hilfe zu finden.


.. _hat_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: HAT_Brick_hlpi.table
