
.. _api_bindings_uc:

C/C++ - API Bindings for Microcontrollers
=========================================

.. note::
 The C/C++ bindings for microcontrollers are currently in beta.

The C/C++ bindings for microcontrollers allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` with a C/C++ programm running on a microcontroller. The
`ZIP file <https://www.tinkerunity.org/topic/5468-beta-version-of-the-cc-bindings-for-microcontrollers/>`__ for the bindings contains:

* in ``source/bindings`` the source code of the bindings
* in ``source/hal*`` the source code of HALs for common platforms.
* in ``examples/`` the examples for every supported Brick and Bricklet

.. _api_bindings_uc_supported_hardware:

Supported Hardware
------------------

The C/C++ bindings for microcontrollers support Co-processor Bricklets (i.e. those with a 7-pole connector),
as well as the HAT Brick and HAT Zero Brick. The older 10-pole Bricklets and other Bricks are not supported.
:ref:`See here <api_bindings_uc_api_reference>` for a complete list of supported devices.

As host (i.e. the device running your C/C++ program that uses the bindings), you can use a microcontroller
that is able to communicate over SPI or an Raspberry Pi with a :ref:`HAT Brick <hat_brick>` or :ref:`HAT Zero Brick <hat_zero_brick>`.

The bindings require a hardware abstraction layer (HAL). :ref:`See here <api_bindings_uc_hal>` for details.

If you use a microcontroller, you have to make sure, that its logic level is 3.3V. If you want to use
an AVR-based Arduino (such as the Arduino Uno or Mega), a level shifter is required.

Due to a bug with the XMC microcontroller used by the Bricklets, they don't correctly
go into a floating state on the MISO signal. This results in interference when multiple
Bricklets are used on the same SPI bus. To be able to use multiple bricklets, a
tri-state buffer chip controlled by the chip select signal has to be used.
In the near future, there will be a new version of the Breakout Bricklet that allows you to use
multiple bricklets without interference on the MISO signal.

Requirements
------------

* C compiler (C99 compatible) or C++ compiler

.. _api_bindings_uc_install:

Installation
------------

.. note:
 The C/C++ bindings for microcontrollers are available in the
 `TinkerUnity <https://www.tinkerunity.org/topic/5468-beta-version-of-the-cc-bindings-for-microcontrollers/>`__ for the beta phase.

Because there is no precompiled library for the bindings there is nothing
to install as such. The recommended way of using the bindings is to include their
bindings and your preferred HAL directly into your C/C++ project.

Testing an Example
------------------

The examples for each supported Brick and Bricklet are not self-contained, as they
depend on the host hardware (and its HAL) you want to use. Many HALs contain an example driver that can run any example. See the specific HAL documentation for examples.

.. _api_bindings_uc_hal:

Hardware Abstraction Layer
--------------------------

The C/C++ bindings for microcontrollers work somewhat different to the other available bindings.
While other bindings, that communicate to a Brick Daemon over TCP/IP, require a IP connection,
the C/C++ bindings for microcontrollers require usage of a hardware abstraction layer (HAL).
The HAL is an abstraction over the platform specific way to communicate over SPI.

The bindings already contain HALs for the following platforms.
For other platforms, a custom HAL must be implemented (see below).

* :ref:`HAL Arduino <api_bindings_uc_hal_arduino>` for Arduino compatible boards with an AVR or ARM processor
* :ref:`HAL Arduino ESP32 <api_bindings_uc_hal_arduino_esp32>` for Arduino compatible boards with ESP32 processor
* :ref:`HAL Linux <api_bindings_uc_hal_linux>` for Linux systems with spidev-support
* :ref:`HAL Raspberry Pi <api_bindings_uc_hal_raspberry_pi>` for Raspberry Pi 2, 3, 4, and Zero with the BCM2835 chip.
* :ref:`HAL STM32F0 <api_bindings_uc_hal_stm32f0>` for the STM32F0 microcontroller.


Implementing a Custom HAL
-------------------------

If you want to use the bindings on another platform, you have to implement
a custom HAL. :ref:`This guide <api_bindings_uc_custom_hal>` shows how.

.. _api_bindings_uc_callbacks:

Callbacks
---------

Callbacks in the C/C++ bindings for microcontrollers work differently than
those in the other bindings. As there is no multi-threading on many of the
target platforms, there is no automatic polling for callbacks. Instead, if
you want to receive callbacks, you have to poll for them yourself with the
``tf_hal_callback_tick`` available in every HAL. This function will poll any
device with a registered callback handler for new packets.

Callbacks are not dispatched by another thread, but instead while
executing a getter, setter or the ``tf_hal_callback_tick`` function.
Because of this, callback handlers will run while the internal state
machines of the bindings are in states, that do not support sending other
packets. Because of this,
**calling getters, setters or tick functions inside a callback handler is not allowed**.

To keep the bindings allocation-free, no high level callbacks are supported.
High level callbacks are those, that use the streaming concept, I.e. send a
payload of dynamic length or one that does not fit in a single TFP packet.
You can instead use the low level callbacks and reassemble the payload yourself
if you need the complete payload at the same time. For some use cases, for
example if you want to find the pixel with the highest temperature in the
:ref:`Thermal Imaging Bricklet <thermal_imaging_bricklet>` linear temperature
image, you don't need to reassemble the payload, as you can just search over
each chunk one after another.

.. _api_bindings_uc_thread_safety:

Thread safety
-------------

As the primary target for these bindings are microcontrollers,
the bindings are **not** thread safe. Some HALs support cooperative
multi-tasking, however no calls to the bindings API are allowed when
they have yielded. All functions will return ``TF_E_LOCKED``
if called inside a callback handler or while the bindings are yielded.

.. _api_bindings_uc_performance:

Optimizing Performance
----------------------

To get the best performance out of the bindings, you can follow this list
of optimizations:

* Increase the SPI clock speed from 1.4 MHz to as close to 2 MHz as you can.
  Note that a too high clock speed will result in worse performance, as the attached
  Devices will fail to receive the payload. In our tests, the best performance can be
  reached at about 1.95 to 1.96 MHz, however this depends on your setup, the used HAL,
  as well as the stability of the host system's SPI clock.

  .. note:
   Regulatory testing is done with the default SPI clock speed.
   If CE compatibility or similar is necessary in your applications we recommend to not
   change the SPI clock speed.

* Prefer to use callbacks. The bindings can poll a device for an available callback
  by clocking out a single byte. If you use getters to poll for rapidly changing state,
  a complete TFP request, response and acknowledgement must be sent over SPI, resulting
  in at least 23 bytes of data to send.

* If you know exactly what callbacks to expect in what intervals,
  don't use ``tf_hal_callback_tick``, instead use your own scheduling to poll
  with the specific ``tf_[device]_callback_tick`` functions. This allows spending
  more time on other tasks instead of polling the devices all the time.
  ``tf_hal_callback_tick`` uses a round-robin scheduler to poll
  all devices with a registered callback handler.

* If multiple SPI devices are available, use multiple HAL instances. This will
  only work with HALs that support using a specific SPI device. However you can
  then communicate with multiple Devices in parallel. Each HAL instance may still
  only be used by a single thread.

.. _api_bindings_uc_flash_size:

Optimizing Flash and RAM Usage
------------------------------

To fit a firmware using the bindings onto smaller platforms, such
as the Arduino Uno, you can change the following configuration options
in :file:`bindings/config.h`:

* ``TF_INVENTORY_SIZE``:
  This is the size of the inventory i.e. the mapping from
  UIDs to the ports under which they are reachable.
  If you know exactly how many devices you want to communicate with,
  set the inventory size to this number. Note that the HAL initialization
  will return ``TF_E_TOO_MANY_DEVICES`` if the inventory size is too small.
* ``TF_IMPLEMENT_CALLBACKS``:
  If you don't want to use callbacks, remove this define to remove the
  callback implementation.
* ``TF_LOG_LEVEL``:
  Reducing the log level will remove string constants at compile time.
  Valid values are

  * ``TF_LOG_LEVEL_NONE``: Disables the logging completely
  * ``TF_LOG_LEVEL_ERROR``: Logs only some HAL specific errors if they occur.
  * ``TF_LOG_LEVEL_INFO``: Additionally logs the initial list of detected devices (default)
  * ``TF_LOG_LEVEL_DEBUG``: Additionally logs all internal state changes in the SPITFP state machine

* ``TF_IMPLEMENT_STRERROR``:
  If you remove this define, the tf_hal_strerror function will not be implemented. This saves about
  500 bytes of flash or RAM, depending on the HAL.

.. _api_bindings_uc_api_reference:

API Reference and Examples
--------------------------

Links to the API reference for the HALs, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: API_Bindings_uC_links.table

.. toctree::
   :hidden:

   HAL Arduino <API_Bindings_uC_HAL_Arduino>
   HAL Arduino ESP32 <API_Bindings_uC_HAL_Arduino_ESP32>
   HAL Linux <API_Bindings_uC_HAL_Linux>
   HAL Raspberry Pi <API_Bindings_uC_HAL_Raspberry_Pi>
   HAL STM32F0 <API_Bindings_uC_HAL_STM32F0>
   Custom HAL <API_Bindings_uC_Custom_HAL>
   Bricks <Bricks_uC>
   Bricks (Discontinued) <Bricks_uC_Discontinued>
   Bricklets <Bricklets_uC>
   Bricklets (Discontinued) <Bricklets_uC_Discontinued>
