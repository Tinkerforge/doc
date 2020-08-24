
.. |ref_api_bindings| replace:: :ref:`Shell API bindings <api_bindings_shell>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_shell_install>`
.. |bindings_name| replace:: Shell

.. _ip_connection_shell:

Shell - IP Connection
=====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ip_connection_shell_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example-enumerate.sh) <https://github.com/Tinkerforge/generators/raw/master/shell/example-enumerate.sh>`__

.. literalinclude:: IPConnection_Shell_example-enumerate.sh
 :language: bash
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example-authenticate.sh) <https://github.com/Tinkerforge/generators/raw/master/shell/example-authenticate.sh>`__

.. literalinclude:: IPConnection_Shell_example-authenticate.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ip_connection_shell_api:

API
---

At first some information about the general command structure:

.. sh:function:: X Ntinkerforge A[<option>..] L<command> L[<argument>..]

 :param <command>: string

 The basic command can take several options:

 * ``--help`` shows general help and exits
 * ``--version`` shows version number and exits
 * ``--host <host>`` IP address or hostname to connect to, default: ``localhost``
 * ``--port <port>`` port number to connect to, default: 4223
 * ``--secret <secret>`` secret for authentication (new in version 2.1.0)
 * ``--item-separator <item-separator>`` separator for array items, default:
   ``,`` (comma)
 * ``--group-separator <group-separator>`` separator for output groups,
   default: ``\n`` (newline)
 * ``--array-ellipsis <array-ellipsis>`` ellipsis for arrays, default: ``..``
   (two dots) (new in version 2.1.5)
 * ``--no-escaped-input`` disables escaped input of values (new in version
   2.1.5)
 * ``--no-escaped-output`` disables escaped output of values (new in version
   2.1.5)
 * ``--no-symbolic-input`` disables symbolic input of values
 * ``--no-symbolic-output`` disables symbolic output of values

 All commands, except if the ``--help`` or ``--version`` option is present,
 create a TCP/IP connection to the given ``host`` and ``port``. The host and
 port can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Since version 2.1.0 the ``--secret`` option can be used to perform an
 authentication handshake with the connected Brick Daemon or WIFI/Ethernet
 Extension.
 If the handshake succeeds the connection switches from non-authenticated to
 authenticated state and communication can continue as normal. If the handshake
 fails then the connection gets closed. Authentication can fail if the wrong
 secret was used or if authentication is not enabled at all on the Brick Daemon
 or the WIFI/Ethernet Extension.
 See the :ref:`authentication tutorial <tutorial_authentication>` for more
 information.

 The item separator is used for parsing and formatting arrays. An array with
 three values 1, 2 and 3 is formatted as ``1,2,3``.

 The group separator is used for formatting the output of callbacks. The group
 separator is printed before each callback output with more than one line,
 except before the first one, to separate the output of multiple callback
 invocations. See the section about :ref:`output formatting <ip_connection_shell_output>`
 for details.

 Since version 2.1.5 an array ellipsis can be used to specify partial arrays.
 For example, the :sh:func:`write <rs232-bricklet write>` function of the RS232
 Bricklet takes an array of 60 characters. Normally, all 60 items have to be
 specified. With the array ellipsis a partial array can be specified (e.g.
 ``t,e,s,t,..``) and the missing part will automatically be filled with ``'\0'``
 characters.

 Since version 2.1.5 escaped input and output is enabled by default. For
 example, the :sh:func:`write-line <lcd-20x4-bricklet write-line>` function of
 the LCD 20x4 Bricklet takes a string. This string has to specified in the
 special character set of the display. For example, the degree sign (°) is
 represented by a non-ASCII character with value 0xDF. With escaped input
 enabled the degree sign can be specified as ``"\xDF"`` on the command line.
 Ensure to quote such strings to stop the shell from interpreting it. With
 escaped output enabled non-ASCII characters in string values will be
 represented as ``\x`` escape sequence.

 By default symbolic input and output is enabled. For example, the
 :sh:func:`set-i2c-mode <temperature-bricklet set-i2c-mode>` function of the
 Temperature Bricklet can take two different values: 0 and 1. With symbolic
 input enabled there are also two symbols ``fast`` (0) and ``slow`` (1) for
 this values. The same holds for the :sh:func:`get-i2c-mode
 <temperature-bricklet get-i2c-mode>` function: the same two symbols are used
 for symbolic output, if enabled.

 There are four subcommands: ``call``, ``dispatch``, ``enumerate`` and ``listen``


.. sh:function:: X Ptinkerforge Ncall A[<option>..] L<device> L<uid> L<function> L[<argument>..]

 :param <device>: string
 :param <uid>: string
 :param <function>: string

 The ``call`` command is used to call a function of a Brick or Bricklet. It can
 take several options:

 * ``--help`` shows help for the ``call`` command and exits
 * ``--list-devices`` shows a list of known devices and exits
 * ``--timeout <timeout>`` maximum time (ms) to wait for response, default: 2500

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
 to dispatch. By default only enumerate callbacks with
 ``enumeration-type=available`` are dispatched.

 The ``--execute`` option allows for advanced output formatting. See the
 :ref:`section about this <ip_connection_shell_output>` for details.

 The command has seven output values:

 * ``uid`` is the UID of the device.
 * ``connected-uid`` is the UID where the device is connected to. For a Bricklet this
   is the UID of the Brick or Bricklet it is connected to. For a Brick it is
   the UID of the bottommost Brick in the stack. For the bottommost Brick
   in a stack it is "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position`` is for Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'h' (position on Brick) or 'i' (position of the Raspberry Pi (Zero) HAT)
   or 'z' (Bricklet on :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardware-version`` is in major, minor and release format.
 * ``firmware-version`` is in major, minor and release format.
 * ``device-identifier`` is the name of the device as known from the
   ``--list-devices`` option of the ``call`` and ``dispatch`` commands. With
   symbolic output disabled it is a number that represents the device.
 * ``enumeration-type`` is the type of enumeration.

 Possible enumeration types are:

 * ``available`` = 0: The device is available (enumeration triggered by user:
   :sh:func:`enumerate <tinkerforge enumerate>`). This enumeration type can
   occur multiple times for the same device.
 * ``connected`` = 1: The device is newly connected (automatically send by Brick
   after establishing a communication connection). This indicates that the
   device has potentially lost its previous configuration and needs to be
   reconfigured.
 * ``disconnected`` = 2: The device is disconnected (only possible for USB
   connection). In this case only ``uid`` and ``enumeration-type`` are valid.

 The device identifier numbers can be found :ref:`here <device_identifier>`.

Advanced Functions
^^^^^^^^^^^^^^^^^^

.. toctree::
   :hidden:

   NetIO_Setup

.. sh:function:: X Ptinkerforge Nlisten A[<option>..]

 The ``listen`` command is used to open a TCP/IP socket that accepts ``call``,
 ``dispatch`` and ``enumerate`` commands. This enables the Shell bindings to
 act as a text protocol proxy for clients such as ``netcat``, ``telnet`` or the
 :ref:`NetIO Controller App <netio_setup>`. The ``listen`` command can take
 several options:

 * ``--help`` shows help for the ``listen`` command and exits
 * ``--address <address>`` IP address to listen to, default: ``0.0.0.0``
 * ``--port <port>`` port number to listen to, default: ``4217``
 * ``--enable-host`` enables ``--host`` option to override IP address or hostname to connect to
 * ``--enable-port`` enables ``--port`` option to override port number to connect to
 * ``--enable-execute`` enables ``--execute`` option for getters and callbacks

 In listen mode some command line options are disabled by default for incoming
 commands.

 The ``--host`` and ``--port`` options are disabled by default so incoming
 commands can only connect to the host and port given to the ``listen`` command.
 Use ``--enable-host`` and ``--enable-port`` to enable these options for
 incoming commands.

 The ``--execute`` option for getter calls and callback dispatching is disabled
 by default so incoming command cannot execute other commands. Use
 ``--enable-execute`` to enable this option for incoming commands.

 Incoming commands have to be terminated by ``\n``. The output is also
 terminated by ``\n``. See the :ref:`output formatting <ip_connection_shell_output>`
 section for details.

 .. versionadded:: 2.0.3

.. _ip_connection_shell_output:

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

The output in listen mode (see :sh:func:`tinkerforge listen`) differs in two
aspects to simplify parsing on the client side:

* no group separator is included in the output and the ``--group-separator``
  option is ignored
* output lines in a group are separated by ``\t`` instead of ``\n``

This means the output for the ``enumerate`` command looks like this in listen mode::

 uid=68yjBL\tconnected-uid=0\tposition=0\thardware-version=1,0,0\tfirmware-version=2,0,6\tdevice-identifier=master-brick\tenumeration-type=available\n
 uid=eN3\tconnected-uid=68yjBL\tposition=a\thardware-version=1,1,0\tfirmware-version=2,0,0\tdevice-identifier=distance-ir-bricklet\tenumeration-type=available\n

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

    $ tinkerforge call distance-ir-bricklet eN3 get-distance\
      --execute "echo 'scale=2; {distance} / 10' | bc | xargs printf 'current distance is %.1fcm\n'"
    current distance is 46.3cm

Before the command line is executed the contained placeholders are replaced with
the actual values. In the example above a call to ``get-distance`` without
``--execute`` outputs a single line with key ``distance``. This key is also the
placeholder for ``--execute`` usage wrapped in curly brackets: ``{distance}``.

In listen mode (see :sh:func:`tinkerforge listen`) the ``--execute`` option is
not available by default and has to be enabled by the ``--enable-execute``
option of the ``listen`` command.
