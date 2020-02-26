
.. _api_bindings_delphi:

Delphi/Lazarus - API Bindings
=============================

Die Delphi/Lazarus Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Delphi/Lazarus Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``source/`` den Quelltext der Bindings
* in ``examples/`` die Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* Delphi 2007 oder neuer, oder Lazarus (Free Pascal Compiler 2.4 oder neuer),
  andere Delphi oder Object Pascal Compiler sollten auch funktionieren


.. _api_bindings_delphi_install:

Installation
------------

Um die Delphi/Lazarus Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und macOS, usw.) lauffähig sein.

Da es keine vorkompilierte Bibliothek für die Delphi/Lazarus Bindings gibt, gibt es in
diese Sinne auch nichts zu installieren. Die empfohlene Art und Weise die
Bindings zu verwenden, ist ihren Quelltext direkt in das jeweilige Delphi/Lazarus Projekt
mit einzubinden. Der folgenden Abschnitt zeigt an verschiedenen Beispielen auf
wie das gemacht werden kann.


Test eines Beispiels
--------------------

Um ein Delphi/Lazarus Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit dem Free
Pascal Compiler (FPC), sowie der Lazarus IDE und der Delphi IDE kompilieren.
Dafür müssen die IP Connection und die Stepper Brick Bindings vom ``source/``
Ordner sowie ``ExampleConfiguration.pas`` aus dem ``examples/Brick/Stepper/``
Ordner in ein neuen Ordner kopiert werden::

 example_project/
  -> Base58.pas
  -> BlockingQueue.pas
  -> BrickDaemon.pas
  -> Device.pas
  -> DeviceBase.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> SHAone.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: delphi

  const
    HOST = 'localhost';
    PORT = 4223;
    UID = 'XXYYZZ'; { Change XXYYZZ to the UID of your Stepper Brick }


Free Pascal Compiler (FPC)
^^^^^^^^^^^^^^^^^^^^^^^^^^

FPC findet die verwendeten Units automatisch, dadurch sieht der Befehl für die
Kompilierung des Beispiels mit FPC wie folgt aus::

 fpc ExampleConfiguration.pas

Runtime Error 211
"""""""""""""""""

Wenn Runtime Error 211 beim Starten des Programms auftritt, oder das Programm
folgendes ausgibt::

 Threading has been used before cthreads was inizialized.

Dann muss ``CThreads`` am Anfang der ``Uses`` Liste des Programms eingefügt
werden.


Lazarus IDE
^^^^^^^^^^^

Mit Lazarus kann der ``example_project/`` Ordner so verwendet werden:

* Project
* New Project from file ...
* Wähle ``example_project/ExampleConfiguration.pas``
* Klicke Open
* Wähle "Console Application"
* Klicke OK
* Wähle einen "Application Class Name" und "Title"
* Klicke OK

Jetzt kann das Projekt kompiliert und gestartet werden!

Runtime Error 211
"""""""""""""""""

Wenn Runtime Error 211 beim Starten des Programms auftritt, oder das Programm
folgendes ausgibt::

 Threading has been used before cthreads was initialized.

Dann muss ``-dUseCThreads`` zu den Lazarus Compilereinstellungen hinzugefügt
werden:

* Projekt
* Projekteinstellungen ...
* Compilereinstellungen
* Andere

Jetzt das Projekt neu kompilieren. Falls dies das Problem nicht behebt, dann
muss ``CThreads`` am Anfang der ``Uses`` Liste des Programms eingefügt werden.


Delphi IDE
^^^^^^^^^^

Mit Delphi XE2 (ältere Delphi-Versionen sollten ähnlich funktionieren) kann der
``example_project/`` Ordner wie folgt verwendet werden. Zuerst muss
``ExampleConfiguration.pas`` in ``ExampleConfiguration.dpr`` umbenannt werden
dann bleiben noch diese Schritte:

* Project
* Add Existing Project...
* Choose ``example_project/ExampleConfiguration.dpr``
* Klicke Open

Jetzt kann das Projekt kompiliert und gestartet werden!


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Delphi_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Delphi>
   Bricks <Bricks_Delphi>
   Bricks (Abgekündigt) <Bricks_Delphi_Discontinued>
   Bricklets <Bricklets_Delphi>
   Bricklets (Abgekündigt) <Bricklets_Delphi_Discontinued>
