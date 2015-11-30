
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/ServerRoomMonitoring/ServerRoomMonitoring.html">Startekit: Serverraum-Überwachung</a> / Serverraum-Überwachung mit Nagios oder Icinga

.. _starter_kit_server_room_monitoring_nagios_or_icinga:

Serverraum-Überwachung mit Nagios oder Icinga
=============================================

`Icinga <https://www.icinga.org/>`__ und `Nagios <https://www.nagios.org/>`__
sind Computer Überwachungswerkzeuge. Icinga ist ein Fork von Nagios und gilt
als rückwärtskompatibel zu diesem. Die nachfolgenden Beispielen beziehen
sich auf die Nagios API sind daher aber auch kompatibel zu Icinga.

Beide Überwachungswerkzeuge nutzen Plugins, instantiiert als Services,
um die Prozessorauslastung, Speicherbelegung, spezielle Software Prozesse oder
physikalische Werte, wie die Temperatur, zu überwachen. Die jeweilige 
Dokumentation gibt hier weitere Informationen.

Plugins werden genutzt um überwachende Services zu erzeugen. Dies sind 
Programme mit einem definierten Rückgabewert (z.B. 0=OK, 1=Warning, 2=Critical, 
3=Unknown). Deren Standardausgabe wird von Nagios genutzt um Informationen
über deren Zustand zu bekommen. Die
`Nagios Developer Guidelines <https://nagios-plugins.org/doc/guidelines.html>`__
geben hier weitere Auskünfte.

Nach der Grundinstallation von Nagios kann damit begonnen werden ein eigens
Plugin zu entwickeln. Als erstes sollten die 
:ref:`Bindings <api_bindings>` für die gewünschte Programmiersprache
installiert werden. Anschließend kann das eigene Plugin unter Beachtung der
Nagios Developer Guidelines geschrieben werden.

Basis Nagios/Icinga Skript
^^^^^^^^^^^^^^^^^^^^^^^^^^

Für dieses Beispiel nutzen wir die :ref:`Python Bindings <api_bindings_python>`. 
Das `Skript <https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp.py>`__
basiert auf einem
`Wiki Projekt <http://www.tinkerunity.org/wiki/index.php/EN/Projects/IT_Infrastructure_Monitoring_-_Nagios_Plugin>`__
und nutzt das Temperature oder PTC Bricklet um die Temperatur zu messen und zu
warnen falls zu hohe Temperaturen gemessen werden.

Das kleine Skript, ``check_tf_temp.py`` genannt, besitzt folgende Schnittstelle:

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

Der Großteil der Schnittstelle sollte selbsterklärend sein. Diese unterstützt
drei Modi:

* ``high``: Nachricht wird abgegeben wenn die gemessene Temperatur über WARNING oder CRITICAL liegt
* ``low``: Nachricht wird abgegeben wenn die gemessene Temperatur unter WARNING oder CRITICAL liegt
* ``range``: Nachricht wird abgegeben falls die Temperatur über WARNING oder CRITICAL der unter WARNING2 oder CRITICAL2 liegt

Das Skript sollte global ausführbar sein, z.B. durch speichern unter ``/usr/local/bin``.

Das folgende Beispiel verbindet zu einer Ethernet Extension mit dem Hostnamen
``ServerMonitoring`` und zu einem Temperature Bricklet mit der UID ``SCT31``. Eine
Warning Nachricht wird bei Temperaturen über 26°C abgegeben und eine Critical 
Nachricht bei Temperaturen über 27°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m high -w 26 -c 27

Das folgende Beispiel erzeugt ein Warning bei Temperaturen unter 10°C oder über 
30°C und Critical Nachrichten bei Temperaturen unter 8°C und über 35°C:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m range -w 10 -w2 30 -c 8 -c2 35

Um diese Funktion mit einem PTC Bricklet anstatt mit dem Temperature Bricklet zu
nutzen muss die UID und der Typ des Bricklets entsprechend angepasst werden.
Das Kommando sieht dann wie folgt aus:

.. code-block:: bash

 check_tf_temp.py -H ServerMonitoring -u fow -t ptc -m range -w 10 -w2 30 -c 8 -c2 35

Das ``check_tf_temp.py`` Skript kann einfach an andere Tinkerforge Sensoren 
angepasst werden. Die ``read`` Methode ist der Hauptteil des Skripts. Diese liest
das Bricklet aus und vergleicht die gemessene Temperatur mit den Warning
und Critical Grenzwerten. Falls notwendig generiert sie eine Meldung und
den dazu passenden Rückgabewert. Das gesamte Skript sieht wie folgt aus (`download
<https://raw.githubusercontent.com/Tinkerforge/server-room-monitoring/master/nagios_icinga/check_tf_temp_ext.py>`__):

.. literalinclude:: ../../../../../server-room-monitoring/nagios_icinga/check_tf_temp.py
 :language: python
 :tab-width: 4

Um das Skript mit Nagios auszuführen muss es zuerst registriert werden.
Dazu wird dieses mit den folgenden Zeilen in einer Command Konfigurationsdatei
(z.B. ``/usr/local/nagios/etc/checkcommands.cfg`` oder ``/etc/icinga/commands.cfg``)
registriert:

.. code-block:: none

 define command {
     command_name    check_tf_temp
     command_line    /usr/local/bin/check_tf_temp.py -H ServerMonitoring -u SCT31 -t temp -m high -w 26 -c 27
 }

Anschließend kann dieses Kommando einem Service zugeordnet werden. Ein neuer
Service kann in eine Service Konfigurationsdatei mit den folgenden Zeilen:

.. code-block:: none

 define service {
     use                             generic-service
     host_name                       localhost
     service_description             Check Temperature
     check_command                   check_tf_temp
     check_interval                  1
 }

erzeugt werden. Mögliche Konfigurationsdateien befinden sich unter
``/usr/local/nagios/etc/services.cfg``, ``/etc/icinga/objects/services_icinga.cfg``
oder an anderen Positionen. Die jeweilige Dokumentation gibt hier Aufschluss.

Das war es. Es sollte ein neuer Service im Web-Interface angezeigt werden,
der vor zu hohen Temperaturen warnt.

.. image:: /Images/Kits/server_room_monitoring_icinga_screenshot_350.jpg
   :scale: 100 %
   :alt: Icinga Screenshot
   :align: center
   :target: ../../_images/Kits/server_room_monitoring_icinga_screenshot_orig.jpg
