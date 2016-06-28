#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2
import math
from collections import namedtuple

sys.path.append(os.path.join(os.getcwd(), '..', '..', 'generators'))
from device_infos import DeviceInfo, brick_infos, bricklet_infos

lang = 'en'

ToolInfo = namedtuple('ToolInfo', 'display_name url_part')

tool_infos = \
[
    ToolInfo('Brick Daemon', 'brickd'),
    ToolInfo('Brick Viewer', 'brickv'),
    ToolInfo('Brick Logger', 'brick_logger')
]

BindingsInfo = namedtuple('BindingsInfo', 'display_name url_part software_doc_suffix is_programming_language is_released tutorial')

bindings_infos = \
[
    BindingsInfo('C/C++', 'c', 'C', True, True,
                 {'en': 'http://www.cprogramming.com/',
                  'de': 'http://www.cprogramming.com/'}), # http://www.c-howto.de/
    BindingsInfo('C#', 'csharp', 'CSharp', True, True,
                 {'en': 'http://csharp.net-tutorials.com/',
                  'de': 'http://csharp.net-tutorials.com/'}),
    BindingsInfo('Delphi/Lazarus', 'delphi', 'Delphi', True, True,
                 {'en': 'http://www.delphibasics.co.uk/',
                  'de': 'http://www.delphi-treff.de/tutorials/grundlagen-tutorials/'}),
    BindingsInfo('Java', 'java', 'Java', True, True,
                 {'en': 'http://docs.oracle.com/javase/tutorial/',
                  'de': 'http://docs.oracle.com/javase/tutorial/'}), # http://openbook.galileocomputing.de/javainsel/
    BindingsInfo('JavaScript',  'javascript', 'JavaScript', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('LabVIEW', 'labview', 'LabVIEW', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('Mathematica', 'mathematica', 'Mathematica', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('MATLAB/Octave', 'matlab', 'MATLAB', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('Perl', 'perl', 'Perl', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('PHP', 'php', 'PHP', True, True,
                 {'en': 'http://www.php.net/manual/en/getting-started.php',
                  'de': 'http://www.php.net/manual/de/getting-started.php'}),
    BindingsInfo('Python', 'python', 'Python', True, True,
                 {'en': 'https://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
                  'de': 'https://www.python.org/about/gettingstarted/'}),
    BindingsInfo('Ruby', 'ruby', 'Ruby',  True, True,
                 {'en': 'https://www.ruby-lang.org/en/documentation/quickstart/',
                  'de': 'https://www.ruby-lang.org/de/documentation/quickstart/'}),
    BindingsInfo('Shell', 'shell', 'Shell', True, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('Tinkerforge Visual Programming Language (TVPL)', 'tvpl', 'TVPL', True, False,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('Visual Basic .NET', 'vbnet', 'VBNET', True, True,
                 {'en': 'http://howtostartprogramming.com/vb-net/',
                  'de': 'http://howtostartprogramming.com/vb-net/'}), # http://openbook.galileocomputing.de/vb_net/index.htm
    BindingsInfo('TCP/IP', 'tcpip', 'TCPIP', False, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
    BindingsInfo('Modbus', 'modbus', 'Modbus', False, True,
                 {'en': 'FIXME',
                  'de': 'FIXME'}),
]

extension_infos = \
[
    DeviceInfo(None, 'Chibi Extension', 'Chibi', 'chibi_extension', 'Chibi_Extension', None, 'chibi-extension', None, True, False,
               {'en': 'Wireless Chibi connection between stacks',
                'de': 'Drahtlose Chibi Verbindung zwischen Stapeln'}),
    DeviceInfo(None, 'Ethernet Extension', 'Ethernet', 'ethernet_extension', 'Ethernet_Extension', None, 'ethernet-extension', None, True, False,
               {'en': 'Cable based Ethernet connection between stack and PC',
                'de': 'Kabelgebundene Ethernet Verbindung zwischen Stapel und PC'}),
    DeviceInfo(None, 'RS485 Extension', 'RS485', 'rs485_extension', 'RS485_Extension', None, 'rs485-extension', None, True, False,
               {'en': 'Cable based RS485 connection between stacks',
                'de': 'Kabelgebundene RS485 Verbindung zwischen Stapeln'}),
    DeviceInfo(None, 'WIFI Extension', 'WIFI', 'wifi_extension', 'WIFI_Extension', None, 'wifi-extension', None, True, False,
               {'en': 'Wireless Wi-Fi connection between stack and PC',
                'de': 'Drahtlose WLAN Verbindung zwischen Stapel und PC'}),
    DeviceInfo(None, 'WIFI Extension 2.0', 'WIFI 2.0', 'wifi_v2_extension', 'WIFI_V2_Extension', None, 'wifi-v2-extension', None, False, False,
               {'en': 'Wireless Wi-Fi connection between stack and PC',
                'de': 'Drahtlose WLAN Verbindung zwischen Stapel und PC'})
]

power_supply_infos = \
[
    DeviceInfo(None, 'Step-Down Power Supply', 'Step-Down', 'step_down_power_supply', 'Step_Down', None, 'step-down-powersupply', None, True, False,
               {'en': 'Powers a stack of Bricks with 5V',
                'de': 'Versorgt einen Stapel von Bricks mit 5V'})
]

accessory_infos = \
[
    DeviceInfo(None, 'DC Jack Adapter', 'DC Jack Adapter', 'dc_jack_adapter', 'DC_Jack_Adapter', None, 'dc-adapter', None, True, False,
               {'en': 'Adapter between a 5mm DC jack and 2 Pole Black Connector',
                'de': 'Adapter zwischen einem 5mm DC Stecker und 2 Pin Stecker Schwarz'})
]

KitInfo = namedtuple('KitInfo', 'display_name url_part')

kit_infos = \
[
    KitInfo({'en': 'Blinkenlights', 'de': 'Blinkenlights'}, 'blinkenlights'),
    KitInfo({'en': 'Camera Slider', 'de': 'Kameraschlitten'}, 'camera_slider'),
    KitInfo({'en': 'Weather Station', 'de': 'Wetterstation'}, 'weather_station')
]

LATEST_VERSIONS_URL = 'http://download.tinkerforge.com/latest_versions.txt'

tool_versions = {}
bindings_versions = {}
firmware_versions = {}
plugin_versions = {}
kit_versions = {}

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
        elif parts[0] == 'kits':
            kit_versions[parts[1]] = latest_version

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
        if device_info.is_released:
            rows.append(row.format(device_info.short_display_name, device_info.ref_name, device_info.description[lang].replace('"', "inch")))

    return table_head[lang] + '\n'.join(rows) + '\n'

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
 :widths: 17, 32, 5, 5, 8

""",
    'de': """.. csv-table::
 :header: "Tool", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
    }

    row_brickd = ' :ref:`{0} <{1}>` | Linux (`amd64 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_amd64.deb>`__, `i386 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_i386.deb>`__, `armhf <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_armhf.deb>`__, `RED Brick <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}+redbrick_armhf.deb>`__), `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <http://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/src/changelog>`__'
    row_brick_logger = ' :ref:`{0} <{1}>` | `Linux, Mac OS X, Windows <http://download.tinkerforge.com/tools/{1}/{1}_{4}_{5}_{6}.zip>`__, `RED Brick <http://download.tinkerforge.com/tools/{1}/{1}_{4}_{5}_{6}.tfrba>`__, `{2} <https://github.com/Tinkerforge/brickv/archive/brick-logger-{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <http://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/brickv/master/src/changelog.brick-logger>`__'
    row_other = ' :ref:`{0} <{1}>` | `Linux <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_all.deb>`__, `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <http://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/src/changelog>`__'
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
 :widths: 17, 32, 5, 5, 8

""",
    'de': """.. csv-table::
 :header: "Sprache", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
    }

    row = ' `{0} <http://www.tinkerforge.com/' + lang + '/doc/Software/API_Bindings_{2}.html>`__ | `{4} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_{5}_{6}_{7}.zip>`__ | {5}.{6}.{7} | `{3} <http://download.tinkerforge.com/bindings/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/generators/master/{1}/changelog.txt>`__'
    rows = []

    for bindings_info in bindings_infos:
        if not bindings_info.is_programming_language or not bindings_info.is_released:
            continue

        rows.append(row.format(bindings_info.display_name,
                               bindings_info.url_part,
                               bindings_info.software_doc_suffix,
                               archive[lang],
                               bindings_and_examples[lang],
                               *bindings_versions[bindings_info.url_part]))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_firmwares_table():
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
 :widths: 17, 32, 5, 5, 8

""",
    'de': """.. csv-table::
 :header: "Brick", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
    }

    row = ' :ref:`{0} <{1}>` | `Firmware <http://download.tinkerforge.com/firmwares/bricks/{2}/brick_{2}_firmware_{6}_{7}_{8}.bin>`__, `{3} <https://github.com/Tinkerforge/{4}/archive/v{6}.{7}.{8}.zip>`__ | {6}.{7}.{8} | `{5} <http://download.tinkerforge.com/firmwares/bricks/{2}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{4}/master/software/changelog>`__'
    rows = []

    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.firmware_url_part != None and brick_info.is_released:
            firmware_version = firmware_versions.get(brick_info.firmware_url_part, (0,0,0))

            rows.append(row.format(brick_info.short_display_name,
                                   brick_info.ref_name,
                                   brick_info.firmware_url_part,
                                   source_code[lang],
                                   brick_info.git_name,
                                   archive[lang],
                                   *firmware_version))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_download_plugins_table():
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
 :widths: 17, 32, 5, 5, 8

""",
    'de': """.. csv-table::
 :header: "Bricklet", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
    }

    row = ' :ref:`{0} <{1}>` | `Plugin <http://download.tinkerforge.com/firmwares/bricklets/{2}/bricklet_{2}_firmware_{6}_{7}_{8}.bin>`__, `{3} <https://github.com/Tinkerforge/{4}/archive/v{6}.{7}.{8}.zip>`__ | {6}.{7}.{8} | `{5} <http://download.tinkerforge.com/firmwares/bricklets/{2}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{4}/master/software/changelog>`__'
    rows = []

    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.firmware_url_part != None and bricklet_info.is_released:
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
                                       *plugin_version))

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
 :header: "Starter Kit", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

""",
    'de': """.. csv-table::
 :header: "Starterkit", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
    }

    row = ' :ref:`{0} <starter_kit_{1}>` | `Linux <http://download.tinkerforge.com/kits/{1}/linux/starter-kit-{2}-demo-{5}.{6}.{7}_all.deb>`__, `Mac OS X <http://download.tinkerforge.com/kits/{1}/macos/starter_kit_{1}_demo_macos_{5}_{6}_{7}.dmg>`__, `Windows <http://download.tinkerforge.com/kits/{1}/windows/starter_kit_{1}_demo_windows_{5}_{6}_{7}.exe>`__, `{3} <https://github.com/Tinkerforge/{2}/archive/demo-{5}.{6}.{7}.zip>`__ | {5}.{6}.{7} | `{4} <http://download.tinkerforge.com/kits/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{2}/master/demo/changelog>`__'
    rows = []

    for kit_info in kit_infos:
        rows.append(row.format(kit_info.display_name[lang],
                               kit_info.url_part,
                               kit_info.url_part.replace('_', '-'),
                               source_code[lang],
                               archive[lang],
                               *kit_versions[kit_info.url_part]))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_api_bindings_links_table(bindings_info):
    table_head = {
    'en': """.. csv-table::
 :header: "", "API", "Examples"
 :delim: |
 :widths: 20, 10, 10

{0}
 | |
 **Bricks** | |
{1}
 | |
 **Bricklets** | |
{2}
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
 **Bricklets** | |
{2}
"""
    }

    ipcon_row = {
    'en': ' IP Connection | :ref:`API <ipcon_{0}>` | :ref:`Examples <ipcon_{0}_examples>`',
    'de': ' IP Connection | :ref:`API <ipcon_{0}>` | :ref:`Beispiele <ipcon_{0}_examples>`'
    }

    device_row = {
    'en': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Examples <{0}_{1}_examples>`',
    'de': ' :ref:`{2} <{0}>` | :ref:`API <{0}_{1}_api>` | :ref:`Beispiele <{0}_{1}_examples>`'
    }

    brick_lines = []
    for brick_info in sorted(brick_infos, key=lambda x: x.short_display_name.lower()):
        if brick_info.is_released and brick_info.has_bindings:
            brick_lines.append(device_row[lang].format(brick_info.ref_name, bindings_info.url_part, brick_info.short_display_name))

    bricklet_lines = []
    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_released and bricklet_info.has_bindings:
            bricklet_lines.append(device_row[lang].format(bricklet_info.ref_name, bindings_info.url_part, bricklet_info.short_display_name))

    return table_head[lang].format(ipcon_row[lang].format(bindings_info.url_part),
                                   '\n'.join(brick_lines),
                                   '\n'.join(bricklet_lines))

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
        if brick_info.is_released and brick_info.has_bindings:
            brick_lines.append(device_row[lang].format(brick_info.ref_name, bindings_info.url_part, brick_info.short_display_name))

    bricklet_lines = []
    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_released and bricklet_info.has_bindings:
            bricklet_lines.append(device_row[lang].format(bricklet_info.ref_name, bindings_info.url_part, bricklet_info.short_display_name))

    return table_head[lang].format('\n'.join(brick_lines),
                                   '\n'.join(bricklet_lines))

def make_source_code_gits_table():
    table_head = {
    'en': """.. csv-table::
 :header: "", "Repository", "Bug Tracking"
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
        if brick_info.is_released:
            brick_rows.append(row[lang].format(brick_info.short_display_name, brick_info.git_name))

    for bricklet_info in sorted(bricklet_infos, key=lambda x: x.short_display_name.lower()):
        if bricklet_info.is_released:
            bricklet_rows.append(row[lang].format(bricklet_info.short_display_name, bricklet_info.git_name))

    for extension_info in sorted(extension_infos, key=lambda x: x.short_display_name.lower()):
        if extension_info.is_released:
            extension_rows.append(row[lang].format(extension_info.short_display_name, extension_info.git_name))

    for power_supply_info in sorted(power_supply_infos, key=lambda x: x.short_display_name.lower()):
        if power_supply_info.is_released:
            power_supply_rows.append(row[lang].format(power_supply_info.short_display_name, power_supply_info.git_name))

    for accessory_info in sorted(accessory_infos, key=lambda x: x.short_display_name.lower()):
        if accessory_info.is_released:
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
        if not device_info.is_released:
            continue

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
        if device_info.is_released and device_info.has_bindings:
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
    misc_html_en = """
<ul>
    <li><a class="reference internal" href="Software/IPConnection_{0}.html">IP Connection</a></li>
    <li><a class="reference internal" href="Software/API_Bindings_{0}.html">Usage</a></li>
    {1}
</ul>
"""

    llp_html_en = """
<ul>
    <li><a class="reference internal" href="Low_Level_Protocols/{0}.html">Specification</a></li>
</ul>
"""

    additional_li_en = '<li><a class="reference internal" href="Software/API_Bindings_{0}_{1}.html">Usage ({2})</a></li>'

    misc_html = {
    'en': misc_html_en,
    'de': misc_html_en.replace('Usage', 'Benutzung')
    }

    llp_html = {
    'en': llp_html_en,
    'de': llp_html_en.replace('Specification', 'Spezifikation')
    }

    additional_li = {
    'en': additional_li_en,
    'de': additional_li_en.replace('Usage', 'Benutzung')
    }

    windows_phone = {
    'en': 'Windows Phone',
    'de': 'Win Phone'
    }

    if not binding.is_programming_language:
        return llp_html[lang].format(binding.software_doc_suffix)
    else:
        if binding.url_part == 'c':
            add = additional_li[lang].format(binding.software_doc_suffix, 'iOS', 'iOS')
        elif binding.url_part == 'csharp':
            add = additional_li[lang].format(binding.software_doc_suffix, 'Windows_Phone', windows_phone[lang])
        elif binding.url_part == 'java':
            add = additional_li[lang].format(binding.software_doc_suffix, 'Android', 'Android')
        else:
            add = ''

        return misc_html[lang].format(binding.software_doc_suffix, add)

    return ''

def make_index_api():
    index_html = """
<div class="category_api">
    <div class="category_head btn-more btn-more-down">
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

        $(".btn-more").parent().find(".category_body").slideUp(duration);
        $(".btn-more").removeClass("btn-more-up").addClass("btn-more-down");
    }

    function toggleContent(parent, duration, forceShow) {
        togglingContent = true;

        categoryBody = parent.find(".category_body")
        btnMore = parent.find(".btn-more")

        if (categoryBody.is(":hidden") || forceShow === true) {
            anchorName = categoryBody.parent().find(".category_head a").attr("name")

            // only set hash, if it doesn't point to the current category already
            if (location.hash.indexOf(anchorName) < 0) {
                location.hash = "/" + anchorName + "-open";
            }

            $(".btn-more").parent().find(".category_body").slideUp(duration);
            $(".btn-more").removeClass("btn-more-up").addClass("btn-more-down");

            btnMore.removeClass("btn-more-down").addClass("btn-more-up");

            // this has to be the last line and after the hash change
            categoryBody.slideDown(duration, function() { togglingContent = false });
        }
        else {
            btnMore.removeClass("btn-more-up").addClass("btn-more-down");

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

    html = '<div class="category_api_outer">'
    first = True

    for bindings_info in bindings_infos:
        if bindings_info.is_released:
            if first:
                first = False
                style = ''
            else:
                style = ' style="display: none;"'

            html += index_html.format(make_index_api_device(brick_infos, 'Bricks', bindings_info.software_doc_suffix),
                                      make_index_api_misc(bindings_info, lang),
                                      make_index_api_device(bricklet_infos, 'Bricklets', bindings_info.software_doc_suffix),
                                      bindings_info.display_name,
                                      bindings_info.url_part,
                                      style,
                                      misc[lang])

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
    'en': '   "{0}", ":ref:`API <{1}_{2}_api>`", ":ref:`Examples <{1}_{2}_examples>`", ":ref:`Installation <api_bindings_{2}>`"',
    'de': '   "{0}", ":ref:`API <{1}_{2}_api>`", ":ref:`Beispiele <{1}_{2}_examples>`", ":ref:`Installation <api_bindings_{2}>`"'
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
        if device_info.identifier != None:
            rows.append(row.format(device_info.identifier, device_info.long_display_name, device_info.ref_name))

    return table_head[lang] + '\n'.join(rows) + '\n'

def make_authentication_tutorial_examples_table():
    row = '* :ref:`{0} <ipcon_{1}_examples>`'
    rows = []

    for bindings_info in bindings_infos:
        if bindings_info.is_programming_language and bindings_info.is_released:
            rows.append(row.format(bindings_info.display_name, bindings_info.url_part))

    return '\n'.join(rows) + '\n'

def make_hardware_devices_toctree(device_infos):
    prefix = """
.. toctree::
   :hidden:

"""
    line = '   {0} <{1}>'
    lines = []

    for device_info in sorted(device_infos, key=lambda x: x.long_display_name.lower()):
        if device_info.is_released:
            lines.append(line.format(device_info.long_display_name, device_info.hardware_doc_name))

    return prefix + '\n'.join(lines) + '\n'

def make_software_devices_toctree(bindings_info, device_infos, category):
    prefix = """
.. toctree::
   :hidden:

"""
    line = '   {0} <{1}/{2}_{3}>'
    lines = []

    for device_info in sorted(device_infos, key=lambda x: x.short_display_name.lower()):
        if device_info.has_bindings and device_info.is_released:
            lines.append(line.format(device_info.long_display_name, category, device_info.software_doc_prefix, bindings_info.software_doc_suffix))

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

    print('Generating Downloads_firmwares.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_firmwares.table'), make_download_firmwares_table())

    print('Generating Downloads_plugins.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_plugins.table'), make_download_plugins_table())

    print('Generating Downloads_kits.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_kits.table'), make_download_kits_table())

    print('Generating Source_Code_gits.table')
    write_if_changed(os.path.join(path, 'source', 'Source_Code_gits.table'), make_source_code_gits_table())

    print('Generating Bricks.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', 'Bricks.toctree'), make_hardware_devices_toctree(brick_infos))

    print('Generating Bricklets.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', 'Bricklets.toctree'), make_hardware_devices_toctree(bricklet_infos))

    print('Generating Master_Extensions.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Master_Extensions', 'Master_Extensions.toctree'), make_hardware_devices_toctree(extension_infos))

    print('Generating Power_Supplies.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Power_Supplies', 'Power_Supplies.toctree'), make_hardware_devices_toctree(power_supply_infos))

    print('Generating Accessories.toctree')
    write_if_changed(os.path.join(path, 'source', 'Hardware', 'Accessories', 'Accessories.toctree'), make_hardware_devices_toctree(accessory_infos))

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
        print('Generating Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix))
        write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, brick_infos, 'Bricks'))

    for bindings_info in bindings_infos:
        print('Generating Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix))
        write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets_{0}.toctree'.format(bindings_info.software_doc_suffix)), make_software_devices_toctree(bindings_info, bricklet_infos, 'Bricklets'))

if __name__ == "__main__":
    generate(os.getcwd())
