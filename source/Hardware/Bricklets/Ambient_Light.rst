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
 * Outline and drilling plan (`Download <../../_images/Dimensions/ambient-light_dimensions.png>`__)
 * TEMT6000 datasheet (`Download <http://www.vishay.com/docs/81579/temt6000.pdf>`__)
 * `Kicad <http://kicad.sourceforge.net/>`__ Project (Download)

Test your Ambient Light Bricklet
--------------------------------

To test your Ambient Light Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial). 
The former is a bridge between the Bricks/Bricklets and the programming 
language API bindings (you need this in any case if you want to use the 
Bricks/Bricklets). The latter is only for testing purposes.

Now you can connect your Ambient Light Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. 

.. image:: /Images/Bricklets/ambient_light_with_master_thumb.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/ambient_light_with_master_big.jpg

If you then connect the Brick to the PC over USB,
you should see a tab named "Ambient Light" in the Brick Viewer after you
pressed "connect".

If everything went as expected you can now see the exact illuminance in lux,
a graphical representation of the illuminance and a graph that shows the
illuminance over time. A good test of the sensor is to darken the room and
slowly move a flashlight over the sensor, the graph should then look
approximately like in the screenshot below.

.. image:: /Images/Bricklets/ambient_light_brickv.png
   :scale: 100 %
   :alt: Ambient Light Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/ambient_light_brickv.png

As a next step you might pick your favorite of the available programming
languages (see :ref:`below <ambl_interface_coding>`) and understand and 
execute one of the available examples. From there it should be straight 
forward to integrate the Ambient Light Bricklet into your project.

.. _ambl_interface_coding:

Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12


   "Python", ":ref:`API <ambient_light_bricklet_python_api>`", ":ref:`Examples <ambient_light_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <ambient_light_bricklet_java_api>`", ":ref:`Examples <ambient_light_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <ambient_light_bricklet_c_api>`", ":ref:`Examples <ambient_light_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <ambient_light_bricklet_cpp_api>`", ":ref:`Examples <ambient_light_bricklet_cpp_examples>`", "Installation"


.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

