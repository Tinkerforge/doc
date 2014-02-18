
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Mathematica - API Bindings

.. _api_bindings_mathematica:

Mathematica - API Bindings
==========================

**Voraussetzungen**: Mathematica 5.0 oder neuer auf Windows, Linux und Mac OS X mit .NET/Link Unterstützung

Die Mathematica Bindings (:ref:`Download <downloads_bindings_examples>`)
und die :ref:`C# Bindings <api_bindings_csharp>`
sind gleich. Seit Version 2.0.0 sind die C# Bindings `CLS
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `CLI/.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. Mathematicas `.NET/Link Unterstützung
<http://reference.wolfram.com/mathematica/NETLink/tutorial/CallingNETFromMathematica.html>`__.

Die .NET/Link Unterstützung in Mathematica benötigt das `.NET Framework
<http://www.microsoft.com/net>`__ auf Windows und das `Mono Framework
<http://www.mono-project.com/>`__ unter Linux und Mac OS X.

Die Bindings bestehen aus einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem C# Quelltext der DLL (in ``source/``)
und allen verfügbaren Mathematica Beispielen (in ``examples/``).


Test eines Beispiels
--------------------

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu das ``examples/Brick/Stepper/ExampleConfiguration.nb`` Notebook in
Mathematica öffnen, die UID des Stepper Bricks eintragen und alle Cells von
oben nach unten auswerten.

Falls das Notebook von einem anderen Ordner aus geöffnet wurde muss unter
Umständen die ``LoadNETAssembly[]`` Zeile angepasst werden, damit Mathematica
die ``Tinkerforge.dll`` finden kann:

 .. code-block:: mathematica

    LoadNETAssembly["Tinkerforge",NotebookDirectory[]<>"../.."]

Ersetze das ``NotebookDirectory[]<>"../.."`` Parameter mit einem absoluten
Pfad zum Ordner der die ``Tinkerforge.dll`` enthält.

Hier ein weiters :ref:`Beispiel <temperature_bricklet_mathematica_examples>`,
das einen dynamischen Plot der Temperaturwerte eines Temperature Bricklets
zeigt. Der Einbruch bei Sample 82 wurde mittels eines Kältesprays erzeugt.

.. image:: /Images/Screenshots/mathematica_example.jpg
   :scale: 100 %
   :alt: Temprature Bricklet mit dynamischem Plot der Messwerte
   :align: center

API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_Mathematica_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
