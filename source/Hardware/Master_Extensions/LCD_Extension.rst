.. _lcd_extension:

LCD Extension
=============

.. raw:: html

        {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
        {{ tfdocstart() }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
        {{ tfdocend() }}


Description
-----------

The 485 Extension is a :ref:`Master Extension <product_overview_master_extensions>`
which can be used to provide a :ref:`Master Bricks <master_brick>` with a
`RS485 <http://en.wikipedia.org/wiki/RS485>`_ interface.
Usage is only intended together with a Master Brick.

Since RS485 is differental interface standard, information can be communicated
over large distances. Therefore this interface is better suited to connect a
stack cable-based to a PC than USB.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            TBD
================================  ============================================================


Bus Assembly
------------
* Picture Bus
* explain termination


Resources
---------

* Schematic (Download)
* Outline and drilling plan (Download)
* Project (Download)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__

Connectivity
------------

The following picture depicts the different connection possibilities of the 
485-Extension.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/lcd_extension_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


.. Powersupply
.. ^^^^^^^^^^^

.. Todo: Bildchen


Usage
-----

 * Explain usage

Troubleshoot
------------

