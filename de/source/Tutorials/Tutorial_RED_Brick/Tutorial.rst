
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#tutorials-and-faq">Tutorials und FAQ</a> / RED Brick - Tutorial

.. _tutorial_red_brick:

RED Brick - Tutorial
====================

Das folgende Tutorial zeigt wie man mit dem 
:ref:`RED Brick <red_brick>` zusammen mit anderen :ref:`Bricks <primer_bricks>` 
und :ref:`Bricklets <primer_bricklets>` Software entwickelt. Ein vollständiges
Schritt-für-Schritt Tutorial, das zeigt wie man Bricks, Bricklets und Extensions
nutzt kann in dem :ref:`Erste Schritte Tutorial <tutorial_first_steps>` gefunden
werden.

Der RED Brick kann als Gehirn des Tinkerforge Baukastensystems bezeichnet 
werden. Ein Programm, welches Bricks und Bricklets steuert, kann auf diesen 
hochgeladen und ausgeführt werden.

In diesem Tutorial werden wir die verschiedenen Fähigkeiten des RED Bricks
vorstellen. Um das Beispiel einfach zu halten nutzen wir einen kleinen Aufbau,
bestehend aus einem RED Brick, einem :ref:`Master Brick <master_brick>` und 
einem :ref:`Temperature Bricklet <temperature_bricklet>`. Später stecken wir
eine :ref:`Ethernet Extension <ethernet_extension>` hinzu um Zugriff auf das
Internet zu bekommen.

Als erstes werden wir ein einfaches Programm an einem PC entwickeln und testen 
und dieses anschließend auf den RED Brick hochladen und ausführen. Das Programm
wird einfach nur die aktuelle Temperatur ausgeben. Danach 
werden wir das Programm erweitern, so dass auch die grafischen 
Nutzerschnittstelle (GUI) genutzt wird und zeigen auf einen HDMI Monitor die
aktuelle Uhrzeit an. Im nächsten Schritt werden wir eine Web Schnittstelle 
anbieten, mit der wir auf die gemessene Temperatur zugreifen können.
Die Fähigkeiten dieses Beispiel sind sicherlich nicht sonderlich 
sinnvoll, zeigen aber die wichtigsten Möglichkeiten der Nutzung eines RED 
Bricks.

Für die eigene Anwendung werden sicher andere Bricks, Bricklets oder eine andere
Programmiersprache verwendet, als die in diesem Beispiel. Die vorgestellten 
Konzepte und Abläufe sind aber für alle im wesentlichen die gleichen.
	

Notwendige Software installieren
--------------------------------

Als erstes müssen der: :ref:`Brick Daemon <brickd>` und der
:ref:`Brick Viewer <brickv>` auf einem PC oder Mac installiert werden.
Dazu sind die dokumentierten Schritte zu befolgen:

 * :ref:`Brick Daemon Installation <brickd_installation>`
 * :ref:`Brick Viewer Installation <brickv_installation>` 

Teste den RED Brick
-------------------

Nachdem die notwendige Software installiert wurde kann der RED Brick getestet
werden. Dazu stecken wir eine Micro-SD-Karte mit
:ref:`RED Brick Software Image <red_brick_images>` in den Micro-SD-Karten Slot
des RED Bricks. Dieser befindet sich auf der Unterseite des Bricks (eine
`Micro-SD-Karte mit vorinstalliertem Image <TODO>`__ kann in unserem Shop
gefunden werden). Anschließend wir der RED Brick per Mini-USB Kabel mit dem
Rechner verbunden.

.. image:: /Images/Bricks/brick_red_mini_usb_600.jpg
   :scale: 100 %
   :alt: RED Brick mit Mini-USB-Kabel
   :align: center
   :target: ../../_images/Bricks/brick_red_mini_usb_800.jpg

Nun starten wir die Brick Viewer Software und klicken auf **Connect**. Ein Tab
mit **RED Brick** bezeichnet sollte nun auftauchen. Klicke auf diesen. Der Tab
zeigt Informationen zum Status des RED Bricks. Eine volle Beschreibung zum RED
Brick Tab der Brick Viewers ist :ref:`hier dokumentiert <red_brick_brickv>`.

Der RED Brick ist nun bereit!

Bricks und Bricklets hinzufügen
-------------------------------

Nun wissen wir das der RED Brick wie erwartet funktioniert. Bevor andere
Bricks/Bricklets hinzugesteckt werden, sollte der RED Brick heruntergefahren 
werden. Dazu klickt man in der oberen rechten Ecke auf **System**, wählt 
**shut down** und wartet bis alle LEDs aus sind. Anschließend stecken wir
den Master Brick auf den RED Brick und verbinden das Temperature Bricklet mit 
diesem.

.. image:: /Images/Bricks/brick_red_master_temp_600.jpg
   :scale: 100 %
   :alt: RED Brick mit Master Brick und Temperature Bricklet
   :align: center
   :target: ../../_images/Bricks/brick_red_master_temp_800.jpg

Danach wird der RED Brick wieder mit dem Computer verbunden, der Brick Viewer
geöffnet und auf **Connect** geklickt. Es sollten Tabs für den RED Brick, 
Master Brick und das Temperature Bricklet angezeigt werden. Klicke durch die 
Tabs um die angeschlossene Hardware zu testen.

Beispielprogramm ausführen
--------------------------

Bevor das erste eigene Programm geschrieben wird, sollte ein Blick in die API
Dokumentation der genutzten Bricks/Bricklets geworfen werden, um einen Eindruck
von deren unterstützen Funktionen zu bekommen. Jede Dokumentationsseite beginnt 
mit Beispielen. Wir empfehlen diese
Beispielprogramm zuerst auszuführen. Wir nehmen das "Simple" Beispiel des
:ref:`Temperature Bricklet API Dokumentation <temperature_bricklet_python>` und
führen es aus.

.. literalinclude:: ../Software/Bricklets/Temperature_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Dazu laden wir das **example_simple.py** Python Program herunter und ersetzen
die UID in der Zeile **UID = "XYZ"** mit der UID des Temperature Bricklets.
Die UID kann im **Setup** Tab des Brick Viewers oder im Tab des Temperature 
Bricklets gefunden werden.

Führe dieses Programm auf dem PC aus. Wenn alles wie erwartet funktioniert 
sollte die aktuelle Temperatur in der Kommandozeile ausgegeben werden.

Führe das Programm auf dem RED Brick aus
----------------------------------------

Nun haben wir das Beispiel ausgeführt und wissen nun das es korrekt 
funktioniert. Das Beispiel wartet auf eine Benutzereingabe mittels::
 
 raw_input('Press key to exit\n')

Diese Zeile dient zum verhindern, dass sich die Kommandozeile sofort beendet. 
Auf dem RED Brick wird es keine Benutzereingabe geben. Wir wollen, dass das 
Programm nur einmal die gemessene Temperatur ausgibt und sich anschließend 
beendet. Dazu entferen wir diese Zeile.

`Download (example_simple_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_simple_red.py>`__

.. literalinclude:: example_simple_red.py
 :language: python
 :linenos:
 :tab-width: 4

Nun können wir das Programm auf dem RED Brick ausführen. Die allgemeine 
Beschreibung wie Programme hochgeladen werden findet sich in der
:ref:`RED Brick Brick Viewer Beschreibung <red_brick_brickv_program>`.
Nachfolgend werden wir nur die notwendigen Schrtte beschreiben:

.. image:: /Images/Screenshots/red_brick_tutorial_upload_1.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 1
   :align: center

Als erstes öffnen wir im Brick Viewer den RED Brick Tab und wählen
den Untertab **Program** aus.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_2.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 2
   :align: center

Mit dem **New** Button öffen wir den **New Program** Wizard. Wir geben
"Temperature Logger" als Name für das Programm ein und wählen **Python** als 
Sprache. Anschließend klicken wir auf **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_3.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 3
   :align: center

Wir klicken auf  **Add Files** und wählen das **example_simple_red.py** 
Programm. Klicke auf **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_4.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 4
   :align: center

Wir werden Python Version **2.7.3**, **Script File** als Start Mode und unsere
Datei als Script File nutzen. Diese Einstellungen sind alle voreingestellt.
Wir klicken wieder auf **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_5.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 5
   :align: center

Unser einfaches Beispielprogramm benötigt keine Argumente oder 
Umgebungsvariablen, so dass wir einfach wieder auf **Next** klicken.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_6.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 6
   :align: center

Wir nutzen Pipe als Standard Input und loggen alle Ausgaben (Standard Output
und Standard Error) in einer forlaufenden Logdatei. Es sind also wieder keine 
Änderungen notwendig. Wir klicken wieder auf **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_7.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 7
   :align: center

Es gibt viele Optionen für das Scheduling des Programms. Eine der einfachsten 
Optionen ist es das Programm in einem gegebenen Intervall auszuführen. Dazu 
wählen wir **Interval** mit einer Zeit von 10 Minuten (**600 Sekunden**).
Somit wird unser Programm alle 10 Minuten ausgeführt und die Temperatur
alle 10 Minuten einmal ausgegeben.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_8.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 8
   :align: center

Die Übersichtsseite zeigt die gewählten Einstellungen. Klicke auf **Next**.

.. image:: /Images/Screenshots/red_brick_tutorial_upload_9.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Programm Uploads Schritt 9
   :align: center

Klicke auf den **Start Upload** Button um die Datei hochzuladen. Klicke 
anschließend auf **Finish**. Nun können wir der Logdatei des Programms, die 
gemessenen Temperaturen entnehmen.

TODO: Screenshots that show how log files can be viewed.

Zugriff auf das Internet bekommen
---------------------------------

Um Zugriff auf das Internet zu bekommen kann entweder ein USB WLAN oder Ethernet
Stick oder eine :ref:`Ethernet Extension <ethernet_extension>` mit dem RED Brick
verbunden werden. In diesem Beispiel werden wir eine Ethernet Extension nutzen:

.. image:: /Images/Bricks/brick_red_master_temp_600.jpg
   :scale: 100 %
   :alt: RED Brick mit Master Brick, Temperature Bricklet und Ethernet Extension
   :align: center
   :target: ../../_images/Bricks/brick_red_master_temp_800.jpg

Fahre den RED Brick herunter und entferne die Stromversorgung bevor du die 
Ethernet Extension auf den Stapel steckst.

Nachdem wirder die Stromversorgung angeschlossen wurde und der erweiterte Stapel 
fertig gebootet hat, klicke auf "Settings",
"Network" und "Wired" in dem RED Brick Tab des Brick Viewers.
Wähle **tf0** als Interface und wähle entweder DHCP oder eine statische IP.
Klicke auf **Save**.

TODO anpassen an neue Version!!!!

In dem **General** Tab wird anschließend das konfigurierte **tf0** Interface
angezeigt. Falls DHCP verwendet wird, kann es notwendig sein **Refresh** einige 
male zu klicken bis die empfangene IP Adresse angezeigt wird.

.. image:: /Images/Screenshots/red_brick_tutorial_network_general.jpg
   :scale: 100 %
   :alt: Screenshot of RED Brick network settings.
   :align: center

Nachdem wir nun Zugriff auf das Internet haben können wir IoT oder ähnliche 
Anwendungen einfach implementieren. Ein weiterer Vorteil des Internetzugriffs 
ist, dass das RED Brick automatsch die Systemzeit 
mittels `NTP <http://de.wikipedia.org/wiki/Network_Time_Protocol>`__ 
aktualisieren wird.

Somit können wir jeder Messung die entsprechende Uhrzeit zuordnen.

`Download (example_time_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_time_red.py>`__

.. literalinclude:: example_time_red.py
 :language: python
 :linenos:
 :tab-width: 4

Dieses Programm kann genauso wie das vorherige hochgeladen werden.

Entwicklung von GUI Programmen mit dem RED Brick
------------------------------------------------

.. note::
	Programme mit grafischer Nutzerschnittstelle (GUI) können nur auf dem Full
	Image ausgeführt werden.

Eine weitere Art von Programmen, die auf dem RED Brick ausgeführt werden können,
sind Programme mit grafischer Nutzerschnittstelle (GUI), die über die HDMI
Schnittstelle des Bricks angezeigt werden. In diesem Beispiel fügen wir eine 
`Qt <http://pyqt.sourceforge.net/>`__ GUI unserem einfachen Temperature Bricklet 
Programm hinzu.

`Download (example_gui_red.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/example_gui_red.py>`__

.. literalinclude:: example_gui_red.py
 :language: python
 :linenos:
 :tab-width: 4

Die GUI besitzt ein Label, dass jede Sekunde mit der aktuellen Temperatur
aktualisiert wird. Zusätzlich gibt es einen **Refresh** Button, der die 
Aktualisierung erzwingt.

Das Programm kann mit kleinen Änderungen genauso hochgeladen werden wie das 
Programm zuvor. Dabei sind zwei Änderungen vorzunehmen:

.. image:: /Images/Screenshots/red_brick_tutorial_gui_environment.jpg
   :scale: 100 %
   :alt: Screenshot der RED Brick GUI Umgebung
   :align: center

In Schritt 4 muss die Umgebungsvariable **DISPLAY** mit dem Wert **:0**
gesetzt werden. Damit wird das Programm auf dem RED Brick Desktop angezeigt.
Diese Variable muss gesetzt werden, da sonst das Programm nicht startet.

.. image:: /Images/Screenshots/red_brick_tutorial_gui_schedule.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick GUI Schedulers
   :align: center

Für den Scheduler möchte man **Always**  auswählen und **Continue After Error**
abwählen. Diese Konfiguration startet das Programm und dessen GUI automatisch 
neu wenn es beendet wurde.

Auf dem RED Brick Desktop sieht dann die kleine GUI Anwendung wie folgt aus:

.. image:: /Images/Screenshots/red_brick_tutorial_gui.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Temperature GUI.
   :align: center

Entwicklung eines eigenen RED Brick Web Interfaces
--------------------------------------------------

Wenn der RED Brick über eine Netzwerkschnittstelle verfügt (WLAN Stick oder
Ethernet Extension), dann kann er auch dazu genutzt werden um eine dynamische 
Webseite anzuzeigen. Aktuell werden HTML/JavaScript, PHP und Python 
dafür unterstützt.

Die Beschreibung der 
:ref:`RED Brick Web Interface Dokumentation <red_brick_web_interface>`
gibt mehr Informationen dazu. Im wesentlichen kann eine als Startpunkt eines 
Pfades dienende index.html, index.php oder index.py genutzt werden.

Unser einfaches Temperature Bricklet Programm mit Web Interface sieht wie folgt
aus (Python und PHP):

`Download (index.py) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/index.py>`__

.. literalinclude:: index.py
 :language: python
 :linenos:
 :tab-width: 4

`Download (index.php) <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_RED_Brick/index.php>`__

.. literalinclude:: index.php
 :language: php
 :linenos:
 :tab-width: 4

Wenn das Programm ein Web Interface nutzt, müssen
die auszuführende Datei, deren Argumente, Umgebungsvariablen und
Arbeitsverzeichnis nicht angegeben werden. Schritte 4-6 werden ausgelassen
wenn **Web Interface** in Schritt 3 ausgewählt wird.

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface_execution.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Web Interface: Ausführungskonfiguration
   :align: center

Um das eigene Web Interface aufzurufen, müssen nur die IP Adresse oder der 
Hostname des RED Bricks im Browser aufgerufen werden und der **Bin** Button
des eigenen Programms geklickt werden. Dies öffnet den Pfad zum eigenen Programm
für den die Indexdatei automatisch aufgerufen wird:

.. image:: /Images/Screenshots/red_brick_tutorial_web_interface.jpg
   :scale: 100 %
   :alt: Screenshot des RED Brick Web Interface
   :align: center

