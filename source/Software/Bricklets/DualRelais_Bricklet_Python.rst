..
 #############################################################
 # This file was automatically generated on 2011-08-18.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - DualRelais Bricklet
============================

.. _dual_relais_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DualRelais_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

.. _dual_relais_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: DualRelais(uid)

 Creates a dual_relais object with the unique device ID *uid*::

    dual_relais = DualRelais("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dual_relais_bricklet_python_examples>`).


.. py:function:: DualRelais.set_state(relais1, relais2)

 :param relais1: bool
 :param relais2: bool
 :rtype: None

 Sets the state of the relais, *true* means on and *false* means off. 
 For example: (true, false) turns relais 1 on and relais 2 off.
 
 If you just want to set one of the relais and don't know the current state
 of the other relais, you can get the state with :py:func:`DualRelais.get_state`.
 
 The default value is (false, false).
 
.. py:function:: DualRelais.get_state()

 :rtype: (bool, bool)

 Returns the state of the relais, *true* means on and *false* means off. 
 


