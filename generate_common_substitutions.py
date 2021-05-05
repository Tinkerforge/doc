#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DEBUG = False

if __name__ == "__main__" and not DEBUG:
    print("Suppressing output of generate_common_substitutions.py")

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

import os
import sys

sys.path.append(os.path.join(os.path.split(__file__)[0], '../generators'))
from device_infos import brick_infos, bricklet_infos

lang = 'en'

ipcon_common = {
'en': """
>>>intro
This is the description of the |ref_api_bindings| for the IP Connection.
The IP Connection manages the communication between the API bindings and the
:ref:`Brick Daemon <brickd>` or a :ref:`WIFI <wifi_extension>`/:ref:`Ethernet
<ethernet_extension>` Extension. Before :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` can be controlled using their API an
IP Connection has to be created and its TCP/IP connection has to be established.

An |ref_install_guide| for the |bindings_name| API bindings is part of their
general description.
<<<intro
""",
'de': """
>>>intro
Dies ist die Beschreibung der |ref_api_bindings| für die IP Connection.
Die IP Connection kümmert sich um die Kommunikation zwischen einem
:ref:`Brick Daemon <brickd>` oder einer
:ref:`WIFI <wifi_extension>`/:ref:`Ethernet <ethernet_extension>` Extension.
Bevor :ref:`Bricks <primer_bricks>` und :ref:`Bricklets <primer_bricklets>` über
deren API angesprochen werden können muss eine IP Connection erzeugt und
die TCP/IP Verbindung hergestellt werden.

Eine |ref_install_guide| für die |bindings_name| API Bindings ist Teil deren
allgemeine Beschreibung.
<<<intro
"""
}

brick_test_intro = {
'en':
""".. |test_intro| replace::
 To test a {0} you need to have :ref:`Brick Daemon <brickd>` and
 :ref:`Brick Viewer <brickv>` installed. Brick Daemon acts as a proxy between
 the USB interface of the Bricks and the API bindings. Brick Viewer connects
 to Brick Daemon. It helps to figure out basic information about the connected
 Bricks and Bricklets and allows to test them.
""",
'de':
""".. |test_intro| replace::
 Um einen {0} testen zu können, müssen zuerst :ref:`Brick Daemon
 <brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
 arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
 Bindings. Brick Viewer kann sich mit Brick Daemon verbinden, gibt
 Informationen über die angeschlossenen Bricks und Bricklets aus und ermöglicht
 es diese zu testen.
"""
}

brick_test_tab = {
'en':
""".. |test_tab| replace::
 Now connect the Brick to the PC over USB, you should see a new tab named
 "{0}" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0}" auftauchen. Wähle diesen Tab
 aus.
"""
}

brick_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{1}_programming_interface>`
 section for the API of the {0} and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{1}_programming_interface>` listet die
 API des {0} und Beispiele in verschiedenen Programmiersprachen auf.
"""
}

bricklet_case_steps = {
'en':
"""
>>>bricklet_case_steps
The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* screw bottom plate to bottom spacers,
* build up side plates,
* plug side plates into bottom plate and
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the {0} case:
<<<bricklet_case_steps
""",
'de':
"""
>>>bricklet_case_steps
Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* schraube Unterteil an untere Abstandshalter,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil und
* schraube Oberteil auf obere Abstandshalter.

Im Folgenden befindet sich eine Explosionszeichnung des {0} Gehäuses:
<<<bricklet_case_steps
"""
}

bricklet_case_hint = {
'en':
""".. |bricklet_case_hint| replace::
 Hint: There is a protective film on both sides of the plates,
 you have to remove it before assembly.
""",
'de':
""".. |bricklet_case_hint| replace::
 Hinweis: Auf beiden Seiten der Platten ist eine Schutzfolie, 
 diese muss vor dem Zusammenbau entfernt werden.
"""
}

bricklet_test_intro = {
'en':
""".. |test_intro| replace::
 To test a {0} you need to have :ref:`Brick Daemon <brickd>` and
 :ref:`Brick Viewer <brickv>` installed. Brick Daemon acts as a proxy between
 the USB interface of the Bricks and the API bindings. Brick Viewer connects
 to Brick Daemon. It helps to figure out basic information about the connected
 Bricks and Bricklets and allows to test them.
""",
'de':
""".. |test_intro| replace::
 Um ein {0} testen zu können, müssen zuerst :ref:`Brick Daemon
 <brickd>` und :ref:`Brick Viewer <brickv>` installiert werden. Brick Daemon
 arbeitet als Proxy zwischen der USB Schnittstelle der Bricks und den API
 Bindings. Brick Viewer kann sich mit Brick Daemon verbinden, gibt
 Informationen über die angeschlossenen Bricks und Bricklets aus und ermöglicht
 es diese zu testen.
"""
}

bricklet_test_connect = {
'en':
""".. |test_connect| replace::
 Connect the {0} to a :ref:`Brick <primer_bricks>`
 with a Bricklet Cable
""",
'de':
""".. |test_connect| replace::
 Als nächstes muss das {0} mittels eines Bricklet Kabels mit
 einem :ref:`Brick <primer_bricks>` verbunden werden
"""
}

bricklet_test_tab = {
'en':
""".. |test_tab| replace::
 If you connect the Brick to the PC over USB, you should see a new tab named
 "{0}" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0}" auftauchen.
 Wähle diesen Tab aus.
"""
}

bricklet_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{1}_programming_interface>`
 section for the API of the {0} and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{1}_programming_interface>` listet
 die API des {0} und Beispiele in verschiedenen
 Programmiersprachen auf.
"""
}

def make_ipcon_substitutions():
    substitutions = ''
    substitutions += ipcon_common[lang]

    return substitutions

def make_brick_substitutions(brick_info):
    substitutions = ''
    substitutions += brick_test_intro[lang].format(brick_info.long_display_name) + '\n'
    substitutions += brick_test_tab[lang].format(brick_info.long_display_name) + '\n'
    substitutions += brick_test_pi_ref[lang].format(brick_info.long_display_name, brick_info.ref_name)

    return substitutions

def make_bricklet_substitutions(bricklet_info):
    substitutions = ''
    substitutions += '>>>substitutions\n'
    substitutions += bricklet_test_intro[lang].format(bricklet_info.long_display_name) + '\n'
    substitutions += bricklet_test_connect[lang].format(bricklet_info.long_display_name) + '\n'
    substitutions += bricklet_test_tab[lang].format(bricklet_info.long_display_name) + '\n'
    substitutions += bricklet_test_pi_ref[lang].format(bricklet_info.long_display_name, bricklet_info.ref_name) + '\n'
    substitutions += bricklet_case_hint[lang] + '\n'
    substitutions += '<<<substitutions\n'
    substitutions += bricklet_case_steps[lang].format(bricklet_info.long_display_name) + '\n'

    return substitutions

def write_if_changed(path, content):
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing = f.read()

        if existing == content:
            return

    with open(path, 'w') as f:
        f.write(content)

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        debug('Wrong working directory')
        sys.exit(1)

    write_if_changed(os.path.join(path, 'source', 'Software', 'IPConnection_Common.substitutions'), make_ipcon_substitutions())

    for brick_info in brick_infos:
        debug('Generating {0}.substitutions (Hardware)'.format(brick_info.hardware_doc_name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', brick_info.hardware_doc_name + '.substitutions'), make_brick_substitutions(brick_info))

    for bricklet_info in bricklet_infos:
        debug('Generating {0}.substitutions (Hardware)'.format(bricklet_info.hardware_doc_name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', bricklet_info.hardware_doc_name + '.substitutions'), make_bricklet_substitutions(bricklet_info))

if __name__ == "__main__":
    generate(os.getcwd())
