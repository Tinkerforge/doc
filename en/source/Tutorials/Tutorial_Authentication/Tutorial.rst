
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / Authentication - Tutorial

.. _tutorial_authentication:

Authentication - Tutorial
=========================

By default no access control is performed on the TCP/IP interface of
Brick Daemon and the Ethernet/WIFI Extension. If you can connect to it you
can control the Bricks and Bricklets. In most cases this might no be a problem
because there are no untrusted third parties in your network.

In cases where you need to protect your stack against access from untrusted
third parties you can use authentication to do so. With authentication enabled
only parties that know your authentication secret can control your Bricks and
Bricklets.

Support for authentication was added in this software versions:

* Brick Daemon: 2.1.0
* Brick Viewer: 2.1.0
* All API bindings: 2.1.0
* Master Brick firmware (Ethernet/WIFI Extension): 2.2.0

Concept
-------

With authentication enabled any client (e.g. API bindings and Brick Viewer) can
still connect to the TCP/IP interface of Brick Daemon and the Ethernet/WIFI
Extension, but the connection starts in non-authenticated state. In this state
all incoming communication to control Bricks and Bricklets is dropped and all
outgoing callbacks from the devices are dropped as well. No normal communication
happens in non-authenticated state.

To switch a TCP/IP connection from non-authenticated to authenticated state the
client has to authenticate itself, it has to prove to the Brick Daemon or the
Ethernet/WIFI Extension that it knows the authentication secret and thus is
allowed to control the Bricks and Bricklets. This prove is done by a HMAC-SHA1
based handshake during which the authentication secret is never directly
exchanged over the wire.

If the handshake succeeds the connection switches from non-authenticated to
authenticated state and communication can continue as normal. If the handshake
fails then the connection gets closed. Authentication can fail if the wrong
secret was used or if authentication is not enabled at all on the Brick Daemon
or the WIFI/Ethernet Extension.


Configuration
-------------

Authentication is not enabled by default it has to be configured first.
Select an authentication secret. This can be up to 64 ASCII characters long.
In this tutorial ``My Authentication Secret!`` will be used as secret. See the
Brick Daemon and Ethernet/WIFI Extension documentation for detail on how to
configure the authentication secret:

* :ref:`Brick Daemon: Authentication <brickd_authentication>`
* :ref:`Ethernet Extension: Authentication <ethernet_configuration_authentication>`
* :ref:`WIFI Extension: Authentication <extension_wifi_authentication>`

Usage
-----

Once authentication is enabled you need to perform the authentication handshake
in your program to switch the connection from non-authenticated to authenticated
state. In Brick Viewer you just tick the "Use Authentication" check box on the
Setup tab and enter your authentication secret before clicking connect and
Brick Viewer will just work as normal.

In your own program you need to call the ``authenticate()`` function that was
added to all API bindings. This function takes the secret and performs the
handshake. It'll either succeed or fail with and error or exception indicating
that you provided the wrong secret or that authentication is not enabled at all
on the Brick Daemon or the WIFI/Ethernet Extension.

There are two ways to call ``authenticate()`` in your program, one without
callbacks and one with callbacks.

Without Callbacks
^^^^^^^^^^^^^^^^^

You can just insert the call to ``authenticate()`` after the call to
``connect()``. Such a program looks as follows (pseudo code)::

 func main() {
     ipcon.connect(HOST, PORT);
     ipcon.authenticate("My Authentication Secret!");

     // here comes the rest of your program
 }

It's easy to insert a single additional line in your program and use
authentication. But this does not work with auto-reconnect. As explained
in the tutorial about the :ref:`rugged approach <tutorial_rugged_approach>`
your code should follow a basic structure using the connected and enumerate
callback to be more resilient to outages.

With Callbacks
^^^^^^^^^^^^^^

Inserting the call to ``authenticate()`` after the call to ``connect()`` works
just fine. But you have to call ``authenticate()`` after an auto-reconnect
occurs too, because auto-reconnect creates a new TCP/IP connection that starts
in non-authenticated state again. A modified version of the
:ref:`rugged approach <tutorial_rugged_approach>` example looks as follows
(pseudo code)::

 func connected_callback(...) {
     ipcon.authenticate("My Authentication Secret!");

     ipcon.enumerate();
 }

 func main() {
     ipcon.connect(HOST, PORT);

     // here comes the rest of your program
 }

Each time the TCP/IP connection gets established the connected callback is
called to notify the program about this. Then the connected callback function
calls ``authenticate()`` to switch the connection to authenticated state again
before calling ``enumerate()``. This way you can ensure that your connection
is always in the authenticated state.

For all API bindings there is a new authenticate example that demonstrates
this approach available in the :ref:`IPConnection <api_bindings_ip_connection>`
documentation.
