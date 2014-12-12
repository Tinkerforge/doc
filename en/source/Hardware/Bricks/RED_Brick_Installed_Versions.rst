
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / <a href="RED_Brick.html">RED Brick</a> / Installed Versions
:shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions

.. |c| unicode:: 0x2713
    :trim:

.. _red_brick_installed_versions:

RED Brick - Installed Library Versions
======================================

Description
-----------

The RED Brick comes with a plethora of different programming language
libraries already installed. Below you can find the versions that are
installed on the latest ``full`` and ``fast`` image.

This list of versions is automatically generated and not fully complete.
We install libraries from many different sources (Debian packages,
pip packages, tarball, etc). Unfortunately not all of the sources are
easily parsable, thus they are not all included.

Installation of other Libraries
-------------------------------

We made it easy to install other libraries to the RED Brick.

For the languages with package managers (JavaScript, Perl, PHP, Python, Ruby)
the package manager (``npm``, ``cpanm``, ``pear``, ``pip``, ``gem``) is
pre-installed and you can use it through the :ref:`console tab of the Brick
Viewer <red_brick_brickv_console>`. Even if you don't have any experience with
Linux or terminals, you can read up on these package managers and learn how
to use them in a matter of minutes!

For C# and Visual Basic .NET you can just take the .NET DLL, upload it
with your program and add it as a reference during the upload process.
Similarly for Java you can upload missing JARs. They are automatically
added to the class path by the upload wizard.

Most C libraries are available through the normal Debian repository, just
use ``apt-get`` to install them through the RED Brick console tab.

The Tinkerforge Bindings are of course pre-installed for all of the
languages. You can just assume that they are available and use them.

If you know a library that should definitely be in the default images,
please write us an email (info@tinkerforge.com). Include a place where we
can find it and how we can install it. Preferably it is available in the
Debian wheezy repository.

Installed Libraries
-------------------

.. include:: RED_Brick_c_features.table

.. include:: RED_Brick_java_features.table

.. include:: RED_Brick_mono_features.table

.. include:: RED_Brick_perl_features.table

.. include:: RED_Brick_php_features.table

.. include:: RED_Brick_python_features.table

.. include:: RED_Brick_ruby_features.table

