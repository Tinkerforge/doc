#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as etreefromstring

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
'barometer': {
    'en': 'Measures air pressure and altitude changes',
    'de': 'Misst Luftdruck und Höhenänderungen'
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
'gps': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'humidity': {
    'en': 'Measures relative humidity',
    'de': 'Misst relative Luftfeuchtigkeit'
    },
'industrial_digital_in_4': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'industrial_digital_out_4': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'industrial_quad_relay': {
    'en': 'FIXME',
    'de': 'FIXME'
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
    'en': 'Wireless WIFI Master Extension',
    'de': 'Drahtlose WIFI Master Extension'
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

download_tools_source_code = {
'en': 'Source Code',
'de': 'Quelltext'
}

download_tools_table_head = {
'en':
""".. csv-table::
 :header: "Tool", "Current Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

""",
'de':
""".. csv-table::
 :header: "Tool", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

"""
}

download_bindings_table_head = {
'en':
""".. csv-table::
 :header: "Language", "Current Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

""",
'de':
""".. csv-table::
 :header: "Sprache", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

"""
}

download_firmwares_table_head = {
'en':
""".. csv-table::
 :header: "", "Current Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

 **Bricks** | |
{0}
 | |
 **Bricklets** | |
 {1}""",
'de':
""".. csv-table::
 :header: "", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 20, 50, 20

 **Bricks** | |
{0}
 | |
 **Bricklets** | |
{1}"""
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
    global tools, bindings, bricks, bricklets, extensions, power_supplies

             # display,        uri
    tools = [('Brick Daemon', 'brickd'),
             ('Brick Viewer', 'brickv')]

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

                 # display,                      uri,                         bindings, description
    bricklets = [('Ambient Light',              'ambient_light',              bindings, bricklet_descriptions['ambient_light'][lang]),
                 ('Analog In',                  'analog_in',                  bindings, bricklet_descriptions['analog_in'][lang]),
                 ('Analog Out',                 'analog_out',                 bindings, bricklet_descriptions['analog_out'][lang]),
                 ('Barometer',                  'barometer',                  bindings, bricklet_descriptions['barometer'][lang]),
                 ('Breakout',                   'breakout',                   [],       bricklet_descriptions['breakout'][lang]),
                 ('Current12',                  'current12',                  bindings, bricklet_descriptions['current12'][lang]),
                 ('Current25',                  'current25',                  bindings, bricklet_descriptions['current25'][lang]),
                 ('Distance IR',                'distance_ir',                bindings, bricklet_descriptions['distance_ir'][lang]),
                 ('Dual Relay',                 'dual_relay',                 bindings, bricklet_descriptions['dual_relay'][lang]),
                 #('GPS',                        'gps',                        bindings, bricklet_descriptions['gps'][lang]),
                 ('Humidity',                   'humidity',                   bindings, bricklet_descriptions['humidity'][lang]),
                 #('Industrial Digital In 4',    'industrial_digital_in_4',    bindings, bricklet_descriptions['industrial_digital_in_4'][lang]),
                 #('Industrial Digital Out 4',   'industrial_digital_out_4',   bindings, bricklet_descriptions['industrial_digital_out_4'][lang]),
                 #('Industrial Quad Relay',      'industrial_quad_relay',      bindings, bricklet_descriptions['industrial_quad_relay'][lang]),
                 ('IO-16',                      'io16',                       bindings, bricklet_descriptions['io16'][lang]),
                 ('IO-4',                       'io4',                        bindings, bricklet_descriptions['io4'][lang]),
                 ('Joystick',                   'joystick',                   bindings, bricklet_descriptions['joystick'][lang]),
                 ('LCD 16x2',                   'lcd_16x2',                   bindings, bricklet_descriptions['lcd_16x2'][lang]),
                 ('LCD 20x4',                   'lcd_20x4',                   bindings, bricklet_descriptions['lcd_20x4'][lang]),
                 ('Linear Poti',                'linear_poti',                bindings, bricklet_descriptions['linear_poti'][lang]),
                 ('Piezo Buzzer',               'piezo_buzzer',               bindings, bricklet_descriptions['piezo_buzzer'][lang]),
                 ('Rotary Poti',                'rotary_poti',                bindings, bricklet_descriptions['rotary_poti'][lang]),
                 ('Temperature',                'temperature',                bindings, bricklet_descriptions['temperature'][lang]),
                 ('Temperature IR',             'temperature_ir',             bindings, bricklet_descriptions['temperature_ir'][lang]),
                 ('Voltage',                    'voltage',                    bindings, bricklet_descriptions['voltage'][lang])]

                  # display,             uri,     bindings, description
    extensions = [('Chibi Extension',   'chibi',  [],       extension_descriptions['chibi'][lang]),
                  ('RS485 Extension',   'rs485',  [],       extension_descriptions['rs485'][lang]),
                  ('WIFI Extension',    'wifi',   [],       extension_descriptions['wifi'][lang])]

                      # display,                  uri,         bindings, description
    power_supplies = [('Step-Down Power Supply', 'step_down',  [],       power_supply_descriptions['step_down'][lang])]

def get_body(url):
    response = urllib2.urlopen(url)
    data = response.read().replace('<hr>', '').replace('<br>', '')
    response.close()
    tree = etreefromstring(data)
    return tree.find('body')

def get_tool_versions(url, regex):
    print 'Discovering ' + url
    body = get_body(url)
    versions = []

    for a in body.getiterator('a'):
        url_part = a.text.replace('/', '')

        if url_part == '..':
            continue

        m = re.match(regex, url_part)

        if m is None:
            continue

        versions.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

    return sorted(versions)

def get_bindings_versions(url, name):
    print 'Discovering ' + url
    body = get_body(url)
    versions = []

    for a in body.getiterator('a'):
        url_part = a.text.replace('/', '')

        if url_part == '..':
            continue

        m = re.match('tinkerforge_{0}_bindings_(\d+)_(\d+)_(\d+)\.zip'.format(name), url_part)

        if m is None:
            continue

        versions.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

    return sorted(versions)

def get_firmware_versions(url, prefix):
    print 'Discovering ' + url
    body = get_body(url)
    versions = []

    for a in body.getiterator('a'):
        url_part = a.text.replace('/', '')

        if url_part == '..':
            continue

        m = re.match(prefix + '_firmware_(\d+)_(\d+)_(\d+)\.bin', url_part)

        if m is None:
            continue

        versions.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

    return sorted(versions)

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

def make_download_tools_table():
    source_code = download_tools_source_code[lang]
    table_head = download_tools_table_head[lang]
    row_cell = ' :ref:`{0} <{1}>` | {3}.{4}.{5} - `Linux <http://download.tinkerforge.com/tools/{1}/linux/{1}-{3}.{4}.{5}_all.deb>`__, `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{3}_{4}_{5}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{3}_{4}_{5}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/zipball/v{3}.{4}.{5}>`__ | `Changelog <https://raw.github.com/Tinkerforge/{1}/master/changelog>`__'
    rows = []

    for tool in tools:
        linux_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/linux/'.format(tool[1]), '{0}-(\d+).(\d+).(\d+)_all.deb'.format(tool[1]))
        macos_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/macos/'.format(tool[1]), '{0}_macos_(\d+)_(\d+)_(\d+).dmg'.format(tool[1]))
        windows_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/windows/'.format(tool[1]), '{0}_windows_(\d+)_(\d+)_(\d+).exe'.format(tool[1]))

        if len(linux_versions) == 0:
            raise 'Could not find Linux versions of {0}'.format(tool[0])

        if len(macos_versions) == 0:
            raise 'Could not find Mac OS X versions of {0}'.format(tool[0])

        if len(windows_versions) == 0:
            raise 'Could not find Windows versions of {0}'.format(tool[0])

        if len(set([linux_versions[-1], macos_versions[-1], windows_versions[-1]])) != 1:
            raise 'Cross-platform version mismatch for {0}'.format(tool[0])

        rows.append(row_cell.format(tool[0], tool[1], source_code, *linux_versions[-1]))

    return table_head + '\n'.join(rows)

def make_download_bindings_table():
    table_head = download_bindings_table_head[lang]
    row_cell = ' {0} | `{2}.{3}.{4} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_{2}_{3}_{4}.zip>`__ | `Changelog <https://raw.github.com/Tinkerforge/generators/master/{1}/changelog.txt>`__'
    rows = []

    for binding in bindings:
        if binding[2]:
            versions = get_bindings_versions('http://download.tinkerforge.com/bindings/{0}/'.format(binding[1]), binding[1])

            if len(versions) == 0:
                raise 'Could not find versions of the {0} bindings'.format(binding[0])

            rows.append(row_cell.format(binding[0], binding[1], *versions[-1]))

    return table_head + '\n'.join(rows)

def make_download_firmwares_table():
    table_head = download_firmwares_table_head[lang]
    brick_row_cell = ' :ref:`{0} <{1}_brick>` | `{3}.{4}.{5} <http://download.tinkerforge.com/firmwares/bricks/{1}/brick_{1}_firmware_{3}_{4}_{5}.bin>`__ | `Changelog <https://raw.github.com/Tinkerforge/{2}-brick/master/software/changelog>`__'
    bricklet_row_cell = ' :ref:`{0} <{1}_bricklet>` | `{3}.{4}.{5} <http://download.tinkerforge.com/firmwares/bricklets/{1}/bricklet_{1}_firmware_{3}_{4}_{5}.bin>`__ | `Changelog <https://raw.github.com/Tinkerforge/{2}-bricklet/master/software/changelog>`__'
    brick_rows = []
    bricklet_rows = []

    for brick in bricks:
        if len(brick[2]) > 0:
            versions = get_firmware_versions('http://download.tinkerforge.com/firmwares/bricks/{0}/'.format(brick[1]), 'brick_' + brick[1])

            if len(versions) < 1:
                raise 'Could not find versions of the {0} Brick firmware'.format(brick[0])

            brick_rows.append(brick_row_cell.format(brick[0], brick[1], brick[1].replace('_', '-'), *versions[-1]))

    for bricklet in bricklets:
        if len(bricklet[2]) > 0:
            versions = get_firmware_versions('http://download.tinkerforge.com/firmwares/bricklets/{0}/'.format(bricklet[1]), 'bricklet_' + bricklet[1])

            if len(versions) < 1:
                raise 'Could not find versions of the {0} Bricklet firmware'.format(bricklet[0])

            bricklet_rows.append(bricklet_row_cell.format(bricklet[0], bricklet[1], bricklet[1].replace('_', '-'), *versions[-1]))

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows))

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

    print 'Generating Downloads_tools.table'
    file(os.path.join(path, 'source', 'Downloads_tools.table'), 'wb').write(make_download_tools_table())

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
