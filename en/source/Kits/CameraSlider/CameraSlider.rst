
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#starter-kits">Starter Kits</a> / Starter Kit: Camera Slider
:FIXME_shoplink: ../../../shop/kits/starter-kit-camera-slider.html

.. _starter_kit_camera_slider:

Starter Kit: Camera Slider
==========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Kits/kit_camera_slider_complete1_350.jpg",
	               "Kits/kit_camera_slider_complete1_800.jpg",
	               "Camera Slider: Complete kit")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_content_100.jpg",
	             "Kits/kit_camera_slider_content_800.jpg",
	             "Camera Slider: Content")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_camera1_100.jpg",
	             "Kits/kit_camera_slider_camera1_800.jpg",
	             "Camera Slider: With video camera")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_camera2_100.jpg",
	             "Kits/kit_camera_slider_camera2_800.jpg",
	             "Camera Slider: With camera")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_w_lcd1_100.jpg",
	             "Kits/kit_camera_slider_w_lcd1_800.jpg",
	             "Camera Slider: With LCD")
	}}
	{{
	    tfdocimg("Kits/kit_camera_slider_w_lcd2_100.jpg",
	             "Kits/kit_camera_slider_w_lcd2_800.jpg",
	             "Camera Slider: With LCD")
	}}
	{{ tfdocend() }}

.. note::
 This kit is currently work-in-progress!

Features
--------

* Easy to modify
* Build your own brackets with MakerBeams
* Extend functionality of kit with Bricks and Bricklets


Description
-----------

The `Starter Kit: Camera Slider <#>`__ allows an automatic and fluid linear
motion of photo- and video-camera. With the provided demo application
you can control the slider freely and you can make automatic time
laps shoots. An easy API can be used to integrate the camera slider
into you own project. This means that the kit can be used as a
general purpose axis for linear motion.

The kit is build from `MakerBeams <https://www.tinkerforge.com/en/shop/makerbeam.html>`__. 
Other Beams can be attached easily.
This makes it easy to construct your own brackets that can hold
other devices. This means that the kit can be used as a
general purpose axis for linear motion.

A `Stepper Brick <https://www.tinkerforge.com/en/shop/bricks/stepper-brick.html>`__ 
moves the cart with millimeter precision and it can
be extended with other Bricks and Bricklets. It is for example possible
to automatically trigger the camera with a Industrial Quad Relay Bricklet.
A `RED Brick <https://www.tinkerforge.com/en/shop/bricks/red-brick.html>`__ 
together with a 
`HDMI display <https://www.tinkerforge.com/en/shop/accessories/red-brick/hdmi-display-5-inch.html>`__ 
can be used to implement an autonomous solution that can be controlled 
via touchscreen.

Technical Specifications
------------------------


.. _starter_kit_camera_slider_resources:

Resources
---------


Firmware updating and first tests
---------------------------------

Construction
------------

The construction of the kit is described
:ref:`here <starter_kit_camera_slider_construction>`.

.. image:: /Images/Kits/kit_camera_slider_construction_collage_800.jpg
   :scale: 100 %
   :alt: Camera Slider kit construction collage
   :align: center
   :target: ../CameraSlider/Construction.html


.. toctree::
   :hidden:

   Details <Construction>


.. _starter_kit_camera_slider_demo:

Demo Application
----------------

The demo application shows two possible uses cases for this kit:

* Linear motion
* Moving time-lapse photography

Before starting you have to configure the host and port. If you use the
standard kit and have connected it directly to your PC via USB "localhost" and
"4223" is fine. If you extended the kit by
:ref:`Extensions <primer_master_extensions>` or want to control the kit from
another PC you have to enter the IP address or hostname of the extension or
the PC where the kit is connected to.

.. image:: /Images/Kits/kit_camera_slider_demo_connection_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Connection
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_connection.jpg

Calibration
^^^^^^^^^^^

Initially the demo does not know the current position and the motion range of
the cart. Before you can move the cart around you have to calibrate its minimum
and maximum position:

* Choose the Stepper Brick mounted to the camera slider.
* Click the "Start" button to start the calibration process.
* Use the "Forward" and "Backward" buttons to move the cart close to one end of
  the frame and click the "Set Minimum" button.
* Use the "Forward" and "Backward" buttons to move the cart close to the
  opposite end of the frame and click the "Set Maximum" button.
* Click the "Apply" button to finish the calibration process.

Now the demo knows and remembers the current position and the motion range of
the cart. If the cart is moved manually then the calibration process has to be
repeated.

.. image:: /Images/Kits/kit_camera_slider_demo_calibration_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Demo Application Screenshot: Calibration
   :align: center
   :target: ../../_images/Kits/kit_camera_slider_demo_calibration.jpg

Linear Motion
^^^^^^^^^^^^^


Time Lapse
^^^^^^^^^^
