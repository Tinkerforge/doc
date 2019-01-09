
.. _api_bindings_c:

C/C++ - API Bindings
====================

.. note::
 There is an extra section for :ref:`Objective-C and iOS <api_bindings_c_ios>`.

The C/C++ bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` from your C/C++ programs. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* in ``source/`` the source code of the bindings
* in ``examples/`` the examples for every Brick and Bricklet


Requirements
------------

* C compiler (C99 compatible) or C++ compiler


.. _api_bindings_c_install:

Installation
------------

To keep the C/C++ bindings stupid and simple, they only have
dependencies that are available nearly everywhere, thus making it
possible to compile into any project hassle-free.
We do not offer a precompiled library, since it would be a
pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the
bindings should work on most architectures (ARM, x86, etc.) and on most
operating systems (Windows and POSIX systems, such as Linux and macOS, etc.).

Because there is no precompiled library for the C/C++ bindings there is nothing
to install as such. The recommended way of using the bindings is to include their
source code directly into your C/C++ project. The next section shows some examples
about how to do that.


Testing an Example
------------------

To test a C/C++ example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

As an example we will compile the Stepper Brick configuration example
with GCC on the command line and with some IDEs. For that we have to copy the
IP Connection and the Stepper Brick bindings from the ``source/`` folder
as well as the ``example_configuration.c`` from the ``examples/brick/stepper/``
folder into a new folder::

 example_project/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c

In the example ``HOST`` and ``PORT`` specify at which network address the
Stepper Brick can be found. If it is connected locally to USB then ``localhost``
and 4223 is correct. The ``UID`` value has to be changed to the UID of the
connected Stepper Brick, which you can figure out using Brick Viewer:

.. code-block:: c

  #define HOST "localhost"
  #define PORT 4223
  #define UID "XYZ" // Change to your UID


GCC
^^^

The only dependency on Unix-like systems is pthreads, therefore a
compilation of the example with GCC on Linux and macOS looks like this::

 gcc -pthread -o example *.c

On Windows Win32 is used for threading and WinSock2 (``ws2_32``) for the network
connection. Under MinGW we can compile the example as following (the library
linking must come after the source)::

 gcc -o example.exe *.c -lws2_32 -ladvapi32

The simplest way to use the bindings in a C++ project is to rename the required
source files from ``*.c`` to ``*.cpp``. Then the compiler will treat the source
code as C++ and does the right thing automatically.


Visual Studio
^^^^^^^^^^^^^

With Visual Studio we can use the ``example_project/`` folder too. The simplest
way to use the bindings in a Visual C++ project is to rename the required source
files from ``*.c`` to ``*.cpp``. Then the compiler will treat the source code as
C++ and does the right thing automatically. This will also avoid the problem
that the Visual Studio compiler supports the C89 standard only, but the bindings
uses the newer C99 standard.

IDE
"""

Now a new project can be created in Visual Studio by clicking:

* File
* New
* Project From Existing Code
* Choose Type "Visual C++"
* Choose ``example_project/``
* Choose a project name
* Click Next
* Choose "Console Application"
* Click Finish

Then ``ws2_32.lib`` (WinSock2) and ``advapi32.lib`` have to included by clicking:

* Project
* Properties
* Linker
* Input, option "Additional Dependencies"
* Add ``ws2_32.lib;advapi32.lib;``

Older version of Visual Studio don't come with ``stdint.h``. A compatible
version can be found `here <https://github.com/chemeris/msinttypes/blob/master/stdint.h>`__.
If necessary download it to the ``example_project/`` folder.

That's it, now the project can be compiled an executed!

Command Line
""""""""""""

The Visual Studio compiler can also be used from the command line in the
``example_project/`` folder::

 cl.exe /I. *.cpp /link /out:example.exe ws2_32.lib advapi32.lib


Qt Creator
^^^^^^^^^^

A new Qt Creator project for the ``example_project/`` folder can be created by
clicking:

* File
* New File or Project...
* Choose Other Project
* Choose Empty Qt Project
* Click Choose...
* Choose "example_project" as Name
* Choose the folder that contains the ``example_project/`` folder for "Create in"
* Click Next
* Click Next
* Click Finish

Qt Creator should now show an empty file named ``example_project.pro``.
Copy and paste the following lines into it and save the result::

  TEMPLATE = app
  CONFIG += console
  TARGET = example_configuration
  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread
  SOURCES += ip_connection.c brick_stepper.c example_configuration.c
  HEADERS += ip_connection.h brick_stepper.h

This tells Qt Creator that this is an console application named
"example_configuration". It is linked to the ``ws2_32`` and ``advapi32``
libraries on Windows and uses pthreads on Unix (Linux, macOS, etc).

Before stating the program you need to tick the "Run in terminal" check box on
the project's run configuration tab, otherwise its output will not be visible.

Now the program can be compiled and started!

This is an example for a project in C. If you want to use the bindings in a C++
project then the simplest way to do this is to rename the required source files
from ``*.c`` to ``*.cpp`` and to change the ``SOURCES`` line in
``example_project.pro`` accordingly. Then the compiler will treat the source
code as C++ and does the right thing automatically.

If you want to add the C/C++ bindings to an existing Qt Creator project then
you just need to add the required source files to the ``SOURCES`` and
``HEADERS`` variables and add these two lines to your ``.pro`` file::

  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread


Orwell Dev-C++
^^^^^^^^^^^^^^

A new Dev-C++ project for the ``example_project/`` folder can be created by
clicking:

* File
* New
* Project...
* Choose Console Application and C Project
* Click Ok

Dev-C++ will now create a new files named ``main.c``. We don't need it, remove
it by clicking on "Remove file" in its context menu in the project view. Now add
all files from the ``example_project/`` folder to the project by clicking on
"Add to Project" in the project's context menu.

Then ``libws2_32.a`` (WinSock2) and ``libadvapi32.a`` have to included by clicking:

* Project
* Project Options
* Parameters
* Click Add Library or Object
* Choose ``libws2_32.a`` and ``libadvapi32.a``
* Click Open
* Click Ok

Now the program can be compiled and started!

This is an example for a project in C. If you want to use the bindings in a C++
project then the simplest way to do this is to rename the required source files
from ``*.c`` to ``*.cpp``. Then the compiler will treat the source code as C++
and does the right thing automatically.


API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_C_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_C>
   Bricks <Bricks_C>
   Bricks (Discontinued) <Bricks_C_Discontinued>
   Bricklets <Bricklets_C>
   Bricklets (Discontinued) <Bricklets_C_Discontinued>
