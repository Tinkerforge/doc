
.. _api_bindings_matlab:

MATLAB/Octave - API Bindings
============================

The MATLAB/Octave bindings allow you to control :ref:`Bricks <primer_bricks>`
and :ref:`Bricklets <primer_bricklets>` from your MATLAB/Octave scripts. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``matlab/Tinkerforge.jar``, a precompiled Java library for MATLAB
* in ``matlab/source/`` the source code of ``Tinkerforge.jar`` for MATLAB
* in ``matlab/examples/`` the MATLAB examples for every Brick and Bricklet
* ``octave/Tinkerforge.jar``, a precompiled Java library for Octave
* in ``octave/source/`` the source code of ``Tinkerforge.jar`` for Octave
* in ``octave/examples/`` the Octave examples for every Brick and Bricklet

The MATLAB/Octave bindings are based on the :ref:`Java bindings
<api_bindings_java>`.


Requirements
------------

* MATLAB or Octave 3.6 with Java support


.. _api_bindings_matlab_install:

Installation
------------

Before you and use the bindings with MATLAB or Octave you have to install them.

MATLAB
^^^^^^

The Java support in MATLAB is typically enabled by default. You can test this
with the following command in MATLAB:

.. code-block:: matlab

 version -java

If this command doesn't show Java support then see the MATLAB documentation
about how to configure `Java for MATLAB
<http://www.mathworks.com/help/compiler_sdk/java/configure-your-java-environment.html>`__.

To use the bindings MATLAB needs to know where to find the ``Tinkerforge.jar``
file. There are several ways to archive this, see the `MATLAB documentation
<http://www.mathworks.com/help/matlab/matlab_external/bringing-java-classes-and-methods-into-matlab-workspace.html>`__
for more details on all of them.
The recommended way is to the add the bindings to the preferences folder.

Start MATLAB and run the following command to get the path of the preferences
folder:

.. code-block:: matlab

 prefdir(1)

Preferences folder path examples:

* Windows: ``C:\Users\<user>\AppData\local\MathWorks\MATLAB\R2016a``
* Linux: ``/home/<user>/.matlab/R2016a``
* Mac OS X: ``/Users/<user>/.matlab/R2016a``

Copy the ``Tinkerforge.jar`` file from the ``matlab/`` folder to the preferences
folder. Then the ``Tinkerforge.jar`` file has to be added to MATLAB's class path.
Edit or create a file named ``javaclasspath.txt`` in the preferences folder
and add the absolute path to the ``Tinkerforge.jar`` file as a new line to it.
For example:

* Windows: ``C:\Users\<user>\AppData\local\MathWorks\MATLAB\R2016a\Tinkerforge.jar``
* Linux: ``/home/<user>/.matlab/R2016a/Tinkerforge.jar``
* Mac OS X: ``/Users/<user>/.matlab/R2016a/Tinkerforge.jar``

Restart MATLAB and run the following command, it should list the
``Tinkerforge.jar`` file:

.. code-block:: matlab

 javaclasspath

The bindings are now ready to use.

Octave
^^^^^^

If Java support is available in Octave depends on the Octave version. Until
version 3.6 (inclusive) Java support was in a separate module. Since version
3.8 it is available by default.

But in Octave 3.8 callbacks don't work, see the :ref:`known problems
<api_bindings_matlab_known_problems>` section. We recommend Octave 3.6 for now.

On Linux you have to install an extra package for the Java support in
Octave 3.6::

  sudo apt-get install octave octave-java

For Windows we recommend the MinGW build of Octave, because it comes with Java
support by default. The `Octave Wiki
<http://wiki.octave.org/Octave_for_Microsoft_Windows>`__ has a guide about
how to set up Octave for Windows.

You can test if Java support is available with the following command in Octave:

.. code-block:: octave

  octave_config_info("features").JAVA

To make the bindings available in Octave the ``Tinkerforge.jar`` from the
``octave/`` folder has to be added to Octave's class path. This can be done with
the following Octave command on Windows:

.. code-block:: octave

  javaaddpath("C:\\Absolute\\path\\to\\Octave\\Tinkerforge.jar");

Or by this Octave command on Linux:

.. code-block:: octave

  javaaddpath("/Absolute/path/to/Octave/Tinkerforge.jar");

To make this change persistent you can add the command to the following file
on Linux::

 ~/.octaverc

If this file didn't exist yet you can just create it. Octave has to be restarted
after changing this file.


Testing an Example
------------------

To test a MATLAB/Octave example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

MATLAB
^^^^^^

As an example we will run the Stepper Brick configuration example. To do this
open the ``matlab_example_configuration.m`` file from the
``matlab/examples/brick/stepper/`` folder in MATLAB.

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: matlab

  HOST = 'localhost';
  PORT = 4223;
  UID = 'XYZ'; % Change to your UID

Now you're ready to test the examples.

Octave
^^^^^^

As an example we will run the Stepper Brick configuration example. To do this
open the ``octave_example_configuration.m`` file from the
``octave/examples/brick/stepper/`` folder in Octave.

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: octave

  HOST = "localhost";
  PORT = 4223;
  UID = "XYZ"; % Change to your UID

Now you're ready to test the examples.


.. _api_bindings_matlab_octave_function_vs_script_files:

Function vs Script Files
""""""""""""""""""""""""

The Octave examples are `function files
<https://www.gnu.org/software/octave/doc/interpreter/Function-Files.html>`__.
To execute them directly from a terminal, they have to be extended to
`script files
<https://www.gnu.org/software/octave/doc/interpreter/Script-Files.html>`__.
Just add a call to the example function at the end of the example:

.. code-block:: octave

  function octave_example_configuration()
      % ...
  end

  octave_example_configuration(); % Add this line


.. _api_bindings_matlab_known_problems:

Known Problems
--------------

In bindings version 2.0.13 or older in Octave 3.8 the Invoke function throws
an ``java.lang.UnsatisfiedLinkError`` exception. The Invoke function is required
to call Octave functions from Java. The bindings use this for callbacks.
This means that you cannot use callbacks in Octave 3.8. A `discussion
<http://octave.1599824.n4.nabble.com/Problem-with-invoke-call-from-Java-td4664495.html>`__
on the Octave mailing list didn't come to a conclusion of fix for this yet.
Because of this we recommend Octave 3.6 for now. This version is not affected
by this problem and the bindings works without any problems.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_MATLAB_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MATLAB>
   Bricks <Bricks_MATLAB>
   Bricks (Discontinued) <Bricks_MATLAB_Discontinued>
   Bricklets <Bricklets_MATLAB>
   Bricklets (Discontinued) <Bricklets_MATLAB_Discontinued>
