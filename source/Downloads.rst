.. _downloads:

Downloads
=========

   By downloading any of our software you agree to the following terms::

     OUR SOFTWARE IS PROVIDED TO YOU "AS IS". WITHOUT WARRENTY OF ANY KIND, 
     EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
     WE EXPRESSLY DISCLAIM ANY LIABILITY WHATSOEVER FOR ANY DIRECT, INDIRECT, 
     CONSEQUENTIAL, INCIDENTAL OR SPECIAL DAMAGES, INCLUDING, WITHOUT 
     LIMITATION, LOST REVENUES, LOST PROFITS, LOSSES RESULTING FROM BUSINESS 
     INTERRUPTION OR LOSS OF DATA, REGARDLESS OF THE FORM OF ACTION OR LEGAL 
     THEORY UNDER WHICH THE LIABILITY MAY BE ASSERTED, EVEN IF ADVISED OF THE 
     POSSIBILITY OR LIKELIHOOD OF SUCH DAMAGES.

   This page only contains compiled programs and firmwares. The source code
   for all of these programs and firmwares can be found :ref:`here <source_code>`.
   
.. terms from arduino.cc, and berkely-based copyrights

   
.. _downloads_tools:

Tools
-----

.. csv-table::
 :header: "Tool", "Download", "Description"
 :delim: |
 :widths: 20, 30, 60

 **Brick Daemon** | `deb <http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest.deb>`__, rpm*, dmg* , `exe <http://download.tinkerforge.com/tools/brickd/windows/brickd_windows_latest.exe>`__, `src <https://github.com/Tinkerforge/brickd>`__ | For Linux (.deb based, .rpm based), Mac OS, Windows and Source Code. [:ref:`Installation Instructions <brickd>`]
 **Brick Viewer** | `deb <http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb>`__, rpm*, dmg* , `exe <http://download.tinkerforge.com/tools/brickv/windows/brickv_windows_latest.exe>`__, `src <https://github.com/Tinkerforge/brickv>`__ | For Linux (.deb based, .rpm based), Mac OS, Windows and Source Code. [:ref:`Installation Instructions <brickv>`]
 **SAM-BA** | `Windows <http://www.atmel.com/dyn/resources/prod_documents/sam-ba_2.11.exe>`__, `Linux <http://www.atmel.com/dyn/resources/prod_documents/sam-ba_2.11.zip>`__ | For Linux and Windows, SAM-BA for Mac OS not yet available. [:ref:`Installation Instructions <flash_firmware_on_brick>`]
 **SAM-BA Files** | `Download <http://download.tinkerforge.com/tools/samba/samba_files_latest.zip>`__ | Contains bootloader for Bricks, has to be unziped inside SAM-BA. [:ref:`Installation Instructions <flash_firmware_on_brick>`]

You will need the Brick Daemon if you want to use any Bricks and Bricklets. The Brick Viewer is for testing purposes and not absolutely necessary. If you want to flash new firmwares onto Bricks, you need to download SAM-BA from the Atmel website and extract the SAM-BA Files into the SAM-BA folder. For flashing Bricklet Plugins, the Brick Viewer can be used. 

If you use a linux distribution that does not use .debs or .rpms, you can install the Brick Viewer and the Brick Daemon from source.

\*: Coming soon

For older Versions click `here <http://download.tinkerforge.com/tools/>`__.

.. _downloads_bindings_examples:

Bindings and Examples
---------------------

.. csv-table::
 :header: "", "Bindings and Examples"
 :delim: |
 :widths: 10, 60

 **Language** | `C/C++ <http://download.tinkerforge.com/bindings/c/tinkerforge_c_bindings_latest.zip>`__, `C# <http://download.tinkerforge.com/bindings/csharp/tinkerforge_csharp_bindings_latest.zip>`__, `Java <http://download.tinkerforge.com/bindings/java/tinkerforge_java_bindings_latest.zip>`__, `Python <http://download.tinkerforge.com/bindings/python/tinkerforge_python_bindings_latest.zip>`__

The zip for each language contains all bindings and all available examples for the language. A tutorial on how to use the bindings can be found :ref:`here <api_bindings>`.

For older Versions click `here <http://download.tinkerforge.com/bindings/>`__.



.. _downloads_firmwares_plugins:

Brick Firmwares and Bricklet Plugins
------------------------------------

.. csv-table::
 :header: "", "Firmwares and Plugins"
 :delim: |
 :widths: 10, 60

 **Bricks** | `DC <http://download.tinkerforge.com/firmwares/bricks/dc/brick_dc_firmware_latest.bin>`__, `IMU <http://download.tinkerforge.com/firmwares/bricks/imu/brick_imu_firmware_latest.bin>`__, `Master <http://download.tinkerforge.com/firmwares/bricks/master/brick_master_firmware_latest.bin>`__, `Servo <http://download.tinkerforge.com/firmwares/bricks/servo/brick_servo_firmware_latest.bin>`__, `Stepper <http://download.tinkerforge.com/firmwares/bricks/stepper/brick_stepper_firmware_latest.bin>`__
 **Bricklets** | `Ambient Light <http://download.tinkerforge.com/firmwares/bricklets/ambient_light/bricklet_ambient_light_firmware_latest.bin>`__, `Current12 <http://download.tinkerforge.com/firmwares/bricklets/current12/bricklet_current12_firmware_latest.bin>`__, `Current25 <http://download.tinkerforge.com/firmwares/bricklets/current25/bricklet_current25_firmware_latest.bin>`__, `Distance IR <http://download.tinkerforge.com/firmwares/bricklets/distance_ir/bricklet_distance_ir_firmware_latest.bin>`__, `Dual Relay <http://download.tinkerforge.com/firmwares/bricklets/dual_relay/bricklet_dual_relay_firmware_latest.bin>`__, `Humidity <http://download.tinkerforge.com/firmwares/bricklets/humidity/bricklet_humidity_firmware_latest.bin>`__, `IO 16 <http://download.tinkerforge.com/firmwares/bricklets/io16/bricklet_io16_firmware_latest.bin>`__, `IO 4 <http://download.tinkerforge.com/firmwares/bricklets/io4/bricklet_io4_firmware_latest.bin>`__, `Joystick <http://download.tinkerforge.com/firmwares/bricklets/joystick/bricklet_joystick_firmware_latest.bin>`__, `LCD 16x2 <http://download.tinkerforge.com/firmwares/bricklets/lcd_16x2/bricklet_lcd_16x2_firmware_latest.bin>`__, `LCD 20x4 <http://download.tinkerforge.com/firmwares/bricklets/lcd_20x4/bricklet_lcd_20x4_firmware_latest.bin>`__, `Linear Poti <http://download.tinkerforge.com/firmwares/bricklets/linear_poti/bricklet_linear_poti_firmware_latest.bin>`__, `Piezo Buzzer <http://download.tinkerforge.com/firmwares/bricklets/piezo_buzzer/bricklet_piezo_buzzer_firmware_latest.bin>`__, `Rotary Poti <http://download.tinkerforge.com/firmwares/bricklets/rotary_poti/bricklet_rotary_poti_firmware_latest.bin>`__, `Temperature <http://download.tinkerforge.com/firmwares/bricklets/temperature/bricklet_temperature_firmware_latest.bin>`__, `Temperature IR <http://download.tinkerforge.com/firmwares/bricklets/temperature_ir/bricklet_temperature_ir_firmware_latest.bin>`__, `Voltage <http://download.tinkerforge.com/firmwares/bricklets/voltage/bricklet_voltage_firmware_latest.bin>`__

The Brick firmwares can be flashed onto Bricks with SAM-BA (:ref:`tutorial <brickv_flash_plugin>`) and the Bricklet plugins can be written onto Bricklets with the Brick Viewer (:ref:`tutorial <flash_firmware_on_brick>`).

For older Versions click `here <http://download.tinkerforge.com/firmwares/>`__.
