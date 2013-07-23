#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2
import traceback
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as etreefromstring

sys.path.append(os.path.join(os.getcwd(), '..', '..', 'generators'))
from device_identifiers import device_identifiers

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
'distance_us': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'dual_button': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'dual_relay': {
    'en': 'Two relays to switch AC/DC devices',
    'de': 'Zwei Relais um AC/DC Geräte zu schalten'
    },
'gps': {
    'en': 'Determine position, velocity and altitude',
    'de': 'Bestimmt Position, Geschwindigkeit und Höhe'
    },
'humidity': {
    'en': 'Measures relative humidity',
    'de': 'Misst relative Luftfeuchtigkeit'
    },
'industrial_digital_in_4': {
    'en': '4 galvanically isolated digital inputs',
    'de': '4 galvanisch getrennte digitale Eingänge'
    },
'industrial_digital_out_4': {
    'en': '4 galvanically isolated digital outputs',
    'de': '4 galvanisch getrennte digitale Ausgänge'
    },
'industrial_dual_0_20ma': {
    'en': 'Senses two currents between 0 and 20mA (IEC 60381-1)',
    'de': 'Misst zwei Stromquellen zwischen 0 und 20mA (IEC 60381-1)'
    },
'industrial_quad_relay': {
    'en': '4 galvanically isolated solid state relays',
    'de': '4 galvanisch getrennte Solid State Relais'
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
'led_strip': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'linear_poti': {
    'en': '59mm linear potentiometer',
    'de': '59mm Linear-Potentiometer'
    },
'moisture': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'motion_detector': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'multi_touch': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'piezo_buzzer': {
    'en': 'Creates 1kHz beep',
    'de': 'Erzeugt 1kHz Piepton'
    },
'ptc': {
    'en': 'Reads temperatures from Pt100/1000 sensors',
    'de': 'Liest Temperaturen von Pt100/1000-Sensoren'
    },
'remote_switch': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'rotary_encoder': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'rotary_poti': {
    'en': '300° rotary potentiometer',
    'de': '300° Dreh-Potentiometer'
    },
'segment_display_4x7': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'sound_intensity': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'temperature': {
    'en': 'Measures ambient temperature with 0.5°C accuracy',
    'de': 'Misst Umgebungstemperatur mit 0,5°C Genauigkeit'
    },
'temperature_ir': {
    'en': 'Measures contactless object temperature from -70°C to 380°C',
    'de': 'Kontaktlose Objekttemperaturmessung von -70°C bis 380°C'
    },
'tilt': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'voltage': {
    'en': 'Measures voltages up to 50V',
    'de': 'Misst Spannungen bis zu 50V'
    },
'voltage_current': {
    'en': 'Measure power, voltage and current up to 720W/36V/20A',
    'de': 'Misst Leistung, Spannung und Strom bis zu 720W/36V/20A'
    },
'water': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
}

extension_descriptions = {
'chibi': {
    'en': 'Wireless Chibi Master Extension',
    'de': 'Drahtlose Chibi Master Extension'
    },
'ethernet': {
    'en': 'Cable based Ethernet Master Extension',
    'de': 'Kabelgebundene Ethernet Master Extension'
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

accessories_descriptions = {
'dc_jack_adapter': {
    'en': 'Adapter between a 5mm DC jack and 2 Pole Black Connector',
    'de': 'Adapter zwischen einem 5mm DC Stecker und 2 Pin Stecker Schwarz'
    }
}


index_table_head = {
'en':
""".. csv-table::
 :header: "Hardware", "API"
 :delim: |
 :widths: 15, 40

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
 |
 **Master Extensions** |
{2}
 |
 **Power Supplies** |
{3}
 |
 **Accessories** |
{4}
""",
'de':
""".. csv-table::
 :header: "Hardware", "API"
 :delim: |
 :widths: 15, 40

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
 |
 **Master Extensions** |
{2}
 |
 **Stromversorgungen** |
{3}
 |
 **Zubehör** |
{4}
"""
}

product_overview_table_head = {
'en':
"""
.. csv-table::
   :header: "Name", "Description"
   :widths: 30, 70

""",
'de':
"""
.. csv-table::
   :header: "Name", "Beschreibung"
   :widths: 30, 70

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
 :widths: 15, 40, 8

""",
'de':
""".. csv-table::
 :header: "Tool", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 15, 40, 8

"""
}

download_bindings_table_head = {
'en':
""".. csv-table::
 :header: "Language", "Current Version", "Changelog"
 :delim: |
 :widths: 15, 40, 8

""",
'de':
""".. csv-table::
 :header: "Sprache", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 15, 40, 8

"""
}

download_firmwares_table_head = {
'en':
""".. csv-table::
 :header: "", "Current Version", "Changelog"
 :delim: |
 :widths: 15, 40, 8

 **Bricks** | |
{0}
 | |
 **Bricklets** | |
 {1}""",
'de':
""".. csv-table::
 :header: "", "Aktuelle Version", "Changelog"
 :delim: |
 :widths: 15, 40, 8

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
 :widths: 15, 30, 10

 **Tools** | |
 Brick Daemon | `git://github.com/Tinkerforge/brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Report Bug <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `git://github.com/Tinkerforge/brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Report Bug <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `git://github.com/Tinkerforge/brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Report Bug <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `git://github.com/Tinkerforge/bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Report Bug <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `git://github.com/Tinkerforge/brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Report Bug <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `git://github.com/Tinkerforge/generators.git <https://github.com/Tinkerforge/generators/>`__ | `Report Bug <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `git://github.com/Tinkerforge/kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Report Bug <https://github.com/Tinkerforge/kicad-libraries/issues>`__
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
 :widths: 15, 30, 10

 **Tools** | |
 Brick Daemon | `git://github.com/Tinkerforge/brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Problem melden <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `git://github.com/Tinkerforge/brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Problem melden <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `git://github.com/Tinkerforge/brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Problem melden <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `git://github.com/Tinkerforge/bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Problem melden <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `git://github.com/Tinkerforge/brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Problem melden <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `git://github.com/Tinkerforge/generators.git <https://github.com/Tinkerforge/generators/>`__ | `Problem melden <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `git://github.com/Tinkerforge/kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Problem melden <https://github.com/Tinkerforge/kicad-libraries/issues>`__
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

def fill_dicts():
    global tools, bindings, bricks, bricklets, extensions, power_supplies, accessories

             # display,        uri
    tools = [('Brick Daemon', 'brickd'),
             ('Brick Viewer', 'brickv')]

                # display,  uri      is_language
    bindings = [('Modbus', 'modbus', False),
                ('TCP/IP', 'tcpip',  False),
                ('C/C++',  'c',      True),
                ('C#',     'csharp', True),
                ('Delphi', 'delphi', True),
                ('Java',   'java',   True),
                ('PHP',    'php',    True),
                ('Python', 'python', True),
             #   ('Shell',  'shell',  True),
                ('Ruby',   'ruby',   True),
                ('VB.NET', 'vbnet',  True)]

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
                 #('Distance US',                'distance_us',                bindings, bricklet_descriptions['distance_us'][lang]),
                 #('Dual Button',                'dual_button',                bindings, bricklet_descriptions['dual_button'][lang]),
                 ('Dual Relay',                 'dual_relay',                 bindings, bricklet_descriptions['dual_relay'][lang]),
                 ('GPS',                        'gps',                        bindings, bricklet_descriptions['gps'][lang]),
                 ('Humidity',                   'humidity',                   bindings, bricklet_descriptions['humidity'][lang]),
                 ('Industrial Digital In 4',    'industrial_digital_in_4',    bindings, bricklet_descriptions['industrial_digital_in_4'][lang]),
                 ('Industrial Digital Out 4',   'industrial_digital_out_4',   bindings, bricklet_descriptions['industrial_digital_out_4'][lang]),
                 ('Industrial Dual 0-20mA',     'industrial_dual_0_20ma',     bindings, bricklet_descriptions['industrial_dual_0_20ma'][lang]),
                 ('Industrial Quad Relay',      'industrial_quad_relay',      bindings, bricklet_descriptions['industrial_quad_relay'][lang]),
                 ('IO-16',                      'io16',                       bindings, bricklet_descriptions['io16'][lang]),
                 ('IO-4',                       'io4',                        bindings, bricklet_descriptions['io4'][lang]),
                 ('Joystick',                   'joystick',                   bindings, bricklet_descriptions['joystick'][lang]),
                 ('LCD 16x2',                   'lcd_16x2',                   bindings, bricklet_descriptions['lcd_16x2'][lang]),
                 ('LCD 20x4',                   'lcd_20x4',                   bindings, bricklet_descriptions['lcd_20x4'][lang]),
                 #('LED Strip',                  'led_strip',                  bindings, bricklet_descriptions['led_strip'][lang]),
                 ('Linear Poti',                'linear_poti',                bindings, bricklet_descriptions['linear_poti'][lang]),
                 #('Moisture',                   'moisture',                   bindings, bricklet_descriptions['moisture'][lang]),
                 #('Motion Detector',            'motion_detector',            bindings, bricklet_descriptions['motion_detector'][lang]),
                 #('Multi Touch',                'multi_touch',                bindings, bricklet_descriptions['multi_touch'][lang]),
                 ('Piezo Buzzer',               'piezo_buzzer',               bindings, bricklet_descriptions['piezo_buzzer'][lang]),
                 ('PTC',                        'ptc',                        bindings, bricklet_descriptions['ptc'][lang]),
                 #('Remote Switch',              'remote_switch',              bindings, bricklet_descriptions['remote_switch'][lang]),
                 #('Rotary Encoder',             'rotary_encoder',             bindings, bricklet_descriptions['rotary_encoder'][lang]),
                 ('Rotary Poti',                'rotary_poti',                bindings, bricklet_descriptions['rotary_poti'][lang]),
                 #('Segment Display 4x7',        'segment_display_4x7',        bindings, bricklet_descriptions['segment_display_4x7'][lang]),
                 #('Sound Intensity',            'sound_intensity',            bindings, bricklet_descriptions['sound_intensity'][lang]),
                 ('Temperature',                'temperature',                bindings, bricklet_descriptions['temperature'][lang]),
                 ('Temperature IR',             'temperature_ir',             bindings, bricklet_descriptions['temperature_ir'][lang]),
                 #('Tilt',                      'tilt',                       bindings, bricklet_descriptions['tilt'][lang]),
                 ('Voltage',                    'voltage',                    bindings, bricklet_descriptions['voltage'][lang]),
                 ('Voltage/Current',            'voltage_current',            bindings, bricklet_descriptions['voltage_current'][lang]),
                 #('Water',                     'water',                       bindings, bricklet_descriptions['water'][lang]),
                ]

                  # display,              uri,       bindings, description
    extensions = [('Chibi Extension',    'chibi',    [],       extension_descriptions['chibi'][lang]),
                  ('Ethernet Extension', 'ethernet', [],       extension_descriptions['ethernet'][lang]),
                  ('RS485 Extension',    'rs485',    [],       extension_descriptions['rs485'][lang]),
                  ('WIFI Extension',     'wifi',     [],       extension_descriptions['wifi'][lang])]

                      # display,                  uri,         bindings, description
    power_supplies = [('Step-Down Power Supply', 'step_down',  [],       power_supply_descriptions['step_down'][lang])]

                    # display,          uri,               bindings, description
    accessories = [('DC Jack Adapter', 'dc_jack_adapter',  [],       accessories_descriptions['dc_jack_adapter'][lang])]

def get_body(url):
    try:
        response = urllib2.urlopen(url)
        data = response.read().replace('<hr>', '').replace('<br>', '')
        response.close()
        tree = etreefromstring(data)
        return tree.find('body')
    except Exception as e:
        print 'Could not download {0}: {1}'.format(url, e)
        return None

def get_tool_versions(url, regex):
    print 'Discovering ' + url
    body = get_body(url)
    versions = []

    if body is None:
        return versions

    for a in body.getiterator('a'):
        if 'href' not in a.attrib:
            continue

        url_part = a.attrib['href'].replace('/', '')

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

    if body is None:
        return versions

    for a in body.getiterator('a'):
        if 'href' not in a.attrib:
            continue

        url_part = a.attrib['href'].replace('/', '')

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

    if body is None:
        return versions

    if body != None:
        for a in body.getiterator('a'):
            if 'href' not in a.attrib:
                continue

            url_part = a.attrib['href'].replace('/', '')

            if url_part == '..':
                continue

            m = re.match(prefix + '_firmware_(\d+)_(\d+)_(\d+)\.bin', url_part)

            if m is None:
                continue

            versions.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

        return sorted(versions)

    return []

def make_index_table_ipcon():
    table_head = """
.. container:: indextable

 .. csv-table::
  :widths: 30, 60
  :delim: |

"""
    row_head = '  * :ref:`IP Connection <api_bindings_ip_connection>` | '
    row_cell_ipcon = ':ref:`{0} <ipcon_{1}>`'
    row_cell_llproto = ':ref:`{0} <llproto_{1}>`'
    cells = []

    for binding in bindings:
        if binding[2]:
            cells.append(row_cell_ipcon.format(binding[0], binding[1]))
        else:
            cells.append(row_cell_llproto.format(binding[0], binding[1]))

    return table_head + row_head + ', '.join(cells) + '\n'

def make_product_overview_table(devices, category, add_category_to_name=True):
    table_head = product_overview_table_head[lang]

    if add_category_to_name:
        row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}"'
        row_cell = '":ref:`{0} <{1}_' + category + '_{2}>`"'
    else:
        row_head = '   ":ref:`{0} <{1}>`", "{2}"'
        row_cell = '":ref:`{0} <{1}_{2}>`"'

    rows = []

    for device in devices:
        rows.append(row_head.format(device[0], device[1], device[3]))

    return table_head + '\n'.join(rows) + '\n'

def make_download_tools_table():
    source_code = download_tools_source_code[lang]
    table_head = download_tools_table_head[lang]
    row_multi_cell = ' :ref:`{0} <{1}>` | {3}.{4}.{5} - Linux (`amd64 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{3}.{4}.{5}_amd64.deb>`__, `i386 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{3}.{4}.{5}_i386.deb>`__, `armhf <http://download.tinkerforge.com/tools/{1}/linux/{1}-{3}.{4}.{5}_armhf.deb>`__), `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{3}_{4}_{5}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{3}_{4}_{5}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{3}.{4}.{5}.zip>`__ | `Changelog <https://raw.github.com/Tinkerforge/{1}/master/changelog>`__'
    row_all_cell = ' :ref:`{0} <{1}>` | {3}.{4}.{5} - `Linux <http://download.tinkerforge.com/tools/{1}/linux/{1}-{3}.{4}.{5}_all.deb>`__, `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{3}_{4}_{5}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{3}_{4}_{5}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{3}.{4}.{5}.zip>`__ | `Changelog <https://raw.github.com/Tinkerforge/{1}/master/changelog>`__'
    rows = []

    for tool in tools:
        if tool[1] == 'brickd':
            row_cell = row_multi_cell
            linux_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/linux/'.format(tool[1]), '{0}-(\d+).(\d+).(\d+)_amd64.deb'.format(tool[1]))
        else:
            row_cell = row_all_cell
            linux_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/linux/'.format(tool[1]), '{0}-(\d+).(\d+).(\d+)_all.deb'.format(tool[1]))
        macos_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/macos/'.format(tool[1]), '{0}_macos_(\d+)_(\d+)_(\d+).dmg'.format(tool[1]))
        windows_versions = get_tool_versions('http://download.tinkerforge.com/tools/{0}/windows/'.format(tool[1]), '{0}_windows_(\d+)_(\d+)_(\d+).exe'.format(tool[1]))

        if len(linux_versions) == 0:
            raise RuntimeError('Could not find Linux versions of {0}'.format(tool[0]))

        if len(macos_versions) == 0:
            raise RuntimeError('Could not find Mac OS X versions of {0}'.format(tool[0]))

        if len(windows_versions) == 0:
            raise RuntimeError('Could not find Windows versions of {0}'.format(tool[0]))

        if len(set([linux_versions[-1], macos_versions[-1], windows_versions[-1]])) != 1:
            raise RuntimeError('Cross-platform version mismatch for {0}'.format(tool[0]))

        rows.append(row_cell.format(tool[0], tool[1], source_code, *linux_versions[-1]))

    return table_head + '\n'.join(rows) + '\n'

def make_download_bindings_table():
    table_head = download_bindings_table_head[lang]
    row_cell = ' {0} | `{2}.{3}.{4} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_{2}_{3}_{4}.zip>`__ | `Changelog <https://raw.github.com/Tinkerforge/generators/master/{1}/changelog.txt>`__'
    rows = []

    for binding in bindings:
        if binding[2]:
            versions = get_bindings_versions('http://download.tinkerforge.com/bindings/{0}/'.format(binding[1]), binding[1])

            if len(versions) == 0:
                print('Could not find versions of the {0} bindings'.format(binding[0]))
            else:
                rows.append(row_cell.format(binding[0], binding[1], *versions[-1]))

    return table_head + '\n'.join(rows) + '\n'

def make_download_firmwares_table():
    table_head = download_firmwares_table_head[lang]
    brick_row_cell = ' :ref:`{0} <{1}_brick>` | `{3}.{4}.{5} <http://download.tinkerforge.com/firmwares/bricks/{1}/brick_{1}_firmware_{3}_{4}_{5}.bin>`__ | `Changelog <https://raw.github.com/Tinkerforge/{2}-brick/master/software/changelog>`__'
    bricklet_row_cell = ' :ref:`{0} <{1}_bricklet>` | `{4}.{5}.{6} <http://download.tinkerforge.com/firmwares/bricklets/{3}/bricklet_{3}_firmware_{4}_{5}_{6}.bin>`__ | `Changelog <https://raw.github.com/Tinkerforge/{2}-bricklet/master/software/changelog>`__'
    brick_rows = []
    bricklet_rows = []

    for brick in bricks:
        if len(brick[2]) > 0:
            versions = get_firmware_versions('http://download.tinkerforge.com/firmwares/bricks/{0}/'.format(brick[1]), 'brick_' + brick[1])

            if len(versions) < 1:
                print('Could not find versions of the {0} Brick firmware'.format(brick[0]))
            else:
                brick_rows.append(brick_row_cell.format(brick[0], brick[1], brick[1].replace('_', '-').replace('/', '-'), *versions[-1]))

    def handle_bricklet(name, common_url_part, plugin_url_part):
        versions = get_firmware_versions('http://download.tinkerforge.com/firmwares/bricklets/{0}/'.format(plugin_url_part), 'bricklet_' + plugin_url_part)

        if len(versions) < 1:
            print('Could not find versions of the {0} Bricklet firmware'.format(name))
        else:
            bricklet_rows.append(bricklet_row_cell.format(name, common_url_part, common_url_part.replace('_', '-').replace('/', '-'), plugin_url_part, *versions[-1]))

    for bricklet in bricklets:
        if len(bricklet[2]) > 0:
            if bricklet[1] == 'lcd_20x4':
                handle_bricklet(bricklet[0] + ' 1.1', bricklet[1], bricklet[1] + '_v11')
                handle_bricklet(bricklet[0] + ' 1.2', bricklet[1], bricklet[1] + '_v12')
            else:
                handle_bricklet(bricklet[0], bricklet[1], bricklet[1])

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows)) + '\n'

def make_api_bindings_table():
    row = '* :ref:`{0} <ipcon_{1}>`'
    rows = []

    for binding in bindings:
        if binding[2]:
            rows.append(row.format(binding[0], binding[1]))

    return '\n'.join(rows) + '\n'

def make_source_code_gits_table():
    table_head = source_code_gits_table_head[lang]
    brick_row_cell = source_code_gits_brick_row_cell[lang]
    bricklet_row_cell = source_code_gits_bricklet_row_cell[lang]
    extension_row_cell = source_code_gits_extension_row_cell[lang]
    brick_rows = []
    bricklet_rows = []
    extension_rows = []

    for brick in bricks:
        brick_rows.append(brick_row_cell.format(brick[0], brick[1].replace('_', '-').replace('/', '-')))

    for bricklet in bricklets:
        bricklet_rows.append(bricklet_row_cell.format(bricklet[0], bricklet[1].replace('_', '-').replace('/', '-')))

    for extension in extensions:
        extension_rows.append(extension_row_cell.format(extension[0], extension[1].replace('_', '-').replace('/', '-')))

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows), '\n'.join(extension_rows)) + '\n'

def make_index_table_block(devices, category, add_category_to_name=True):
    if add_category_to_name:
        row_head = ' :ref:`{0} <{1}_' + category + '>` | '
        row_cell = ' :ref:`{0} <{1}_' + category + '_{2}>`'
    else:
        row_head = ' :ref:`{0} <{1}>` | '
        row_cell = ' :ref:`{0} <{1}_{2}>`'

    rows = []

    for device in devices:
        cells = []

        for binding in device[2]:
            cells.append(row_cell.format(binding[0], device[1], binding[1]))

        row = row_head.format(device[0], device[1]) + ', '.join(cells)
        rows.append(row)

    return '\n'.join(rows)

def make_index_table():
    return index_table_head[lang].format(make_index_table_block(bricks, 'brick'),
                                         make_index_table_block(bricklets, 'bricklet'),
                                         make_index_table_block(extensions, 'extension'),
                                         make_index_table_block(power_supplies, 'power_supply'),
                                         make_index_table_block(accessories, 'accessory', False))

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

hlpi_row = {
'en': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"',
'de': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"'
}

def make_hlpi_table(device, category):
    table_head = hlpi_table_head[lang]
    row_source = hlpi_row_source[lang]
    row = hlpi_row[lang]
    rows = []

    for binding in device[2]:
        if binding[2]:
            rows.append(row_source.format(binding[0], device[1], category, binding[1]))
        else:
            rows.append(row.format(binding[0], device[1], category, binding[1]))

    return table_head + '\n'.join(rows) + '\n'

device_identifier_table_head = {
'en':
"""
.. csv-table::
   :header: "Device Identifier", "Device Name"
   :widths: 30, 100

""",
'de':
"""
.. csv-table::
   :header: "Device Identifier", "Device Name"
   :widths: 30, 100

"""
}

device_identifier_row = {
'en': '   "{0}", "{1}"',
'de': '   "{0}", "{1}"'
}

def make_device_identifier_table():
    table_head = device_identifier_table_head[lang]
    row = device_identifier_row[lang]
    rows = []

    for device_identifier in device_identifiers:
        rows.append(row.format(device_identifier[0], device_identifier[1]))

    return table_head + '\n'.join(rows) + '\n'

def write_if_changed(path, content):
    if os.path.exists(path):
        f = open(path, 'rb')
        existing = f.read()
        f.close()
        if existing == content:
            return

    f = open(path, 'wb')
    f.write(content)
    f.close()

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        print('Wrong working directory')
        sys.exit(1)

    fill_dicts()

    print('Generating index_links.table')
    write_if_changed(os.path.join(path, 'source', 'index_links.table'), make_index_table())

    print('Generating Product_Overview_bricks.table')
    write_if_changed(os.path.join(path, 'source', 'Product_Overview_bricks.table'), make_product_overview_table(bricks, 'brick'))

    print('Generating Product_Overview_bricklets.table')
    write_if_changed(os.path.join(path, 'source', 'Product_Overview_bricklets.table'), make_product_overview_table(bricklets, 'bricklet'))

    print('Generating Product_Overview_extensions.table')
    write_if_changed(os.path.join(path, 'source', 'Product_Overview_extensions.table'), make_product_overview_table(extensions, 'extension'))

    print('Generating Product_Overview_power_supplies.table')
    write_if_changed(os.path.join(path, 'source', 'Product_Overview_power_supplies.table'), make_product_overview_table(power_supplies, 'power_supply'))

    print('Generating Product_Overview_accessories.table')
    write_if_changed(os.path.join(path, 'source', 'Product_Overview_accessories.table'), make_product_overview_table(accessories, 'accessory', False))

    print('Generating Downloads_tools.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_tools.table'), make_download_tools_table())

    print('Generating Downloads_bindings.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_bindings.table'), make_download_bindings_table())

    print('Generating Downloads_firmwares.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_firmwares.table'), make_download_firmwares_table())

    print('Generating API_Bindings_bindings.table')
    write_if_changed(os.path.join(path, 'source', 'Software', 'API_Bindings_bindings.table'), make_api_bindings_table())

    print('Generating Source_Code_gits.table')
    write_if_changed(os.path.join(path, 'source', 'Source_Code_gits.table'), make_source_code_gits_table())

    for brick in bricks:
        if len(brick[2]) == 0:
            continue

        name = brick[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print('Generating {0}_Brick_hlpi.table'.format(name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick_hlpi.table'), make_hlpi_table(brick, 'brick'))

    for bricklet in bricklets:
        if len(bricklet[2]) == 0:
            continue

        name = bricklet[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print('Generating {0}_hlpi.table'.format(name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '_hlpi.table'), make_hlpi_table(bricklet, 'bricklet'))

    print('Generating Device_Identifier.table')
    write_if_changed(os.path.join(path, 'source', 'Software', 'Device_Identifier.table'), make_device_identifier_table())

if __name__ == "__main__":
    generate(os.getcwd())
