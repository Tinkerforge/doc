..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _master_brick_python:

Python - Master Brick
=====================

.. _master_brick_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Stack Status
^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Master_Brick_Python_example_stack_status.py
 :language: python
 :linenos:
 :tab-width: 4

.. _master_brick_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Master(uid)

 Creates a master object with the unique device ID *uid*::

    master = Master("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <master_brick_python_examples>`).


.. py:function:: Master.get_stack_voltage()

 :rtype: int

 Returns the stack voltage in mV. The stack voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. py:function:: Master.get_stack_current()

 :rtype: int

 Returns the stack current in mA. The stack current is the
 current that is drawn via the stack, i.e. it is given by a
 Step-Down or Step-Up power supply Brick.
 


