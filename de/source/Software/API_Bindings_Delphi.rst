
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-delphi">Software</a> / Delphi/Lazarus - API Bindings

.. _api_bindings_delphi:

Delphi/Lazarus - API Bindings
=============================

**Voraussetzungen**: Delphi 2007 oder neuer, oder Lazarus (Free Pascal Compiler
2.4 oder neuer), andere Delphi oder Object Pascal Compiler sollten auch
funktionieren

Die Delphi Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus den Bindings für alle Tinkerforge Bricks und
Bricklets (in ``bindings/``) und allen verfügbaren Delphi Beispielen (in
``examples/``).

Um die Delphi Bindings einfach zu halten haben sie nur externe Abhängigkeiten,
die möglichst überall verfügbar sind, wodurch sie leicht in jegliches Projekt
eingebunden werden können. Wir bieten keine vorkompilierte Bibliothek an, da
dies zu viel Aufwand wäre alle möglichen Kombinationen von Architekturen und
Betriebssystem zu versorgen. Die Bindings sollten aber auf den meisten
Architekturen (ARM, x86, etc.) und den meisten Betriebssystemen (Windows und
POSIX Systeme, wie Linux und Mac OS X, usw.) lauffähig sein.


Test eines Beispiels
--------------------

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit Lazarus
und Delphi XE2 kompilieren.


Lazarus
^^^^^^^

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit dem Free
Pascal Compiler (FPC) kompilieren. FPC ist Teil der Lazarus IDE. Dafür
müssen die IP Connection (``Base58.pas``, ``BlockingQueue.pas``,
``BrickDaemon.pas``, ``Device.pas``, ``DeviceBase.pas``, ``IPConnection.pas``,
``LEConverter.pas``, ``SHA1.pas`` und ``TimedSemaphore.pas``) und die
Stepper Brick Bindings (``BrickStepper.pas``) vom ``bindings/`` Ordner sowie
``ExampleConfiguration.pas`` vom ``examples/Brick/Stepper/`` Ordner in ein
Projektordner kopiert werden::

 project_folder/
  -> Base58.pas
  -> BlockingQueue.pas
  -> BrickDaemon.pas
  -> Device.pas
  -> DeviceBase.pas
  -> IPConnection.pas
  -> LEConverter.pas
  -> SHA1.pas
  -> TimedSemaphore.pas
  -> BrickStepper.pas
  -> ExampleConfiguration.pas

FPC findet die verwendeten Units, dadurch sieht der Befehl für die Kompilierung
des Beispiels mit FPC wie folgt aus::

 fpc ExampleConfiguration.pas

Mit Lazarus kann der ``project_folder/`` so verwendet werden:

* Project
* New Project from file ...
* Wähle ``project_folder/ExampleConfiguration.pas``
* Klicke Open
* Wähle "Console Application"
* Klicke OK
* Wähle einen "Application Class Name" und "Title"
* Klicke OK


Delphi IDE
^^^^^^^^^^

Mit Delphi XE2 (ältere Delphi-Versionen sollten ähnlich funktionieren) kann der
``project_folder/`` wie folgt verwendet werden. Zuerst muss
``ExampleConfiguration.pas`` in ``ExampleConfiguration.dpr`` umbenannt werden
dann bleiben noch diese Schritte:

* Project
* Add Existing Project...
* Choose ``project_folder/ExampleConfiguration.dpr``
* Klicke Open


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Delphi_links.table
