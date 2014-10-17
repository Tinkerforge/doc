
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RED Brick
:FIXME_shoplink: ../../../shop/bricks/red-brick.html

.. include:: RED_Brick.substitutions


.. _red_brick:

RED Brick
=========

.. note::
 This Brick is under development and not yet available. 

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_red_prototype_350.jpg",
	               "Bricks/brick_red_prototype_600.jpg",
	               "RED Brick Prototype")
	}}
	{{ tfdocend() }}


Features
--------

* Controls other Bricks and Bricklets
* Executes directly your program
* Supports nearly every language

.. _red_brick_description:

Description
-----------

.. note::
 This Brick is under development and not yet available. Planned release: Dec. 2014. 

 You can find news in our `blog <http://www.tinkerforge.com/en/blog/>`__.  Blog posts so far:

 * `Tinkerforge goes Stand-Alone aka RED Brick <http://www.tinkerforge.com/en/blog/2014/2/21/tinkerforge-goes-stand-alone-aka-red-brick>`__
 * `RED Brick circuit boards arrived <http://www.tinkerforge.com/en/blog/2014/4/10/red-brick-circuit-boards-arrived>`__
 * `RED Brick news <http://www.tinkerforge.com/en/blog/2014/5/13/red-brick-news>`__
 * `RED Brick: Does it work? <http://www.tinkerforge.com/en/blog/2014/5/23/red-brick:-does-it-work>`__
 * `RED Brick Software Infrastructure <http://www.tinkerforge.com/en/blog/2014/6/20/red-brick-software-infrastructure>`__
 * `RED Brick in EMC laboratory <http://www.tinkerforge.com/en/blog/2014/8/28/red-brick-in-emc-laboratory>`__
 * `RED Brick status report <http://www.tinkerforge.com/en/blog/2014/10/16/red-brick-status-report>`__

The Rapid Embedded Development Brick (RED Brick) can control other
Bricks and Bricklets. Currently supported languages as: C/C++, C#, 
Delphi/Lazarus, Java, JavaScript, MATLAB/Octave, Perl, PHP, Python, Ruby, Shell 
and Visual Basic .NET can be directly executed on the Brick.

A program that controls Bricks and Bricklets can be written and tested 
on a normal PC/Mac. Afterwards the program can be transferred to the RED Brick
by the press of a button and can be executed without any changes. Multiple 
programs can be executed simultaneously, whereas their execution can be 
configurated (permanently execution, every X seconds etc.) and monitored.

This approach enables a very easy and very fast solution for embedded 
programming. To our knowledge there is no other solution available that is
even remotely comparable. 

For each supported programming language the Tinkerforge API and commonly used 
software libraries are preinstalled on the system. Other necessary libraries can 
be manually installed.

The Brick is equipped with a Micro-HDMI connector, such that it can also used 
for programs with graphical user interface. A onboard USB 2.0 Host connector 
supports input and pointing devices, such that keyboards, mouses or touchscreens 
can be also connected and used.

With an Ethernet Master Extension the RED Brick can be extended by an Ethernet 
interface. The RS485 Master Extension is also supported by the Brick and let you 
interconnect the controlling RED Brick with other remote stacks of Bricks and 
Bricklets.

Advanced users can use the module with full access on the underlying Debian 
system. Over a GPIO FPC header, the export user can directly access 
different processor pins and can use them in his own developments.




Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (W x D x H)            40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                            TBD g
Current Consumption               TBD mA
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/red-brick/raw/master/hardware/red-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/red_brick_dimensions.png>`__)
* Linux image and hardware design files (`Download <https://github.com/Tinkerforge/red-brick/zipball/master>`__)

FAQ
---

* Q: I connected the RED Brick to my Linux PC. Why is there no ``/dev/ttyACM0``
  device to access its serial console?
* A: The ``cdc_acm`` driver has to be loaded for this to work.


.. _red_brick_hardware:

Hardware Description
--------------------
TODO: Image of each part in each section

Power Button
^^^^^^^^^^^^

LEDs
^^^^

TODO: Image of RED Brick with arrows to LEDs

The RED Brick has a blue, a red and a green LED.

The blue LED is directly connected to the power supply and is on if the 
RED Brick is powered.

The red LED shows if an error is present. If the red LED stays on during
startup, no image could be found. There may be no sd card inserted or 
there is no valid image on the sd card.

The green LED shows the current state. If on startup the red LED is off
and the green LED does not turn on, Linux couldn't start booting. During
boottime the green LED turns on. After the RED Brick has booted up
and all of the services are available the green led starts showing a
heartbeat.

You can change the function of the green LED after bootup to `show
cpu or sd card usage <TODO>`__ instead of a heartbeat.

SD Card Slot
^^^^^^^^^^^^
TODO: Link images

USB 2.0 Host Connector
^^^^^^^^^^^^^^^^^^^^^^
TODO: what kind of devices are usable?

USB Mini Connector
^^^^^^^^^^^^^^^^^^
TODO: used for configuration

Micro-HDMI Connector
^^^^^^^^^^^^^^^^^^^^

Brick Stack Connector
^^^^^^^^^^^^^^^^^^^^^


RED Brick Software Images
-------------------------

Im Hintergrund läuft ein von uns angepasstes Debian Image. Dieses ist in zwei 
Versionen verfügbar. Das Full Image TODO. Das TODO Image.

Full Image
^^^^^^^^^^

X Image
^^^^^^^

Configuration (in Brick Viewer)
-------------------------------
TODO: Describe configuration in Brick Viewer

Program Upload and Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO: Link to Tutorial

Ethernet
^^^^^^^^

RS485
^^^^^




.. _red_brick_test:

Test your RED Brick
-------------------

.. _red_brick_leds:

.. _red_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RED_Brick_hlpi.table
