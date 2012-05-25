.. _embedded:

Bricks/Bricklets with Embedded Boards
=====================================


Raspberry Pi
------------

This section describes how to use Bricks/Bricklets with an 
`Raspberr Pi <http://www.raspberrypi.org/>`__ together
with Debian "squeeze".

Prepare SD Card
^^^^^^^^^^^^^^^

In the first step you have to set up squeeze on a SD Card. 
Download the latest Debian image from 
`here <http://www.raspberrypi.org/downloads>`__
and follow the necessary steps of this description:  
`http://www.raspberrypi.org/downloads <http://elinux.org/RPi_Easy_SD_Card_Setup>`__.

Download necessary Files
^^^^^^^^^^^^^^^^^^^^^^^^

Download Brickd and Brickv .deb's from :ref:`here <downloads_tools>`.
Mount SD Card and move to /home/pi


Set up Brickd/Brickv
^^^^^^^^^^^^^^^^^^^^

To install the :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer<brickv>` Software 
your Raspberry Pi has to be connected to a network.

sudo apt-get install python-twisted python-gudev libusb-1.0-0
sudo dpkg -i brickd_latest.deb

sudo apt-get install python python-qt4 python-qwt5-qt4 python-matplotlib python-scipy python-opengl python-numpy python-qt4-gl
sudo dpkg -i brickv_latest.deb

Download Brickd and Brickv from :ref:`here <downloads_tools>`.


First of all install the necessary tools:

Example Python
^^^^^^^^^^^^^^


Download  :ref:`here <downloads_tools>`.

