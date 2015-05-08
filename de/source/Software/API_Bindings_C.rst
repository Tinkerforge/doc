
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-c">Software</a> / C/C++ - API Bindings

.. _api_bindings_c:

C/C++ - API Bindings
====================

.. note::
 Es gibt einen extra Abschnitt für :ref:`Objective-C und iOS <api_bindings_c_ios>`.

Die C/C++ Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen C/C++ Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``source/`` den Quelltext der Bindings
* in ``examples/`` die Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* C Compiler (C99 kompatible) oder C++ Compiler


.. _api_bindings_c_install:

Installation
------------

Um die C/C++ Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und Mac OS X, usw.) lauffähig sein.

Da es keine vorkompilierte Bibliothek für die C/C++ Bindings gibt, gibt es in
diese Sinne auch nichts zu installieren. Die empfohlene Art und Weise die
Bindings zu verwenden, ist ihren Quelltext direkt in das jeweilige C/C++ Projekt
mit einzubinden. Der folgenden Abschnitt zeigt an verschiedenen Beispielen auf
wie dies gemacht werden kann.


Test eines Beispiels
--------------------

Um ein C/C++ Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit GCC auf der
Kommandozeile und in verschiedenen IDEs kompilieren.
Dafür müssen zuerst die IP Connection und die Stepper Brick Bindings aus dem
``source/`` Ordner sowie ``example_configuration.c`` aus dem
``examples/brick/stepper/`` Ordner in ein neuen Ordner kopiert werden::

 example_project/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: c

  #define HOST "localhost"
  #define PORT 4223
  #define UID "XYZ" // Change to your UID


GCC
^^^

Die einzige Abhängigkeit auf Unix-artigen Systemen ist pthreads. Somit sieht der
Befehl um das Beispiel mit GCC unter Linux und Mac OS X zu kompilieren wie
folgt aus::

 gcc -pthread -o example *.c

Unter Windows wird Win32 für Threads und WinSock2 (``ws2_32``) für die
Netzwerkverbindung verwendet. Mit MinGW lässt sich das Beispiel wie folgt
kompilieren (Linker-Parameter müssen nach den Quelldateien angegeben werden)::

 gcc -o example.exe *.c -lws2_32 -ladvapi32

Der einfachste Weg die Bindings in einem C++ Projekt zu verwenden, ist es alle
benötigten Dateien von ``*.c`` nach ``*.cpp`` umzubenennen. Dann behandelt der
Compiler den Quelltext als C++ und tut automatisch das Richtige.


Visual Studio
^^^^^^^^^^^^^

Mit Visual Studio kann der ``example_project/`` Ordner auch verwendet werden. Der
einfachste Weg die Bindings in einem Visual C++ Projekt zu verwenden, ist es
alle benötigten Dateien von ``*.c`` nach ``*.cpp`` umzubenennen. Dann
behandelt der Compiler den Quelltext als C++ und tut automatisch das Richtige.
Dadurch wird auch das Problem vermieden, dass der Visual Studio
Compiler nur den C89 Standard unterstützt, die Bindings aber den neueren C99
Standard verwenden.

IDE
"""

Jetzt kann ein neues Projekt in Visual Studio erzeugt werden:

* File
* New
* Project From Existing Code
* Wähle als Type "Visual C++"
* Wähle ``example_project/``
* Wähle einen Projektnamen
* Klicke Next
* Wähle "Console Application"
* Klicke Finish

Zusätzlich müssen noch ``ws2_32.lib`` (WinSock2) und ``advapi32.lib`` dem
Projekt hinzugefügt werden:

* Project
* Properties
* Linker
* Input, Option "Additional Dependencies"
* Füge ``ws2_32.lib;advapi32.lib;`` hinzu

Ältere Versionen von Visual Studio bringen kein ``stdint.h`` mit. Eine kompatible
Version gibt es `hier <http://msinttypes.googlecode.com/svn/trunk/stdint.h>`__.
Falls nötig diese herunterladen und im ``example_project/`` Ordner speichern.

Das waren alle nötigen Änderungen, jetzt kann das Projekt kompiliert und
gestartet werden!

Kommandozeile
"""""""""""""

Der Visual Studio Compiler kann auch von der Kommandozeile aus verwendet werden
im ``example_project/`` Ordner::

 cl.exe /I. *.cpp /link /out:example.exe ws2_32.lib advapi32.lib


Qt Creator
^^^^^^^^^^

Ein neues Projekt für der ``example_project/`` Ordner in Qt Creator kann wie folgt
erzeugt werden:

* File
* New File or Project...
* Wähle Other Project
* Wähle Empty Qt Project
* Klicke Choose...
* Wähle "example_project" als Name
* Wähle den Ordner der den ``example_project/`` Ordner beinhaltet für "Create in"
* Klicke Next
* Klicke Next
* Klicke Finish

Qt Creator sollte jetzt eine leere Datei namens ``example_project.pro`` anzeigen.
In diesem müssen jetzt folgende Zeilen kopiert und das Ergebnis gespeichert
werden::

  TEMPLATE = app
  CONFIG += console
  TARGET = example_configuration
  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread
  SOURCES += ip_connection.c brick_stepper.c example_configuration.c
  HEADERS += ip_connection.h brick_stepper.h

Dies weist Qt Creator an, dass dies eine Konsolenanwendung namens
"example_configuration" ist. Sie ist gegen die ``ws2_32`` und ``advapi32``
Bibliothekeb auf Windows gelinkt und verwendet pthreads auf Unix
(Linux, Mac OS X, etc).

Bevor das Programm jetzt gestartet werden kann muss noch der Haken bei
"Run in terminal" auf dem Tab für die Run Konfiguration des Projekts gesetzt
werden, ansonsten wird die Ausgabe des Programms nicht angezeigt.

Jetzt kann das Programm kompiliert und gestartet werden!

Dies ist ein Beispiel ein Projekt in C. Der einfachste Weg die Bindings in
einem C++ Projekt zu verwenden, ist es alle benötigten Dateien von ``*.c`` nach
``*.cpp`` umzubenennen und die ``SOURCES`` Zeile in ``example_project.pro``
entsprechend anzupassen. Dann behandelt der Compiler den Quelltext als C++ und
tut automatisch das Richtige.

Um die C/C++ Bindings zu einem bestehenden Qt Creator Projekt hinzuzufügen
müssen nur die benötigten Dateien zu den ``SOURCES`` und ``HEADERS`` Variablen
hinzugefügt und folgende zwei Zeilen in die ``.pro`` Datei des Projekts
eingefügt werden::

  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread


Orwell Dev-C++
^^^^^^^^^^^^^^

Ein neues Projekt für der ``example_project/`` Ordner in Dev-C++ kann wie folgt
erzeugt werden:

* Datei
* Neu
* Projekt...
* Wähle Console Application und C Projekt
* Klicke Ok

Dev-C++ erzeugt eine neue Datei namens ``main.c``. Diese benötigen wir nicht
und sie kann durch einen Klick auf "Datei entfernen" in deren Kontextmenü in
der Projektansicht entfernt werden. Als nächstes alle Dateien aus dem
``example_project/`` Ordner zum Projekt hinzufügen über den "Zum Projekt
hinzufügen" Eintrag im Kontextmenüs des Projekts.

Dann noch ``libws2_32.a`` (WinSock2) und ``libadvapi32.a`` zum Projekt
hinzufügen:

* Projekt
* Projekt Optionen
* Parameter
* Klicke Bibliothek/Objekt hinzufügen
* Wähle ``libws2_32.a`` und ``libadvapi32.a``
* Klicke Open
* Klicke Ok

Jetzt kann das Programm kompiliert und gestartet werden!

Dies ist ein Beispiel ein Projekt in C. Der einfachste Weg die Bindings in
einem C++ Projekt zu verwenden, ist es alle benötigten Dateien von ``*.c`` nach
``*.cpp`` umzubenennen. Dann behandelt der Compiler den Quelltext als C++ und
tut automatisch das Richtige.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_C_links.table
