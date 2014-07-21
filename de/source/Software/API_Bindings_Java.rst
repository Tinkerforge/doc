
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software-java">Software</a> / Java - API Bindings

.. _api_bindings_java:

Java - API Bindings
===================

**Voraussetzungen**: Java 1.5 oder neuer

.. note::
 Es gibt einen extra Abschnitt für :ref:`Java und Android <api_bindings_java_android>`.

Die Java Bindings (:ref:`Download <downloads_bindings_examples>`) bestehen aus
einer Bibliothek (.jar) für alle Tinkerforge
Bricks und Bricklets (``Tinkerforge.jar``), dem Quelltext des JAR (in
``source/``) und allen verfügbaren Java Beispielen (in ``examples/``).

Die Bibliothek steht auch im `Central Maven Repository
<http://search.maven.org/#search%7Cga%7C1%7Ctinkerforge>`__ zur Verfügung.


.. _api_bindings_java_install:

Installation
------------

TODO


Test eines Beispiels
--------------------

Als Beispiel wird im Folgenden das Konfigurationsbeispiel des Stepper Bricks
kompiliert.

Dafür müssen zuerst die ``Tinkerforge.jar`` und die
``examples/Brick/Stepper/ExampleConfiguration.java`` Datei in einen Ordern
kopiert werden::

 example_folder/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In diesem Ordner kann jetzt der Java Compiler mit den folgenden Parametern
aufgerufen werden (1. Windows und 2. Linux/Mac OS X)::

 1.) javac -cp Tinkerforge.jar;. ExampleConfiguration.java
 2.) javac -cp Tinkerforge.jar:. ExampleConfiguration.java

Und ausgeführt wird es mit dem folgenden Befehl (1. Windows und 2. Linux/Mac OS X)::

 1.) java -cp Tinkerforge.jar;. ExampleConfiguration
 2.) java -cp Tinkerforge.jar:. ExampleConfiguration

.. note::
  Der Unterschied zwischen 1. und 2. ist Semikolon vs Doppelpunkt

Alternativ können die Beispiele auch in einer Java Entwicklungsumgebung deiner
Wahl verwendet werden (wie Eclipse oder NetBeans).


API Dokumentation und Beispiele
-------------------------------

Links zur API Dokumentation der IP Connection, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Starterkits <index_kits>`.

.. include:: API_Bindings_Java_links.table
