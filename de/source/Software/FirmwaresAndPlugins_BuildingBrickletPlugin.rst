
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="Firmwares_And_Plugins.html">Firmwares und Plugins</a> / Bricklet Plugin kompilieren

.. _building_bricklet_plugin:

Bricklet Plugin kompilieren
===========================

Die Plugins werden als Position Independent Code (PIC) übersetzt, so ist es für
die Bricks leichter diese zu verwenden. Das bedeutet aber auch, dass viele der
C Features die man als gegeben ansieht nicht funktionieren. Zum Beispiel können
nicht einfach Funktionen aus der Standardbibliothek aufgerufen werden. Solche
Funktionen müssen vom Brick durch die Bricklet API (BA) bereitgestellt werden.
Globale Variablen können nur im Bricklet Context (BC) gespeichert werden.
Die Konfiguration des Bricklets ist über die Bricklet Settings (BS) abrufbar.
All dies wird vom Brick bereit gestellt. Falls du dich dem gewachsen fühlst,
dann schau dir den Quelltext an um zu verstehen wie es im Detail funktioniert.

Im Folgenden wird anhand des Joystick Bricklet Plugins kurz erklärt wie man
den Quelltext kompiliert. Dies setzt voraus, dass der benötige Compiler und die
Tools installiert sind wie :ref:`hier <firmwares_and_plugins_install>`
beschrieben.


Quelltext herunterladen
-----------------------

Die Quelltexte für alle Bricks und Bricklets sind auf unserem `GitHub Account
<https://github.com/Tinkerforge/>`__ verfügbar. Das Repository für den Joystick
Bricklet findet sich `hier <https://github.com/Tinkerforge/joystick-bricklet>`__.

Der Inhalt des Repositorys kann entweder als `ZIP Datei
<https://github.com/Tinkerforge/joystick-bricklet/archive/master.zip>`__ herunter
geladen oder direkt per git Befehl geclont werden::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

Die brickletlib stellt allgemeine Funktionen für alle Bricklets bereit. Der
Inhalt des brickletlib Repositorys kann entweder als `ZIP Datei
<https://github.com/Tinkerforge/brickletlib/archive/master.zip>`__ herunter
geladen oder direkt per git Befehl geclont werden. Dabei gehört der bricklib
Ordner in den ``software/src/`` Ordner der Firmware (ein Symlink funktioniert
auch)::

 cd joystick-bricklet/software/src/
 git clone https://github.com/Tinkerforge/brickletlib.git

In der ZIP Datei ist der brickletlib Ordner als ``brickletlib-master`` benannt,
dieser muss in ``brickletlib`` umbenannt werden. Die Ordnerstruktur ist richtig
wenn z.B. der Pfad ``joystick-bricklet/software/src/brickletlib/bricklet_entry.h``
existiert.

Neben der brickletlib wird auch noch die bricklib benötigt. Der Inhalt des
bricklib Repositorys kann wieder entweder als `ZIP Datei
<https://github.com/Tinkerforge/bricklib/archive/master.zip>`__ herunter
geladen oder direkt per git Befehl geclont werden. Dabei gehört der bricklib
Ordner in den ``software/src/`` Ordner der Firmware (ein Symlink funktioniert
auch)::

 cd joystick-bricklet/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

In der ZIP Datei ist der bricklib Ordner als ``bricklib-master`` benannt,
dieser muss in ``bricklib`` umbenannt werden. Die Ordnerstruktur ist richtig
wenn z.B. der Pfad ``joystick-bricklet/software/src/bricklib/com/com.h``
existiert.


Quelltext kompilieren
---------------------

Als erstes muss aus der CMake Projektkonfiguration ein Makefile erzeugt werden.
Dazu ist im ``software/`` Ordner das ``generate_makefile`` Script auszuführen::

 cd joystick-bricklet/software/
 ./generate_makefile

Unter Windows muss ``generate_makefile.bat`` statt ``./generate_makefile``
ausgeführt werden. Dieser Schritt ist nur einmal zu Beginn und sonst nur bei
Änderungen an der CMake Projektkonfiguration notwendig.

Jetzt kann die Firmware kompiliert werden::

 cd joystick-bricklet/software/build/
 make

Es kann sein, dass folgende Fehlermeldung unter Linux auftritt::

 make[2]: S: Command not found

oder diese unter Windows::

 process_begin: CreateProcess(NULL, S -O binary servo-brick.elf servo-brick.bin, ...) failed.
 make (e=2): The system cannot find the file specified.

Um dies zu korrigieren muss das ``generate_makefile`` Script ein zweites Mal
ausgeführt werden. Es ist unklar warum dies hilft, aber es hilft. Danach muss
``make`` auch noch einmal aufgerufen werden.

Das war's. Im ``software/build/`` Ordner liegt jetzt das frisch kompilierte
Plugin: ``joystick-bricklet.bin``. Diese kann mit dem  :ref:`Brick Viewer
<brickv_flash_plugin>` auf das Bricklet geflasht werden. Im Flashing
Dialog muss dazu "Custom..." statt "Joystick" ausgewählt und die frisch
kompilierte Plugin Datei angegeben werden.
