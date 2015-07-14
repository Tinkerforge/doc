
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-labview">Software</a> / LabVIEW - API Bindings

.. _api_bindings_labview:

LabVIEW - API Bindings
======================

The LabVIEW bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your LabVIEW programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.dll``, a precompiled .NET library
* in ``source/`` the source code of ``Tinkerforge.dll``
* in ``examples/`` the examples for every Brick and Bricklet in LabVIEW 2010
  and LabVIEW 2013 format

The LabVIEW bindings are based on the :ref:`C# bindings <api_bindings_csharp>`.
Since version 2.0.0 the C# bindings are
`CLS <https://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `.NET compatible languages
<https://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
LabVIEW's `.NET support
<http://zone.ni.com/reference/en-XX/help/371361K-01/lvcomm/dotnet_pal/>`__.


Requirements
------------

* LabVIEW on Windows with .NET support


.. _api_bindings_labview_install:

Installation
------------

To make the bindings work LabVIEW has to be able to find the ``Tinkerforge.dll``.
If you open an example then LabVIEW will search for it and ask you if it could
not find it. You can avoid this search and ask procedure by putting the
``Tinkerforge.dll`` in a folder known to LabVIEW. The easiest option is the
``vi.lib`` folder of your LabVIEW installation::

 C:\Program Files\National Instruments\LabVIEW 2013\vi.lib\

Then LabVIEW will find the ``Tinkerforge.dll`` automatically and does not ask
for your support. But LabVIEW might warn that ``Tinkerforge.dll`` was loaded
from a different folder. This warning can be ignored.


Testing an Example
------------------

To test a LabVIEW example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.


Stepper Brick
^^^^^^^^^^^^^

As an example let's run the configuration example for the Stepper Brick. For
this we copy the ``Example Configuration.vi`` file from the
``examples/Brick/Stepper/`` folder into a new folder::

 example_project/
  -> Example Configuration.vi

If you did **not** copy the bindings to the ``vi.lib`` folder of your LabVIEW
installation then the ``Tinkerforge.dll`` file has to be copied to the
``example_project/`` folder as well before the example can be opened in LabVIEW::

 example_project/
  -> Tinkerforge.dll
  -> Example Configuration.vi

In the example ``host`` and ``port`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``uid`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer.

Now you're ready to test this example.

Barometer Bricklet
^^^^^^^^^^^^^^^^^^

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

API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_LabVIEW_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_LabVIEW>
   Bricks <Bricks_LabVIEW>
   Bricklets <Bricklets_LabVIEW>
