
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="Firmwares_And_Plugins.html">Firmwares und Plugins</a> / Brick Firmware kompilieren

.. _building_brick_firmware:

Brick Firmware kompilieren
==========================

Im Folgenden wird anhand der Servo Brick Firmware kurz erklärt wie man den
Quelltext kompiliert. Dies setzt voraus, dass der benötige Compiler und die
Tools installiert sind wie :ref:`hier <firmwares_and_plugins_install>`
beschrieben.


Quelltext herunterladen
-----------------------

Die Quelltexte für alle Bricks und Bricklets sind auf unserem `GitHub Account
<https://github.com/Tinkerforge/>`__ verfügbar. Das Repository für den Servo
Brick findet sich `hier <https://github.com/Tinkerforge/servo-brick>`__.

Der Inhalt des Repositorys kann entweder als `ZIP Datei
<https://github.com/Tinkerforge/servo-brick/archive/master.zip>`__ herunter
geladen oder direkt per git Befehl geclont werden::

 git clone https://github.com/Tinkerforge/servo-brick.git

Die bricklib stellt allgemeine Funktionen für alle Bricks bereit. Der
Inhalt des bricklib Repositorys kann wieder entweder als `ZIP Datei
<https://github.com/Tinkerforge/bricklib/archive/master.zip>`__ herunter
geladen oder direkt per git Befehl geclont werden. Dabei gehört der bricklib
Ordner in den ``software/src/`` Ordner der Firmware (ein Symlink funktioniert
auch)::

 cd servo-brick/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

In der ZIP Datei ist der bricklib Ordner als ``bricklib-master`` benannt,
dieser muss in ``bricklib`` umbenannt werden. Die Ordnerstruktur ist richtig
wenn z.B. der Pfad ``servo-brick/software/src/bricklib/com/com.h`` existiert.


Quelltext kompilieren
---------------------

Als erstes muss aus der CMake Projektkonfiguration ein Makefile erzeugt werden.
Dazu ist im ``software/`` Ordner das ``generate_makefile`` Script auszuführen::

 cd servo-brick/software/
 ./generate_makefile

Unter Windows muss ``generate_makefile.bat`` statt ``./generate_makefile``
ausgeführt werden. Dieser Schritt ist nur einmal zu Beginn und sonst nur bei
Änderungen an der CMake Projektkonfiguration notwendig.

Jetzt kann die Firmware kompiliert werden::

 cd servo-brick/software/build/
 make

Es kann sein, dass folgende Fehlermeldung unter Linux auftritt::

 make[2]: S: Command not found

oder diese unter Windows::

 process_begin: CreateProcess(NULL, S -O binary servo-brick.elf servo-brick.bin, ...) failed.
 make (e=2): The system cannot find the file specified.

Um dies zu korrigieren muss das ``generate_makefile`` Script ein zweites Mal
ausgeführt werden. Es ist unklar warum dies hilft, aber es hilft. Danach muss
``make`` auch noch einmal aufgerufen werden.

Das war's. Im ``software/build/`` Ordner liegt jetzt die frisch kompilierte
Firmware: ``servo-brick.bin``. Diese kann mit dem  :ref:`Brick Viewer
<brickv_flash_firmware>` auf den Brick geflasht werden. Im Flashing
Dialog muss dazu "Custom..." statt "Servo" ausgewählt und die frisch
kompilierte Firmware Datei angegeben werden.
