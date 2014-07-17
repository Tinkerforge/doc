
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-matlab">Software</a> / MATLAB/Octave - API Bindings

.. _api_bindings_matlab:

MATLAB/Octave - API Bindings
============================

**Requirements**: MATLAB or Octave with Java support

The MATLAB bindings (:ref:`download <downloads_bindings_examples>`) consist of
two .jar files with the bindings for all Tinkerforge Bricks and Bricklets,
one .jar for MATLAB (``matlab/Tinkerforge.jar``) and another one für Octave
(``octave/Tinkerforge.jar``). The source for the MATLAB .jar
(``matlab/source/``) and for the Octave .jar (``octave/source/``) and all
available MATLAB (``matlab/examples/``) and Octave examples
(``octave/examples/``) are included as well.


Testing an Example
------------------

The bindings include examples for MATLAB and Octave.

MATLAB
^^^^^^

First thing you have to make sure is that the Java support for MATLAB is
configured properly. Currently MATLAB only works with Java version 1.6.
So if you have some other version of Java installed on your system then
you have to make sure that MATLAB Java uses Java version 1.6.

Usually MATLAB is by default configured with Java support. You can verify
the MATLAB Java interface with the following command in your MATLAB console::

 version -java

If it is made sure that MATLAB has the Java interface properly configured
the next thing to make sure is to add the ``Tinkerforge.jar`` file to the
``javaclasspath`` of MATLAB. To do this, place the ``Tinkerforge.jar`` file
for MATLAB to the MATLAB installation root directory. Then add the following
line::

 $matlabroot/Tinkerforge.jar

to the file located at::

 <MATLAB-installation-root>/toolbox/local/classpath.txt

This applies for both Windows and Linux installation of MATLAB.

Now all the MATLAB examples can be tried out simply by executing them
form MATLAB console.


Octave
^^^^^^

It is important to verify that Java support is enabled for Octave. For Debian
Linux you can just install the  ``octave`` and ``octave-java`` packages::

  sudo apt-get install octave octave-java

Ensure that you have at least ``octave-java`` 1.2.8-6 installed. This should
make Octave's Java support properly configured. Now add the following line:

.. code-block:: none

 javaaddpath("<path-to-bindings>/Tinkerforge.jar");

to the file located at::

 ~/.octaverc

If this file is not there then create one. After adding this line
restart Octave if you had any running Octave console. Now the examples
can be executed from Octave console.

For using these bindings with Octave in Windows you need to setup the
MinGW version of Octave. This version comes preconfigured with Java support
enabled by default. Follow the instructions from `here
<http://wiki.octave.org/Octave_for_Microsoft_Windows>`__ to set up Octave
in Windows.

Once Octave setup is complete then run Octave console and from the console
add the ``Tinkerforge.jar`` file for Octave with the following command:

.. code-block:: none

 javaaddpath("<path-to-bindings>/Tinkerforge.jar");

Now all the examples should be able to execute from Octave console.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`kits <index_kits>` section.

.. include:: API_Bindings_MATLAB_links.table
