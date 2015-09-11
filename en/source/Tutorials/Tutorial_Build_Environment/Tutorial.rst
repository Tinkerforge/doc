
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#getting-started">Getting Started</a> / Tutorial - Build Environment Setup

.. _tutorial_build_environment_setup:

Tutorial - Build Environment Setup
==================================

Nearly everything we do at Tinkerforge is open source. Including all of the
generators, source code, schematics, layout and CAD design files that make up
the building block system of Bricks and Bricklets.

Take a look at our `GitHub account <https://github.com/Tinkerforge>`__ to
get an overview over all of our open source projects.

We offer a script that sets up a complete build environment for the
Tinkerforge ecosystem:

* `build_environment_setup.sh <https://github.com/Tinkerforge/generators/blob/master/build_environment_setup.sh>`__

It was tested with a Ubuntu 15.04 VirtualBox image from `osboxes.org <http://www.osboxes.org/>`__.
It should work as-is on most current Debian based Linux distribution. For
non-Debian based distribution you have to replace the ``apt-get`` calls with the
respective counterpart (``yum``, ``emerge``, ``packman``, etc). If your
distribution does not have a package for the ``arm-none-eabi-gcc`` you
can use the ``gcc-arm-embedded`` compiler 
`from launchpad <https://launchpad.net/gcc-arm-embedded>`__.

For development on Windows or Mac OS X we recommend that you use a VirtualBox
image with a shared ``tf/`` directory. Then you can develop on your favorite
OS with your IDE etc and still use all of the Linux specific infrastructure 
that is needed for our development environment.

If you have an environment set-up with the script above, you can:

* Modify and compile Brick firmwares
* Modify and compile Bricklet plugins
* Modify and generate APIs/bindings for all of our supported programming languages
* Modify and compile Brick Viewer/Daemon
* View and modify schematics and layout files for Bricks and Bricklets (with KiCad)
* View and modify case CAD files (with FreeCAD).
* Modify and build the documentation

In the following we will assume that a build environment is set-up with
the above script.

Brick Firmwares
---------------

To compile a Brick firmware you first have to link in the ``bricklib``
and generate the ``Makefile`` (e.g. for the Master Brick)::

 cd ~/tf/master-brick/software/src/
 ln -s ../../../bricklib/ .
 cd ~/tf/master-brick/software/
 ./generate_makefile

Then you can build the source with a normal ``make`` call::

 cd ~/tf/master-brick/software/build
 make

The build firmware will be available in the ``software/build/`` directory.
In this case ``master-brick.bin``. It can be flashed to the Brick with the
:ref:`Brick Viewer <brickv_flash_firmware>`. Just select "Custom..." 
in the Updates/Flashing dialog and pick the newly compiled firmware file.

Bricklet Plugins
----------------

To compile a Bricklet plugin you first have to link in the ``bricklib``
and the ``brickletlib`` and generate the ``Makefile`` 
(e.g. for the Master Brick)::

 cd ~/tf/temperature-bricklet/software/src/
 ln -s ../../../bricklib/ .
 ln -s ../../../brickletlib/ .
 cd ~/tf/temperature-bricklet/software/
 ./generate_makefile

Then you can build the source with a normal ``make`` call::

 cd ~/tf/temperature-bricklet/software/build
 make

The build firmware will be available in the ``software/build/`` directory.
In this case ``temperature-bricklet.bin``. It can be flashed to the Bricklet 
with the :ref:`Brick Viewer <brickv_flash_firmware>`. Just select "Custom..." 
in the Updates/Flashing dialog and pick the newly compiled firmware file.

APIs/Bindings
-------------

We offer Bindings for many programming languages. Each of the bindings
provides access to the API of all Bricks and Bricklets. These bindings and APIs
are automatically generated from config files. If you want
to add a function to a API, you have to change the appropriate config file
and add the code that implements this function to a Brick/Bricklet.

The generators for the bindings are all in one big
`generators git repository <https://github.com/Tinkerforge/generators>`__.
The configs can be found in ``~/tf/generators/configs/``.

Lets pretend that we want to add a ``SetBreakCondition`` API function to
the RS232 Bricklet to be used in Java.

To achieve that we first have to add the function to 
``bricklet_rs232_config.py`` in ``~/tf/generators/configs/``:

* `Add function to config <https://github.com/Tinkerforge/generators/commit/dc4dd52c24ab470c5582cfaa0d67690490ec5d0c>`__.

Then we have to implement the function in the plugin source code of the
RS232 Bricklet (see above on how to compile Bricklet firmware):

* `Implement function in plugin <https://github.com/Tinkerforge/rs232-bricklet/commit/3139edc7d8399c9feb82570fcce061e9c9d27944>`__.

Now we can re-generate the bindings::

 cd ~/tf/generators/
 python generate_all.py
 python copy_all.py

That is all! The new Java bindings are now available in
``~/tf/generators/java/tinkerforge_java_bindings_2_x_y.zip``.
Since we also executed the ``copy_all.py`` script, the new bindings
are now also automatically available in the Brick Viewer source code and
the documentation for the new API was automatically added to the ``doc``-git.

Brick Viewer/Daemon
-------------------

The Brick Daemon is available in ``~/tf/brickd/``. You can build it with::

 cd ~/tf/brickd/src/brickd
 make

You can install the compiled version with::

 sudo make install

Run the following commands to register brickd for autostart on Debian based
Linux distributions and start it::

 sudo update-rc.d brickd defaults
 sudo /etc/init.d/brickd start

The Brick Viewer is available in ``~/tf/brickv/``. It can be started with::

 cd ~/tf/brickv/src/brickv
 python main.py

If you change GUI elements you have to rebuild the UI before starting brickv::

 cd ~/tf/brickv/src
 python build_all_ui.py


Schematic and Layout Files
--------------------------

You can view or modify Brick/Bricklet schematics and PCB layouts. All of
our hardware designs are made with the open source EDA tool 
`KiCad <http://kicad-pcb.org/>`__.

To open a KiCad project file you first have to link in the ``kicad-libraries``
git (e.g. for the Master Brick)::

 cd ~/tf/master-brick/hardware/
 ln -s ../../kicad-libraries/ .

Then you can open the project with KiCad::

 kicad ~/tf/master-brick/hardware/master.pro

KiCad is also available for Windows and Mac OS X.

Case CAD Files
--------------

Our laser-cut acrylic cases are designed with
`FreeCAD <http://www.freecadweb.org/>`__. The cases are in the 
``cases``-git which is in ``~/tf/cases``.

As an example, you can open the case project file of the Ambient Light 
Bricklet with::

 freecad ~/tf/cases/ambient_light/ambient_light.fcstd

FreeCAD is also available for Windows and Mac OS X.

Documentation
-------------

The documentation is written in
`reStructuredText <http://docutils.sourceforge.net/rst.html>`__. It is available
in the ``doc``-git in ``~/tf/doc``.

You can build the whole documentation with::

 cd ~/tf/doc/
 make html

Please make sure to not change any of the auto-generated files. All of the
API documentation is automatically generated by the generators (see above).

The build English documentation will be available at
``~/tf/doc/en/build/html/index.html`` and the German documentation at
``~/tf/doc/de/build/html/index.html``.
