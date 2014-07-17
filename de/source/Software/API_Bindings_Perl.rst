
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-perl">Software</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

**Voraussetzungen**: Perl 5.014 oder neuer mit Thread::Queue 3.02 oder neuer

Die Perl Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem CPAN Paket mit den Bindings für alle Tinkerforge Bricks und Bricklets
(``Tinkerforge.tar.gz``), dem Quelltext des CPAN Pakets (in ``source/``) und
allen verfügbaren Perl Beispielen (in ``examples/``).

Es sind Deadlock-Probleme auf Windows mit Strawberry Perl und Active State Perl
bekannt. Der empfohlene Workaround dafür ist Cygwins Perl zu verwenden, das von
diesen Problemen nicht betroffen ist. Siehe diesen `PerlMonks Thread
<http://perlmonks.org/?node_id=1078634>`__ für weitere Details.

Die Bindings können auch von `CPAN <http://www.cpan.org/>`__ installiert werden
mit folgendem Befehl (wir emfehlen dafür das `CPANminus
<http://search.cpan.org/dist/App-cpanminus/lib/App/cpanminus.pm>`__ Tool
``cpanm``)::

 cpanm Tinkerforge

Das CPAN Paket (``Tinkerforge.tar.gz``) ist in der ZIP Datei
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

Jetzt kann das Beispiel wieder ausgeführt werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Perl_links.table
