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
For this project we are assuming, that you have a {0} environment set up
and that you have a rudimentary understanding of the {0} language.

If you are totally new to {0} itself you should start `here <{2}>`__. If you are
new to the Tinkerforge API, you should start :ref:`here <api_bindings_{1}>`.
<<<intro
""",
'de':
"""
>>>intro
For this project we are assuming, that you have a {0} environment set up
and that you have a rudimentary understanding of the {0} language.

If you are totally new to {0} itself you should start `here <{2}>`. If you are
new to the Tinkerforge API, you should start :ref:`here <api_bindings_{1}>`.
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

* Temperature, ambient light, humidity and air pressure should be shown on the LCD 20x4 Bricklet,
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
We are setting the following goals for this project:

* Temperature, ambient light, humidity and air pressure should be shown on the LCD 20x4 Bricklet,
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
 When the program is started, we need to register the enumerate
 and connected callbacks and trigger a first enumerate:

.. |step1_enumerate_callback| replace::
 The enumerate callback is triggered if a Brick gets connected over USB or if
 the enumerate function is called. This allows to discover the Bricks and
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
 reconfigured if they were disconnected or there was a power loss.

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
 (depending on the number of digits of the measured value). Also,
 reading the temperature in the air pressure callback is suboptimal. If the
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
 what exactly caused a problem, when the Weather Station failed for some
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
 To start off, we need to define where our program should connect to:

.. |step1_ip_address| replace::
 If the WIFI Extension is used or if the Brick Daemon is
 running on a different PC, you have to exchange "localhost" with the
 IP address or hostname of the WIFI Extension or PC.

.. |step1_register_callbacks| replace::
 When the program is started, we need to register the enumerate
 and connected callbacks and trigger a first enumerate:

.. |step1_enumerate_callback| replace::
 The enumerate callback is triggered if a Brick gets connected over USB or if
 the enumerate function is called. This allows to discover the Bricks and
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
 reconfigured if they were disconnected or there was a power loss.

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
 (depending on the number of digits of the measured value). Also,
 reading the temperature in the air pressure callback is suboptimal. If the
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
 what exactly caused a problem, when the Weather Station failed for some
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
