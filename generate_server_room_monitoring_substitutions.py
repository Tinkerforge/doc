#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from kit_generics import bindings
from kit_generics import binding_name
from kit_generics import binding_names

lang = 'en'

def make_substitutions():
    substitutions = ''

    formated_binding_names = []
    for binding in bindings:
        formated_binding_names.append(binding_name[lang].format(binding[0], binding[2]))

    substitutions += binding_names[lang].format(', '.join(formated_binding_names)) + '\n'

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
        print 'Wrong working directory'
        sys.exit(1)

    print 'Generating ServerRoomMonitoring.substitutions'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'ServerRoomMonitoring', 'ServerRoomMonitoring.substitutions'), make_substitutions())

if __name__ == "__main__":
    generate(os.getcwd())
