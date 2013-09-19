
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Starter Kit: Server Room Monitoring</a> / Server Room Monitoring with Nagios or Icinga

.. _starter_kit_server_room_monitoring_nagios_or_icinga:

Server Room Monitoring with Nagios or Icinga
============================================

`Icinga <https://www.icinga.org/>`__ and `Nagios <http://www.nagios.org/>`__ 
are computer system monitoring tools. Icinga is a fork of Nagios and is 
said to be backward compatible to Nagios. In the following examples we are
referring to the Nagios API to be also compatible with Icinga.

Both monitoring tools use plugins, instantiated as services to 
monitor processor load, memory utilization, software processes or physical 
values like temperature. Please refer to the respective documentation for more
information.

Plugins are used to create monitoring services. Plugins are programs with 
defined return codes (e.g. 0=OK, 1=Warning, 2=Critical, 3=Unknown). Their 
standard output is used by Nagios to get information about their state. Please 
refer to the 
`Nagios Developer Guidelines <http://nagiosplug.sourceforge.net/developer-guidelines.html#AEN76>`__
for more information.

After the basic installation of Nagios you can start with the 
development of your own plugin. At first install the 
:ref:`bindings <api_bindings>` for your programming language. Next you can start 
to write your program considering the Nagios Developer Guidelines. 

Basic Nagios/Icinga Script
^^^^^^^^^^^^^^^^^^^^^^^^^^

For this example we use the :ref:`Python Bindings <api_bindings_python>`. 
The script is based on a `Wiki project <http://www.tinkerunity.org/wiki/index.php/EN/Projects/IT_Infrastructure_Monitoring_-_Nagios_Plugin>`__
and uses the a Temperature or PTC Bricklet to measure the temperature
and to warn if high temperatures are detected.

The small script, called ``check_tf_temp.py``, uses the following interface:

.. code-block:: none

 usage: check_tf_temp.py [-h] -u UID -t {temp,ptc} [-H HOST] [-P PORT]
                        [-m {none,high,low,range}] [-w WARNING] [-c CRITICAL]
                        [-w2 WARNING2] [-c2 CRITICAL2]

 optional arguments:
  -h, --help            show this help message and exit
  -u UID, --uid UID     UID from Temperature Bricklet
  -t {temp,ptc}, --type {temp,ptc}
                        Type: temp = Temperature Bricklet, ptc = PTC Bricklet
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


Most of the interface should be self-explanatory. It supports three modes:

* ``high``: Message is raised if measured temperature is above WARNING or CRITICAL
* ``low``: Message is raised if measured temperature is below WARNING or CRITICAL
* ``range``: Message is raised if measured temperature is above WARNING or CRITICAL or below WARNING2 or CRITICAL2

Make the script globally executable, e.g. store it under ``/usr/local/bin``.

The following example connects to the Ethernet Extension with hostname 
``ServerMonitoring`` and to the Temperature Bricklet with UID ``SCT31``. It creates 
a warning if the temperature is above 26°C and a critical message if the
temperature is above 27°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m high -w 26 -c 27


The following example creates a warning if the temperature is below 10°C or above
30°C and a critical message if the temperature is below 8°C or above 35°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m range -w 10 -w2 30 -c 8 -c2 35

To use the same function with the PTC Bricklet instead of the Temperature 
Bricklet we have to change the UID and the type of the Bricklet. The command
will then look like this:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u fow -t ptc -m range -w 10 -w2 30 -c 8 -c2 35


The ``check_tf_temp.py`` script is small and is easy to adapted for other
Tinkerforge sensors. The ``read`` method is the main part of the script. It reads
out the Bricklet and compares the measured temperature with
the warning and critical thresholds and generates the necessary message and 
return value.

.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp.py
 :language: python
 :tab-width: 4

To run this script with Nagios you have to register it. To do this you have
to register the command with the following lines in a commands config file
(e.g. ``/usr/local/nagios/etc/checkcommands.cfg`` or ``/etc/icinga/commands.cfg``):

.. code-block:: none

 define command {
     command_name    check_tf_temp
     command_line /usr/local/bin/check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m high -w 26 -c 27
 }

After the command is known to Nagios it can be used by a service.
To register a new service you can add the following lines to a service
config file:

.. code-block:: none

 define service {
     use                             generic-service
     host_name                       localhost
     service_description             Check Temperature
     check_command                   check_tf_temp
     check_interval                  1
 }

Possible config file locations are ``/usr/local/nagios/etc/services.cfg`` 
``/etc/icinga/objects/services_icinga.cfg`` or other. The respective documentation
should give more information.

That's it. You should see a new service in the web interface and should be
warned if the ambient temperature is too hot.

.. image:: /Images/Kits/server_room_monitoring_icinga_screenshot_350.jpg
   :scale: 100 %
   :alt: Icinga Screenshot
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_icinga_screenshot_orig.jpg
