
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

**Voraussetzungen**: Perl 5.014 oder neuer

Die Perl Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem CPAN Paket mit den Bindings für alle Tinkerforge Bricks und Bricklets
(``Tinkerforge.tar.gz``), dem Quelltext des CPAN Pakets (in ``source/``) und
allen verfügbaren Perl Beispielen (in ``examples/``).

Das Paket wird in Kürze auch auf CPAN verfügbar sein und kann dann von dort aus
installiert werden.

Das vorläufige CPAN Paket (``Tinkerforge.tar.gz``) ist in der ZIP Datei
enthalten. Es kann entpackt und dann mit den folgenden Befehlen installiert
werden::

 perl Makefile.PL
 make
 make test
 make install

Danach können alle Beispiel unverändert verwendet werden.


Test eines Beispiels
--------------------

Wenn das CPAN Paket nicht verwenden werden soll oder kann, dann kann der
Quelltext auch direkt verwendet werden. Dafür muss der ``Tinkerforge`` Ordner
vom ``source/`` Ordner und das Beispiel, das ausprobiert werden soll (z.B. das
Stepper Konfigurationsbeispiel
``examples/brick/stepper/example_configuration.pl``), in einen Ordner kopiert
werden::

 example_folder/
  -> Tinkerforge/
  -> example_configuration.pl

Dann muss noch am Anfang von ``example_configuration.pl`` folgende Zeile
eingefügt werden:

.. code-block:: perl

 use lib './';

Falls nur einige ausgewählte Bricks oder Bricklets verwendet werden sollen und
keine unnötigen Dateien im Projekt auftauchen sollen, dann können auch nur die
wirklich benötigten Dateien in einen Ordner kopiert werden. Das Stepper Brick
Beispiel benötigt ``IPConnection.pm`` und ``BrickStepper.pm``::

 example_folder/
  -> IPConnection.pm
  -> BrickStepper.pm
  -> example_configuration.pl

Nachdem diese Dateien in einen Ordner kopiert sind muss noch das ``Tinkerforge::``
Package aus dem Quelltext des Beispiels entfernt werden. Statt:

.. code-block:: perl

 use Tinkerforge::IPConnection;
 use Tinkerforge::Device;
 use Tinkerforge::BrickStepper;

mss nun dort dies stehen:

.. code-block:: perl

 use lib './';
 use IPConnection;
 use Device;
 use BrickStepper;

Jetzt kann das Beispiel wieder ausgeführt werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_Perl_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
