
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-mathematica">Software</a> / Mathematica - API Bindings

.. _api_bindings_mathematica:

Mathematica - API Bindings
==========================

**Voraussetzungen**: Mathematica 5.0 oder neuer auf Windows, Linux und Mac OS X
mit .NET/Link Unterstützung

Die Mathematica Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Mathematica Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.dll``, eine vorkompilierte .NET Bibliothek
* in ``source/`` den Quelltext für ``Tinkerforge.dll``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Mathematica Bindings basieren auf den :ref:`C# Bindings <api_bindings_csharp>`.
Seit Version 2.0.0 sind die C# Bindings `CLS
<http://de.wikipedia.org/wiki/Common_Language_Specification>`__-konform.
Dies erlaubt es die Bindings mit allen `.NET kompatiblen Sprachen
<http://de.wikipedia.org/wiki/Liste_von_.NET-Sprachen>`__ zu verwenden, wie
z.B. Mathematicas `.NET/Link Unterstützung
<http://reference.wolfram.com/language/NETLink/tutorial/CallingNETFromTheWolframLanguage.html>`__.
Die .NET/Link Unterstützung in Mathematica benötigt das `.NET Framework
<http://www.microsoft.com/net>`__ auf Windows und das `Mono Framework
<http://www.mono-project.com/>`__ unter Linux und Mac OS X.


.. _api_bindings_mathematica_install:

Installation
------------

Die Installation der Mathematica Bindings is optional, sie können installiert
werden, sie können aber auch ohne Installation genutzt werden. Zur Installation
einfach die ``Tinkerforge.dll`` in Mathematicas .NET/Link Ordner kopieren.
Dieser ist unter Windows hier zu finden::

 C:\Program Files\Wolfram Research\Mathematica\9.0\SystemFiles\Links\NETLink\

hier unter Linux::

 /usr/local/Wolfram/Mathematica/9.0/SystemFiles/Links/NETLink/

und hier unter Mac OS X::

 /Applications/Mathematica.app/SystemFiles/Links/NETLink/


Test eines Beispiels
--------------------

Um ein Mathematica Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.




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

Hier ein weiteres :ref:`Beispiel <temperature_bricklet_mathematica_examples>`,
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
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Mathematica_links.table
