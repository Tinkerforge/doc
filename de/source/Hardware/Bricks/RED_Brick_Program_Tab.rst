
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / <a href="RED_Brick.html">RED Brick</a> / Program Tab
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick_program_tab:

RED Brick Program Tab
=====================


Beschreibung
------------

Der Program Tab ist der wichtigste Teil in der Brick Viewer Ansicht des RED 
Bricks. Er dient dazu Programme hochzuladen, zu modifizieren und zu verwalten.

.. image:: /Images/Screenshots/red_brick_program_overview.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Program Tabs.
   :align: center

Wenn der RED Brick das erste mal gestartet wird ist die Programmliste leer.
Mit drei Buttons unter der Programmliste können folgende Aktionen durchgeführt 
werden:

* **Refresh**: Aktualisiert die Liste
* **New**: Startet den "New Program Wizard"
* **Delete**: Löscht das ausgewählte Programm

Nachdem das erste eigene Programm hochgeladen wurde, kann dieses ausgewählt 
werden. Auf der rechten Seite werden dann Informationen zu dem Programm 
angezeigt. Dazu gehört die Programm-Konfiguration, die geändert werden kann
und die Logs des Programms.


Ein eigenes Programm kann auf den RED Brick in 8 einfachen Schritten hochgeladen
werden:

Wizard Schritt 1: Einfache Informationen
----------------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step1.jpg
   :scale: 60 %
   :alt: Screenshot der RED Brick Wizard Schritt 1.
   :align: center

* Name: Dies ist der Name des Programms. Er wird in der Programmliste angezeigt
  und dient auch an vielen anderen Stellen zur Identifikation.
* Language: Wählt die Programmiersprache des Programms
* Description: Der eingegebene Text wird als Beschreibung angezeigt, wenn das 
  Programm ausgewählt wird.
* Unique Identifier: Wenn *Auto-generate unique identifier* abgewählt wird, muss
  ein eigener eindeutiger Bezeichner gewählt werden. Dieser wird hauptsächlich 
  intern verwendet und dient zum Beispiel zur Benennung des Programmordners
  im Linux System.

Wizard Schritt 2: Dateien
-------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step2.jpg
   :scale: 60 %
   :alt: Screenshot der RED Brick Wizard Schritt 2.
   :align: center

* **Add files**: Fügt einzelne Programm-Dateien hinzu.
* **Add Directory**: Fügt einzelne Programm-Ordner, deren enthaltenen Dateien 
  und Unterordner hinzu.
* **Remove**: Löscht die selektierte Datei oder Ordner.

Die hierarchische Struktur die hier definiert wird, wird eins zu eins auf dem
RED Brick genutzt.

Wenn als Beispiel eine kleine Webseite, die mit Python/Flask geschrieben wurde, 
mit folgender Struktur hochgeladen werden soll

* myproject/

  * index.py
  * templates/
 
    * template1.html
    * template2.html

  * static/

    * static.css
    * static.js

und sowohl index.py als auch die beiden Ordner in dem Root Verzeichnis seien 
sollen, muss als erstes die index.py mit **Add files** hinzugefügt werden. 
Anschließend muss jedes Unterverzeichnis einzelnd mit **Add Directory** 
hinzugefügt werden.

Jedes "Add" fügt etwas zum Root Verzeichnis des RED Brick Programms hinzu.

* Bei JavaScript, Perl, PHP, Python und Ruby können die Script-Dateien hochgeladen werden (z.B.: .js, .pl, .php, .py, .rb)
* Bei Java, C# und Visual Basic .NET müssen bereits kompilierte Dateien hochgeladen werden (z.B.: .jar, .class, .exe)
* Bei C/C++ und Delphi/Lazarus kann eine cross-kompilierte ausführbare Datei (executeable) oder eine Makefile mit Source Code hochgeladen werden (siehe folgende Beschreibung)



Wizard Schritt 3: Sprachen spezifische Konfiguration
----------------------------------------------------

In Schritt 3 werden die Compiler/Interpreter Einstellungen, der in Schritt 1
spezifizierten Sprache, vorgenommen. Dieser Schritt ist nachfolgend für jede
Sprache dokumentiert.

C/C++
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_c.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (C/C++).
   :align: center

Die Tinkerforge C/C++ Bindings sind auf dem RED Brick vorinstalliert
(Kompiliert als Bibliothek libtinkerforge.so, verfügbar in ``/usr/lib/``).
Die Header sind verfügbar in ``/usr/include/tinkerforge``. Es kann direkt gegen 
die Bibliothek gelinkt werden (siehe das nachfolgende Beispiel).

* Start Mode: Aktuell ist nur *Executable* verfügbar.
* Executable: Name der ausführbaren Datei, die aufgerufen werden soll. Diese ist 
  entweder eine Cross-Kompilierte Datei, die direkt mit hochgeladen wurde oder 
  es ist der Name der ausführbaren Datei, die während des Kompilierens erstellt 
  wird.
* Compile From Source: Wird diese Checkbox aktiviert, so wird der Code nach dem
  Hochladen kompiliert. Eine **Makefile** muss in dem Projekt enthalten sein, damit 
  diese Option genutzt werden kann. Nachfolgend eine Beispiel-Makefile für ein 
  kleines  Projekt, das die Tinkerforge Bindings benutzt und die Datei
  **example.c** kompiliert::

    # Defines
    CC=g++
    CFLAGS=-c -Wall -I/usr/include/tinkerforge
    LIBS=-ltinkerforge -lpthread
    EXE=example
    SOURCES=example.c
    OBJECTS=$(SOURCES:.c=.o)

    # Build Rules
    all: $(SOURCES) $(EXE)

    .c.o:
    	$(CC) $(CFLAGS) $< -o $@

    $(EXE): $(OBJECTS)
    	$(CC) $(OBJECTS) -o $(EXE) $(LIBS)

    clean:
    	rm -f *.o $(EXE)
* Make options: Wenn vom Source kompiliert wird, könnnen hier Makefile Parameter
  angegeben werden.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.

C#
^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_csharp.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (C#).
   :align: center

Die C# Tinkerforge.dll ist in ``/usr/lib/`` verfügbar und wird daher von Mono
direkt gefunden. Jedes C# Programm, dass die Tinkerforge.dll als Referenz nutzt,
kann also ohne Angabe der Tinkerforge.dll im vorherigen Schritt (Schritt 2) 
kompiliert werden.

* Mono Version: Aktuell ist nur eine Mono Version installiert.
* Start Mode: Aktuell ist nur *Executable* verfügbar.
* Executable: Wähle die ausführbare .NET Datei, die in Schritt 2 hinzugefügt 
  wurde. Diese Datei hat typischerweise die Endung .exe.

  Die ausführbare Datei wird mit `Mono <http://www.mono-project.com/>`__ 
  ausgeführt. Die Datei kann auch unter Windows mit Visual Studio kompiliert 
  und auf dem RED Brick mit Mono ausgeführt werden, dabei muss allerdings darauf
  geachtet werden, dass keine Windows spezifischen Bibliotheken genutzt werden, 
  die auf dem   RED Brick nicht verfügbar sind.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Mono Options: Hier können Optionen angegeben werden, die dem Mono JIT Compiler
  übergeben werden.

Delphi/Lazarus
^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_delphi.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Delphi/Lazarus).
   :align: center

* Start Mode: Aktuell wird nur *Executable* unterstützt.
* Executable: Der Name der ausführbaren Datei, die ausgeführt werden soll. 
  Dies ist entweder der Name der cross-kompilierten ausführbaren Datei, die 
  hochgeladen wurde, oder der Name der ausführbaren Datei die während des 
  Kompilieren erstellt wird.
* Compile From Source: Wird diese Checkbox aktiviert, so wird der Code nach dem
  Hochladen kompiliert. Es muss eine **Makefile.fpc** enthalten sein, damit 
  diese Option genutzt werden kann. Eine Beispiel-Makefile für ein kleines
  Projekt, das die Tinkerforge Bindings und die Datei **Example.pas** als 
  Hauptmodul nutzt, sieht wie folgt aus::

    [target]
    programs=Example

    [require]
    packages=tinkerforge
* Make options: Wenn von Source kompiliert wird können hier Makefile Parameter
  übergeben werden.  
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.

Java
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_java.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Java).
   :align: center

Die Tinkerforge.jar Bindings sind unter 
``/usr/tinkerforge/bindings/java/`` installiert. Die Datei ist zum Classpath
hinzugefügt, so dass die Tinkerforge Klassen nur importiert werden müssen.
Z.B. mittels ``import com.tinkerforge.IPConnection;``.

* Java Version: Aktuell ist nur eine Java Version installiert.
* Start Mode: **Main Class** und **JAR File** sind als Start Mode verfügbar.

  * Main Class: Wenn Main Class ausgewählt wird, parst der Brick Viewer alle 
    Class Dateien, die in Schritt 2 hinzugefügt wurden und gibt eine Liste aller
    Klassen die eine "main"-Methode enthalten und genutzt werden können um das 
    Programm zu starten.
  * JAR File: Wenn eine JAR Datei von dem Programm erstellt wurde, kann auch von
    dieser aus das Programm direkt gestartet werden. Die verfügbaren JAR Dateien
    werden in einer Drop-Down Box gelistet.
* Class Path: Hier können Dateien zum Class Path hinzugefügt werden. Alle JARs,
  die in Schritt 2 hinzugefügt wurden, werden automatisch zum Class Path
  hinzugefügt.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* JVM Options: Hier können Optionen angegeben werden, die der Java Virtual Machine
  übergeben werden.

JavaScript (Browser/Node.js)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_javascript.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (JavaScript).
   :align: center

* Client-Side (Browser): Wenn Client seitiges JavaScript genutzt wird, muss
  nichts konfiguriert werden. Es mussten nur die **.html** Dateien in Schritt 2
  zuvor hinzugefügt werden, die dann über das 
  :ref:`RED Brick Web Interface <red_brick_web_interface>` verfügbar sind.
  **Tinkerforge.js** kann genutzt werden mittels::

      <script src="/Tinkerforge.js" type='text/javascript'></script>
* Server-Side (Node.js): Wenn Node.js genutzt wird können der Start Mode und 
  weitere Optionen gesetzt werden. Die Tinkerforge Bindings sind verfügbar und
  können mittels ``require('tinkerforge')`` importiert werden.

  * Start Mode: **Script File** und **Command** sind verfügbar
    als Start Mode.

    * Start Mode *Script File*: Gebe die Skriptdatei an, die ausgeführt werden 
      soll.
    * Start Mode *Command*: Gebe das Kommando an, welches von Node mittels der 
      **-e** Option ausgeführt werden soll.
  * Working Directory: Spezifiziert das 
    `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
    des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
    Typischerweise kann dies bei ``.`` belassen werden.

  * Node.js Options: Hier können Optionen hinzugefügt werden, die an Node 
    übergeben werden, wenn die Skriptdatei oder das Kommando ausgeführt werden.

Octave
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_octave.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Octave).
   :align: center

Der Java Pfad zur Tinkerforge.jar ist bereits zur octaverc hinzugefügt worden.
Das eigene Programm kann daher annehmen, dass ``javaaddpath("Tinkerforge.jar")`` 
bereits mit dem korrekten Verzeichnis aufgerufen wurde.

* Octave Version: Aktuell ist nur eine Octave Version auf dem RED Brick 
  installiert.
* Start Mode: Aktuell wird nur **Script File** unterstützt.
* Script File: Es muss eine in Schritt 2 zuvor ausgewählte Datei gewählt werden,
  die ausgeführt werden soll.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Octave Options: Hier können Optionen dem Octave Interpreter übergeben werden.
  Die Option **--silent** ist voreingestellt, welches die Ausgabe von Versions-
  und Copyright-Informationen unterdrückt. Wird diese entfernt so lassen sich 
  diese Informationen in jeder Logdatei finden.

Perl
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_perl.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Perl).
   :align: center

Die Tinkerforge Bindings sind für Perl ebenfalls verfügbar. Nutze die ``use``
Direktive um sie zu importieren, z.B: ``use Tinkerforge::IPConnection;``.

* Perl Version: Aktuell ist nur eine Version des Perl Interpreters installiert.
* Start Mode **Script File** und **Command** stehen zur Verfügung.

  * Start Mode *Script File*: Hier wird die Skriptdatei angegeben, die vom Perl
    Interpreter ausgeführt werden soll.
  * Start Mode *Command*: Spezifiziert ein Kommando, dass vom Perl Interpreter mit
    der **-e** Option ausgeführt werden soll.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Perl Options: Hier werden Optionen definiert, die an Perl während der 
  Ausführung des Programms übergeben werden.


PHP
^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_php.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (PHP).
   :align: center

Die Tinkerforge Bindings wurden mittels `PEAR <http://pear.php.net/>`__
installiert und sind verfügbar.
Mittels ``require_once`` können diese importiert werden, z.B.:
``require_once('Tinkerforge/IPConnection.php');``.

* PHP Version: Aktuell ist nur eine PHP Interpreter Version auf dem RED Brick
  installiert.
* Start Mode **Script File**, **Command** und **Web Interface** stehen zur 
  Verfügung

  * Start Mode *Script File*: Spezifiziert die Skriptdatei, die vom PHP 
    Interpreter ausgeführt werden soll.
  * Start Mode *Command*: Spezifiziert das Kommando, dass vom PHP Interpreter 
    mittels der **-r** Option während der Ausführung ausgeführt werden soll.
  * Start Mode *Web Interface*: Wenn ein Web Interface mit PHP realisiert 
    werden soll, muss diese Option gewählt werden. In diesem Fall wird PHP von
    Apache aufgerufen, so dass keine weiteren Optionen anzugeben sind. Siehe
    :ref:`RED Brick Web Interface <red_brick_web_interface>` für weitere 
    Informationen zum Web Interface.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* PHP Options: Hier können Optionen hinzugefügt werden, die dem PHP Interpreter
  übergeben werden, wenn eine Skriptdatei oder ein Kommando ausgeführt wird.

Python
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_python.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Python).
   :align: center

Die Tinkerforge Bindings wurden mittels 
`pip <https://pypi.python.org/pypi/pip>`__ installiert und stehen zur 
Verfügung. Die Bindings können mit der normalen ``import`` Direktive eingebunden
werden, z.B.: ``from tinkerforge.ip_connection import IPConnection``.

* Python Version: Es kann zwischen Python 2 und Python 3 gewählt werden.
* Start Mode **Script File**, **Command**, **Module Name** und **Web Interface** 
  stehen zur Verfügung

  * Start Mode *Script File*: Spezifiziert die Skriptdatei, die vom Python 
    Interpreter ausgefürt werden soll.
  * Start Mode *Module Name*: Spezifiziert einen Modulnamen, der vom Python
    Interpreter mittels der **-m** Option ausgeführt werden soll
  * Start Mode *Command*: Spezifiziert ein Kommando, welches mittels der **-c** 
    Option des Interpreters ausgeführt werden soll.
  * Start Mode *Web Interface*: Wenn ein Web Interface mit Python realisiert 
    werden soll muss diese Option gewählt werden. In diesem Fall wird Python von
    Apache/WSGI aufgerufen, so dass keine weiteren Optionen anzugeben sind. 
    Siehe :ref:`RED Brick Web Interface <red_brick_web_interface>` für 
    weitere Informationen zum Web Interface.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Python Options: Hier können Optionen angegeben werden, die dem Python 
  Interpreter übergeben werden, wenn die Skriptdatei oder ein Kommando 
  ausgeführt werden.

Ruby
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_ruby.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Ruby).
   :align: center

Die Tinkerforge Bindings sind mittels `gem <https://rubygems.org/>`__
installiert und daher direkt 
verfügbar. Die ``require`` Anweisung kann genutzt werden um diese zu 
importieren, z.B. ``require 'tinkerforge/ip_connection'``.

* Ruby Version: Aktuell ist nur eine Ruby Interpreter Version auf dem RED Brick
  installiert.
* Start Mode **Script File** und **Command** stehen zur Verfügung

  * Start Mode *Script File*: Spezifiziert eine Skriptdatei die vom Ruby 
    Interpreter ausgeführt werden soll.
  * Start Mode *Command*: Spezifiziert ein Kommando, das vom Ruby Interpreter 
    mit der **-e** Option ausgeführt werden soll.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Ruby Options: Hier können Optionen dem Ruby Interpreter übergeben werden, wenn
  eine Skriptdatei oder ein Kommando ausgeführt werden.

Shell
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_shell.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Shell).
   :align: center

Die Shell Bindings liegen unter ``/usr/local/bin``, was im Pfad liegt. Somit
kann in einem Shellskript direkt ``tinkerforge`` ohne jeden Prefix aufgerufen 
werden.

* Shell Version: Es ist nur eine Bash Version auf dem RED Brick verfügbar.
* Start Mode **Script File** und **Command** stehen zur Verfügung.

  * Start Mode *Script File*: Spezifiziert eine Skriptdatei, die von der Bash
    ausgeführt werden soll.
  * Start Mode *Command*: Spezifiziert ein Kommando, welches von Bash mittels 
    der **-c** Version ausgeführt werden soll.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Shell Options: Hier können Optionen an Bash während der Ausführung der 
  Skriptdatei oder des Kommandos übergeben werden.

Visual Basic .NET
^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_vbnet.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 3 (Visual Basic .NET).
   :align: center

Die Tinkerforge.dll ist unter ``/usr/lib/`` für Visual Basic .NET verfügbar und
kann direkt von Mono gefunden werden. Jedes Visual Basic .NET Programm, dass die 
Tinkerforge.dll als Referenz nutzt, kann also ohne Angabe der Tinkerforge.dll im 
zuvorigen Schritt (Schritt 2) kompiliert werden.

* Mono Version: Aktuell ist nur eine Mono Version installiert.
* Start Mode: Es wird momentan nur *Executable* unterstützt.
* Executable: Wähle die ausführbare .NET Datei von den in Schritt 2 zuvor 
  gewählten dateien. Die Endung ist typischerweise .exe.

  Die ausführbare Datei wird mit `Mono <http://www.mono-project.com/>`__ 
  ausgeführt. Die Datei kann unter Windows zuvor mit Visual Studio kompiliert
  worden sein und anschließend auf dem RED Brick mit Mono ausgeführt werden. 
  Dabei muss allerdings darauf geachtet werden, dass keine Windows spezifischen 
  Bibliotheken genutzt werden, die auf dem RED Brick nicht verfügbar sind.
* Working Directory: Spezifiziert das 
  `Arbeitsverzeichnis <http://en.wikipedia.org/wiki/Working_directory>`__ 
  des Programms. Dieser Pfad ist relativ zum Root Verzeichnis des Programms.
  Typischerweise kann dies bei ``.`` belassen werden.
* Mono Options: Hier können Optionen angegeben werden, die dem Mono JIT Compiler
  übergeben werden.
  

Wizard Schritt 4: Argumente und Umgebungsvariablen
--------------------------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step4.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 4.
   :align: center

* Arguments: Das Programm wird mit den angegebenen Argumenten aufgerufen

Dabei ist zu beachten, dass Argumente nicht escaped werden müssen. Wenn zum 
Beispiel ein Programm mittels::

 ./my_program --setting value1 value2

aufgerufen werden soll, so müssen drei Argumente 
**--settings**, **value1** und **value2** einzeln in der Liste angegeben werden.

Wenn nur ein Argument mit dem Inhalt **--settings value1 value2** übergeben wird
ist dies gleichbedeutend mit folgendem Programmaufruf::

 ./my_program --settings\ value1\ value2

* Environment: Die Umgebungsvariablen, die hier gesetzt werden, sind für das 
  Programm verfügbar. Umgebungsvariablen, die zum Programmstart notwendig sind, 
  sind bereits voreingestellt. Falls du dir unsicher bist was diese bedeuten, 
  ist es sehr wahrscheinlich das du hier nichts anpassen musst.
  
Wizard Schritt 5: Stdio Umleitung
---------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step5.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 5.
   :align: center

In vielen Fällen können die Einstellungen hier so bleiben wie sie sind. Wenn
dir die Begriffe Standard Input und Standard Output das erste mal begegnen, 
kannst du vermutlich einfach **Next** klicken.

* Standard Input:
 
  * /dev/null: Das Programm nutzt keine Eingaben.
  * Pipe: Wenn Pipe ausgewählt wird, können Eingaben an das Programm mit dem
    Brick Viewer (:w
			Stdio Redirect des Program Tabs) gesendet 
    werden. Viele unserer Beispiele warten auf Eingaben vom Nutzer und reagieren
    nur auf Callbacks. Wenn du Programme dieser Art nutzt wähle *Pipe* als
    Standard Input.
  * File: Hiermit wird eine Datei ausgewählt, deren Inhalt als Eingabe übergeben
    wird.
  
* Standard Output:

  * /dev/null: Jede Ausgabe des Programms wird verworfen.
  * File: Gib eine Datei an in der die Ausgabe des Programms geschrieben wird.
  * Individual Log Files: Erzeugt eine neue Log Datei für jede Ausführung des
    Programms.
  * Continuous Log File: Erzeugt eine Log Datei in der alle Ausgaben des 
    Programms geschrieben wird.

* Standard Error: Für die Ausgabe von Fehlern werden die gleichen Möglichkeiten
  geboten, wie für den Standard Output. Zusätzlich gibt es die Möglichkeit 
  Fehler ebenfalls in das Log des Standard Outputs zu schreiben (redirect).


Wizard Schritt 6: Schedule
--------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step6.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 6.
   :align: center

* Mode *Never*: Der Scheduler des RED Bricks wird nicht benutzt. Das Programm
  kann nur manuell in dem Program Tab des Brick Viewers gestartet werden.
* Mode *Always*: Der Scheduler versucht immer das Programm am laufen zu halten.
  Wenn das Programm beendet wird, so wird es direkt wieder gestartet. Dies ist
  insbesondere für Kontroll-Programme sinnvoll, die permanent laufen sollen.
* Mode *Interval*: Hier kann ein Intervall (in Sekunden) definiert werden in dem
  das Programm ausgeführt werden soll.
* Mode *Cron*: Nutze `cron <http://de.wikipedia.org/wiki/Cron>`__ um die 
  Programmausführung zu planen. Cron ist ein *zeitbasierter* Aufgaben Scheduler.
  
  Damit kann man zum Beispiel die Ausführung eines Programms planen, das
  
  * jeden Tag um 20:00: ``00 20 * * *``
  * jeden Wochentag zur Arbeitszeit (6:00-18:00) einmal pro Stunde: ``00 09-18 * * 1-5``
  * oder jede Minute in der 12. Stunde des Montags, sofern dieser der 16. Tag 
    des Monats ist: ``* 12 16 * Mon``

  ausgeführt wird.

  Wie man sieht können auch sehr komplizierte Aufgaben mit Cron erledigt werden.
  Es gibt eine große Menge an 
  `Cron Tutorials <http://www.linuxhelp.net/guides/cron/>`__ 
  im Internet.

  Zur Nutzung von Cron ist die aktuelle Uhrzeit notwendig. Der RED Brick verfügt 
  aber über keine Uhr, die weiterläuft wenn der Brick heruntergefahren 
  wurde. Verfügt der RED Brick eine Verbindung zum Internet, so werden Datum und
  Uhrzeit neu gesetzt (mittels NTP). Sie können auch manuell in dem Date/Time
  Abschnitt des Settings Tab gesetzt werden. Alternativ kann auch das GPS 
  Bricklet genutzt werden um 
  `die Uhrzeit mittels GPS zu synchronisieren <https://github.com/Tinkerforge/red-brick/tree/master/programs/gps_time>`__.

* Mode *Once After Startup*: Der Scheduler führt das Programm nur einmal nach 
  dem Hochladen aus.
* Continue After Error: Der Scheduler startet das Programm nicht neu, wenn es 
  mit einem Fehler beendet wurde, wenn diese Checkbox deaktiviert wird.

Wizard Schritt 7: Zusammenfassung
---------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step7.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 7.
   :align: center

Die Seite zeigt eine Zusammenfassung der zuvor gewählten Konfiguration. Falls
Probleme auftreten und es Fragen gibt hilft die Angabe dieser Zusammenfassung.

Wizard Schritt 8: Upload
------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step8.jpg
   :scale: 60 %
   :alt: Screenshot des RED Brick Wizard Schritt 8.
   :align: center

Im letzen Schritt kann der **Start Upload** Button geklickt werden um die
ausgewählten Dateien hochzuladen und die Konfiguration zu übernehmen. Das 
Programm wird direkt nach dem Hochladen oder verzögert, je nach dem gewählten
Scheduling in Schritt 6, ausgeführt.

