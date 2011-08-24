..
 #############################################################
 # This file was automatically generated on 2011-08-18.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - DualRelais Bricklet
=======================

.. _dual_relais_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DualRelais_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

.. _dual_relais_bricklet_c_api:

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


.. c:function:: void dual_relais_create(DualRelais *dual_relais, const char *uid)

 Creates a DualRelais object with the unique device ID *uid*::

    DualRelais dual_relais;
    dual_relais_create(&dual_relais, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dual_relais_bricklet_c_examples>`).


.. c:function:: int dual_relais_set_state(DualRelais *dual_relais, bool relais1, bool relais2)

 Sets the state of the relais, *true* means on and *false* means off. 
 For example: (true, false) turns relais 1 on and relais 2 off.
 
 If you just want to set one of the relais and don't know the current state
 of the other relais, you can get the state with :c:func:`dual_relais_get_state`.
 
 The default value is (false, false).
 
.. c:function:: int dual_relais_get_state(DualRelais *dual_relais, bool *ret_relais1, bool *ret_relais2)

 Returns the state of the relais, *true* means on and *false* means off. 
 


