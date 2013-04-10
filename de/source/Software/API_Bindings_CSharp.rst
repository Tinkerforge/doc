
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C# - API Bindings

.. _api_bindings_csharp:

C# - API Bindings
=================

Die C# Bindings bestehen aus einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem Quelltext der DLL (in ``source/``) und
allen verfügbaren C# Beispielen (in ``examples/``).

Die Bibliothek wurde mit dem folgenden Befehl erzeugt::

 gmcs /optimize /target:library /out:Tinkerforge.dll source/Tinkerforge/*.cs

Diese hat keine weiteren Abhängigkeiten.


Test eines Beispiels
--------------------

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
kompiliert.

Dafür müssen zuerst die ``Tinkerforge.dll`` und die
``examples/Brick/Stepper/ExampleConfiguration.cs`` Datei in einen Ordern kopiert
werden::

 example_folder/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In diesem Ordner kann jetzt ein C# Compiler mit den folgenden Parametern
aufgerufen werden (1. Windows und 2. Linux/Mac OS X (Mono))::

 1.) csc.exe       /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs
 2.) /usr/bin/gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Alternativ können die Beispiele auch in einer C# Entwicklungsumgebung deiner
Wahl verwendet werden (wie Visual Studio oder Mono Develop).


CLS Konformität
---------------

Seit Version 2.0.0 sind die C# Bindings konform zur `Common Language Specification
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__.
Dies erlaubt es diese Bindings mit allen `CLI/.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden.
Für :ref:`Visual Basic .NET <api_bindings_vbnet>` stehen gesondert
Beispielcode und Dokumentation zur Verfügung um dies zu demonstrieren.
