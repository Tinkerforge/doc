
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Starter Kit: Server Room Monitoring</a> / Server Room Monitoring with Nagios or Icinga

.. _starter_kit_server_room_monitoring_server_room_monitoring_with_nagios_or_icinga:

Server Room Monitoring with Nagios or Icinga
============================================
`Icinga <https://www.icinga.org/>`__ and `Nagios <http://www.nagios.org/>`__ 
are computer system monitoring tools, whereis Icinga is a fork of Nagios and is 
said to be backward compatible to Nagios. So we refering in the following 
examples to the Nagios API to be also compatible with Icinga.

These monitoring tools use so called plugins, instantiated as services to 
monitor processor load, memory utilization, software processes or physical 
values like temperature. Please refer to the respective documentation for more
information.

To create these monitoring services plugins are used. Plugins are programs with 
defined return codes (e.g. 0=OK, 1=Warning, 2=Critical, 3=Unknown). Their 
standard output is used by Nagios to get information about their state. Please 
refer to the 
`Nagios Developer Guidelines <http://nagiosplug.sourceforge.net/developer-guidelines.html#AEN76>`__
for more information.

After the basic installation of Nagios we can start with the 
development of your own plugin. At first install the 
:ref:`bindings<api_bindings>` for your programming language. Next you can start 
to write your program considering the Nagios Developer Guidelines. 

For this example we have used the :ref:`Python Bindings <api_bindings_python>`. 
The program is based on a `Wiki project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/IT_Infrastructure_Monitoring_-_Nagios_Plugin>`__
and uses the installed Temperature Bricklet to measure the ambient temperature
and to warn for high temperatures.

The small script, called *check_tf_temp.py*, uses the following interface:

.. code-block:: none

 usage: check_tf_temp [-h] -u UID [-H HOST] [-P PORT] [-m MODUS]
                             [-w WARNING] [-c CRITICAL] [-w2 WARNING2]
                             [-c2 CRITICAL2]
 
 Checks temperature
 
 optional arguments:
  -h, --help            show this help message and exit
  -u UID, --uid UID     UID from Temperature Bricklet
  -H HOST, --host HOST  Host Server (brickd, default=localhost)
  -P PORT, --port PORT  Port (default=4223)
  -m MODUS, --modus MODUS
                        Modus: high (default), low or range
  -w WARNING, --waring WARNING
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

Most of the interface should be self-explanatory. It supports three modes:

 * ``high``: Message is raised if measured temperature is above WARNING or CRITICAL
 * ``low``: Message is raised if measured temperature is below WARNING or CRITICAL
 * ``range``: Message is raised if measured temperature is above WARNING or CRITICAL or below WARNING2 or CRITICAL2

We make this script globally executable, e.g. store it under /usr/local/bin.

The following example connects to the Ethernet Extension with hostname 
ServerMonitoring and to the Temperature Bricklet with UID SCT31. It creates a 
warning if temperature above 26°C and a critical message if temperature is 
above 27°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -m high -w 26 -c 27


The following example creates a warning if temperature is below 10°C or above
30°C and a critical message if temperature is below 8°C or above 35°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -m range -w 10 -w2 30 -c 8 -c2 35


The *check_tf_temp.py* script is small and can be easily adapted for other
Tinkerforge sensors. The *read* method is the main part of the script. It reads
out the Temperature Bricklet and compares the measured temperature with
the warning and critical thresholds and generate the necessary message and 
return value.

.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp.py
 :language: python
 :tab-width: 4

To run this script with Nagios you have to register it. To do this you have
to register the command with the following lines in a config file:

.. code-block:: none

 define command {
     command_name    check_tf_temp
     command_line /usr/local/bin/check_tf_temp.py -H ServerMonitoring -u SCT31 -m high -w 26 -c 27
 }

And register the service the follogin lines:

.. code-block:: none

 define service {
     use                             generic-service
     host_name                       localhost
     service_description             Check Temperature
     check_command                   check_tf_temp
     check_interval                  1
 }

That's it. You should see a new service in the web interface and should be
warned if the ambient temperature get's to hot.
