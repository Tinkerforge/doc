
.. _starter_kit_hardware_hacking_doorbell_notifier_python:

Doorbell Notifier using Python
==============================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

We are also assuming that you have a doorbell connected to an
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`
as described :ref:`here
<starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>`.


Goals
-----

In this project we modify the source code from the
:ref:`starter_kit_hardware_hacking_smoke_detector_python` project just minimally
to notify us if the doorbell is ringing. Of course this script can be extended
such that it will send an email or text message to you.


Source Code
-----------

`Download <https://raw.githubusercontent.com/Tinkerforge/hardware-hacking/master/doorbell_notifier/python/doorbell_notifier.py>`__

.. literalinclude:: ../../../../../hardware-hacking/doorbell_notifier/python/doorbell_notifier.py
 :language: python
 :tab-width: 4
