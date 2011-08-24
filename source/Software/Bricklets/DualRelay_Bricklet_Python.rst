..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - DualRelay Bricklet
===========================

.. _dual_relay_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DualRelay_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

.. _dual_relay_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: DualRelay(uid)

 Creates a dual_relay object with the unique device ID *uid*::

    dual_relay = DualRelay("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dual_relay_bricklet_python_examples>`).


.. py:function:: DualRelay.set_state(relay1, relay2)

 :param relay1: bool
 :param relay2: bool
 :rtype: None

 Sets the state of the relays, *true* means on and *false* means off. 
 For example: (true, false) turns relay 1 on and relay 2 off.
 
 If you just want to set one of the relays and don't know the current state
 of the other relay, you can get the state with :py:func:`DualRelay.get_state`.
 
 The default value is (false, false).
 
.. py:function:: DualRelay.get_state()

 :rtype: (bool, bool)

 Returns the state of the relays, *true* means on and *false* means off. 
 


