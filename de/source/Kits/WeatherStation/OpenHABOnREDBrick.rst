
.. _starter_kit_weather_station_openhab_red_brick:

Smart Home Integration mit openHAB und RED Brick
================================================

Für diese Projekt setzen wir voraus, dass eine aufgebaut
:ref:`RED Brick Wetterstation <starter_kit_weather_station_construction_red_brick>`
vorhanden ist, dass der RED Brick mit mindesten Image Version 1.6 läuft und dass
mindestens Brick Viewer 2.2.3 installiert ist.

Die in diesem Projekt verwendete openHAB Konfiguration basiert auf einem
Beispiel von einem der openHAB Entwickler. Das originale Beispiel ist auf
`GitHub <https://github.com/theoweiss/tinkerforge-RED-Brick>`__ abrufbar.

Ziele
-----

Wir setzen uns folgende Ziele für dieses Projekt:

* Temperatur, Helligkeit, Luftfeuchte und Luftdruck sollen auf dem LCD 20x4
  Bricklet angezeigt werden,
* die gemessenen Werte sollen automatisch aktualisiert werden sobald sie sich
  verändern und
* mit Knopf 0 am LCD 20x4 Bricklet soll die Hintergrundbeleuchtung des Displays
  an- und ausgeschaltet werden können.

Zusätzlich, wenn der RED Brick Netzwerkverbindung hat:

* Temperatur, Helligkeit, Luftfeuchte und Luftdruck sollen auf einer openHAB
  Sitemap im RED Brick Web Interface angezeigt werden.

Im Folgenden werden wir Schritt für Schritt zeigen wie openHAB konfiguriert
werden muss um diese Ziele zu erreichen.

Schritt 1: openHAB Service aktivieren
-------------------------------------

Der `openHAB <https://www.openhab.org/>`__ Service ist auf dem RED Brick
standardmäßig deaktiviert, da er etwas länger zum Starten benötigt und so den
Bootprozess etwas verlangsamt. Daher müssen wir zuerst openHAB aktivieren.
Die :ref:`RED Brick Services Dokumentation <red_brick_brickv_settings_services>`
erklärt wie das geht.

Schritt 2: Bricklet Items definieren
------------------------------------

Bricks und Bricklets werden in openHAB durch `Items
<https://github.com/openhab/openhab/wiki/Explanation-of-items>`__ repräsentiert.
Diese Items werden in ``.items`` Konfigurationsdateien definiert die auf dem
RED Brick gespeichert werden. Der Brick Viewer ermöglicht es diese Dateien zu
bearbeiten. Die :ref:`RED Brick openHAB Dokumentation
<red_brick_brickv_settings_openhab>` enthält mehr Details dazu.

1. Öffne den openHAB Settings Tab im Brick Viewer und klicke auf *New*.
2. Gib ``weather-station.items`` als Name ein und klicke auf *Create*.
3. Kopiere das unten stehende ``.items`` Template in das leere Textfeld.
4. Ersetze die UID Platzhalter (z.B. ``<HUMIDITY_UID>``) durch die
   entsprechenden UIDs deiner Bricklets.
5. Klicke auf *Apply Changes* um die Datei zu speichern.

Dies ist das ``.items`` Template
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.items>`__),
das in Schritt 3 verwendet wird:

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.items
 :tab-width: 4

Schritt 3: Rules definieren
---------------------------

`Rules <https://github.com/openhab/openhab/wiki/Rules>`__ ermögliches es
Ereignisse und Aktionen in Wenn-Dann artiger Weise zu verbinden. Wir nutzen
dies um die gemessenen Werte auf dem LCD 20x4 Bricklet anzuzeigen, wenn sie
sich ändern.

Erzeuge eine neue Config Datei (wie in Schritt 1 beschrieben) namens
``weather-station.rules`` mit folgendem Inhalt
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.rules>`__):

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.rules
 :tab-width: 4

* Die "Weather Station LCD Init From Backlight" Rule schreibt den fixen
  Teil des Textes auf das Display und schaltet die Hintergrundbeleuchtung ein.
* Die "Weather Station LCD Update \*" Rules aktualisieren die angezeigten
  Messwerte wenn sie sich ändern.
* Die "Weather Station LCD Backlight" Rule schaltet die Hintergrundbeleuchtung
  ein und aus, wenn Knopf 0 am LCD 20x4 Bricklet gedrückt wird.

Schritt 4: Sitemap definieren
-----------------------------

Eine `Sitemap <https://github.com/openhab/openhab/wiki/Explanation-of-Sitemaps>`__
definiert die Elemente des openHAB User Interfaces. Wir nutzen dies, um die
Messwerte im :ref:`RED Brick Web Interface <red_brick_web_interface>` anzuzeigen.

Erzeuge eine neue Config Datei (wie in Schritt 1 beschrieben) namens
``weather-station.sitemap`` mit folgendem Inhalt
(`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/openhab/weather-station.sitemap>`__):

.. literalinclude:: ../../../../../weather-station/openhab/weather-station.sitemap
 :tab-width: 4

Jetzt ist das Web Interface dieser Sitemap erreichbar unter::

 http://<RED_BRICK_IP_ADDRESS>:8080/openhab.app?sitemap=weather-station

.. image:: /Images/Kits/weather_station_openhab_orig.jpg
   :scale: 100 %
   :alt: openHAB Beispiel Sitemap
   :align: center
   :target: ../../_images/Kits/weather_station_openhab_orig.jpg

Alternativ kann auch die Sitemap auch über das RED Brick Web Interface aufgerufen
werden, da sort alle Sitemaps verlinkt sind::

 http://<RED_BRICK_IP_ADDRESS>
