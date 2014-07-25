
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-labview">Software</a> / LabVIEW - API Bindings

.. _api_bindings_labview:

LabVIEW - API Bindings
======================

Die LabVIEW Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen LabVIEW Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.dll``, eine vorkompilierte .NET Bibliothek
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets im LabVIEW 2010
  und LabVIEW 2013 Format

Die LabVIEW Bindings basieren auf den :ref:`C# Bindings <api_bindings_csharp>`.
Seit Version 2.0.0 sind die C# Bindings `CLS
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. LabVIEWs `.NET Unterstützung
<http://zone.ni.com/reference/en-XX/help/371361K-01/lvcomm/dotnet_pal/>`__.


Voraussetzungen
---------------

* LabVIEW auf Windows mit .NET Unterstützung


.. _api_bindings_labview_install:

Installation
------------

Damit die Bindings funktionieren können muss LabVIEW in der Lage sein die
``Tinkerforge.dll`` zu finden. Beim Öffnen einen Beispiels wird LabVIEW nach
der DLL suchen und nachfragen falls sie nicht gefunden werden kann. Dieses
Suchen-und-Nachfragen kann vermieden werden, indem die ``Tinkerforge.dll`` in
einem LabVIEW bekannten Ordern gespeichert wird. Die einfachsten Möglichkeiten
ist der ``vi.lib`` Ordern der LabVIEW Installation::

 C:\Programme\National Instruments\LabVIEW 2013\vi.lib\

Dann kann LabVIEW die ``Tinkerforge.dll`` automatisch finden und nicht
Nachfragen. Allderdings wird LabVIEW möglicherweise darüber warnen, dass
die DLL aus einen anderen Ordner geladen wurde. Diese Warnung kann ignoriert
werden.


Test eines Beispiels
--------------------

Um ein LabVIEW Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Stepper Brick
^^^^^^^^^^^^^

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
ausführen. Dafür muss zuerst die ``Example Configuration.vi`` Datei aus dem
``examples/Brick/Stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> Example Configuration.vi

Wenn die Bindings **nicht** in den ``vi.lib`` Ordern der LabVIEW Installation
kopiert wurden, dann muss auch noch die ``Tinkerforge.dll`` in den
``example_project/`` Ordner kopiert werden bevor das Beispiel in LabVIEW
geöffnet werden kann::

 example_project/
  -> Tinkerforge.dll
  -> Example Configuration.vi

Am Anfang des Beispiels ist mit ``host`` und ``port`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``uid`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden.

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können.

Barometer Bricklet
^^^^^^^^^^^^^^^^^^

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
