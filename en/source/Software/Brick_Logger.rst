
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / Brick Logger

.. _brick_logger:

Brick Logger
============

The Brick Logger can collect sensor data from Bricks and Bricklets and write
it to a `CSV <https://en.wikipedia.org/wiki/Comma-separated_values>`__ file for
later analysis. Which data from which Bricklet with which interval and with
which options should be collected can be configured.

The Brick Logger is part of Brick Viewer since version 2.3.0 and can be opened
with the "Data Logger" button. From here it can be configured and executed.
There is also a :ref:`standalone version <brick_logger_standalone>` that can be
executed from a terminal.

Configuration
-------------

.. image:: /Images/Screenshots/brick_logger_setup.jpg
   :scale: 100 %
   :alt: Brick Logger (Setup Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_setup.jpg

All logged sensor data and debug messages are timestamped. The time format can
be configured.

By default the sensor data and debug messages are only shown on the "Data" and
"Debug" tabs. Those tabs only show the latest 1000 entries. Additionally, the
data and messages will also be written to files if the corresponding check
boxes are activated.

.. image:: /Images/Screenshots/brick_logger_devices.jpg
   :scale: 100 %
   :alt: Brick Logger (Devices Tab)
   :align: center
   :target: ../_images/Screenshots/brick_logger_devices.jpg

The "Devices" tab allows to configure which sensor data should be collected and
how. First, the UID of the Brick or Bricklet has to be configured. The
"Add Device" dialog will suggest connected devices including their UID.

Each supported device provides at least one loggable sensor value listed in the
"Values" section. By default the interval for each sensor value is set to 0
seconds, which means that the value will not be logged. If the interval is set
to X (with X larger than 0) then the corresponding sensor value is logged every
X seconds.

If the device has options then those are listed in the "Options" section. The
Brick Logger automatically takes care of applying the selected options.

Once the configuration is finished the logging process can be started with
the "Start Logging" button. The logging process continues until it is stopped
with the "Stop Logging" button or by exiting Brick Viewer.

The "Load Config" and "Save Config" buttons can be used to load and save the
current configuration.

.. _brick_logger_standalone:

Standalone
----------

The Brick Logger can also be used outside of Brick Viewer. It is available
as single `Python script
<http://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.zip>`__.
To use it you need to install the :ref:`Python API bindings
<api_bindings_python>` and create and save a configuration in Brick Viewer.
Then you can run it like this (``config.json`` is your manually saved
configuration):

.. code-block:: bash

  python brick-logger.py config.json

RED Brick
^^^^^^^^^

The Brick Logger is also available as `preconfigured RED Brick program
<http://download.tinkerforge.com/tools/brick_logger/brick_logger_latest.tfrba>`__
that you can import. See the :ref:`RED Brick documentation
<red_brick_brickv_import_export_tab>` for details.

After the program got imported the configuration has to be uploaded as
``config.json`` replacing the existing dummy file. Next, the Brick Logger has
to be exited using the "Exit" button in Brick Viewer. The RED Brick will
automatically restart it with the new configuration.

.. image:: /Images/Screenshots/brick_logger_red_brick.jpg
   :scale: 100 %
   :alt: Brick Logger Program on RED Brick
   :align: center
   :target: ../_images/Screenshots/brick_logger_red_brick.jpg
