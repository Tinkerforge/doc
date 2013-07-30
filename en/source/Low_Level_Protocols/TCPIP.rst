
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#specifications">Specifications</a> / TCP/IP Protocol

.. _llproto_tcpip:

TCP/IP Protocol
===============

This is the API description for the TCP/IP protocol of the Brick Daemon
and the WIFI Extension.

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
packet starts with a 8 byte header followed by a payload of variable length. The
header consists of:

* UID as uint32 (4 byte),
* Packet length as uint8 (1 byte),
* Function ID as uint8 (1 bytes),
* Sequence number and Options as uint8 (1 byte) and
* Flags as uint8 (1 byte)

.. image:: /Images/Misc/protocol_new.png
   :scale: 100 %
   :alt: TF Protocol
   :align: center
   :target: ../_images/Misc/protocol_new.png

The UID is the unique identifier that is given to every Brick and Bricklet.

The *packet length* specifies the length of the complete packet (header and
payload) in bytes. A packet without a payload has a packet length of 8.
The function ID combined with the transfer direction defines the content of the
payload and this determines the packet length.

In a request packet the *function ID* specifies which function to execute on the
device specified by the UID.
In a response packet the function ID specifies from which function or callback
the packet was send.

The sequence number is incremented with every
packet send. The answer from a Brick/Bricklet has the same sequence number.
Since the Bricks/Bricklets currently guarantee that packets are answered in
the correct order, this is not strictly needed. However, we can't rule
out the possibility that there will be a Brick in the future that has
a processor that is capable of real multitasking.

For callbacks the sequence number is always 0 and this value is not
allowed for other packets. Non-callback packets can only use 1 - 15 as
sequence number. This allows to distinguish callback packets from other
packets.

Options:

* Response Expected (1 bit): This bit is set to 1, if the packet should
  be answered. This has two advantages: First, the routing table can be
  constructed more efficiently, since it is known if there is an answer to a
  packet or not.
  Second, it is possible to receive an answer for a "setter". If you call
  a setter such as ``setPosition``, there is normally no answer
  from a Brick and the call does not block. This means, that it is possible
  to spam the Bricks with more messages then they can swallow. With the R flag
  it is possible to turn blocking setters on.
  Additionally, the R option can be used together with the E flag,
  see below.

* Authentication (1 bit): This bit is set to 1 if the authentication is
  used (not implemented yet on Bricks).

* Other Options (2 bit): Two currently unused options, for future use.

Flags:

* Error Code (2 bit): This number can be set by a Brick or Bricklet in an
  answer message to a function call. If it is different from zero it means that
  an error occurred.

 * 0 = OK
 * 1 = INVALID_PARAMETER (index out of range or similar)
 * 2 = FUNCTION_NOT_SUPPORTED
 * Value 3 is not used yet.

* Future use (6 bit): Six possible flags for future use.

All data is represented in little endian. A *bool* value is represented by 1
byte; 0 is false, all other values are true. A *float* value is represented by
4 bytes in IEEE 754 format. A *char* value is represented by 1 byte in ASCII
encoding.

A fixed size char array represents a string. If the string is shorter than the
capacity of the array then the remaining space is filled with 0. In this case
the contained string is null-terminated. In case that the string fills the
whole array no null-terminator can be appended and the string is *not*
null-terminated. Therefore, you cannot rely on strings being null-terminated.


Function Calls
""""""""""""""

When the UID of a device is known its specific functions can be called.
To do this you need to send a corresponding request packet. The UID
specifies the destination of the request packet and also affects the meaning
of the function ID. This is because the same function ID has different meanings
for different Bricks and Bricklets. For example, function ID 1 maps to the
:tcpip:func:`get_stack_voltage <Master.get_stack_voltage>` function on the
Master Brick and to the :tcpip:func:`set_port <IO16.set_port>` function on the
IO-16 Bricklet.

The following example shows how to call the
:tcpip:func:`get_humidity <Humidity.get_humidity>` function of a Humidity
Bricklet with UID "b1Q" (Base58) or 33688 (integer). The corresponding
request packet has

* UID 33688 as uint32 (0x98 0x83 0x00 0x00),
* Packet length 8 as uint8 (0x08),
* Function ID 1 as uint8 (0x01),
* Sequence number 1 and response expected 1 as uint8 (0x18) and
* Flags 0 as uint8 (0x00).

and an empty payload. Its hex dump looks like this::

  0000   98 83 00 00 08 01 18 00                          .. ......

The corresponding response packet can be identified by the UID,
the function ID and the sequence number as they will have the same values
as the request packet. The response packet has

* UID 33688 as uint32 (0x98 0x83 0x00 0x00),
* Packet length 10 as uint8 (0x0a),
* Function ID 1 as uint8 (0x01),
* Sequence number 1 and response expected 1 as uint8 (0x18) and
* Flags 0 as uint8 (0x00).

The payload contains the

* humidity 421 as uint16 (0xa5 0x01).

A humidity value of 421 means 42.1 %RH and is just an example. The hex dump of
the packet looks like this::

  0000   98 83 00 00 0a 01 18 00 a5 01                    ..........

If there is no device with the given UID then the request is ignored and
no response is send at all. This means that you should wait for a response
packet only for a certain amount of time. The recommended timeout is 2500ms.
After this amount of time you can assume that there is no device with the given
UID.

There are also specific functions that do not send a response packet under
normal conditions, for example the :tcpip:func:`set_state <DualRelay.set_state>`
function of the Dual Relay Bricklet
(assuming the response expected flag is not set).


Callbacks
"""""""""

Devices can send response packets spontaneously back to the host to notify
about an event or specific condition.

Most callbacks are disabled by default and have to enabled first.
For example, the :tcpip:func:`CALLBACK_MAGNETIC_FIELD <IMU.CALLBACK_MAGNETIC_FIELD>`
callback of the IMU Brick with UID ``6wVE7W`` (3631747890 as integer) can be enabled
with a call to :tcpip:func:`IMU.set_magnetic_field_period` with a period larger 0.
Afterwards you will periodically receive response packets with

* UID 3631747890 as uint32 (0x32 0x13 0x78 0xd8),
* Packet length 14 as uint8 (0x0e),
* function ID 32 as uint8 (0x20),
* Sequence number 0 and response expected 1 as uint8 (0x08)
* Flags 0 as uint8 (0x00)

The payload contains

* x -239 as int16 (0x11 0xff),
* y 60 as int16 (0x3c 0x00) and
* z -223 as int16 (0x21 0xff)

representing the magnetic field and is just an example.
The hex dump of the packet looks like this::

  0000   32 13 78 d8 0e 20 08 00 11 ff 3c 00 21 ff        2.x.. ....<.!.

As callbacks are spontaneously triggered you can receive their response packet at
any time. For example between sending a request packet and receiving the
corresponding response packet.

.. note::
 Using callbacks for recurring events is *always* preferred
 compared to using getters. It will use less USB bandwidth and the latency
 will be a lot better, since there is no round-trip time.


.. _llproto_tcpip_api:

API
---

The following functions and callbacks are supported by all devices.


.. tcpip:function:: disconnect_probe

 :functionid: 128
 :emptyrequest: empty payload
 :noresponse: no response

 Should be send periodically to the :ref:`WIFI Extenstion <wifi_extension>` to
 improve the detection of Wi-Fi disconnects. Without this a disconnect of the
 WIFI Extension might no be detected at all due to the way TCP/IP works.

 The :ref:`API bindings <api_bindings>` send a disconnect probe if there was
 no other packet send or received for at least 5s. Bricks and Bricklets just
 ignore this function ID.

 As this feature is only useful for the WIFI Extension the Brick Daemon just
 drops incoming packets with this function ID and does not forward them over USB.

 This is a broadcast function and the UID in the packet header has to be
 set to 0 (broadcast).


.. tcpip:function:: enumerate

 :functionid: 254
 :emptyrequest: empty payload
 :noresponse: no response

 Triggers the :tcpip:func:`CALLBACK_ENUMERATE` callback for all devices
 currently connected to the Brick Daemon.

 This is a broadcast function and the UID in the packet header has to be
 set to 0 (broadcast).

 Use this function to enumerate all connected devices without the need to know
 their UIDs beforehand.


.. tcpip:function:: CALLBACK_FORCED_ACK

 :functionid: 0
 :emptyresponse: empty payload

 The :ref:`WIFI Extenstion <wifi_extension>` can send this callback to affect
 the TCP/IP buffer handling of clients. This can improve the handling of
 request packets on the client side.

 This feature is internal and bindings should just drop incoming packets with
 this function ID.


.. tcpip:function:: CALLBACK_ENUMERATE

 :functionid: 253
 :response uid: char[8]
 :response connected_uid: char[8]
 :response position: char
 :response hardware_version: uint8[3]
 :response firmware_version: uint8[3]
 :response device_identifier: uint16
 :response enumeration_type: uint8

 The callback has seven parameters:

 * *uid*: The UID of the device.
 * *connected_uid*: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "1". With this information it is possible to
   reconstruct the complete network topology.
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * *hardware_version*: Major, minor and release number for hardware version.
 * *firmware_version*: Major, minor and release number for firmware version.
 * *device_identifier*: A number that represents the device, instead of the
   name of the device (easier to parse).
 * *enumeration_type*: Type of enumeration.

 Possible enumeration types are:

 * IPCON_ENUMERATION_TYPE_AVAILABLE (0): Device is available (enumeration
   triggered by user).
 * IPCON_ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPCON_ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
   possible for USB connection). In this case only *uid* and *enumeration_type*
   are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifiers can be found :ref:`here <device_identifier>`.
