
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / Firmwares and Plugins

.. _firmwares_and_plugins:

Firmwares and Plugins
=====================

.. note::
 If you accidentally erased the firmware of a Brick or Bricklet, you can
 download the latest firmware and plugin
 versions :ref:`here <downloads_firmwares_plugins>`.

 Only if you want to change something in a firmware of a Brick or a
 plugin of a Bricklet you will need to compile them yourself.


You can modify and build the Brick firmwares and Bricklet plugins. At the
moment there is no official Brick API or documentation of the Brick firmware
Bricklet plugin code. So you will need some prior knowledge in C programming
to do this.


.. _firmwares_and_plugins_install:

Install Compiler and Tools
--------------------------

As compiler we use GCC for ARM from `CodeSourcery
<http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__.
Choose EABI as Target OS and download the Lite Edition of the Sourcery
CodeBench. It includes GCC for ARM and other tools. The Sourcery CodeBench
installer is available for Linux and Windows.

If you're running a 64-bit version of Linux you might have to install 32-bit
support libraries to get the compiler working. On Debian you just have to
install the ``ia32-libs`` package, see this `CodeSourcery Knowledgebase entry
<https://sourcery.mentor.com/GNUToolchain/kbentry62>`__ for more details.

There are versions of this compiler that do not produce working firmwares.
It's recommended to only use compiler versions that are known to work correctly,
see the following list:

.. csv-table::
   :header: "Version", "Works"
   :widths: 25, 5

   "Sourcery CodeBench Lite 2011.09-69, GCC 4.6.1", "Yes"
   "Sourcery CodeBench Lite 2012.03-56, GCC 4.6.3", "Yes"
   "Sourcery CodeBench Lite 2012.09-63, GCC 4.7.2", "No"
   "Sourcery CodeBench Lite 2013.05-23, GCC 4.7.3", "Yes"

Install the compiler and ensure that the ``bin`` folder of the CodeSourcery
installation is added to the ``PATH`` environment variable. On Windows the
installer offers to do this. Check that the compiler is properly installed by
running this in a terminal::

 arm-none-eabi-gcc --version

You should see some version information about GCC.

Next, CMake and make have to be installed. On Debian and related Linux
distributions they can installed as follows::

 sudo apt-get install cmake make

A CMake installer for Windows is available on the `project's website
<http://www.cmake.org/cmake/resources/software.html>`__. The `GnuWin32 project
<http://gnuwin32.sourceforge.net/packages/make.htm>`__ provides a make installer
for Windows. In both cases ensure that the ``bin`` folder of the CMake and make
installation is added to the ``PATH`` environment variable. Again this can be
check by running this in a terminal::

 cmake --version

.. code-block:: none

 make --version

You should see some version information about CMake and make.

Now the compiler and tools are ready to be used from a terminal.


Building a Brick Firmware or a Bricklet Plugin
----------------------------------------------

There are detailed descriptions about how to get the necessary source code
from GitHub and how to compile it for:

* :ref:`Brick Firmwares <building_brick_firmware>`
* :ref:`Bricklet Plugins <building_bricklet_plugin>`
