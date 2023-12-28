
.. _tutorial_esp32_firmware:

Tutorial - ESP32 Firmware
=========================

Die :ref:`ESP32 Firmware <esp32_firmware>` ist modular aufgebaut und nutzt
`PlatformIO <https://platformio.org/>`__. Dieses Tutorial zeigt wie die ESP32
Firmware um ein eigenes Modul erweitert werden kann. Exemplarisch wird ein Modul zur
Interaktion mit einem :ref:`RGB LED Button Bricklet <rgb_led_button_bricklet>`
entwickelt. Als Editor wird Visual Studio Code verwendet.

.. image:: /Images/Tutorial/tutorial_esp32_hardware_600.jpg
   :scale: 100 %
   :alt: ESP32 Ethernet Brick mit angeschlossenem RGB LED Button Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_hardware_1200.jpg

Als erster Schritt muss das Bauen der ESP32 Standard-Firmware
vorbereitet werden. Dazu sollte die Schritte aus der 
:ref:`ESP32 Firmware Dokumentation <esp32_firmware_setup>`
durchgeführt werden.

Alle Pfade und Dateinamen in diesem Tutorial beziehen sich auf das ``software/``
Verzeichnis der ESP32 Firmware. Achte bitte auch darauf das ``software/``
Verzeichnis in Visual Studio Code als PlatformIO Projekt-Verzeichnis zu öffnen.

Dieses Tutorial ist in fünf Phasen unterteilt. Die jeweiligen Ausbaustufen des
neuen Moduls liegen unbenutzt der ESP32 Firmware bereits bei und werden hier
Schritt für Schritt erklärt.

Es können der :ref:`ESP32 Brick <esp32_brick>` und der
:ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` für dieses Tutorial verwendet
werden. Der einzige Unterschied zwischen den beiden Bricks ist welche ``.ini``
Datei im Laufe des Tutorial abgeändert werden muss:

* ESP32 Brick: ``esp32.ini``
* ESP32 Ethernet Brick: ``esp32_ethernet.ini``

Um das jeweilige Tutorial-Modul zu aktivieren muss dessen Name am Ende der
Optionen ``custom_backend_modules`` und ``custom_frontend_modules`` der entsprechenden
``.ini`` Datei hinzufügt werden und die Firmware mittels "Upload and Monitor"
Ausgabe in Visual Studio Code neu gebaut und auf den Brick geflasht werden.

Phase 1: Leeres Modul anlegen
-----------------------------

Am Ende der ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei wird wie oben
beschrieben ``Tutorial Phase 1`` den Backend- und Frontend-Modulen hinzugefügt.

Nachdem das Projekt neu compiliert und geflasht wurde taucht im Webinterface 
das neue Modul als eine leere Unterseite namens "Tutorial (Phase 1)" auf:

.. image:: /Images/Tutorial/tutorial_esp32_phase_1_frontend_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 1)
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_1_frontend_de_1200.png

Auf der seriellen Konsole wird die Meldung ``Tutorial (Phase 1) module initialized``
ausgegeben:

.. image:: /Images/Tutorial/tutorial_esp32_phase_1_backend_600.png
   :scale: 100 %
   :alt: Serielle Konsole (Phase 1)
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_1_backend_600.png

Module teilen sich in zwei Gruppen auf:

* **Backend**: Diese sind Teil der Firmware und werden in C/C++ programmiert.
  Backend-Module stellen die eigentliche Funktionalität bereit und können mit
  der Hardware kommunizieren. Backend-Module befinden sich unter: ``src/modules/``
* **Frontend**: Diese sind Teil des Webinterfaces und werden in
  HTML/Sass/TypeScript programmiert. Frontend-Module stellen die
  Benutzerschnittstelle bereit und können mit den Backend-Modulen kommunizieren.
  Frontend-Module befinden sich unter: ``web/src/modules/``

Typischerweise treten Module in Backend/Frontend-Paaren auf, dies ist aber nicht
zwingend. Es kann Backend-Module ohne entsprechendes Frontend-Modul geben und
anders herum.

Aus dem Modulname in der ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei leitet
sich der Verzeichnisname für das Modul ab. Aus ``Tutorial Phase 1`` wird
``tutorial_phase_1`` (alle Zeichen zu Kleinbuchstaben umwandeln und Leerzeichen
durch Unterstriche ersetzen).

Dateien eines Backend-Moduls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedes Backend-Modul wird durch eine C++ Klasse repräsentiert. Der Name dieser
Klasse leitet sich auch wieder aus dem Modulnamen ab. Aus ``Tutorial Phase 1``
wird ``TutorialPhase1`` (alle Leerzeichen entfernen).

Die Backend-Modul-Klasse muss in einer Header-Datei deklariert werden, deren
Name dem Verzeichnisnamen des Moduls entspricht und ``.h`` angehängt hat. In
diesem Fall also ``tutorial_phase_1.h``.

Alle Dateien im Modulverzeichnis, die auf ``.cpp``, ``.c`` oder ``.h`` enden,
werden unabhängig von ihrem Namen mit in die Firmware kompiliert.

Dateien eines Frontend-Moduls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedes Frontend-Modul kann optional folgende Dateien beinhalten:

* **navbar.html**: HTML des Menüeintrags des Moduls. Der Menüeintrags wird
  dynamisch ein- und ausgeblendet, abhängig davon ob das entsprechende
  Backend-Modul erfolgreich initialisiert werden konnte.
* **content.html**: HTML der Unterseite des Moduls. Dies stellt die
  Benutzerschnittstelle des Moduls dar.
* **status.html**: HTML des Eintrags des Moduls auf der Statusseite. Die
  Statusseite stellt einen Übersicht der Module dar.
* **api.ts**: TypeScript-Definition der Backend-API die dieses Frontend-Modul
  nutzt.
* **main.tsx**: TypeScript-Code der für dieses Modul ausgeführt wird.
* **translation_de.json**: Deutsche Übersetzung der Texte des Moduls.
* **translation_en.json**: Englische Übersetzung der Texte des Moduls.

Phase 2: Kommunikation Backend zu Frontend
------------------------------------------

Modulname für die ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei: ``Tutorial Phase 2``
(Änderung des Eintrags von ``Phase 1`` zu ``Phase 2`` sowohl bei den Backend- als auch
bei den Frontend-Modulen).

Mit diesem Modul aktiviert taucht im Webinterface eine Unterseite mit Farbanzeige
namens "Tutorial (Phase 2)" auf:

.. image:: /Images/Tutorial/tutorial_esp32_phase_2_frontend_red_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 2), Farbe Rot
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_2_frontend_red_de_1200.png

Die Farbe wird dabei durch das Backend-Modul festgelegt und an das Frontend-Modul
kommuniziert. Dies funktioniert wie folgt:

Backend-Teil der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das Backend-Modul repräsentiert die Daten, die zum Frontend-Modul kommuniziert
werden sollen, strukturiert als ``ConfigRoot`` Objekt. In diesem Fall ist nur
ein Element namens ``color`` vorhanden, das als Wert einen String mit exakt 7 Byte
Länge hat, um eine Farbe in HTML Notation ``#RRGGBB`` zu speichern. Der Wert
``#FF0000`` stellt die Farbe Rot dar. Auszug aus ``tutorial_phase_2.cpp`` dazu:

.. code-block:: cpp

    void TutorialPhase2::pre_setup()
    {
        tutorial_config = Config::Object({
            {"color", Config::Str("#FF0000", 7, 7)}
        });
    }

Damit die Farbe an das Frontend-Modul kommuniziert wird, muss das ``ConfigRoot``
Objekt dem API Manager als Zustand bekannt gemacht werden. Dafür wird der Name
``tutorial_phase_2/config`` verwendet. Der API Manager überprüft dann alle 1000
Millisekunden das ``ConfigRoot`` Objekt auf Änderungen und schickt diese
automatisch an das Frontend-Modul. Auszug aus ``tutorial_phase_2.cpp`` dazu:

.. code-block:: cpp

    void TutorialPhase2::register_urls()
    {
        api.addState("tutorial_phase_2/config", &tutorial_config, {}, 1000);
    }

Frontend-Teil der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das Frontend-Modul legt in seiner ``api.ts`` Datei die Struktur der Daten fest,
die es vom Backend-Modul empfangen will:

.. code-block:: ts

    export interface config
    {
        color: string
    }

In der ``main.ts`` Datei wird ein Event-Listener für den Zustand
``tutorial_phase_2/config`` erzeugt, damit die lokale Funktion ``update_config``
aufgerufen wird, wenn vom API Manager Änderungen mitgeteilt werden:

.. code-block:: ts

    export function add_event_listeners(source: API.APIEventTarget)
    {
        source.addEventListener("tutorial_phase_2/config", update_config);
    }

In der ``update_config`` Funktion wird der aktuelle Wert des
``tutorial_phase_2/config`` Zustand abgefragt und der enthaltene Farbwert zur
Anzeige an das HTML Element ``#tutorial_phase_2_color`` zugewiesen:

.. code-block:: ts

    function update_config()
    {
        let config = API.get("tutorial_phase_2/config");
        $("#tutorial_phase_2_color").val(config.color);
    }

Test der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^

Als Test kann der Farbwert in ``tutorial_phase_2.cpp`` von ``#FF0000`` (Rot) zu
``#0000FF`` (Blau) geändert werden:

.. code-block:: cpp
   :emphasize-lines: 4

    void TutorialPhase2::pre_setup()
    {
        tutorial_config = Config::Object({
            {"color", Config::Str("#0000FF", 7, 7)}
        });
    }

Jetzt wird im Webinterface Blau angezeigt:

.. image:: /Images/Tutorial/tutorial_esp32_phase_2_frontend_blue_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 2), Farbe Blau
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_2_frontend_blue_de_1200.png

Phase 3: Kommunikation Frontend zu Backend
------------------------------------------

Modulname für die ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei: ``Tutorial Phase 3``

Mit diesem Modul aktiviert taucht im Webinterface eine Unterseite mit Farbanzeige
namens "Tutorial (Phase 3)" auf:

.. image:: /Images/Tutorial/tutorial_esp32_phase_3_frontend_red_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 3), Farbe Rot
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_3_frontend_red_de_1200.png

Die Farbe kann jetzt über den Auswahldialog geändert werden.

Frontend-Teil der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In der ``main.ts`` Datei wird dem ``change`` Events des HTML Elements die
lokale Funktion ``save_config`` zugewiesen. Diese wird dann bei Änderung der
Farbe aufgerufen:

.. code-block:: ts

    export function init()
    {
        $("#tutorial_phase_3_color").on("change", save_config);
    }

In der ``save_config`` Funktion wird der aktuelle Farbwert des HTML Elements
abgefragt, damit ein neuer Wert für den ``tutorial_phase_3/config`` Zustand
erstellt und dieser an das Backend-Modul übertragen:

.. code-block:: ts

    function save_config()
    {
        let config = {"color": $("#tutorial_phase_3_color").val().toString()}
        API.save("tutorial_phase_3/config", config, __("tutorial_phase_3.script.save_config_failed"));
    }

Backend-Teil der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das Backend-Modul repräsentiert die Daten, die vom Frontend-Modul empfangen
werden können, strukturiert als ``ConfigRoot`` Objekt. Dies wird einfach
als Kopie ``tutorial_config_update`` des ersten ``ConfigRoot`` Objekts angelegt,
da es die gleiche Struktur hat. Auszug aus ``tutorial_phase_3.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 7

    void TutorialPhase3::pre_setup()
    {
        tutorial_config = Config::Object({
            {"color", Config::Str("#FF0000", 7, 7)}
        });

        tutorial_config_update = tutorial_config;
    }

Damit die Farbe vom Frontend-Modul empfangen werden kann, muss das zweite
``ConfigRoot`` Objekt dem API Manager als Kommando bekannt gemacht werden.
Dafür wird der Name ``tutorial_phase_3/config_update`` verwendet. Der API Manager
empfängt die Daten vom Frontend-Modul und ruft die Lambda-Funktion auf, um die
Daten zu behandeln. Es wird eine Meldung auf die serielle Konsole ausgegeben und
die neue Farbe gespeichert. Auszug aus ``tutorial_phase_3.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 5,6,8,9,10

    void TutorialPhase3::register_urls()
    {
        api.addState("tutorial_phase_3/config", &tutorial_config, {}, 1000);

        api.addCommand("tutorial_phase_3/config_update", &tutorial_config_update, {}, [this]() {
            String color = tutorial_config_update.get("color")->asString();

            logger.printfln("Tutorial (Phase 3) module received color update: %s", color.c_str());
            tutorial_config.get("color")->updateString(color);
        }, false);
    }

Test der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^

Als Test kann der Farbwert im Webinterface von ``#FF0000`` (Rot) zu
``#00FF00`` (Grün) geändert werden:

.. image:: /Images/Tutorial/tutorial_esp32_phase_3_frontend_green_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 3), Farbe Grün
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_3_frontend_green_de_1200.png

Auf der seriellen Konsole wird die Meldung ``Tutorial (Phase 3) module received
color update: #00ff00`` ausgegeben:

.. image:: /Images/Tutorial/tutorial_esp32_phase_3_backend_600.png
   :scale: 100 %
   :alt: Serielle Konsole (Phase 3)
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_3_backend_600.png

Phase 4: Kommunikation Backend zu Bricklet
------------------------------------------

Modulname für die ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei: ``Tutorial Phase 4``

Ab dieser Phase wird vorausgesetzt, dass am Brick ein
:ref:`RGB LED Button Bricklet <rgb_led_button_bricklet>` angeschlossen ist. Der
Bricklet-Anschluss kann dabei frei gewählt werden.

Mit diesem Modul aktiviert taucht im Webinterface eine Unterseite mit Farbanzeige
namens "Tutorial (Phase 4)" auf:

.. image:: /Images/Tutorial/tutorial_esp32_phase_4_frontend_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 4)
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_4_frontend_de_1200.png

Die Farbe kann jetzt über den Auswahldialog geändert und an das Backend-Modul
und dadurch an das RGB LED Button Bricklet kommuniziert werden.

Die Kommunikation von Frontend zu Backend ist gleichgeblieben. Es wird jetzt
zusätzlich im Backend mit dem RGB LED Button Bricklet über die
:ref:`C/C++ Bindings für Mikrocontroller <api_bindings_uc>` kommuniziert. Dazu
wird ein RGB LED Button Bricklet Objekt angelegt. Das zweite Parameter der
:c:func:`tf_rgb_led_button_create <tf_rgb_led_button_create>` Funktion kann
verwendet werden, um per UID oder
Port-Namen anzugeben welches RGB LED Button Bricklet gemeint ist. Wird dieser
Parameter auf ``nullptr`` gesetzt, dann wird das erste verfügbare RGB LED Button
Bricklet verwendet. Falls das RGB LED Button Bricklet Objekt nicht erzeugt
werden kann, dann wird der Aufruf der ``setup`` Funktion vorzeitig beendet,
bevor ``initialized`` auf true gesetzt wird. Dadurch blendet sich das
Frontend-Modul auf dem Webinterface aus, da das benötige Backend-Modul nicht
zur Verfügung steht. Auszug aus ``tutorial_phase_4.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 3,4,5,6,8

    void TutorialPhase4::setup()
    {
        if (tf_rgb_led_button_create(&rgb_led_button, nullptr, &hal) != TF_E_OK) {
            logger.printfln("No RGB LED Button Bricklet found, disabling Tutorial (Phase 4) module");
            return;
        }

        set_bricklet_color(tutorial_config.get("color")->asString());

        logger.printfln("Tutorial (Phase 4) module initialized");

        initialized = true;
    }

Initial und bei Änderung der Farbe durch das Frontend-Modul wird die
``set_bricklet_color`` Funktion aufgerufen, um die LED Farbe des Bricklets zu
ändern. Auszug aus ``tutorial_phase_4.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 10

    void TutorialPhase4::register_urls()
    {
        api.addState("tutorial_phase_4/config", &tutorial_config, {}, 1000);

        api.addCommand("tutorial_phase_4/config_update", &tutorial_config_update, {}, [this]() {
            String color = tutorial_config_update.get("color")->asString();

            logger.printfln("Tutorial (Phase 4) module received color update: %s", color.c_str());
            tutorial_config.get("color")->updateString(color);
            set_bricklet_color(color);
        }, false);
    }

Die ``set_bricklet_color`` Funktion nimmt die Farbe in HTML Notation
``#RRGGBB`` entgegen und zerlegt diese in die Rot-, Grün- und Blau-Anteile, um
diese dann per :c:func:`tf_rgb_led_button_set_color <tf_rgb_led_button_set_color>`
Funktion an das Bricklet zu senden. Auszug aus ``tutorial_phase_4.cpp`` dazu:

.. code-block:: cpp

    void TutorialPhase4::set_bricklet_color(String color)
    {
        uint8_t red = hex2num(color.substring(1, 3));
        uint8_t green = hex2num(color.substring(3, 5));
        uint8_t blue = hex2num(color.substring(5, 7));

        if (tf_rgb_led_button_set_color(&rgb_led_button, red, green, blue) != TF_E_OK) {
            logger.printfln("Tutorial (Phase 4) module could not set RGB LED Button Bricklet color");
        }
    }

Test der Kommunikation
^^^^^^^^^^^^^^^^^^^^^^

Als Test kann der Farbwert im Webinterface von ``#FF0000`` (Rot) zu
``#00FF00`` (Grün) geändert werden.

Vor der Änderung zu Grün:

.. image:: /Images/Tutorial/tutorial_esp32_phase_4_hardware_red_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet, Farbe Rot
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_4_hardware_red_1200.jpg

Nach der Änderung zu Grün:

.. image:: /Images/Tutorial/tutorial_esp32_phase_4_hardware_green_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet, Farbe Grün
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_4_hardware_green_1200.jpg


Phase 5: Kommunikation Bricklet zu Backend/Frontend
---------------------------------------------------

Modulname für die ``esp32.ini`` bzw. ``esp32_ethernet.ini`` Datei: ``Tutorial Phase 5``

Mit diesem Modul aktiviert taucht im Webinterface eine Unterseite mit Farb- und
Tasteranzeige namens "Tutorial (Phase 5)" auf:

.. image:: /Images/Tutorial/tutorial_esp32_phase_5_frontend_released_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 5)
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_5_frontend_released_de_1200.png

Neben der Farbe wird auch der Zustand des Tasters angezeigt.

Zustand des Tasters übertragen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die ``api.ts`` Datei des Frontend-Moduls wird erweitert, um den Zustand des
Tasters vom Backend-Modul abfragen zu können. Die neue ``button`` Variable kann
nicht dem existierenden ``config`` Zustand hinzugefügt werden, da der ``config``
Zustand vom Frontend-Modul geändert werden kann, die ``button`` Variable im
Frontend-Modul aber nur lesend zugegriffen werden können soll:

.. code-block:: ts
   :emphasize-lines: 6,7,8,9

    export interface config
    {
        color: string
    }

    export interface state
    {
        button: boolean
    }

Entsprechend muss auch ein neues ``ConfigRoot`` Objekt angelegt werden. Auszug
aus ``tutorial_phase_5.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 9,10,11

    void TutorialPhase5::pre_setup()
    {
        tutorial_config = Config::Object({
            {"color", Config::Str("#FF0000", 7, 7)}
        });

        tutorial_config_update = tutorial_config;

        tutorial_state = Config::Object({
            {"button", Config::Bool(false)}
        });
    }

Dieses neue ``ConfigRoot`` Objekt muss dann auch dem API Manager als weiterer
Zustand bekannt gemacht werden. Dafür wird der Name ``tutorial_phase_5/state``
verwendet, entsprechend der Änderung der ``api.ts`` im Frontend-Modul. Auszug
aus ``tutorial_phase_5.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 13

    void TutorialPhase5::register_urls()
    {
        api.addState("tutorial_phase_5/config", &tutorial_config, {}, 1000);

        api.addCommand("tutorial_phase_5/config_update", &tutorial_config_update, {}, [this]() {
            String color = tutorial_config_update.get("color")->asString();

            logger.printfln("Tutorial (Phase 5) module received color update: %s", color.c_str());
            tutorial_config.get("color")->updateString(color);
            set_bricklet_color(color);
        }, false);

        api.addState("tutorial_phase_5/state", &tutorial_state, {}, 100);
    }

Um auf einen Tasterdruck reagieren zu können wird die Funktion
``button_state_changed_handler`` als Handler für den Button-State-Changed-Callback
des RGB LED Button Bricklets registriert. Dadurch wird diese Funktion beim Drücken
und Loslassen des Tasters automatisch aufgerufen und die Zustandsänderung kann
entsprechend behandelt werden. Auszug aus ``tutorial_phase_5.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 1,2,3,4,5,16,17,19,20,21,22,23

    static void button_state_changed_handler(TF_RGBLEDButton *rgb_led_button, uint8_t state, void *user_data)
    {
        TutorialPhase5 *tutorial = (TutorialPhase5 *)user_data;
        tutorial->tutorial_state.get("button")->updateBool(state == TF_RGB_LED_BUTTON_BUTTON_STATE_PRESSED);
    }

    void TutorialPhase5::setup()
    {
        if (tf_rgb_led_button_create(&rgb_led_button, nullptr, &hal) != TF_E_OK) {
            logger.printfln("No RGB LED Button Bricklet found, disabling Tutorial (Phase 5) module");
            return;
        }

        set_bricklet_color(tutorial_config.get("color")->asString());

        tf_rgb_led_button_register_button_state_changed_callback(&rgb_led_button, button_state_changed_handler, this);
        uint8_t state;

        if (tf_rgb_led_button_get_button_state(&rgb_led_button, &state) != TF_E_OK) {
            logger.printfln("Could not get RGB LED Button Bricklet button state");
        } else {
            tutorial_state.get("button")->updateBool(state == TF_RGB_LED_BUTTON_BUTTON_STATE_PRESSED);
        }

        logger.printfln("Tutorial (Phase 5) module initialized");

        initialized = true;
    }

In der ``main.ts`` Datei des Frontend-Moduls muss dann auf die Änderung des
neuen Zustands ``tutorial_phase_5/state`` für den Tasterzustand genau so
reagiert werden, wie auf die Änderung des bisherigen ``tutorial_phase_5/config``
Zustand für die Farbe:

.. code-block:: ts
   :emphasize-lines: 1,2,3,4,5,10

    function update_state()
    {
        let state = API.get("tutorial_phase_5/state");
        $("#tutorial_phase_5_button").val(state.button ? __("tutorial_phase_5.script.button_pressed") : __("tutorial_phase_5.script.button_released"));
    }

    export function add_event_listeners(source: API.APIEventTarget)
    {
        source.addEventListener("tutorial_phase_5/config", update_config);
        source.addEventListener("tutorial_phase_5/state", update_state);
    }

Ein Druck auf den Taster wird im Webinterface angezeigt:

.. image:: /Images/Tutorial/tutorial_esp32_phase_5_frontend_pressed_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 5), Taster gedrückt
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_5_frontend_pressed_de_1200.png


Auf externe Farbänderungen reagieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Standard-Firmware macht die angeschlossenen Bricklets durch das
``Proxy``-Modul extern über die :ref:`API Bindings <api_bindings>` und damit
auch :ref:`Brick Viewer <brickv>` zugänglich. Farbänderungen des RGB LED Button
Bricklets über diesen Weg werden vom Tutorial-Modul bisher nicht wahrgenommen
und daher nicht auf dem Webinterface angezeigt.

Damit externe Farbänderungen vom Tutorial-Modul auch wahrgenommen werden können
wird die Farbe alle 1000 Millisekunden vom RGB LED Button Bricklet abgefragt und
bei Änderung automatisch über den API Manager an das Webinterface übertragen.
Auszug aus ``tutorial_phase_5.cpp`` dazu:

.. code-block:: cpp
   :emphasize-lines: 13,14,15,22,23,24,26,27,28,29,31,32,33

    void TutorialPhase5::setup()
    {
        // ...

        uint8_t state;

        if (tf_rgb_led_button_get_button_state(&rgb_led_button, &state) != TF_E_OK) {
            logger.printfln("Could not get RGB LED Button Bricklet button state");
        } else {
            tutorial_state.get("button")->updateBool(state == TF_RGB_LED_BUTTON_BUTTON_STATE_PRESSED);
        }

        task_scheduler.scheduleWithFixedDelay([this]() {
            poll_bricklet_color();
        }, 0, 1000);

        logger.printfln("Tutorial (Phase 5) module initialized");

        initialized = true;
    }

    void TutorialPhase5::poll_bricklet_color()
    {
        uint8_t red, green, blue;

        if (tf_rgb_led_button_get_color(&rgb_led_button, &red, &green, &blue) != TF_E_OK) {
            logger.printfln("Could not get RGB LED Button Bricklet color");
            return;
        }

        String color = "#" + num2hex(red) + num2hex(green) + num2hex(blue);
        tutorial_config.get("color")->updateString(color);
    }

Änderung der Farbe von Rot auf Gelb in Brick Viewer:

.. image:: /Images/Tutorial/tutorial_esp32_phase_5_brickv_600.png
   :scale: 100 %
   :alt: Brick Viewer (Phase 5), Gelb
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_5_brickv_1200.png

Jetzt wird im Webinterface Gelb angezeigt:

.. image:: /Images/Tutorial/tutorial_esp32_phase_5_frontend_yellow_de_600.png
   :scale: 100 %
   :alt: Webinterface (Phase 5), Gelb
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_5_frontend_yellow_de_1200.png

Damit ist der gesamte Kommunikationsweg von Hardware durch Firmware zum Webinterface
und zurück durchlaufen und dieses Tutorial abgeschlossen.
