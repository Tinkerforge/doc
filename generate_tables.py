#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2
import math
from collections import namedtuple

sys.path.append(os.path.join(os.path.split(__file__)[0], '../generators'))
from device_infos import DeviceInfo, brick_infos, bricklet_infos

lang = 'en'

ToolInfo = namedtuple('ToolInfo', 'display_name url_part')

tool_infos = \
[
    ToolInfo('Brick Daemon', 'brickd'),
    ToolInfo('Brick Viewer', 'brickv'),
    ToolInfo('Brick Logger', 'brick_logger')
]

BindingsInfo = namedtuple('BindingsInfo', 'display_name url_part software_doc_suffix is_programming_language is_released has_authentication_example has_download misc_docs tutorial')

bindings_infos = \
[
    BindingsInfo(display_name='C/C++',
                 url_part='c',
                 software_doc_suffix='C',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'}),
                     ('API_Bindings_{suffix}_iOS', {'en': 'Usage (iOS)', 'de': 'Benutzung (iOS)'})
                 ],
                 tutorial={'en': 'https://www.cprogramming.com/',
                           'de': 'https://www.cprogramming.com/'}), # http://www.c-howto.de/
    BindingsInfo(display_name='C#',
                 url_part='csharp',
                 software_doc_suffix='CSharp',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'}),
                     ('API_Bindings_{suffix}_Windows_Phone', {'en': 'Usage (Windows Phone)', 'de': 'Benutzung (Win Phone)'})
                 ],
                 tutorial={'en': 'https://csharp.net-tutorials.com/',
                           'de': 'https://csharp.net-tutorials.com/'}),
    BindingsInfo(display_name='Delphi/Lazarus',
                 url_part='delphi',
                 software_doc_suffix='Delphi',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'http://www.delphibasics.co.uk/',
                           'de': 'https://www.delphi-treff.de/tutorials/grundlagen-tutorials/'}),
    BindingsInfo(display_name='Go',
                 url_part='go',
                 software_doc_suffix='Go',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'https://tour.golang.org',
                           'de': 'https://tour.golang.org'}),
    BindingsInfo(display_name='Java',
                 url_part='java',
                 software_doc_suffix='Java',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'}),
                     ('API_Bindings_{suffix}_Android', {'en': 'Usage (Android)', 'de': 'Benutzung (Android)'})
                 ],
                 tutorial={'en': 'https://docs.oracle.com/javase/tutorial/',
                           'de': 'https://docs.oracle.com/javase/tutorial/'}), # http://openbook.galileocomputing.de/javainsel/
    BindingsInfo(display_name='JavaScript',
                 url_part='javascript',
                 software_doc_suffix='JavaScript',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='LabVIEW',
                 url_part='labview',
                 software_doc_suffix='LabVIEW',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='Mathematica',
                 url_part='mathematica',
                 software_doc_suffix='Mathematica',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='MATLAB/Octave',
                 url_part='matlab',
                 software_doc_suffix='MATLAB',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='MQTT',
                 url_part='mqtt',
                 software_doc_suffix='MQTT',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='openHAB',
                 url_part='openhab',
                 software_doc_suffix='openHAB',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=False,
                 has_download=False, # FIXME
                 misc_docs=[
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='Perl',
                 url_part='perl',
                 software_doc_suffix='Perl',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='PHP',
                 url_part='php',
                 software_doc_suffix='PHP',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'https://www.php.net/manual/en/getting-started.php',
                           'de': 'https://www.php.net/manual/de/getting-started.php'}),
    BindingsInfo(display_name='Python',
                 url_part='python',
                 software_doc_suffix='Python',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'https://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
                           'de': 'https://www.python.org/about/gettingstarted/'}),
    BindingsInfo(display_name='Ruby',
                 url_part='ruby',
                 software_doc_suffix='Ruby',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'https://www.ruby-lang.org/en/documentation/quickstart/',
                           'de': 'https://www.ruby-lang.org/de/documentation/quickstart/'}),
    BindingsInfo(display_name='Rust',
                 url_part='rust',
                 software_doc_suffix='Rust',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'https://doc.rust-lang.org/tutorial.html',
                           'de': 'https://doc.rust-lang.org/tutorial.html'}),
    BindingsInfo(display_name='Shell',
                 url_part='shell',
                 software_doc_suffix='Shell',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    #BindingsInfo(display_name='Tinkerforge Visual Programming Language (TVPL)',
    #             url_part='tvpl',
    #             software_doc_suffix='TVPL',
    #             is_programming_language=True,
    #             is_released=False,
    #             has_authentication_example=False,
    #             has_download=True,
    #             misc_docs=[
    #                 ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
    #                 ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
    #             ],
    #             tutorial={'en': 'FIXME',
    #                       'de': 'FIXME'}),
    BindingsInfo(display_name='Visual Basic .NET',
                 url_part='vbnet',
                 software_doc_suffix='VBNET',
                 is_programming_language=True,
                 is_released=True,
                 has_authentication_example=True,
                 has_download=True,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'http://howtostartprogramming.com/vb-net/',
                           'de': 'http://howtostartprogramming.com/vb-net/'}), # http://openbook.galileocomputing.de/vb_net/index.htm
    BindingsInfo(display_name='TCP/IP',
                 url_part='tcpip',
                 software_doc_suffix='TCPIP',
                 is_programming_language=False,
                 is_released=True,
                 has_authentication_example=False,
                 has_download=False,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
    BindingsInfo(display_name='Modbus',
                 url_part='modbus',
                 software_doc_suffix='Modbus',
                 is_programming_language=False,
                 is_released=True,
                 has_authentication_example=False,
                 has_download=False,
                 misc_docs=[
                     ('IPConnection_{suffix}', {'en': 'IP Connection', 'de': 'IP Connection'}),
                     ('API_Bindings_{suffix}', {'en': 'Usage', 'de': 'Benutzung'})
                 ],
                 tutorial={'en': 'FIXME',
                           'de': 'FIXME'}),
]

extension_infos = \
[
    DeviceInfo(None, 'Chibi Extension', 'Chibi', 'chibi_extension', 'Chibi_Extension', None, 'chibi-extension', None, False, True, True, True, False,
               {'en': 'Wireless Chibi connection between stacks',
                'de': 'Drahtlose Chibi Verbindung zwischen Stapeln'}),
    DeviceInfo(None, 'Ethernet Extension', 'Ethernet', 'ethernet_extension', 'Ethernet_Extension', None, 'ethernet-extension', None, False, True, True, False, False,
               {'en': 'Cable based Ethernet connection between stack and PC',
                'de': 'Kabelgebundene Ethernet Verbindung zwischen Stapel und PC'}),
    DeviceInfo(None, 'RS485 Extension', 'RS485', 'rs485_extension', 'RS485_Extension', None, 'rs485-extension', None, False, True, True, False, False,
               {'en': 'Cable based RS485 connection between stacks',
                'de': 'Kabelgebundene RS485 Verbindung zwischen Stapeln'}),
    DeviceInfo(None, 'WIFI Extension', 'WIFI', 'wifi_extension', 'WIFI_Extension', None, 'wifi-extension', None, False, True, True, False, False,
               {'en': 'Wireless Wi-Fi connection between stack and PC',
                'de': 'Drahtlose WLAN Verbindung zwischen Stapel und PC'}),
    DeviceInfo(None, 'WIFI Extension 2.0', 'WIFI 2.0', 'wifi_v2_extension', 'WIFI_V2_Extension', None, 'wifi-v2-extension', 'wifi_v2', False, True, True, False, False,
               {'en': 'Wireless Wi-Fi connection between stack and PC',
                'de': 'Drahtlose WLAN Verbindung zwischen Stapel und PC'})
]

power_supply_infos = \
[
    DeviceInfo(None, 'Step-Down Power Supply', 'Step-Down', 'step_down_power_supply', 'Step_Down', None, 'step-down-powersupply', None, False, True, True, False, False,
               {'en': 'Powers a stack of Bricks with 5V',
                'de': 'Versorgt einen Stapel von Bricks mit 5V'})
]

accessory_infos = \
[
    DeviceInfo(None, 'DC Jack Adapter', 'DC Jack Adapter', 'dc_jack_adapter', 'DC_Jack_Adapter', None, 'dc-adapter', None, False, True, True, False, False,
               {'en': 'Adapter between a 5mm DC jack and 2 Pole Black Connector',
                'de': 'Adapter zwischen einem 5mm DC Stecker und 2 Pin Stecker Schwarz'})
]

KitInfo = namedtuple('KitInfo', 'display_name url_part prefix released')

kit_infos = \
[
    KitInfo({'en': 'Starter Kit: Blinkenlights', 'de': 'Starterkit: Blinkenlights'}, 'blinkenlights', 'starter_kit_', True),
    KitInfo({'en': 'Starter Kit: Camera Slider', 'de': 'Starterkit: Kameraschlitten'}, 'camera_slider', 'starter_kit_', True),
    KitInfo({'en': 'Tabletop Weather Station', 'de': 'Tisch-Wetterstation'}, 'tabletop_weather_station', '', True),
    KitInfo({'en': 'Starter Kit: Weather Station', 'de': 'Starterkit: Wetterstation'}, 'weather_station', 'starter_kit_', True)
]

LATEST_VERSIONS_URL = 'https://download.tinkerforge.com/latest_versions.txt'

tool_versions = {}
bindings_versions = {}
firmware_versions = {}
plugin_versions = {}
extension_versions = {}
kit_versions = {}
red_image_versions = {}

def get_latest_version_info():
    print 'Discovering latest versions on tinkerforge.com'

    try:
        response = urllib2.urlopen(LATEST_VERSIONS_URL)
        latest_versions_data = response.read()
    except urllib2.URLError:
        raise Exception('Latest version information on tinkerforge.com is not available (error code 1)')

    for line in latest_versions_data.split('\n'):
        line = line.strip()

        if len(line) < 1:
            continue

        parts = line.split(':')

        if len(parts) != 3:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 2)')

        latest_version_parts = parts[2].split('.')

        if len(latest_version_parts) != 3:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 3)')

        try:
            latest_version = int(latest_version_parts[0]), int(latest_version_parts[1]), int(latest_version_parts[2])
        except:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 4)')

        if parts[0] == 'tools':
            tool_versions[parts[1]] = latest_version
        elif parts[0] == 'bindings':
            bindings_versions[parts[1]] = latest_version
        elif parts[0] == 'bricks':
            firmware_versions[parts[1]] = latest_version
        elif parts[0] == 'bricklets':
            plugin_versions[parts[1]] = latest_version
        elif parts[0] == 'extensions':
            extension_versions[parts[1]] = latest_version
        elif parts[0] == 'kits':
            kit_versions[parts[1]] = latest_version
        elif parts[0] == 'red_images':
            red_image_versions[parts[1]] = latest_version

def make_primer_table(device_infos):
    table_head = {
    'en': """
.. csv-table::
   :header: "Name", "Description"
   :widths: 25, 75

""",
    'de': """
.. csv-table::
   :header: "Name", "Beschreibung"
   :widths: 25, 75

"""
}
    row = '   ":ref:`{0} <{1}>`", "{2}"'
    rows = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and not device_info.is_discontinued:
            rows.append(row.format(device_info.short_display_name, device_info.ref_name, device_info.description[lang].replace('"', "inch")))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_discontinued_products_table():
    table_head = {
    'en': """
.. csv-table::
 :header: "Name", "Description"
 :delim: |
 :widths: 25, 75

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
 |
 **Master Extensions** |
{2}
""",
# FIXME
#"""
# |
# **Power Supplies** |
#{3}
# |
# **Accessories** |
#{4}
#"""
    'de': """
.. csv-table::
 :header: "Name", "Beschreibung"
 :delim: |
 :widths: 25, 75

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
 |
 **Master Extensions** |
{2}
"""
# FIXME
#"""
# |
# **Stromversorgungen** |
#{3}
# |
# **Zubehör** |
#{4}
#"""
    }
    row = ' :ref:`{0} <{1}>` | {2}'
    brick_rows = []
    bricklet_rows = []
    extension_rows = []
    power_supply_rows = []
    accessory_rows = []

    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.is_documented and brick_info.is_discontinued:
            brick_rows.append(row.format(brick_info.short_display_name, brick_info.ref_name, brick_info.description[lang].replace('"', "inch")))

    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_documented and bricklet_info.is_discontinued:
            bricklet_rows.append(row.format(bricklet_info.short_display_name, bricklet_info.ref_name, bricklet_info.description[lang].replace('"', "inch")))

    for extension_info in sorted(extension_infos, key=lambda x: x.short_display_name.lower()):
        if extension_info.is_documented and extension_info.is_discontinued:
            extension_rows.append(row.format(extension_info.short_display_name, extension_info.ref_name, extension_info.description[lang].replace('"', "inch")))

    for power_supply_info in sorted(power_supply_infos, key=lambda x: x.short_display_name.lower()):
        if power_supply_info.is_documented and power_supply_info.is_discontinued:
            power_supply_rows.append(row.format(power_supply_info.short_display_name, power_supply_info.ref_name, power_supply_info.description[lang].replace('"', "inch")))

    for accessory_info in sorted(accessory_infos, key=lambda x: x.short_display_name.lower()):
        if accessory_info.is_documented and accessory_info.is_discontinued:
            accessory_rows.append(row.format(accessory_info.short_display_name, accessory_info.ref_name, accessory_info.description[lang].replace('"', "inch")))

    return table_head[lang].format('\n'.join(brick_rows),
                                   '\n'.join(bricklet_rows),
                                   '\n'.join(extension_rows),
                                   '\n'.join(power_supply_rows),
                                   '\n'.join(accessory_rows))

def make_download_tools_table():
    source_code = {
    'en': 'Source Code',
    'de': 'Quelltext'
    }

    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Tool", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Tool", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row_brickd = ' :ref:`{0} <{1}>` | Linux (`amd64 <https://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_amd64.deb>`__, `i386 <https://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_i386.deb>`__, `armhf <https://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_armhf.deb>`__, `RED Brick <https://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}+redbrick_armhf.deb>`__), `macOS <https://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <https://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <https://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/src/changelog>`__'
    row_brick_logger = ' :ref:`{0} <{1}>` | `Linux, macOS, Windows <https://download.tinkerforge.com/tools/{1}/{1}_{4}_{5}_{6}.zip>`__, `RED Brick <https://download.tinkerforge.com/tools/{1}/{1}_{4}_{5}_{6}.tfrba>`__, `{2} <https://github.com/Tinkerforge/brickv/archive/brick-logger-{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <https://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/brickv/master/src/changelog.brick-logger>`__'
    row_other = ' :ref:`{0} <{1}>` | `Linux <https://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_all.deb>`__, `macOS <https://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <https://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <https://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/src/changelog>`__'
    rows = []

    for tool_info in tool_infos:
        if tool_info.url_part == 'brickd':
            row = row_brickd
        elif tool_info.url_part == 'brick_logger':
            row = row_brick_logger
        else:
            row = row_other

        rows.append(row.format(tool_info.display_name,
                               tool_info.url_part,
                               source_code[lang],
                               archive[lang],
                               *tool_versions[tool_info.url_part]))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_bindings_table():
    bindings_and_examples = {
    'en': 'Bindings and Examples',
    'de': 'Bindings und Beispiele'
    }

    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Language", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Sprache", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' :ref:`{0} <api_bindings_{1}>` | `{3} <https://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_{4}_{5}_{6}.zip>`__ | {4}.{5}.{6} | `{2} <https://download.tinkerforge.com/bindings/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/generators/master/{1}/changelog.txt>`__'
    rows = []

    for bindings_info in bindings_infos:
        if not bindings_info.is_released or not bindings_info.has_download:
            continue

        rows.append(row.format(bindings_info.display_name,
                               bindings_info.url_part,
                               archive[lang],
                               bindings_and_examples[lang],
                               *(bindings_versions[bindings_info.url_part] if bindings_info.display_name != 'openHAB' else (2, 0 ,0))))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_red_images_table():
    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Type", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Typ", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' RED Brick Image | `Image <https://download.tinkerforge.com/red_images/{0}/red_image_{2}_{3}_{0}.img.7z>`__ | {2}.{3} | `{1} <https://download.tinkerforge.com/red_images/{0}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/red-brick/master/image/changelog_{0}>`__'
    rows = []

    for image in ['full']:
        rows.append(row.format(image,
                               archive[lang],
                               *red_image_versions[image]))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_brick_firmwares_table():
    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    source_code = {
    'en': 'Source Code',
    'de': 'Quelltext'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Brick", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Brick", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' :ref:`{0} <{1}>` | `Firmware <https://download.tinkerforge.com/firmwares/{6}s/{2}/{6}_{2}_firmware_{8}_{9}_{10}.{7}>`__, `{3} <https://github.com/Tinkerforge/{4}/archive/v{8}.{9}.{10}.zip>`__ | {8}.{9}.{10} | `{5} <https://download.tinkerforge.com/firmwares/{6}s/{2}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{4}/master/software/changelog>`__'
    rows = []

    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.firmware_url_part != None and brick_info.is_documented:
            if brick_info.firmware_url_part in ['hat', 'hat_zero']:
                firmware_version = plugin_versions.get(brick_info.firmware_url_part, (0,0,0))
                category = 'bricklet'
                extension = 'zbin'
            else:
                firmware_version = firmware_versions.get(brick_info.firmware_url_part, (0,0,0))
                category = 'brick'
                extension = 'bin'

            rows.append(row.format(brick_info.short_display_name,
                                   brick_info.ref_name,
                                   brick_info.firmware_url_part,
                                   source_code[lang],
                                   brick_info.git_name,
                                   archive[lang],
                                   category,
                                   extension,
                                   *firmware_version))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_bricklet_plugins_table():
    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    source_code = {
    'en': 'Source Code',
    'de': 'Quelltext'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Bricklet", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Bricklet", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' :ref:`{0} <{1}>` | `Plugin <https://download.tinkerforge.com/firmwares/bricklets/{2}/bricklet_{2}_firmware_{7}_{8}_{9}.{6}>`__, `{3} <https://github.com/Tinkerforge/{4}/archive/v{7}.{8}.{9}.zip>`__ | {7}.{8}.{9} | `{5} <https://download.tinkerforge.com/firmwares/bricklets/{2}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{4}/master/software/changelog>`__'
    rows = []

    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.firmware_url_part != None and bricklet_info.is_documented:
            subversion = []

            if bricklet_info.firmware_url_part == 'lcd_20x4':
                subversion.append((bricklet_info.short_display_name + ' 1.1', bricklet_info.firmware_url_part + '_v11'))
                subversion.append((bricklet_info.short_display_name + ' 1.2', bricklet_info.firmware_url_part + '_v12'))
            else:
                subversion.append((bricklet_info.short_display_name, bricklet_info.firmware_url_part))

            for short_display_name, firmware_url_part in subversion:
                plugin_version = plugin_versions.get(firmware_url_part, (0,0,0))

                rows.append(row.format(short_display_name,
                                       bricklet_info.ref_name,
                                       firmware_url_part,
                                       source_code[lang],
                                       bricklet_info.git_name,
                                       archive[lang],
                                       'zbin' if bricklet_info.has_comcu else 'bin',
                                       *plugin_version))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_extension_firmwares_table():
    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    source_code = {
    'en': 'Source Code',
    'de': 'Quelltext'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Brick", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Brick", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' :ref:`{0} <{1}>` | `Firmware <https://download.tinkerforge.com/firmwares/extensions/{2}/extension_{2}_firmware_{6}_{7}_{8}.zbin>`__, `{3} <https://github.com/Tinkerforge/{4}/archive/v{6}.{7}.{8}.zip>`__ | {6}.{7}.{8} | `{5} <https://download.tinkerforge.com/firmwares/extensions/{2}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{4}/master/software/changelog>`__'
    rows = []

    for extension_info in sorted(extension_infos, key=lambda x: x.short_display_name.lower()):
        if extension_info.firmware_url_part != None and extension_info.is_documented:
            extension_version = extension_versions.get(extension_info.firmware_url_part, (0,0,0))

            rows.append(row.format(extension_info.short_display_name,
                                   extension_info.ref_name,
                                   extension_info.firmware_url_part,
                                   source_code[lang],
                                   extension_info.git_name,
                                   archive[lang],
                                   *extension_version))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_kits_table():
    source_code = {
    'en': 'Source Code',
    'de': 'Quelltext'
    }

    archive = {
    'en': 'Archive',
    'de': 'Archiv'
    }

    table_head = {
    'en': """.. csv-table::
 :header: "Kit", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

""",
    'de': """.. csv-table::
 :header: "Kit", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 25, 50, 7, 7, 10

"""
    }

    row = ' :ref:`{0} <{5}{1}>` | `Linux <https://download.tinkerforge.com/kits/{1}/linux/{6}{2}-demo-{7}.{8}.{9}_all.deb>`__, `macOS <https://download.tinkerforge.com/kits/{1}/macos/{5}{1}_demo_macos_{7}_{8}_{9}.dmg>`__, `Windows <https://download.tinkerforge.com/kits/{1}/windows/{5}{1}_demo_windows_{7}_{8}_{9}.exe>`__, `{3} <https://github.com/Tinkerforge/{2}/archive/demo-{7}.{8}.{9}.zip>`__ | {7}.{8}.{9} | `{4} <https://download.tinkerforge.com/kits/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{2}/master/demo/changelog>`__'
    rows = []

    for kit_info in kit_infos:
        if not kit_info.released:
            continue

        rows.append(row.format(kit_info.display_name[lang],
                               kit_info.url_part,
                               kit_info.url_part.replace('_', '-'),
                               source_code[lang],
                               archive[lang],
                               kit_info.prefix,
                               kit_info.prefix.replace('_', '-'),
                               *kit_versions[kit_info.url_part]))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_api_bindings_links_table(bindings_info):
    table_head = {
    'en': """.. csv-table::
 :header: "Name", "API", "Examples"
 :delim: |
 :widths: 20, 10, 10

{0}
 **Bricks** | |
{1}
 | |
 **Bricks (Discontinued)** | |
{2}
 | |
 **Bricklets** | |
{3}
 | |
 **Bricklets (Discontinued)** | |
{4}
""",
    'de': """.. csv-table::
 :header: "", "API", "Beispiele"
 :delim: |
 :widths: 20, 10, 10

{0}
 | |
 **Bricks** | |
{1}
 | |
 **Bricks (Abgekündigt)** | |
{2}
 | |
 **Bricklets** | |
{3}
 | |
 **Bricklets (Abgekündigt)** | |
{4}
"""
    }

    ipcon_row = {
    'en': ' IP Connection | :ref:`API <ipcon_{0}_api>` | :ref:`Examples <ipcon_{0}_examples>`',
    'de': ' IP Connection | :ref:`API <ipcon_{0}_api>` | :ref:`Beispiele <ipcon_{0}_examples>`'
    }

    device_row = {
    'en': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Examples <{0}_{1}_examples>`',
    'de': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Beispiele <{0}_{1}_examples>`'
    }

    brick_lines = [[], []]
    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        line = device_row[lang].format(brick_info.ref_name, bindings_info.url_part, brick_info.short_display_name)

        if brick_info.is_documented and brick_info.has_bindings:
            if not brick_info.is_discontinued:
                brick_lines[0].append(line)
            else:
                brick_lines[1].append(line)

    bricklet_lines = [[], []]
    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        line = device_row[lang].format(bricklet_info.ref_name, bindings_info.url_part, bricklet_info.short_display_name)

        if bricklet_info.is_documented and bricklet_info.has_bindings:
            if not bricklet_info.is_discontinued:
                bricklet_lines[0].append(line)
            else:
                bricklet_lines[1].append(line)

    has_ipcon = False

    for misc_doc in bindings_info.misc_docs:
        if misc_doc[0].startswith('IPConnection'):
            has_ipcon = True
            break

    if has_ipcon:
        ipcon = ipcon_row[lang].format(bindings_info.url_part) + '\n | |'
    else:
        ipcon = ''

    return table_head[lang].format(ipcon,
                                   '\n'.join(brick_lines[0]),
                                   '\n'.join(brick_lines[1]),
                                   '\n'.join(bricklet_lines[0]),
                                   '\n'.join(bricklet_lines[1]))

def make_llproto_links_table(bindings_info):
    table_head = {
    'en': """.. csv-table::
 :header: "", "API"
 :delim: |
 :widths: 20, 20

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
""",
    'de': """.. csv-table::
 :header: "", "API"
 :delim: |
 :widths: 20, 20

 **Bricks** |
{0}
 |
 **Bricklets** |
{1}
"""
    }

    device_row = {
    'en': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>`',
    'de': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>`'
    }

    brick_lines = []
    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.is_documented and brick_info.has_bindings:
            brick_lines.append(device_row[lang].format(brick_info.ref_name, bindings_info.url_part, brick_info.short_display_name))

    bricklet_lines = []
    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_documented and bricklet_info.has_bindings:
            bricklet_lines.append(device_row[lang].format(bricklet_info.ref_name, bindings_info.url_part, bricklet_info.short_display_name))

    return table_head[lang].format('\n'.join(brick_lines),
                                   '\n'.join(bricklet_lines))

def make_api_bindings_devices_table(bindings_info, device_infos, category, discontinued):
    table_head = {
    'en': """.. csv-table::
 :header: "{0}", "API", "Examples"
 :delim: |
 :widths: 20, 10, 10

{1}
""",
    'de': """.. csv-table::
 :header: "{0}", "API", "Beispiele"
 :delim: |
 :widths: 20, 10, 10

{1}
"""
    }

    device_row = {
    'en': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Examples <{0}_{1}_examples>`',
    'de': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Beispiele <{0}_{1}_examples>`'
    }

    lines = []
    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and device_info.has_bindings and device_info.is_discontinued == discontinued:
            lines.append(device_row[lang].format(device_info.ref_name, bindings_info.url_part, device_info.short_display_name))

    return table_head[lang].format(category, '\n'.join(lines))

def make_llproto_devices_table(bindings_info, device_infos, category, discontinued):
    table_head = {
    'en': """.. csv-table::
 :header: "{0}", "API"
 :delim: |
 :widths: 20, 20

{1}
""",
    'de': """.. csv-table::
 :header: "{0}", "API"
 :delim: |
 :widths: 20, 20

{1}
"""
    }

    device_row = {
    'en': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>`',
    'de': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>`'
    }

    lines = []
    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and device_info.has_bindings and device_info.is_discontinued == discontinued:
            lines.append(device_row[lang].format(device_info.ref_name, bindings_info.url_part, device_info.short_display_name))

    return table_head[lang].format(category, '\n'.join(lines))

def make_source_code_gits_table():
    table_head = {
    'en': """.. csv-table::
 :header: "Name", "Repository", "Bug Tracking"
 :delim: |
 :widths: 20, 23, 12

 **Tools** | |
 Brick Daemon | `brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Report Bug <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Report Bug <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Report Bug <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Report Bug <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Report Bug <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `generators.git <https://github.com/Tinkerforge/generators/>`__ | `Report Bug <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Report Bug <https://github.com/Tinkerforge/kicad-libraries/issues>`__
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
{3}
 | |
 **Accessories** | |
{4}

""",
    'de': """.. csv-table::
 :header: "", "Repository", "Bug Tracking"
 :delim: |
 :widths: 20, 23, 12

 **Tools** | |
 Brick Daemon | `brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Problem melden <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Problem melden <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Problem melden <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Problem melden <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Problem melden <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `generators.git <https://github.com/Tinkerforge/generators/>`__ | `Problem melden <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Problem melden <https://github.com/Tinkerforge/kicad-libraries/issues>`__
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
{3}
 | |
 **Zubehör** | |
{4}

"""
    }

    row = {
    'en': ' {0} | `{1}.git <https://github.com/Tinkerforge/{1}/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}/issues>`__',
    'de': ' {0} | `{1}.git <https://github.com/Tinkerforge/{1}/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}/issues>`__',
    }

    brick_rows = []
    bricklet_rows = []
    extension_rows = []
    power_supply_rows = []
    accessory_rows = []

    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.is_documented:
            brick_rows.append(row[lang].format(brick_info.short_display_name, brick_info.git_name))

    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_documented:
            bricklet_rows.append(row[lang].format(bricklet_info.short_display_name, bricklet_info.git_name))

    for extension_info in sorted(extension_infos, key=lambda x: x.short_display_name.lower()):
        if extension_info.is_documented:
            extension_rows.append(row[lang].format(extension_info.short_display_name, extension_info.git_name))

    for power_supply_info in sorted(power_supply_infos, key=lambda x: x.short_display_name.lower()):
        if power_supply_info.is_documented:
            power_supply_rows.append(row[lang].format(power_supply_info.short_display_name, power_supply_info.git_name))

    for accessory_info in sorted(accessory_infos, key=lambda x: x.short_display_name.lower()):
        if accessory_info.is_documented:
            accessory_rows.append(row[lang].format(accessory_info.short_display_name, accessory_info.git_name))

    return table_head[lang].format('\n'.join(brick_rows),
                                   '\n'.join(bricklet_rows),
                                   '\n'.join(extension_rows),
                                   '\n'.join(power_supply_rows),
                                   '\n'.join(accessory_rows))

def make_index_hardware_device(device_infos, category):
    hardware_li = """<li><a class="reference internal" href="Hardware/{1}/{2}.html">{0}</a></li>"""
    lis = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and not device_info.is_discontinued:
            lis.append(hardware_li.format(device_info.short_display_name, category, device_info.hardware_doc_name))

    if category == 'Bricklets':
        split = int(math.ceil(len(lis) / 3.0))
    else:
        split = 15

    ret = ''

    while len(lis) > 0:
        if category in ['Bricks', 'Bricklets']:
            ret += '\n<div class="category_content_inner">\n<ul>' +'\n'.join(lis[:split]) + '</ul>\n</div>'
        else:
            ret += '\n<ul>' +'\n'.join(lis[:split]) + '</ul>\n'

        lis = lis[split:]

    return ret

def make_index_hardware():
    index_html_en = """
<div class="category_hardware_outer">
    <div class="category_body">
        <div class="category_content">
            <h3>Bricks</h3>
            {0}
        </div>
        <div class="category_content">
            <h3>Bricklets</h3>
            {1}
        </div>
        <div class="category_content">
            <h3>Master Extensions</h3>
            {2}
            <h3>Power Supplies</h3>
            {3}
            <h3>Accesories</h3>
            {4}
        </div>
    </div>
</div>
<div style="clear: both;"></div>
"""

    index_html = {
    'en': index_html_en,
    'de': index_html_en.replace('Power Supplies', 'Stromversorgungen').replace('Accesories', 'Zubehör')
    }

    return index_html[lang].format(make_index_hardware_device(brick_infos, 'Bricks'),
                                   make_index_hardware_device(bricklet_infos, 'Bricklets'),
                                   make_index_hardware_device(extension_infos, 'Master_Extensions'),
                                   make_index_hardware_device(power_supply_infos, 'Power_Supplies'),
                                   make_index_hardware_device(accessory_infos, 'Accessories'))

def make_index_api_device(device_infos, category, language):
    li = '<li><a class="reference internal" href="Software/{1}/{2}_{3}.html">{0}</a></li>'
    lis = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and device_info.has_bindings and not device_info.is_discontinued:
            lis.append(li.format(device_info.short_display_name, category, device_info.software_doc_prefix, language))

    if category == 'Bricklets':
        split = int(math.ceil(len(lis) / 4.0))
    else:
        split = 15

    ret = ''
    while len(lis) > 0:
        if category == 'Bricklets':
            ret += '\n<div class="category_content_inner">\n<ul>' +'\n'.join(lis[:split]) + '</ul>\n</div>'
        else:
            ret += '\n<ul>' +'\n'.join(lis[:split]) + '</ul>\n'

        lis = lis[split:]

    return ret

def make_index_api_misc(binding, lang):
    misc_html = """
<ul>
    {0}
</ul>
"""
    llp_html_en = """
<ul>
    <li><a class="reference internal" href="Low_Level_Protocols/{0}.html">Specification</a></li>
</ul>
"""
    misc_li = '<li><a class="reference internal" href="Software/{0}.html">{1}</a></li>'

    llp_html = {
    'en': llp_html_en,
    'de': llp_html_en.replace('Specification', 'Spezifikation')
    }

    if not binding.is_programming_language:
        return llp_html[lang].format(binding.software_doc_suffix)
    else:
        misc_lis = []

        for misc_doc in binding.misc_docs:
            misc_lis.append(misc_li.format(misc_doc[0].format(suffix=binding.software_doc_suffix), misc_doc[1][lang]))

        return misc_html.format('\n'.join(misc_lis))

    return ''

def make_index_api():
    index_html = """
<div class="category_api">
    <div class="category_head tf-btn-more tf-btn-more-down">
        <a name="software-{4}"></a>
        {3}
    </div>
    <div class="category_body" {5}>
        <div class="category_content">
            <h3>Bricks</h3>
            {0}
            <h3>{6}</h3>
            {1}
        </div>
        <div class="category_content">
            <h3>Bricklets</h3>
            {2}
        </div>

        <p>{7}</p>
    </div>
</div>
<div style="clear: both;"></div>
"""

    script_html = """
<script type="text/javascript">
    var togglingContent = false;

    $(document).ready(function () {
        $(".category_head").click(function() {
            toggleContent($(this).parent(), 100);
        });

        updateContent(0);
    });

    $(window).on("hashchange", function () {
        if (!togglingContent) {
            updateContent(100);
        }
    });

    function updateContent(duration) {
        anchorName = location.hash.replace(/^[^#]*#/, '').replace(/^#+|#+$/, '').replace(/^\/*/, '').replace(/-open$/, '')

        if (anchorName.length > 0 && anchorName.substring(0, 9) === "software-" && anchorName !== "software-none") {
            a = $("a[name="+anchorName+"]")

            if (a.length > 0) {
                toggleContent(a.parent().parent(), duration, true);
                return;
            }
        }

        $(".tf-btn-more").parent().find(".category_body").slideUp(duration);
        $(".tf-btn-more").removeClass("tf-btn-more-up").addClass("tf-btn-more-down");
    }

    function toggleContent(parent, duration, forceShow) {
        togglingContent = true;

        categoryBody = parent.find(".category_body")
        btnMore = parent.find(".tf-btn-more")

        if (categoryBody.is(":hidden") || forceShow === true) {
            anchorName = categoryBody.parent().find(".category_head a").attr("name")

            // only set hash, if it doesn't point to the current category already
            if (location.hash.indexOf(anchorName) < 0) {
                location.hash = "/" + anchorName + "-open";
            }

            $(".tf-btn-more").parent().find(".category_body").slideUp(duration);
            $(".tf-btn-more").removeClass("tf-btn-more-up").addClass("tf-btn-more-down");

            btnMore.removeClass("tf-btn-more-down").addClass("tf-btn-more-up");

            // this has to be the last line and after the hash change
            categoryBody.slideDown(duration, function() { togglingContent = false });
        }
        else {
            btnMore.removeClass("tf-btn-more-up").addClass("tf-btn-more-down");

            if (/software-/.test(location.hash)) {
                location.hash = "/software-none-open";
            }

            // this has to be the last line and after the hash change
            categoryBody.slideUp(duration, function() { togglingContent = false });
        }
    }
</script>
"""

    misc = {
    'en': 'Miscellaneous',
    'de': 'Sonstiges'
    }

    discontinued_p = {
    'en': 'There is an extra section for discontinued {0} and {1}.',
    'de': 'Es gibt einen extra Abschnitt für abgekündigte {0} und {1}.'
    }

    discontinued_a = '<a class="reference internal" href="{0}/{1}_{2}_Discontinued.html">{1}</a>'

    html = '<div class="category_api_outer">'
    first = True

    for bindings_info in bindings_infos:
        if bindings_info.is_released:
            if first:
                first = False
                style = ''
            else:
                style = ' style="display: none;"'

            if bindings_info.is_programming_language:
                directory = 'Software'
            else:
                directory = 'Low_Level_Protocols'

            html += index_html.format(make_index_api_device(brick_infos, 'Bricks', bindings_info.software_doc_suffix),
                                      make_index_api_misc(bindings_info, lang),
                                      make_index_api_device(bricklet_infos, 'Bricklets', bindings_info.software_doc_suffix),
                                      bindings_info.display_name,
                                      bindings_info.url_part,
                                      style,
                                      misc[lang],
                                      discontinued_p[lang].format(discontinued_a.format(directory, 'Bricks', bindings_info.software_doc_suffix),
                                                                  discontinued_a.format(directory, 'Bricklets', bindings_info.software_doc_suffix)))

    return html + '</div>' + script_html

def make_hlpi_table(device_info):
    table_head = {
    'en': """
.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 10, 10, 10

""",
    'de': """
.. csv-table::
   :header: "Sprache", "API", "Beispiele", "Installation"
   :widths: 25, 10, 10, 10

"""
    }

    row_source = {
    'en': '   "{0}", ":ref:`API <{1}_{2}_api>`", ":ref:`Examples <{1}_{2}_examples>`", ":ref:`Installation <api_bindings_{2}_install>`"',
    'de': '   "{0}", ":ref:`API <{1}_{2}_api>`", ":ref:`Beispiele <{1}_{2}_examples>`", ":ref:`Installation <api_bindings_{2}_install>`"'
    }

    row = '   "{0}", ":ref:`API <{1}_{2}_api>`"'
    rows = []

    for bindings_info in bindings_infos:
        if not bindings_info.is_released:
            continue

        if bindings_info.is_programming_language:
            rows.append(row_source[lang].format(bindings_info.display_name, device_info.ref_name, bindings_info.url_part))
        else:
            rows.append(row.format(bindings_info.display_name, device_info.ref_name, bindings_info.url_part))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_device_identifier_table():
    table_head = {
    'en': """
.. csv-table::
   :header: "Device Identifier", "Device"
   :widths: 30, 100

""",
    'de': """
.. csv-table::
   :header: "Device Identifier", "Device"
   :widths: 30, 100

"""
    }

    row = '   "{0}", ":ref:`{1} <{2}>`"'
    rows = []

    for device_info in sorted(brick_infos + bricklet_infos, key=lambda x: x.identifier):
        if device_info.is_documented and device_info.identifier != None:
            rows.append(row.format(device_info.identifier, device_info.long_display_name, device_info.ref_name))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_authentication_tutorial_examples_table():
    row = '* :ref:`{0} <ipcon_{1}_examples>`'
    rows = []

    for bindings_info in bindings_infos:
        if bindings_info.has_authentication_example and bindings_info.is_released:
            rows.append(row.format(bindings_info.display_name, bindings_info.url_part))

    return '\n'.join(rows) + '\n'

def make_hardware_devices_toctree(device_infos, discontinued):
    prefix = """
.. toctree::
   :hidden:

"""
    line = '   {0} <{1}>'
    lines = []

    for device_info in sorted(device_infos, key=lambda x: x.long_display_name.lower()):
        long_display_name = device_info.long_display_name

        if not device_info.is_documented:
            long_display_name = '~' + long_display_name

        if device_info.is_discontinued == discontinued:
            lines.append(line.format(long_display_name, device_info.hardware_doc_name))

    return prefix + '\n'.join(lines) + '\n'

def make_hardware_devices_table(device_infos, discontinued):
    table_head = {
    'en': """
.. csv-table::
   :header: "Name", "Description"
   :widths: 25, 75

""",
    'de': """
.. csv-table::
   :header: "Name", "Beschreibung"
   :widths: 25, 75

"""
}
    row = '   ":ref:`{0} <{1}>`", "{2}"'
    rows = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.is_documented and device_info.is_discontinued == discontinued:
            rows.append(row.format(device_info.short_display_name, device_info.ref_name, device_info.description[lang].replace('"', "inch")))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_software_devices_toctree(bindings_info, device_infos, category, ref_prefix, discontinued):
    prefix = """
.. toctree::
   :hidden:

"""
    line = '   {0} <{1}{2}/{3}_{4}>'
    lines = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        long_display_name = device_info.long_display_name

        if not device_info.is_documented:
            long_display_name = '~' + long_display_name

        if device_info.has_bindings and device_info.is_discontinued == discontinued:
            lines.append(line.format(long_display_name, ref_prefix, category, device_info.software_doc_prefix, bindings_info.software_doc_suffix))

    return prefix + '\n'.join(lines) + '\n'

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

    get_latest_version_info()

    print('Generating index_hardware.html')
    write_if_changed(os.path.join(path, 'source', 'index_hardware.html'), make_index_hardware())

    print('Generating index_api.html')
    write_if_changed(os.path.join(path, 'source', 'index_api.html'), make_index_api())

    print('Generating Primer_bricks.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_bricks.table'), make_primer_table(brick_infos))

    print('Generating Primer_bricklets.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_bricklets.table'), make_primer_table(bricklet_infos))

    print('Generating Primer_extensions.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_extensions.table'), make_primer_table(extension_infos))

    print('Generating Primer_power_supplies.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_power_supplies.table'), make_primer_table(power_supply_infos))

    print('Generating Primer_accessories.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_accessories.table'), make_primer_table(accessory_infos))

    print('Generating Downloads_tools.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_tools.table'), make_download_tools_table())

    print('Generating Downloads_bindings.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_bindings.table'), make_download_bindings_table())

    print('Generating Downloads_red_images.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_red_images.table'), make_download_red_images_table())

    print('Generating Downloads_brick_firmwares.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_brick_firmwares.table'), make_download_brick_firmwares_table())

    print('Generating Downloads_bricklet_plugins.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_bricklet_plugins.table'), make_download_bricklet_plugins_table())

    print('Generating Downloads_extension_firmwares.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_extension_firmwares.table'), make_download_extension_firmwares_table())

    print('Generating Downloads_kits.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_kits.table'), make_download_kits_table())

    print('Generating Source_Code_gits.table')
    write_if_changed(os.path.join(path, 'source', 'Source_Code_gits.table'), make_source_code_gits_table())

    print('Generating Bricks.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', 'Bricks.toctree'), make_hardware_devices_toctree(brick_infos, False))

    print('Generating Bricks_Discontinued.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', 'Bricks_Discontinued.toctree'), make_hardware_devices_toctree(brick_infos, True))

    print('Generating Bricklets.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', 'Bricklets.toctree'), make_hardware_devices_toctree(bricklet_infos, False))

    print('Generating Bricklets_Discontinued.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', 'Bricklets_Discontinued.toctree'), make_hardware_devices_toctree(bricklet_infos, True))

    print('Generating Master_Extensions.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Master_Extensions', 'Master_Extensions.toctree'), make_hardware_devices_toctree(extension_infos, False))

    print('Generating Master_Extensions_Discontinued.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Master_Extensions', 'Master_Extensions_Discontinued.toctree'), make_hardware_devices_toctree(extension_infos, True))

    print('Generating Power_Supplies.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Power_Supplies', 'Power_Supplies.toctree'), make_hardware_devices_toctree(power_supply_infos, False))

    print('Generating Power_Supplies_Discontinued.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Power_Supplies', 'Power_Supplies_Discontinued.toctree'), make_hardware_devices_toctree(power_supply_infos, True))

    print('Generating Accessories.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Accessories', 'Accessories.toctree'), make_hardware_devices_toctree(accessory_infos, False))

    print('Generating Accessories_Discontinued.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Accessories', 'Accessories_Discontinued.toctree'), make_hardware_devices_toctree(accessory_infos, True))

    print('Generating Bricks.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', 'Bricks.table'), make_hardware_devices_table(brick_infos, False))

    print('Generating Bricks_Discontinued.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', 'Bricks_Discontinued.table'), make_hardware_devices_table(brick_infos, True))

    print('Generating Bricklets.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', 'Bricklets.table'), make_hardware_devices_table(bricklet_infos, False))

    print('Generating Bricklets_Discontinued.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', 'Bricklets_Discontinued.table'), make_hardware_devices_table(bricklet_infos, True))

    print('Generating Master_Extensions.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Master_Extensions', 'Master_Extensions.table'), make_hardware_devices_table(extension_infos, False))

    print('Generating Master_Extensions_Discontinued.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Master_Extensions', 'Master_Extensions_Discontinued.table'), make_hardware_devices_table(extension_infos, True))

    print('Generating Power_Supplies.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Power_Supplies', 'Power_Supplies.table'), make_hardware_devices_table(power_supply_infos, False))

    print('Generating Power_Supplies_Discontinued.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Power_Supplies', 'Power_Supplies_Discontinued.table'), make_hardware_devices_table(power_supply_infos, True))

    print('Generating Accessories.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Accessories', 'Accessories.table'), make_hardware_devices_table(accessory_infos, False))

    print('Generating Accessories_Discontinued.table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Accessories', 'Accessories_Discontinued.table'), make_hardware_devices_table(accessory_infos, True))

    print('Generating Discontinued_Products_table')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Discontinued_Products.table'), make_discontinued_products_table())

    for brick_info in brick_infos:
        if not brick_info.has_bindings:
            continue

        print('Generating {0}_hlpi.table'.format(brick_info.hardware_doc_name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', brick_info.hardware_doc_name + '_hlpi.table'), make_hlpi_table(brick_info))

    for bricklet_info in bricklet_infos:
        if not bricklet_info.has_bindings:
            continue

        print('Generating {0}_hlpi.table'.format(bricklet_info.hardware_doc_name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', bricklet_info.hardware_doc_name + '_hlpi.table'), make_hlpi_table(bricklet_info))

    print('Generating Device_Identifier.table')
    write_if_changed(os.path.join(path, 'source', 'Software', 'Device_Identifier.table'), make_device_identifier_table())

    print('Generating Tutorial_authenticate_examples.table')
    write_if_changed(os.path.join(path, 'source', 'Tutorials', 'Tutorial_Authentication', 'Tutorial_authenticate_examples.table'), make_authentication_tutorial_examples_table())

    for bindings_info in bindings_infos:
        if bindings_info.is_programming_language:
            print('Generating API_Bindings_{0}_links.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'API_Bindings_{0}_links.table'.format(bindings_info.software_doc_suffix)), make_api_bindings_links_table(bindings_info))
        else:
            print('Generating {0}_links.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', '{0}_links.table'.format(bindings_info.software_doc_suffix)), make_llproto_links_table(bindings_info))

    for bindings_info in bindings_infos:
        if not bindings_info.is_programming_language:
            continue

        template = {'en': u"""
{lang} - {device_type}{discontinued_title_parenthesis}
{equal_signs}

Links to the API reference for the {discontinued}{device_type} as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Kits <index_kits>` section.

.. include:: {device_type}_{lang_path}{discontinued_title_underscore}.table

.. include:: {device_type}_{lang_path}{discontinued_title_underscore}.toctree
""",
'de': u"""
{lang} - {device_type}{discontinued_title_parenthesis}
{equal_signs}

Links zur API Referenz der {discontinued}{device_type} sowie den
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: {device_type}_{lang_path}{discontinued_title_underscore}.table

.. include:: {device_type}_{lang_path}{discontinued_title_underscore}.toctree
""" }
        disc_title_par = {'en': u" (Discontinued)", 'de': u" (Abgekündigt)"}
        disc = {'en': u"discontinued ", 'de': u"abgekündigten "}
        disp_name = bindings_info.display_name
        lang_path = bindings_info.software_doc_suffix
        for dev in [u"Bricks", u"Bricklets"]:
            print('Generating {dev}_{lang}_Discontinued.rst'.format(dev=dev, lang=lang_path))
            discontinued = template[lang].format(lang=disp_name,
                                                    lang_path = lang_path,
                                                    device_type=dev,
                                                    discontinued=disc[lang],
                                                    discontinued_title_parenthesis=disc_title_par[lang],
                                                    equal_signs="="*(len(disp_name) + 3 + len(dev) + len(disc_title_par[lang])),
                                                    discontinued_title_underscore="_Discontinued")
            write_if_changed(os.path.join(path, 'source', 'Software', "{dev}_{lang}_Discontinued.rst".format(dev=dev, lang=lang_path)), discontinued.encode('utf-8'))

            print('Generating {dev}_{lang}.rst'.format(dev=dev, lang=lang_path))
            normal = template[lang].format(lang=disp_name,
                                            lang_path = lang_path,
                                            device_type=dev,
                                            discontinued="",
                                            discontinued_title_parenthesis="",
                                            equal_signs="="*(len(disp_name) + 3 + len(dev)),
                                            discontinued_title_underscore="")
            write_if_changed(os.path.join(path, 'source', 'Software', "{dev}_{lang}.rst".format(dev=dev, lang=lang_path)), normal.encode('utf-8'))

    for bindings_info in bindings_infos:
        if bindings_info.is_programming_language:
            print('Generating Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, brick_infos, 'Bricks', '', False))

            print('Generating Bricks_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, brick_infos, 'Bricks', '', True))

            print('Generating Bricks_{0}.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks_{0}.table'.format(bindings_info.software_doc_suffix)), make_api_bindings_devices_table(bindings_info, brick_infos, 'Brick', False))

            print('Generating Bricks_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix)), make_api_bindings_devices_table(bindings_info, brick_infos, 'Brick', True))
        else:
            print('Generating Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, brick_infos, 'Bricks', '../Software/', False))

            print('Generating Bricks_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricks_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, brick_infos, 'Bricks', '../Software/', True))

            print('Generating Bricks_{0}.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricks_{0}.table'.format(bindings_info.software_doc_suffix)), make_llproto_devices_table(bindings_info, brick_infos, 'Brick', False))

            print('Generating Bricks_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricks_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix)), make_llproto_devices_table(bindings_info, brick_infos, 'Brick', True))

    for bindings_info in bindings_infos:
        if bindings_info.is_programming_language:
            print('Generating Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, bricklet_infos, 'Bricklets', '', False))

            print('Generating Bricklets_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, bricklet_infos, 'Bricklets', '', True))

            print('Generating Bricklets_{0}.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets_{0}.table'.format(bindings_info.software_doc_suffix)), make_api_bindings_devices_table(bindings_info, bricklet_infos, 'Bricklet', False))

            print('Generating Bricklets_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix)), make_api_bindings_devices_table(bindings_info, bricklet_infos, 'Bricklet', True))
        else:
            print('Generating Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, bricklet_infos, 'Bricklets', '../Software/', False))

            print('Generating Bricklets_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricklets_{0}_Discontinued.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, bricklet_infos, 'Bricklets', '../Software/', True))

            print('Generating Bricklets_{0}.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricklets_{0}.table'.format(bindings_info.software_doc_suffix)), make_llproto_devices_table(bindings_info, bricklet_infos, 'Bricklet', False))

            print('Generating Bricklets_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix))
            write_if_changed(os.path.join(path, 'source', 'Low_Level_Protocols', 'Bricklets_{0}_Discontinued.table'.format(bindings_info.software_doc_suffix)), make_llproto_devices_table(bindings_info, bricklet_infos, 'Bricklet', True))

if __name__ == "__main__":
    generate(os.getcwd())
