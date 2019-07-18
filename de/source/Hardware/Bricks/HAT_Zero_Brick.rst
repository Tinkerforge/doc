
:shoplink: ../../../shop/bricks/hat-zero-brick.html

.. include:: HAT_Zero_Brick.substitutions


.. _hat_zero_brick:

HAT Zero Brick
==============

.. raw:: html

	{% tfgallery %}
	Bricks/brick_hat_zero_tilted_top_[?|?].jpg          HAT Zero Brick Oberseite
	Bricks/brick_hat_zero_tilted_bottom_[?|?].jpg       HAT Zero Brick Unterseite
	Bricks/brick_hat_zero_tilted_w_rpi_[?|?].jpg        HAT Zero Brick mit Raspberry Pi Zero
	Bricks/brick_hat_zero_tilted_w_bricklets_[?|?].jpg  HAT Zero Brick mit Bricklets
	Bricks/brick_hat_w_hat_zero_[?|?].jpg               HAT Zero Brick und HAT Brick
	Bricks/brick_hat_zero_w_std_rpi_[?|?].jpg           HAT Zero Brick mit Raspberry Pi 4
	Bricks/brick_hat_zero_brickv_[100|].jpg             HAT Zero Brick im Brick Viewer
	Dimensions/hat_zero_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Raspberry Pi HAT mit Raspberry Pi Zero Formfaktor
* **Vier** Anschlüsse für Bricklets
* Misst die USB Versorgungsspannung


.. _hat_zero_brick_description:

Beschreibung
------------

Der HAT Zero Brick ist ein `Raspberry Pi HAT <https://www.raspberrypi.org/blog/introducing-raspberry-pi-hats/>`__
im Standard-Zero-HAT-Formfaktor. Der Brick ist zur HAT-Spezifikation konform und funktioniert automatisch
mit Raspbian ohne irgendwelche Änderungen.

Mit dem HAT Zero Brick können bis zu **vier** :ref:`Bricklets <primer_bricklets>` an ein Raspberry Pi
angeschlossen werden.

.. note::
  Das HAT Zero Brick besitzt 7-Pol-Bricklet-Anschlüsse. Über ein 7-Pol <-> 7-Pol Kabel können Bricklets
  an das Brick angeschlossen werden. Es werden nur Bricklets unterstützt die über einen 7-poligen Anschluss verfügen. 

Die USB Versorgungsspannung kann gemessen werden und ist über die API zugänglich.

Der HAT Zero Brick ist elektronisch kompatibel zu den Raspberry Pi 2B, 3B, 3B+, 4B, Zero und Zero W. Die
Befestigungslöcher snd kompatibel zum Raspberry Pi Zero und Zero W. Der Brick ist darauf ausgelegt,
möglichst wenig Platz zu benötigen. Zusätzlich bieten wir mit dem 
:ref:`HAT Brick <hat_brick>` eine größere Version mit acht Bricklet-Anschlüssen und weiteren Features. 
Die Befestigungslöcher sind bei der Version kompatibel zu den standard Raspberry Pis 2/3/4.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    90mW (18mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet-Anschlüsse               4
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           65 x 30 x 5mm (2,56 x 1,18 x 0,2")
Gewicht                           12g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/hat-zero-brick/raw/master/hardware/hat-zero-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/hat_zero_brick_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/hat-zero-brick/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2Xh7HUf>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/hat_zero/hat-zero.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/hat_zero/hat-zero.FCStd>`__)


.. _hat_zero_brick_erste_schritte:

Erste Schritte
--------------

Um mit dem HAT Zero Brick zu beginnen, muss zuerst der :ref:`Brick Daemon <brickd>`
auf dem Raspberry Pi installiert werden. Der Brick Daemon agiert als Proxy zwischen 
den Bricklet-Anschlüssen des HATs und den API Bindings.

Der Brick Daemon kann auf dem Raspberry Pi im Terminal mit folgenden Kommandos 
installiert werden:

.. code-block:: shell

	sudo apt-get install libusb-1.0-0 libudev0 pm-utils
	wget https://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
	sudo dpkg -i brickd_linux_latest_armhf.deb

Nachdem der Brick Daemon installiert ist, kann der HAT Zero Brick auf den Raspberry Pi gesteckt
und dieser neugestartet werden.

Anschließend kann der :ref:`Brick Viewer <brickv>` genutzt werden, um sich mit dem HAT Zero Brick 
und den angeschlossenen Bricklets zu verbinden. 
Der Brick Viewer kann entweder direkt auf dem Raspberry Pi oder aber auf einem externen PC,
der über WLAN Zugriff auf den Raspberry Pi besitzt, installiert werden. Von einem
externen PC aus muss sich auf den Hostnamen oder die IP des Raspberry Pis verbunden werden, vom Raspberry Pi aus auf localhost.

Im Brick Viewer sollte ein Tab namens "HAT Zero Brick" und für jedes angeschlossene Bricklet
ein weiterer Tab angezeigt werden.

.. image:: /Images/Bricks/brick_hat_zero_brickv.jpg
   :scale: 100 %
   :alt: HAT Zero Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/brick_hat_zero_brickv.jpg

Im HAT Zero Brick Tab des Brick Viewers kann die gemessene USB-Spannung betrachtet werden
und die an den HAT Zero angeschlossenen Bricklets werden angezeigt.

Sollte unklar sein, ob der HAT Zero Brick korrekt erkannt wurde, kann ein Blick in den Ordner
``/proc/device-tree/hat/`` auf dem Raspberry Pi helfen:

.. code-block:: shell

	cd /proc/device-tree/hat/
	echo Name: "$(tr -d '\0'<name)", Product: "$(tr -d '\0'<product)",  Product ID: "$(tr -d '\0'<product_id)", Vendor: "$(tr -d '\0'<vendor)"

Dies sollte etwa das folgende ausgeben::

	Name: hat, Product: HAT Zero Brick, Product ID: 0x085d, Vendor: Tinkerforge GmbH

Falls der Order nicht exisitiert, oder die Ausgabe nicht korrekt ist, war die Installation nicht erfolgreich.
Dann sollte geprüft werden, ob der HAT Zero Brick korrekt verbunden wurde und ob der Raspberry Pi nach dem aufstecken
neugestartet wurde.

HAT Zero Brick auf normalen Raspberry Pi befestigen
---------------------------------------------------

Das HAT Zero Brick kann zusammen mit einem normalen (nicht-zero) Raspbery Pi 2/3/4 verwendet werden.

.. image:: /Images/Bricks/brick_hat_zero_w_std_rpi_600.jpg
   :scale: 100 %
   :alt: HAT Zero Brick mit Raspberry Pi 4
   :align: center
   :target: ../../_images/Bricks/brick_hat_zero_w_std_rpi_1200.jpg

Zur Befestigung empfehlen wir die Nutzung eines `Raspberry Pi Befestigungskit <https://www.tinkerforge.com/de/shop/accessories/mounting/raspberry-pi-mounting-kit.html>`__.

Nutze die Zwei Montagelöcher auf der Rückseite des HATs und des RPi. Die Zwei Montagelöcher
auf der Vorderseite des HATs bleiben unbenutzt. Das HAT Zero Brick ist so bereits hinreichend
befestigt, es löst sich auch nicht bei Vibrationen. Zwei weitere Abstandshalter und Muttern
des Befestigungskits können auf der Vorderseite des RPi genutzt werden um den Aufbau eben zu
machen oder woanders zu befestigen.

Zwischen RPi und HAT Zero Brick ist genug Platz um alle vier Bricklet ports mit Bricklets
zu verbinden.

Kompatibilität zu anderen Boards und Images
-------------------------------------------

Wird Raspbian genutzt, wird der HAT Zero Brick automatisch erkannt und kann verwendet werden. 
Die Pins werden automatisch für eine Kommunikation mit den Bricklets konfiguriert, indem die gespeicherte HAT-Konfiguration aus dem EEPROM des HAT Zero Bricks gelesen wird.

Wird ein Linux-Image, welches das ``raspi-config`` Framework nicht bietet,
oder ein anderes Board mit Raspberry Pi kompatiblen GPIO-Pinheadern aber anderem Prozessor genutzt,
funktioniert dies nicht automatisch.

In diesem Fall kann der Brick Daemon die notwendige SPI und GPIO Pinkonfiguration vornehmen, falls sie in der Datei ``/etc/brickd.conf`` angegeben wird.

Für ein Standard-Raspberry Pi beispielsweise::

	bricklet.group0.spidev = /dev/spidev0.0

	bricklet.group0.cs0.driver = gpio
	bricklet.group0.cs0.name = gpio27
	bricklet.group0.cs0.num = 27

	bricklet.group0.cs1.driver = gpio
	bricklet.group0.cs1.name = gpio23
	bricklet.group0.cs1.num = 23

	bricklet.group0.cs2.driver = gpio
	bricklet.group0.cs2.name = gpio24
	bricklet.group0.cs2.num = 24

	bricklet.group0.cs3.driver = gpio
	bricklet.group0.cs3.name = gpio22
	bricklet.group0.cs3.num = 22

	bricklet.group0.cs4.driver = gpio
	bricklet.group0.cs4.name = gpio25
	bricklet.group0.cs4.num = 25

Als erstes muss das SPI-Device, das genutzt werden soll, konfiguriert werden 
(``/dev/spidev0.0`` für den Raspberry Pi). Anschließend müssen ein GPIO-Treiber,
sowie Name und Nummer des GPIO für jeden Chip Select Pin definiert werden.
Es gibt vier Chip Selects für die vier Bricklet-Anschlüsse und ein Chip Select für
den HAT Zero Brick selbst.

Wird ein komplett anderes Board genutzt, so kann der Schaltplan des Boards
Aufschlüsse darüber bieten, wie die Konfiguration angepasst werden muss. `tinkerunity.org <https://www.tinkerunity.org>`__ bietet eine Möglichkeit, Hilfe zu finden.



.. _hat_zero_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: HAT_Zero_Brick_hlpi.table
