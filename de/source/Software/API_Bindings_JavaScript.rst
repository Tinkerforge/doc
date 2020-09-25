
.. _api_bindings_javascript:

JavaScript - API Bindings
=========================

Die JavaScript Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen JavaScript Skripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``nodejs/tinkerforge.tgz``, ein Node.js NPM Package (installierbar mit `npm
  <https://www.npmjs.com/>`__ Tool)
* in ``nodejs/source/`` den Quelltext für ``tinkerforge.tgz``
* in ``nodejs/examples/`` die Node.js Beispiele für alle Bricks und Bricklets
* in ``browser/source/`` den Quelltext der Browser Version der Bindings
* in ``browser/examples/`` die HTML Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* Node.js 0.10 oder neuer oder jeder aktuelle Browser mit
  WebSocket Unterstützung (getestet mit Chrome, Firefox und Internet Explorer)

.. note:
  Unterstützung für 64-Bit-Ganzzahlen wurde erst kürzlich zu Node.js und den Browsern hinzugefügt.
  Funktionen und Callbacks, die Unterstützung von 64-Bit-Zahlen benötigen geben den Fehlercode 91
  (`IPConnection.ERROR_INT64_NOT_SUPPORTED``) zurück, wenn sie in älteren Node.js-Versionen
  oder Browsern aufgerufen werden.

.. _api_bindings_javascript_install:

Installation
------------

Ob und wie die JavaScript Bindings installiert werden können oder müssen hängt
von der Art der Verwendung ab.

Node.js
^^^^^^^

Die Node.js Version der Bindings können auf zwei Weisen installiert werden:
von unserem :ref:`APT Repository <api_bindings_javascript_install_apt>` für
Debian basierte Linux Distributionen oder vom
:ref:`NPM Package <api_bindings_javascript_install_npm>`. Die Bindings können
aber auch :ref:`ohne Installation <api_bindings_javascript_install_without>`
genutzt werden.

.. _api_bindings_javascript_install_apt:

Vom APT Repository
""""""""""""""""""

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit (dazu wird die ZIP Datei der Bindings nicht benötigt).
Zuerst das :ref:`APT Repository einrichten <apt_repository_setup>` dann
die Bindings installieren::

 sudo apt install node-tinkerforge

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das Debian
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_javascript_install_npm:

Vom NPM Package
"""""""""""""""

Für die Verwendung der Bindings mit Node.js steht in NPM Package bereit. Dies
ist im `Node.js Package Repository <https://www.npmjs.com/package/tinkerforge>`__
verfügbar und kann von dort mit folgendem Befehl global installiert werden.
Möglicherweise muss dies mit ``sudo`` bzw. als Administrator ausgeführt werden::

 npm -g install tinkerforge

Alternativ ist das NPM Package auch in der ZIP Datei der Bindings enthalten und
kann mit folgendem Befehl global installiert werden. Möglicherweise muss dies
mit ``sudo`` bzw. als Administrator ausgeführt werden::

 npm -g install nodejs/tinkerforge.tgz

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das NPM Package
beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_javascript_install_without:

Ohne Installation
"""""""""""""""""

Die JavaScript Bindings für Node.js müssen nicht unbedingt installiert werden.
Stattdessen kann auch einfach der ``Tinkerforge/`` Ordner und die
``Tinkerforge.js`` Datei vom ``nodejs/source/`` Ordner in den gleichen Ordner
wie dein JavaScript Skript kopiert werden. Der Abschnitt über den Test eines
Beispiels vermittelt mehr Details darüber.

HTML
^^^^

Für die Verwendung der Bindings im Browser steht im ``browser/source/`` Ordner
eine ``Tinkerforge.js`` Datei bereit, die die kompletten Bindings beinhaltet.
Diese wird einfach in das gleiche Verzeichnis wie deine HTML Datei kopiert. Der
Abschnitt über den Test eines Beispiels vermittelt mehr Details darüber.


Test eines Beispiels
--------------------

Um ein JavaScript Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Node.js
^^^^^^^

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``ExampleConfiguration.js`` Datei aus dem
``nodejs/examples/Brick/Stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> ExampleConfiguration.js

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: javascript

  var HOST = 'localhost';
  var PORT = 4223;
  var UID = 'XXYYZZ'; // Change XXYYZZ to the UID of your Stepper Brick

Wenn die Bindings installiert wurden, dann kann das Beispiele jetzt direkt
ausgeführt werden::

 node ExampleConfiguration.js

Wenn die Bindings **nicht** installiert wurden, dann kann der Quelltext der
Bindings auch direkt verwendet werden. Dafür muss der ``Tinkerforge/`` Ordner
und die ``Tinkerforge.js`` Datei vom ``nodejs/source/`` Ordner in den
``example_project/`` Ordner kopiert werden::

 example_project/
  -> Tinkerforge/
  -> Tinkerforge.js
  -> ExampleConfiguration.js

Dann muss noch der ``require`` Aufruf in ``ExampleConfiguration.js`` angepasst
werden. Statt:

.. code-block:: javascript

  var Tinkerforge = require('tinkerforge');

muss dort nun dies stehen:

.. code-block:: javascript

  var Tinkerforge = require('./Tinkerforge.js');

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 node ExampleConfiguration.js


HTML
^^^^

Die Browser Version der JavaScript Bindings verwendet `WebSockets
<https://de.wikipedia.org/wiki/WebSocket>`__. WebSockets werden von Brick
Daemon (seit Version 2.1.0) und der Ethernet Extension (seit Master Brick
Firmware Version 2.2.0) unterstützt. Sie sind allerdings standardmäßig nicht
aktiviert und müssen erst konfiguriert werden:

* :ref:`Brick Daemon: WebSockets <brickd_websockets>`
* :ref:`Ethernet Extension: WebSockets <ethernet_extension_websockets>`
* :ref:`WIFI Extension 2.0: Ports (WebSocket) <wifi_v2_extension_ports>`

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``ExampleConfiguration.html`` Datei aus dem
``browser/examples/Brick/Stepper/`` Ordner und die ``Tinkerforge.js`` Datei
aus dem ``browser/source/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> Tinkerforge.js
  -> ExampleConfiguration.html

Dann ist auch schon alles bereit, um dieses Beispiel im Browser zu öffnen.

Am Anfang des Beispiels gibt es Eingabefelder für Host und Port. Hier
muss angegeben werden unter welcher Netzwerkadresse der Stepper Brick zu
erreichen ist. Ist er lokal per USB angeschlossen dann ist ``localhost`` und
4280 richtig. Als UID muss die UID des angeschlossen Stepper Bricks
angegeben werden, diese kann über den Brick Viewer ermittelt werden. Ist alles
richtig eingegeben kann über den "Start Example" Knopf das Beispiel gestartet
werden.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_JavaScript_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_JavaScript>
   Bricks <Bricks_JavaScript>
   Bricks (Abgekündigt) <Bricks_JavaScript_Discontinued>
   Bricklets <Bricklets_JavaScript>
   Bricklets (Abgekündigt) <Bricklets_JavaScript_Discontinued>
