
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-c">Software</a> / C/C++ - API Bindings

.. _api_bindings_c:

C/C++ - API Bindings
====================

.. note::
 There is an extra section for :ref:`Objective-C and iOS <api_bindings_c_ios>`.

The C/C++ bindings (:ref:`download <downloads_bindings_examples>`) consist of
the bindings for all Tinkerforge Bricks and
Bricklets (in ``bindings/``) and all available C/C++ examples (in
``examples/``).

To keep the C/C++ bindings stupid and simple, they only have
dependencies that are available nearly everywhere, thus making it
possible to compile into any project hassle-free.
We do not offer a pre-compiled library, since it would be a
pain in the ass to provide them for all combinations of architectures and
operating systems. This means, the
bindings should work on most architectures (ARM, x86, etc.) and on most
operating systems (Windows and POSIX systems, such as Linux and Mac OS X, etc.).


Testing an Example
------------------

As an example we will compile the Stepper Brick configuration example
with GCC on Windows and Linux.
For that we have to copy the IP Connection and the Stepper Brick
bindings (``ip_connection.h``, ``ip_connection.c``, ``brick_stepper.c`` and
``brick_stepper.h``) from the ``bindings/`` folder as well as the
``example_configuration.c`` from the ``examples/brick/stepper/`` folder into our
project::

 project_folder/
  -> ip_connection.c
  -> ip_connection.h
  -> brick_stepper.c
  -> brick_stepper.h
  -> example_configuration.c


GCC
^^^

The only dependency on Unix-like systems is pthreads, therefore a
compilation of the example with GCC on Linux looks like::

 gcc -pthread -o example_configuration brick_stepper.c ip_connection.c example_configuration.c

On Windows Win32 is used for threading and WinSock2 (``ws2_32``) for the network
connection. Under MinGW we can compile the example as following (the library
linking must come after the source)::

 gcc -o example_configuration.exe brick_stepper.c ip_connection.c example_configuration.c -lws2_32 -ladvapi32

The simplest way to use the bindings in a C++ project is to rename the required
source files from ``*.c`` to ``*.cpp``. Then the compiler will treat the source
code as C++ and does the right thing automatically.


Visual Studio
^^^^^^^^^^^^^

With Visual Studio we can use the ``project_folder/`` too. The simplest way to
use the bindings in a Visual C++ project is to rename the required source files
from ``*.c`` to ``*.cpp``. Then the compiler will treat the source code as C++
and does the right thing automatically.

As a side note: this will also avoid the problem that the Visual Studio
compiler supports the C89 standard only, but the bindings uses the newer C99
standard.

Now a new project can be created in Visual Studio by clicking:

* File
* New
* Project From Existing Code
* Choose Type "Visual C++"
* Choose ``project_folder/``
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
version can be found `here <http://msinttypes.googlecode.com/svn/trunk/stdint.h>`__.
If necessary download it to the ``project_folder/``.

That's it, we are ready to go!

The Visual Studio compiler can also be used from the command line::

 cl.exe /I. brick_stepper.cpp ip_connection.cpp example_configuration.cpp /link /out:example_configuration.exe ws2_32.lib advapi32.lib


Qt Creator
^^^^^^^^^^

With Qt Creator we can use the ``project_folder/`` too.

A new Qt Creator project for the ``project_folder/`` can be created by clicking:

* File
* New File or Project...
* Choose Other Project
* Choose Empty Qt Project
* Click Choose...
* Choose "project_folder" as Name
* Choose the folder that contains the ``project_folder/`` for "Create in"
* Click Next
* Click Next
* Click Finish

Qt Creator should now show an empty file named ``project_folder.pro``. Copy
and paste the following lines into it and save the result::

  TEMPLATE = app
  CONFIG += console
  TARGET = example_configuration
  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread
  SOURCES += ip_connection.c brick_stepper.c example_configuration.c
  HEADERS += ip_connection.h brick_stepper.h

This tells Qt Creator that this is an console application named
"example_configuration". It is linked to the ``ws2_32`` and ``advapi32``
libraries on Windows and uses pthreads on Unix (Linux, Mac OS X, etc).

Before stating the program you need to tick the "Run in terminal" check box on
the project's run configuration tab, otherwise its output will not be visible.

Now the program can be compiled and started!

This is an example for a project in C. If you want to use the bindings in a C++
project then the simplest way to do this is to rename the required source files
from ``*.c`` to ``*.cpp`` and to change the ``SOURCES`` line in
``project_folder.pro`` accordingly. Then the compiler will treat the source
code as C++ and does the right thing automatically.

If you want to add the C/C++ bindings to an existing Qt Creator project then
you just need to add the required source files to the ``SOURCES`` and
``HEADERS`` variables and add these two lines to your ``.pro`` file::

  win32:LIBS += -lws2_32 -ladvapi32
  unix:QMAKE_CXXFLAGS += -pthread


Orwell Dev-C++
^^^^^^^^^^^^^^

With Dev-C++ we can use the ``project_folder/`` too.

A new Dev-C++ project for the ``project_folder/`` can be created by clicking:

* File
* New
* Project...
* Choose Console Application and C Project
* Click Ok

Dev-C++ will now create a new files named ``main.c``. We don't need it, remove
it by clicking on "Remove file" in its context menu in the project view. Now add
all files from the ``project_folder/`` to the project by clicking on
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


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_C_links.table
