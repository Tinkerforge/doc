
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

* Refresh: Refreshes programs tab
* New: Starts New Program wizward
* Delete: Delets selected program

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
* Langauge: Select the language of your program.
* Description: The description will be shown in the program, if your program
  is selected.
* Unique Identifier: If you uncheck *Auto-generate unique identifier* you will
  have to specify your own identifier. The identifier ist mostly used 
  intenally, you can use your own identifier if you want to have a specfic
  name of the program folder in the underlying Linux.

Wizard Step 2: Files
--------------------

.. image:: /Images/Screenshots/red_brick_wizard_step2.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 2.
   :align: center

* Add files: Adds your program files.
* Add Directory: Adds you program directories.
* Remove: Removes the selected file or directory.

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
select the index.py with *Add file* and then independently select the 
two folders with *Add Directory*.

Every "Add" will add the thing you are selecting to the root directory
of the RED Brick program.

Wizard Step 3: Language Specific Configuration
----------------------------------------------

C/C++
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_c.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (C/C++).
   :align: center

C#
^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_csharp.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (C#).
   :align: center

Delphi/Lazarus
^^^^^^^^^^^^^^
TODO: Screenshot still missing

.. image:: /Images/Screenshots/red_brick_wizard_step3_delphi.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Delphi/Lazarus).
   :align: center

Java
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_java.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Java).
   :align: center

JavaScript (Browser/Node.js)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_javascript.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (JavaScript).
   :align: center

Octave
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_octave.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Octave).
   :align: center

Perl
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_perl.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Perl).
   :align: center

Python
^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_python.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Python).
   :align: center

PHP
^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_php.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (PHP).
   :align: center

Ruby
^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_ruby.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Ruby).
   :align: center

Shell
^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_shell.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Shell).
   :align: center

Visual Basic .NET
^^^^^^^^^^^^^^^^^

.. image:: /Images/Screenshots/red_brick_wizard_step3_vbnet.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 3 (Visual Basic .NET).
   :align: center

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
  necessary to start a standard program in the chosen programming
  language will already be there by default. If you don't know what
  this means you very likely don't have to touch this setting. 

Wizard Step 5: Stdio Redirection
--------------------------------

.. image:: /Images/Screenshots/red_brick_wizard_step5.jpg
   :scale: 60 %
   :alt: Screenshot of RED Brick Wizard Step 5.
   :align: center

If you don't quite understand what any of this means, you can 
likely just leave the default values as they are and click **Next**.

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
  program that uses some input to control some output that should just
  always do its thing, this mode is the right one for you.
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
  cron to work. The time will be automatically set if your RED Brick is
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

The summary page shows a summary of your configuration. If you want to 
ask for help regarding the configuration of a program it probably makes 
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
