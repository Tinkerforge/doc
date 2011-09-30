.. _chibi_extension:

Chibi Extension
===============

.. raw:: html

        {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
        {{ tfdocstart() }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
        {{ tfdocend() }}


Description
-----------

This board is equipped with a AT86RF212 900Mhz Transceiver of 
`Atmel <http://www2.atmel.com/>`_. Typically these transceivers are used
for long range `Zigbee <http://en.wikipedia.org/wiki/Zigbee>`_ networks.
Since Zigbee licences are not GPL compatible we decided to use a free implementation
by Akriba. See this 
`article <http://freaklabs.org/index.php/Blog/Embedded/Introducing...Chibi-A-Simple-Small-Wireless-stack-for-Open-Hardware-Hackers-and-Enthusiasts.html>`__
for more information about chibi. In this 
`article <http://freaklabs.org/index.php/Blog/Zigbee/Zigbee-Linux-and-the-GPL.html>`__
the GPL problem of Zigbee is explained.

Two or more of this 
:ref:`Master Extension <product_overview_master_extensions>` with one
:ref:`Master Brick <master_brick>` each
can be used to create a Chibi network.
Each Master Brick can be a master of a stack. Using our
:ref:`High Level Concept <pi_hlpi>` this network
is completely transparent, which means that each device in this bus
is usable like it would be connected to the PC with its own USB connection.
You can write the same programming code.

.. note:: Coming soon! 
   Currently not available. Please be patient.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
Range (Outdoor/Indoor)            TBD/TBD
Maximum Baud Rate                 TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            13g
================================  ============================================================



Resources
---------
 
* AT86RF212 datasheet (Download)
* Schematic (Download)
* Outline and drilling plan (`Download <../../_images/Dimensions/chibi_extensions_dimensions.png>`__)
* Project (Download)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__

.. Chibi Network Assembly
  ----------------------
  * Picture Network
  * explain creation and configuration
  * explain usage



.. Connectivity
   ------------
  The following picture depicts the different connection possibilities of the 
  Chibi-Extension.
  .. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

.. Troubleshoot
   ------------

