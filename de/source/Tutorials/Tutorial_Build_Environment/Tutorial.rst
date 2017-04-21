
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#einstieg">Einstieg</a> / Tutorial - Build-Umgebung aufsetzen

.. _tutorial_build_environment_setup:

Tutorial - Build-Umgebung aufsetzen 
===================================

Fast alles was wir bei Tinkerforge machen ist Open Soruce. Inklusive aller
Generatoren, Quelltexten, Schaltpläne, Layouts und CAD Entwürfe, welche das
Baukastensystem, bestehend aus Bricks und Bricklets, ausmachen.

Einen guten Überblick über unsere Open Source Projekte erlaubt unser
`GitHub Account <https://github.com/Tinkerforge>`__.

Wir bieten ein Skript an, welches eine Build-Umgebung für das
komplette Tinkerforge Ökosystem aufsetzt:

* `build_environment_setup.sh <https://github.com/Tinkerforge/generators/blob/master/build_environment_setup.sh>`__

Das Skript wurde mit einem Ubuntu 15.04 VirtualBox Image von `osboxes.org
<http://www.osboxes.org/>`__ getestet. Es sollte auf allen aktuellen Debian
basierten Linux Distributionen funktionieren. Für nicht-Debian basierende
Distribution müssen die Aufrufe von ``apt-get`` mit Aufrufen
der entsprechenden Gegenstücke (``yum``, ``emerge``, ``packman``, etc)
ausgetauscht werden. Falls die Distribution kein Paket für den 
``arm-none-eabi-gcc`` besitzt, kann auch der ``gcc-arm-embedded`` Compiler
`von Launchpad <https://launchpad.net/gcc-arm-embedded>`__ genutzt
werden.

Mit einer Umgebung welche mit dem obigen Skript aufgesetzt ist, kann man:

* Brick Firmwares verändern und kompilieren
* Bricklet Plugins verändern und kompilieren
* APIs/Bindings für alle unterstützten Programmiersprachen verändern und generieren
* Brick Viewer/Daemon verändern und kompilieren
* Schaltpläne und Layouts der Bricks und Bricklets ansehen und verändern (mit KiCad)
* CAD Gehäusedaten ansehen und verändern (mit FreeCAD)
* Die Dokumentation verändern und bauen

Im folgenden gehen wir davon aus das eine Build-Umgebung mit dem obigen
Skript aufgesetzt wurde.

Brick Firmwares
---------------

Zum kompilieren von Brick Firmwares muss zuerst ein Symlink zur ``bricklib``
gesetzt werden sowie eine ``Makefile`` generiert werden (als
Beispiel für den Master Brick)::

 cd ~/tf/master-brick/software/src/
 ln -sf ../../../bricklib/ .
 cd ~/tf/master-brick/software/
 ./generate_makefile

Dann kann der Quellcode mit einem normalen ``make`` Aufruf gebaut werden::

 cd ~/tf/master-brick/software/build
 make

Die gebaute Firmware liegt im ``software/build/`` Verzeichnis. In diesem
Fall ``master-brick.bin``. Sie kann mit dem 
:ref:`Brick Viewer <brickv_flash_brick_firmware>` auf ein Brick geflasht werden.
Einfach auf "Custom..." im Updates/Flashing-Dialog klicken und die frisch
kompilierte Firmware auswählen.


Bricklet Plugins
----------------

Zum kompilieren von Bricklet Plugins muss zuerst ein Symlink zur ``bricklib``
und ``brickletlib`` gesetzt werden sowie eine ``Makefile`` generiert werden 
(als Beispiel für das Temperature Bricklet)::

 cd ~/tf/temperature-bricklet/software/src/
 ln -sf ../../../bricklib/ .
 ln -sf ../../../brickletlib/ .
 cd ~/tf/temperature-bricklet/software/
 ./generate_makefile


Dann kann der Quellcode mit einem narmalen ``make`` Aufruf gebaut werden::

 cd ~/tf/temperature-bricklet/software/build
 make

Das gebaute Plugin liegt im ``software/build/`` Verzeichnis. In diesem
Fall ``temperature-bricklet.bin``. Es kann mit dem 
:ref:`Brick Viewer <brickv_flash_brick_firmware>` auf ein Bricklet geflasht werden.
Einfach auf "Custom..." im Updates/Flashing-Dialog klicken und das frisch
kompilierte Plugin auswählen.


APIs/Bindings
-------------

Wir bieten Bindings für viele Programmierspachen. Jedes der Bindings hat
eine API für alle Bricks und Bricklets. Diese Bindings und APIs werden
automatisch aus Konfigurationsdateien generiert. Wenn eine Funktion der API
hinzugefügt werden soll, muss die passende Konfigurationsdatei angepasst werden
und der Quelltext für die Funktion muss zum Brick/Bricklet Quelltext
hinzugefügt werden.

Die Generatoren für die Bindings sind alle in einem großen
`generators git repositroy <https://github.com/Tinkerforge/generators>`__.
Die Konfigurationsdateien können in ``~/tf/generators/configs/`` gefunden werden.

Im folgenden gehen wir davon aus, das wir die Funktion ``SetBreakCondition``
zur API des RS232 Bricklets hinzufügen und per Java nutzen wollen.

Dazu muss erst die Funktion erst zur Datei
``bricklet_rs232_config.py`` in ``~/tf/generators/configs/`` hinzufügen:

* `Funktion zur Konfiration hinzufügen <https://github.com/Tinkerforge/generators/commit/dc4dd52c24ab470c5582cfaa0d67690490ec5d0c>`__.

Dann muss die Funktion im Plugin-Quelltext des RS232 Bricklets implementiert
werden (siehe oben wie Bricklet Plugins kompiliert werden):

* `Funktion in Plugin implementieren <https://github.com/Tinkerforge/rs232-bricklet/commit/3139edc7d8399c9feb82570fcce061e9c9d27944>`__.

Jetzt können die Bindings regeneriert werden::

 cd ~/tf/generators/
 python generate_all.py
 python copy_all.py

Das ist alles! Die neuen Java Bindings stehen nun in 
``~/tf/generators/java/tinkerforge_java_bindings_2_x_y.zip``.
zur Verfpgung. Da wir zusätzlich das ``copy_all.py``-Skript aufgerufen
haben, sind die neuen Bindings automatisch auch im Brick Viewer
Quelltext verfügbar. Zusätzlich wurde die API Dokumentation automatisch
zum ``doc``-git hinzugefügt.

Brick Viewer/Daemon
-------------------

Der Brick Daemon befindet sich in ``~/tf/brickd/``. Er kann gebaut werden mit::

 cd ~/tf/brickd/src/brickd
 make

Die kompilierte Version kann installiert werden per::

 sudo make install

Die folgenden Kommandos können auf Debian-basierten Distributionen
ausgeführt werden um brickd automatisch beim Start auszuführen::

 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start

Der Brick Viewer befindet sich in ``~/tf/brickv/``. Er kann gebaut werden mit::

 cd ~/tf/brickv/src/brickv
 python main.py

Wenn GUI-Elemente geändert werden, muss das UI neugebaut werden bevor
brickv wieder gestartet werden kann::

 cd ~/tf/brickv/src
 python build_all_ui.py


Schaltpläne und Layouts
-----------------------

Brick/Bricklet Schaltpläne und Layouts können angesehen und modifiziert werden.
Die komplette Hardwareentwicklung der Bricks und Bricklets wurde mit dem
Open Source EDA-Werkzeug `KiCad <http://kicad-pcb.org/>`__ bewerkstelligt.

Um eine KiCad-Projektdatei zu öffnen muss zuerst ein Symlink auf das
``kicad-libraries``-git gesetzt werden (zum Beispiel für den Master Brick)::

 cd ~/tf/master-brick/hardware/
 ln -s ../../kicad-libraries/ .

Dann kann das Projekt mit KiCad geöffnet werden::

 kicad ~/tf/master-brick/hardware/master.pro

Um sich die Leiterkarte mit dem 3D-Viewer von KiCad anzusehen muss der KISYS3DMOD Pfad angepasst werden:

1. Klicken auf Preferences
2. Klicken auf Configure Paths
3. Ändern des KISYS3DMOD Pfades auf ``$HOME/tf/kicad-libraries/3d/`` (Der Pfad muss in KiCad absolut angegeben werden)
4. KiCad neustarten

KiCad funktioniert auch auf Windows und Mac OS X.

Gehäuse CAD Dateien
-------------------

Unsere lasergeschnittenen Acrylgehäuse wurden mit 
`FreeCAD <http://www.freecadweb.org/>`__ erstellt. Die Gehöuse
sind im ``cases``-git welches in ``~/tf/cases`` zu finden ist.

Beispielsweise kann die Gehäuse-Projektdatei des Ambient Light
Bricklets mit folgendem Befehl geöffent werden::

 freecad ~/tf/cases/ambient_light/ambient_light.fcstd

FreeCAD funktioniert auch auf Windows und Mac OS X.

Dokumentation
-------------

Die Dokumentation ist in
`reStructuredText <http://docutils.sourceforge.net/rst.html>`__ geschrieben.
Sie ist im ``doc``-git welches in ``~/tf/doc`` zu finden ist.

Die komplette Dokumentation kann gebaut werden mit::

 cd ~/tf/doc/
 make html

Die Dokumentation der API ist autogeneriert von den Generatoren (siehe oben).
Diese kann also nicht händisch im ``doc``-git angepasst werden.

Nach dem bauen befindet sich die Startseite der englischen Dokumentation in 
``~/tf/doc/en/build/html/index.html`` und die Startseite der deutschen 
Dokumentation in ``~/tf/doc/de/build/html/index.html``.
