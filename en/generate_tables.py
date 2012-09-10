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
bricks = [('DC',      'dc',      bindings, 'Drives one brushed DC motor with max. 28V and 5A'),
          ('Debug',   'debug',   [],       'For Firmware Developers: JTAG and serial console'),
          ('IMU',     'imu',     bindings, 'Full fledged AHRS with 9 degrees of freedom'),
          ('Master',  'master',  bindings, 'Is the basis to build stacks and has 4 Bricklet Ports'),
          ('Servo',   'servo',   bindings, 'Drives up to 7 RC Servos with max. 3A'),
          ('Stepper', 'stepper', bindings, 'Drives one bipolar stepper motor with max. 38V and 2.5A per phase')]

             # display,          uri,             bindings,  description
bricklets = [('Ambient Light',  'ambient_light',  bindings, 'Measures ambient light up to 900lux'),
             ('Analog In',      'analog_in',      bindings, 'Measures voltages up to 45V'),
             ('Analog Out',     'analog_out',     bindings, 'Generates configurable voltages up to 5V'),
             ('Breakout',       'breakout',       [],       'Makes all Bricklet signals available'),
             ('Current12',      'current12',      bindings, 'Bidirectional current sensor for up to 12.5A'),
             ('Current25',      'current25',      bindings, 'Bidirectional current sensor for up to 25A'),
             ('Distance IR',    'distance_ir',    bindings, 'Measures distances up to 150cm with IR light'),
             ('Dual Relay',     'dual_relay',     bindings, 'Two relays to switch AC/DC devices'),
             ('Humidity',       'humidity',       bindings, 'Measures relative humidity'),
             ('IO-16',          'io16',           bindings, '16-channel digital input/output'),
             ('IO-4',           'io4',            bindings, '4-channel digital input/output'),
             ('Joystick',       'joystick',       bindings, '2-axis joystick with push-button'),
             ('LCD 16x2',       'lcd_16x2',       bindings, '16x2 character alphanumeric display with blue backlight'),
             ('LCD 20x4',       'lcd_20x4',       bindings, '20x4 character alphanumeric display with blue backlight'),
             ('Linear Poti',    'linear_poti',    bindings, '59mm linear potentiometer'),
             ('Piezo Buzzer',   'piezo_buzzer',   bindings, 'Creates 1kHz beep'),
             ('Rotary Poti',    'rotary_poti',    bindings, '300° rotary potentiometer'),
             ('Temperature',    'temperature',    bindings, 'Measures ambient temperature with 0.5°C accuracy'),
             ('Temperature IR', 'temperature_ir', bindings, 'Measures contactless object temperature from -70°C to 380°C'),
             ('Voltage',        'voltage',        bindings, 'Measures voltages up to 50V')]

              # display,            uri,      bindings,  description
extensions = [('Chibi Extension',   'chibi',  [],        'Wireless Chibi Master Extension'),
              ('RS485 Extension',   'rs485',  [],        'Cable based RS485 Master Extension')]

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

def make_product_overview_table(devices, category, name_width, description_width, has_bindings):
    if has_bindings:
        table_head = """
.. csv-table::
   :header: "Name", "Description", {0}
   :widths: {1}, {2}, {3}

""".format(', '.join(['"{0}"'.format(binding[0]) for binding in bindings]),
           name_width,
           description_width,
           ', '.join(['5'] * len(bindings)))
        row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}", '
    else:
        table_head = """
.. csv-table::
   :header: "Name", "Description"
   :widths: {0}, {1}

""".format(name_width, description_width)
        row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}"'

    row_cell = '":ref:`{0} <{1}_' + category + '_{2}>`"'
    rows = []

    for device in devices:
        cells = []

        for binding in device[2]:
            cells.append(row_cell.format(binding[0], device[1], binding[1]))

        row = row_head.format(device[0], device[1], device[3]) + ', '.join(cells)
        rows.append(row)

    return table_head + '\n'.join(rows)

def make_download_bindings_table():
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

def make_download_firmwares_table():
    table_head = """.. csv-table::
 :header: "", "Firmwares and Plugins"
 :delim: |
 :widths: 10, 60

 **Bricks** | {0}
 **Bricklets** | {1}"""
    brick_row_cell = '`{0} <http://download.tinkerforge.com/firmwares/bricks/{1}/brick_{1}_firmware_latest.bin>`__'
    bricklet_row_cell = '`{0} <http://download.tinkerforge.com/firmwares/bricklets/{1}/bricklet_{1}_firmware_latest.bin>`__'
    brick_rows = []
    bricklet_rows = []

    for brick in bricks:
        if len(brick[2]) > 0:
            brick_rows.append(brick_row_cell.format(brick[0], brick[1]))

    for bricklet in bricklets:
        if len(bricklet[2]) > 0:
            bricklet_rows.append(bricklet_row_cell.format(bricklet[0], bricklet[1]))

    return table_head.format(', '.join(brick_rows), ', '.join(bricklet_rows))

def make_api_bindings_table():
    row = '* :ref:`{0} <ipcon_{1}>`'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row.format(binding[0], binding[1]))

    return '\n'.join(rows)

def make_source_code_gits_table():
    table_head = """.. csv-table::
 :header: "", "Repository", "Bug Tracking"
 :delim: |
 :widths: 10, 30, 10

 **Tools** | |
 Brick Daemon | `git://github.com/Tinkerforge/brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Report Bug <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `git://github.com/Tinkerforge/brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Report Bug <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `git://github.com/Tinkerforge/brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Report Bug <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `git://github.com/Tinkerforge/bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Report Bug <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `git://github.com/Tinkerforge/brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Report Bug <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `git://github.com/Tinkerforge/generators.git <https://github.com/Tinkerforge/generators/>`__ | `Report Bug <https://github.com/Tinkerforge/generators/issues>`__
 Kicad Libraries | `git://github.com/Tinkerforge/kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Report Bug <https://github.com/Tinkerforge/kicad-libraries/issues>`__
 | |
 **Bricks** | |
{0}
 | |
 **Bricklets** | |
{1}
 | |
 **Master Extensions** | |
{2}
 | |
 **Power Supplies** | |
 Step-Down Power Supply | `git://github.com/Tinkerforge/step-down-powersupply.git <https://github.com/Tinkerforge/step-down-powersupply/>`__ | `Report Bug <https://github.com/Tinkerforge/step-down-powersupply/issues>`__
 | |
 **Accessories** | |
 DC Jack Adapter | `git://github.com/Tinkerforge/dc-adapter.git <https://github.com/Tinkerforge/dc-adapter/>`__ | `Report Bug <https://github.com/Tinkerforge/dc-adapter/issues>`__
 """
    brick_row_cell = ' {0} | `git://github.com/Tinkerforge/{1}-brick.git <https://github.com/Tinkerforge/{1}-brick/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-brick/issues>`__'
    bricklet_row_cell = ' {0} | `git://github.com/Tinkerforge/{1}-bricklet.git <https://github.com/Tinkerforge/{1}-bricklet/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-bricklet/issues>`__'
    extension_row_cell = ' {0} | `git://github.com/Tinkerforge/{1}-extension.git <https://github.com/Tinkerforge/{1}-extension/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-extension/issues>`__'
    brick_rows = []
    bricklet_rows = []
    extension_rows = []

    for brick in bricks:
        brick_rows.append(brick_row_cell.format(brick[0], brick[1].replace('_', '-')))

    for bricklet in bricklets:
        bricklet_rows.append(bricklet_row_cell.format(bricklet[0], bricklet[1].replace('_', '-')))

    for extension in extensions:
        extension_rows.append(extension_row_cell.format(extension[0], extension[1].replace('_', '-')))

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows), '\n'.join(extension_rows))

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

    print 'Generating index_extensions.table'
    file(os.path.join(path, 'source', 'index_extensions.table'), 'wb').write(make_index_table(extensions, 'extension'))

    print 'Generating Product_Overview_bricks.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricks.table'), 'wb').write(make_product_overview_table(bricks, 'brick', 15, 40, True))

    print 'Generating Product_Overview_bricklets.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricklets.table'), 'wb').write(make_product_overview_table(bricklets, 'bricklet', 20, 70, True))

    print 'Generating Product_Overview_extensions.table'
    file(os.path.join(path, 'source', 'Product_Overview_extensions.table'), 'wb').write(make_product_overview_table(extensions, 'extension', 20, 70, False))

    print 'Generating Downloads_bindings.table'
    file(os.path.join(path, 'source', 'Downloads_bindings.table'), 'wb').write(make_download_bindings_table())

    print 'Generating Downloads_firmwares.table'
    file(os.path.join(path, 'source', 'Downloads_firmwares.table'), 'wb').write(make_download_firmwares_table())

    print 'Generating API_Bindings_bindings.table'
    file(os.path.join(path, 'source', 'Software', 'API_Bindings_bindings.table'), 'wb').write(make_api_bindings_table())

    print 'Generating Source_Code_gits.table'
    file(os.path.join(path, 'source', 'Source_Code_gits.table'), 'wb').write(make_source_code_gits_table())

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
