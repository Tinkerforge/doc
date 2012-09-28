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

             # display,          uri
bricklets = [('Ambient Light',  'ambient_light'),
             ('Analog In',      'analog_in'),
             ('Analog Out',     'analog_out'),
             #('Barometer',      'barometer'),
             ('Breakout',       'breakout'),
             ('Current12',      'current12'),
             ('Current25',      'current25'),
             ('Distance IR',    'distance_ir'),
             ('Dual Relay',     'dual_relay'),
             ('Humidity',       'humidity'),
             ('IO-16',          'io16'),
             ('IO-4',           'io4'),
             ('Joystick',       'joystick'),
             ('LCD 16x2',       'lcd_16x2'),
             ('LCD 20x4',       'lcd_20x4'),
             ('Linear Poti',    'linear_poti'),
             ('Piezo Buzzer',   'piezo_buzzer'),
             ('Rotary Poti',    'rotary_poti'),
             ('Temperature',    'temperature'),
             ('Temperature IR', 'temperature_ir'),
             ('Voltage',        'voltage')]

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
 sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
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
 Schließe jetzt den Brick per USB an den PC an. Einen Moment später im Brick
 Viewer ein neuer Tab namens "{0} Brick" auftauchen. Wähle diesen Tab aus.
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
 Nun kann ein eigenes Programm geschreiben werden. Der Abschnitt
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
 sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
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
 Nun kann ein eigenes Programm geschreiben werden. Der Abschnitt
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
        name = brick[0].replace(' ', '_').replace('-', '')

        print 'Generating {0}_Brick.substitutions'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick.substitutions'), 'wb').write(make_brick_substitutions(brick))

    for bricklet in bricklets:
        name = bricklet[0].replace(' ', '_').replace('-', '')

        print 'Generating {0}.substitutions'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '.substitutions'), 'wb').write(make_bricklet_substitutions(bricklet))


if __name__ == "__main__":
    generate(os.getcwd())
