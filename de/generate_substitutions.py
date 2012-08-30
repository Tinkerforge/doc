#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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

def make_brick_substitutions(brick):
    test_intro = """.. |test_intro| replace::
 Um den {0} Brick testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.
"""

    test_tab = """.. |test_tab| replace::
 Schließe jetzt den Brick per USB an den PC an. Einen Moment später im Brick
 Viewer ein neuer Tab namens "{0} Brick" auftauchen. Wähle diesen Tab aus.
"""

    test_pi_ref = """.. |test_pi_ref| replace::
 Nun kannst du dein eigenes Programm schreiben. Der Abschnitt
 :ref:`Programmierschnittstellen <{0}_brick_programming_interfaces>` listet die
 API des {1} Bricks und Beispiele in verschiedenen Programmiersprachen auf.
"""

    substitutions = ''
    substitutions += test_intro.format(brick[0]) + '\n'
    substitutions += test_tab.format(brick[0]) + '\n'
    substitutions += test_pi_ref.format(brick[1], brick[0])

    return substitutions

def make_bricklet_substitutions(bricklet):
    test_intro = """.. |test_intro| replace::
 Um das {0} Bricklet testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.
"""

    test_connect = """.. |test_connect| replace::
 Als nächstes muss das {0} Bricklet über das mitgelieferte Kabel mit
 einem :ref:`Brick <product_overview_bricks>` verbunden werden
"""

    test_tab = """.. |test_tab| replace::
 Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Bricklet" auftauchen.
 Wähle diesen Tab aus.
"""

    test_pi_ref = """.. |test_pi_ref| replace::
 Nun kannst du dein eigenes Programm schreiben. Der Abschnitt
 :ref:`Programmierschnittstellen <{0}_bricklet_programming_interfaces>` listet die
 API des {1} Bricklets und Beispiele in verschiedenen
 Programmiersprachen auf.
"""

    substitutions = ''

    substitutions += test_intro.format(bricklet[0]) + '\n'
    substitutions += test_connect.format(bricklet[0]) + '\n'
    substitutions += test_tab.format(bricklet[0]) + '\n'
    substitutions += test_pi_ref.format(bricklet[1], bricklet[0])

    return substitutions

def generate(path):
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
