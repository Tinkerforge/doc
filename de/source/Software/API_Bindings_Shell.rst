
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - API Bindings

.. _api_bindings_shell:

Shell - API Bindings
====================

**Voraussetzungen**: Python 2.5 oder neuer, Python 3 wird auch unterstützt

Die Shell Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen
aus einem Python Script zur Interaktion mit alle
Tinkerforge Bricks und Bricklets (``tinkerforge``), einem passendes Bash
Completion Script (``tinkerforge-bash-completion.sh``) und allen verfügbaren
Shell Beispielen (in ``examples/``).

Für funktionierende Bash Completion muss sich das ``tinkerforge`` Script im
``PATH`` befinden und das Bash Completion Script ``tinkerforge-bash-completion.sh``
in ``/etc/bash_completion.d/``.


Test eines Beispiels
--------------------

Alle Beispiele sind für typische Unix Shells wie z.B. Bash gemacht. Sie
funktionieren auf Linux und Mac OS X so wie sie sind. Es gibt Portierungen von
Bash für Windows, die es ermöglichen die Beispiele unverändert auszuführen.

Wenn die Beispiele von der Windows Eingabeaufforderung ``cmd.exe`` verwendet
werden sollen, dann muss die Shebang Zeile ``#!/bin/sh`` entfernt werden und
allen Zeilen die mit ``tinkerforge`` beginnen muss ein ``python``
vorangestellt werden. So dass aus::

 #!/bin/sh
 tinkerforge enumerate

dies wird::

 python tinkerforge enumerate

Als letzten Schritt muss dann noch die Dateiendung von ``.sh`` zu ``.bat`` oder
``.cmd`` geändert werden.


Weitere Beispiele und Projekte
------------------------------

Die kleinen Beispiele aus der ZIP Datei der Bindings sind auch in der API
Dokumentation der :ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` zu finden

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. FIXME: add a list with direct links here
