
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-mathematica">Software</a> / Mathematica - API Bindings

.. _api_bindings_mathematica:

Mathematica - API Bindings
==========================

**Requirements**: Mathematica 5.0 or newer on Windows, Linux or Mac OS X with .NET/Link support

The Mathematica bindings (:ref:`download <downloads_bindings_examples>`)
are the same as the :ref:`C# bindings <api_bindings_csharp>`.
Since version 2.0.0 the C# bindings are
`CLS <http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `CLI/.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
Mathematica's `.NET/Link support
<http://reference.wolfram.com/language/NETLink/tutorial/CallingNETFromTheWolframLanguage.html>`__.

The .NET/Link support in Mathematica requires the `.NET Framework
<http://www.microsoft.com/net>`__ on Windows and the `Mono Framework
<http://www.mono-project.com/>`__ on Linux and Mac OS X.

The bindings consist of a library (.dll) for all Tinkerforge
Bricks and Bricklets (``Tinkerforge.dll``), the C# source of the DLL
(in ``source/``) and all available Mathematica examples (in ``examples/``).


Testing an Example
------------------

As an example we will run the Stepper Brick configuration example. To do this
open the ``examples/Brick/Stepper/ExampleConfiguration.nb`` Notebook in
Mathematica, change the UID to the one of your Stepper Brick and evaluate all
cells in top-down order.

If you moved the Notebook file to a different folder you might need to change
the ``LoadNETAssembly[]`` line to make Mathematica find the ``Tinkerforge.dll``:

 .. code-block:: mathematica

    LoadNETAssembly["Tinkerforge",NotebookDirectory[]<>"../.."]

Replace the ``NotebookDirectory[]<>"../.."`` parameter with an absolute path
to the folder that contains the ``Tinkerforge.dll``.

Here's an another :ref:`example <temperature_bricklet_mathematica_examples>`
showing a dynamic plot of Temperature Bricklet measurements. The drop at sample
82 was created using a freezer spray.

.. image:: /Images/Screenshots/mathematica_example.jpg
   :scale: 100 %
   :alt: Temprature Bricklet dynamic plot example
   :align: center


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_Mathematica_links.table
