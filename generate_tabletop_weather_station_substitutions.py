#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

DEBUG = False
if __name__ == "__main__" and not DEBUG:
    print("Suppressing output of generate_tabletop_weather_station_substitutions.py")

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

import os
import sys

import generate_tables

bindings_infos = generate_tables.bindings_infos
lang = 'en'

          # url_part, display_name
examples = {'c':      'C',
            'csharp': 'C#',
            'delphi': 'Delphi',
            'java':   'Java',
            'php':    'PHP',
            'python': 'Python',
            'ruby':   'Ruby',
            'vbnet':  'Visual Basic .NET'}

binding_name = {
'en':
""":ref:`{0} <api_bindings_{1}>`""",
'de':
""":ref:`{0} <api_bindings_{1}>`"""
}

binding_names = {
'en':
"""
.. |bindings| replace:: {0}
""",
'de':
"""
.. |bindings| replace:: {0}
"""
}

example_downloads = {
'en':
"""
.. |examples_download| replace:: {0}
""",
'de':
"""
.. |examples_download| replace:: {0}
"""
}

example_download_simple = {
'en':
"""`{0} <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/examples/{1}>`__""",
'de':
"""`{0} <https://github.com/Tinkerforge/tabletop-weather-station/tree/master/examples/{1}>`__"""
}



def make_substitutions():
    substitutions = '\n>>>general\n'

    formated_binding_names = []
    for bindings_info in bindings_infos:
        if bindings_info.is_programming_language and bindings_info.is_released:
            formated_binding_names.append(binding_name[lang].format(bindings_info.display_name, bindings_info.url_part))

    substitutions += binding_names[lang].format(', '.join(formated_binding_names)) + '\n'

    example_download_lines = []
    for bindings_info in bindings_infos:
        if bindings_info.url_part in examples and bindings_info.is_programming_language and bindings_info.is_released:
            example_download_lines.append(example_download_simple[lang].format(examples[bindings_info.url_part], bindings_info.url_part))

    substitutions += example_downloads[lang].format(', '.join(example_download_lines)) 
    substitutions += '\n<<<general\n'

    substitutions += '\n>>>example_list\n'
    substitutions += '* ' + '\n* '.join(example_download_lines)
    substitutions += '\n<<<example_list\n'

    return substitutions

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
        debug('Wrong working directory')
        sys.exit(1)

    generate_tables.lang = lang

    debug('Generating TabletopWeatherStation.substitutions')
    write_if_changed(os.path.join(path, 'source', 'Kits', 'TabletopWeatherStation', 'TabletopWeatherStation.substitutions'), make_substitutions())

if __name__ == "__main__":
    generate(os.getcwd())
