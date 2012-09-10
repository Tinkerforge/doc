.. _rs485_extension:

RS485 Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_rs485_tilted_350.jpg",
	               "Extensions/extension_rs485_tilted_600.jpg",
	               "RS485 Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_rs485_top_100.jpg",
	             "Extensions/extension_rs485_top_600.jpg",
	             "RS485 Extension Oberseite")
	}}
	{{
	    tfdocimg("Extensions/extension_rs485_bottom_100.jpg",
	             "Extensions/extension_rs485_bottom_600.jpg",
	             "RS485 Extension Unterseite")
	}}
	{{ tfdocend() }}


Features
--------

* Lange Verbindungen möglich (bis zu 1200m)
* Erlaubt kabelgebundene Verbindungen zwischen Stapeln
* Konfigurierbare Baudrate, Parität und Stop Bits
* Kann in existierendem RS485 Netzwerk genutzt
  werden (:ref:`Modbus RTU <llproto_modbus>`)


Beschreibung
------------

Die RS485 Extension kann für lange kabelgebundene Kommunikation zwischen
Stapeln genutzt werden. Es wird der differentielle RS485 Standard verwendet
um Längen von **bis zu 1200m** zu erreichen.

Für einen RS485 Bus mit Bricks werden zwei RS485 Extension und zwei Master
Bricks benötigt. Beide Master Bricks können mit einem vollen Stapel aus Bricks
und Bricklets verbunden sein. Dabei muss ein Master per USB mit dem PC
verbunden sein. Aus Programmierer-Sicht ist der RS485 Bus vollkommen
transparent, d.h. alle Bricks und Bricklets können genauso benutzt werden
als wenn sie einzeln per USB angeschlossen wären.

Es ist möglich einen Bus mit mehreren RS485 Extension zu betreiben, dabei
muss einer per USB verbunden sein (Many-to-One Routing).

:ref:`Modbus RTU <llproto_modbus>` wird als Protokoll auf der RS485
Schnittstelle genutzt. Dadurch ist es möglich Stapel aus Bricks und Bricklets
mit RS485 Extension in ein vorhandenes Modbus Netwerk zu integrieren. Es ist
auch möglich direkt mit einem Stapel über Modbus zu kommunizieren, z.B. über
ein eingebettetes Gerät oder über einen Modbus Gateway.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    8mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Distanz                  1200m
Maximale Baudrate                 2Mbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Gewicht                           13g
================================  ============================================================


Ressourcen
----------

* ADM3485 Datenblatt (`Download <https://github.com/Tinkerforge/rs485-extension/blob/master/datasheets/ADM3485.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/hardware/rs485-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/rs485_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/rs485-extension>`__)


.. _rs485_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der RS485 Extension.

.. image:: /Images/Extensions/extension_rs485_caption_600.jpg
   :scale: 100 %
   :alt: RS485 Extension mit Beschriftung
   :align: center
   :target: ../../_images/Extensions/extension_rs485_caption_800.jpg


RS485 Busaufbau
---------------

A RS485 bus consists of one master and multiple slaves.
RS485 master is the Master Brick which has a USB connection to the PC
running brickd. All the other Master Bricks with RS485 Extension must not have
a USB connection (they can use a USB Power Supply).
Each RS485 slave is identified with its own ID. The IDs have
to be unique on the bus.

To create a RS485 bus, stack the RS485 Extension on top of a Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer
software. You should see the Master Brick view
with the identified RS485 Extension (see images below). Configure the extension
as slave or master (as described :ref:`here <rs485_configuration>`).

If you have configured all extensions you can build your system. Connect
Bricks and Bricklets as you like. The Master Brick of each stack has to be the
lowermost Brick (except if you are using a Power Supply). The RS485 Extension
can be positioned in the stack as you wish. Wire up the RS485 stacks and set
the termination switch on the first and last RS485 Extension in the bus to
"on", as shown below.

.. image:: /Images/Extensions/extension_rs485_assembly.jpg
   :scale: 90 %
   :alt: RS485 Extension Busaufbau
   :align: center
   :target: ../../_images/Extensions/extension_rs485_assembly.jpg

You have to power up the slaves before the master, since the RS485 master
searches for slaves only at startup. You should now be able to see all
connected stacks in the Brick Viewer.


.. _rs485_configuration:

RS485 Konfiguration
^^^^^^^^^^^^^^^^^^^

To configure a RS485 Extension you first have to choose the baud rate,
parity and stop bits.

.. image:: /Images/Extensions/extension_rs485_config.jpg
   :scale: 100 %
   :alt: RS485 Extension Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_rs485_config.jpg

If your bus isn't absolutely huge you should probably
choose "speed: 2000000 (2Mbit/s), parity: None, Stop bits: 1". If you start to
get timeouts and the CRC error counter is rising rapidly, you might want
to lower the baud rate. If you want to use a stack with RS485 extension in
your existing Modbus network, you have to match the values with the
other bus participants.

For slave configuration choose "Slave" as type and set an address for
the slave (1-255).

.. image:: /Images/Extensions/extension_rs485_slave.jpg
   :scale: 100 %
   :alt: RS485 Konfiguration für Slave Modus
   :align: center
   :target: ../../_images/Extensions/extension_rs485_slave.jpg

For master configuration choose "Master" as type and input the addresses
of the slaves in the RS485 bus as a comma separated list.

.. image:: /Images/Extensions/extension_rs485_master.jpg
   :scale: 100 %
   :alt: RS485 Konfiguration für Master Modus
   :align: center
   :target: ../../_images/Extensions/extension_rs485_master.jpg


RS485 Busmodifikation
^^^^^^^^^^^^^^^^^^^^^

If you want to change something in your bus, e.g. add new Bricks or
Bricklets, you have to power down the stack you would like to change.
Change it and repower it. If the stack was slave in the RS485 bus, you
also have to reset the RS485 master (it only searches for new
Bricks/Bricklets on startup).
This can be achieved by a power cycle or pressing the reset
button on the Master Brick.
