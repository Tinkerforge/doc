
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-labview">Software</a> / LabVIEW - API Bindings

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
und allen verfügbaren LabVIEW Beispielen (in ``examples/``). Die Beispiele sind
in LabVIEW 2013 Format gespeichert. Alle Beispiele liegen aber auch im LabVIEW
2010 Format bei.


.. _api_bindings_labview_install:

Installation
------------

TODO


Test eines Beispiels
--------------------

Um ein LabVIEW Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.





Damit die Bindings funktionieren können muss LabVIEW in der Lage sein die
``Tinkerforge.dll`` zu finden. Beim Öffnen einen Beispiels wird LabVIEW nach
der DLL suchen und nachfragen falls sie nicht gefunden werden kann. Dieses
Suchen-und-Nachfragen kann vermieden werden, indem die ``Tinkerforge.dll`` in
einem LabVIEW bekannten Ordern gespeichert wird. Die einfachsten Möglichkeiten
sind der ``vi.lib`` Ordern der LabVIEW Installation (z.B.
``C:\Program Files\National Instruments\LabVIEW 2013\vi.lib\``) oder der
gleiche Ordner in dem auch das zu öffnende Beispiel gespeichert ist. In beiden
Fällen wird LabVIEW die ``Tinkerforge.dll`` automatisch finden und nicht
Nachfragen. Allderdings wird LabVIEW möglicherweise darüber warnen, dass die
DLL aus einen anderen Ordner geladen wurde. Diese Warnungs kann ignoriert
werden.

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu ``examples/Brick/Stepper/ExampleConfiguration.nb`` in
LabVIEW öffnen, die UID des Stepper Bricks eintragen und ausführen.

Hier ein weiteres :ref:`Beispiel <barometer_bricklet_labview_examples>`,
das einen Graph der gemessenen Luftdruckwerte eines Barometer Bricklets
zeigt.

.. image:: /Images/Screenshots/labview_example_frontpanel.jpg
   :scale: 100 %
   :alt: Frontpanel Barometer Bricklet Graph Beispiel
   :align: center

Und hier das dazugehörige Blockdiagramm:

.. image:: /Images/Screenshots/labview_example_blockdiagram_small.png
   :scale: 100 %
   :alt: Block Diagramm Barometer Bricklet Graph Beispiel
   :align: center
   :target: ../_images/Screenshots/labview_example_blockdiagram.png

API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_LabVIEW_links.table
