
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Visual Basic .NET - API Bindings

.. _api_bindings_vbnet:

Visual Basic .NET - API Bindings
================================

**Voraussetzungen**: Visual Basic 2005 (VB 8.0) oder neuer, oder Mono 1.2.3 oder neuer

Die Visual Basic .NET Bindings (:ref:`Download <downloads_bindings_examples>`)
und die :ref:`C# Bindings <api_bindings_csharp>`
sind gleich. Seit Version 2.0.0 sind die C# Bindings `CLS
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `CLI/.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. Visual Basic .NET.

Die Bindings bestehen aus einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem C# Quelltext der DLL (in ``source/``)
und allen verfügbaren Visual Basic .NET Beispielen (in ``examples/``).


Test eines Beispiels
--------------------

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit MonoDevelop
und Visual Studio kompilieren.

MonoDevelop
^^^^^^^^^^^

Am Beispiel werden wir das Stepper Brick Konfigurationsbeispiel mit dem
Visual Basic .NET Compiler (VBNC) kompilieren, der Teil von Mono ist. Dazu muss
als erstes ein neues Visual Basic .NET Projekt in MonoDevelop erstellt werden,
klicke:

* Datei
* Neu
* Projektmappe...
* Wähle "VBNet"
* Wähle "Konsolenprojekt"
* Wähle einen Name (e.g. ExampleConfiguration)
* Klicke Vor
* Klicke OK

MonoDevelop sollte jetzt einen ``Application.vb`` Datei in seinem Editor
anzeigen. Ersetze deren Inhalt durch dem Inhalt von
``examples/Brick/Stepper/ExampleConfiguration.vb``.

Jetzt muss noch ``Tinkerforge.dll`` dem Projekt als Verweis hinzugefügt werden:

* Rechtsklick auf Verweise im Projektmappen Explorer
* Verweise bearbeiten...
* Klicke den .NET Assembly Tab an
* Wähle ``Tinkerforge.dll`` aus
* Klicke Hinzufügen

Das Projekt ist jetzt bereit für einen Test, klicke:

* Ausführen
* Ausführen

Der Visual Basic .NET Compiler kann auch von der Kommandozeile aus verwendet
werden::

 /usr/bin/vbnc /target:exe /out:ExampleConfiguration.exe /reference:Tinkerforge.dll ExampleConfiguration.vb


Visual Studio
^^^^^^^^^^^^^

Am Beispiel werden wir das Stepper Brick Konfigurationsbeispiel in Microsoft
Visual Basic 2010 kompilieren. Dazu muss als erstes ein neues Visual Basic
erstellt werden, klicke:

* Datei
* Neues Projekt...
* Wähle "Visual Basic"
* Wähle "Console Application"
* Wähle einen Name (e.g. ExampleConfiguration)
* Klicke OK

Visual Studio sollte jetzt einen ``Module1.vb`` Datei in seinem Editor
anzeigen. Ersetze deren Inhalt durch dem Inhalt von
``examples\Brick\Stepper\ExampleConfiguration.vb``.

Jetzt muss noch ``Tinkerforge.dll`` dem Projekt als Verweis hinzugefügt werden:

* Rechtsklick auf das Projekt im Projektmappen-Explorer
* Verweis hinzufügen...
* Klicke den Durchsuchen Tab an
* Wähle ``Tinkerforge.dll`` aus
* Klicke OK

Bevor das Projekt getestet werden kann muss Visual Studio wissen was das
richtige Startobjekt ist:

* Rechtsklick auf das Projekt im Projektmappen-Explorer
* Eigenschaften
* Klicke den Anwendung Tab an
* Wähle "Sub Main" als Startobjekt
* Klicke Save

Das Projekt ist jetzt bereit für einen Test, klicke:

* Debuggen
* Debugging starten


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_VBNET_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
