
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-shell">Software</a> / Shell - API Bindings

.. _api_bindings_shell:

Shell - API Bindings
====================

**Voraussetzungen**: Python 2.5 oder neuer mit argparse Modul, Python 3 wird auch unterstützt

Die Shell Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem Python Script zur Interaktion mit alle
Tinkerforge Bricks und Bricklets (``tinkerforge``), einem passendes Bash
Completion Script (``tinkerforge-bash-completion.sh``) und allen verfügbaren
Shell Beispielen (in ``examples/``).

Für funktionierende Bash Completion muss sich das ``tinkerforge`` Script im
``PATH`` befinden, z.B. durch Kopieren nach ``/usr/local/bin/``. Das Bash
Completion Script ``tinkerforge-bash-completion.sh`` muss nach
``/etc/bash_completion.d/`` kopiert werden. Dann Bash Completion kann mittels::

 . /etc/bash_completion

neugeladen werden.


.. _api_bindings_shell_install:

Installation
------------

TODO


Test eines Beispiels
--------------------

Um ein Shell Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.




Alle Beispiele sind für typische Unix Shells wie z.B. Bash gemacht. Sie
funktionieren auf Linux und Mac OS X so wie sie sind. Es gibt Portierungen von
Bash für Windows, die es ermöglichen die Beispiele unverändert auszuführen.


.. _api_bindings_shell_links:

API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Shell_links.table
