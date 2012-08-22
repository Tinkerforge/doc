.. _llproto_tcpip:

TCP/IP
======

This is the API site for the TCP/IP protocol of the Brick Daemon.

An overview of products that are controllable over TCP/IP
can be found :ref:`here <product_overview>`.

.. _llproto_tcpip_protocol:

Protocol
--------

The TCP/IP protocol is modeled after the concept of a function call.
A request packet is send to the stack to trigger the execution of a function
on a selected Brick or Bricklet. Functions that return something send a response
packet back containing the return value(s).
Functions that return nothing don't send a response packet back to the host.
Beside normal functions there are also callbacks. Bricks and Bricklets can send
response packets spontaneously back to the host to notify about an event or
specific condition.

Packet Layout
^^^^^^^^^^^^^

The TCP/IP protocol is based on packets transfered between host and stack. Each
packet starts with a 4 byte header followed by a payload of variable length. The
header consists of 3 unsigned integers:

* stack ID as uint8 (1 byte),
* function ID as uint8 (1 byte) and
* packet length as uint16 (2 bytes).

The meaning of the *stack ID* depends on the transfer direction of the packet.
If the packet is send from host to stack (request packet) then the stack ID
specifies its destination. If the packet is send from stack to host (response
packet) then the stack ID specifies its source. Stack ID 0 is the broadcast
address for request packets.

In a request packet the *function ID* specifies which function to execute on the
device specified by the stack ID.
In a response packet the function ID specifies from which function or callback
the packet was send.

The *packet length* specifies the length of the complete packet (header and
payload) in bytes. A packet without a payload has a packet length of 4.
The function ID combined with the transfer direction defines the content of the
payload and this determines the packet length.

All data is represented in little endian. A *bool* value is represented by 1
byte; 0 is false, all other values are true. A *float* value is represented by
4 bytes in IEEE 754 format. A *char* value is represented by 1 byte in ASCII
encoding.

A fixed size char array represents a string. If the string is shorter than the
capacity of the array then the remaining space is filled with 0. In this case
the contained string is null-terminated. In case that the string fills the
whole array no null-terminator can be appended and the string is *not*
null-terminated. Therefore, you cannot rely on strings being null-terminated.

Communication
^^^^^^^^^^^^^

A typical TCP/IP communication has three phases. The first phase consists of
establishing a TCP/IP connection to the Brick Daemon. Before you can call any
function on the connected devices you need to know their stack IDs.
Discovering those stack IDs is the second phase. In the third phase you can
call specific functions on the connected devices.

.. _llproto_tcpip_resolve_uid:

Resolve UID to Stack ID
"""""""""""""""""""""""

To resolve a known UID to the corresponding stack ID the
:tcpip:func:`get_stack_id` function can be used.
The corresponding request packet that you need to send has

* stack ID 0 as uint8 (0x00),
* function ID 255 as uint8 (0xff) and
* packet length 12 as uint16 (0x0c 0x00).

The payload contains the

* UID 3904673860505581361 as uint64 (0x31 0x37 0x30 0x33 0x30 0x30 0x30 0x36).

This is an example UID of a Brick and needs to be replaced with the actual UID of your
device. The UID is shown as integer here to emphasis that the TCP/IP protocol
represents UIDs as uint64 (8 bytes). The Brick Viewer
and the other API bindings represent UIDs in Base58 encoding instead.
The example UID 3904673860505581361 is represented as a4GeP9ZpQFT in Base58.

The hex dump of the :tcpip:func:`get_stack_id` request
packet looks like this::

  0000   00 ff 0c 00 31 37 30 33 30 30 30 36              ....17030006

If there is a device with the given UID then you will receive a response
packet with function ID 255. If there is no device with the given UID then no
response is send at all. This means that you should wait for a response packet
only for a certain amount of time. The recommended timeout is 2500ms. After
this amount of time you can assume that there is no device with the given UID.

The :tcpip:func:`get_stack_id` response packet from the Master Brick has

* stack ID 0 as uint8 (0x00),
* function ID 255 as uint8 (0xff) and
* packet length 56 as uint16 (0x38 0x00).

The payload contains

* device UID 3904673860505581361 as uint64 (0x31 0x37 0x30 0x33 0x30 0x30 0x30 0x36),
* device firmware version 1.1.7 as uint8[3] (0x01 0x01 0x07)
* device name "Master Brick 1.0" as char[40] (0x4d 0x61 ... 0x30 0x00 ... 0x00) and
* device stack ID 1 as uint8 (0x01).

The hex dump of the packet looks like this::

  0000   00 ff 38 00 31 37 30 33 30 30 30 36 01 01 07 4d  ..8.17030006...M
  0010   61 73 74 65 72 20 42 72 69 63 6b 20 31 2e 30 00  aster Brick 1.0.
  0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0030   00 00 00 00 00 00 00 01                          ........

Bricklets typically have UIDs with much smaller values compared to the UIDs of
Bricks. A request packet for the :tcpip:func:`get_stack_id`
function for a Bricklet with UID 21238 has

* stack ID 0 as uint8 (0x00),
* function ID 255 as uint8 (0xff) and
* packet length 12 as uint16 (0x0c 0x00).

The payload contains the

* UID 21238 as uint64 (0xf6 0x52 0x00 0x00 0x00 0x00 0x00 0x00).

The hex dump of this request packet looks like this::

  0000   00 ff 0c 00 f6 52 00 00 00 00 00 00              .....R......

Enumeration
"""""""""""

The :tcpip:func:`enumerate` function can be used to receive
information about all connected devices. The corresponding request packet
has

* stack ID 0 as uint8 (0x00),
* function ID 254 as uint8 (0xfe),
* packet length 4 as uint16 (0x04 0x00)

and an empty payload. Its hex dump looks like this::

  0000   00 fe 04 00                                      ....

There is no response packet for this function, but as a reaction the
:tcpip:func:`CALLBACK_ENUMERATE` callback is
triggered for each connected device, in this example, a Master Brick and a
Linear Poti Bricklet. The callback response packet for the Master Brick has

* stack ID 0 as uint8 (0x00),
* function ID 253 as uint8 (0xfd) and
* packet length 54 as uint16 (0x36 0x00).

The payload contains

* device UID 3904673860505581361 as uint64 (0x31 0x37 0x30 0x33 0x30 0x30 0x30 0x36),
* device name "Master Brick 1.0" as char[40] (0x4d 0x61 ... 0x30 0x00 ... 0x00),
* device stack ID 1 as uint8 (0x01) and
* is-new set to true as uint8 (0x01).

The hex dump of the packet looks like this::

  0000   00 fd 36 00 31 37 30 33 30 30 30 36 4d 61 73 74  ..6.17030006Mast
  0010   65 72 20 42 72 69 63 6b 20 31 2e 30 00 00 00 00  er Brick 1.0....
  0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0030   00 00 00 00 01 01                                ......

The callback response packet for the Linear Poti Bricklet has

* stack ID 0 as uint8 (0x00),
* function ID 253 as uint8 (0xfd) and
* packet length 54 as uint16 (0x36 0x00).

The payload contains

* device UID 21238 as uint64 (0xf6 0x52 0x00 0x00 0x00 0x00 0x00 0x00),
* device name "Linear Poti Bricklet 1.0" as char[40] (0x4c 0x69 ... 0x30 0x00 ... 0x00),
* device stack ID 2 as uint8 (0x02) and
* is-new set to true as uint8 (0x01).

The hex dump of the packet looks like this::

  0000   00 fd 36 00 f6 52 00 00 00 00 00 00 4c 69 6e 65  ..6..R......Line
  0010   61 72 20 50 6f 74 69 20 42 72 69 63 6b 6c 65 74  ar Poti Bricklet
  0020   20 31 2e 30 00 00 00 00 00 00 00 00 00 00 00 00   1.0............
  0030   00 00 00 00 02 01                                ......

Function Calls
""""""""""""""

When the stack ID of a device is known its specific functions can be called.
To do this you need to send a corresponding request packet. The stack ID
specifies the destination of the request packet and also affects the meaning
of the function ID. This is because the same function ID has different meanings
for different Bricks and Bricklets. For example, function ID 1 maps to the
:tcpip:func:`get_stack_voltage <Master.get_stack_voltage>` function on the
Master Brick and to the :tcpip:func:`set_port <IO16.set_port>` function on the
IO-16 Bricklet.

The following example shows how to call the
:tcpip:func:`get_humidity <Humidity.get_humidity>` function of a Humidity
Bricklet with stack ID 3. The corresponding request packet has

* stack ID 3 as uint8 (0x03),
* function ID 1 as uint8 (0x01),
* packet length 4 as uint16 (0x04 0x00)

and an empty payload. Its hex dump looks like this::

  0000   03 01 04 00                                      ....

The corresponding response packet can be identified by the stack ID and
function ID field as they will have the same values as the request packet.
The response packet has

* stack ID 3 as uint8 (0x03),
* function ID 1 as uint8 (0x01),
* packet length 6 as uint16 (0x06 0x00)

The payload contains the

* humidity 421 as uint16 (0xa5 0x01).

A humidity value of 421 means 42.1 %RH and is just an example. The hex dump of
the packet looks like this::

  0000   03 01 06 00 a5 01                                ......

If there is no device with the given stack ID then the request is ignored and
no response is send at all. This means that you should wait for a response
packet only for a certain amount of time. The recommended timeout is 2500ms.
After this amount of time you can assume that there is no device with the given
stack ID.

There are also specific functions that do not send a response packet under
normal conditions, for example the :tcpip:func:`set_state <DualRelay.set_state>`
function of the Dual Relay Bricklet.

Callbacks
"""""""""

Devices can send response packets spontaneously back to the host to notify
about an event or specific condition.

The Brick Daemon does not forward callback packets by default, because it does
not know which IP connection is interested in receiving them. Therefore, you need
to tell brickd that you want to receive callback packets for a specific device.
This is a side effect of calling the :tcpip:func:`get_stack_id` for that device.
In summary: you need to call :tcpip:func:`get_stack_id`
for each device from which you want to receive callbacks.

Most callbacks are disabled by default and have to enabled first.
For example, the :tcpip:func:`CALLBACK_MAGNETIC_FIELD <IMU.CALLBACK_MAGNETIC_FIELD>`
callback of the IMU Brick (with stack ID 5) can be enabled with a call to
:tcpip:func:`IMU.set_acceleration_period` with a period larger 0. Afterwards
you will periodically receive response packets with

* stack ID 5 as uint8 (0x05),
* function ID 31 as uint8 (0x1f) and
* packet length 10 as uint16 (0x0a 0x00).

The payload contains

* x 269 as int16 (0x0d 0x01),
* y 184 as int16 (0xb8 0x00) and
* z 357 as int16 (0x65 0x01)

representing the magnetic field and is just an example.
The hex dump of the packet looks like this::

  0000   05 1f 0a 00 0d 01 b8 00 65 01                    ........e.

As callbacks are spontaneously triggered you can receive their response packet at
any time. For example between sending a request packet and reveicing the
corrsponding response packet.

.. note::
  Using callbacks for recurring events is *always* preferred
  compared to using getters. It will use less USB bandwidth and the latency
  will be a lot better, since there is no roundtrip time.

.. _llproto_tcpip_api:

API
---

The following functions and callbacks are supported by all devices.

Basic Methods
^^^^^^^^^^^^^

.. tcpip:function:: get_stack_id

 :functionid: 255
 :request uid: uint64
 :response device_uid: uint64
 :response device_firmware_version: uint8[3]
 :response device_name: char[40]
 :response device_stack_id: uint8

 Returns the metadata (UID, firmware version, name and stack ID) of the device
 with the UID given in the request. No response is send if there is no Brick or
 Bricklet with the given UID.

 This is a broadcast function and the stack ID in the packet header has to be
 set to 0 (broadcast stack ID).

 Use this function to resolve a UID to the corresponding stack ID that is
 required for calling other functions of the device.

Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tcpip:function:: enumerate

 :functionid: 254
 :emptyrequest: empty payload
 :noresponse: no response

 Triggers the :tcpip:func:`CALLBACK_ENUMERATE` callback for all devices
 currently connected to the Brick Daemon.

 This is a broadcast function and the stack ID in the packet header has to be
 set to 0 (broadcast stack ID).

 Use this function to enumerate all connected devices without the need to know
 their UIDs beforehand.

Callbacks
^^^^^^^^^

.. tcpip:function:: CALLBACK_ENUMERATE

 :functionid: 253
 :response device_uid: uint64
 :response device_name: char[40]
 :response device_stack_id: uint8
 :response is_new: bool

 There are three different possibilities for the callback to be called.
 Firstly, the callback is triggered for all currently connected devices
 (with *is_new* set to *true*) when the :tcpip:func:`enumerate` function is
 called. Secondly, the callback is triggered if a new Brick is plugged
 in via USB (with *is_new* set to *true*) and lastly it is triggered if a Brick is
 unplugged (with *is_new* set to *false*).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).
