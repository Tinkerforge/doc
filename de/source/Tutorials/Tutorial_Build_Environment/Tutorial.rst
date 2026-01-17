
.. _tutorial_build_environment_setup:

Tutorial - Build-Umgebung aufsetzen
===================================

Fast alles was wir bei Tinkerforge machen ist Open Source. Inklusive aller
Generatoren, Quelltexten, Schaltpläne, Layouts und CAD Entwürfe, welche das
Baukastensystem, bestehend aus Bricks und Bricklets, ausmachen.

Einen guten Überblick über unsere Open Source Projekte erlaubt unser
`GitHub Account <https://github.com/Tinkerforge>`__.

Wir bieten ein Skript an, welches eine Build-Umgebung für das
komplette Tinkerforge Ökosystem aufsetzt:

* `build_environment_setup.sh <https://github.com/Tinkerforge/generators/blob/master/build_environment_setup.sh>`__

Das Skript wurde zuletzt mit einem Debian Trixie 13.3 getestet.
Es sollte auf allen aktuellen Debian
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

Docker
------

Das ``build_environment_setup.sh``-Skript erstellt eine komplette Build-Umgebung auf
dem lokalen System. Intern bei Tinkerforge nutzen wir eine Build-Umgebung in einem
Docker-Container für alle Brick/Bricklet Firmwares und den Brick Daemon. Dies stellt
sicher, dass die Builds auf allen PCs und auch auf dem Jenkins Build/Test Server
reproduzierbar sind.

Wenn die ``tinkerforge/build_environment_c`` und ``tinkerforge/build_environment_comcu`` Docker-Container installiert sind, wird
dies von den Makefiles der Firmwares automatisch erkannt und die Kompilierung findet
über einen Docker-Container statt.

Unser Docker-Container kann wie folgt installiert werden::

 apt-get install docker.io        # For Debian based distributions
 sudo usermod -aG docker <USER>   # Replace <USER> by the user that should be able to compile
                                  # through docker. You have to log in/out once after this
 docker pull tinkerforge/build_environment_c     # For Bricks and old Bricklets
 docker pull tinkerforge/build_environment_comcu # For Co-Processor Bricklets

Wenn die Brick/Bricklet Firmwares mit dem Docker-Container kompiliert werden, ist
die einzige Abhängigkeit für das Host-System GNU make.

Brick Firmwares
---------------

Zum kompilieren von Brick Firmwares muss zuerst ein Symlink zur ``bricklib``
gesetzt werden sowie eine ``Makefile`` generiert werden (als
Beispiel für den Master Brick)::

 cd ~/tf/master-brick/software/src/
 ln -sf ../../../bricklib/ .

Die Verzeichnisstruktur sollte jetzt so aussehen::

 ~/tf/
   +- bricklib/
   +- master-bricklet/
       +- software/
           +- src/
               +- bricklib -> ../../../bricklib/

Dann kann der Quellcode mit einem normalen ``make`` Aufruf gebaut werden::

 cd ~/tf/master-brick/software
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

Die Verzeichnisstruktur sollte jetzt so aussehen::

 ~/tf/
   +- bricklib/
   +- brickletlib/
   +- temperature-bricklet/
       +- software/
           +- src/
               +- bricklib -> ../../../bricklib/
               +- brickletlib -> ../../../brickletlib/

Dann kann der Quellcode mit einem normalen ``make`` Aufruf gebaut werden::

 cd ~/tf/temperature-bricklet/software
 make

Das gebaute Plugin liegt im ``software/build/`` Verzeichnis. In diesem
Fall ``temperature-bricklet.bin``. Es kann mit dem
:ref:`Brick Viewer <brickv_flash_brick_firmware>` auf ein Bricklet geflasht werden.
Einfach auf "Custom..." im Updates/Flashing-Dialog klicken und das frisch
kompilierte Plugin auswählen.


Bricklet mit Co-Prozessor Firmwares
-----------------------------------

Wir ersetzen aktuell alle alten Bricklets mit EEPROMs durch neue Bricklets
mit Co-Prozessor. Die alten Bricklets nutzten Plugins, welche vom Brick aus
einem EEPROM geladen wurden (siehe oben).

Die neuen Bricklets werden anders gehandhabt.

Als Co-Prozessor wird die XMC Mikrocontroller Serie von Infineon verwendet.
Daher wird die `XMC Peripheral Library v2.1.16 (xmclib) <https://dave.infineon.com/Libraries/XMCLib/XMC_Peripheral_Library_v2.1.16.zip>`__
von Infineon benötigt. Diese herunterladen, entpacken und einen Symlink
in ``bricklib2`` anlegen. In der Standardumgebung wid die ``xmclib`` nach
``~/tf/XMC_Peripheral_Library_v2.1.16`` entpackt::

 cd ~/tf/bricklib2/
 ln -sf ../XMC_Peripheral_Library_v2.1.16/ xmclib

Zum kompilieren von Co-Prozessor Bricklet Firmwares muss zuerst ein Symlink
zur ``bricklib2`` gesetzt sowie eine ``Makefile`` generiert werden
(als Beispiel für das Humidity Bricklet 2.0)::

 cd ~/tf/humidity-v2-bricklet/software/src/
 ln -sf ../../../bricklib2/ .

Das Co-Prozessor Bricklet baut automatisch seinen eigenen Bootloader sowie
Bootstrapper mit. Dafür müssen die gits ``brickletboot_xmc`` und
``bootstrapper_xmc`` geklont werden. Die Buildumgebung geht davon aus das
diese gits auf dem selben Verzeichnislevel liegen wie die gits der
Bricks aund Bricklets. In der Standardumgebung ist dies ``~/tf/``.
Für diese gits muss auch ein Symlink auf die ``bricklib2`` gesetzt werden::

 cd ~/tf/brickletboot_xmc/software/src/
 ln -sf ../../../bricklib2/ .
 cd ~/tf/bootstrapper_xmc/software/src/
 ln -sf ../../../bricklib2/ .

Die Verzeichnisstruktur sollte jetzt so aussehen::

 ~/tf/
   +- XMC_Peripheral_Library_v2.1.16/
   +- bricklib2/
       +- xmclib -> ../XMC_Peripheral_Library_v2.1.16/
   +- humidity-v2-bricklet/
       +- software/
           +- src/
               +- bricklib2 -> ../../../bricklib2/
   +- brickletboot_xmc/
       +- software/
           +- src/
               +- bricklib2 -> ../../../bricklib2/
   +- bootstrapper_xmc/
       +- software/
           +- src/
               +- bricklib2 -> ../../../bricklib2/

Dann kann der Quellcode mit einem normalen ``make`` Aufruf gebaut werden::

 cd ~/tf/humidity-v2-bricklet/software
 make

Das gebaute Plugin liegt im ``software/build/`` Verzeichnis. In diesem
Fall ``humidity-v2-bricklet.zbin``. Es kann mit dem
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

Dazu muss zuerst die Funktion zur Datei
``bricklet_rs232_config.py`` in ``~/tf/generators/configs/`` hinzufügt werden:

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
zur Verfügung. Da wir zusätzlich das ``copy_all.py``-Skript aufgerufen
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
Open Source EDA-Werkzeug `KiCad <http://kicad.org/>`__ bewerkstelligt.

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

KiCad funktioniert auch auf Windows und macOS.

3D Modelle erzeugen
-------------------

Im Hardwareordner der Bricks und Bricklets befinden sich ``*.step`` und ``*.FCStd`` - Dateien der Bricks und Bricklets.
Diese wurden erzeugt mit dem FreeCAD Skript `StepUp Tools <https://sourceforge.net/projects/kicadstepup/>`__.

Um das Skript benutzen zu können, müssen einige Änderungen vorgenommen werden:

1. Erzeugen der Datei  ``ksu-config.ini`` im Home-Verzeichnis. Die Datei wird beim ersten Starten des Skripts mit Inhalt gefüllt.
2. Einen Symlink auf das ``kicad-libraries``-git setzten (Beispiel: siehe oben)
3. Ändern des KISYS3DMOD Pfades auf ``$HOME/tf/kicad-libraries/3d/`` (Der Pfad muss in KiCad absolut angegeben werden)
4. Kopieren des `Skriptes <https://github.com/Tinkerforge/kicad-libraries/blob/master/3d/Scripts/kicad-StepUp-tools.FCMacro>`__ in den Ordner, in welchem sich die umzuwandelnde ``*.kicad-pcb`` befindet.
5. Das Skript einmal starten mit::

    freecad kicad-StepUp-tools.FCMacro <brick(let)-name>

6. Anpassen des ``prefix3D`` Pfades in der ``ksu-config.ini`` Datei zu ``$HOME/tf/kicad-libraries/3d/`` (Hier auch wieder als absoluten Pfad!)
7. Das Skript erneut starten.

Das Skript erzeugt eine ``*.step`` und eine ``*.FCStd`` - Projektdatei.

Das FreeCAD Makro ``kicad-StepUp-tools.FCMacro`` kann auch direkt in FreeCAD geöffnet werden um damit die erforderlichen ``*.wrl`` und ``*.step`` - Dateien zu erzeugen, die benötigt werden um im 3d Viewer von KiCad korrekt angezeigt zu werden (*.wrl) sowie die (*.step) für die
Ausführung des Scriptes. Mithilfe des Makros kann auch einfach die X/Y/Z-Achsen Ausrichtung vorgenommen werden sowie KiCad footprints laden, die als Basis dienen können für selbst erstellte 3D-Modelle.

Die vollständige Dokumentation findet sich `hier <https://github.com/Tinkerforge/kicad-libraries/raw/master/3d/Scripts/kicadStepUp-starter-Guide.pdf>`__. Desweiteren gibt es `hier <https://github.com/Tinkerforge/kicad-libraries/raw/master/3d/Scripts/kicadStepUp-cheat-sheet.pdf>`__
ein Cheat-Sheet mit einer Kurzübersicht über die wichtigsten Funktionen.

Gehäuse CAD Dateien
-------------------

Unsere lasergeschnittenen Acrylgehäuse wurden mit
`FreeCAD <https://www.freecadweb.org/>`__ erstellt. Die Gehöuse
sind im ``cases``-git welches in ``~/tf/cases`` zu finden ist.

Beispielsweise kann die Gehäuse-Projektdatei des Ambient Light
Bricklets mit folgendem Befehl geöffent werden::

 freecad ~/tf/cases/ambient_light/ambient_light.fcstd

FreeCAD funktioniert auch auf Windows und macOS.

Dokumentation
-------------

Die Dokumentation ist in
`reStructuredText <https://de.wikipedia.org/wiki/ReStructuredText>`__ geschrieben.
Sie ist im ``doc``-git welches in ``~/tf/doc`` zu finden ist.

Die komplette Dokumentation kann gebaut werden mit::

 cd ~/tf/doc/
 make html

Die Dokumentation der API ist autogeneriert von den Generatoren (siehe oben).
Diese kann also nicht händisch im ``doc``-git angepasst werden.

Nach dem bauen befindet sich die Startseite der englischen Dokumentation in
``~/tf/doc/en/build/html/index.html`` und die Startseite der deutschen
Dokumentation in ``~/tf/doc/de/build/html/index.html``.
