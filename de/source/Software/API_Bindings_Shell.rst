
.. _api_bindings_shell:

Shell - API Bindings
====================

Die Shell Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Shell Skripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``tinkerforge``, ein Python Skript, das als Shell Befehl agiert
* ``tinkerforge-bash-completion.sh``, ein Bash Completion Skript
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Shell Bindings basieren auf den :ref:`Python Bindings <api_bindings_python>`.

Voraussetzungen
---------------

* Python 3.4 oder neuer

.. _api_bindings_shell_install:

Installation
------------

Die Shell Bindings können auf zwei Weisen installiert werden:
von unserem :ref:`APT Repository <api_bindings_shell_install_apt>` für Debian
basierte Linux Distributionen oder durch
:ref:`händisches <api_bindings_shell_install_manual>` Kopieren der Dateien an
die richtige Stelle. Die Bindings können aber auch ohne Installation genutzt werden.

.. _api_bindings_shell_install_apt:

Vom APT Repository
^^^^^^^^^^^^^^^^^^

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit. Zuerst das :ref:`APT Repository einrichten
<apt_repository_setup>` dann die Bindings installieren::

 sudo apt install tinkerforge-shell

Dann ist auch schon alles bereit, um Beispiele testen zu können. Das Debian
Package beinhaltet keine Beispiele. Diese sind als Teil der :ref:`ZIP Datei
<downloads_bindings_examples>` der Bindings verfügbar.

.. _api_bindings_shell_install_manual:

Händische Installation
^^^^^^^^^^^^^^^^^^^^^^

Zur händischen Installation die ``tinkerforge`` Datei in einen
Ordner kopiert werden, der sich im PATH befindet. Das kann unter Linux und macOS
folgender Ordner sein::

 /usr/local/bin/

Unter Windows bietet sich der ``Scripts/`` Ordner der Python Installation an::

 C:\Python\Scripts\

Damit die Bindings unter Windows direkt aufgerufen werden können muss noch eine
``tinkerforge.bat`` Datei im ``Scripts/`` Ordner mit folgendem Inhalt angelegt
werden::

 @"C:\Python\python.exe" "C:\Python\Scripts\tinkerforge" %*

Wenn sich die Python Installation nicht im ``C:\Python\`` Ordner befindet,
dann ist natürlich der Inhalt der ``tinkerforge.bat`` Datei entsprechend
abzuändern.

Bash Completion
^^^^^^^^^^^^^^^

Wird Bash als Shell verwendet so kann auch das Bash Completion Skript
``tinkerforge-bash-completion.sh`` installiert werden. Falls die Bindings über
unser APT Repository installiert wurden, dann isr das Bash Completion Skript
schon korrekt installiert und die folgenden Schritt können übersprungen werden.

Zur Installation die ``tinkerforge-bash-completion.sh`` Datei in den
``/etc/bash_completion.d/`` Ordner kopieren und dann die Bash Completions mit
folgendem Befehl neu laden::

 . /etc/bash_completion

Die Bash Completion für ``tinkerforge`` kann Optionen, UIDs, Brick und Bricklet
Namen sowie Funktions- und Callback-Namen vervollständigen.

Test eines Beispiels
--------------------

Um ein Shell Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Alle Beispiele sind für typische Unix Shells wie z.B. Bash gemacht. Sie
funktionieren auf Linux und macOS so wie sie sind. Es gibt Portierungen von
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

  uid=XXYYZZ # Change XXYYZZ to the UID of your Stepper Brick

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können::

 ./example-configuration.sh

.. _api_bindings_shell_links:

API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Shell_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Shell>
   Bricks <Bricks_Shell>
   Bricks (Abgekündigt) <Bricks_Shell_Discontinued>
   Bricklets <Bricklets_Shell>
   Bricklets (Abgekündigt) <Bricklets_Shell_Discontinued>
