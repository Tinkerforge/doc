
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-shell">Software</a> / Shell - API Bindings

.. _api_bindings_shell:

Shell - API Bindings
====================

Die Shell Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Shell Scripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``tinkerforge``, ein Python Script, das als Shell Befehl agiert
* ``tinkerforge-bash-completion.sh``, ein Bash Completion Script
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Shell Bindings basieren auf den :ref:`Python Bindings <api_bindings_python>`.


Voraussetzungen
---------------

* Python 2.5 oder neuer mit ``argparse`` Modul, Python 3 wird auch unterstützt


.. _api_bindings_shell_install:

Installation
------------

Die Shell Bindings können installiert werden, können aber auch ohne Installation
verwendet werden.

Zur Installation wird die ``tinkerforge`` Datei in einen Ordner kopiert der
sich im PATH befindet. Das kann unter Linux und Mac OS X folgender Ordner sein::

 /usr/local/bin/

Unter Windows bietet sich der ``Scripts/`` Ordner der Python Installation an::

 C:\Python27\Scripts\

Damit die Bindings unter Windows direkt aufgerufen werden können muss noch eine
``tinkerforge.bat`` Datei im ``Scripts/`` Ordner mit folgendem Inhalt angelegt
werden::

 @"C:\Python27\python.exe" "C:\Python27\Scripts\tinkerforge"

Wenn sich die Python Installation nicht im ``C:\Python27\`` Ordner befindet,
dann ist natürlich der Inhalt der ``tinkerforge.bat`` Datei entsprechend
abzuändern.

Bash Completion
^^^^^^^^^^^^^^^

Wird Bash als Shell verwendet so kann auch das Bash Completion Script
``tinkerforge-bash-completion.sh`` installiert werden. Dazu die
``tinkerforge-bash-completion.sh`` Datei in den ``/etc/bash_completion.d/``
Ordner kopieren und dann die Bash Completions mit folgendem Befehl neu laden::

 . /etc/bash_completion

Die Bash Completion für ``tinkerforge`` kann Optionen, UIDs, Brick und Bricklet
Namen sowie Funktions- und Callback-Namen vervollständigen.


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

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
getestet. Dafür muss zuerst die ``example-configuration.sh`` Datei aus dem
``examples/brick/stepper/`` Ordner in einen neuen Ordner kopiert werden::

 example_project/
  -> example-configuration.sh

Wenn die Bindings **nicht** installiert wurden, dann muss die ``tinkerforge``
Datei in den ``example_project/`` Ordner kopiert werden::

 example_project/
  -> tinkerforge
  -> example-configuration.sh

Damit das Beispiel die nicht installierte ``tinkerforge`` Datei finden kann
muss jedes Auftreten des ``tinkerforge`` Befehls in der
``example-configuration.sh`` Datei durch ``./tinkerforge`` ersetzt werden.

Am Anfang des Beispiels steht ein Kommentar der darauf hinweist die
Netzwerkadresse mittels ``--host`` und ``--port`` Option anzugeben, wenn sie
von ``localhost:4223`` abweicht. Wenn der Stepper Brick lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig.

.. code-block:: bash

  # connects to localhost:4223 by default, use --host and --port to change it

Um z.B. zu einen Stepper Brick zu steuern, der an Host ``foobar`` und Port 5678
erreichbar ist dann muss das Beispiel so abgewandelt werden: Jedes Auftreten
des ``tinkerforge`` Befehls muss durch diesen Ausdruck ersetzt werden:

.. code-block:: bash

  tinkerforge --host foobar --port 5678

Als ``uid`` muss die UID des angeschlossen Stepper Bricks angegeben werden,
diese kann über den Brick Viewer ermittelt werden:

.. code-block:: bash

  # change to your UID
  uid=XYZ

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 ./example-configuration.sh


.. _api_bindings_shell_links:

API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Shell_links.table
