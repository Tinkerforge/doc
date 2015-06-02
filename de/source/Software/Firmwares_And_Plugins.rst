
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Firmwares und Plugins

.. _firmwares_and_plugins:

Firmwares und Plugins
=====================

.. note::
 Falls die Firmware eines Bricks oder Bricklets aus versehen gelöscht wurde,
 dann können die neusten Firmwares und Plugins :ref:`hier <downloads_firmwares>`
 und :ref:` hier <downloads_plugins>` heruntergeladen werden.

 Nur wenn du die Firmware eines Bricks oder das Plugin eines Bricklets nach
 deinen Vorstellungen ändern willst musst du sie selbst kompilieren.


Du kannst selbst die Firmwares der Bricks und die Plugins der Bricklets
verändern und kompilieren. Im Moment gibt es keine offizielle Brick API oder
Dokumentation über die Quelltext der Firmwares und Plugins. Also musst du dich
schon etwas in C Programmierung auskennen und den bestehenden Quelltext lesen.


.. _firmwares_and_plugins_install:

Compiler und Tools installieren
-------------------------------

Als Compiler verwenden wir GCC für ARM von `CodeSourcery
<http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__.
Wähle EABI als Target OS und lade die Lite Edition der Sourcery CodeBench
herunter. Diese beinhaltet GCC für ARM sowie weitere Tools. Der Sourcery
CodeBench Installer ist für Linux und Windows verfügbar.

Auf 64-Bit Version von Linux müssen möglicherweise die 32-Bit Support
Bibliotheken installiert werden, damit der Compiler funktioniert. Für Debian
muss dazu nur das ``ia32-libs`` Paket installiert werden. Siehe diesen
`CodeSourcery Knowledgebase Eintrag
<https://sourcery.mentor.com/GNUToolchain/kbentry62>`__ für weitere Informationen.

Dabei gibt es Versionen dieses Compilers, die keine funktionsfähige Firmware
erzeugen. Daher wird empfohlen nur Versionen zu verwenden von denen bekannt
ist, dass sie richtig funktionieren:

.. csv-table::
   :header: "Version", "Funktioniert"
   :widths: 25, 5

   "Sourcery CodeBench Lite 2011.09-69, GCC 4.6.1", "Ja"
   "Sourcery CodeBench Lite 2012.03-56, GCC 4.6.3", "Ja"
   "Sourcery CodeBench Lite 2012.09-63, GCC 4.7.2", "Nein"
   "Sourcery CodeBench Lite 2013.05-23, GCC 4.7.3", "Ja"
   "Sourcery CodeBench Lite 2013.11-24, GCC 4.8.1", "Ja"

Nach der Installation muss der ``bin`` Order der CodeSourcery Installation zur
PATH Umgebungsvariable hinzugefügt werden. Unter Windows bietet der Installer
an dies zu übernehmen. Teste mittels des folgenden Kommandozeilenbefehls, dass
der Compiler richtig installiert ist::

 arm-none-eabi-gcc --version

Es sollten Versionsinformationen über GCC ausgegeben werden.

Also nächstes müssen CMake und make installiert werden. Auf Debian und
verwandten Linux Distribution können beide wie folgt installiert werden::

 sudo apt-get install cmake make

Ein CMake Installer für Windows ist auf der `Webseite des Projekts
<http://www.cmake.org/cmake/resources/software.html>`__ verfügbar. Das
`GnuWin32 Projekt <http://gnuwin32.sourceforge.net/packages/make.htm>`__ stellt
einen make Installer für Windows bereit. In beiden Fällen muss sichergestellt
werden, dass der ``bin`` Ordner der CMake und make Installation zur PATH
Umgebungsvariable hinzugefügt werden. Dies kann wieder mittels folgender
Kommandozeilenbefehle getestet werden::

 cmake --version

.. code-block:: none

 make --version

Es sollten Versionsinformationen über CMake und make ausgegeben werden.

Jetzt sind Compiler und Tools bereit um von der Kommandozeile aus benutzt zu
werden.


Firmwares und Plugins kompilieren
---------------------------------

Es folgen detaillierte Beschreibungen wie man den nötigen Quelltext von GitHub
herunterlädt und diesen kompiliert:

* :ref:`Brick Firmwares <building_brick_firmware>`
* :ref:`Bricklet Plugins <building_bricklet_plugin>`

.. toctree::
   :hidden:

   Brick Firmwares <FirmwaresAndPlugins_BuildingBrickFirmware>
   Bricklet Plugins <FirmwaresAndPlugins_BuildingBrickletPlugin>
