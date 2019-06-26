
:DISABLED_shoplink: ../../../shop/bricks/hat-zero-brick.html

.. include:: HAT_Zero_Brick.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _hat_zero_brick:

HAT Zero Brick
==============

.. note::
  Dieses Brick befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricks/brick_hat_zero_tilted_[?|?].jpg              HAT Zero Brick
	Bricks/brick_hat_zero_horizontal_[?|?].jpg          HAT Zero Brick
	Bricks/brick_hat_zero_brickv_[100|].jpg             HAT Zero Brick im Brick Viewer
	Dimensions/hat_zero_brick_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Raspberry Pi HAT mit RPi Zero Formfaktor
* Besitzt **vier** Anschlüsse für Bricklets
* Misst die USB Versorgungsspannung


.. _hat_zero_brick_description:

Beschreibung
------------

Der HAT Zero Brick ist ein `Raspberry Pi HAT <https://www.raspberrypi.org/blog/introducing-raspberry-pi-hats/>`__
im standard RPi Zero HAT Formfaktor. Der Brick ist zur HAT Spezifikation konform und funktioniert automatisch
mit Raspbian ohne irgendwelche Änderungen.

Mit dem HAT Zero Brick können bis zu **vier** :ref:`Bricklets <primer_bricklets>` an ein Raspberry Pi
angeschlossen werden.

Die USB Versorgungsspannung kann gemessen werden und ist über die API zugänglich.


Der HAT Brick ist elektronisch kompatibel zu den Raspberry Pi 2B, 3B, 3B+, 4B, Zero und Zero W. Die
Befestigungslöcher snd kompatibel zum Raspberry Pi Zero und Zero W. Der Brick ist darauf ausgelegt möglichst
wenig Platz zu benötigen. Zusätzlich bieten wir mit dem 
:ref:`HAT Brick <hat_brick>` eine größere Version mit acht Bricklet Anschlüssen und weiteren Features. 
Die Befestigungslöcher sind bei der Version kompatibel zu den standard Raspberry Pis 2/3/4.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    90mW (18mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Anschlüsse               4
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
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _hat_zero_brick_erste_schritte:

Erste Schritte
--------------

Um mit dem HAT Zero Brick zu beginnen muss zuerst der :ref:`Brick Daemon <brickd>`
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
der Zugriff auf den RPi besitzt (über WLAN) installiert werden. Von einem
externen PC muss sich auf die IP des Raspberry Pis verbunden werden. Ansonste auf localhost.

Im Brick Viewer sollte ein Tab (Reiter) namens "HAT Zero Brick" und für jedes angeschlossene Bricklet
ein weiteres Tab angezeigt werden.

.. image:: /Images/Bricks/hat_zero_brickv.jpg
   :scale: 100 %
   :alt: HAT Zero Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/hat_zero_brickv.jpg

Im HAT Zero Brick Tab des Brick Viewers kann die gemessene USB-Spannung betrachtet werden
und die an den HAT Zero angeschlossenen Bricklets werden angezeigt.

Sollte unklar sein, ob der HAT Zero Brick korrekt erkannt wurden kann ein Blick in den Ordner
``/proc/device-tree/hat/`` auf dem Raspberry Pi helfen:

.. code-block:: shell

	cd /proc/device-tree/hat/
	echo Name: "$(tr -d '\0'<name)", Product: "$(tr -d '\0'<product)",  Product ID: "$(tr -d '\0'<product_id)", Vendor: "$(tr -d '\0'<vendor)"

Dies sollte etwa das folgende ausgeben::

	Name: hat, Product: HAT Zero Brick, Product ID: 0x085d, Vendor: Tinkerforge GmbH

Falls der Order nicht exisitiert, oder die Ausgabe nicht korrekt ist war die Installation nicht erfolgreich.
Dann sollte geprüft werden ob der HAT Zero Brick korrekt verbunden wurde und ob der Raspberry Pi nach dem aufstecken
neugestartet wurde.

Kompatibilität zu anderen Boards und Images
-------------------------------------------

Wird Raspbian genutzt, so wird der HAT Zero Brick automatisch erkannt und genutzt. 
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

Als erstes muss das SPI Device, das genutzt werden soll konfiguriert werden 
(``/dev/spidev0.0`` für den Raspberry Pi). Anschließend muss ein GPIO Treiber,
und Name und Nummer des GPIO für jedes Chip Selects definiert werden.
Es gibt vier Chip Selects für die vier Bricklet Anschlüsse und ein Chip Select für
den HAT Zero Brick selbst.

Wird ein komplett verschiedenes Board genutzt, so kann der Schaltplan zu dem Board
Aufschlüsse bieten, wie die Konfiguration angepasst werden muss. Sollte Hilfe 
notwendig sein, bietet `tinkerunity.org <https://www.tinkerunity.org>`__
eine Möglichkeit Hilfe zu finden.



.. _hat_zero_brick_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: HAT_Zero_Brick_hlpi.table
