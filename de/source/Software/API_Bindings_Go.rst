
.. _api_bindings_go:

Go - API Bindings
=================

Die Go Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Go Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``github.com/Tinkerforge/go-api-bindings`` den Quelltext der Bindings
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Voraussetzungen
---------------

* Go Compiler 1.11 oder neuer

.. _api_bindings_go_install:

Installation
------------

Die Go Bindings können auf zwei Weisen installiert werden:
von :ref:`GitHub <api_bindings_go_install_github>` oder vom
:ref:`Quelltext <api_bindings_go_install_source>`.

.. _api_bindings_go_install_github:

Von GitHub
^^^^^^^^^^

Die Bindings stehen auf `GitHub
<https://github.com/Tinkerforge/go-api-bindings>`__ bereit (dazu wird die ZIP
Datei der Bindings nicht benötigt). Von dort können sie mit
dem ``go get`` Tool installiert werden::

 go get -u github.com/Tinkerforge/go-api-bindings

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das GitHub
Repository beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_go_install_source:

Vom Quelltext
^^^^^^^^^^^^^

Dazu muss das ``github.com`` Verzeichnis aus der ZIP Datei in ein beliebiges
Verzeichnis entpackt werden.

In die ``go.mod`` Datei des Go Programms muss dann diese Zeile eingefügt werden,
um dem Go Compiler mitzuteilen wo die Go Bindings zu finden sind::

 replace github.com/Tinkerforge/go-api-bindings => /path/to/your/github.com/Tinkerforge/go-api-bindings

Dabei muss der ``/path/to/your`` Teil durch das Verzeichnis ersetzt werden,
in die das ``github.com`` Verzeichnis aus der ZIP Datei entpackt wurde.

Dann ist auch schon alles bereit, um Beispiele testen zu können.

Test eines Beispiels
--------------------

Um ein Go Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
auf der Kommandozeile kompiliert. Dafür nutzen wir die Datei
``example_configuration.go`` aus dem ``examples/StepperBrick/``-Ordner der
ZIP Datei.

Am Anfang des Beispiels ist mit ``ADDR`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost:4223`` richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: go

    const ADDR string = "localhost:4223"
    const UID string = "XXYYZZ" // Change XXYYZZ to the UID of your Stepper Brick.

Jetzt kann das Projekt mit ``go run example_configuration.go`` kompiliert
und ausgeführt werden.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Go_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Go>
   Bricks <Bricks_Go>
   Bricks (Abgekündigt) <Bricks_Go_Discontinued>
   Bricklets <Bricklets_Go>
   Bricklets (Abgekündigt) <Bricklets_Go_Discontinued>
