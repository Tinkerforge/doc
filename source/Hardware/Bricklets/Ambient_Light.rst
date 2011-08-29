.. _ambient_light_bricklet:

Ambient Light
=============

.. container:: twocol 

   .. container:: leftside

     .. image:: /Images/Bricklets/ambient_light_0_thumb.jpg
        :scale: 100 %
        :alt: Ambient Light Bricklet
        :target: ../../_images/Bricklets/ambient_light_0_big.jpg

   .. container:: rightside

     .. image:: /Images/Bricklets/ambient_light_1_thumb.jpg
        :scale: 100 %
        :alt: Ambient Light Bricklet
        :target: ../../_images/Bricklets/ambient_light_1_big.jpg

Description
-----------

With the Ambient Light :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by the possibility to
measure the ambient light.  The measured illuminance can be readout in `lux
<http://en.wikipedia.org/wiki/Lux>`_ directly. With configureable events
you can react on changing illuminance without polling.

Typical applications are 
illuminance dependent switching of backlights, motors etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight                            1.2g
Power Consumption                 TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            TEMT6000 (Vishay)
Output: Illumination              0-900 lux, unit 0.1 lux, resolution 12bit
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * TEMT6000 Datasheet (`Download <http://www.vishay.com/docs/81579/temt6000.pdf>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/ambient-light_dimensions.png
   :width: 300pt
   :alt: Ambient Light Bricklet outline and drilling plan
   :align: center
   :target: ../../_images/Dimensions/ambient-light_dimensions.png


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricklets/ambient_light_with_master_thumb.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_interface_coding>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _ambl_interface_coding:

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <pi_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12


   "Python", ":ref:`API <ambient_light_bricklet_python_api>`", ":ref:`Examples <ambient_light_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <ambient_light_bricklet_java_api>`", ":ref:`Examples <ambient_light_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <ambient_light_bricklet_c_api>`", ":ref:`Examples <ambient_light_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <ambient_light_bricklet_cpp_api>`", ":ref:`Examples <ambient_light_bricklet_cpp_examples>`", "Installation"


:ref:`Low Level Interfaces <pi_llpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI, over Brick", "API", "Example", "Installation"
   "I2C, over Brick", "API", "Example", "Installation"
   "UART(serial), over Brick", "API", "Example", "Installation"
   "Analog Voltage, directly", "\-", "Example", "\-"

.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

