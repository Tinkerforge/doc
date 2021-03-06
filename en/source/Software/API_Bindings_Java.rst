
.. _api_bindings_java:

Java - API Bindings
===================

.. note::
 There is an extra section for :ref:`Java and Android <api_bindings_java_android>`.

The Java bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Java programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.jar``, a precompiled Java library
* in ``source/`` the source code of ``Tinkerforge.jar``
* in ``examples/`` examples for every Brick and Bricklet

The Java library has no external dependencies.


Requirements
------------

* Java JDK 8 or newer


.. _api_bindings_java_install:

Installation
------------

If and how the Java bindings have to be installed depends heavily on how you are
going to use them. If you are just calling the Java compiler from the command
line then you can just put the ``Tinkerforge.jar`` file into the same folder
as the Java code of your program and include it in the class path.

How the bindings can be used in a certain IDE depends on the specific IDE and
will be explained in the documentation of the IDE.

.. _api_bindings_java_install_apt:

From APT Repository
^^^^^^^^^^^^^^^^^^^

The bindings are available in our APT repository for Debian based Linux
distributions (in this case you don't even need the ZIP file for the bindings).
Follow the :ref:`setup guide <apt_repository_setup>` then install the bindings::

 sudo apt install libtinkerforge-java

The bindings JAR file is installed to this location::

 /usr/share/java/tinkerforge.jar

The Debian package does not include the examples. Those are available as part
of the bindings :ref:`ZIP file <downloads_bindings_examples>`.

.. _api_bindings_java_install_maven:

From Maven Central Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The bindings are available from the `Maven Central Repository
<https://search.maven.org/search?q=a:tinkerforge>`__. This allows
to use them directly in Maven project. Just add ``tinkerforge`` as a dependency
to your Maven project file (``pom.xml``). The placeholder ``X.Y.Z`` represents
the specific version of the bindings to be used, e.g. ``2.1.1``:

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

The Maven package does not include the examples. Those are available as part of
the bindings :ref:`ZIP file <downloads_bindings_examples>`.


Testing an Example
------------------

To test a Java example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's compile the configuration example for the Stepper Brick.
Copy the ``Tinkerforge.jar`` file and the ``ExampleConfiguration.java`` file
from ``examples/Brick/Stepper/`` into a new folder::

 example_project/
  -> Tinkerforge.jar
  -> ExampleConfiguration.java

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: java

  private static final String HOST = "localhost";
  private static final int PORT = 4223;
  private static final String UID = "XXYYZZ"; // Change XXYYZZ to the UID of your Stepper Brick

Now we can execute the Java compiler in the ``example_project/`` folder like
this on Windows (replace ``;`` in class path with ``:`` on Linux and macOS)::

 javac -cp Tinkerforge.jar;. ExampleConfiguration.java

and run it with the following parameters on Windows (replace ``;`` in
class path with ``:`` on Linux and macOS again)::

 java -cp Tinkerforge.jar;. ExampleConfiguration

Alternatively you can use the Java library and example in an Java IDE of your
choice such as Eclipse or NetBeans.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_Java_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Java>
   Bricks <Bricks_Java>
   Bricks (Discontinued) <Bricks_Java_Discontinued>
   Bricklets <Bricklets_Java>
   Bricklets (Discontinued) <Bricklets_Java_Discontinued>
