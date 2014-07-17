
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-labview">Software</a> / LabVIEW - API Bindings

.. _api_bindings_labview:

LabVIEW - API Bindings
======================

**Requirements**: LabVIEW on Windows with .NET support

The LabVIEW bindings (:ref:`download <downloads_bindings_examples>`)
are the same as the :ref:`C# bindings <api_bindings_csharp>`.
Since version 2.0.0 the C# bindings are
`CLS <http://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `CLI/.NET compatible languages
<http://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
LabVIEW's `.NET support
<http://zone.ni.com/reference/en-XX/help/371361K-01/lvcomm/dotnet_pal/>`__.

The bindings consist of a library (.dll) for all Tinkerforge
Bricks and Bricklets (``Tinkerforge.dll``), the C# source of the DLL
(in ``source/``) and all available LabVIEW examples (in ``examples/``).
The examples are stored in LabVIEW 2013 format. All examples are
provided in LabVIEW 2010 format as well.


.. _api_bindings_labview_install:

Installation
------------

TODO


Testing an Example
------------------

To make the bindings work LabVIEW has to be able to find the ``Tinkerforge.dll``.
If you open an example then LabVIEW will search fo it and ask you if it could
not find it. You can avoid this search and ask procedure by putting the
``Tinkerforge.dll`` in a folder known to LabVIEW. The easiest options are
the ``vi.lib`` folder of your LabVIEW installation (for example:
``C:\Program Files\National Instruments\LabVIEW 2013\vi.lib\``) or you can put
it in the same folder as the example you want to test. In both cases LabVIEW
will find the ``Tinkerforge.dll`` automatically and does not ask for your
support. But LabVIEW might warn that ``Tinkerforge.dll`` was loaded from a
different folder. This warning can be ignored.

As an example we will run the Stepper Brick configuration example. To do this
open ``examples/Brick/Stepper/ExampleConfiguration.vi`` in LabVIEW, change the
UID to the one of your Stepper Brick and run it.

Here's an another :ref:`example <barometer_bricklet_labview_examples>`
showing a graph of air pressure values measured by a Barometer Bricklet.

.. image:: /Images/Screenshots/labview_example_frontpanel.jpg
   :scale: 100 %
   :alt: Front Panel Barometer Bricklet Graph Example
   :align: center

And here the corresponding block diagram:

.. image:: /Images/Screenshots/labview_example_blockdiagram_small.png
   :scale: 100 %
   :alt: Block Diagram Barometer Bricklet Graph Example
   :align: center
   :target: ../_images/Screenshots/labview_example_blockdiagram.png

API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_LabVIEW_links.table
