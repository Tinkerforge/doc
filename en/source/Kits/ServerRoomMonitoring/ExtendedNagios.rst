
.. _starter_kit_server_room_monitoring_extended_nagios:

Extended Nagios Example
=======================

This example is an extended version of the 
:ref:`Nagios/Icinga project <starter_kit_server_room_monitoring_nagios_or_icinga>`.
It is extended by the usage of a 
:ref:`Motion Detector Bricklet <motion_detector_bricklet>` and a 
:ref:`Segment Display 4x7 Bricklet <segment_display_4x7_bricklet>`.

With the extended script you can display if there is an error occurred
and can detect motion in the server room. The script can be used as a starting
point for your own projects.

Extended Script
^^^^^^^^^^^^^^^

The small script, called ``check_tf_temp_ext.py``, uses the following interface:

.. code-block:: none

 usage: check_tf_temp_ext.py [-h] -u UID
                             -t {temp,ptc,humidity,motion_detector,segment_display_4x7}
                             [-H HOST] [-P PORT] [-m {none,high,low,range}]
                             [-w WARNING] [-c CRITICAL] [-w2 WARNING2]
                             [-c2 CRITICAL2] [-e {true,false}]

 optional arguments:
  -h, --help            show this help message and exit
  -u UID, --uid UID     UID from Bricklet
  -t {temp,ptc,humidity,motion_detector,segment_display_4x7},
  --type {temp,ptc,humidity,motion_detector,segment_display_4x7,humidity}
                        Choose fitting type for your Bricklet
  -H HOST, --host HOST  Host Server (default=localhost)
  -P PORT, --port PORT  Port (default=4223)
  -m {none,high,low,range}, --modus {none,high,low,range}
                        Modus: none (default, only print temperature), high,
                        low or range
  -w WARNING, --warning WARNING
                        Warning temperature level (temperatures above this
                        level will trigger a warning message in high mode,
                        temperature below this level will trigger a warning
                        message in low mode)
  -c CRITICAL, --critical CRITICAL
                        Critical temperature level (temperatures above this
                        level will trigger a critical message in high mode,
                        temperature below this level will trigger a critical
                        message in low mode)
  -w2 WARNING2, --warning2 WARNING2
                        Warning temperature level (temperatures below this
                        level will trigger a warning message in range mode)
  -c2 CRITICAL2, --critical2 CRITICAL2
                        Critical temperature level (temperatures below this
                        level will trigger a critical message in range mode)
  -e {true,false}, --error {true,false}
                        Set Error Message on 4x7 Segment On/Off

The interface is extended in comparison to the ``check_tf_temp.py`` script.

You can write "Err" on the Segment Display 4x7 Bricklet by

.. code-block:: bash

 python check_tf_temp_ext.py -u 9VU -H ServerMonitoring -t segment_display_4x7 -e true

and disable it with

.. code-block:: bash

 python check_tf_temp_ext.py -u 9VU -H ServerMonitoring -t segment_display_4x7 -e false

With the Motion Detector Bricklet you can get information if motion was detected 
by running

.. code-block:: bash

 python check_tf_temp_ext.py -H ServerMonitoring -u abc -t motion_detector

The full script looks like this (`download
<https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp_ext.py>`__):

.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp_ext.py
 :language: python
 :tab-width: 4
