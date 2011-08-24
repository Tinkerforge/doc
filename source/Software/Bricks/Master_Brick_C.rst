..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - Master Brick
================

.. _master_brick_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Stack Status
^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Master_Brick_C_example_stack_status.c
 :language: c
 :linenos:
 :tab-width: 4

.. _master_brick_c_api:

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


.. c:function:: void master_create(Master *master, const char *uid)

 Creates a Master object with the unique device ID *uid*::

    Master master;
    master_create(&master, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <master_brick_c_examples>`).


.. c:function:: int master_get_stack_voltage(Master *master, uint16_t *ret_voltage)

 Returns the stack voltage in mV. The stack voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. c:function:: int master_get_stack_current(Master *master, uint16_t *ret_current)

 Returns the stack current in mA. The stack current is the
 current that is drawn via the stack, i.e. it is given by a
 Step-Down or Step-Up power supply Brick.
 


