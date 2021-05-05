
.. _api_bindings_php:

PHP - API Bindings
==================

Die PHP Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen PHP Skripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.tgz``, ein PEAR Package (installierbar mit `pear
  <https://pear.php.net/>`__ Tool)
* in ``source/`` den Quelltext für ``Tinkerforge.tgz``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Voraussetzungen
---------------

* PHP 5.3 oder neuer mit ``bcmath`` und ``sockets`` Erweiterung

.. _api_bindings_php_install:

Installation
------------

Die PHP Bindings können auf zwei Weisen installiert werden:
von unserem :ref:`APT Repository <api_bindings_php_install_apt>` für Debian
basierte Linux Distributionen oder vom
:ref:`PEAR Package <api_bindings_php_install_pear>`. Die Bindings können aber
auch :ref:`ohne Installation <api_bindings_php_install_without>` genutzt werden.

.. _api_bindings_php_install_apt:

Vom APT Repository
^^^^^^^^^^^^^^^^^^

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit (dazu wird die ZIP Datei der Bindings nicht benötigt).
Zuerst das :ref:`APT Repository einrichten <apt_repository_setup>` dann
die Bindings installieren::

 sudo apt install php-tinkerforge

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das Debian
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_php_install_pear:

Vom PEAR Package
^^^^^^^^^^^^^^^^

Die Bindings stehen als PEAR Package bereit, das mit dem `pear
<https://pear.php.net/>`__ Tool und folgendem Befehl installiert werden kann.
Abhängig von der Art der PHP Installation muss dies möglicherweise mit ``sudo``
bzw. als Administrator ausgeführt werden::

 pear install Tinkerforge.tgz

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das PEAR
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_php_install_without:

Ohne Installation
^^^^^^^^^^^^^^^^^

Die Bindings müssen nicht unbedingt installiert werden. Stattdessen kann auch
einfach der ``Tinkerforge/`` Ordner vom ``source/`` Ordner in den gleichen
Ordner wie dein PHP Skript kopiert werden. Der Abschnitt über den Test eines
Beispiels vermittelt mehr Details darüber.

Test eines Beispiels
--------------------

Um ein PHP Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``ExampleConfiguration.php`` Datei aus dem
``examples/Brick/Stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> ExampleConfiguration.php

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: php

  <?php

  const HOST = 'localhost';
  const PORT = 4223;
  const UID = 'XXYYZZ'; // Change XXYYZZ to the UID of your Stepper Brick

  ?>

Wenn die Bindings installiert wurden, dann kann das Beispiele jetzt direkt
ausgeführt werden::

 php ExampleConfiguration.php

Wenn die Bindings **nicht** installiert wurden, dann kann der Quelltext der
Bindings auch direkt verwendet werden. Dafür muss der ``Tinkerforge/`` Ordner
vom ``source/`` Ordner in den ``example_project/`` Ordner kopiert werden und
PHP wird die Bindings automatisch finden::

 example_project/
  -> Tinkerforge/
  -> ExampleConfiguration.php

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 php ExampleConfiguration.php


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_PHP_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_PHP>
   Bricks <Bricks_PHP>
   Bricks (Abgekündigt) <Bricks_PHP_Discontinued>
   Bricklets <Bricklets_PHP>
   Bricklets (Abgekündigt) <Bricklets_PHP_Discontinued>
