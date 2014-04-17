
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / MATLAB/Octave - API Bindings

.. _api_bindings_matlab:

MATLAB/Octave - API Bindings
============================

**Voraussetzungen**: MATLAB oder Octave mit Java Unterstützung

Die MATLAB Bindings (:ref:`download <downloads_bindings_examples>`) bestehen
aus zwei .jar Dateien mit den Bindings für alle Tinkerforge Bricks und Bricklets,
ein .jar for MATLAB (``matlab/Tinkerforge.jar``) und eines für Octave
(``octave/Tinkerforge.jar``). Der Quelltext des MATLAB .jar (``matlab/source/``)
und des Octave .jar (``octave/source/``) und alle verfügbaren MATLAB
(``matlab/examples/``) und Octave Beispiele (``octave/examples/``) sind
ebenfalls enthalten.


Testing an Example
------------------

MATLAB
^^^^^^

Als erstes ist sicherzustellen, dass die Java Unterstützung in MATLAB richtig
konfiguriert ist. Derzeit wird nur Java 1.6 von MATLAB unterstützt. Falls also
eine andere Java Version installiert ist kann es sein, dass Java in MATLAB nicht
richtig funktioniert.

Normalerweise ist die Java Unterstützung in MATLAB standardmäßig aktiviert.
Dies kann mit dem folgenden Befehl in der MATLAB Konsole kontrolliert werden::

 version -java

Als nächstes muss das ``Tinkerforge.jar`` dem ``javaclasspath`` in MATLAB
hinzugefügt werden. Dazu einfach die ``Tinkerforge.jar`` für MATLAB in das
Installationsverzeichnis von MATLAB kopieren und dann die folgende Zeile::

 $matlabroot/Tinkerforge.jar

am Ende dieser Datei einfügen::

 <MATLAB-Installationverzeichnis>/toolbox/local/classpath.txt

Dies gilt gleichermaßen für MATLAB unter Windows und Linux.

Jetzt können alle MATLAB Beispiel einfach von der MATLAB Konsole aus
ausprobiert werden.


Octave
^^^^^^

Auch hier muss zuerst sichergestellt werden, dass die Java Unterstützung
aktiviert ist. Unter Debian Linux kann einfach das ``octave`` und das
``octave-java`` Package installiert werden::

  sudo apt-get install octave octave-java

Stelle sicher, dass mindestens ``octave-java`` 1.2.8-6 installiert ist. Dann
sollte deie Java Unterstützung in Octave korrekt konfiguriert sein. Als
nächstes muss folgende Zeile:

.. code-block:: none

 javaaddpath("<path-to-bindings>/Tinkerforge.jar");

am Ende dieser Datei einfügen werden::

 ~/.octaverc

Falls diese Datei noch nicht existiert kann sie einfach angelegt werden.
Nach der Änderung dieser Datei muss Octave neugestartet werden, falls es lief.
Jetzt können alle Octave Beispiel einfach von der Octave Konsole aus
ausprobiert werden.

Um die Bindings auf Windows zu verwenden wird die MinGW Variante von Octave
benötigt. In dieser Variante ist die Java Unterstützung standardmäßig aktiviert.
Eine Anleitung wie man Octave für Windows installiert findet sich im
`Octave Wiki <http://wiki.octave.org/Octave_for_Microsoft_Windows>`__.

Wenn die Installation für Windows abgeschlossen ist muss das ``Tinkerforge.jar``
noch Octave bekannt gemacht werden. Dies kann mit dem folgenden Befehl in der
MATLAB Octave getan werden:

.. code-block:: none

 javaaddpath("<path-to-bindings>/Tinkerforge.jar");

Jetzt können alle Octave Beispiel einfach von der Octave Konsole aus auf
Windows ausprobiert werden.


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet.

.. include:: API_Bindings_MATLAB_links.table

Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.
