.. _chibi_extension:

Chibi Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_chibi_tilted_350.jpg",
	               "Extensions/extension_chibi_tilted_600.jpg",
	               "Chibi Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_chibi_tilted_complete_100.jpg",
	             "Extensions/extension_chibi_tilted_complete_600.jpg",
	             "Chibi Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_chibi_top_100.jpg",
	             "Extensions/extension_chibi_top_600.jpg",
	             "Chibi Extension Oberseite")
	}}
	{{
	    tfdocimg("Extensions/extension_chibi_bottom_100.jpg",
	             "Extensions/extension_chibi_bottom_600.jpg",
	             "Chibi Extension Unterseite")
	}}
	{{ tfdocend() }}


Features
--------

* 700/800/900MHz Funk Transceiver
* Erlaubt eine drahtlose Verbindung von Stapeln
* Konfigurierbare Frequenz und Kanal
* Messbare Signalstärke


Beschreibung
------------

Die Chibi Extension ist mit einem 700/800/900MHz Funk Transceiver ausgestattet.
Typischerweise wird dieser für weitreichende `Zigbee
<http://de.wikipedia.org/wiki/ZigBee>`__ Netzwerke eingesetzt.
Leider verbieten es die Zigbee Bedingungen eine GPL Implementierung des Zigbee
Protokoll Stacks (klicke `hier
<http://freaklabs.org/index.php/Blog/Zigbee/Zigbee-Linux-and-the-GPL.html>`__
für weitere Informationen).

Daher haben wir uns dazu entschlossenden den Open Source `Chibi Wireless Stack
<http://freaklabs.org/index.php/Blog/Embedded/Introducing...Chibi-A-Simple-Small-Wireless-stack-for-Open-Hardware-Hackers-and-Enthusiasts.html>`__
für diese Extension zu portieren. Es ist ein einfacher und kleiner Protokoll
Stack der perfekt geeignet ist für unsere Anwendungen.

Bei guten Bedingungen können Reichweiten **bis zu 2km** draußen erreicht werden.

Um ein Chibi Netzwerk aufzubauen sind mindestens zwei Chibi Extensions and zwei
Master Bricks notwendig. Jeder dieser Master Bricks kann in einem Stapel aus
Bricks und Bricklets stecken, wobei einer der Master Bricks per USB und der
andere über eine externe Stromversorgung versorgt wird. Aus Programmierersicht
ist das Chibi Netzwerk vollkommen transparent, d.h. alle Bricks und Bricklets
können genauso benutzt werden als wenn sie einzelnd per USB angeschlossen wären.

Es ist auch möglich ein Netzwerk mit mehr als zwei Chibi Extensions aufzubauen,
wobei immer nur ein Stapel per USB verbunden sein darf (Many-to-One Routing).

.. note::
 Nach der Konfiguration verhalten sich alle Module des Netzwerks als wenn sie
 einzeln per USB mit dem PC verbunden wären. Daher sind keine
 Programmcodeänderungen notwendig. Allerdings ist die
 Übertragungsgeschwindigkeit von USB höher als die von Chibi, so dass mit
 einem geringeren Durchsatz gerechnet werden muss.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    10mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Reichweite (Outdoor)     2km
Maximule Baudrate                 250kbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Gewicht                           13g
================================  ============================================================


Ressourcen
----------

* AT86RF212 Datenblatt (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/datasheets/at86rf212.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/hardware/chibi-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/chibi_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/chibi-extension/zipball/master>`__)


Chibi Network Assembly
----------------------

A Chibi network consists of one master and multiple slaves.
Chibi master is the Master Brick which has a USB connection to the PC
running brickd. All the other Master Bricks with Chibi Extension must not have
a USB connection (they can use a USB power supply since Master Brick firmware
1.1.3). Each Chibi Extension is identified with
its own address. The addresses have to be unique in the transmission range.

.. note::
 If you use multiple networks in parallel with identical channel and
 frequency make sure that every address is unique and not used in different
 networks in transmission range.

To create a Chibi network, stack the Chibi Extension on top of a Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer
software. You should see the Master Brick view
with the identified Chibi Extension (see image below). Configure the extension
as slave or master (as described :ref:`here <chibi_configuration>`).

If you have configured all extensions you can build your system. Connect
Bricks and Bricklets as you like. The Master of each stack has to be the
lowermost Brick (except if you are using a Power Supply). The Chibi Extension
can be positioned in the stack as you wish.

After you have plugged together your system you have to power it up.
You have to power up the slaves before the master, since the Chibi master
searches for slaves only at startup.
You should now be able to see all connected stacks in the Brick Viewer.


.. _chibi_configuration:

Chibi Configuration
^^^^^^^^^^^^^^^^^^^

.. note::
 The Chibi configuration changed starting from Brick Viewer version 1.0.6,
 before this version it was not necessary to specify if the extension
 should be used as master or slave (it was inferred by other means).

 It turns out that this was highly confusing to most, so we recommend that
 you update to the newest Brick Viewer version before you configure your
 Chibi network.

To configure a Chibi Extension you first have to choose a unique
address and a frequency and channel

.. image:: /Images/Extensions/extension_chibi.jpg
   :scale: 100 %
   :alt: Configuration of Chibi address, frequency and channel
   :align: center
   :target: ../../_images/Extensions/extension_chibi.jpg

If you want to configure the extension as slave, you have to choose
"Slave" as type and specify the address of the Chibi master.

.. image:: /Images/Extensions/extension_chibi_slave.jpg
   :scale: 100 %
   :alt: Configuration of Chibi in slave mode
   :align: center
   :target: ../../_images/Extensions/extension_chibi_slave.jpg

If you want to configure the extension as master, you have to choose
"Master" as type and specify a list of the slave addresses the master should
be able to talk to (as a comma separated list).

.. image:: /Images/Extensions/extension_chibi_master.jpg
   :scale: 100 %
   :alt: Configuration of Chibi in master mode
   :align: center
   :target: ../../_images/Extensions/extension_chibi_master.jpg


Modify your Chibi Network
^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to change something in your network, e.g. add new Bricks or
Bricklets, you have to power down the stack you like to change. Change it
and repower it. If the node was a Chibi slave, you also have to reset the
Chibi master (it only searches for new Bricks/Bricklets on startup).
This can be achieved by a power cycle or pressing the reset
button on the Master Brick.


Chibi Frequency and Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Chibi Extension supports several frequencies with different channels
and different frequencies are allowed in different countries.

Here is a small list of frequencies with corresponding possible channels:

.. csv-table::
 :header: "Frequency", "Possible Channels"
 :widths: 40, 60

 "OQPSK 868Mhz (Europe)", "0"
 "OQPSK 915Mhz (US)", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
 "OQPSK 780Mhz (China)", "0, 1, 2, 3"
 "BPSK40 915Mhz", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

.. warning::
 The Chibi Extension is sold as an electronic component. You are building
 a system with this component and it is your responsibility that the
 system you are building abides by your local law. Make sure that you
 are allowed to use the frequency you are configuring!
