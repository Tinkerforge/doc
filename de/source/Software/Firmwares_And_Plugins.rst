
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Firmwares und Plugins

.. _firmwares_and_plugins:

Firmwares und Plugins
=====================

.. note::
 Falls die Firmware eines Bricks oder Bricklets aus versehen gelöscht wurde,
 dann können die neusten Firmwares und Plugins :ref:`hier
 <downloads_firmwares_plugins>` heruntergeladen werden.

 Nur wenn du die Firmware eines Bricks oder das Plugin eines Bricklets nach
 deinen Vorstellungen ändern willst musst du sie selbst kompilieren.


.. _building_brick_firmware:

Brick Firmware kompilieren
--------------------------

Du kannst selbst die Firmware eines Bricks verändern und kompilieren. Im Moment
gibt es keine offizielle Brick API oder Dokumentation über den Quelltext der
Firmware. Also musst du dich schon etwas in C Programmierung auskennen und den
bestehenden Quelltext lesen.

Die Quelltexte für alle Bricks und Bricklets sind auf unserem `Github Account
<https://github.com/Tinkerforge/>`__ verfügbar. Im Folgenden wird anhand der
Servo Brick Firmware kurz erklärt wie man den Quelltext kompiliert.

Zuerst muss das Servo Brick Repository geclont werden::

 git clone https://github.com/Tinkerforge/servo-brick.git

Dann wird noch die bricklib benötigt, diese muss in den ``software/src/`` Ordner
der Firmware geclont werden (ein Symlink funktioniert auch)::

 cd servo-brick/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

Als Compiler wird GCC in der none-eabi Version für ARM benötigt. Lade eine
passende Version von
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__
herunter und installiere diese. Dabei ist auf die :ref:`Kompatiblität
des Compilers <compiler_compatibility>` zu achten.

Erzeugt das Makefile im ``software/`` Ordner (dafür wir CMake benötigt)::

 cd servo-brick/software/
 ./generate_makefile

Kompiliere die Firmware::

 cd servo-brick/software/build/
 make

Das war's. Im ``software/build/`` Ordner liegt jetzt die frisch kompilierte
Firmware: ``servo-brick.bin``.


.. _flash_firmware_on_brick:

Firmware auf Brick flashen
--------------------------

Siehe :ref:`brickv_flash_firmware` in der :ref:`Brick Viewer <brickv>`
Dokumentation für weitere Informationen.

.. _building_bricklet_plugin:

Bricklet Plugin kompilieren
---------------------------

Du kannst selbst das Plugin eines Bricklets verändern und kompilieren.
Du wirst etwas tiefere Kenntnisse in C Programmierung brauchen. Die
Plugins werden als Position Independent Code übersetzt, so ist es für die
Bricks leichter diese zu verwenden. Das bedeutet aber auch, dass viele der
C Features die man als gegeben ansieht nicht funktionieren. Zum Beispiel können
nicht einfach Funktionen aus der Standardbibliothek aufgerufen werden. Solche
Funktionen müssen vom Brick durch die Bricklet API (BA) bereitgestellt werden.
Globale Variablen können nur im Bricklet Context (BC) gespeichert werden.
Die Konfiguration des Bricklets ist über die Bricklet Settings (BS) abrufbar.
All dies wird vom Brick bereit gestellt. Falls du dich dem gewachsen fühlst,
dann schau dir den Quelltext an um zu verstehen wie es im Detail funktioniert.

Die Quelltexte für alle Bricks und Bricklets sind auf unserem `Github Account
<https://github.com/Tinkerforge/>`__ verfügbar. Im Folgenden wird anhand des
Joystick Bricklet Plugins kurz erklärt wie man den Quelltext kompiliert.

Zuerst muss das Joystick Bricklet Repository geclont werden::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

Dann wird noch die bricklib und die brickletlib benötigt, diese müssen in den
``software/src/`` Ordner des Plugins geclont werden (ein Symlink funktioniert
auch)::

 cd joystick-bricklet/software/src
 git clone https://github.com/Tinkerforge/bricklib.git
 git clone https://github.com/Tinkerforge/brickletlib.git

Als Compiler wird GCC in der none-eabi Version für ARM benötigt. Lade eine
passende Version von
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__
herunter und installiere diese. Dabei ist auf die :ref:`Kompatibilität
des Compilers <compiler_compatibility>` zu achten.

Stelle sicher, dass der ``bin`` Order der CodeSourcery Installation zur PATH
Umgebungsvariable hinzugefügt wird, ansonsten kann CMake die nötigen
Compiler Tools nicht finden.

Erzeugt das Makefile im ``software/`` Ordner (dafür wir CMake benötigt)::

 cd joystick-bricklet/software
 ./generate_makefile

Kompiliere das Plugin::

 cd joystick-bricklet/software/build/
 make

Das war's. Im ``software/build/`` Ordner liegt jetzt das frisch kompilierte
Plugin: ``joystick-bricklet.bin``.


Plugin auf Bricklet flashen
---------------------------

Siehe :ref:`brickv_flash_plugin` in der :ref:`Brick Viewer <brickv>`
Dokumentation für weitere Informationen.


.. _compiler_compatibility:

Compiler-Kompatibilität
-----------------------

Als Compiler wird GCC in der none-eabi Version für ARM von
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__
benötigt. Dabei gibt es Versionen dieses Compilers, die
keine funktionsfähige Firmware erzeugen. Daher wird empfohlen nur Versionen zu
verwenden von denen bekannt ist, dass sie richtig funktionieren:

.. csv-table::
   :header: "Version", "Funktioniert"
   :widths: 25, 5

   "Sourcery CodeBench Lite 2011.09-69, GCC 4.6.1", "Ja"
   "Sourcery CodeBench Lite 2012.03-56, GCC 4.6.3", "Ja"
   "Sourcery CodeBench Lite 2012.09-63, GCC 4.7.2", "Nein"
   "Sourcery CodeBench Lite 2013.05-23, GCC 4.7.3", "Ja"
