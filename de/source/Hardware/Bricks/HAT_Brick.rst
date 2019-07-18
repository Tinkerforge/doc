
:shoplink: ../../../shop/bricks/hat-brick.html

.. include:: HAT_Brick.substitutions


.. _hat_brick:

HAT Brick
=========

.. raw:: html

	{% tfgallery %}
	Bricks/brick_hat_tilted_top_[?|?].jpg          HAT Brick Oberseite
	Bricks/brick_hat_tilted_bottom_[?|?].jpg       HAT Brick Unterseite
	Bricks/brick_hat_tilted_w_rpi_[?|?].jpg        HAT Brick mit Raspberry Pi 4
	Bricks/brick_hat_top_w_rpi_[?|?].jpg           HAT Brick
	Bricks/brick_hat_w_bricklets_[?|?].jpg         HAT Brick mit Bricklets
	Bricks/brick_hat_w_hat_zero_[?|?].jpg          HAT Brick und HAT Zero Brick
	Bricks/brick_hat_caption_[?|?].jpg             HAT Brick mit Funktionsblöcken
	Bricks/brick_hat_brickv_[100|].jpg             HAT Brick im Brick Viewer
	Dimensions/hat_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Raspberry Pi HAT im Standard-HAT-Formfaktor
* **Acht** Anschlüsse für Bricklets
* Integrierte 5.3V Stromversorgung (5V-28V Eingang, bis zu 4A)
* Misst USB- und DC-Spannungsversorgung
* Bietet eine Real-Time-Clock für den Raspberry Pi
* Bietet Schlafmodus (low power) und Watchdog


.. _hat_brick_description:

Beschreibung
------------

Der HAT Brick ist ein `Raspberry Pi HAT <https://www.raspberrypi.org/blog/introducing-raspberry-pi-hats/>`__
im Standard-HAT-Formfaktor. Der Brick ist zur HAT-Spezifikation konform und funktioniert automatisch und ohne Änderungen mit Raspbian.

Mit dem HAT Brick können bis zu **acht** :ref:`Bricklets <primer_bricklets>` an ein Raspberry Pi
angeschlossen werden.

.. note::
  Der HAT Brick besitzt 7-Pol-Bricklet-Anschlüsse. Über ein 7-Pol- <-> 7-Pol-Kabel können Bricklets
  an den Brick angeschlossen werden. Es werden nur Bricklets unterstützt, die über einen 7-poligen Anschluss verfügen. 

Der Raspberry Pi kann über den HAT Brick mit einer externen 5V-28V DC Stromversorgung betrieben werden.
Die integrierte Stromversorgung liefert auch unter großer Last stabile 5V für den Raspberry Pi. Somit können
auch angeschlossene Bricklets und verbundene USB-Geräte versorgt werden. Das HAT Brick liefert hierfür eine etwas erhöhte Spannung von 5,3V.

Alternativ können HAT Brick und Raspberry Pi auch über Micro-USB versorgt werden. In diesem Fall muss allerdings sichergestellt werden,
dass die Stromversorgung stabile 5V bietet. Dies ist zum Beispiel mit dem offiziellen Raspberry Pi
Universal-Netzteil möglich.
Die USB/DC Versorgungsspannungen werden vom HAT gemessen und sind über die API zugänglich.

Der HAT Brick bietet eine :ref:`Real-Time-Clock mit Batteriebackup <hat_brick_real_time_clock>`,
die direkt mit dem Raspberry Pi verbunden ist. Mit dieser kann :ref:`der Raspberry Pi für eine angegebene Zeit ausgeschaltet werden <hat_brick_low_power_sleep_mode>`. 
Somit kann der Raspberry Pi auch in batteriebetriebenen
Anwendungen eingesetzt werden, zum Beispiel in einer Anwendung, in der Sensorinformationen jede Stunde
in die Cloud geschickt werden sollen.

Mit dem HAT Brick kann ein :ref:`Watchdog <hat_brick_watchdog>` implementiert werden, der den
Raspberry Pi neustartet, wenn sich dieser aufhängt oder das eigene Programm steckenbleibt.

Der HAT Brick ist elektronisch kompatibel zu den Raspberry Pis 2B, 3B, 3B+, 4B, Zero und Zero W. Die
Befestigungslöcher sind kompatibel zum Raspberry Pi 2/3/4. Zusätzlich bieten wir mit dem 
:ref:`HAT Zero Brick <hat_zero_brick>` eine kleinere Version, deren Befestigungslöcher zum Raspberry
Pi Zero kompatibel sind.


Beispielprojekt: Nutze HAT Brick + Raspberry PI 4 mit :ref:`Thermal Imaging Bricklet <thermal_imaging_bricklet>` und 
:ref:`LCD 128x64 Bricklet <lcd_128x64_bricklet>` um eine 1-Bit Repräsentation des Wärmebildes auf dem LCD 128x64 zu
zeigen. Der Quellcode kann `hier <https://www.tinkerforge.com/de/doc/Software/Bricklets/ThermalImaging_Bricklet_Python.html#thermal-imaging-to-lcd>`__ gefunden werden.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/brick_hat_with_thermal_imaging_and_lcd.mp4" type="video/mp4">
	  <source src="../../_images/Videos/brick_hat_with_thermal_imaging_and_lcd.ogg" type="video/ogg">
	  <source src="../../_images/Videos/brick_hat_with_thermal_imaging_and_lcd.webm" type="video/webm">
	</video>

Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Stromverbrauch                        100mW (20mA bei 5V)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Bricklet-Anschlüsse                   8
DC Eingangsspannungsbereich           5-28V
DC Ausgang                            5,3V, max. 4A
Stromverbrauch im Sleepmodus (≤1.4)*  70mW (14mA bei 5V) + 1.5mW wenn die Sleep-LED aktiv ist
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               65 x 56 x 25mm (2,56 x 2,20 x 0,98")
Gewicht                               30g 
====================================  ============================================================

\*: Dieser Wert ist für den HAT Brick in Hardware-Version 1.4 oder kleiner.

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/hat-brick/raw/master/hardware/hat-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hat_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hat-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2XiDCDT>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/hat/hat.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/hat/hat.FCStd>`__)


.. _hat_brick_erste_schritte:

Erste Schritte
--------------

.. image:: /Images/Bricks/brick_hat_caption_800.jpg
   :scale: 100 %
   :alt: HAT Brick mit Funktionsblöcken
   :align: center
   :target: ../../_images/Bricks/brick_hat_caption_1200.jpg

Um den HAT Brick verwenden zu können, muss zuerst der :ref:`Brick Daemon <brickd>`
auf dem Raspberry Pi installiert werden. Der Brick Daemon agiert als Proxy zwischen 
den Brickletanschlüssen des HAT Brickss und den API Bindings. Er kümmert sich auch um die
Real-Time-Clock.

Der Brick Daemon kann auf dem Raspberry Pi im Terminal mit folgenden Kommandos 
installiert werden:

.. code-block:: shell

	sudo apt-get install libusb-1.0-0 libudev0 pm-utils
	wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
	sudo dpkg -i brickd_linux_latest_armhf.deb

Nachdem der Brick Daemon installiert wurde, kann der HAT Brick auf den Raspberry Pi gesteckt
und dieser neugestartet werden.

Anschließend kann der :ref:`Brick Viewer <brickv>` genutzt werden, um sich mit dem HAT Brick 
und den angeschlossenen Bricklets zu verbinden. 
Der Brick Viewer kann entweder direkt auf dem Raspberry Pi oder auf einem externen PC,
der über Ethernet oder WLAN Zugriff auf den Raspberry Pi besitzt, installiert werden. Von einem
externen PC aus muss sich auf den Hostnamen oder die IP des Raspberry Pis verbunden werden, vom Raspberry Pi aus auf localhost.

Im Brick Viewer sollte ein Tab namens "HAT Brick" und für jedes angeschlossene Bricklet
ein weiterer Tab angezeigt werden.

.. image:: /Images/Bricks/brick_hat_brickv.jpg
   :scale: 100 %
   :alt: HAT Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/brick_hat_brickv.jpg

Im HAT Brick Tab des Brick Viewers können der Schlafmodus getestet und die gemessenen Spannungen
betrachtet werden.

Sollte unklar sein, ob der HAT Brick korrekt erkannt wurde, kann ein Blick in den Ordner
``/proc/device-tree/hat/`` auf dem Raspberry Pi helfen:

.. code-block:: shell

	cd /proc/device-tree/hat/
	echo Name: "$(tr -d '\0'<name)", Product: "$(tr -d '\0'<product)",  Product ID: "$(tr -d '\0'<product_id)", Vendor: "$(tr -d '\0'<vendor)"

Dies sollte etwa das folgende ausgeben::

	Name: hat, Product: HAT Brick, Product ID: 0x084e, Vendor: Tinkerforge GmbH

Falls der Order nicht exisitiert, oder die Ausgabe nicht korrekt ist, war die Installation nicht erfolgreich.
Dann sollte geprüft werden, ob der HAT Brick korrekt verbunden wurde und ob der Raspberry Pi nach dem aufstecken neugestartet wurde.


.. _hat_brick_low_power_sleep_mode:

Low Power Sleep Modus
---------------------

Der HAT Brick kann den Raspberry Pi mit einer konfigurierbaren Ausschaltzeit aus- und einschalten.

Es kann auch konfiguriert werden, dass die Bricklets ebenfalls abgeschaltet werden sollen. Zusätzlich
kann die blaue Status-LED deaktiviert, oder, um den Sleep-Modus anzuzeigen, auf ein Blink-Intervall von einer Sekunde konfiguriert werden.

Während der Raspberry Pi ausgeschaltet ist, läuft die Real-Time-Clock weiter. Die Uhrzeit wird beim Neustart
wieder korrekt gesetzt.

Die Sleep-Modi werden in der API-Beschreibung der Funktion ``SetSleepMode`` genauer beschrieben.


.. _hat_brick_watchdog:

Watchdog
--------

Der HAT Brick kann als Watchdog für den Raspberry Pi genutzt werden. Er kann
den Raspberry Pi neustarten, falls sich dieser oder ein eigenes Programm aufhängt.

Um einen Watchdog zu implementieren können die ``Sleep Delay`` und ``Sleep Duration`` Parameter der 
``SetSleepMode`` Funktion genutzt werden, wie im folgenden Beispiel (in Python) gezeigt wird:

.. code-block:: python

	while True:
		hat.set_sleep_mode(10, 2, True, False, False)
		time.sleep(1)

Der Beispielcode teilt dem HAT Brick in jedem Schleifendurchlauf mit, den Raspberry Pi in 10 
Sekunden neuzustarten. Dies erfolgt einmal pro Sekunde, in jedem Schleifendurchlauf wird der Neustart
somit auf in 10 Sekunden zurückgesetzt. Falls der Raspberry Pi sich aufhängt, erfolgt dieser Reset nicht mehr und der Raspberry Pi wird nach 10 Sekunden neugestartet.

Die Schleife kann als eigenständiges Programm implementiert werden. Alternativ kann der  ``SetSleepMode``
Aufruf in der Hauptschleife einer eigenen Anwendung, die auf dem Raspberry Pi läuft, eingebaut werden, um diese gegenüber Abstürzen robust zu machen.


.. _hat_brick_real_time_clock:

Real-Time-Clock
---------------

Der HAT Brick bietet eine I2C Real-Time-Clock (Echtzeituhr), welche direkt mit 
dem Raspberry Pi verbunden ist. Die Uhr wird automatisch vom Raspberry Pi erkannt. Mit ``dmesg``
kann überprüft werden ob die Uhr korrekt erkannt wurde. Es sollte ein Eintrag
wie der folgende existieren::

	[    3.850299] rtc-pcf8523 1-0068: rtc core: registered rtc-pcf8523 as rtc0

Falls NTP nicht zur Verfügung steht, muss das Datum und Uhrzeit einmal gesetzt
werden. Anschließend kann mit folgenden Kommando:

.. code-block:: shell

	hwclock --systohc

die Uhrzeit des Raspberry Pi auf die Real-Time-Clock übertragen werden. Dies ist nur einmal notwendig.

Steht NTP zur Verfügung, so wird die Real-Time-Clock automatisch aktualisiert.

Der Brick Daemon stellt sicher, dass Datum und Uhrzeit automatisch nach einem Neustart von der
Real-Time-Clock übernommen werden.

Ohne Brick Daemon kann dies mit dem folgenden Kommando durchgeführt werden:

.. code-block:: shell

	hwclock --hctosys


Kompatibilität zu anderen Boards und Images
-------------------------------------------

Wird Raspbian genutzt, wird der HAT Brick automatisch erkannt und kann verwendet werden. 
Die Pins werden automatisch für eine Kommunikation mit Bricklets konfiguriert, indem die gespeicherte HAT-Konfiguration aus dem EEPROM des HAT Brick gelesen wird.

Wird ein Linux-Image, welches das ``raspi-config``-Framework nicht bietet,
oder ein anderes Board mit Raspberry Pi kompatiblen GPIO-Pinheadern, aber anderem Prozessor genutzt,
funktioniert das nicht automatisch.

In diesem Fall kann der Brick Daemon die notwendige SPI- und GPIO-Pinkonfiguration vornehmen, falls sie in der Datei ``/etc/brickd.conf`` angegeben wird.

Für ein Standard-Raspberry Pi beispielsweise::

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

Als erstes muss das SPI-Device, das genutzt werden soll, konfiguriert werden
(``/dev/spidev0.0`` für den Raspberry Pi). Anschließend müssen ein GPIO-Treiber,
sowie Name und Nummer des GPIOs für jeden Chip Select Pin definiert werden.
Es gibt acht Chip Selects für die acht Bricklet-Anschlüsse und ein Chip Select für
den HAT Brick selbst.

Wird ein komplett anderes Board genutzt, so kann der Schaltplan des Boards
Aufschlüsse darüber bieten, wie die Konfiguration angepasst werden muss. `tinkerunity.org <https://www.tinkerunity.org>`__ bietet eine Möglichkeit, Hilfe zu finden.


.. _hat_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: HAT_Brick_hlpi.table
