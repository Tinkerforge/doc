
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - API Bindings

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


Test eines Beispiels
--------------------

Alle Beispiele sind für typische Unix Shells wie z.B. Bash gemacht. Sie
funktionieren auf Linux und Mac OS X so wie sie sind. Es gibt Portierungen von
Bash für Windows, die es ermöglichen die Beispiele unverändert auszuführen.


.. _api_bindings_shell_links:

API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_Shell_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
