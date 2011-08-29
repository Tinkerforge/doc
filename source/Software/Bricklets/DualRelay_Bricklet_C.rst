..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _dual_relay_bricklet_c:

C - DualRelay Bricklet
======================

.. _dual_relay_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DualRelay_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

.. _dual_relay_bricklet_c_api:

API
---

Every function of the c bindings returns an integer which describes an
error code. Data returned from the device, when a getter is called,
is handled via call by reference. These parameters are labelled with the
``ret_`` prefix.

Possible error codes are

 * E_OK = 0
 * E_TIMEOUT = -1
 * E_NO_STREAM_SOCKET = -2
 * E_HOSTNAME_INVALID = -3
 * E_NO_CONNECT = -4
 * E_NO_THREAD = -5
 * E_NOT_ADDED = -6

as defined in :file:`ip_connection.h`.


Basic Methods
^^^^^^^^^^^^^


.. c:function:: void dual_relay_create(DualRelay *dual_relay, const char *uid)

 Creates a DualRelay object with the unique device ID *uid*::

    DualRelay dual_relay;
    dual_relay_create(&dual_relay, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dual_relay_bricklet_c_examples>`).


.. c:function:: int dual_relay_set_state(DualRelay *dual_relay, bool relay1, bool relay2)

 Sets the state of the relays, *true* means on and *false* means off. 
 For example: (true, false) turns relay 1 on and relay 2 off.
 
 If you just want to set one of the relays and don't know the current state
 of the other relay, you can get the state with :c:func:`dual_relay_get_state`.
 
 The default value is (false, false).
 
.. c:function:: int dual_relay_get_state(DualRelay *dual_relay, bool *ret_relay1, bool *ret_relay2)

 Returns the state of the relays, *true* means on and *false* means off. 
 


