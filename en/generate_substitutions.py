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
 To test the {0} Brick you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
"""

    test_tab = """.. |test_tab| replace::
 Now connect the Brick to the PC over USB, you should see a new tab named
 "{0} Brick" in the Brick Viewer after a moment. Select this tab.
"""

    test_pi_ref = """.. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_brick_programming_interfaces>` section for
 the API of the {1} Brick and examples in different programming languages.
"""

    substitutions = ''
    substitutions += test_intro.format(brick[0]) + '\n'
    substitutions += test_tab.format(brick[0]) + '\n'
    substitutions += test_pi_ref.format(brick[1], brick[0])

    return substitutions

def make_bricklet_substitutions(bricklet):
    test_intro = """.. |test_intro| replace::
 To test the {0} Bricklet you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
"""

    test_connect = """.. |test_connect| replace::
 Connect the {0} Bricklet to a :ref:`Brick <product_overview_bricks>`
 with the supplied cable
"""

    test_tab = """.. |test_tab| replace::
 If you connect the Brick to the PC over USB, you should see a new tab named
 "{0} Bricklet" in the Brick Viewer after a moment. Select this tab.
"""

    test_pi_ref = """.. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_bricklet_programming_interfaces>` section for
 the API of the {1} Bricklet and examples in different programming languages.
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
