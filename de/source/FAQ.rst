
:breadcrumbs: <a href="index.html">Startseite</a> / <a href="index.html#tutorials-und-faq">Tutorials und FAQ</a> / FAQ

.. _faq:

FAQ
===

Allgemeine Informationen zu Bricks, Bricklets und Master Extensions sowie
zu deren Benutzung können auf der :ref:`Einführungsseite <primer>` gefunden 
werden.


Mein Programm funktioniert nur wenn Brick Viewer läuft
------------------------------------------------------

Dann benutzt dein Programm wahrscheinlich Callbacks ohne sie richtig zu
aktivieren. Brick Viewer benutzt auch Callbacks und aktiviert sie wenn der Tab
eines Bricks oder Bricklets ausgewählt wird. Da die Einstellungen der Callbacks
global sind ist dann der Callback auch für dein Programm aktiviert.

Die Lösung ist also die verwendeten Callbacks richtig zu konfigurieren und
aktivieren im Programm. Die Dokumentation des Callbacks beschreibt wie dies
zu tun ist.


.. _faq_brick_hot:

Mein Brick wird heiß
--------------------

Für gewöhnlich bedeutet dies, dass es irgendeine Art von Kurzschluss
gibt. In den meisten Fällen handelt es sich dabei um leicht verbogene
Beinchen in einem der Bricklet Stecker:

.. image:: /Images/FAQ/bricklet_connector_short_circuit.jpg
   :scale: 100 %
   :alt: DON'T PANIC 
   :align: center

In diesem Fall können die Beinchen einfach zurückgebogen werden.


Eines meiner Bricklets wird im Brick Viewer nicht angezeigt
-----------------------------------------------------------

**Defektes Plugin**:

Es ist möglich, dass das Plugin auf dem EEPROM des Bricklets
defekt oder gar nicht vorhanden ist.

In diesem Fall sollte es neu neu geflasht werden. Falls ein Brick nicht
im Brick Viewer auftaucht wenn das Bricklet angesteckt ist, ist es möglich
das Bricklet anzustecken nachdem das Brick bereits gestartet hat. Danach
kann das Bricklet wie :ref:`hier <brickv_flash_plugin>` beschrieben
aktualisiert werden.

Falls das Flashen nicht funktioniert: Schon ein anderes Bricklet Kabel
ausprobiert?

**Ungültige UID**:

Falls das EEPROM eines Bricklets korrupt ist, kann auch die UID
ungültig sein. Eine UID von "1" ist ungültig. Falls mit dem Brick
Viewer eine "1" als UID von einem Bricklet gelesen werden kann, muss eine
neue UID gesetzt werden. Diese sollte im ganzen System eindeutig sein
und muss als `Base58 <http://de.wikipedia.org/wiki/Base58>`__ kodiert sein.

**Kurzschluss im Bricklet-Stecker**:

Ein Kurzschluss kann durch leicht verbogene Beinchen im Bricklet-Stecker
auftreten, siehe :ref:`oben <faq_brick_hot>`. Dies gilt sowohl
für den benutzten Brick als auch das benutzte Bricklet.

**Defektes Bricklet Kabel**:

Um auszuschließen, dass das Problem durch ein defektes Bricklet Kabel
erzeugt wird, teste mit einem anderen Bricklet Kabel. Sofern dies möglich ist.


Eines meiner Bricks wird im Brick Viewer nicht angezeigt
--------------------------------------------------------

**Brick im Bootloader**:

Es ist möglich, dass der Brick unbeabsichtigt in den Bootloader
gebracht wurde. Dies kann man daran erkennen, dass keine der LEDs mehr
leuchtet. In diesem Fall muss die 
:ref:`Brick Firmware neu geflasht <brickv_flash_firmware>`
werden.

**Kurzschluss im Bricklet-Stecker**:

Ein Kurzschluss kann durch leicht verbogene Beinchen im Bricklet-Stecker
auftreten, siehe :ref:`oben <faq_brick_hot>`.

**Brick Treiber Installation notwendig**:

Unter älteren Windows Versionen ist eine Treiberinstallation notwendig.
Siehe :ref:`hier <brickd_install_windows_driver>`.

**Renesas/NEC USB 3.0 Controller mit altem Treiber**:

Falls der Brick an einem Renesas/NEC USB 3.0 Controller (µPD720200)
angeschlossen ist, dann muss mindestens Treiberversion 2.1.16 für diesen
Controller installiert sein. Ältere Treiberversionen haben einen Bug, der
brickd daran hindert Bricks zu sehen, die an einen solchen USB Controller
angeschlossen sind.

Treiberupdates gibt es auf `usb3-drivers.com
<http://www.usb3-drivers.com/renesas-usb3-drivers.html>`__ und `computerbase.de
<http://www.computerbase.de/downloads/treiber/usb-3.0-host-controller-treiber/>`__.


Eine Extension wird im Brick Viewer nicht angezeigt
---------------------------------------------------

**Die Extension ist unter dem Master Brick**:

Extensions müssen über Master Bricks gesteckt werden. Wird ein Stapel gebaut, so
können andere Bricks dazwischen gesteckt werden. Das Master Brick sollte aber die 
unterste Platine des Stapels sein. Einzige Ausnahme ist die Nutzung einer 
Stromversorgungen wie die Step-Down Power Supply.


**Die Extension ist nicht konfiguriert**:

Schließe ein einzelnes Master Brick an den PC an und öffne den Brick Viewer.
Nachdem das Master Brick Tab angezeigt wird, stecke die Extension auf das Master 
Brick und öffne das Tab. Klicke auf "Configure", wähle Extension 0 und den Typ 
der Extension. Klicke "Save". Danach starte den Master Brick neu. Im Master 
Brick Tab sollte nun die gewählte Extension angezeigt werden.

.. image:: /Images/Screenshots/brickv_configure_extension_type.jpg
   :scale: 60 %
   :alt: Screenshot vom Brickv Configure Extension Type Dialog 
   :align: center


Ich bekomme Timeouts wenn ich eine Funktion aufrufe
---------------------------------------------------

**UID**:

Überprüfe die UID. Die Brick/Bricklet Objekte müssen mit der korrekten
UID angelegt werden. Wenn die UID nicht korrekt ist, kann auf eine
Anfrage nicht geantwortet werden da die Anfrage nicht korrekt
geroutet wird im System.

**Brick Daemon**:

Läuft der Brick Daemon? Dies kann man in der Liste der laufenden
Prozesse nachsehen (zum Beispiel im Task Manager unter Windows).

Falls er nicht läuft aber korrekt installiert ist, ist es möglich
den Service (Windows) oder den Daemon (Mac OS X und Linux) neu zu starten.
Der Brick Daemon wird auch automatisch beim Rechnerneustart gestartet.

**WIFI Extension**:

Wurde die IP Adresse der WIFI Extension genutzt? Wenn eine direkt
Verbindung aufgebaut werden soll, muss die IP Adresse der WIFI Extension
anstatt "localhost" zum Verbinden genutzt werden.


Ich bekomme keine Timeouts wenn ich eine Funktion aufrufe
---------------------------------------------------------

Falls ein Timeout erwartet wird (zum Beispiel weil ein Brick oder Bricklet
nicht angeschlossen ist) aber keiner ausgelöst wird liegt das vermutlich
daran, dass ein "Setter" aufgerufen wurde. Normalerweise warten Funktionen
die nichts zurückgeben nicht auf einem Antwort von Bricks oder Bricklets.

Es ist allerdings möglich dies umzustellen.
Dazu dient die ``SetResponseExpected`` Funktion, diese ist in der API
Dokumentation der Bricks/Bricklets beschrieben.


Die Strommessung meiner Step-Down Power Supply funktioniert nicht
-----------------------------------------------------------------

Die Messung ist auf hohe Ströme ausgelegt. Falls nur ein einziger
Master Brick an der Step-Down Power Supply angeschlossen ist
kann es passieren, dass der Master zu wenig Strom zieht um überhaupt
erkannt zu werden (d.h. ``GetStackCurrent`` gibt 0 zurück).


Mein Brick taucht nicht als serielle Schnittstelle für's Flashing auf
---------------------------------------------------------------------

**Brick nicht im Bootloader**:

Ein Brick kann nur geflasht werden wenn er im Bootloader Modus ist. Um in den
Bootloader zu wechseln muss der Erase Knopf gedrückt gehalten und dabei der
Reset Knopf einmal gedrückt werden. Die blaue LED sollte jetzt aus sein.

**Treiber nicht installiert (auf Windows)**:

Auf Windows kann es nötig sein den Atmel Treiber ``atm6124_cdc.inf`` aus dem
``drivers`` Unterordner der Brick Viewer Installation zu installieren, damit ein
Brick im Bootloader Modus richtig als serielle Schnittstelle erkannt wird.

Windows 7 und 8 erkennen einen Brick im Bootloader Modus normalerweise von sich
aus als "GPS Camera Detect" Gerät. Dann einfach "GPS Camera Detect" als serielle
Schnittstelle im Brick Viewer auswählen.

**Master Brick 2.0 im Stack mit Master Extension**:

Master Brick Hardware Version 2.0 hat eine Änderung im Leiterplattenlayout die
den Bootloader Modus stört wenn eine Master Extension wie WIFI, RS485 oder
Ethernet im Stack vorhanden ist. In diesem Fall muss die Master Extension aus
dem Stack entfernt werden, damit der Bootloader Modus richtig funktioniert.

**/dev/ttyACM0 ist nicht zugreifbar für User (auf Linux)**:

Es kann sein, dass serielle Schnittstellen auf Linux nicht für User zugreifbar
konfiguriert sind. Sie tauchen in Brick Viewer auf, beim Versuch zu Flashen
wird aber eine Fehlermeldung ausgegeben. Dieses Problem kann umgangen werden,
indem zum Flashen Brick Viewer als ``root`` gestartet wird.

Ich habe etwas aktualisiert und jetzt funktioniert es nicht mehr
----------------------------------------------------------------

**Version < 2.0:**

Es handelt sich vermutlich um ein Problem mit inkompatiblen Versionen.
Am 22. Januar 2013 haben wir eine neue Protokollversion veröffentlicht:
Protokoll 2.0. Die Art und Weise wie Bricks und Bricklets
untereinander und mit dem Brick Daemon kommunizieren hat sich
dadurch geändert. Es gibt auch kleine Änderungen in der API. Es ist
daher notwendig, dass die Programmiersprachen Bindings, der Brick
Daemon, der Brick Viewer und die Firmwares/Plugins der Bricks/Bricklets
auf den neuesten Stand gebraucht werden. Alle Versionen müssen mit
einer "2" beginnen um miteinander kompatibel zu sein.

Eine Anleitung zum Aktualisieren gibt es
:ref:`hier <transition_1to2>`.

**Brick Firmware Version < 2.3:**

Am 26. November 2014 haben wir ein neues SPI-Stack-Protokoll veröffentlicht um
Unterstützung für den RED Brick hinzuzufügen. Dieses Protokoll ist nicht
kompatibel zum alten Protokoll. Um eine fehlerfreie Stack-Kommunikation
sicherzustellen sollten alle Bricks eine Firmware Version von mindestens
2.3 haben.
