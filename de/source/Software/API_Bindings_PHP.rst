
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-php">Software</a> / PHP - API Bindings

.. _api_bindings_php:

PHP - API Bindings
==================

**Voraussetzungen**: PHP 5.3 oder neuer mit ``bcmath`` und ``sockets`` Erweiterung

Die PHP Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen aus
einem PEAR Paket mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``Tinkerforge.tgz``), dem Quelltext des PEAR
Pakets (in ``source/``) und allen verfügbaren PHP Beispielen (in ``examples/``).

Das PEAR Paket kann mit Hilfe des pear Tools installiert werden::

 pear install Tinkerforge.tgz

Danach können alle Beispiel unverändert verwendet werden.


.. _api_bindings_php_install:

Installation
------------

TODO


Test eines Beispiels
--------------------

Um ein PHP Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.




Wenn das PEAR Paket nicht verwendet werden soll oder kann, dann kann der
Quelltext auch direkt verwendet werden. Dafür muss der ``Tinkerforge`` Ordner vom
``source/`` Ordner und das Beispiel, das ausprobiert werden soll (z.B. das
Stepper Konfigurationsbeispiel
``examples/brick/stepper/ExampleConfiguration.php``), in einen neuen Ordner kopiert
werden::

 example_project/
  -> Tinkerforge/
  -> ExampleConfiguration.php

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopieren werden. Das Stepper Brick
Beispiel benötigt ``IPConnection.php`` und ``BrickStepper.php``::

 example_project/
  -> IPConnection.php
  -> BrickStepper.php
  -> ExampleConfiguration.php

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``Tinkerforge``
Ordner aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: php

    <?php

    require_once('Tinkerforge/IPConnection.php');
    require_once('Tinkerforge/BrickStepper.php');
    ...

    ?>

muss dort nun dies stehen:

.. code-block:: php

    <?php

    require_once('IPConnection.php');
    require_once('BrickStepper.php');
    ...

    ?>

Jetzt kann das Beispiel wieder ausgeführt werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_PHP_links.table
