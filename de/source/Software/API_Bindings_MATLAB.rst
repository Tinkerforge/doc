
.. _api_bindings_matlab:

MATLAB/Octave - API Bindings
============================

Die MATLAB/Octave Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen MATLAB/Octave Skripten
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``matlab/Tinkerforge.jar``, eine vorkompilierte Java Bibliothek für MATLAB
* in ``matlab/source/`` den Quelltext für ``Tinkerforge.jar`` für MATLAB
* in ``matlab/examples/`` die MATLAB Beispiele für alle Bricks und Bricklets
* ``octave/Tinkerforge.jar``, eine vorkompilierte Java Bibliothek für Octave
* in ``octave/source/`` den Quelltext für ``Tinkerforge.jar`` für Octave
* in ``octave/examples/`` die Octave Beispiele für alle Bricks und Bricklets

Die MATLAB/Octave Bindings basieren auf den :ref:`Java Bindings
<api_bindings_java>`.


Voraussetzungen
---------------

* MATLAB oder Octave 3.6 oder neuer mit Java 8 Unterstützung


.. _api_bindings_matlab_install:

Installation
------------

Bevor die Bindings mit MATLAB oder Octave benutzt werden können müssen sie
installiert werden.

MATLAB
^^^^^^

Die Java Unterstützung in MATLAB ist normalerweise standardmäßig aktiv. Dies
kann mit folgendem Befehl in MATLAB getestet werden:

.. code-block:: matlab

 version -java

Falls dieser Befehl keine Java Unterstürzung zeigt, dann siehe die MATLAB
Dokumentation darüber wie `Java für MATLAB
<https://www.mathworks.com/help/compiler_sdk/java/configure-your-java-environment.html>`__
eingerichtet werden kann.

Um die Bindings verwenden zu können muss MATLAB die ``Tinkerforge.jar`` Datei
finden können. Diese kann auf verschiedene Art und Weisen erreicht werden.
Die `MATLAB Dokumentation
<https://de.mathworks.com/help/matlab/matlab_external/java-class-path.html>`__
beschreibt alle Art und Weisen.
Das empfohlene Vorgehen ist die Bindings dem Preferences-Ordner hinzuzufügen.

Starte MATLAB und führe folgenden Befehl aus, um den Pfad zum Preferences-Ordner
auszugeben:

.. code-block:: matlab

 prefdir(1)

Preferences-Ordner Beispielpfade:

* Windows: ``C:\Users\<user>\AppData\local\MathWorks\MATLAB\R2016a``
* Linux: ``/home/<user>/.matlab/R2016a``
* macOS: ``/Users/<user>/.matlab/R2016a``

Kopiere die ``Tinkerforge.jar`` Datei vom ``matlab/`` Ordner in den
Preferences-Ordner. Dann muss die ``Tinkerforge.jar`` Datei zu MATLABs
Class Path hinzugefügt werden. Dazu eine Datei namens ``javaclasspath.txt``
im Preferences-Ordner anlegen bzw. bearbeiten und den absoluten Pfad zur
``Tinkerforge.jar`` Datei als neue Zeile hinzufügen. Zum Beispiel:

* Windows: ``C:\Users\<User>\AppData\local\MathWorks\MATLAB\R2016a\Tinkerforge.jar``
* Linux: ``/home/<User>/.matlab/R2016a/Tinkerforge.jar``
* macOS: ``/Users/<User>/.matlab/R2016a/Tinkerforge.jar``

Start MATLAB neu und führe folgenden Befehl aus, er sollte die
``Tinkerforge.jar`` Datei mit auflisten:

.. code-block:: matlab

 javaclasspath

Die Java Bindings können jetzt genutzt werden.

Octave
^^^^^^

Die Verfügbarkeit der Java Unterstützung in Octave hängt von der Octave
Version ab. Bis Version 3.6 einschließlich war die Java Unterstürzung ein
einiges Modul. Ab Version 3.8 ist sie standardmäßiger Teil von Octave.

Unter Linux muss die Java Unterstützung für Octave 3.6 separat installiert
werden::

  sudo apt-get install octave octave-java

Für Windows empfehlen wir die MinGW Variante von Octave. In dieser Variante ist
die Java Unterstützung standardmäßig aktiviert. Eine Anleitung wie Octave für
Windows installiert werden kann findet sich im
`Octave Wiki <https://wiki.octave.org/Octave_for_Microsoft_Windows>`__.

Die Verfügbarkeit der Java Unterstützung kann mit folgendem Befehl in Octave
getestet werden:

.. code-block:: octave

  octave_config_info("features").JAVA

Die Bindings stehen in unserem APT Repository für Debian basierte Linux
Distributionen bereit. Zuerst das :ref:`APT Repository einrichten
<apt_repository_setup>` dann die Bindings installieren::

 sudo apt install octave-tinkerforge

Die Bindings JAR Datei ist hier installiert::

 /usr/share/octave/packages/tinkerforge/tinkerforge.jar

Um die Bindings in Octave verfügbar zu machen muss die Bindings JAR Datei zu
Octaves Class Path hinzugefügt werden werden. Zum Beispiel durch folgenden
Octave Befehl unter Debian basierte Linux Distributionen:

.. code-block:: octave

  javaaddpath("/usr/share/octave/packages/tinkerforge/tinkerforge.jar");

Alternativ muss die ``Tinkerforge.jar`` Datei aus dem ``octave/`` Ordner der
ZIP Datei zu Octaves Class Path hinzugefügt werden werden. Zum Beispiel durch
folgenden Octave Befehl unter Windows:

.. code-block:: octave

  javaaddpath("C:\\Absoluter\\Pfad\\zum\\Octave\\Tinkerforge.jar");

Und durch folgenden Octave Befehl unter Linux:

.. code-block:: octave

  javaaddpath("/Absoluter/Pfad/zum/Octave/Tinkerforge.jar");

Damit diese Änderung dauerhaft ist kann der Befehlt unter Linux in folgenden
Datei eingetragen werden::

 ~/.octaverc

Falls diese Datei noch nicht existiert kann sie einfach angelegt werden.
Nach Änderungen an dieser Datei muss Octave neugestartet werden.


Test eines Beispiels
--------------------

Um ein MATLAB/Octave Beispiel testen zu können, müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

MATLAB
^^^^^^

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu die ``matlab_example_configuration.m`` Datei aus dem
``matlab/examples/brick/stepper/`` Ordner in MATLAB öffnen.

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: matlab

  HOST = 'localhost';
  PORT = 4223;
  UID = 'XXYYZZ'; % Change XXYYZZ to the UID of your Stepper Brick

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können.

Octave
^^^^^^

Als Beispiel werden wir das Stepper Brick Konfigurationsbeispiel ausführen.
Dazu die ``octave_example_configuration.m`` Datei aus dem
``octave/examples/brick/stepper/`` Ordner in Octave öffnen.

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: octave

  HOST = "localhost";
  PORT = 4223;
  UID = "XXYYZZ"; % Change XXYYZZ to the UID of your Stepper Brick

Dann ist auch schon alles bereit, um dieses Beispiel testen zu können.


.. _api_bindings_matlab_octave_function_vs_script_files:

Function vs Script Dateien
""""""""""""""""""""""""""

Die Octave Beispiel sind `Function Dateien
<https://www.gnu.org/software/octave/doc/interpreter/Function-Files.html>`__.
Um sie direkt von der Kommandozeile ausführen zu können, müssen sie zu
`Script Dateien
<https://www.gnu.org/software/octave/doc/interpreter/Script-Files.html>`__
erweitert werden. Dazu einfach am Ende des Beispiels die Beispiel Funktion
aufrufen:

.. code-block:: octave

  function octave_example_configuration()
      % ...
  end

  octave_example_configuration(); % Add this line

.. _api_bindings_matlab_known_issues:

Bekannte Probleme
-----------------

**Callbacks funktioneren nicht in Octave 3.8 oder neuer** (gelöst)

In Bindings Version 2.0.13 oder älter in Octave 3.8 funktioniert die Invoke
Funktion nicht und wirft eine ``java.lang.UnsatisfiedLinkError`` Exception.
Die Invoke Funktion erlaubt es von Java aus Octave Funktionen aufzurufen.
Dies wird von den Bindings für Callbacks benutzt. Dies bedeutet, dass in
Octave 3.8 keine Callbacks verwendet werden können. Eine `Diskussion
<http://octave.1599824.n4.nabble.com/Problem-with-invoke-call-from-Java-td4664495.html>`__
auf der Octave Mailing Liste hat zu keinem Erfolg geführt.

Das Problem ist sein Bindings Version 2.0.14 behoben.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_MATLAB_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MATLAB>
   Bricks <Bricks_MATLAB>
   Bricks (Abgekündigt) <Bricks_MATLAB_Discontinued>
   Bricklets <Bricklets_MATLAB>
   Bricklets (Abgekündigt) <Bricklets_MATLAB_Discontinued>
