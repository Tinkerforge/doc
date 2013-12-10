
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Starterkit: Serverraum-Überwachung</a> / Erweitertes Nagios Beispiel

.. _starter_kit_server_room_monitoring_extended_nagios:

Erweitertes Nagios Beispiel
===========================

Dieses Beispiel basiert auf dem
:ref:`Nagios/Icinga Projekt <starter_kit_server_room_monitoring_nagios_or_icinga>`.
Es erweitert dieses um die Möglichkeit einen Fehlerzustand anzuzeigen und
Bewegung im Serverraum zu detektieren. Hierzu wird ein 
:ref:`Motion Detector Bricklet <motion_detector_bricklet>`
und ein :ref:`Segment Display 4x7 Bricklet <segment_display_4x7_bricklet>` 
genutzt. Das Skript kann als Startpunkt für eigene Entwicklungen dienen.

Erweitertes Skript
^^^^^^^^^^^^^^^^^^

Dieses kleine Skript, genannt *check_tf_temp_ext.py*, besitzt die folgende Schnittstelle:

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

Die Schnittstelle ist im Vergleich zu dem *check_tf_temp.py* Skript erweitert.
Ein "Err" kann auf das Segment Display 4x7 Bricklet mittels


.. code-block:: bash

 python check_tf_temp_ext.py -u 9VU -H ServerMonitoring -t segment_display_4x7 -e true

geschrieben werden. Entfernt wird dieses mittels:

.. code-block:: bash

 python check_tf_temp_ext.py -u 9VU -H ServerMonitoring -t segment_display_4x7 -e false

Mit dem Motion Detector Bricklet können Bewegungen im Serverraum detektiert 
werden. Diese Information erhält man mittels:

.. code-block:: bash

 python check_tf_temp_ext.py -H ServerMonitoring -u abc -t motion_detector

Das gesamte Skript sieht wie folgt aus:

(`download <https://raw.github.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp_ext.py>`__)

.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp_ext.py
 :language: python
 :tab-width: 4
