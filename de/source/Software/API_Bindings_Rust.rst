
.. _api_bindings_rust:

Rust - API Bindings
===================

Die Rust Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Rust Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``src/`` den Quelltext der Bindings
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Rust-Bindings sind auch auf `crates.io <https://crates.io/crates/tinkerforge>`_ zu finden.


Voraussetzungen
---------------

* Der Rust-Compiler in Version 1.31 oder neuer.


.. _api_bindings_rust_install:

Installation
------------

Die Rust-Bindings können mit der Zip-Datei oder von crates.io installiert werden.

Durch Hinzufügen von ``tinkerforge = "2.0"`` in den ``[dependencies]``-Abschnitt der
``Cargo.toml`` eines Projektes, wird cargo beim nächsten Durchlauf die Bindings und alle
Abhängigkeiten herunterladen.

Um die Bindings aus der Zip-Datei zu installieren, muss diese entpackt werden.
Danach wird durch das Hinzufügen von ``tinkerforge = {path=[Pfad/hier/einfügen]}`` 
im ``[dependencies]``-Abschnitt der ``Cargo.toml`` und Einfügen des korrekten Pfades zum
entpackten Ordner (ohne ``src``) die Abhängigkeit registriert. Cargo wird beim nächsten Durchlauf
die Abhängigkeiten der Bindings herunterladen.

Test eines Beispiels
--------------------

Um ein Rust Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
auf der Kommandozeile kompiliert. Dafür muss zuerst ein neuer Ordner ``example_project``
erstellt und in dem ``cargo init`` ausgeführt werden. Dann muss die Datei 
``example_configuration.rs`` aus dem ``examples/StepperBrick/``-Ordner der Zip in den von
Cargo erstellten ``src``-Ordner kopiert werden. Diese Datei muss dann in ``main.rs`` umbenannt
werden, die von Cargo erstellte Datei selben Namens kann gelöscht oder überschrieben werden::

 example_project/
  -> Cargo.toml
  -> src/main.rs (war davor example_configuration.rs)


Danach muss entweder ``tinkerforge = "2.0"`` oder ``tinkerforge = {path=[your/path/here]}`` 
in den ``[dependencies]``-Abschnitt der ``Cargo.toml`` des Projekts eingefügt werden.

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: rust

    const HOST: &str = "localhost";
    const PORT: u16 = 4223;
    const UID: &str = "XXYYZZ"; // Change XXYYZZ to the UID of your Stepper Brick.

Jetzt kann das Projekt mit ``cargo run`` kompiliert und ausgeführt werden.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Rust_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Rust>
   Bricks <Bricks_Rust>
   Bricks (Abgekündigt) <Bricks_Rust_Discontinued>
   Bricklets <Bricklets_Rust>
   Bricklets (Abgekündigt) <Bricklets_Rust_Discontinued>
