#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

          # display,   uri
bricks = [('DC',      'dc'),
          ('Debug',   'debug'),
          ('IMU',     'imu'),
          ('Master',  'master'),
          ('Servo',   'servo'),
          ('Stepper', 'stepper')]

             # display,                    uri
bricklets = [('Ambient Light',             'ambient_light'),
             ('Analog In',                 'analog_in'),
             ('Analog Out',                'analog_out'),
             ('Barometer',                 'barometer'),
             ('Breakout',                  'breakout'),
             ('Current12',                 'current12'),
             ('Current25',                 'current25'),
             ('Distance IR',               'distance_ir'),
             ('Dual Relay',                'dual_relay'),
             ('GPS',                       'gps'),
             ('Humidity',                  'humidity'),
             ('Industrial Digital In 4',   'industrial_digital_in_4'),
             ('Industrial Digital Out 4',  'industrial_digital_out_4'),
             ('Industrial Quad Relay',     'industrial_quad_relay'),
             ('IO-16',                     'io16'),
             ('IO-4',                      'io4'),
             ('Joystick',                  'joystick'),
             ('LCD 16x2',                  'lcd_16x2'),
             ('LCD 20x4',                  'lcd_20x4'),
             ('Linear Poti',               'linear_poti'),
             ('Piezo Buzzer',              'piezo_buzzer'),
             ('Rotary Poti',               'rotary_poti'),
             ('Temperature',               'temperature'),
             ('Temperature IR',            'temperature_ir'),
             ('Voltage',                   'voltage'),
             ('Voltage/Current',           'voltage_current'),
            ]

brick_test_intro = {
'en':
""".. |test_intro| replace::
 To test the {0} Brick you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
""",
'de':
""".. |test_intro| replace::
 Um den {0} Brick testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.

"""
}

brick_test_tab = {
'en':
""".. |test_tab| replace::
 Now connect the Brick to the PC over USB, you should see a new tab named
 "{0} Brick" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Brick" auftauchen. Wähle diesen Tab
 aus.
"""
}

brick_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_brick_programming_interfaces>`
 section for the API of the {1} Brick and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstellen <{0}_brick_programming_interfaces>` listet die
 API des {1} Bricks und Beispiele in verschiedenen Programmiersprachen auf.
"""
}

bricklet_test_intro = {
'en':
""".. |test_intro| replace::
 To test the {0} Bricklet you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
""",
'de':
""".. |test_intro| replace::
 Um das {0} Bricklet testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.
"""
}

bricklet_test_connect = {
'en':
""".. |test_connect| replace::
 Connect the {0} Bricklet to a :ref:`Brick <product_overview_bricks>`
 with the supplied cable
""",
'de':
""".. |test_connect| replace::
 Als nächstes muss das {0} Bricklet über das mitgelieferte Kabel mit
 einem :ref:`Brick <product_overview_bricks>` verbunden werden
"""
}

bricklet_test_tab = {
'en':
""".. |test_tab| replace::
 If you connect the Brick to the PC over USB, you should see a new tab named
 "{0} Bricklet" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Bricklet" auftauchen.
 Wähle diesen Tab aus.
"""
}

bricklet_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_bricklet_programming_interfaces>`
 section for the API of the {1} Bricklet and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstellen <{0}_bricklet_programming_interfaces>` listet
 die API des {1} Bricklets und Beispiele in verschiedenen
 Programmiersprachen auf.
"""
}

def make_brick_substitutions(brick):
    substitutions = ''
    substitutions += brick_test_intro[lang].format(brick[0]) + '\n'
    substitutions += brick_test_tab[lang].format(brick[0]) + '\n'
    substitutions += brick_test_pi_ref[lang].format(brick[1], brick[0])

    return substitutions

def make_bricklet_substitutions(bricklet):
    substitutions = ''
    substitutions += bricklet_test_intro[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_connect[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_tab[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_pi_ref[lang].format(bricklet[1], bricklet[0])

    return substitutions

                            # display,            example,              uri,      filename, getting started
weather_station_bindings = [('C/C++',             'C',                  'c',      'C',      {'en': 'http://www.cprogramming.com/',
                                                                                             'de': 'http://www.cprogramming.com/'}),
                            ('C#',                'C#',                 'csharp', 'CSharp', {'en': 'http://csharp.net-tutorials.com/',
                                                                                             'de': 'http://csharp.net-tutorials.com/'}),
                            ('Delphi',            'Delphi',             'delphi', 'Delphi', {'en': 'http://www.delphibasics.co.uk/',
                                                                                             'de': 'http://www.delphi-treff.de/tutorials/grundlagen/'}),
                            ('Java',              'Java',               'java',   'Java',   {'en': 'http://docs.oracle.com/javase/tutorial/',
                                                                                             'de': 'http://docs.oracle.com/javase/tutorial/'}), # http://openbook.galileocomputing.de/javainsel/
                            ('PHP',               'PHP',                'php',    'PHP',    {'en': 'http://www.php.net/manual/en/getting-started.php',
                                                                                             'de': 'http://www.php.net/manual/de/getting-started.php'}),
                            ('Python',            'Python',             'python', 'Python', {'en': 'http://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
                                                                                             'de': 'http://www.python.org/about/gettingstarted/'}),
                            ('Ruby',              'Ruby',               'ruby',   'Ruby',   {'en': 'http://www.ruby-lang.org/en/documentation/quickstart/',
                                                                                             'de': 'http://www.ruby-lang.org/de/documentation/quickstart/'}),
                            ('Visual Basic .NET', 'Visual Basic .NET',  'vbnet',  'VBNET',  {'en': 'http://howtostartprogramming.com/vb-net/',
                                                                                             'de': 'http://howtostartprogramming.com/vb-net/'})] # http://openbook.galileocomputing.de/vb_net/index.htm

weather_station_binding_name = {
'en':
""":ref:`{0} <api_bindings_{1}>`""",
'de':
""":ref:`{0} <api_bindings_{1}>`"""
}

weather_station_binding_names = {
'en':
"""
.. |bindings| replace:: {0}
""",
'de':
"""
.. |bindings| replace:: {0}
"""
}

weather_station_common_intro = {
'en':
"""
>>>intro
For this project we are assuming, that you have a {0} development environment
set up and that you have a rudimentary understanding of the {0} language.

If you are totally new to {0} itself you should start `here <{2}>`__. If you are
new to the Tinkerforge API, you should start :ref:`here <api_bindings_{1}>`.
<<<intro
""",
'de':
"""
>>>intro
Für diese Projekt setzen wir voraus, dass eine {0} Entwicklungsumgebung
eingerichtet ist und ein grundsätzliches Verständnis der {0} Programmiersprache
vorhanden ist.

Falls dem nicht der Fall ist sollte `hier <{2}>`__ begonnen werden. Informationen
über die Tinkerforge API sind dann :ref:`hier <api_bindings_{1}>` zu finden.
<<<intro
"""
}

weather_station_write_to_lcd_examples = {
'en':
"""
.. |write_to_lcd_examples| replace:: {0}
""",
'de':
"""
.. |write_to_lcd_examples| replace:: {0}
"""
}

weather_station_write_to_lcd_example_line = {
'en':
""":ref:`{0} <starter_kit_weather_station_{1}_to_lcd>`""",
'de':
""":ref:`{0} <starter_kit_weather_station_{1}_to_lcd>`"""
}

weather_station_write_to_lcd_goals = {
'en':
"""
>>>goals
We are setting the following goals for this project:

* Temperature, ambient light, humidity and air pressure should be shown on
  the LCD 20x4 Bricklet,
* the measured values should be updated automatically when they change and
* the measured values should be formated to be easily readable.

Since this project will likely run 24/7, we will also make sure
that the application is as robust towards external influences as possible.
The application should still work when

* Bricklets are exchanged (i.e. we don't rely on UIDs),
* Brick Daemon isn't running or is restarted,
* WIFI Extension is out of range or
* Weather Station is restarted (power loss or accidental USB removal).

In the following we will show step-by-step how this can be achieved.
<<<goals
""",
'de':
"""
>>>goals
Wir setzen uns folgende Ziele für dieses Projekt:

* Temperatur, Helligkeit, Luftfeuchte und Luftdruck sollen auf dem LCD 20x4
  Bricklet angezeigt werden,
* die gemessenen Werte sollen automatisch aktualisiert werden sobald sie sich
  verändern und
* die gemessenen Werte sollen in einem verständlichen Format angezeigt werden.

Da dieses Projekt wahrscheinlich 24/7 laufen wird, wollen wir sicherstellen,
dass das Programm möglichst robust gegen externe Einflüsse ist. Das Programm
sollte weiterhin funktionieren falls

* Bricklets ausgetauscht werden (z.B. verwenden wir keine fixen UIDs),
* Brick Daemon läuft nicht oder wird neu gestartet,
* WIFI Extension ist außer Reichweite oder
* Wetterstation wurde neu gestartet (Stromausfall oder USB getrennt).

Im Folgenden werden wir Schritt für Schritt zeigen wie diese Ziele erreicht
werden können.
<<<goals
"""
}

weather_station_write_to_lcd_steps = {
'en':
"""
.. |step1_start_off| replace::
 To start off, we need to define where our program should connect to:

.. |step1_ip_address| replace::
 If the WIFI Extension is used or if the Brick Daemon is
 running on a different PC, you have to exchange "localhost" with the
 IP address or hostname of the WIFI Extension or PC.

.. |step1_register_callbacks| replace::
 When the program is started, we need to register the |ref_CALLBACK_ENUMERATE|
 |callback| and the |ref_CALLBACK_CONNECTED| |callback| and trigger a first
 enumerate:

.. |step1_enumerate_callback| replace::
 The enumerate callback is triggered if a Brick gets connected over USB or if
 the |ref_enumerate| function is called. This allows to discover the Bricks and
 Bricklets in a stack without knowing their types or UIDs beforehand.

.. |step1_connected_callback| replace::
 The connected callback is triggered if the connection to the WIFI Extension or
 to the Brick Daemon got established. In this callback we need to trigger the
 enumerate again, if the reason is an auto reconnect:

.. |step1_auto_reconnect_callback| replace::
 An auto reconnect means, that the connection to the WIFI Extension or to the
 Brick Daemon was lost and could subsequently be established again. In this
 case the Bricklets may have lost their configurations and we have to
 reconfigure them. Since the configuration is done during the
 enumeration process (see below), we have to trigger another enumeration.

.. |step1_put_together| replace::
 Step 1 put together:

.. |step2_intro| replace::
 During the enumeration we want to configure all of the weather measuring
 Bricklets. Doing this during the enumeration ensures that Bricklets get
 reconfigured if the stack was disconnected or there was a power loss.

.. |step2_enumerate| replace::
 The configurations should be performed on first startup
 (|ENUMERATION_TYPE_CONNECTED|) as well as whenever the enumeration is
 triggered externally by us (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_lcd_config| replace::
 The LCD 20x4 configuration is simple, we want the current text cleared and
 we want the backlight on:

.. |step2_other_config1| replace::
 We configure the Ambient Light, Humidity and Barometer Bricklet to
 return their respective measurements continuously with a period of
 1000ms (1s):

.. |step2_other_config2| replace::
 This means that the Bricklets will call the |cb_illuminance|, |cb_humidity|
 and |cb_air_pressure| callback functions whenever the value has changed, but
 with a maximum period of 1000ms.

.. |step2_put_together| replace::
 Step 2 put together:

.. |step3_intro| replace::
 We want a neat arrangement of the measurements on the display, such as

.. |step3_format| replace::
 The decimal marks and the units should be below each other. To achieve this
 we use two characters for the unit, two decimal places and crop the name
 to use the maximum characters that are left. That's why "Illuminanc" is missing
 its final "e".

.. |step3_printf| replace::
 The code above converts a floating point value to a string according to the given
 `format specification <http://en.wikipedia.org/wiki/Printf_format_string>`__.
 The result will be at least 6 characters long with 2 decimal places, filled up
 with spaces from the left if it would be shorter than 6 characters otherwise.

.. |step3_temperature| replace::
 We are still missing the temperature. The Barometer Bricklet can
 measure temperature, but it doesn't have a callback for it. As a
 simple workaround we can retrieve the temperature in the |cb_air_pressure|
 callback function:

.. |step3_put_together| replace::
 Step 3 put together:

.. |step3_complete| replace::
 That's it. If we would copy these three steps together in one file and
 execute it, we would have a working Weather Station!

.. |step3_suggestions1| replace::
 There are some obvious ways to make the output better.
 The name could be cropped according to the exact space that is available
 (depending on the number of digits of the measured value). Also, reading the
 temperature in the |cb_air_pressure| callback function is suboptimal. If the
 air pressure doesn't change, we won't update the temperature.

.. |step3_suggestions2_common| replace::
 It would be better to read the temperature in a different thread in an endless
 loop with a one second sleep after each read. But we want to keep this code as
 simple as possible.

.. |step3_suggestions2_no_thread| replace::
 It would be better to read the temperature every second triggered by an
 additional timer. But we want to keep this code as simple as possible.

.. |step3_robust1| replace::
 However, we do not meet all of our goals yet. The program is not yet
 robust enough. What happens if can't connect on startup? What happens if
 the enumerate after an auto reconnect doesn't work?

.. |step3_robust2| replace::
 What we need is error handling!

.. |step4_intro1| replace::
 On startup, we need to try to connect until the connection works:

.. |step4_intro2| replace::
 and we need to try enumerating until the message goes through:

.. |step4_sleep_in_c| replace::
 There is no portable sleep function in C. On Windows ``windows.h`` declares
 a ``Sleep`` function that takes the duration in milliseconds. On POSIX
 systems such as Linux and Mac OS X there is a ``sleep`` function declared
 in ``unistd.h`` that takes the duration in seconds.

.. |step4_connect_afterwards| replace::
 With these changes it is now possible to first start the program and
 connect the Weather Station afterwards.

.. |step4_lcd_initialized1| replace::
 We also need to make sure, that we only write to the LCD if it is
 already initialized:

.. |step4_lcd_initialized2| replace::
 and that we have to deal with errors during the initialization:

.. |step4_logging1| replace::
 Additionally we added some logging. With the logging we can later find out
 what exactly caused a problem, if the Weather Station failed for some
 time period.

.. |step4_logging2| replace::
 For example, if we connect to the Weather Station via Wi-Fi and we have
 regular auto reconnects, it likely means that the Wi-Fi connection is not
 very stable.

.. |step5_intro| replace::
 That's it! We are already done with our Weather Station and all of the
 goals should be met.

.. |step5_put_together| replace::
 Now all of the above put together
""",
'de':
"""
.. |step1_start_off| replace::
 Als Erstes legen wir fest wohin unser Programm sich verbinden soll:

.. |step1_ip_address| replace::
 Falls eine WIFI Extension verwendet wird, oder der Brick Daemon auf einem
 anderen PC läuft, dann muss "localhost" durch die IP Adresse oder den Hostnamen
 der WIFI Extension oder des anderen PCs ersetzt werden.

.. |step1_register_callbacks| replace::
 Nach dem Start des Programms müssen der |ref_CALLBACK_ENUMERATE| |callback|
 und der |ref_CALLBACK_CONNECTED| |callback| registriert und ein erstes
 Enumerate ausgelöst werden:

.. |step1_enumerate_callback| replace::
 Der Enumerate Callback wird ausgelöst wenn ein Brick per USB angeschlossen wird
 oder wenn die |ref_enumerate| Funktion aufgerufen wird. Dies ermöglicht es die
 Bricks und Bricklets im Stapel zu erkennen ohne im Voraus ihre UIDs kennen zu
 müssen.

.. |step1_connected_callback| replace::
 Der Connected Callback wird ausgelöst wenn die Verbindung zur WIFI Extension
 oder zum Brick Daemon hergestellt wurde. In diesem Callback muss wiederum ein
 Enumerate angestoßen werden, wenn es sich um ein Auto-Reconnect handelt:

.. |step1_auto_reconnect_callback| replace::
 Ein Auto-Reconnect bedeutet, dass die Verbindung zur WIFI Extension oder zum
 Brick Daemon verloren gegangen ist und automatisch wiederhergestellt werden
 konnte. In diesem Fall kann es sein, dass die Bricklets ihre Konfiguration
 verloren haben und wir sie neu konfigurieren müssen. Da die Konfiguration
 beim Enumerate (siehe unten) durchgeführt wird, lösen wir einfach noch ein
 Enumerate aus.

.. |step1_put_together| replace::
 Schritt 1 zusammengefügt:

.. |step2_intro| replace::
 Während des Enumerierungsprozesse sollen alle messenden Bricklets konfiguriert
 werden. Dadurch ist sichergestellt, dass sie neu konfiguriert werden nach
 einem Verbindungsabbrüche oder einer Unterbrechung der Stromversorgung.

.. |step2_enumerate| replace::
 Die Konfiguration soll beim ersten Start (|ENUMERATION_TYPE_CONNECTED|)
 durchgeführt werden und auch bei jedem extern ausgelösen Enumerate
 (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_lcd_config| replace::
 Die Konfiguration des LCD 20x4 ist einfach, wir löschen den aktuellen Inhalt
 des Displays und schalten das Backlight ein:

.. |step2_other_config1| replace::
 Das Ambient Light, Humidity und Barometer Bricklet werden so eingestellt, dass
 sie uns ihre jeweiligen Messwerte höchsten mit einer Periode von 1000ms (1s)
 mitteilen:

.. |step2_other_config2| replace::
 Dies bedeuted, dass die Bricklets die |cb_illuminance|, |cb_humidity|
 und |cb_air_pressure| Callback-Funktionen immer dann aufrufen wenn sich der
 Messwert verändert hat, aber höchsten alle 1000ms.

.. |step2_put_together| replace::
 Schritt 2 zusammengefügt:

.. |step3_intro| replace::
 Wir wollen eine hübsche Darstellung der Messwerte auf dem Display. Zum Beispiel

.. |step3_format| replace::
 Die Dezimaltrennzeichen und die Einheiten sollen in jeweils einer Spalte
 übereinander stehen. Daher verwenden wird zwei Zeichen für jede Einheit, zwei
 Nachkommastellen und kürzen die Namen so, dass sie in den restlichen Platz der
 jeweiligen Zeile passen. Das ist auch der Grund, warum dem "Illuminanc" das
 letzte "e" fehlt.

.. |step3_printf| replace::
 Der obige Ausdruck wandelt eine Fließkommazahl in eine Zeichenkette um,
 gemäß der gegebenen `Formatspezifikation
 <http://en.wikipedia.org/wiki/Printf_format_string>`__. Das Ergebnis ist dann
 mindestens 6 Zeichen lang mit 2 Nachkommastellen. Fall es weniger als 6 Zeichen
 sind wird von Links mit Leerzeichen aufgefüllt.

.. |step3_temperature| replace::
 Es fehlt noch die Temperatur. Das Barometer Bricklet kann auch die Temperatur
 messen, aber es hat dafür keinen Callback. Als einfacher Workaround können wir
 die Temperatur in der |cb_air_pressure| Callback-Funktion abfragen:

.. |step3_put_together| replace::
 Schritt 3 zusammengefügt:

.. |step3_complete| replace::
 Das ist es. Wenn wir diese drei Schritte zusammen in eine Datei kopieren und
 ausführen, dann hätten wir jetzt eine funktionierenden Wetterstation.

.. |step3_suggestions1| replace::
 Es gibt einige offensichtliche Möglichkeiten die Ausgabe der Messdaten noch zu
 verbessern. Die Namen könnten dynamisch exakt gekürzt werden, abhängig vom
 aktuell freien Raum der jeweiligen Zeile. Auch könnten die Namen können noch
 ins  Deutsche übersetzt werden. Ein anderes Problem ist die Abfrage der
 Temperatur in der |cb_air_pressure| Callback-Funktion. Wenn sich der Luftdruck
 nicht ändert dann wird auch die Anzeige der Temperatur nicht aktualisiert, auch
 wenn sich diese eigentlich geändert hat.

.. |step3_suggestions2_common| replace::
 Es wäre besser die Temperatur jede Sekunde in einem eigenen Thread anzufragen.
 Aber wir wollen das Programm für den Anfang einfach halten.

.. |step3_suggestions2_no_thread| replace::
 Es wäre besser die Temperatur jede Sekunde über einen eigenen Timmer anzufragen.
 Aber wir wollen das Programm für den Anfang einfach halten.

.. |step3_robust1| replace::
 Wie dem auch sei, wir haben noch nicht alle Ziele erreicht. Das Programm ist
 noch nicht robust genug. Was passiert wenn die Verbindung beim Start des
 Programms nicht hergestellt werden kann, oder wenn das Enumerate nach einem
 Auto-Reconnect nicht funktioniert?

.. |step3_robust2| replace::
 Wir brauchen noch Fehlerbehandlung!

.. |step4_intro1| replace::
 Beim Start des Programms versuchen wir solange die Verbindung herzustellen,
 bis es klappt:

.. |step4_intro2| replace::
 und es wird solange versucht ein Enumerate zu starten bis auch dis geklappt
 hat:

.. |step4_sleep_in_c| replace::
 Es gibt keine portable Sleep Funktion in C. Auf Windows deklariert `windows.h``
 eine ``Sleep`` Funktion die die Wartedauer in Millisekunden übergeben bekommt.
 Auf POSIX Systemen wie Linux und Mac OS X gibt es eine ``sleep`` Funktion
 deklariert in ``unistd.h`` die die Wartedauer in Sekunden übergeben bekommt.

.. |step4_connect_afterwards| replace::
 Mit diesen Änderungen kann das Programm schon gestartet werden bevor die
 Wetterstation angeschlossen ist.

.. |step4_lcd_initialized1| replace::
 Es muss auch sichergestellt werden, dass wir nur auf das LCD schreiben nachdem
 es initialisiert wurde:

.. |step4_lcd_initialized2| replace::
 und es müssen mögliche Fehler während des Enumerierungsprozesses behandelt
 werden:

.. |step4_logging1| replace::
 Zusätzlich wollen wir noch ein paar Logausgaben einfügen. Diese ermöglichen es
 später herauszufinden was ein Problem ausgelöst hat, wenn die Wetterstation
 nach einer Weile möglicherweise nicht mehr funktioniert wie erwartet.

.. |step4_logging2| replace::
 Zum Beispiel, wenn die Wetterstation über WLAN angebunden ist und häufig
 Auto-Reconnects auftreten, dann ist wahrscheinlich die WLAN Verbindung nicht
 sehr stabil.

.. |step5_intro| replace::
 Jetzt sind alle für diese Projekt gesteckten Ziele erreicht.

.. |step5_put_together| replace::
 Das gesamte Programm für die Wetterstation
"""
}

def make_weather_station_substitutions():
    substitutions = ''

    binding_names = []
    for binding in weather_station_bindings:
        binding_names.append(weather_station_binding_name[lang].format(binding[0], binding[2]))

    substitutions += weather_station_binding_names[lang].format(', '.join(binding_names)) + '\n'

    example_lines = []
    for binding in weather_station_bindings:
        example_lines.append(weather_station_write_to_lcd_example_line[lang].format(binding[1], binding[2]))

    substitutions += weather_station_write_to_lcd_examples[lang].format(', '.join(example_lines))

    return substitutions

def make_weather_station_common_substitutions(binding):
    substitutions = ''
    substitutions += weather_station_common_intro[lang].format(binding[1], binding[2], binding[4][lang])

    return substitutions

def make_weather_station_write_to_lcd_substitutions(binding):
    substitutions = ''
    substitutions += weather_station_write_to_lcd_goals[lang] + '\n'
    substitutions += '>>>substitutions\n'
    substitutions += weather_station_write_to_lcd_steps[lang] + '\n'
    substitutions += '<<<substitutions\n'

    return substitutions

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        print 'Wrong working directory'
        sys.exit(1)

    for brick in bricks:
        name = brick[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print 'Generating {0}_Brick.substitutions (Hardware)'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick.substitutions'), 'wb').write(make_brick_substitutions(brick))

    for bricklet in bricklets:
        name = bricklet[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print 'Generating {0}.substitutions (Hardware)'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '.substitutions'), 'wb').write(make_bricklet_substitutions(bricklet))

    print 'Generating WeatherStation.substitutions'
    file(os.path.join(path, 'source', 'Kits', 'WeatherStation', 'WeatherStation.substitutions'), 'wb').write(make_weather_station_substitutions())

    for binding in weather_station_bindings:
        print 'Generating {0}Common.substitutions (WeatherStation)'.format(binding[3])
        file(os.path.join(path, 'source', 'Kits', 'WeatherStation', binding[3] + 'Common.substitutions'), 'wb').write(make_weather_station_common_substitutions(binding))

    for binding in weather_station_bindings:
        print 'Generating {0}ToLCD.substitutions (WeatherStation)'.format(binding[3])
        file(os.path.join(path, 'source', 'Kits', 'WeatherStation', binding[3] + 'ToLCD.substitutions'), 'wb').write(make_weather_station_write_to_lcd_substitutions(binding))

if __name__ == "__main__":
    generate(os.getcwd())
