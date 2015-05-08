
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-vbnet">Software</a> / Visual Basic .NET - API Bindings

.. _api_bindings_vbnet:

Visual Basic .NET - API Bindings
================================

The Visual Basic .NET bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Visual Basic .NET programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.dll``, a precompiled .NET library
* ``Tinkerforge.xml``, the API documentation for Visual Studio, MonoDevelop, etc
* in ``source/`` the source code of ``Tinkerforge.dll``
* in ``examples/`` the examples for every Brick and Bricklet

The Visual Basic .NET bindings are based on the :ref:`C# bindings
<api_bindings_csharp>`. Since version 2.0.0 the C# bindings are
`CLS <http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
Visual Basic .NET.


Requirements
------------

* Visual Basic 2005 (VB 8.0) or newer, or Mono 1.2.3 or newer


.. _api_bindings_vbnet_install:

Installation
------------

If and how the Visual Basic .NET bindings have to be installed depends heavily
on how you are going to use them. If you are just calling the Visual Basic .NET
compiler from the command line then you can just put the ``Tinkerforge.dll``
file into the same folder as the Visual Basic .NET code of your program.

To use the bindings in an IDE you'll probably have to add the
``Tinkerforge.dll`` file to the assembly catalog of the IDE. How this is done
depends on the IDE and will be explained in documentation of that IDE.


Testing an Example
------------------

To test a Visual Basic .NET example :ref:`Brick Daemon <brickd>` and
:ref:`Brick Viewer <brickv>` have to be installed first. Brick Daemon acts as
a proxy between the USB interface of the Bricks and the API bindings. Brick
Viewer connects to Brick Daemon and helps to figure out basic information about
the connected Bricks and Bricklets.

MonoDevelop
^^^^^^^^^^^

As an example we will compile the Stepper Brick configuration example with
the Visual Basic .NET Compiler (VBNC) that comes with Mono. Create a new
Visual Basic .NET project in MonoDevelop by clicking:

* File
* New
* Solution...
* Choose "VBNet"
* Choose "Console Project"
* Choose a name (e.g. ExampleConfiguration)
* Click Forward
* Click OK

MonoDevelop should show an ``Application.vb`` file in its editor. Replace its
content with the content from ``ExampleConfiguration.vb`` file in the
``examples\Brick\Stepper\`` folder.

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: csharp

  Const HOST As String = "localhost"
  Const PORT As Integer = 4223
  Const UID As String = "XYZ" ' Change to your UID

Now add ``Tinkerforge.dll`` as a reference to the project:

* Right click on References in Solution Explorer
* Edit References...
* Click on .Net Assembly tab
* Select ``Tinkerforge.dll``
* Click Add

The project is now ready for a test, click:

* Run
* Run

The Visual Basic .NET Compiler can also be used from the command line::

 vbnc /target:exe /out:Example.exe /reference:Tinkerforge.dll ExampleConfiguration.vb


Visual Studio
^^^^^^^^^^^^^

As an example we will compile the Stepper Brick configuration example with
Microsoft Visual Basic 2010. Create a new Visual Basic project by clicking:

* File
* New Project...
* Choose "Visual Basic"
* Choose "Console Application"
* Choose a name (e.g. ExampleConfiguration)
* Click OK

Visual Studio should show an ``Module1.vb`` file in its editor. Replace its
content with the content from ``ExampleConfiguration.vb`` file in the
``examples\Brick\Stepper\`` folder.

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: csharp

  Const HOST As String = "localhost"
  Const PORT As Integer = 4223
  Const UID As String = "XYZ" ' Change to your UID

Now add ``Tinkerforge.dll`` as a reference to the project:

* Right click on the project in Solution Explorer
* Add References...
* Click on Browse tab
* Select ``Tinkerforge.dll``
* Click OK

Before the project can be tested Visual Studio needs to know the correct start
object:

* Right click on the project in Solution Explorer
* Properties
* Click on Application tab
* Select "Sub Main" as start object
* Click Save

The project is now ready for a test, click:

* Debug
* Start Debugging


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_VBNET_links.table
