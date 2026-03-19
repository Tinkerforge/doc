
.. _esp32_firmware:

ESP32 Firmware
==============

The ESP32 firmware can be compiled in multiple variations to be used on different
devices:

* :ref:`ESP32 Brick <esp32_brick>`
* :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>`
* `WARP Charger <https://www.warp-charger.com/warp1.html>`__ Smart and Pro
* `WARP2 Charger <https://www.warp-charger.com/warp2.html>`__ Smart and Pro
* `WARP3 Charger <https://www.warp-charger.com/warp3.html>`__ Smart and Pro
* `WARP Energy Manager <https://www.warp-charger.com/warp-energy-manager/>`__
* `WARP Energy Manager 2.0 <https://www.warp-charger.com/warp-energy-manager-2-0/>`__

The firmware is written and C/C++ and the source code is freely available on
`GitHub <https://github.com/Tinkerforge/esp32-firmware>`__. The
`Arduino ESP32 projekt <https://docs.espressif.com/projects/arduino-esp32/>`__
and `PlatformIO <https://platformio.org/>`__ are used as basis.

.. _esp32_firmware_setup:

Preparation
-----------

First, `UV <https://docs.astral.sh/uv/>`__ (version 0.10 or newer),
`Node.js <https://nodejs.org/>`__ (version 24 or newer)
and `Git <https://git-scm.com/>`__ have to be installed according to their
installation manuals.

In general you should always use the latest version of UV and Node.js.
For the Node.js package manager ``npm`` version 11 or newer is required.

We recommend `Visual Studio Code <https://code.visualstudio.com/>`__ as IDE.
But due to Python version conflicts, the PlatformIO IDE extension for
Visual Studio Code is not supported for this project on Windows and macOS.

For Windows the `Silicon Labs CP210x Universal Windows Driver <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`__
has to be installed. Linux and macOS have this driver already build in.

The ESP32 firmware contains a few files with very long filenames. These
might exceed the Windows legacy limit of 260 characters. It is recommended
to `enable long filename support for Windows <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#registry-setting-to-enable-long-paths>`__.

Next, clone the `esp32-firmware <https://github.com/Tinkerforge/esp32-firmware>`__
repository from GitHub using `git <https://www.git-scm.com/>`__.

For initial setup the command ``uv sync`` has to be executed in a terminal in the
``software/`` directory. The terminal inside Visual Studio Code can be used for this.

.. _esp32_firmware_build:

Firmware Building
-----------------

Choose the PlatformIO environment corresponding to the firmware variation you
want to build:

* ESP32 Brick: ``esp32`` defined in ``esp32.ini``
* ESP32 Ethernet Brick: ``esp32_ethernet`` defined in ``esp32_ethernet.ini``
* WARP Charger Smart and Pro: ``warp`` defined in ``warp.ini``
* WARP2 Charger Smart and Pro: ``warp2`` defined in ``warp2.ini``
* WARP3 Charger Smart and Pro: ``warp3`` defined in ``warp3.ini``
* WARP Energy Manager: ``energy_manager`` defined in ``energy_manager.ini``
* WARP Energy Manager 2.0: ``energy_manager_v2`` defined in ``energy_manager_v2.ini``

To build the ESP32 Brick Firmware (``esp32``), this command has to be executed in a terminal in the
``software/`` directory. The terminal inside Visual Studio Code can be used for this::

  uv run pio run -e esp32

To build a firmware, upload it to a Brick and connect to its serial console all
in one step you can run this command::

  uv run pio run -e esp32 -t upload -t montior

This requires that the Brick is connected to USB beforehand.
You can also upload the built firmware via the web interface.

The firmware file can be found in ``software/build/`` and its name ends with ``_merged.bin``
The file name has the form ``[environment]_firmware_[version]_[build timestamp][extension]``.
For example ``warp2_firmware_2_0_7_62d7d0b1_merged.bin`` is a WARP2 Charger firmware
version 2.0.7 that was built at the unix timestamp 0x62d7d0b1 = 1658310833, (i.e. 2022-07-20 13:27:02).

Firmware Structure
------------------

The functionality and the web interface of the firmware are put together from
modules. The variations of the firmware differ mostly in their list of active
modules. This list is specified per environment in the corresponding ``.ini``
file using the ``custom_backend_modules`` and ``custom_frontend_modules`` options.

The tutorial regarding the :ref:`ESP32 firmware <tutorial_esp32_firmware>`
shows step by step how to add a custom module to the firmware.

..
 TODO: WebSocket/HTTP/MQTT API der ESP32 Firmware dokumentieren, dazu den
       WARP Charger API Doc Generator refaktorisieren
