
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
 * ``--no-symbolic-input`` disables symbolic input of values
 * ``--no-symbolic-output`` disables symbolic output of values

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

 By default symbolic input and output is enabled. For example, the
 :sh:func:`set-i2c-mode <temperature-bricklet set-i2c-mode>` function of the
 Temperature Bricklet can take two different values: 0 and 1. With symbolic
 input enabled there are also two symbols ``fast`` (0) and ``slow`` (1) for
 this values. The same holds for the :sh:func:`get-i2c-mode
 <temperature-bricklet get-i2c-mode>` function: the same two symbols are used
 for symbolic output, if enabled.

 There are three subcommands: ``call``, ``dispatch`` and ``enumerate``


.. sh:function:: X Ptinkerforge Ncall A[<option>..] L<device> L<uid> L<function> L[<argument>..]

 :param <device>: string
 :param <uid>: string
 :param <function>: string

 The ``call`` command is used to call a function of a Brick or Bricklet. It can
 take several options:

 * ``--help`` shows help for the ``call`` command and exits
 * ``--list-devices`` shows a list of known devices and exits
 * ``--timeout <timeout>`` maximum time (ms) to wait for response, default:
   ``2500``

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--timeout`` option allows to specify the maximum time in ms for
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
 * ``--duration <duration>`` time (ms) to dispatch incoming callbacks
   (0: exit after first, -1: forever), default: -1

 If the ``--list-devices`` option is present all valid device names for the
 ``<device>`` argument are listed. For example ``master-brick`` and
 ``ambient-light-bricklet``.

 The ``--duration`` option allows to specify the time in ms for dispatching
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
 :returns device-identifier: int (has symbols)
 :returns enumeration-type: int (has symbols)

 The ``enumerate`` command is used to discover the connected Bricks and
 Bricklets. It can take several options:

 * ``--help`` shows help for the ``enumerate`` command and exits
 * ``--duration <duration>`` time (ms) to dispatch incoming responses (0: exit
   after first, -1: forever), default: 250
 * ``--types <types>`` array of enumeration types to dispatch, default:
   ``available``
 * ``--execute <command>`` shell command to execute for each incoming response

 The ``--duration`` option allows to specify the time in ms for dispatch
 incoming enumerate responses.

 The ``--types`` option allows to specify which types of enumerate callbacks
 to dispatch. By default only enuemrate callbacks with
 ``enumeration-type=available`` are dispatched.

 The ``--execute`` option allows for advanced output formatting. See the
 :ref:`section about this <ipcon_shell_output>` for details.

 The command has six outputs:

 * ``uid`` is the UID of the device.
 * ``connected-uid`` is the UID where the device is connected to. For a Bricklet
   this will be a UID of the Brick where it is connected to. For a Brick it will
   be the UID of the bottom Master Brick in the stack. For the bottom Master
   Brick in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position`` is position in stack (0 - 8) for Bricks or the position on
   Brick (a - d) for Bricklets.
 * ``hardware-version`` is in major, minor and release format.
 * ``firmware-version`` is in major, minor and release format.
 * ``device-identifier`` is the name of the device as known from the
   ``--list-devices`` option of the ``call`` and ``dispatch`` commands. With
   symbolic output disabled it is a number that represents the device.
 * ``enumeration-type`` is the type of enumeration.

 Possible enumeration types are:

 * ``available`` = 0, the device is available (enumeration triggered by user).
 * ``connected`` = 1, the device is newly connected (automatically send by Brick
   after establishing a communication connection). This indicates that the
   device has potentially lost its previous configuration and needs to be
   reconfigured.
 * ``disconnected`` = 2, the device is disconnected (only possible for USB
   connection). In this case only ``uid`` and ``enumeration-type`` are valid.

 The device identifier numbers can be found :ref:`here <device_identifier>`.

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
    enumeration-type=available

    uid=eN3
    connected-uid=68yjBL
    position=a
    hardware-version=1,1,0
    firmware-version=2,0,0
    device-identifier=distance-ir-bricklet
    enumeration-type=available


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
