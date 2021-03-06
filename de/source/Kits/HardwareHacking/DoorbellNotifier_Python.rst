
.. _starter_kit_hardware_hacking_doorbell_notifier_python:

Benachrichtigung durch die Türklingel mit Python
================================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Wir setzen weiterhin voraus, dass eine passender Türklingel mit einem
:ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`
verbunden wurde wie :ref:`hier
<starter_kit_hardware_hacking_doorbell_notifier_hardware_setup>` beschrieben.


Ziele
-----

In diesem Projekt wandeln wir den Quelltext des
:ref:`starter_kit_hardware_hacking_smoke_detector_python` Projekts etwas ab,
damit dieser uns benachrichtigt wenn jemand an der Tür klingelt. Natürlich
kann diese Programm auch so erweitert werden, dass es eine E-Mail oder SMS
zur Benachrichtigung verschickt.


Quelltext
---------

`Download <https://raw.githubusercontent.com/Tinkerforge/hardware-hacking/master/doorbell_notifier/python/doorbell_notifier.py>`__

.. literalinclude:: ../../../../../hardware-hacking/doorbell_notifier/python/doorbell_notifier.py
 :language: python
 :tab-width: 4
