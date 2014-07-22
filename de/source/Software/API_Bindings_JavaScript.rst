
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-javascript">Software</a> / JavaScript - API Bindings

.. _api_bindings_javascript:

JavaScript - API Bindings
=========================

**Voraussetzungen**: Node.js 0.10 oder neuer oder jeder aktuelle Browser mit
WebSocket-Unterstützung (getestet mit Chrome, Firefox und IE)

Die JavaScript Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen JavaScript Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``nodejs/tinkerforge.tgz``, ein Node.js NPM Package (installierbar mit ``npm`` Tool)
* in ``nodejs/source/`` den Quelltext für ``tinkerforge.tgz``
* in ``nodejs/examples/`` die Node.js Beispiele für alle Bricks und Bricklets
* in ``browser/source/`` den Quelltext der Browser Version der Bindings
* in ``browser/examples/`` die HTML Beispiele für alle Bricks und Bricklets


.. _api_bindings_javascript_install:

Installation
------------

TODO


Test eines Node.js Beispiels
----------------------------

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

.. code-block:: javascript

    var Tinkerforge = require('tinkerforge');

    var ipcon = new Tinkerforge.IPConnection();
    var stepper = new Tinkerforge.BrickStepper(UID, ipcon);

muss dort nun dies stehen:

.. code-block:: javascript

    var IPConnection = require('./Tinkerforge/IPConnection');
    var BrickStepper = require('./Tinkerforge/BrickStepper');

    var ipcon = new IPConnection();
    var stepper = new BrickStepper(UID, ipcon);

Test eines HTML Beispiels
-------------------------

Die Browser-Version der JavaScript Bindings verwendet `WebSockets
<http://de.wikipedia.org/wiki/WebSocket>`__. WebSockets werden von Brick
Daemon (seit Version 2.1.0) und der Ethernet Extension (seit Master Brick
Firmware Version 2.2.0) unterstützt. Sie sind allerdings standardmäßig nicht
aktiviert und müssen erst konfiguriert werden:

* :ref:`Brick Daemon: WebSockets <brickd_websockets>`
* :ref:`Ethernet Extension: WebSockets <ethernet_configuration_websockets>`

Um eines der HTML Beispiele zu testen muss die Browser JavaScript Datei
``browser/source/Tinkerforge.js`` und das gewünschte HTML Beispiel in einen
Ordner kopiert werden und kann dann einfach im Browser geöffnet werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_JavaScript_links.table
