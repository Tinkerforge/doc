
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Starter Kit: Server Room Monitoring</a> / Server Room Monitoring with Nagios or Icinga

.. _starter_kit_server_room_monitoring_extended_nagios:

Motion Detector and Error Code Display
======================================

`Icinga <https://www.icinga.org/>`__ and `Nagios <http://www.nagios.org/>`__ 
are computer system monitoring tools. Icinga is a fork of Nagios and is 
said to be backward compatible to Nagios. In the following example we are
reffering to the Nagios API to be also compatible with Icinga.

We extend the script introduced in the basic 
:ref:`Nagios/Icinga project <starter_kit_server_room_monitoring_nagios_or_icinga>`
by the Motion Detector Bricklet and the Segment Display 4x7 Bricklet.

Extended Script
^^^^^^^^^^^^^^^

The small script, called *check_tf_temp_ext.py*, uses the following interface:

.. code-block:: none

 usage: check_tf_temp_ext.py [-h] -u UID -t
                            {temp,ptc,motion_detector,segment_display_4x7}
                            [-H HOST] [-P PORT] [-m {none,high,low,range}]
                            [-w WARNING] [-c CRITICAL] [-w2 WARNING2]
                            [-c2 CRITICAL2] [-e {true,false}]

 optional arguments:
  -h, --help            show this help message and exit
  -u UID, --uid UID     UID from Bricklet
  -t {temp,ptc,motion_detector,segment_display_4x7}, --type {temp,ptc,motion_detector,segment_display_4x7}
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

The interface is extended in comparison to the *check_tf_temp.py* script.

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


The full script looks like this:


.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp_ext.py
 :language: python
 :tab-width: 4
