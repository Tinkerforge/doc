
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-matlab">Software</a> / MATLAB/Octave - API Bindings

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

* MATLAB oder Octave 3.6 mit Java Unterstützung


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

Zur Installation der Bindings muss die ``Tinkerforge.jar`` Datei aus dem
``matlab/`` Ordner in den MATLAB Programmordner kopiert werden. Unter Windows
ist dieser für MATLAB R2014a typischerweise hier::

 C:\Programme\MATLAB\R2014a

Unter Linux ist es hier::

 /usr/local/matlab/r2014a

Unter Mac OS X ist es hier::

 /Applications/MATLAB_R2014a.app

Dann muss die neue Java Bibliothek noch zu MATLABs Class Path hinzugefügt
werden. Dazu muss der folgenden Datei bearbeitet::

 <MATLAB Programmordner>/toolbox/local/classpath.txt

und diese Zeile am Ende dieser Datei angehängt werden::

 $matlabroot/Tinkerforge.jar

Nach einem Neustart von MATLAB stehen sie Bindings dann zur Verfügung.

Octave
^^^^^^

Die Verfügbarkeit der Java Unterstützung in Octave hängt von der Octave
Version ab. Bis Version 3.6 einschließlich war die Java Unterstürzung ein
einiges Modul. Ab Version 3.8 ist sie standardmäßiger Teil von Octave.

Allerdings funktionieren Callbacks nicht mit der Java Unterstützung in Octave
3.8, siehe dazu den Abschnitt über :ref:`bekannte Probleme
<api_bindings_matlab_known_problems>`. Wir empfehlen daher derzeit Octave 3.6.

Unter Linux muss die Java Unterstützung für Octave 3.6 separat installiert
werden::

  sudo apt-get install octave octave-java

Für Windows empfehlen wir die MinGW Variante von Octave. In dieser Variante ist
die Java Unterstützung standardmäßig aktiviert. Eine Anleitung wie Octave für
Windows installiert werden kann findet sich im
`Octave Wiki <http://wiki.octave.org/Octave_for_Microsoft_Windows>`__.

Die Verfügbarkeit der Java Unterstützung kann mit folgendem Befehl in Octave
getestet werden:

.. code-block:: octave

  octave_config_info("features").JAVA

Um die Bindings in Octave verfügbar zu machen muss die ``Tinkerforge.jar`` Datei
aus dem ``octave/`` Ordner zu Octaves Class Path hinzugefügt werden werden. Zum
Beispiel durch folgenden Octave Befehl unter Windows:

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

Um ein MATLAB/Octave Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
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
  UID = 'XYZ'; % Change to your UID

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
  UID = "XYZ"; % Change to your UID

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

.. _api_bindings_matlab_known_problems:

Bekannte Probleme
-----------------

In Octave 3.8 funktioniert die Invoke Funktion nicht und wirft eine
``java.lang.UnsatisfiedLinkError`` Exception. Die Invoke Funktion erlaubt es
von Java aus Octave Funktionen aufzurufen. Dies wird von den Bindings für
Callbacks benutzt. Dies bedeutet, dass in Octave 3.8 keine Callbacks verwendet
werden können. Eine `Diskussion
<http://octave.1599824.n4.nabble.com/Problem-with-invoke-call-from-Java-td4664495.html>`__
auf der Octave Mailing Liste hat noch zu keinem Erfolg geführt. Daher
empfehlen wir derzeit Octave 3.6, in dieser Version tritt das Problem nicht auf
und die Bindings funktionieren in vollem Umfang.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_MATLAB_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MATLAB>
   Bricks <Bricks_MATLAB>
   Bricklets <Bricklets_MATLAB>
