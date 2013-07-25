
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - IP Connection

.. _ipcon_shell:

Shell - IP Connection
=====================

Dies ist die API Beschreibung für die Shell Bindings der IP Connection.
Die IP Connection wird zwischen dem Brick Daemon und den API Bindings der
entsprechenden Programmiersprache hergestellt. Bevor Geräte über deren API
angesprochen werden können muss eine IP Connection zu brickd erzeugt und die
Geräte dieser hinzugefügt werden. Im Falle der Shell Bindings passiert dies
alles im Hintergrund, unsichtbar für den Benutzer.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.


.. _ipcon_shell_examples:

Beispiel
--------

Der folgende Beispielcode ist Public Domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/de/source/Software/example.sh>`__

.. literalinclude:: example.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ipcon_shell_api:

API
---

Als erstes einige Information über die allgemeine Struktur der Befehle:

.. sh:function:: X Ntinkerforge A[<option>..] L<command> L[<argument>..]

 :param <command>: string

 Der Grundbefehl kennt mehrere Optionen:

 * ``--help`` zeigt allgemeine Hilfe an und endet dann
 * ``--version`` zeigt die Versionsnummer an und endet dann
 * ``--host <host>`` IP Adresse oder Hostname, Standard: ``localhost``
 * ``--port <port>`` Port-Nummer, Standard: ``4223``
 * ``--item-separator <item-separator>`` Trennzeichen für Array-Einträge,
   Standard: ``,`` (Komma)
 * ``--group-separator <group-separator>`` Trennzeichen für Ausgabegruppen,
   Standard: ``\n`` (neue Zeile)

 Alle Befehle, außer die ``--help`` oder ``--version`` Option sind angegeben,
 erstellen eine TCP/IP Verbindung zum gegebenen *host* und *port*. Host und Port
 können auf einen Brick Daemon oder eine WIFI/Ethernet Extension verweisen.

 Das Trennzeichen für Array-Einträge wird beim Parse und Formatieren von Arrays
 verwendet. Ein Array mit den drei Werten 1, 2 und 3 wird als ``1,2,3``
 formatiert.

 Das Trennzeichen für Ausgabegruppen wird beim Formatieren der Ausgabe von
 Callbacks verwendet. Das Trennzeichen wird vor jeder Callback-Ausgabe mit mehr
 als einer Zeile ausgegeben, außer der ersten, um die Ausgabe von mehreren
 Callback-Aufrufen zu trennen. Siehe den Abschnitt über
 :ref:`Ausgabeformatierung <ipcon_shell_output>` für mehr Details.

 Es gibt drei Unterbefehle: ``call``, ``dispatch`` und ``enumerate``


.. sh:function:: X Ptinkerforge Ncall A[<option>..] L<device> L<uid> L<function> L[<argument>..]

 :param <device>: string
 :param <uid>: string
 :param <function>: string

 Der ``call`` Befehl wird verwendet um eine Funktion eines Bricks oder Bricklets
 aufzurufen. Der Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den spezifischen ``call`` Befehl an und endet dann
 * ``--list-devices`` zeigt eine Liste der bekannten Geräte an und enden dann
 * ``--timeout <timeout>`` maximum time (msec) to wait for response, default:
   ``2500``

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--timeout`` option allows to specifiy the maximum time in msec for
 waiting for the response of a function call. If a response doesn't arrive
 in time the program exits with an error.

 The ``<uid>`` argument takes a UID corresponding to the selected device type.
 This allows to select a specific device.

 The ``<function>`` argument allows to specify which function to call. Which
 additonal arguments have to be specified depends on the specified device and
 function.


.. sh:function:: X Ptinkerforge Ndispatch A[<option>..] L<device> L<uid> L<callback>

 :param <device>: string
 :param <uid>: string
 :param <callback>: string

 Der ``dispatch`` Befehl wird verwendet um eingehende Callbacks eines Brick oder
 Bricklet abzufertigen. Der Befehl kennt mehrere Optionen:

 * ``--help`` zeigt Hilfe für den spezifischen ``dispatch`` Befehl an und endet
   dann
 * ``--list-devices`` zeigt eine Liste der bekannten Geräte an und enden dann
 * ``--duration <duration>`` time (msec) to dispatch incoming callbacks
   (0: exit after first, -1: forever), default: -1

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--duration`` option allows to specifiy the time in msec for dispatching
 incoming callbacks.

 The ``<uid>`` argument takes a UID corresponding to the selected device type.
 This allows to select a specific device.

 The ``<callback>`` argument allows to specify which callback to dispatch.


Basic Functions
^^^^^^^^^^^^^^^

.. sh:function:: X Ptinkerforge Nenumerate A[<option>..]

 :returns uid: string
 :returns connected-uid: string
 :returns position: char
 :returns hardware-version: int,int,int
 :returns firmware-version: int,int,int
 :returns device-identifier: string

 The ``enumerate`` command is used to discover the connected Bricks and
 Bricklets. It can take several options:

 * ``--help`` shows help for the ``enumerate`` command and exits
 * ``--duration <duration>`` time (msec) to dispatch incoming responses (0: exit
   after first, -1: forever), default: 250
 * ``--execute <command>`` shell command to execute for each incoming response

 The ``--duration`` option allows to specifiy the time in msec for dispatch
 incoming enumerate responses.

 The ``--execute`` option allows for advanced output formatting. See the
 :ref:`section about this <ipcon_shell_output>` for details.

 The command has six outputs:

 * ``uid`` is the UID of the device.
 * ``connected-uid`` is the UID where the device is connected to. For a Bricklet
   this will be a UID of the Brick where it is connected to. For a Brick it will
   be the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "1". With this information it is possible to
   reconstruct the complete network topology.
 * ``position`` is position in stack (0 - 8) for Bricks or the position on
   Brick (a - d) for Bricklets.
 * ``hardware-version`` is in major, minor and release format.
 * ``firmware-version`` is in major, minor and release format.
 * ``device-identifier`` is the name of the device as known from the
   ``--list-devices`` option of the ``call`` and ``dispatch`` commands.

.. _ipcon_shell_output:

Output Formatting
^^^^^^^^^^^^^^^^^

By default the output of getters and callbacks is printed in ``<key>=<value>``
format. For example, the output of an enumerate callback:

.. code-block:: bash

    $ tinkerforge enumerate
    uid=68yjBL
    connected-uid=0
    position=0
    hardware-version=1,0,0
    firmware-version=2,0,6
    device-identifier=master-brick

    uid=eN3
    connected-uid=68yjBL
    position=a
    hardware-version=1,1,0
    firmware-version=2,0,0
    device-identifier=distance-ir-bricklet


The ``--item-separator`` option affects how arrays are formatted and the
``--group-separator`` option affects how output groups are formatted. The
example above contains two groups seperated by a blank line.

Advanced Options
""""""""""""""""

For more advanced output formatting all getter functions and callbacks support
the ``--execute`` option. It takes a shell command line with placeholders to be
executed for each incoming response.

A simple example: getting the current distance in mm of a Distance IR Bricklet
in ``<key>=<value>`` format:

.. code-block:: bash

    $ tinkerforge call distance-ir-bricklet eN3 get-distance
    distance=473

Now the ``--execute`` option is used for advanced formatting with ``bc`` and
``printf``:

.. code-block:: bash

    $ tinkerforge call distance-ir-bricklet eN3 get-distance --execute "echo 'scale=2; {distance} / 10' | bc | xargs printf 'current distance is %.1fcm\n'"
    current distance is 46.3cm

Before the command line is executed the contained placeholders are replaced with
the actual values. In the example above a call to ``get-distance`` without
``--execute`` outputs a single line with key ``distance``. This key is also the
placeholder for ``--execute`` usage wrapped in curly brackets: ``{distance}``.
