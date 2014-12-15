
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-csharp">Software</a> / C# - API Bindings

.. _api_bindings_csharp:

C# - API Bindings
=================

.. note::
 There is an extra section for :ref:`C# and Windows Phone
 <api_bindings_csharp_windows_phone>`.

The C# bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your C# programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.dll``, a precompiled C#/.NET library (without debug info)
* ``Tinkerforge.dll.mdb``, debug info for ``Tinkerforge.dll``
* ``Tinkerforge.xml``, the API documentation for Visual Studio, MonoDevelop, etc
* in ``source/`` the source code of ``Tinkerforge.dll``
* in ``examples/`` the examples for every Brick and Bricklet

The C#/.NET library has no external dependencies.


Requirements
------------

* C# compiler


.. _api_bindings_csharp_install:

Installation
------------

If and how the C# bindings have to be installed depends heavily on how you are
going to use them. If you are just calling the C# compiler from the command
line then you can just put the ``Tinkerforge.dll`` file into the same folder
as the C# code of your program.

To use the bindings in an IDE you'll probably have to add the
``Tinkerforge.dll`` file to the assembly catalog of the IDE. How this is done
depends on the IDE and will be explained in documentation of that IDE.

The C# bindings are also available as `NuGet package
<https://www.nuget.org/packages/Tinkerforge/>`__ that can be added in Visual
Studio C# and MonoDevelop (via `NuGet addin
<https://github.com/mrward/monodevelop-nuget-addin`__) to your project as
external reference.


Testing an Example
------------------

To test a C# example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example let's compile the configuration example for the Stepper Brick
from the command line. For this we copy ``Tinkerforge.dll`` file and
``ExampleConfiguration.cs`` file from the ``examples/Brick/Stepper/`` folder
into a new folder::

 example_project/
  -> Tinkerforge.dll
  -> ExampleConfiguration.cs

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: csharp

  private static string HOST = "localhost";
  private static int PORT = 4223;
  private static string UID = "XYZ"; // Change to your UID

Now we can call the Visual Studio C# compiler in the ``example_project/`` folder
like this on Windows::

 csc /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

and the Mono Compiler like this on Linux and Mac OS X::

 gmcs /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.cs

Alternatively you can use the C# library and example in an C# IDE of your choice
such as Visual Studio or MonoDevelop.


.. _api_bindings_csharp_cls_complience:

CLS Compliance
--------------

Since version 2.0.0 the C# bindings are `Common Language Specification
<http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__.
For :ref:`Visual Basic .NET <api_bindings_vbnet>`,
:ref:`Mathematica <api_bindings_mathematica>` and
:ref:`LabVIEW (Windows) <api_bindings_labview>` we provide dedicated
examples and documentation to demonstrate this.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_CSharp_links.table
