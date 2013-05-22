
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../Software.html">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C# - API Bindings

.. _api_bindings_csharp:

C# - API Bindings
=================

The C# bindings (:ref:`download <downloads_bindings_examples>`) consist of a
library (.dll) for all Tinkerforge Bricks and Bricklets
(``Tinkerforge.dll``), the source of the DLL (in ``source/``) and all available
C# examples (in ``examples/``).

The library has been compiled with::

 gmcs /optimize /target:library /out:Tinkerforge.dll source/Tinkerforge/*.cs

It can be used without any further extensions.


Testing an Example
------------------

As an example lets compile the configuration example of the Stepper Brick.

For this we create a folder and copy the ``Tinkerforge.dll`` and the
``examples/Brick/Stepper/ExampleConfiguration.cs`` into this folder::

 example_folder/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In this folder we can now call the C# compiler with the following parameters
(1. Windows and 2. Linux/Mac OS X (Mono))::

 1.) csc.exe       /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs
 2.) /usr/bin/gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Or, alternatively add the DLL and the Example in an C# development environment
of your choice (such as Visual Studio or Mono Develop).


.. _api_bindings_csharp_cls_complience:

CLS Compliance
--------------

Since version 2.0.0 the C# bindings are `Common Language Specification
<http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `CLI/.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__.
For :ref:`Visual Basic .NET <api_bindings_vbnet>` we provide dedicated
example code and documentation to demonstrate this.


More Examples and Projects
--------------------------

All the small examples contained in the ZIP file of the bindings can also be
found in the API documentation of the :ref:`Bricks <index_bricks>` and
:ref:`Bricklets <index_bricklets>`.

Further project descriptions can be found in the :ref:`kits <kits>` section.

.. FIXME: add a list with direct links here
