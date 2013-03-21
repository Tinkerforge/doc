
:breadcrumbs: <a href="../index.html">Startseite</a> / Device Identifier

.. _device_identifier:

Device Identifier
=================

Jeder Brick und jedes Bricklet hat einen "Device Identifier". Dieser Bezeichner
wird in der ``GetIdentity`` und in den Enumerationsfunktionen benutzt. Dadurch
wird es ermöglicht Bricks und Bricklets dynamisch zu benutzen, ohne vorherige
Kenntnisse über UIDs.

In den API Bindings gibts es für jeden Brick und jedes Bricklet eine
"Device Identifier" Konstante mit dem entsprechenden Wert. Genaueres dazu findet
sich im Abschnitt über Konstanten in der jeweiligen API Dokumentation.

 .. csv-table::
  :header: "Device Identifier", "Device Name"
  :widths: 30, 100
 
  "11", "Brick DC"
  "13", "Brick Master"
  "14", "Brick Servo"
  "15", "Brick Stepper"
  "16", "Brick IMU"
  "", ""
  "21", "Bricklet Ambient Light"
  "23", "Bricklet Current12"
  "24", "Bricklet Current25"
  "25", "Bricklet Distance IR"
  "26", "Bricklet Dual Relay"
  "27", "Bricklet Humidity"
  "28", "Bricklet IO-16"
  "29", "Bricklet IO-4"
  "210", "Bricklet Joystick"
  "211", "Bricklet LCD 16x2"
  "212", "Bricklet LCD 20x4"
  "213", "Bricklet Linear Poti"
  "214", "Bricklet Piezo Buzzer"
  "215", "Bricklet Rotary Poti"
  "216", "Bricklet Temperature"
  "217", "Bricklet Temperature IR"
  "218", "Bricklet Voltage"
  "219", "Bricklet Analog In"
  "220", "Bricklet Analog Out"
  "221", "Bricklet Barometer"
  "222", "Bricklet GPS"
  "223", "Bricklet Industrial Digital In 4"
  "224", "Bricklet Industrial Digital Out 4"
  "225", "Bricklet Industrial Quad Relay"
  "226", "Bricklet PTC"
  "227", "Bricklet Voltage/Current"
