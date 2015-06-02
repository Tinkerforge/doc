
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-csharp">Software</a> / C# - API Bindings

.. _api_bindings_csharp:

C# - API Bindings
=================

.. note::
 Es gibt einen extra Abschnitt für :ref:`C# und Windows Phone
 <api_bindings_csharp_windows_phone>`.

Die C# Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen C# Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.dll``, eine vorkompilierte C#/.NET Bibliothek (ohne Debug-Informationen)
* ``Tinkerforge.dll.mdb``, Debug-Informationen für ``Tinkerforge.dll``
* ``Tinkerforge.xml``, die API Dokumentation für Visual Studio,  MonoDevelop, usw.
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die C#/.NET Bibliothek hat keine weiteren Abhängigkeiten.


Voraussetzungen
---------------

* C# Compiler


.. _api_bindings_csharp_install:

Installation
------------

Ob und wie die C# Bindings installiert werden müssen hängt stark davon ab wie
sie benutzt werden sollen. Wenn der C# Compiler direkt von der Kommandozeile
aufgerufen wird genügt es die ``Tinkerforge.dll`` Datei im gleichen Verzeichnis
wie den C# Quelltext des Programms abzulegen.

Um die Bindings in einer IDE zu verwenden muss die ``Tinkerforge.dll`` Datei
wahrscheinlich zuerst dem Assembly-Katalog der IDE hinzugefügt werden. Wie dies
gemacht wird hängt von der IDE ab und wird in der Dokumentation der jeweiligen
IDE erklärt.

Die C# Bindings sind auch als `NuGet Package
<https://www.nuget.org/packages/Tinkerforge/>`__ verfügbar, das in Visual
Studio und MonoDevelop (via `NuGet Addin
<https://github.com/mrward/monodevelop-nuget-addin>`__) zum jeweiligen Projekt
hinzugefügt werden kann.

Das NuGet Package beinhaltet weder den Quelltext der Bindings noch die
Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.


Test eines Beispiels
--------------------

Um ein C# Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
auf der Kommandozeile kompiliert. Dafür müssen zuerst die ``Tinkerforge.dll``
Datei und die ``ExampleConfiguration.cs`` Datei aus dem
``examples/Brick/Stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: csharp

  private static string HOST = "localhost";
  private static int PORT = 4223;
  private static string UID = "XYZ"; // Change to your UID

Jetzt kann im ``example_project/`` Ordner der Visual Studio C# Compiler auf
Windows so aufgerufen werden::

 csc /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

oder so der Mono Compiler auf Linux und Mac OS X::

 gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Alternativ können die Beispiele auch in einer C# IDE deiner Wahl verwendet
werden, wie z.B. Visual Studio oder MonoDevelop.


.. _api_bindings_csharp_cls_complience:

CLS Konformität
---------------

Seit Version 2.0.0 sind die C# Bindings konform zur `Common Language Specification
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__.
Dies erlaubt es diese Bindings mit allen `.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden.
Für :ref:`Visual Basic .NET <api_bindings_vbnet>`,
:ref:`Mathematica <api_bindings_mathematica>` und
:ref:`LabVIEW (Windows) <api_bindings_labview>` stehen eigene
Beispiele und Dokumentation zur Verfügung, um dies zu demonstrieren.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_CSharp_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_CSharp>
   Bricks <Bricks_CSharp>
   Bricklets <Bricklets_CSharp>
