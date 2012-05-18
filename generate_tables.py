#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

            # display,  uri
bindings = [('TCP/IP', 'tcpip',  False),
            ('C/C++',  'c',      True),
            ('C#',     'csharp', True),
            ('Java',   'java',   True),
            ('PHP',    'php',    True),
            ('Python', 'python', True)]

          # display,   uri,      bindings,  description
bricks = [('DC',      'dc',      bindings, '3A DC Motor Driver'),
          ('Debug',   'debug',   [],       'JTAG and serial console debug capabilities'),
          ('IMU',     'imu',     bindings, 'IMU with 9 degrees of freedom'),
          ('Master',  'master',  bindings, 'Allow building of stacks, 4 Bricklet Ports'),
          ('Servo',   'servo',   bindings, 'Control up to 7 Servos'),
          ('Stepper', 'stepper', bindings, '2.5A Stepper Motor Driver')]

             # display,          uri,             bindings,  description
bricklets = [('Ambient Light',  'ambient_light',  bindings, 'Ambient Light Sensor'),
             ('Analog In',      'analog_in',      bindings, 'Measures voltages from 0 to 45V'),
             ('Analog Out',     'analog_out',     bindings, 'Generates voltages from 0 to 5V'),
             ('Breakout',       'breakout',       [],       'Makes all Bricklet signals available'),
             ('Current12',      'current12',      bindings, 'Bidirectional Current Sensor max. 12.5 A'),
             ('Current25',      'current25',      bindings, 'Bidirectional Current Sensor max. 25 A'),
             ('Distance IR',    'distance_ir',    bindings, 'Measure Distances with IR Light'),
             ('Dual Relay',     'dual_relay',     bindings, 'Equipped with two relays'),
             ('Humidity',       'humidity',       bindings, 'Humidity Sensor'),
             ('IO-4',           'io4',            bindings, 'Input/Output 4-Channel'),
             ('IO-16',          'io16',           bindings, 'Input/Output 16-Channel'),
             ('Joystick',       'joystick',       bindings, 'Two directional Joystick with Button'),
             ('LCD 16x2',       'lcd_16x2',       bindings, '16x2 alphanummeric chars display with backlight'),
             ('LCD 20x4',       'lcd_20x4',       bindings, '20x4 alphanummeric chars display with backlight'),
             ('Linear Poti',    'linear_poti',    bindings, 'Linear Potentiometer'),
             ('Piezo Buzzer',   'piezo_buzzer',   bindings, 'Buzzer for signaling'),
             ('Rotary Poti',    'rotary_poti',    bindings, 'Rotary Potentiometer'),
             ('Temperature',    'temperature',    bindings, 'High Precision Thermometer'),
             ('Temperature IR', 'temperature_ir', bindings, 'Infrared Thermometer'),
             ('Voltage',        'voltage',        bindings, 'Sensor to measure voltages')]

def make_index_table(devices, category):
    table_head = """
.. container:: indextable

 .. csv-table::
  :delim: |

"""
    row_head = '  * :ref:`{0} <{1}_' + category + '>` | '
    row_cell = ':ref:`{0} <{1}_' + category + '_{2}>`'
    rows = []

    for device in devices:
        cells = []

        for binding in device[2]:
            cells.append(row_cell.format(binding[0], device[1], binding[1]))

        row = row_head.format(device[0], device[1]) + ', '.join(cells)
        rows.append(row)

    return table_head + '\n'.join(rows)

def make_product_overview_table(devices, category, name_width, description_width):
    table_head = """
.. csv-table::
   :header: "Name", "Description", {0}
   :widths: {1}, {2}, {3}

""".format(', '.join(['"{0}"'.format(binding[0]) for binding in bindings]),
           name_width,
           description_width,
           ', '.join(['5'] * len(bindings)))
    row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}", '
    row_cell = '":ref:`{0} <{1}_' + category + '_{2}>`"'
    rows = []

    for device in devices:
        cells = []

        for binding in device[2]:
            cells.append(row_cell.format(binding[0], device[1], binding[1]))

        row = row_head.format(device[0], device[1], device[3]) + ', '.join(cells)
        rows.append(row)

    return table_head + '\n'.join(rows)

def make_downloads_table():
    table_head = """.. csv-table::
 :header: "", "Bindings and Examples"
 :delim: |
 :widths: 10, 60

 **Language** | """
    row_cell = '`{0} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_latest.zip>`__'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row_cell.format(binding[0], binding[1]))

    return table_head + ', '.join(rows)


def make_hlpi_table(device, category):
    table_head = """
.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

"""
    row_source = '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Examples <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"'
    row = '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"'
    rows = []

    for binding in device[2]:
        if binding[2]:
            rows.append(row_source.format(binding[0], device[1], category, binding[1]))
        else:
            rows.append(row.format(binding[0], device[1], category, binding[1]))

    return table_head + '\n'.join(rows)


def generate(path):
    print 'Generating index_bricks.table'
    file(os.path.join(path, 'source', 'index_bricks.table'), 'wb').write(make_index_table(bricks, 'brick'))

    print 'Generating index_bricklets.table'
    file(os.path.join(path, 'source', 'index_bricklets.table'), 'wb').write(make_index_table(bricklets, 'bricklet'))

    print 'Generating Product_Overview_bricks.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricks.table'), 'wb').write(make_product_overview_table(bricks, 'brick', 15, 40))

    print 'Generating Product_Overview_bricklets.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricklets.table'), 'wb').write(make_product_overview_table(bricklets, 'bricklet', 20, 70))

    print 'Generating Downloads_bindings.table'
    file(os.path.join(path, 'source', 'Downloads_bindings.table'), 'wb').write(make_downloads_table())

    for brick in bricks:
        if len(brick[2]) == 0:
            continue

        name = brick[0].replace(' ', '_').replace('-', '')

        print 'Generating {0}_Brick_hlpi.table'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick_hlpi.table'), 'wb').write(make_hlpi_table(brick, 'brick'))

    for bricklet in bricklets:
        if len(bricklet[2]) == 0:
            continue

        name = bricklet[0].replace(' ', '_').replace('-', '')

        print 'Generating {0}_Brick_hlpi.table'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '_hlpi.table'), 'wb').write(make_hlpi_table(bricklet, 'bricklet'))


if __name__ == "__main__":
    generate(os.getcwd())
