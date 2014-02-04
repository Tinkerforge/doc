
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C# - API Bindings

.. _api_bindings_csharp:

C# - API Bindings
=================

.. note::
 Es gibt einen extra Abschnitt für :ref:`C# und Windows Phone <api_bindings_csharp_windows_phone>`.

Die C# Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen aus
einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem Quelltext der DLL (in ``source/``) und
allen verfügbaren C# Beispielen (in ``examples/``).

Die Bibliothek hat keine weiteren Abhängigkeiten.


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

.. _api_bindings_csharp_cls_complience:

CLS Konformität
---------------

Seit Version 2.0.0 sind die C# Bindings konform zur `Common Language Specification
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__.
Dies erlaubt es diese Bindings mit allen `CLI/.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden.
Für :ref:`Visual Basic .NET <api_bindings_vbnet>` stehen gesondert
Beispielcode und Dokumentation zur Verfügung um dies zu demonstrieren.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_CSharp_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
