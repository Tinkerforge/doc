
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

Docker
------

The ``build_environment_setup.sh`` script will create a complete build environment
on the local system. Internally at Tinkerforge we use a build environment inside a
Docker container for the Brick/Bricklet firmwares and Brick Daemon. This ensures
reproducible builds across all PCs and also the Jenkins build/test server.

If you have the ``tinkerforge/build_environment_c`` docker container installed, the
Makefiles of the firmwares will detect that and automatically compile with the docker
container.

You can install the docker container with::

 apt-get install docker.io        # For Debian based distributions
 sudo usermod -aG docker <USER>   # Replace <USER> by the user that should be able to compile
                                  # through docker. You have to log in/out once after this
 docker pull tinkerforge/build_environment_c

If you want to compile Brick/Bricklet firmware with the docker container, the only 
dependency for the host system is GNU make.

Brick Firmwares
---------------

To compile a Brick firmware you first have to link in the ``bricklib``
and generate the ``Makefile`` (e.g. for the Master Brick)::

 cd ~/tf/master-brick/software/src/
 ln -sf ../../../bricklib/ .

Then you can build the source with a normal ``make`` call::

 cd ~/tf/master-brick/software
 make

The build firmware will be available in the ``software/build/`` directory.
In this case ``master-brick.bin``. It can be flashed to the Brick with the
:ref:`Brick Viewer <brickv_flash_brick_firmware>`. Just select "Custom..."
in the Updates/Flashing dialog and pick the newly compiled firmware file.

Bricklet Plugins
----------------

To compile a Bricklet plugin you first have to link in the ``bricklib``
and the ``brickletlib`` and generate the ``Makefile`` 
(e.g. for the Temperature Bricklet)::

 cd ~/tf/temperature-bricklet/software/src/
 ln -sf ../../../bricklib/ .
 ln -sf ../../../brickletlib/ .

Then you can build the source with a normal ``make`` call::

 cd ~/tf/temperature-bricklet/software
 make

The build firmware will be available in the ``software/build/`` directory.
In this case ``temperature-bricklet.bin``. It can be flashed to the Bricklet 
with the :ref:`Brick Viewer <brickv_flash_brick_firmware>`. Just select "Custom..."
in the Updates/Flashing dialog and pick the newly compiled firmware file.

Bricklet with Co-Processor Firmwares
------------------------------------

We are currently replacing all of the old Bricklets with EEPROM by new Bricklets
that have a Co-Processor. The old Bricklets use plugins that are loaded by
Bricks from an EEPROM (see above).

The new Bricklets have to be setup differently.

To compile a Co-Processor Bricklet firmware you first have to link in the 
``bricklib2`` and generate the ``Makefile`` (e.g. for the Humidity Bricklet 2.0)::

 cd ~/tf/humidity-v2-bricklet/software/src/
 ln -sf ../../../bricklib2/ .

The Co-Processor Bricklets automatically compile there own bootstrapper and
bootloader. You have to clone the ``brickletboot_xmc`` and 
``bootstrapper_xmc`` gits. The build files assume that they are available
at the same directory level as the bricklet git itself. In the standard build
environment this is in ``~/tf/``. Please make sure to also symlink the
``bricklib2`` for these gits::

 cd ~/tf/brickletboot_xmc/software/src/
 ln -sf ../../../bricklib2/ .
 cd ~/tf/bootstrapper_xmc/software/src/
 ln -sf ../../../bricklib2/ .

Then you can build the source with a normal ``make`` call::

 cd ~/tf/humidity-v2-bricklet/software
 make

The build firmware will be available in the ``software/build/`` directory.
In this case ``humidity-v2-bricklet.zbin``. It can be flashed to the Bricklet 
with the :ref:`Brick Viewer <brickv_flash_brick_firmware>`. Just select "Custom..."
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

The KISYS3DMOD path has to be adapted in order to view the circuit board with the 3D-Viewer of KiCad:

1. Click on Preferences
2. Click on Configure Paths
3. Change the KISYS3DMOD path to ``$HOME/tf/kicad-libraries/3d/`` (the path has to be specified as absolute)
4. Restart KiCad

KiCad is also available for Windows and macOS.

Create 3D Models
----------------

In the hardware folders of the bricks and bricklet are ``*.step`` and ``*.FCStd`` - files.
These were created using the FreeCAD script `StepUp Tools <https://sourceforge.net/projects/kicadstepup/>`__.

Before using the script a few things have to be adapted:

1. Create the file ``ksu-config.ini`` in the home directory. The file will be filled with content when the script runs the first time.
2. Set a symlink to ``kicad-libraries``-git (example: see above)
3. Change the KISYS3DMOD path to ``$HOME/tf/kicad-libraries/3d/`` (all paths have to be absolute in KiCad!)
4. Copy the `script <https://github.com/Tinkerforge/kicad-libraries/blob/master/3d/Scripts/kicad-StepUp-tools.FCMacro>`__ into the folder where the ``*.kicad-pcb`` is you would convert to 3d.
5. Run the script once with::

 freecad kicad-StepUp-tools.FCMacro \#brick(let)name\#

6. Adapt the ``prefix3D`` path in ``ksu-config.ini`` file to ``$HOME/tf/kicad-libraries/3d/`` (absolute again!)
7. Run the script again

The script creates a ``*.step`` and a ``*.FCStd`` -project file.

The FreeCAD Macro ``kicad-StepUp-tools.FCMacro`` can be opened directly in FreeCAD for generating the required ``*.wrl`` und ``*.step`` - files. The (*.wrl) file is needed for displaying the model in KiCad 3D Viewer and the (*.step) file for 
running the script. It is very easy to align the X/Y/Z axis with the macro. It is also possible to load KiCad footprints which can be used as starting point for self made 3d models. 

The complete documentation can be found `here <https://github.com/Tinkerforge/kicad-libraries/raw/master/3d/Scripts/kicadStepUp-starter-Guide.pdf>`__. A cheat-sheet with a short overview about
the most important functions can be found `here <https://github.com/Tinkerforge/kicad-libraries/raw/master/3d/Scripts/kicadStepUp-cheat-sheet.pdf>`__.

Case CAD Files
--------------

Our laser-cut acrylic cases are designed with
`FreeCAD <http://www.freecadweb.org/>`__. The cases are in the 
``cases``-git which is in ``~/tf/cases``.

As an example, you can open the case project file of the Ambient Light 
Bricklet with::

 freecad ~/tf/cases/ambient_light/ambient_light.fcstd

FreeCAD is also available for Windows and macOS.

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
