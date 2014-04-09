
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / JavaScript - API Bindings

.. _api_bindings_javascript:

JavaScript - API Bindings
=========================

**Voraussetzungen**: Node.js 0.10 oder neuer oder jeder aktuelle Browser mit
WebSocket-Unterstützung (getestet mit Chrome, Firefox und IE)

Die JavaScript Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem Node.js NPM Package ``tinkerforge.tgz`` und der WebSocket-basierten
Browser-Version (in ``browser/``) der Bindings für alle Tinkerforge Bricks und
Bricklets. Außerdem liegt der Quelltext der Node.js Implementierung (in
``nodejs/source/``) und die Beispiele (in ``nodejs/examples/``) bei, sowie der
Quelltext der Browser-Version (in ``browser/source/``) die HTML Beispiele (in
``browser/examples/``).

Das NPM Package kann entweder mittels ``sudo npm -g install tinkerforge.tgz``
aus der Datei im ZIP installiert werden, oder aus der NPM Registry mittels
``sudo npm -g install tinkerforge``. Danach können alle Node.js Beispiel
unverändert verwendet werden.

Test eines Beispiels
--------------------

Wenn das NPM Package nicht verwenden werden soll oder kann, dann kann der
Quelltext auch direkt verwendet werden. Dafür muss der ``Tinkerforge`` Ordner
vom ``nodejs/source/`` Ordner und das Beispiel, das ausprobiert werden soll
(z.B. das Stepper Konfigurationsbeispiel
``nodejs/examples/Brick/Stepper/ExampleConfiguration.js``), in einen Ordner
kopiert werden::

 example_folder/
 -> Tinkerforge/
 -> ExampleConfiguration.js

Dann muss noch der ``require`` Aufruf angepasst werden. Statt:

.. code-block::javascript

    var Tinkerforge = require('tinkerforge');

    var ipcon = new Tinkerforge.IPConnection();
    var stepper = new Tinkerforge.BrickStepper(UID, ipcon);

muss dort nun dies stehen:

.. code-block::javascript

    var IPConnection = require('./Tinkerforge/IPConnection');
    var BrickStepper = require('./Tinkerforge/BrickStepper');

    var ipcon = new IPConnection();
    var stepper = new BrickStepper(UID, ipcon);

Um eines der HTML Beispiele zu testen muss nur der Quelltext der Browser
Implementierung ``browser/source/Tinkerforge.js`` und das gewünschte HTML
Beispiel in einen Ordner kopiert werden und kann dann einfach im Browser
geöffnet werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_JavaScript_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
