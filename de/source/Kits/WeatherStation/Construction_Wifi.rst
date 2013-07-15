
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html#konstruktion">Starterkit: Wetterstation</a> / Konstruktion: WLAN Wetterstation

.. include:: WeatherStation.substitutions

.. _starter_kit_weather_station_construction_wifi:

Konstruktion: WLAN Wetterstation
================================

Die Wetterstation ist groß genug um eine :ref:`WIFI Extension <wifi_extension>`
einzubauen um die Station drahtlos zu steuern. In dieser Anleitung werden wir
eine :ref:`Step-Down Power Supply <step_down_power_supply>` zusammen mit
einem :ref:`DC Jack Adapter <dc_jack_adapter>` nutzen um die Station mit Strom
zu versorgen. Als Alternative wäre es auch möglich die Station über eine
USB Power Supply zu versorgen, dann wären DC Jack Adapter und Step-Down
Power Supply nicht notwendig.

Dieser Aufbau ist eine Erweiterung der :ref:`Basisversion
<starter_kit_weather_station_construction_basic>`. Daher sollte zuerst die
Basisversion aufgebaut und dann, wie im Folgenden beschrieben, abgewandelt
werden.

Stapel an Rückseite
-------------------

Wir starten damit den Stapel, bestehend aus Step-Down Power Supply,
Master Brick und WIFI Extension auf die Rückseite des Gehäuses zu schrauben.
Es ist eine Aussparung vorhanden damit die Step-Down Power Supply
auch ohne Abstandsbolzen direkt auf die Rückseite geschraubt werden kann.

.. image:: /Images/Kits/weather_station_construction_wifi_stack_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_stack_1200.jpg

DC Jack Adapter an Rückseite
----------------------------

Der DC Jack Adapter kann auf die Rückseite mit einem 21mm Abstandshalter
aufgeschraubt werden. Dieser wird aus einem 9mm und einem 12mm Abstandshalter
aufgebaut. Dieser Abstandshalter wird wiederum über eine Schraube an der
Rückseite des Gehäuses geschraubt. Der DC Jack Adapter wird mit einer Mutter
befestigt.

Wenn alles korrekt verschraubt ist, sollte der DC Jack Adapter in die
Aussparung in dem Seitenteil passen.

.. image:: /Images/Kits/weather_station_construction_wifi_dc_jack_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_dc_jack_1200.jpg

Das war's! Wir müssen nun nur wieder die Vorderseite auf die Rückseite
schrauben. Falls eine Tinkerforge Antenne genutzt werden soll, so muss dies die
große RP-SMA oder die Externe sein. Die kleine Antenne passt nicht.

.. image:: /Images/Kits/weather_station_construction_wifi_ready_350.jpg
   :scale: 100 %
   :alt: WLAN Wetterstation Aufbau Schritt 3
   :align: center
   :target: ../../_images/Kits/weather_station_construction_wifi_ready_1200.jpg
