
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - IP Connection

.. _ipcon_shell:

Shell - IP Connection
=====================

This is the API description for the Shell bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them. In case of the Shell Bindings all this happens in the background,
invisible to you.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_shell_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/en/source/Software/example.sh>`__

.. literalinclude:: example.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ipcon_shell_api:

API
---

At first some information about the general command structure:

.. sh:function:: X Ntinkerforge A[<option>..] L<command> L[<argument>..]

 :param <command>: string

 The basic command can take several options:

 * ``--help`` shows general help and exits
 * ``--version`` shows version number and exits
 * ``--host <host>`` IP address or hostname, default: ``localhost``
 * ``--port <port>`` port number, default: ``4223``
 * ``--item-separator <item-separator>`` separator for array items, default: ``,`` (comma)
 * ``--group-separator <group-separator>`` separator for output groups, default: ``\n`` (newline)

 All commands, except if the ``--help`` or ``--version`` option is present,
 create a TCP/IP connection to the given *host* and *port*. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 The item separator is used for parsing and formatting arrays. An array with
 three values 1, 2 and 3 is formatted as ``1,2,3``.

 The group separator is used for formatting the output of callbacks. The group
 separator is printed before each callback output with more than one line,
 except before the first one, to separate the output of multiple callback
 invocations. See the section about :ref:`output formatting <ipcon_shell_output>`
 for details.

 There are three subcommands: ``call``, ``dispatch`` and ``enumerate``


.. sh:function:: X Ptinkerforge Ncall A[<option>..] L<device> L<uid> L<function> L[<argument>..]

 :param <device>: string
 :param <uid>: string
 :param <function>: string

 The ``call`` command is used to call a function of a Brick or Bricklet. It can
 take several options:

 * ``--help`` shows help for the ``call`` command and exits
 * ``--list-devices`` shows a list of known devices and exits
 * ``--timeout <timeout>`` maximum time (msec) to wait for response, default:
   ``2500``

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--timeout`` option allows to specify the maximum time in msec for
 waiting for the response of a function call. If a response doesn't arrive
 in time the program exits with an error.

 The ``<uid>`` argument takes a UID corresponding to the selected device type.
 This allows to select a specific device. All connected Bricks and Bricklets
 can be found with the :sh:func:`enumerate <tinkerforge enumerate>` command.

 The ``<function>`` argument allows to specify which function to call. Which
 additional arguments have to be specified depends on the specified device and
 function.


.. sh:function:: X Ptinkerforge Ndispatch A[<option>..] L<device> L<uid> L<callback>

 :param <device>: string
 :param <uid>: string
 :param <callback>: string

 The ``dispatch`` command is used handle incoming callbacks of a Brick or
 Bricklet. It can take several options:

 * ``--help`` shows help for the ``dispatch`` command and exits
 * ``--list-devices`` shows a list of known devices and exits
 * ``--duration <duration>`` time (msec) to dispatch incoming callbacks
   (0: exit after first, -1: forever), default: -1

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--duration`` option allows to specify the time in msec for dispatching
 incoming callbacks.

 The ``<uid>`` argument takes a UID corresponding to the selected device type.
 This allows to select a specific device. All connected Bricks and Bricklets
 can be found with the :sh:func:`enumerate <tinkerforge enumerate>` command.

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
example above contains two groups separated by a blank line.

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
