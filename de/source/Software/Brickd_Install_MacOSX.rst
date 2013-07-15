
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="Brickd.html">Brick Daemon (brickd)</a> / Brick Daemon Installation auf Mac OS X

.. _brickd_install_macosx:

Brick Daemon Installation auf Mac OS X
======================================

Der :ref:`Brick Daemon <brickd>` kann mittels einer ``.dmg`` Datei
installiert werden.


Disk Image
----------

Als erstes muss das Brick Daemon ``.dmg`` von der :ref:`Download-Seite
<downloads_tools>` heruntergeladen werden.
Ein Klick auf die Datei sollte das Disk Image öffnen:

.. image:: /Images/Screenshots/brickd_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 1
   :align: center
   :target: ../_images/Screenshots/brickd_macos_1.jpg

Danach muss auf ``INSTALL`` geklickt werden, es sollte ein
Passwort-Abfrage geöffnet werden. Es kann aber auch folgende Fehlermeldung
angezeigt werden:

.. image:: /Images/Screenshots/brickd_macos_not_signed_1_small.jpg
   :scale: 100 %
   :alt: Brickd Installation: Fehlermeldung unter Mac OS X Mountain Lion
   :align: center
   :target: ../_images/Screenshots/brickd_macos_not_signed_1.jpg

Seit Mac OS X Mountain Lion kann ausschließlich signierte Software installiert
werden. Der Brick Daemon Installer ist im Moment nicht signiert. Daher kann
es passieren, dass Mac OS X beim Versuch den Installer zu starten die oben
gezeigte Fehlermeldung ausgibt. Als Ausweg können die Sicherheitseinstellungen
kurzzeitig abgeschwächt werden, unter:

* Systemeinstellungen
* Sicherheit
* Programme aus folgenden Quellen erlauben: Keine Einschränkungen

Jetzt noch einmal auf ``INSTALL`` klicken. Möglicherweise zeigt Mac OS X
Mountain Lion die folgende Warnung an:

.. image:: /Images/Screenshots/brickd_macos_not_signed_2_small.jpg
   :scale: 100 %
   :alt: Brickd installation: Warnung auf Mac OS X Mountain Lion
   :align: center
   :target: ../_images/Screenshots/brickd_macos_not_signed_2.jpg

Ein Klick auf "Open", es sollte nun die Passwort-Abfrage
geöffnet werden. Es werden Root-Rechte benötigt um den Brick Daemon als
Launchd Daemon zu installieren.

.. image:: /Images/Screenshots/brickd_macos_2_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 2
   :align: center
   :target: ../_images/Screenshots/brickd_macos_2.jpg

Danach sollte ein "Installation Finished" Fenster erscheinen.

.. image:: /Images/Screenshots/brickd_macos_3_small.jpg
   :scale: 100 %
   :alt: Brickd Installation Schritt 3
   :align: center
   :target: ../_images/Screenshots/brickd_macos_3.jpg

Nach einem Klick auf "OK" ist die Installation beendet. Der Brick Daemon
sollte nun bei jedem Neustart beim Hochfahren gestartet werden.

Falls der Brick Daemon nicht laufen sollte oder er abgestürzt ist, kann er
aus der Console mit folgendem Befehl gestartet werden::

 sudo launchctl start com.tinkerforge.brickd
