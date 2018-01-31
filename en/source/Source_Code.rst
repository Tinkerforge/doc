
.. _source_code:

Source Code and Bug Tracking
============================

Every product that is released by Tinkerforge is Open Source. The firmware
source as well as the hardware design files for all Bricks and Bricklets are
available. Additionally the source code for all tools, such as the Brick
Daemon, the Brick Viewer and the generators for the language bindings is
available.

This means you can use all of the Tinkerforge hardware and software as a
starting point for your own project, extend or modify it. Furthermore
you can help us in the development effort and most importantly report bugs.

To make it easy for the community to commit patches and report bugs, all
of the `Tinkerforge projects <https://github.com/Tinkerforge>`__ are hosted
on GitHub.

If you don't know git, you can find information `here <https://git-scm.com/>`__.
Our projects can be cloned with::

 git clone git://github.com/Tinkerforge/PROJECT.git

Below is a list of the Tinkerforge project repositories and corresponding
bug tracker.

.. include:: Source_Code_gits.table


Where and How do I report Bugs?
-------------------------------

If you found a bug in one of the Tinkerforge projects, we would love if you
could report it! First of all, you have to identify the correct repository for
your problem:

Bugs that are specific to a Brick/Bricklet (e.g. a specific parameter of a
function in a Brick/Bricklet does not work or there is a hardware bug on a
Brick/Bricklet) and bugs in the Brick Daemon and Brick Viewer can be reported
to the obviously belonging repository.

However, if the bug is in every Brick (e.g. Stack communication is
erroneous or a bug in the USB communication) report to the Brick Library
repository. If it is in every Bricklet (e.g. the timing of recurring
events is wrong) report to the Bricklet Library repository. If it is in the API
or the API Documentation (e.g. typo in the API of a Brick/Bricklet or
wrong statement in the documentation of a Brick/Bricklet) report to the API
Generator repository.

For us it is important that we can reproduce the bug you found. You should
try to write anything in the bug report that is needed to reproduce your
scenario. This includes code snippets that crash something, the setup
of your hardware project or instructions how you connected Bricks and
Bricklets.
