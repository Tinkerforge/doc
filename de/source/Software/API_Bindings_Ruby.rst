
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Ruby - API Bindings

.. _api_bindings_ruby:

Ruby - API Bindings
===================

**Voraussetzungen**: Ruby 1.9 oder neuer

Die Ruby Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen aus
einem Ruby GEM mit den Bindings für alle
Tinkerforge Bricks und Bricklets (``tinkerforge.gem``), dem Quelltext des GEMs
(in ``source/``) und allen verfügbaren Ruby Beispielen (in ``examples/``).

Der GEM kann mit Hilfe des gem Tools installiert werden::

 gem install tinkerforge.gem

Der GEM wird auch auf `rubygems.org <https://rubygems.org/gems/tinkerforge>`__
gehostet und kann alternativ auch von dort installiert werden::

 gem install tinkerforge

Danach können alle Beispiel unverändert verwendet werden.


Test eines Beispiels
--------------------

Wenn der GEM nicht verwendet werden soll oder kann, dann kann der Quelltext auch
direkt verwendet werden. Dafür muss der ``tinkerforge`` Ordner vom ``source/``
Ordner und das Beispiel, das ausprobiert werden soll (z.B. das Stepper
Konfigurationsbeispiel ``examples/brick/stepper/example_configuration.rb``),
in einen Ordner kopiert werden::

 example_folder/
  -> tinkerforge/
  -> example_configuration.rb

Damit Ruby das ``tinkerforge`` findet muss es per ``-I.`` Option angewiesen
werden im aktuelle Ordner danach zu schauen::

 ruby -I. example_configuration.rb

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopiert werden. Das Stepper Brick
Beispiel benötigt ``ip_connection.rb`` und ``brick_stepper.rb``::

 example_folder/
  -> ip_connection.rb
  -> brick_stepper.rb
  -> example_configuration.rb

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``tinkerforge``
Package aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: ruby

 require 'tinkerforge/ip_connection'
 require 'tinkerforge/brick_stepper'

muss dort nun dies stehen:

.. code-block:: ruby

 require 'ip_connection'
 require 'brick_stepper'

Jetzt kann das Beispiel wieder ausgeführt werden.
