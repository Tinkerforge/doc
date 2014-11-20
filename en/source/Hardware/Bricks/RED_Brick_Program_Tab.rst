
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / <a href="RED_Brick.html">RED Brick</a> / Program Tab
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick_program_tab:

RED Brick Program Tab
=====================


Description
-----------

The program tab of the RED Brick tab of the Brick Viewer is the most important
piece of user interface for the RED Brick. It can help you to upload, modify
and monitor your programs.

.. image:: /Images/Screenshots/red_brick_program_overview.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Program tab.
   :align: center

If you start the RED Brick for the first time you will be presented with an
empty program list and three buttons:

* **Refresh**: Refreshes programs tab
* **New**: Starts New Program wizard
* **Delete**: Deletes selected program

After you uploaded your first program you can select the program and
information about the program will be displayed on the right. You
can edit the configuration and also view and download logs.

Uploading a program to the RED Brick consists of 8 easy steps
that you are guided through by a wizard:

Wizard Step 1: General Information
----------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step1.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 1.
   :align: center

* Name: This is the name of your program. It will be shown in the program list
  and every other time the program is referred to.
* Language: Select the language of your program.
* Description: The description will be shown in the program, if your program
  is selected.
* Unique Identifier: If you uncheck *Auto-generate unique identifier* you will
  have to specify your own identifier. The identifier is mostly used 
  internally. You can use your own identifier if you want to have a specific
  name of the program folder in the underlying Linux.

Wizard Step 2: Files
--------------------

.. image:: /Images/Screenshots/red_brick_wizard_step2.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 2.
   :align: center

* **Add files**: Adds single program files.
* **Add Directory**: Adds your program directory, the included files 
  and subdirectories.
* **Remove**: Removes the selected file or directory.

Please note that the hierarchical structure that you create here will be used
on the RED Brick exactly as specified.

For example, if you want to upload a small web page that is written in
Python/Flask with the following structure

* myproject/

  * index.py
  * templates/
 
    * template1.html
    * template2.html

  * static/

    * static.css
    * static.js

and you want the index.py as well as the two folders to be in the root 
directory of your program on the RED Brick, you need to first
select the index.py with **Add file** and then independently select the 
two folders with **Add Directory**.

Every "Add" will add the thing you are selecting to the root directory
of the RED Brick program.

Wizard Step 3: Language Specific Configuration
----------------------------------------------

In step 3 you have to configure the compiler/interpreter of the language
that you selected in step 1. This step is documented for each
language individually.

C/C++
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_c.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (C/C++).
   :align: center

The Tinkerforge C Bindings are preinstalled on the RED Brick
(compiled as a library (libtinkerforge.so), available in ``/usr/lib/``). 
The headers are available in ``/usr/include/tinkerforge``. You can
directly link against this library (see example below).

* Start Mode: Currently only *Executable* is available as start mode.
* Executable: Name of the executable that should be called. This is
  either the name of the cross compiled executable that you are 
  uploading or it is the name of the executable that is created
  during compilation
* Compile From Source: If you check this checkbox, your code will be
  compiled upon upload. If you use this option your project must
  contain a **Makefile**. An example Makefile for a small
  project that uses the Tinkerforge Bindings and consists otherwise
  of the file **example.c** looks as follows::

    # Defines
    CC=g++
    CFLAGS=-c -Wall -I/usr/include/tinkerforge
    LIBS=-ltinkerforge -lpthread
    EXE=example
    SOURCES=example.c
    OBJECTS=$(SOURCES:.c=.o)

    # Build Rules
    all: $(SOURCES) $(EXE)

    .c.o:
    	$(CC) $(CFLAGS) $< -o $@

    $(EXE): $(OBJECTS)
    	$(CC) $(OBJECTS) -o $(EXE) $(LIBS)

    clean:
    	rm -f *.o $(EXE)
* Make options: If you compile from source you can also add
  Makefile parameters.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.

C#
^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_csharp.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (C#).
   :align: center

For C# the Tinkerforge.dll is available in ``/usr/lib/`` and can
thus be found by mono. That means, if you compile your C# program
and you use the Tinkerforge.dll as reference, it will be
automatically found on the RED Brick. You don't have to add
the Tinkerforge.dll in step 2.

* Mono Version: Currently there is only one mono version installed.
* Start Mode: Currently only *Executable* is available as start mode.
* Executable: Choose the .NET executable from the files that you added
  in step 2. A .NET executable usually has the file ending .exe.

  Your executable will be executed with 
  `mono <http://www.mono-project.com/>`__, but you can compile 
  on Windows with Visual Studio, that works without problem. 
  Make sure that you don't use any Windows specific libraries that 
  are not available on the RED Brick.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Mono Options: Here you can add options that will be given to
  the mono JIT compiler.

Delphi/Lazarus
^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_delphi.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Delphi/Lazarus).
   :align: center

* Start Mode: Currently only *Executable* is available as start mode.
* Executable: Name of the executable that should be called. This is
  either the name of the cross compiled executable that you are 
  uploading or it is the name of the executable that is created
  during compilation
* Compile From Source: If you check this checkbox, your code will be
  compiled upon upload. If you use this option your project must
  contain a **Makefile.fpc**. An example Makefile for a small
  project that uses the Tinkerforge Bindings and has the file
  **Example.pas** as main unit looks as follows::

    [target]
    programs=Example

    [require]
    packages=tinkerforge
* Make options: If you compile from source you can also add
  Makefile parameters.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.

Java
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_java.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Java).
   :align: center

The Tinkerforge.jar Java Bindings are available in
``/usr/tinkerforge/bindings/java/``. The file is already added
to the classpath by default, so you can just import the Tinkerforge
classes by the usual means, e.g. ``import com.tinkerforge.IPConnection;``.

* Java Version: Currently there is only one Java version installed.
* Start Mode: The start modes **Main Class** and **JAR File** are
  available as start mode.

  * Main Class: If you choose main class, the Brick Viewer will parse
    all of the class files that you added in step two and show you
    all Classes that contain a main method and can thus be used to
    start your program.
  * JAR File: If you create a JAR file from your program, you can
    also start your program directly from the JAR file. The available
    JAR files will be listed in the drop down box.
* Class Path: You can add files that are added to your class path.
  All JARs that you added in step 2 will automatically be added
  to the classpath.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* JVM Options: Here you can add options that will be given to
  the Java virtual machine.

JavaScript (Browser/Node.js)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_javascript.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (JavaScript).
   :align: center

* Client-Side (Browser): If you use client-side JavaScript, there is
  nothing to configure. You can add your **.html** files in step 2,
  which are then available through the
  :ref:`RED Brick web interface <red_brick_web_interface>`. The
  **Tinkerforge.js** can be used via::

      <script src="/Tinkerforge.js" type='text/javascript'></script>
* Server-Side (Node.js): If you use Node.js, you can configure the
  start mode and other options. The Tinkerforge Bindings are available,
  you can use ``require('tinkerforge')`` to import them.

  * Start Mode: The start modes **Script File** and **Command** are
    available as start mode.

    * Start Mode *Script File*: Specify the script file that should be
      executed by node.
    * Start Mode *Command*: Specify a command that should be executed
      by node with the **-e** option.
  * Working Directory: Specify the 
    `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
    of your program. You can use a path that is relative to the
    root directory of your program. Usually you will leave this as ``.``.
  * Node.js Options: Here you can add options that will be given to
    node when your script file or command is executed.

Octave
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_octave.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Octave).
   :align: center

For octave the java path to the Tinkerforge.jar is already added
in the octaverc. This means that in your program you can assume
that ``javaaddpath("Tinkerforge.jar")`` was already called with
the correct directory.

* Octave Version: Currently there is only one Octave version installed
  on the RED Brick.
* Start Mode: Currently only **Script File** is available as start mode.
* Script File: Choose one of the script files that you added in step 2,
  it will be executed by octave.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Octave Options: Here you can add options that will be given to
  the Octave interpreter. By default the **--silent** options is
  already set, it suppresses the output version and copyright information
  that is usually done by octave. If you remove this option your log
  file will have this output added to each log entry.

Perl
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_perl.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Perl).
   :align: center

The Tinkerforge Bindings are available. You can use the ``use``
directive to import them, e.g.: ``use Tinkerforge::IPConnection;``.

* Perl Version: Currently there is only one Perl interpreter version
  installed on the RED Brick.
* Start Mode: The start modes **Script File** and **Command** are
  available as start mode.

  * Start Mode *Script File*: Specify the script file that should be
    executed by the Perl interpreter.
  * Start Mode *Command*: Specify a command that should be executed
    by the Perl interpreter with the **-e** option.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Perl Options: Here you can add options that will be given to
  Perl when your script file or command is executed.

PHP
^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_php.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (PHP).
   :align: center

The Tinkerforge Bindings are installed through `PEAR <http://pear.php.net/>`__
and thus available. You can import them with the ``require_once``
function, e.g.: ``require_once('Tinkerforge/IPConnection.php');``.

* PHP Version: Currently there is only one PHP interpreter version
  installed on the RED Brick.
* Start Mode: The start modes **Script File**, **Command** and **Web Interface**
  are available as start mode.

  * Start Mode *Script File*: Specify the script file that should be
    executed by the PHP interpreter.
  * Start Mode *Command*: Specify a command that should be executed
    by the PHP interpreter with the **-r** option.
  * Start Mode *Web Interface*: If you want to implement a web
    interface with PHP you have to chose this option.
    In this case PHP will be called from Apache, thus there are
    no other configurations to be made. See 
    :ref:`RED Brick web interface <red_brick_web_interface>` for
    more informations about the web interface.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* PHP Options: Here you can add options that will be given to
  the PHP interpreter when your script file or command is executed.

Python
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_python.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Python).
   :align: center

The Tinkerforge Bindings are installed through 
`pip <https://pypi.python.org/pypi/pip>`__ and thus
available. You can import them with the normal ``import``
statement, e.g.: ``from tinkerforge.ip_connection import IPConnection``.

* Python Version: You can choose between Python 2 and Python 3.
* Start Mode: The start modes **Script File**, **Module Name**, **Command** and
  **Web Interface** are available as start mode.

  * Start Mode *Script File*: Specify the script file that should be
    executed by the Python interpreter.
  * Start Mode *Module Name*: Specify a module name that should be executed
    by the Python interpreter with the **-m** option.
  * Start Mode *Command*: Specify a command that should be executed
    by the Python interpreter with the **-c** option.
  * Start Mode *Web Interface*: If you want to implement a web
    interface with Python you have to chose this option.
    In this case Python will be called from Apache/WSGI, thus there are
    no other configurations to be made. See 
    :ref:`RED Brick web interface <red_brick_web_interface>` for
    more informations about the web interface.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Python Options: Here you can add options that will be given to
  Python interpreter when your script file or command is executed.


Ruby
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_ruby.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Ruby).
   :align: center

The Tinkerforge Bindings are installed through `gem <https://rubygems.org/>`__
and thus available. You can use the ``require`` statement to import them, 
e.g.: ``require 'tinkerforge/ip_connection'``.

* Ruby Version: Currently there is only one Ruby interpreter version
  installed on the RED Brick.
* Start Mode: The start modes **Script File** and **Command** are
  available as start mode.

  * Start Mode *Script File*: Specify the script file that should be
    executed by the Ruby interpreter.
  * Start Mode *Command*: Specify a command that should be executed
    by the Ruby interpreter with the **-e** option.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Ruby Options: Here you can add options that will be given to
  Ruby when your script file or command is executed.

Shell
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_shell.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Shell).
   :align: center

The Shell Bindings are available in ``/usr/local/bin``, which is
in the PATH. In your shell script you can just call ``tinkerforge`` 
without any prefix.

* Shell Version: Currently there is only one bash version available on the
  RED Brick.
* Start Mode: The start modes **Script File** and **Command** are
  available as start mode.

  * Start Mode *Script File*: Specify the script file that should be
    executed by bash.
  * Start Mode *Command*: Specify a command that should be executed
    by bash with the **-c** option.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Shell Options: Here you can add options that will be given to
  bash when your script file or command is executed.

Visual Basic .NET
^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_vbnet.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Visual Basic .NET).
   :align: center

For Visual Basic .NET the Tinkerforge.dll is available in ``/usr/lib/`` 
and can thus be found by mono. That means, if you compile your VB.NET 
program and you use the Tinkerforge.dll as reference, it will be
automatically found on the RED Brick. You don't have to add
the Tinkerforge.dll in step 2.

* Mono Version: Currently there is only one mono version installed.
* Start Mode: Currently only *Executable* is available as start mode.
* Executable: Choose the .NET executable from the files that you added
  in step 2. A .NET executable usually has the file ending .exe.

  Your executable will be executed with 
  `mono <http://www.mono-project.com/>`__, but you can compile 
  on Windows with Visual Studio, that works without problem. 
  Make sure that you don't use any Windows specific libraries that 
  are not available on the RED Brick.
* Working Directory: Specify the 
  `working directory <http://en.wikipedia.org/wiki/Working_directory>`__ 
  of your program. You can use a path that is relative to the
  root directory of your program. Usually you will leave this as ``.``.
* Mono Options: Here you can add options that will be given to
  the mono JIT compiler.


Wizard Step 4: Arguments and Environment
----------------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step4.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 4.
   :align: center

* Arguments: Your program will be called with the given arguments.

Please note that you don't have to escape your arguments. If you would
call your program on the terminal with::

 ./my_program --setting value1 value2

You have to add the three arguments **--settings**, **value1**
and **value2** individually to the argument list.

If you only add the one argument **--settings value1 value2**
it will be equivalent to the following call in  the terminal::

 ./my_program --settings\ value1\ value2

* Environment: Your program will have the environment variables
  that you set here available. Environment variables that are
  necessary to start a program in the chosen programming
  language will already be there by default. If you don't know what
  this means you very likely don't have to touch this setting. 

Wizard Step 5: Stdio Redirection
--------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step5.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 5.
   :align: center

In many cases the default values can just leaved as they are. If you don't know
what the standard input and output is you can likely just click **Next**.
   
* Standard Input:
 
  * /dev/null: Your program does not have any input.
  * Pipe: If you choose Pipe you can send input to your program 
    with the Brick Viewer (in the Stdio Redirection section of the
    program tab). Many of our example programs wait for user input
    and only react on callbacks. If your program is of this nature
    you have to select *Pipe* as standard input.
  * File: You can specify a file that will be given to your program as
    input.

* Standard Output:

  * /dev/null: Through output of your program away.
  * File: You can specify a file where the standard output is written to.
  * Individual Log Files: Create a new log file for each execution of
    your program.
  * Continuous Log File: Create one log file that has an entry for each
    execution of your program.

* Standard Error: For error output you can use the same configurations
  as for standard output. Additionally you can redirect the error
  output to the standard output (i.e. they will both be written to the
  same file).


Wizard Step 6: Schedule
-----------------------

.. image:: /Images/Screenshots/red_brick_wizard_step6.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 6.
   :align: center

* Mode *Never*: The scheduler of the RED Brick will not be used. You can
  start your program manually in the program tab of the Brick Viewer.
* Mode *Always*: The scheduler will try to always keep your program running.
  If your program ends it will be restarted immediately. If you have a 
  controlling program that uses some input to control some output that should 
  just always do its thing, this mode is the right one for you.
* Mode *Interval*: Define an interval (in seconds) in which your program 
  should be executed.
* Mode *Cron*: Use `cron <http://en.wikipedia.org/wiki/Cron>`__ to 
  schedule your program. Cron is a *time-based* job scheduler. You can
  specify things like

  * Every day at 20:00: ``00 20 * * *``
  * Every weekday during working hours (6:00-18:00) once per hour: ``00 09-18 * * 1-5``
  * Every minute during the 12th hour of Monday, but only if the day is the 16th of the month: ``* 12 16 * Mon``

  As you can see, you can specify quite complex tasks with cron. There
  is a big number of `cron tutorials <http://www.linuxhelp.net/guides/cron/>`__ 
  available on the internet.

  Please note that your RED Brick needs to have the current time available for
  cron to work. The RED Brick is not equipped with a clock, which is also active
  when the RED Brick is powered down. Such that the time is lost
  after power down. The time will be automatically set if your RED Brick is
  connected to the Internet (through NTP). You can set it in the Date/Time
  section of the settings tab and you can use the GPS Bricklet to 
  `sync the Linux system time with the GPS time <https://github.com/Tinkerforge/red-brick/tree/master/programs/gps_time>`__.

* Mode *Once After Startup*: The scheduler will execute the program only once
  directly after it is uploaded.
* Continue After Error: If this checkbox is unchecked, the scheduler will stop
  after your program exits with an error. If it is checked errors are ignored.

Wizard Step 7: Summary
----------------------

.. image:: /Images/Screenshots/red_brick_wizard_step7.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 7.
   :align: center

The summary page shows a summary of the previous made configuration. If you want
to ask for help regarding the configuration of a program it probably makes 
sense to append the content of this summary to your inquiry.

Wizard Step 8: Upload
---------------------

.. image:: /Images/Screenshots/red_brick_wizard_step8.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 8.
   :align: center

In the last step you can press **Start Upload** to start the upload
of your program files and configuration. Your program will either start
directly after upload or later, depending on the scheduling configurations
in step 6.
