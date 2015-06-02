
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-ruby">Software</a> / Ruby - API Bindings

.. _api_bindings_ruby:

Ruby - API Bindings
===================

Die Ruby Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Ruby Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``tinkerforge.gem``, ein Ruby GEM (installierbar mit `gem
  <https://rubygems.org/pages/download>`__ Tool)
* in ``source/`` den Quelltext für ``tinkerforge.gem``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* Ruby 1.9 oder neuer


.. _api_bindings_ruby_install:

Installation
------------

Die Ruby Bindings können installiert werden, können aber auch ohne Installation
verwendet werden.

Vom Ruby GEM
^^^^^^^^^^^^

Die Bindings stehen als GEM auf `rubygems.org
<https://rubygems.org/gems/tinkerforge>`__ bereit. Von dort können sie mit
dem `gem <https://rubygems.org/pages/download>`__ Tool und folgendem Befehl
installiert werden (dazu wird die ZIP Datei der Bindings nicht benötigt).
Abhängig von der Art der Ruby Installation muss dies möglicherweise mit
``sudo`` bzw. als Administrator ausgeführt werden::

 gem install tinkerforge

Alternativ ist der GEM auch in der ZIP Datei der Bindings enthalten und kann
mit folgendem Befehl installiert werden. Möglicherweise muss dies mit ``sudo``
bzw. als Administrator ausgeführt werden::

 gem install tinkerforge.gem

Dann ist auch schon alles bereit, um Beispiele testen zu können. Der GEM
beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.


Ohne Installation
^^^^^^^^^^^^^^^^^

Die Bindings müssen nicht unbedingt installiert werden. Stattdessen kann auch
einfach der ``tinkerforge/`` Ordner vom ``source/`` Ordner in den gleichen
Ordner wie dein Ruby Programm kopiert werden. Der Abschnitt über den Test eines
Beispiels vermittelt mehr Details darüber.


Test eines Beispiels
--------------------

Um ein Ruby Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``example_configuration.rb`` Datei aus dem
``examples/brick/stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> example_configuration.rb

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: ruby

  HOST = 'localhost'
  PORT = 4223
  UID = 'XYZ' # Change to your UID

Wenn die Bindings installiert wurden, dann kann das Beispiele jetzt direkt
ausgeführt werden::

 ruby example_configuration.rb

Wenn die Bindings **nicht** installiert wurden, dann kann der Quelltext der
Bindings auch direkt verwendet werden. Dafür muss der ``tinkerforge/`` Ordner
vom ``source/`` Ordner in den ``example_project/`` Ordner kopiert werden::

 example_project/
  -> tinkerforge/
  -> example_configuration.rb

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können.
Damit Ruby den ``tinkerforge/`` Ordner findet muss es per ``-I.`` Option
angewiesen werden im aktuelle Ordner danach zu suchen::

 ruby -I. example_configuration.rb


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Ruby_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Ruby>
   Bricks <Bricks/Bricks_Ruby>
   Bricklets <Bricklets/Bricklets_Ruby>
