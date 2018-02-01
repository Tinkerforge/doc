
.. _api_bindings_vbnet:

Visual Basic .NET - API Bindings
================================

Die Visual Basic .NET Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Visual Basic .NET
Programmen heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>`
für die Bindings beinhaltet:

* ``Tinkerforge.dll``, eine vorkompilierte .NET Bibliothek
* ``Tinkerforge.xml``, die API Dokumentation für Visual Studio,  MonoDevelop, usw.
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Visual Basic .NET Bindings basieren auf den :ref:`C# Bindings
<api_bindings_csharp>`. Seit Version 2.0.0 sind die C# Bindings `CLS
<https://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `.NET kompatiblen Sprachen
<https://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. Visual Basic .NET.


Voraussetzungen
---------------

* Visual Basic 2005 (VB 8.0) oder neuer, oder Mono 1.2.3 oder neuer


.. _api_bindings_vbnet_install:

Installation
------------

Ob und wie die Visual Basic .NET Bindings installiert werden müssen hängt stark
davon ab wie sie benutzt werden sollen. Wenn der Visual Basic .NET Compiler
direkt von der Kommandozeile aufgerufen wird genügt es die ``Tinkerforge.dll``
Datei im gleichen Verzeichnis wie den Visual Basic .NET Quelltext des Programms
abzulegen.

Um die Bindings in einer IDE zu verwenden muss die ``Tinkerforge.dll`` Datei
wahrscheinlich zuerst dem Assembly-Katalog der IDE hinzugefügt werden. Wie dies
gemacht wird hängt von der IDE ab und wird in der Dokumentation der jeweiligen
IDE erklärt.


Test eines Beispiels
--------------------

Um ein Visual Basic .NET Beispiel testen zu können müssen zuerst :ref:`Brick
Daemon <brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick
Daemon arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

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
anzeigen. Ersetze deren Inhalt durch dem Inhalt der ``ExampleConfiguration.vb``
Datei im ``examples/Brick/Stepper/`` Ordner.

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: vbnet

  Const HOST As String = "localhost"
  Const PORT As Integer = 4223
  Const UID As String = "XYZ" ' Change to your UID

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

 vbnc /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.vb


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
anzeigen. Ersetze deren Inhalt durch dem Inhalt der ``ExampleConfiguration.vb``
Datei im ``examples/Brick/Stepper/`` Ordner.

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: vbnet

  Const HOST As String = "localhost"
  Const PORT As Integer = 4223
  Const UID As String = "XYZ" ' Change to your UID

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


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_VBNET_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_VBNET>
   Bricks <Bricks_VBNET>
   Bricks (Abgekündigt) <Bricks_VBNET_Discontinued>
   Bricklets <Bricklets_VBNET>
   Bricklets (Abgekündigt) <Bricklets_VBNET_Discontinued>
