
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C/C++ - API Bindings

.. _api_bindings_c:

C/C++ - API Bindings
====================

Die C/C++ Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen aus
den Bindings für alle Tinkerforge Bricks und
Bricklets (in ``bindings/``) und allen verfügbaren C/C++ Beispielen (in
``examples/``).

Um die C/C++ Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und Mac OS X, usw.) lauffähig sein.


Test eines Beispiels
--------------------

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit GCC unter
Linux kompilieren. Dafür müssen die IP Connection und die Stepper Brick
Bindings (``ip_connection.h``, ``ip_connection.c``, ``brick_stepper.c`` und
``brick_stepper.h``) vom ``bindings/`` Ordner sowie
``example_configuration.c`` vom ``examples/brick/stepper/`` Ordner in ein
Projektordner kopiert werden::

 project_folder/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c


GCC
^^^

Die einzige Abhängigkeit auf Unix-artigen Systemen ist pthreads. Somit sieht der
Befehl um das Beispiel mit GCC unter Linux zu kompilieren wie folgt aus::

 gcc -pthread -o example_configuration brick_stepper.c ip_connection.c example_configuration.c

Unter Windows wird Win32 für Threads und WinSock2 (``ws2_32``) für die
Netzwerkverbindung verwendet. Mit MinGW lässt sich das Beispiel wie folgt
kompilieren (Linkerparameter müssen nach den Quelldateien angegeben werden)::

 gcc -o example_configuration.exe brick_stepper.c ip_connection.c example_configuration.c -lws2_32


Visual Studio
^^^^^^^^^^^^^

Mit Visual Studio kann der ``project_folder/`` wie folgt verwendet werden:

* File
* New
* Project From Existing Code
* Wähle als Type "Visual C++"
* Wähle ``project_folder/``
* Wähle einen Projektnamen
* Klicke Next
* Wähle "Console Application"
* Klicke Finish

Als nächstes muss das Projekt auf den C++ Compiler umgestellt werden. Unser C
Quelltext verwendet den C99 Standard, Visual Studio unterstützt aber nur C89.
Diese Problem kann durch die Verwendung des C++ Compilers umgangen werden:

* Project
* Properties
* C/C++
* Advanced, Option "Compile as"
* Wähle "Compile as C++ Code (/TP)"

Zusätzlich muss noch ``ws2_32.lib`` (WinSock2) dem Projekt hinzugefügt werden:

* Project
* Properties
* Linker
* Input, Option "Additional Dependencies"
* Füge ``ws2_32.lib;`` hinzu

Ältere Versionen von Visual Studio bringen kein ``stdint.h`` mit. Eine kompatible
Version gibt es `hier <http://msinttypes.googlecode.com/svn/trunk/stdint.h>`__.
Falls nötig diese herunterladen und im ``project_folder/`` speichern.

Das waren alle nötigen Änderungen, jetzt kann es los gehen!

Der Visual Studio Compiler kann auch von der Kommandozeile aus verwendet werden::

 cl.exe /TP /I. brick_stepper.c ip_connection.c example_configuration.c /link /out:example_configuration.exe ws2_32.lib
