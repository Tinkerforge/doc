
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / WIFI Master Extension
:shoplink: ../../../shop/master-extensions/wifi-master-extension.html

.. _wifi_extension:

WIFI Master Extension
=====================

.. raw:: html

	{% tfgallery %}

	Extensions/extension_wifi_tilted_[?|?].jpg      WIFI Extension
	Extensions/extension_wifi_stack_[?|?].jpg       WIFI Extension mit Master Brick im Stapel
	Extensions/extension_wifi_horizontal_[?|?].jpg  WIFI Extension Unterseite
	Extensions/extension_wifi_bottom_[?|?].jpg      WIFI Extension Oberseite
	Extensions/extension_wifi_caption_[?|?].jpg     WIFI Extension mit Beschriftung
	Extensions/extension_wifi_ufl_[100|600].jpg     U.FL Connector der WIFI Extension
	Extensions/extension_wifi_front_[?|?].jpg       WIFI Extension Vorderseite

	{% tfgalleryend %}



.. note::
 Die WIFI Extension wurde durch die verbesserte :ref:`WIFI Extension 2.0
 <wifi_v2_extension>` abgelöst. Die alte WIFI Extension ist noch verfügbar,
 sollte aber nur dann noch verwendet werden, wenn ein externen Antennenanschluss
 benötigt wird. Dieser `Blogeintrag <httpsF://www.tinkerforge.com/de/blog/2016/6/30/wifi-extension-2-0-verfuegbar>`__
 über die WIFI Extension 2.0 beschreibt die Unterschiede genauer.


Features
--------

* Steuere Bricks/Bricklets drahtlos über Smartphone oder Tablet
* Arbeitet mit 802.11b/g/n Access Points, WEP, WPA, WPA2 Personal und Enterprise Verschlüsselung
* Ausgestattet mit einem 18dBm Verstärker für große Reichweite
* Externer RP-SMA und U.FL Antennenanschluss


Beschreibung
------------

Mit dieser WIFI Extension können :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` drahtlos mittels
Smartphone, Tablet oder PC gesteuert werden.
Weitere Informationen zum Master Extension Konzept gibt es in der allgemeinen
:ref:`Beschreibung <primer_master_extensions>`. Die Extension ist mit einem `GainSpan <http://www.gainspan.com>`__
`GS1011MEES <http://www.gainspan.com/gs1011mees>`__ WLAN Modul mit integriertem Leistungsverstärker ausgestattet
der eine erweiterte Reichweite im Vergleich zu ähnlichen Modulen erlaubt.

Die Extension unterstützt zwei Modi. Im Full Speed Modus ist der WLAN Transceiver permanent eingeschaltet.
Eingehende Daten werden unverzüglich verarbeitet. Im Low Power Mode ist das Modul nicht permanent an,
der Transceiver geht nach jeder Nachricht in den Schlafmodus.
Dies führt zu einer drastisch reduzierten Leistungsaufnahme aber auch zu einem deutlich geringeren Datendurchsatz.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, ist es möglich direkt vom
Smartphone, Tablet oder (Embedded) PC zu steuern. Der :ref:`Brick Daemon <brickd>` ist dann nicht mehr notwendig.

Um die WIFI Extension zu nutzen ist ein :ref:`Master Brick <master_brick>` notwendig.
Der :ref:`RED Brick <red_brick>` wird zurzeit nicht unterstützt.
Wenn andere Bricks gesteuert werden sollen, so kann ein :ref:`Stapel <primer_stack>` 
aus diesen gebaut werden
und auf den Master Brick gesteckt werden. Wenn Bricklets verwendet werden sollen,
so können diese einfach an der Master Brick oder andere Bricks im Stapel angeschlossen werden.
Aus der Programmierersicht ist dies absolut transparent, d.h. alle Bricks und Bricklets können
so genutzt werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick sollte eine Firmware Version von 1.3.0 oder neuer besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich.
Die Reihenfolge im Stapel ist dabei nicht relevant:

* WIFI / RS485 Master

Technische Spezifikation
------------------------

============================================  =============================================================================
Eigenschaft                                   Wert
============================================  =============================================================================
Stromverbrauch                                110mA (Senden), 23mA (im Schlafmodus)
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
Maximale Reichweite (Freifeld)                TBD
Maximaler Datendurchsatz                      TBD
Maximale Anzahl gleichzeitiger Verbindungen   15
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
RF Ausgangsstärke (Typisch)                   18dBm
Externer Antennenanschluss                    RP-SMA Female (mit Pin) und U.FL
Sicherheitsprotokolle                         WEP, WPA, WPA2 (Personal und Enterprise), EAP-FAST, EAP-TLS, EAP-TTLS, PEAP
Unterstützte Standards                        IEEE 802.11b/g/n, mit DSSS und CCK-Modulation
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
Abmessungen (B x T x H)                       40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                                       18g
============================================  =============================================================================


Ressourcen
----------

* GS1011MEES Homepage (`here <http://www.gainspan.com/gs1011mees>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/wifi-extension/zipball/master>`__)


WLAN Netzwerk
-------------

Die Master Extension erlaubt es eine drahtlose Verbindung zu
einem Master Brick und allen angeschlossenen Bricks und Bricklets herzustellen.
Es ist kein Brick Deamon notwendig um diese Extension zu nutzen.

Um den Brick Viewer mit einem drahtlosen Aufbau zu verbinden muss
die IP Adresse und der konfigurierte Port im Setup Tab eingegeben werden.
Nach dem Klick auf "Connect" wird dann eine Verbindung zu der WIFI Extension
und nicht zu dem lokal laufenden Brick Daemon hergestellt.

.. image:: /Images/Extensions/extension_wifi_brickv.jpg
   :scale: 100 %
   :alt: Brick Viewer Konfigration für WIFI Extension
   :align: center
   :target: ../../_images/Extensions/extension_wifi_brickv.jpg

Für die eigene Anwendung muss im Quelltext der übergebene Host und Port
im ``connect`` Aufruf modifiziert werden, z.B.:

.. code-block:: python

 ipcon.connect("localhost", 4223)

muss nach

.. code-block:: python

 ipcon.connect("192.168.0.25", 4223)

geändert werden.


WLAN Konfiguration
------------------

Die WIFI Extension wird über das Tab des Master Bricks im Brick Viewer
konfiguriert. Als erstes muss die SSID des WLAN Netzes eingegeben werden.
Die SSID ist der Name des WLAN Netzes zu dem sich die WIFI Extension im
Client Modus verbinden soll, bzw. der Name des WLAN Netzes das die WIFI
Extension im Access Point Modus oder Ad Hoc Modus bereitstellt (im Folgenden
geht es um den Client Modus). Die SSID kann maximal 32 ASCII Zeichen lang sein
(Anführungszeichen ist nicht erlaubt).

IP Adresse
^^^^^^^^^^

Dann zwischen DHCP oder statischer IP Adresse wählen. Für den Fall, dass DHCP
genutzt werden soll muss einfach DHCP ausgewählt werden und der Port definiert
werden.

.. image:: /Images/Extensions/extension_wifi_connection_dhcp.jpg
   :scale: 100 %
   :alt: Konfiguriere die Verbindung mit DHCP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_dhcp.jpg

Wenn eine statische IP Adresse genutzt werden soll muss diese zusammen mit
der Subnet Mask und Gateway Adresse konfiguriert werden.
Zusätzlich ist auch der Port über den kommuniziert werden soll zu konfigurieren.

.. image:: /Images/Extensions/extension_wifi_connection_static.jpg
   :scale: 100 %
   :alt: Konfiguriere die Verbindung mit statischer IP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_static.jpg

Verschlüsselung
^^^^^^^^^^^^^^^

Wir empfehlen ein verschlüsseltes Netzwerk zu nutzen.
WPA/WPA2, WPA Enterprise (EAP-FAST, EAP-TLS, EAP-TTLS, PEAP) und WEP
sind verfügbar.

Um WPA zu nutzen muss nur der Schlüssel (eingeschränkt auf ASCII Zeichen, ohne
das Anführungszeichen) eingegeben werden.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa.jpg
   :scale: 100 %
   :alt: Konfiguriere WPA Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa.jpg

Für WPA Enterprise muss die äußere Authentifizierung
(FAST, TLS, TTLS, PEAP), die innere (MSCHAP, GTC), Benutzer und Passwort
konfiguriert werden sowie die notwendigen Zertifikate (ca cert, client cert, private key)
hinzugefügt werden.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg
   :scale: 100 %
   :alt: Konfiguriere WPA Enterprise Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg

Um WEP zu benutzen muss ein Schlüssel und ein Schlüssel Index eingegeben werden.
Ist kein Index bekannt so ist dieser vermutlich 1.
Der Schlüssel ist hierbei in Hex-Notation einzutragen mit voller Schlüssellänge
(abhängig von 64bit und 128bit Schlüssel).

.. image:: /Images/Extensions/extension_wifi_encryption_wep.jpg
   :scale: 100 %
   :alt: Konfiguriere WEP Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wep.jpg

.. note::
 WEP Verschlüsselung ist gebrochen und bietet keine Sicherheit mehr. Daher wird
 dringend dazu geraten stattdessen WPA/WPA2 Verschlüsselung zu verwenden.

Soll keine Verschlüsselung genutzt werden muss "No Encryption" gewählt werden.

Power Mode
^^^^^^^^^^

Nun kann noch der Power Mode konfiguriert werden. Es gibt zwei Modi:
Full Speed und Low Power. Im Full Speed Modus verbraucht die Extension mehr Leistung
besitzt aber einen deutlich höheren Datendurchsatz. Dies ist für die meisten Anwendungen
die typische Konfiguration. Müssen nur ein paar Nachrichten pro Sekunden transferiert werden,
z.B. bei der drahtlosen Temperaturmessung, so kann auch der Low Power Mode gewählt
und Energie gespart werden.

.. image:: /Images/Extensions/extension_wifi_power_mode.jpg
   :scale: 100 %
   :alt: Konfiguriere Power Mode
   :align: center
   :target: ../../_images/Extensions/extension_wifi_power_mode.jpg

.. note::
 Der Power Mode wird nicht permanent gespeichert, er wird beim Neustart des Master Bricks automatisch
 auf Full Speed zurückgestellt. Dies ist notwendig, da der Low Power Mode nicht
 schnell genug ist für die initiale Enumerierung nach einem Neustart. Daher muss
 der Low Power Mode nach jedem Neustart neu eingestellt werden.

Zum Schluss muss auf "Save WIFI Configuration" geklickt werden um die Konfiguration
dauerhaft auf der WIFI Extension zu speichern.
Falls andere Einstellungen als der Power Mode geändert wurden muss der Master Brick
neu gestartet werden um die neue Konfiguration zu übernehmen. Nach dem Neustart
sollte der Master Brick bei Eingabe der konfigurierten IP Adresse und Port im Brick Viewer erreichbar sein.

Beispiel: Client Modus mit dynamischer IP Adresse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Diese Beispiel zeigt wie die WIFI Extension eingestellt werden muss, damit sie
sich zu einem typischen WLAN Access Point verbindet. Für diese Beispiel wird
angenommen, dass die SSID des Access Points "MyHomeNetwork" lautet und WPA/WPA2
als Verschlüsselung mit Schlüssel "1234567890ABCDEF" verwendet wird.

Dazu als erstes im Brick Viewer die SSID (Name des WLAN Netzes) eingeben zu
der eine Verbindung hergestellt werden soll. Ein Beispiel:

* SSID: MyHomeNetwork

Dann einen Hostnamen eingeben. Mit diesem kann dann eine Verbindung zur WIFI
Extension aufgebaut werden ohne vorher deren dynamische IP Adresse ermitteln zu
müssen. Ein Beispiel:

* Hostname: WIFI-Extension

Als nächstes "Client: DHCP" für Mode und Address und "WPA/WPA2" für Encryption
auswählen und den WPA/WPA2 Schlüssel eingeben. Ein Beispiel:

* Key: 1234567890ABCDEF

Dann die WIFI Konfiguration speichern und den Master Brick neustarten. Jetzt
sollte sich die WIFI Extension zum Access Point verbinden und dann im eigenen
Programm und im Brick Viewer unter dem eingestellten Hostnamen "WIFI-Extension"
erreichbar sein.


Access Point Modus und Ad Hoc Modus
-----------------------------------

.. note::
 Access Point und Ad Hoc Modus stehen ab Master Brick Firmware
 Version 1.3.3 und Brick Viewer Version 1.1.8 zur Verfügung.

Es ist möglich direkt mit der WIFI Extension zu kommunizieren, ohne einen
zusätzlichen externen Access Point. Um dies zu ermöglichen wurde ein
Access Point und ein Ad Hoc Modus implementiert. Da der Ad Hoc Modus
vom sich verbindenden Gerät spezifisch unterstützt werden muss,
empfehlen wir die Verwendung des Access Point Modus. Im AP Modus
simuliert die WIFI Extension einen Access Point und sie sollte
als ganz normaler Access Point auf dem PC angezeigt werden.

.. image:: /Images/Extensions/extension_wifi_connection_adhoc_ap.jpg
   :scale: 100 %
   :alt: Konfiguration von Ad Hoc und Access Point Modus
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_adhoc_ap.jpg

Es ist möglich bei beiden Modi zwischen DHCP und statischer IP auszuwählen.
Falls DHCP ausgewählt wird, muss der DHCP Server von außen bereitgestellt werden!
Es gibt keine DHCP Server Implementierung auf dem WLAN Modul. Da das aufsetzen
eines DHCP Servers mühselig sein kann, empfehlen wir die Benutzung einer
statischen IP.

Als Verschlüsselung steht WEP zur Verfügung. WPA wird
im Ad Hoc und Access Point Modus leider nicht unterstützt. Der WEP Schlüssel
sollte 64 oder 128 Bit groß sein und in hexadezimaler Schreibweise angegeben
sein. Gültige WEP Schlüssel können
`hier <http://www.andrewscompanies.com/tools/wep.asp>`__ generiert werden.

Beispiel: Access Point Modus mit statischer IP Adresse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Als Beispiel wird hier die WIFI Extension als Access Point mit statischer
IP Adresse konfiguriert und mit einem Android Smartphone verbunden.

Dazu als erstes im Brick Viewer die SSID (der Name des WLAN Netzes)
festlegen. Dabei ist darauf zu achten, dass der Name nicht schon von einem
anderen WLAN Netz in der Nähe verwendet wird. Ein Beispiel:

* SSID: TinkerforgeWLAN

Dann Mode und Address auf "Access Point: Static IP" stellen und IP, Subnet Mask
und Gateway einstellen. Ein Beispiel:

* IP: 192.168.1.17
* Subnet Mask: 255.255.255.0
* Gateway: 192.168.1.1

Als Encryption "No Encryption" oder "WEP" wählen. Falls "WEP" verwendet wird
muss noch ein Key eingegeben werden. Ein 64 oder 128 Bit WEP Schlüssel kann
`hier <http://www.andrewscompanies.com/tools/wep.asp>`__ generiert werden.
Der Key muss in hexadezimaler Schreibweise eingeben werden.

.. note::
 WEP Verschlüsselung ist gebrochen und bietet keine Sicherheit mehr. Leider
 unterstützt die WIFI Extension keine WPA/WPA2 Verschlüsselung im Ad Hoc und
 Access Point Modus.

Dann die WIFI Konfiguration speichern und den Master Brick neustarten. Jetzt
sollte WIFI Extension einen Access Point bereitstellen.

Am Android Smartphone die WLAN Einstellungen aufrufen und ein neues Netzwerk
hinzufügen. Dazu die SSID der WIFI Extension eingeben (Standard:
TinkerforgeWLAN) und für Sicherheit "Keine" oder "WEP" entsprechend der
Einstellung der WIFI Extension wählen. Für WEP dann den gewählten Schlüssel als
Passwort in hexadezimaler Schreibweise eingeben.

Da die WIFI Extension keinen DHCP Server beinhaltet muss nun noch unter den
Erweiterten Optionen eine statische IP Adresse für das Smartphone eingegeben
werden. Dazu die IP-Einstellung von "DHCP" auf "Statisch" ändern und
IP-Adresse, Gateway und Länge Netzwerkpräfix einstellen. Ein Beispiel:

* IP-Adresse: 192.168.1.23
* Gateway: 192.168.1.1
* Länge Netzwerkpräfix: 24

Dann Speichern und mit dem Netzwerk verbinden. Jetzt sollte das Smartphone mit
dem Access Point der WIFI Extension verbunden sein.


.. _wifi_extension_authentication:

Authentifizierung
-----------------

Die WIFI Extension unterstützt seit Master Brick Firmware Version 2.2.0
Authentifizierung. Diese ist standardmäßig deaktiviert. Um
Authentifizierung zu aktivieren muss das Häkchen bei "Use Authentication"
gesetzt und ein Authentifizierungsgeheimnis eingetragen werden. Das Geheimnis
kann maximal 64 ASCII Zeichen lang sein. Nachdem die Konfiguration gespeichert
und der Master Brick neugestartet wurde ist Authentifizierung aktiv.

.. image:: /Images/Extensions/extension_wifi_authentication.jpg
   :scale: 100 %
   :alt: Configure Authentication
   :align: center
   :target: ../../_images/Extensions/extension_wifi_authentication.jpg

Ab jetzt muss jede TCP/IP Verbindung zur WIFI Extension zuerst nachweisen,
dass sie das Authentifizierungsgeheimnis kennt, bevor normale Kommunikation
stattfinden kann. Für mehr Informationen zur Authentifizierung siehe das
dazugehörige :ref:`Tutorial <tutorial_authentication>`.


LEDs und Anschlussmöglichkeiten
-------------------------------

.. image:: /Images/Extensions/extension_wifi_caption_600.jpg
   :scale: 100 %
   :alt: WIFI Extension mit Beschriftung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_caption_800.jpg

Die blaue LED leuchtet permanent wenn die Extension mit Strom versorgt wird.
Als Status LED ist eine grüne LED vorhanden (permanent aus = Fehler,
blinkend = Verbindungsaufbau, permanent an = Verbunden).

Das WLAN Modul ist mit einem U.FL Anschluss und einem 75Ω U.FL nach RP-SMA
Kabel ausgestattet. Abhängig von der Anwendung kann dieses Kabel auch vom WLAN
Modul getrennt und ein eigenes angeschlossen werden.


Programmierschnittstelle
------------------------

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interface>`.
