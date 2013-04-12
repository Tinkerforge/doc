
:breadcrumbs: <a href="../index.html">Startseite</a> / Device Identifier

.. _device_identifier:

Device Identifier
=================

Jeder Brick und jedes Bricklet hat einen "Device Identifier". Dieser Bezeichner
wird in der ``GetIdentity`` und in den Enumerate Callbacks benutzt. Dadurch
wird es ermöglicht Bricks und Bricklets dynamisch zu benutzen, ohne vorherige
Kenntnisse über UIDs.

In den API Bindings gibt es für jeden Brick und jedes Bricklet eine
"Device Identifier" Konstante mit dem entsprechenden Wert. Genaueres dazu findet
sich im Abschnitt über Konstanten in der jeweiligen API Dokumentation.

.. include:: Device_Identifier.table
