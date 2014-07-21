
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-vbnet">Software</a> / Visual Basic .NET - API Bindings

.. _api_bindings_vbnet:

Visual Basic .NET - API Bindings
================================

**Requirements**: Visual Basic 2005 (VB 8.0) or newer, or Mono 1.2.3 or newer

The Visual Basic .NET bindings (:ref:`download <downloads_bindings_examples>`)
are the same as the :ref:`C# bindings <api_bindings_csharp>`.
Since version 2.0.0 the C# bindings are
`CLS <http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `CLI/.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
Visual Basic .NET.

The bindings consist of a library (.dll) for all Tinkerforge
Bricks and Bricklets (``Tinkerforge.dll``), the C# source of the DLL
(in ``source/``) and all available Visual Basic .NET examples (in ``examples/``).


.. _api_bindings_vbnet_install:

Installation
------------

TODO


Testing an Example
------------------

As an example we will compile the Stepper Brick configuration example with
MonoDevelop and Visual Studio.


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
content with the content from ``examples/Brick/Stepper/ExampleConfiguration.vb``.

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

 /usr/bin/vbnc /target:exe /out:ExampleConfiguration.exe /reference:Tinkerforge.dll ExampleConfiguration.vb


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
content with the content from ``examples\Brick\Stepper\ExampleConfiguration.vb``.

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


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_VBNET_links.table
