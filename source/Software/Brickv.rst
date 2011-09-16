.. _brickv:

Brick Viewer (brickv)
=====================

This tool can be used to test :ref:`Bricks <product_overview_bricks>` and
:ref:`Bricklets <product_overview_bricklets>`. Each device has its own view
which shows you the main features or lets you control it.

Additionally this tool can be used to calibrate the analog to digital converter
(ADC) of the Bricks to improve measurement quality 
(see :ref:`here <brickv_adc_calibration>`)
or to flash bricklet plugins (see :ref:`here <brickv_flash_plugin>`).

Installation
------------

Windows
^^^^^^^

Linux
^^^^^

Mac OS
^^^^^^


Usage
-----


.. _brickv_adc_calibration:

Brick ADC Calibration
---------------------

.. image:: /Images/Software/brickv_advanced_functions.jpg
   :scale: 100 %
   :alt: Brickv's Advanced Functions Window
   :align: center


.. _brickv_flash_plugin:

Bricklet Plugin Flashing
------------------------

* only connect one Brick

.. image:: /Images/Software/brickv_not_connected.jpg
   :scale: 100 %
   :alt: Brickv not connected to Brickd
   :align: center

* press "connect"

.. image:: /Images/Software/brickv_connected_with_master_brick.jpg
   :scale: 100 %
   :alt: Brickv connected to Brickd, one Master Brick attached
   :align: center

* press "advanced functions"

.. image:: /Images/Software/brickv_advanced_functions.jpg
   :scale: 100 %
   :alt: Brickv's Advanced Functions Window
   :align: center

* then connect bricklet
* choose port on which bricklet is connected
* choose bin file, press "save", wait for "Check Ok"



TBD
---

* Name of Bricklet is used to match gui, names list? we need firmware,names tuples
* writing name, wait check ok
* UID is BASE... no \"1\" etc allowed, describe, when base wrong then \"Check Failed\"

