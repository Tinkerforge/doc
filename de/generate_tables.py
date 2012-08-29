#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

            # display,  uri
bindings = [('Modbus', 'modbus', False),
            ('TCP/IP', 'tcpip',  False),
            ('C/C++',  'c',      True),
            ('C#',     'csharp', True),
            ('Delphi', 'delphi', True),
            ('Java',   'java',   True),
            ('PHP',    'php',    True),
            ('Python', 'python', True),
            ('Ruby',   'ruby',   True)]

          # display,   uri,      bindings,  description
bricks = [('DC',      'dc',      bindings, 'Steuert einen DC Motor mit max. 28V und 5A'),
          ('Debug',   'debug',   [],       'Für Firmware Entwickler: JTAG und serielle Konsole'),
          ('IMU',     'imu',     bindings, 'Voll ausgestattetes AHRS mit 9 Freiheitsgraden'),
          ('Master',  'master',  bindings, 'Ist Grundlage um Stapel zu bauen und bietet 4 Bricklet Anschlüsse'),
          ('Servo',   'servo',   bindings, 'Steuert bis zu 7 RC Servos mit max. 3A'),
          ('Stepper', 'stepper', bindings, 'Steuert einen bipolaren Schrittmotor mit max. 38V und 2,5A pro Phase')]

             # display,          uri,             bindings,  description
bricklets = [('Ambient Light',  'ambient_light',  bindings, 'Misst Umgebungslicht bis zu 900Lux'),
             ('Analog In',      'analog_in',      bindings, 'Misst elektrische Spannungen bis zu 45V'),
             ('Analog Out',     'analog_out',     bindings, 'Erzeugt konfigurierbare elektrische Spannungen bis zu 5V'),
             ('Breakout',       'breakout',       [],       'Macht alle Bricklet Signale zugänglich'),
             ('Current12',      'current12',      bindings, 'Bidirektionaler Stromsensor für bis zu 12,5A'),
             ('Current25',      'current25',      bindings, 'Bidirektionaler Stromsensor für bis zu 25A'),
             ('Distance IR',    'distance_ir',    bindings, 'Misst Entfernungen bis zu 150cm mit IR Licht'),
             ('Dual Relay',     'dual_relay',     bindings, 'Zwei Relais um AC/DC Geräte zu schalten'),
             ('Humidity',       'humidity',       bindings, 'Misst relative Luftfeuchtigkeit'),
             ('IO-16',          'io16',           bindings, '16 digitale Ein- und Ausgänge'),
             ('IO-4',           'io4',            bindings, '4 digitale Ein- und Ausgänge'),
             ('Joystick',       'joystick',       bindings, '2-Achsen Joystick mit Taster'),
             ('LCD 16x2',       'lcd_16x2',       bindings, '16x2 Zeichen alphanumerisches Display'),
             ('LCD 20x4',       'lcd_20x4',       bindings, '20x4 Zeichen alphanumerisches Display'),
             ('Linear Poti',    'linear_poti',    bindings, '59mm Linear-Potentiometer'),
             ('Piezo Buzzer',   'piezo_buzzer',   bindings, 'Erzeugt 1kHz Piepton'),
             ('Rotary Poti',    'rotary_poti',    bindings, '300° Dreh-Potentiometer'),
             ('Temperature',    'temperature',    bindings, 'Misst Umgebungstemperatur mit 0,5°C Genauigkeit'),
             ('Temperature IR', 'temperature_ir', bindings, 'Kontaktlose Objekttemperaturmessung von -70°C bis 380°C'),
             ('Voltage',        'voltage',        bindings, 'Misst Spannungen bis zu 50V')]

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
   :header: "Name", "Beschreibung", {0}
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
 :header: "", "Bindings und Beispiele"
 :delim: |
 :widths: 10, 60

 **Sprache** | """
    row_cell = '`{0} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_latest.zip>`__'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row_cell.format(binding[0], binding[1]))

    return table_head + ', '.join(rows)

def make_api_bindings_table():
    row = '* :ref:`{0} <ipcon_{1}>`'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row.format(binding[0], binding[1]))

    return '\n'.join(rows)

def make_hlpi_table(device, category):
    table_head = """
.. csv-table::
   :header: "Sprache", "API", "Beispiele", "Installation"
   :widths: 25, 8, 15, 12

"""
    row_source = '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Beispiele <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"'
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

    print 'Generating API_Bindings_bindings.table'
    file(os.path.join(path, 'source', 'Software', 'API_Bindings_bindings.table'), 'wb').write(make_api_bindings_table())

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

        print 'Generating {0}_hlpi.table'.format(name)
        file(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '_hlpi.table'), 'wb').write(make_hlpi_table(bricklet, 'bricklet'))


if __name__ == "__main__":
    generate(os.getcwd())
