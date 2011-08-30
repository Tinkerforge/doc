.. _current25_bricklet:

Current25
=========


.. raw:: html

	<div id="container">
	<!-- Start Advanced Gallery Html Containers -->
	<div id="gallery2" class="content">
	<div id="controls" class="controls"></div>
	<div class="slideshow-container">
	<div id="loading" class="loader"></div>
	<div id="slideshow" class="slideshow"></div>
	</div>
	<div id="caption" class="caption-container"></div>
	</div>
	<div id="thumbs" class="navigation">
	<ul class="thumbs noscript">
	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #0">
	<img src="../../_images/test_k.jpg" alt="Title #0" />
	</a>
	</li>

	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #1">
	<img src="../../_images/test_k.jpg" alt="Title #1" />
	</a>
	</li>
	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #0">
	<img src="../../_images/test_k.jpg" alt="Title #0" />
	</a>
	</li>

	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #1">
	<img src="../../_images/test_k.jpg" alt="Title #1" />
	</a>
	</li>
	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #0">
	<img src="../../_images/test_k.jpg" alt="Title #0" />
	</a>
	</li>

	<li>
	<a class="thumb" name="leaf" href="../../_images/Bricklets/test.jpg" title="Title #1">
	<img src="../../_images/test_k.jpg" alt="Title #1" />
	</a>
	</li>

	</ul>
	</div>
	<div style="clear: both;"></div>
	</div>

Description
-----------

The Current25 :ref:`Bricklet <product_overview_bricklets>` extend the features
of an :ref:`Brick <product_overview_bricks>` by bidirectional current flow
measurments up to 25 Ampere. 
The measured current can be readout in `Ampere <http://en.wikipedia.org/wiki/Ampere>`_ 
directly. Additionally events can be configured, triggered when a specified current is 
exceeded.

Typical applications can be found in robotics. The bidirectional current 
flow measurement is advantageous since you can distinguish between charge and discharge.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight
Current Consumption
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            ACS711 25A Version (Allegro Microsystems)
Output: Current                   -25A to 25A, unit 10mA, resolution 12bit
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * ACS711 Datasheet (`Download <http://www.allegromicro.com/en/Products/Part_Numbers/0711/0711.pdf>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

.. Connectivity
.. ------------

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/current25_bricklet_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Test your Ambient Light Bricklet
--------------------------------

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_programming_interfaces>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


.. _current25_programming_interfaces:

Programming Interfaces
----------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <current25_bricklet_python_api>`", ":ref:`Examples <current25_bricklet_python_examples>`", "Installation"
   "Java", ":ref:`API <current25_bricklet_java_api>`", ":ref:`Examples <current25_bricklet_java_examples>`", "Installation"
   "C", ":ref:`API <current25_bricklet_c_api>`", ":ref:`Examples <current25_bricklet_c_examples>`", "Installation"
   "C++", ":ref:`API <current25_bricklet_cpp_api>`", ":ref:`Examples <current25_bricklet_cpp_examples>`", "Installation"


.. Troubleshoot
.. ------------

.. Servos dither
.. ^^^^^^^^^^^^^
.. **Reason:** The reason for this is typically a voltage drop-in, caused by 

.. **Solution:**
..  * Check input voltage.

