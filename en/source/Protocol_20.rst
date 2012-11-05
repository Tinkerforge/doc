.. _protocol_20:

Protocol 2.0
============

We intend to replace the protocol that is used to communicate between the 
PC and Bricks/Bricklets by a new protocol in early December.

This page is still in a state of flux. Currently changes to the new protocol
are still expected. If you have an idea or suggestion for improvement, 
please give us a hint in the forum.


Holy Moly! Won't this break everything?
---------------------------------------

Yes. There will be a 2.0 version of all Brick firmwares, all Bricklet plugins,
all bindings, brickd and brickv. These will be incompatible to there 1.X.Y
counterparts. Unfortunately there is no way around that. We will of course try 
to make the transition and flashing process for the new versions as easy as 
possible.

What is the Problem with the old protocol?
------------------------------------------

The old protocol has state. What do we mean with *state*? It means that there
is information distributed throughout system, that is only gathered on startup.
Without this information the system will not work. Thus the system can not be
changed without a restart.

E.g.: If a RS485 slave stack is restarted, it is not usable until the RS485 
master stack is restarted too.

In particular the Stack ID is at fault here. At startup, every Brick and 
Bricklet in a system of interconnected Bricks/Bricklets and Extensions 
gets a unique Stack ID assigned. In the bindings, the UID is used to resolve
the Stack ID for every device.

After this startup phase, the whole communication between PC and
Bricks/Bricklets can be done using the Stack ID as a unique address.
The routing table is distributed in the Bricks and it is constant.
This is efficient, since the Stack ID is only 1 byte in size, as can
be seen in the old protocol structure below:

.. image:: /Images/protocol_old.png
   :alt: Old TF Protocol
   :align: center
   :target: ../../_images/protocol_old.png

On first glance this approach sounds reasonable. But as it turned out,
it is highly desirable to be robust towards:

* Parts of the system being not available for a time,
* parts of the system restarting,
* losing a connections for a time
* and losing a connections completely, with the need to reconnect.

In a small system that is connected via USB, none of the above problems
happen. So in the early days of the Bricks and Bricklets the
protocol was suitable. Now with the Extensions, long cable
connections, wireless connections, battery powered stacks and so on,
those problems happen all the time and the protocol can't handle them
properly.

Another problem with the old protocol: Bricks that are connected via
USB independently get the same Stack ID. Since it is not possible to route
the packets in a system where two Bricks have the same Stack ID, the
Brick Daemon has to secretly inspect all messages from Bricks and 
Bricklets and change them to make them unique. Messages that come from the
PC have to be inspected again to change the Stack ID back to the one
that is expected by the Bricks and Bricklets. In the meantime Bricks can
be connected and disconnected via USB and the Brick Daemon has to keep
all of the Stack IDs unique.

It is certainly possible to do this in a stable manner. As far as we can
tell this doesn't make any problems currently. But this also makes the
Brick Daemon implementation unnecessary complex.


How does the new protocol work?
-------------------------------

You probably guessed it already: There is no state in the new protocol.

That means, it will be possible to communicate with Bricks/Bricklets without
any prior resolving process, enumeration or similar. If your PC is connected
to a system of Bricks/Bricklets and you know the UID for one of them, you
will be able to communicate with it.

Routing in the new protocol is done similar to the way Ethernet switches
operate. The routing tables are dynamic and are extended everytime a
new packet from a currently unknown device is received. Packets that
have a currently unknown receiver are simply broadcasted.

.. image:: /Images/protocol_new.png
   :alt: TF Protocol 2.0
   :align: center
   :target: ../../_images/protocol_new.png

TF Protocol 2.0 packages are constructed as follows:

* **UID (32bit)**: The UID is now in every packet and used as the device 
  identifier, instead of the Stack ID. The old UIDs had a size of 64 bit. To
  make sure that the new protocol is not too inefficient, we changed the the
  size of the UID to 32 bit. Since the UID for the Bricks is read from a
  128 bit unique identifier register in the Brick, it is now more likely
  that there is a collision. To accommodate this, we will add a "setUID" 
  function to all Bricks, that can be used change the UID in the unlikely 
  case of a collision.

* **Length (8 bit)**: Length of the whole packet, including the optional data.

* **Function ID (8 bit)**: The ID of the function that is called.

* **Sequence Number (4 bit)**: A sequence number that is incremented with every 
  packet send. The answer from a Brick/Bricklet has the same sequence number.
  Since the Bricks/Bricklets currently guarantee that packets are answered in
  the correct order, this is not strictly needed. However, we can't rule
  out the possibility that there will be a Brick in the future that has
  a processor that is capable of real multitasking.

* **Options (4 bit)**:

 * **R [Return Expected] (1 bit)**: This bit is set to 1, if the packet should
   be answered. This has two advantages: First, the routing table can be 
   constructed more efficiently, since it is known if there is an answer to a 
   packet or not. 
   Second, it is now possible to receive an answer for a "setter". If you call
   a setter such as "setPosition" with the old protocol, there is no answer
   from a Brick and the call does not block. This means, that it is possible
   to spam the Bricks with more messages then they can swallow. With the new
   protocol you will have the option to turn blocking setters on. 
   Additionally, the R option can be used together with the E flag,
   see below.

 * **A [Authentication] (1 bit)**: This bit is set to 1 if the authentication is
   used. For a detailed explanation of the new authentication feature, see 
   :ref:`protocol_20_authentication`.

 * **OO [Other Options] (2 bit)**: Two currently unused options, for future use.

* **Flags (8 bit)**:

 * **E [Error] (1 bit)**: This flag can be set by a Brick or Bricklet in an
   answer message to a function call. It means that an error occured.
   Example: With the current protocol, if you call the "setPosition" function
   for a Servo Brick and you address a servo that is greater then 7 (does
   not exist), the message is discarded and there is no response from the Brick.
   With the E flag, a Brick/Bricklet can clarify that something went wrong.
   For a setter this is of course only possible if the R option is set.
 * **Future use (7 bit)**: Seven possible flags for future use.

* **Payload (0-512 bit)**: The data of the function call (as in the old 
  protocol).

* **Optional Data (0-64 bit)**: Data that is optionally attached to the packet.
  This includes the authentication hash if the authentication option is set.

Advantages
----------

TF Protocol 2.0

* is easily extendable,
* is more resilient to accidental restarts, ESD/EMI problems etc,
* allows simpler brickd implementations, therefore

 * the standard brickd will be implemented in c and be more efficient,
   especially on small embedded boards like the Raspberry PI,
 * it is possible to easily reimplement brickd, e.g. for android in java.

A robust program written for the new protocol can look as follows
(pseudo code)::

 func enumerate_callback {
     configure_brick();
     configure_bricklet();
 }
 
 func main() {
     while(true) {
         if(brick_is_configured) {
             do_something_with_brick();
         }
         if(bricklet_is_configured) {
             do_something_with_bricklet();
         }
     }
 }

The new enumeration features will make it possible to detect a Brick or
Bricklet that was restarted or newly connected in a way that allows to
easily reconfigure them if necessary. If a Brick is restarted (for whatever
reason) it will of course loose its configuration (e.g. the callback period).
Thus it has to be configured again.


Enumeration
-----------

Currently the enumeration process is messy and incomplete.
Problems are:

* It is not clear if a device is newly connected or if the enumeration is
  triggered by user.

* enumeration has not enough data to determine the complete network 
  topology (which bricklet is connected to which brick, etc).

* Type of Brick/Bricklet has to be parsed from a string.

In new protocol, the enumerate callback will have the following parameters:

* **String UID**: UID of device.

* **String connctedUID**: UID where the device is connected to. For a Bricklet
  this will be a UID of the Brick where it is connected to. For a Brick it
  will be the UID of the bottom Master Brick in the stack. For the
  bottom Master Brick in a Stack this will be "1". With this information
  it is possible to reconstruct the complete network topology.

* **char position**: Position in stack. For Bricks: '0' - '8' 
  (position in stack). For Bricklets: 'A' - 'D' (position on Brick).

* **int[3][3] version**: Major, minor and release number for Hardware, 
  Software and API Version.

* **int type**: Type of enumeration:

 * *ADDED*: If device is newly added.
 
 * *REMOVED*: If device is removed (only possible for USB connection).
 
 * *AVAILABLE*: If device is available (enumeration triggered by user).
 
 * *NO_AUTHENTICATION*: If authentication is enabled in ipcon but not on Brick.
 
 * *WRONG_AUTHENICATION*: If authentication in enabled for both, but the
   hash is wrong.
 
 * *AUTHENTICATION_NEEDED*: If authentication is enabled on Brick,
   but not in ipcon.

* **int deviceIdentifier**: A number that represents the Brick, instead of the 
  name of the Brick (easier to parse).


Bricklets
---------

Problems:
 * Bricklets without or with faulty Plugin crash Bricks.

In the new protocol:
 * Magic numbers to make sure plugin is really there.
 * Updated Bricklet API to make Bricklet programming more efficient (only 
   internal).

.. _protocol_20_authentication:

Authentication
--------------

For the authentication `UMAC <http://en.wikipedia.org/wiki/UMAC>`__ will be 
used. UMAC is an authentication code based on universal hashing.
It has provable cryptographic strength, but is still implementable and
usable on the Cortex M3 microcontroller that we use. There will nevertheless
be a small performance penalty if authentication is used.

There will be a "setAuthenticationKey" function for the IP Connection and
all Brick/Bricklet objects in the bindings. Bricks and Bricklets that
are configured to use an authentication key will not be controllable
by a third party that does not know the key. This allows to operate
Bricks and Bricklets in potentially vulnerable places, e.g. in a big 
university network.

If the key is lost, the Brick has to be reflashed. There is
no "getAuthenticationKey" or similar.

Internal Communication
----------------------

The internal communication (SPI in stack, RS485 for RS485 extension, Chibi) 
needs to be adapted to the new protocol. The now unavailable Stack ID is 
currently part of the internal protocols. For this a top-to-bottom approach 
is not suitable, we have to tinker with the implementations to find a new 
suitable approach.
