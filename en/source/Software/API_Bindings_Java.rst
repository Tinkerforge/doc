
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-java">Software</a> / Java - API Bindings

.. _api_bindings_java:

Java - API Bindings
===================

**Requirements**: Java 1.5 or newer

.. note::
 There is an extra section for :ref:`Java and Android <api_bindings_java_android>`.

The Java bindings (:ref:`download <downloads_bindings_examples>`) consist of a
library (.jar) for all Tinkerforge Bricks and
Bricklets (``Tinkerforge.jar``), the source of the JAR (in ``source/``) and all
available Java examples (in ``examples/``).

The library is also available from the `Central Maven Repository
<http://search.maven.org/#search%7Cga%7C1%7Ctinkerforge>`__.


.. _api_bindings_java_install:

Installation
------------

TODO

Testing an Example
------------------

As an example lets compile the configuration example of the Stepper Brick.

Create a new folder and copy the ``Tinkerforge.jar`` and the
``examples/Brick/Stepper/ExampleConfiguration.java`` into this folder::

 example_folder/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In this folder we can now call the Java compiler with the following
parameters (1. Windows and 2. Linux/Mac OS X)::

 1.) javac -cp Tinkerforge.jar;. ExampleConfiguration.java
 2.) javac -cp Tinkerforge.jar:. ExampleConfiguration.java

and run it with the following parameters (1. Windows and 2. Linux/Mac OS X)::

 1.) java -cp Tinkerforge.jar;. ExampleConfiguration
 2.) java -cp Tinkerforge.jar:. ExampleConfiguration

.. note::
 The difference between 1. and 2. is semicolon vs colon

Or, alternatively add the JAR and the Example in an Java development environment
of your choice (such as Eclipse or NetBeans).


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Java_links.table
