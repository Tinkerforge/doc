
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-perl">Software</a> / Perl - API Bindings

.. _api_bindings_perl:

Perl - API Bindings
===================

Die Perl Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Perl Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* in ``source/`` den Quelltext der Bindings (installierbar mit ``Makefile.PL``
  Skript)
* in ``examples/`` die Beispiele für alle Bricks und Bricklets


Voraussetzungen
---------------

* Perl 5.14 oder neuer mit Thread Unterstützung, ``Digest::HMAC_SHA1`` Modul
  und ``Thread::Queue`` Modul 3.02 oder neuer


.. _api_bindings_perl_install:

Installation
------------

Die Perl Bindings können auf zwei Weisen installiert werden: von
:ref:`CPAN <api_bindings_perl_install_cpan>` oder vom
:ref:`Quelltext <api_bindings_perl_install_source>`. Die Bindings können aber
auch :ref:`ohne Installation <api_bindings_perl_install_without>` genutzt werden.


.. _api_bindings_perl_install_cpan:

Von CPAN
^^^^^^^^

Die Bindings stehen auch im Comprehensive Perl Archive Network `CPAN
<http://search.cpan.org/dist/Tinkerforge/>`__ bereit. Von dort können sie mit
dem CPANminus Tool `cpanm
<http://search.cpan.org/dist/App-cpanminus/lib/App/cpanminus.pm>`__ und
folgendem Befehl installiert werden (dazu wird die ZIP Datei der Bindings nicht
benötigt). Abhängig von der Art der Perl Installation muss dies möglicherweise
mit ``sudo`` bzw. als Administrator ausgeführt werden::

 cpanm Tinkerforge

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das CPAN
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.


.. _api_bindings_perl_install_source:

Vom Quelltext
^^^^^^^^^^^^^

Der ``source/`` Ordner beinhaltet ein ``Makefile.PL`` Skript. Um die Bindings
zu installieren müssen folgende Befehle im ``source/`` Ordner ausgeführt werden.
Abhängig von der Art der Perl Installation muss dies möglicherweise mit
``sudo`` bzw. als Administrator ausgeführt werden::

 perl Makefile.PL
 make
 make test
 make install

Dann ist auch schon alles bereit, um Beispiele testen zu können.


.. _api_bindings_perl_install_without:

Ohne Installation
^^^^^^^^^^^^^^^^^

Die Perl Bindings müssen nicht unbedingt installiert werden. Stattdessen
kann auch einfach der ``Tinkerforge/`` Ordner vom ``source/lib/`` Ordner in den
gleichen Ordner wie dein Perl Programm kopiert werden. Der Abschnitt über den
Test eines Beispiels vermittelt mehr Details darüber.


Test eines Beispiels
--------------------

Um ein Perl Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``example_configuration.pl`` Datei aus dem
``examples/brick/stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> example_configuration.pl

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: perl

  use constant HOST => 'localhost';
  use constant PORT => 4223;
  use constant UID => 'XYZ'; # Change to your UID

Wenn die Bindings vom :ref:`Quelltext <api_bindings_perl_install_source>` oder
von :ref:`CPAN <api_bindings_perl_install_cpan>` installiert wurden, dann kann
das Beispiele jetzt direkt ausgeführt werden::

 perl example_configuration.pl

Wenn die Bindings **nicht** installiert wurden, dann kann der Quelltext der
Bindings auch direkt verwendet werden. Dafür muss der ``Tinkerforge/`` Ordner
vom ``source/lib/`` Ordner in den ``example_project/`` Ordner kopiert werden::

 example_project/
  -> Tinkerforge/
  -> example_configuration.pl

Damit Perl den ``Tinkerforge/`` Ordner auch findet muss am Anfang des Beispiels
folgende Zeile eingefügt werden:

.. code-block:: perl

 use lib './';

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 perl example_configuration.pl


.. _api_bindings_perl_known_problems:

Bekannte Probleme
-----------------

Es sind Deadlock-Probleme auf Windows mit `Strawberry Perl
<http://strawberryperl.com/>`__ und `Active State Perl
<http://www.activestate.com/activeperl>`__ bekannt. Der empfohlene Workaround
dafür ist `Cygwin <https://www.cygwin.com/>`__ Perl zu verwenden, das von
diesen Problemen nicht betroffen ist. Siehe diesen `PerlMonks Thread
<http://perlmonks.org/?node_id=1078634>`__ für weitere Details.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Perl_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Perl>
   Bricks <Bricks/Bricks_Perl>
   Bricklets <Bricklets/Bricklets_Perl>
