
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / LabVIEW - API Bindings

.. _api_bindings_labview:

LabVIEW - API Bindings
======================

**Voraussetzungen**: LabVIEW auf Windows mit .NET Unterstützung

Die LabVIEW Bindings (:ref:`Download <downloads_bindings_examples>`)
und die :ref:`C# Bindings <api_bindings_csharp>`
sind gleich. Seit Version 2.0.0 sind die C# Bindings `CLS
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `CLI/.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. LabVIEWs `.NET Unterstützung
<http://zone.ni.com/reference/en-XX/help/371361K-01/lvcomm/dotnet_pal/>`__.

Die Bindings bestehen aus einer Bibliothek (.dll) für alle Tinkerforge Bricks
und Bricklets (``Tinkerforge.dll``), dem C# Quelltext der DLL (in ``source/``)
und allen verfügbaren LabVIEW Beispielen (in ``examples/``).


Test eines Beispiels
--------------------

Damit die Bindings funktionieren können muss LabVIEW in der Lage sein die
``Tinkerforge.dll`` zu finden. Beim Öffnen einen Beispiels wird LabVIEW nach
der DLL suchen und nachfragen falls sie nicht gefunden werden kann. Dieses
Suchen-und-Nachfragen kann vermieden werden, indem die ``Tinkerforge.dll`` in
einem LabVIEW bekannten Ordern gespeichert wird. Die einfachsten Möglichkeiten
sind der ``vi.lib`` Ordern der LabVIEW oder der gleiche Ordner in dem auch das
zu öffnende Beispiel gespeichert ist. In beiden Fällen wird LabVIEW die
``Tinkerforge.dll`` automatisch finden und nicht Nachfragen.

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu ``examples/Brick/Stepper/ExampleConfiguration.nb`` in
LabVIEW öffnen, die UID des Stepper Bricks eintragen und ausführen.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_LabVIEW_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
