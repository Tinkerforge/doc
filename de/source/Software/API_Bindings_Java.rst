
.. _api_bindings_java:

Java - API Bindings
===================

.. note::
 Es gibt einen extra Abschnitt für :ref:`Java und Android <api_bindings_java_android>`.

Die Java Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` aus selbst erstellen Java Programmen
heraus zu steuern. Die :ref:`ZIP Datei <downloads_bindings_examples>` für
die Bindings beinhaltet:

* ``Tinkerforge.jar``, eine vorkompilierte Java Bibliothek
* in ``source/`` den Quelltext für ``Tinkerforge.jar``
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

Die Java Bibliothek hat keine weiteren Abhängigkeiten.


Voraussetzungen
---------------

* Java JDK 8 oder neuer


.. _api_bindings_java_install:

Installation
------------

Ob und wie die Java Bindings installiert werden müssen hängt stark davon ab wie
sie benutzt werden sollen. Wenn der Java Compiler direkt von der Kommandozeile
aufgerufen wird genügt es die ``Tinkerforge.jar`` Datei im gleichen Verzeichnis
wie den Java Quelltext des Programms abzulegen und sie im Class Path mit anzugeben.

Wie die Bindings in einer bestimmten IDE zu verwenden sind hängt von der IDE ab
und wird in der Dokumentation der jeweiligen IDE erklärt.

Maven
^^^^^

Die Bindings steht auch im `Central Maven Repository
<https://search.maven.org/search?q=a:tinkerforge>`__ zur Verfügung.
Dadurch können sie direkt in Maven Projekte eingebunden werden. Dazu einfach
``tinkerforge`` als Abhängigkeit in die Maven Projektdatei (``pom.xml``)
aufnehmen. Der Platzhalter ``X.Y.Z`` steht dabei für die zu verwendende Version
der Bindings, z.B. ``2.1.1``:

.. code-block:: xml

  <project>
    ...
    <dependencies>
      ...
      <dependency>
        <groupId>com.tinkerforge</groupId>
        <artifactId>tinkerforge</artifactId>
        <version>X.Y.Z</version>
      </dependency>
      ...
    </dependencies>
    ...
  </project>

Das Maven Package beinhaltet keine Beispiele. Diese sind als Teil der
:ref:`ZIP Datei <downloads_bindings_examples>` der Bindings verfügbar.


Test eines Beispiels
--------------------

Um ein Java Beispiel testen zu können müssen zuerst :ref:`Brick Daemon
<brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
Bindings. Brick Viewer kann sich mit Brick Daemon verbinden und gibt
Informationen über die angeschlossenen Bricks und Bricklets aus.

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
kompiliert. Dafür müssen zuerst die ``Tinkerforge.jar`` Datei und die
``ExampleConfiguration.java`` Datei aus dem ``examples/Brick/Stepper/`` in
einen neuen Ordern kopiert werden::

 example_project/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

Am Anfang des Beispiels ist mit ``HOST`` und ``PORT`` angegeben unter welcher
Netzwerkadresse der Stepper Brick zu erreichen ist. Ist er lokal per USB
angeschlossen dann ist ``localhost`` und 4223 richtig. Als ``UID`` muss die
UID des angeschlossen Stepper Bricks angegeben werden, diese kann über den
Brick Viewer ermittelt werden:

.. code-block:: java

  private static final String HOST = "localhost";
  private static final int PORT = 4223;
  private static final String UID = "XXYYZZ"; // Change XXYYZZ to the UID of your Stepper Brick

Im ``example_project/`` Ordner kann jetzt der Java Compiler mit den folgenden
Parametern auf Windows aufgerufen werden (für Linux und macOS das ``;`` im
Class Path durch ``:`` ersetzen)::

 javac -cp Tinkerforge.jar;. ExampleConfiguration.java

Und ausgeführt wird es mit dem folgenden Befehl (für Linux und macOS wieder
das ``;`` im Class Path durch ``:`` ersetzen)::

 java -cp Tinkerforge.jar;. ExampleConfiguration

Alternativ können die Beispiele auch in einer Java IDE deiner Wahl verwendet
werden, wie z.B. Eclipse oder NetBeans.


API Referenz und Beispiele
--------------------------

Links zur API Referenz der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_Java_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Java>
   Bricks <Bricks_Java>
   Bricks (Abgekündigt) <Bricks_Java_Discontinued>
   Bricklets <Bricklets_Java>
   Bricklets (Abgekündigt) <Bricklets_Java_Discontinued>
