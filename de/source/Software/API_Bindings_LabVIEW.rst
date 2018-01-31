
.. _api_bindings_labview:

LabVIEW - API Bindings
======================

Die LabVIEW Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen LabVIEW Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``net20/Tinkerforge.dll``, eine vorkompilierte .NET 2.0 Bibliothek
* ``net40/Tinkerforge.dll``, eine vorkompilierte .NET 4.0 Bibliothek
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets im LabVIEW 2010
  und LabVIEW 2013 Format

Die LabVIEW Bindings basieren auf den :ref:`C# Bindings <api_bindings_csharp>`.
Seit Version 2.0.0 sind die C# Bindings `CLS
<https://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `.NET kompatiblen Sprachen
<https://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. LabVIEWs `.NET Unterstützung
<http://zone.ni.com/reference/en-XX/help/371361K-01/lvcomm/dotnet_pal/>`__.


Voraussetzungen
---------------

* LabVIEW auf Windows mit .NET Unterstützung


.. _api_bindings_labview_install:

Installation
------------

Damit die Bindings funktionieren können muss LabVIEW in der Lage sein die
``Tinkerforge.dll`` zu finden. Die einfachsten Möglichkeiten ist es die
``Tinkerforge.dll`` im LabVIEW Installationsordner abzulegen. Der
Standardinstallationsordner für LabVIEW 2015 ist::

 C:\Programme\National Instruments\LabVIEW 2015\

Die ``Tinkerforge.dll`` kann auch im gleichen Ordner wie die .vi Datei, die
diese nutzen soll, abgelegt werden. In beiden Fällen sollte LabVIEW die
``Tinkerforge.dll`` automatisch finden.

Die ZIP Datei für die Bindings beinhaltet zwei verschiedene Versionen der
``Tinkerforge.dll``:

* Für LabVIEW 2011 und ältere LabVIEW Versionen sollte die ``Tinkerforge.dll``
  aus dem ``net20`` Ordner verwendet werden.
* Für LabVIEW 2012 und neuere LabVIEW Versionen sollte die ``Tinkerforge.dll``
  aus dem ``net40`` Ordner verwendet werden.

Warnungen
^^^^^^^^^

LabVIEW warnt möglicherweise darüber, dass die ``Tinkerforge.dll`` aus einen
anderen Ordner geladen wurde. Diese Warnung kann ignoriert werden.

Es kann auch sein, dass LabVIEW darüber warnt, dass eine ``Tinkerforge.dll`` mit
abweichender Versionsnummer gefunden wurde. Wenn die gefundene Versionsnummer
höher als die gesucht ist, kann diese Warnung ignoriert werden. Andernfalls
sollten die LabVIEW Bindings aktualisiert werden.

Fehlermeldungen
^^^^^^^^^^^^^^^

Falls LabVIEW Fehler 1386 "Die angegebene .NET-Klasse ist in LabVIEW nicht
verfügbar." meldet, dann bitte sicherstellen, dass alle ".NET Konstruktor"
Knoten der .vi Datei richtig eingestellt sind. Per Doppelklick auf einen
".NET Konstruktor" Knoten den .NET Konstruktor Auswahldialog aufrufen und
"Tinkerforge" als Assembly auswählen.

Falls der .NET Konstruktor Auswahldialog meldet "Beim Laden der Assembly trat
ein Fehler auf.", dann bitte im Windows Explorer überprüfen, ob die
``Tinkerforge.dll`` als von einem anderen Computer stammend markiert ist. Falls
das der Fall ist, dann verweigert LabVIEW das Laden der ``Tinkerforge.dll``.

Den Eigenschaftendialog der ``Tinkerforge.dll`` im Windows Explorer aufrufen.
Falls dort unten auf der "Allgemein" Seite ein "Zulassen" Häkchen ist, dann ist
die Datei blockiert. Ein Klick auf das "Zulassen" Häkchen behebt das Problem
und nach einem Neustart von LabVIEW sollte die ``Tinkerforge.dll`` jetzt auch
geladen werden können.


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

Wenn die ``Tinkerforge.dll`` **nicht** in den LabVIEW Installationsordner
kopiert wurde, dann muss auch noch die ``Tinkerforge.dll`` in den
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

API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_LabVIEW_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_LabVIEW>
   Bricks <Bricks_LabVIEW>
   Bricklets <Bricklets_LabVIEW>
