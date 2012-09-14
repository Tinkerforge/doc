#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

brick_descriptions = {
'dc': {
    'en': 'Drives one brushed DC motor with max. 28V and 5A',
    'de': 'Steuert einen DC Motor mit max. 28V und 5A'
    },
'debug': {
    'en': 'For Firmware Developers: JTAG and serial console',
    'de': 'Für Firmware Entwickler: JTAG und serielle Konsole'
    },
'imu': {
    'en': 'Full fledged AHRS with 9 degrees of freedom',
    'de': 'Voll ausgestattetes AHRS mit 9 Freiheitsgraden'
    },
'master': {
    'en': 'Is the basis to build stacks and has 4 Bricklet Ports',
    'de': 'Ist Grundlage um Stapel zu bauen und bietet 4 Bricklet Anschlüsse'
    },
'servo': {
    'en': 'Drives up to 7 RC Servos with max. 3A',
    'de': 'Steuert bis zu 7 RC Servos mit max. 3A'
    },
'stepper': {
    'en': 'Drives one bipolar stepper motor with max. 38V and 2.5A per phase',
    'de': 'Steuert einen bipolaren Schrittmotor mit max. 38V und 2,5A pro Phase'
    }
}

bricklet_descriptions = {
'ambient_light': {
    'en': 'Measures ambient light up to 900lux',
    'de': 'Misst Umgebungslicht bis zu 900Lux'
    },
'analog_in': {
    'en': 'Measures voltages up to 45V',
    'de': 'Misst elektrische Spannungen bis zu 45V'
    },
'analog_out': {
    'en': 'Generates configurable voltages up to 5V',
    'de': 'Erzeugt konfigurierbare elektrische Spannungen bis zu 5V'
    },
'breakout': {
    'en': 'Makes all Bricklet signals available',
    'de': 'Macht alle Bricklet Signale zugänglich'
    },
'current12': {
    'en': 'Bidirectional current sensor for up to 12.5A',
    'de': 'Bidirektionaler Stromsensor für bis zu 12,5A'
    },
'current25': {
    'en': 'Bidirectional current sensor for up to 25A',
    'de': 'Bidirektionaler Stromsensor für bis zu 25A'
    },
'distance_ir': {
    'en': 'Measures distances up to 150cm with IR light',
    'de': 'Misst Entfernungen bis zu 150cm mit IR Licht'
    },
'dual_relay': {
    'en': 'Two relays to switch AC/DC devices',
    'de': 'Zwei Relais um AC/DC Geräte zu schalten'
    },
'humidity': {
    'en': 'Measures relative humidity',
    'de': 'Misst relative Luftfeuchtigkeit'
    },
'io16': {
    'en': '16-channel digital input/output',
    'de': '16 digitale Ein- und Ausgänge'
    },
'io4': {
    'en': '4-channel digital input/output',
    'de': '4 digitale Ein- und Ausgänge'
    },
'joystick': {
    'en': '2-axis joystick with push-button',
    'de': '2-Achsen Joystick mit Taster'
    },
'lcd_16x2': {
    'en': '16x2 character alphanumeric display with blue backlight',
    'de': '16x2 Zeichen alphanumerisches Display'
    },
'lcd_20x4': {
    'en': '20x4 character alphanumeric display with blue backlight',
    'de': '20x4 Zeichen alphanumerisches Display'
    },
'linear_poti': {
    'en': '59mm linear potentiometer',
    'de': '59mm Linear-Potentiometer'
    },
'piezo_buzzer': {
    'en': 'Creates 1kHz beep',
    'de': 'Erzeugt 1kHz Piepton'
    },
'rotary_poti': {
    'en': '300° rotary potentiometer',
    'de': '300° Dreh-Potentiometer'
    },
'temperature': {
    'en': 'Measures ambient temperature with 0.5°C accuracy',
    'de': 'Misst Umgebungstemperatur mit 0,5°C Genauigkeit'
    },
'temperature_ir': {
    'en': 'Measures contactless object temperature from -70°C to 380°C',
    'de': 'Kontaktlose Objekttemperaturmessung von -70°C bis 380°C'
    },
'voltage': {
    'en': 'Measures voltages up to 50V',
    'de': 'Misst Spannungen bis zu 50V'
    }
}

extension_descriptions = {
'chibi': {
    'en': 'Wireless Chibi Master Extension',
    'de': 'Drahtlose Chibi Master Extension'
    },
'rs485': {
    'en': 'Cable based RS485 Master Extension',
    'de': 'Kabelgebundene RS485 Master Extension'
    },
'wifi': {
    'en': 'WIFI Master Extension',
    'de': 'WIFI Master Extension'
    }
}

power_supply_descriptions = {
'step_down': {
    'en': 'Powers a stack of Bricks with 5V',
    'de': 'Versorgt einen Stapel von Bricks mit 5V'
    }
}

product_overview_table_head_with_bindings = {
'en':
"""
.. csv-table::
   :header: "Name", "Description", {0}
   :widths: {1}, {2}, {3}

""",
'de':
"""
.. csv-table::
   :header: "Name", "Beschreibung", {0}
   :widths: {1}, {2}, {3}

"""
}

product_overview_table_head_without_bindings = {
'en':
"""
.. csv-table::
   :header: "Name", "Description"
   :widths: {0}, {1}

""",
'de':
"""
.. csv-table::
   :header: "Name", "Beschreibung"
   :widths: {0}, {1}

"""
}

download_bindings_table_head = {
'en':
""".. csv-table::
 :header: "", "Bindings and Examples"
 :delim: |
 :widths: 10, 60

 **Language** | """,
'de':
""".. csv-table::
 :header: "", "Bindings und Beispiele"
 :delim: |
 :widths: 10, 60

 **Sprache** | """
}

download_firmwares_table_head = {
'en':
""".. csv-table::
 :header: "", "Firmwares and Plugins"
 :delim: |
 :widths: 10, 60

 **Bricks** | {0}
 **Bricklets** | {1}""",
'de':
""".. csv-table::
 :header: "", "Firmwares und Plugins"
 :delim: |
 :widths: 10, 60

 **Bricks** | {0}
 **Bricklets** | {1}"""
}

source_code_gits_table_head = {
'en':
""".. csv-table::
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
""",
'de':
 """.. csv-table::
 :header: "", "Repository", "Bug Tracking"
 :delim: |
 :widths: 10, 30, 10

 **Tools** | |
 Brick Daemon | `git://github.com/Tinkerforge/brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Problem melden <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `git://github.com/Tinkerforge/brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Problem melden <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `git://github.com/Tinkerforge/brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Problem melden <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `git://github.com/Tinkerforge/bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Problem melden <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `git://github.com/Tinkerforge/brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Problem melden <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `git://github.com/Tinkerforge/generators.git <https://github.com/Tinkerforge/generators/>`__ | `Problem melden <https://github.com/Tinkerforge/generators/issues>`__
 Kicad Libraries | `git://github.com/Tinkerforge/kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Problem melden <https://github.com/Tinkerforge/kicad-libraries/issues>`__
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
 **Stromversorgungen** | |
 Step-Down Power Supply | `git://github.com/Tinkerforge/step-down-powersupply.git <https://github.com/Tinkerforge/step-down-powersupply/>`__ | `Problem melden <https://github.com/Tinkerforge/step-down-powersupply/issues>`__
 | |
 **Zubehör** | |
 DC Jack Adapter | `git://github.com/Tinkerforge/dc-adapter.git <https://github.com/Tinkerforge/dc-adapter/>`__ | `Problem melden <https://github.com/Tinkerforge/dc-adapter/issues>`__
"""
}

source_code_gits_brick_row_cell = {
'en': ' {0} | `git://github.com/Tinkerforge/{1}-brick.git <https://github.com/Tinkerforge/{1}-brick/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-brick/issues>`__',
'de': ' {0} | `git://github.com/Tinkerforge/{1}-brick.git <https://github.com/Tinkerforge/{1}-brick/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-brick/issues>`__'
}

source_code_gits_bricklet_row_cell = {
'en': ' {0} | `git://github.com/Tinkerforge/{1}-bricklet.git <https://github.com/Tinkerforge/{1}-bricklet/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-bricklet/issues>`__',
'de': ' {0} | `git://github.com/Tinkerforge/{1}-bricklet.git <https://github.com/Tinkerforge/{1}-bricklet/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-bricklet/issues>`__',
}

source_code_gits_extension_row_cell = {
'en': ' {0} | `git://github.com/Tinkerforge/{1}-extension.git <https://github.com/Tinkerforge/{1}-extension/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-extension/issues>`__',
'de': ' {0} | `git://github.com/Tinkerforge/{1}-extension.git <https://github.com/Tinkerforge/{1}-extension/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-extension/issues>`__',
}

hlpi_table_head = {
'en':
"""
.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

""",
'de':
"""
.. csv-table::
   :header: "Sprache", "API", "Beispiele", "Installation"
   :widths: 25, 8, 15, 12

"""
}

hlpi_row_source = {
'en': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Examples <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"',
'de': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Beispiele <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"'
}

def fill_dicts():
    global bindings, bricks, bricklets, extensions, power_supplies

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

              # display,   uri,      bindings, description
    bricks = [('DC',      'dc',      bindings, brick_descriptions['dc'][lang]),
              ('Debug',   'debug',   [],       brick_descriptions['debug'][lang]),
              ('IMU',     'imu',     bindings, brick_descriptions['imu'][lang]),
              ('Master',  'master',  bindings, brick_descriptions['master'][lang]),
              ('Servo',   'servo',   bindings, brick_descriptions['servo'][lang]),
              ('Stepper', 'stepper', bindings, brick_descriptions['stepper'][lang])]

                 # display,          uri,             bindings, description
    bricklets = [('Ambient Light',  'ambient_light',  bindings, bricklet_descriptions['ambient_light'][lang]),
                 ('Analog In',      'analog_in',      bindings, bricklet_descriptions['analog_in'][lang]),
                 ('Analog Out',     'analog_out',     bindings, bricklet_descriptions['analog_out'][lang]),
                 ('Breakout',       'breakout',       [],       bricklet_descriptions['breakout'][lang]),
                 ('Current12',      'current12',      bindings, bricklet_descriptions['current12'][lang]),
                 ('Current25',      'current25',      bindings, bricklet_descriptions['current25'][lang]),
                 ('Distance IR',    'distance_ir',    bindings, bricklet_descriptions['distance_ir'][lang]),
                 ('Dual Relay',     'dual_relay',     bindings, bricklet_descriptions['dual_relay'][lang]),
                 ('Humidity',       'humidity',       bindings, bricklet_descriptions['humidity'][lang]),
                 ('IO-16',          'io16',           bindings, bricklet_descriptions['io16'][lang]),
                 ('IO-4',           'io4',            bindings, bricklet_descriptions['io4'][lang]),
                 ('Joystick',       'joystick',       bindings, bricklet_descriptions['joystick'][lang]),
                 ('LCD 16x2',       'lcd_16x2',       bindings, bricklet_descriptions['lcd_16x2'][lang]),
                 ('LCD 20x4',       'lcd_20x4',       bindings, bricklet_descriptions['lcd_20x4'][lang]),
                 ('Linear Poti',    'linear_poti',    bindings, bricklet_descriptions['linear_poti'][lang]),
                 ('Piezo Buzzer',   'piezo_buzzer',   bindings, bricklet_descriptions['piezo_buzzer'][lang]),
                 ('Rotary Poti',    'rotary_poti',    bindings, bricklet_descriptions['rotary_poti'][lang]),
                 ('Temperature',    'temperature',    bindings, bricklet_descriptions['temperature'][lang]),
                 ('Temperature IR', 'temperature_ir', bindings, bricklet_descriptions['temperature_ir'][lang]),
                 ('Voltage',        'voltage',        bindings, bricklet_descriptions['voltage'][lang])]

                  # display,             uri,     bindings, description
    extensions = [('Chibi Extension',   'chibi',  [],       extension_descriptions['chibi'][lang]),
                  ('RS485 Extension',   'rs485',  [],       extension_descriptions['rs485'][lang]),
                  #('WIFI Extension',    'wifi',   [],       extension_descriptions['wifi'][lang])
                  ]

                      # display,                  uri,         bindings, description
    power_supplies = [('Step-Down Power Supply', 'step_down',  [],       power_supply_descriptions['step_down'][lang])]

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

def make_product_overview_table(devices, category, name_width,
                                description_width, has_bindings):
    if has_bindings:
        table_head = product_overview_table_head_with_bindings[lang] \
                     .format(', '.join(['"{0}"'.format(binding[0]) for binding in bindings]),
                             name_width,
                             description_width,
                             ', '.join(['5'] * len(bindings)))
        row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}", '
    else:
        table_head = product_overview_table_head_without_bindings[lang] \
                     .format(name_width, description_width)
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
    table_head = download_bindings_table_head[lang]
    row_cell = '`{0} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_latest.zip>`__'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row_cell.format(binding[0], binding[1]))

    return table_head + ', '.join(rows)

def make_download_firmwares_table():
    table_head = download_firmwares_table_head[lang]
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
    table_head = source_code_gits_table_head[lang]
    brick_row_cell = source_code_gits_brick_row_cell[lang]
    bricklet_row_cell = source_code_gits_bricklet_row_cell[lang]
    extension_row_cell = source_code_gits_extension_row_cell[lang]
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
    table_head = hlpi_table_head[lang]
    row_source = hlpi_row_source[lang]
    row = '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"'
    rows = []

    for binding in device[2]:
        if binding[2]:
            rows.append(row_source.format(binding[0], device[1], category, binding[1]))
        else:
            rows.append(row.format(binding[0], device[1], category, binding[1]))

    return table_head + '\n'.join(rows)

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        print 'Wrong working directory'
        sys.exit(1)

    fill_dicts()

    print 'Generating index_bricks.table'
    file(os.path.join(path, 'source', 'index_bricks.table'), 'wb').write(make_index_table(bricks, 'brick'))

    print 'Generating index_bricklets.table'
    file(os.path.join(path, 'source', 'index_bricklets.table'), 'wb').write(make_index_table(bricklets, 'bricklet'))

    print 'Generating index_extensions.table'
    file(os.path.join(path, 'source', 'index_extensions.table'), 'wb').write(make_index_table(extensions, 'extension'))

    print 'Generating index_power_supplies.table'
    file(os.path.join(path, 'source', 'index_power_supplies.table'), 'wb').write(make_index_table(power_supplies, 'power_supply'))

    print 'Generating Product_Overview_bricks.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricks.table'), 'wb').write(make_product_overview_table(bricks, 'brick', 15, 40, True))

    print 'Generating Product_Overview_bricklets.table'
    file(os.path.join(path, 'source', 'Product_Overview_bricklets.table'), 'wb').write(make_product_overview_table(bricklets, 'bricklet', 20, 70, True))

    print 'Generating Product_Overview_extensions.table'
    file(os.path.join(path, 'source', 'Product_Overview_extensions.table'), 'wb').write(make_product_overview_table(extensions, 'extension', 20, 70, False))

    print 'Generating Product_Overview_power_supplies.table'
    file(os.path.join(path, 'source', 'Product_Overview_power_supplies.table'), 'wb').write(make_product_overview_table(power_supplies, 'power_supply', 30, 60, False))

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
