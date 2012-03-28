.. _brickv:

Brick Viewer (brickv)
=====================

The Brick Viewer can be used to test :ref:`Bricks <product_overview_bricks>` 
and :ref:`Bricklets <product_overview_bricklets>`. Each device has its own 
view that shows the main features and allows to control them.

Additionally brickv can be used to calibrate the analog to digital converter
(ADC) of the Bricks to improve measurement quality 
(see :ref:`here <brickv_adc_calibration>`)
and to flash bricklet plugins (see :ref:`here <brickv_flash_plugin>`).

.. _brickv_installation:

Installation
------------

Windows
^^^^^^^
To install the Brick Viewer on Windows, download the
brick viewer .exe form :ref:`here <downloads_tools>`. 
Click on the downloaded file, this should open the installer:

.. image:: /Images/Screenshots/brickv_windows_1_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_windows_1.jpg

Click on "Next" to start the installation process.

.. image:: /Images/Screenshots/brickv_windows_2_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_windows_2.jpg

Next you will be the installation path will be questioned.
Change it if necessary and click "Install".

.. image:: /Images/Screenshots/brickv_windows_3_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 3
   :align: center
   :target: ../_images/Screenshots/brickv_windows_3.jpg

After this you have finished the installation process.


Linux
^^^^^

To install the Brick Viewer on a Debian based distribution 
(Ubuntu, Mint, etc.), download the Brick Viewer .deb from 
:ref:`here <downloads_tools>`. Right-click on the file and choose 
"Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickv_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_linux_1.jpg

Then click "Install Package":

.. image:: /Images/Screenshots/brickv_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_linux_2.jpg

Ready:

.. image:: /Images/Screenshots/brickv_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 3
   :align: center
   :target: ../_images/Screenshots/brickv_linux_3.jpg

In Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.
You can start the Brick Viewer in the application menu under electronic
or in the console with::

 brickv

To install Brick Viewer from the console use the following::

 sudo apt-get install python python-qt4 python-qwt5-qt4 python-matplotlib python-scipy python-opengl python-numpy python-qt4-gl
 sudo dpkg -i brickv_latest.deb

To install Brick Viewer from source, download the source from `here <https://github.com/Tinkerforge/brickv>`__ and install the dependencies:

* python-qt4 
* python-qt4-gl
* python-qwt5-qt4
* python-matplotlib
* python-scipy
* python-opengl
* python-numpy

On Debian based distributions you can do that as shown above, on other
distribution you have to search for and install the equivalent packages.

To start brickv from source, change to the directory 
brickv/src/brickv/ and start with::

 python main.py

.. note::
 
 Unfortunately Debian has at the time of writing this tutorial problems with
 the python-qwt5-qt4 in wheezy. If you use Debian wheezy and you can't
 find python-qwt5-qt4 in the repository, you have to install it from sid::

  echo 'APT::Default-Release "testing";' >> /etc/apt/apt.conf
  edit /etc/apt/sources.list, copy your non-security testing lines and change one set to sid
  apt-get update
  apt-get -t sid install python-qwt5-qt4


Mac OS X
^^^^^^^^

To install the Brick Viewer on Mac OS X, download the
.dmg form :ref:`here <downloads_tools>`. 
Click on the downloaded file, this should open the package:

.. image:: /Images/Screenshots/brickv_macos_1_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_macos_1.jpg

To install the Brick Viewer drag and drop the file to your applications folder

.. image:: /Images/Screenshots/brickv_macos_2_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_macos_2.jpg

After this you have finished the installation process.
Please restart your machine after this (otherwise the icons don't show up for
some unexplained reason).

Usage
-----

To use the Brick Viewer you have to first start the 
:ref:`Brick Daemon <brickd>` either on the same PC or on a PC in the same
network. Enter the IP (localhost if you started the Brick Daemon on the 
same PC). Press "connect". Now you can go through the tabs at the top
and test your Bricks and Bricklets.

.. image:: /Images/Screenshots/brickv_setup_tab.jpg
   :scale: 100 %
   :alt: Brickv (ADC Calibration)
   :align: center

If you click on advanced functions, you can calibrate the ADCs and
flash plugins to Bricks (see below).

.. _brickv_adc_calibration:

Brick ADC Calibration
^^^^^^^^^^^^^^^^^^^^^

If you have problems with inaccurate measurements (e.g. Linear Poti does not
reach the maximum or the voltage measurements in a stack are slightly off)
it is possible that the calibration of the ADC is to blame.

To measure analog values, the microcontrollers
on the Bricks have analog to digital converter (ADC). It is never guaranteed 
that an ADC on a microcontroller is perfectly calibrated. To overcome 
this problem, we make it possible to calibrate the ADC in your Bricks.

For the calibration you need one of the potentiometer Bricklets (Rotary Poti
or Linear Poti). Connect it to a Brick and click on "Advanced Functions" in
the Setup tab of Brick Viewer:

.. image:: /Images/Screenshots/brickv_advanced_functions_calibrate.jpg
   :scale: 100 %
   :alt: Brickv (ADC Calibration)
   :align: center

Choose the port your poti is connected to (A-D). 
Turn your poti completely to the left and press "Calibrate", then turn
your poti completely to right and press "Calibrate" again. If your ADC
wasn't calibrated well the gain and offset values should be different then
the default values (4095 and 0). You can test if the calibration works in
principle by pressing "Calibrate" when the poti is in the middle position,
then one of the values has to change (after that you have to recalibrate,
of course).


.. _brickv_flash_plugin:

Bricklet Plugin Flashing
^^^^^^^^^^^^^^^^^^^^^^^^

Flashing of Bricklet plugins into the EEPROM of the Bricklet is also
possible in the advanced functions window. The latest plugins can
be found :ref:`here <downloads_firmwares_plugins>`.

Connect a Brick (any Brick will do) via USB, start the Brick Viewer
and, click "Connect" and then click "Advanced Functions":

.. image:: /Images/Screenshots/brickv_advanced_functions_plugin.jpg
   :scale: 100 %
   :alt: Brickv (Bricklet Plugin)
   :align: center

Now connect the Bricklet that is to be flashed to the Brick. Select
the corresponding Brick and Port, click "Browse.." and select the firmware
you want to flash. If you now press "Save", the plugin will be written
to the EEPROM, then read again from the EEPROM and verified to be
correctly written. A "Check OK" or "Check Failed" window will pop up.
If the check failed, check if you selected the correct port and if the
Bricklet is connected properly. 

You can also read the UID currently written on the Bricklet and set a
new one. Note that the UID has to be in Base58 encoding
(i.e. 0-9a-zA-Z without 0 (zero), I (big i), O (big o) and l (small L)).
The only other restriction is that all Bricklet UIDs you use at the same 
time need to be unique, you can use recognizable names or patterns.
