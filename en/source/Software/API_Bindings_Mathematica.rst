
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-mathematica">Software</a> / Mathematica - API Bindings

.. _api_bindings_mathematica:

Mathematica - API Bindings
==========================

The Mathematica bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your Mathematica programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``Tinkerforge.dll``, a precompiled .NET library
* in ``source/`` the source code of ``Tinkerforge.dll``
* in ``examples/`` the examples for every Brick and Bricklet

The Mathematica bindings are based on the :ref:`C# bindings <api_bindings_csharp>`.
Since version 2.0.0 the C# bindings are
`CLS <https://en.wikipedia.org/wiki/Common_Language_Specification>`__
compliant. This allows to use them with all `.NET compatible languages
<https://en.wikipedia.org/wiki/List_of_CLI_languages>`__, such as
Mathematica's `.NET/Link support
<http://reference.wolfram.com/language/NETLink/tutorial/CallingNETFromTheWolframLanguage.html>`__.
It requires the `.NET Framework <http://www.microsoft.com/net>`__ on Windows
and the `Mono Framework <http://www.mono-project.com/>`__ on Linux and Mac OS X.


Requirements
------------

* Mathematica 5.0 or newer on Windows, Linux or Mac OS X with .NET/Link support


.. _api_bindings_mathematica_install:

Installation
------------

The installation of the Mathematica bindings is optional. You can install them
as Mathematica :ref:`AddOn <api_bindings_mathematica_install_addon>` or as
Mathematica :ref:`SystemFile <api_bindings_mathematica_install_systemfile>`,
but you can also use them :ref:`without installing
<api_bindings_mathematica_install_without>` them first.


.. _api_bindings_mathematica_install_addon:

As AddOn
^^^^^^^^

To install the bindings as AddOn just create a new folder for Tinkerforge in the
Mathematica AddOn-Applications folder and copy the ``Tinkerforge.dll`` file to
it. On Windows the AddOn-Applications folder for Mathematica 9 is located here
(for Mathematica 10 replace ``9.0`` by ``10.0``)::

 C:\Program Files\Wolfram Research\Mathematica\9.0\AddOns\Applications\

On Linux it's located here (for Mathematica 10 replace ``9.0`` by ``10.0``)::

 /usr/local/Wolfram/Mathematica/9.0/AddOns/Applications/

And on Mac OS X it's located here::

 /Applications/Mathematica.app/AddOns/Applications/

Create a ``Tinkerforge/`` folder here, create an ``assembly/`` folder in copy
the ``Tinkerforge.dll`` file to it. Afterwards it should look like this on
Windows::

 C:\Program Files\Wolfram Research\Mathematica\9.0\AddOns\Applications\Tinkerforge\assembly\Tinkerforge.dll

Like this on Linux::

 /usr/local/Wolfram/Mathematica/9.0/AddOns/Applications/Tinkerforge/assembly/Tinkerforge.dll

And like this on Mac OS X::

 /Applications/Mathematica.app/AddOns/Applications/Tinkerforge/assembly/Tinkerforge.dll

If you installed the bindings like this then you have to modify the
``LoadNETAssembly[]`` call in the examples like this:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge","Tinkerforge`"]

The section about testing an example has more details about this.


.. _api_bindings_mathematica_install_systemfile:

As SystemFile
^^^^^^^^^^^^^

To install the bindings as Systemfile copy the ``Tinkerforge.dll`` file to
Mathematica's SystemFiles folder for .NET/Link. On Windows the SystemFiles
folder for .NET/Link for Mathematica 9 is located here (for Mathematica 10
replace ``9.0`` by ``10.0``)::

 C:\Program Files\Wolfram Research\Mathematica\9.0\SystemFiles\Links\NETLink\

On Linux it's located here (for Mathematica 10 replace ``9.0`` by ``10.0``)::

 /usr/local/Wolfram/Mathematica/9.0/SystemFiles/Links/NETLink/

And on Mac OS X it's located here::

 /Applications/Mathematica.app/SystemFiles/Links/NETLink/

If you installed the bindings like this then you have to modify the
``LoadNETAssembly[]`` call in the examples like this:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge"]

The section about testing an example has more details about this.


.. _api_bindings_mathematica_install_without:

Without Installation
^^^^^^^^^^^^^^^^^^^^

You can use the Mathematica bindings without having to install them. Just
give the folder that contains the ``Tinkerforge.dll`` file as parameter to
the ``LoadNETAssembly[]`` call. The examples are set up in a ways that the
``LoadNETAssembly[]`` call already points correctly to the ``Tinkerforge.dll``
file if the bindings and the examples have been unpacked from the ZIP file. The
section about testing an example has more details about this.


Testing an Example
------------------

To test a Mathematica example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

Stepper Brick
^^^^^^^^^^^^^

As an example we will run the Stepper Brick configuration example. To do this
open the ``ExampleConfiguration.nb`` Notebook from the
``examples/Brick/Stepper/`` folder in Mathematica.

Loading the Bindings
""""""""""""""""""""

Depending on if and how you installed the Mathematica bindings you have to
adapt the ``LoadNETAssembly[]`` call accordingly to make Mathematica find the
``Tinkerforge.dll`` file. Further details about handling .NET libraries in
`Mathematica documentation
<http://reference.wolfram.com/language/NETLink/ref/LoadNETAssembly.html>`__.

If the bindings are installed as :ref:`AddOn
<api_bindings_mathematica_install_addon>` then the ``LoadNETAssembly[]``
call has to look like this:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge","Tinkerforge`"]

If the bindings are installed as :ref:`SystemFile
<api_bindings_mathematica_install_systemfile>` then the ``LoadNETAssembly[]``
call has to look like this:

.. code-block:: mathematica

  LoadNETAssembly["Tinkerforge"]

If you did :ref:`not install <api_bindings_mathematica_install_without>` the
bindings then the ``LoadNETAssembly[]`` call can stay as it is, if you run the
examples from the unpacked ZIP file for the bindings. The examples are set up in
a ways that the ``LoadNETAssembly[]`` call already points correctly to the
``Tinkerforge.dll`` file if the bindings and the examples have been unpacked
from the ZIP file.

You can also call ``LoadNETAssembly[]`` with an absolute path to the
``Tinkerforge.dll`` file. For example like this on Windows:

.. code-block:: mathematica

  LoadNETAssembly["C:\\Absolute\\path\\to\\Tinkerforge.dll"]

Or like this on Linux and Mac OS X:

.. code-block:: mathematica

  LoadNETAssembly["/Absolute/path/to/Tinkerforge.dll"]

Configure Network Address and UID
"""""""""""""""""""""""""""""""""

In the example ``host`` and ``port`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``uid`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: mathematica

  host="localhost"
  port=4223
  uid="XYZ"(* Change to your UID *)

Now you're ready to test this example. Evaluate all cells in top-down order
to do this.

Temperature Bricklet
^^^^^^^^^^^^^^^^^^^^

Here's an another :ref:`example <temperature_bricklet_mathematica_examples>`
showing a dynamic plot of Temperature Bricklet measurements. The drop at sample
82 was created using a freezer spray.

.. image:: /Images/Screenshots/mathematica_example.jpg
   :scale: 100 %
   :alt: Temprature Bricklet dynamic plot example
   :align: center


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_Mathematica_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_Mathematica>
   Bricks <Bricks_Mathematica>
   Bricklets <Bricklets_Mathematica>
