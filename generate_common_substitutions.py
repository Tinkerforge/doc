#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

          # display,   uri
bricks = [('DC',      'dc'),
          ('Debug',   'debug'),
          ('IMU',     'imu'),
          ('Master',  'master'),
          ('RED',     'red'),
          ('Servo',   'servo'),
          ('Stepper', 'stepper')]

             # display,                    uri
bricklets = [('AC Current',                'ac_current'),
             ('Accelerometer',             'accelerometer'),
             ('Ambient Light',             'ambient_light'),
             ('Ambient Light 2.0',         'ambient_light_v2'),
             ('Analog In',                 'analog_in'),
             ('Analog In 2.0',             'analog_in_v2'),
             ('Analog Out',                'analog_out'),
             ('Analog Out 2.0',            'analog_in_v2'),
             ('Barometer',                 'barometer'),
             ('Breakout',                  'breakout'),
             ('Color',                     'color'),
             ('Current12',                 'current12'),
             ('Current25',                 'current25'),
             ('Distance IR',               'distance_ir'),
             ('Distance US',               'distance_us'),
             ('Dual Button',               'dual_button'),
             ('Dual Relay',                'dual_relay'),
             ('Gas Detector',              'gas_detector'),
             ('GPS',                       'gps'),
             ('Hall Effect',               'hall_effect'),
             ('Heart Rate',                'heart_rate'),
             ('Humidity',                  'humidity'),
             ('Industrial Analog Out',     'industrial_analog_out'),
             ('Industrial Digital In 4',   'industrial_digital_in_4'),
             ('Industrial Digital Out 4',  'industrial_digital_out_4'),
             ('Industrial Dual 0-20mA',    'industrial_dual_0_20ma'),
             ('Industrial Dual Analog In', 'industrial_dual_analog_in'),
             ('Industrial Quad Relay',     'industrial_quad_relay'),
             ('IO-16',                     'io16'),
             ('IO-4',                      'io4'),
             ('Joystick',                  'joystick'),
             ('Laser Range Finder',        'laser_range_finder'),
             ('LCD 16x2',                  'lcd_16x2'),
             ('LCD 20x4',                  'lcd_20x4'),
             ('LED Strip',                 'led_strip'),
             ('Line',                      'line'),
             ('Linear Poti',               'linear_poti'),
             ('Load Cell',                 'load_cell'),
             ('Moisture',                  'moisture'),
             ('Motion Detector',           'motion_detector'),
             ('Multi Touch',               'multi_touch'),
             ('NFC/RFID',                  'nfc_rfid'),
             ('Piezo Buzzer',              'piezo_buzzer'),
             ('Piezo Speaker',             'piezo_speaker'),
             ('PTC',                       'ptc'),
             ('Remote Switch',             'remote_switch'),
             ('Rotary Encoder',            'rotary_encoder'),
             ('Rotary Poti',               'rotary_poti'),
             ('RS232',                     'rs232'),
             ('Segment Display 4x7',       'segment_display_4x7'),
             ('Solid State Relay',         'solid_state_relay'),
             ('Sound Intensity',           'sound_intensity'),
             ('Temperature',               'temperature'),
             ('Temperature IR',            'temperature_ir'),
             ('Tilt',                      'tilt'),
             ('Voltage',                   'voltage'),
             ('Voltage/Current',           'voltage_current'),
            ]

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
 To test a {0} Brick you need to have :ref:`Brick Daemon <brickd>` and
 :ref:`Brick Viewer <brickv>` installed. Brick Daemon acts as a proxy between
 the USB interface of the Bricks and the API bindings. Brick Viewer connects
 to Brick Daemon. It helps to figure out basic information about the connected
 Bricks and Bricklets and allows to test them.
""",
'de':
""".. |test_intro| replace::
 Um einen {0} Brick testen zu können müssen zuerst :ref:`Brick Daemon
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
 "{0} Brick" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Brick" auftauchen. Wähle diesen Tab
 aus.
"""
}

brick_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_brick_programming_interface>`
 section for the API of the {1} Brick and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{0}_brick_programming_interface>` listet die
 API des {1} Bricks und Beispiele in verschiedenen Programmiersprachen auf.
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

Below you can see an exploded assembly drawing of the {0} Bricklet case:
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

Im folgenden befindet sich eine Explosionszeichnung des {0} Bricklet-Gehäuse:
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
 To test a {0} Bricklet you need to have :ref:`Brick Daemon <brickd>` and
 :ref:`Brick Viewer <brickv>` installed. Brick Daemon acts as a proxy between
 the USB interface of the Bricks and the API bindings. Brick Viewer connects
 to Brick Daemon. It helps to figure out basic information about the connected
 Bricks and Bricklets and allows to test them.
""",
'de':
""".. |test_intro| replace::
 Um ein {0} Bricklet testen zu können müssen zuerst :ref:`Brick Daemon
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
 Connect the {0} Bricklet to a :ref:`Brick <primer_bricks>`
 with a Bricklet Cable
""",
'de':
""".. |test_connect| replace::
 Als nächstes muss das {0} Bricklet mittels eines Bricklet Kabels mit
 einem :ref:`Brick <primer_bricks>` verbunden werden
"""
}

bricklet_test_tab = {
'en':
""".. |test_tab| replace::
 If you connect the Brick to the PC over USB, you should see a new tab named
 "{0} Bricklet" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Bricklet" auftauchen.
 Wähle diesen Tab aus.
"""
}

bricklet_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_bricklet_programming_interface>`
 section for the API of the {1} Bricklet and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{0}_bricklet_programming_interface>` listet
 die API des {1} Bricklets und Beispiele in verschiedenen
 Programmiersprachen auf.
"""
}

def make_ipcon_substitutions():
    substitutions = ''
    substitutions += ipcon_common[lang]

    return substitutions

def make_brick_substitutions(brick):
    substitutions = ''
    substitutions += brick_test_intro[lang].format(brick[0]) + '\n'
    substitutions += brick_test_tab[lang].format(brick[0]) + '\n'
    substitutions += brick_test_pi_ref[lang].format(brick[1], brick[0])

    return substitutions

def make_bricklet_substitutions(bricklet):
    substitutions = ''
    substitutions += '>>>substitutions\n'
    substitutions += bricklet_test_intro[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_connect[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_tab[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_pi_ref[lang].format(bricklet[1], bricklet[0]) + '\n'
    substitutions += bricklet_case_hint[lang] + '\n'
    substitutions += '<<<substitutions\n'
    substitutions += bricklet_case_steps[lang].format(bricklet[0]) + '\n'

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

    write_if_changed(os.path.join(path, 'source', 'Software', 'IPConnection_Common.substitutions'), make_ipcon_substitutions())

    for brick in bricks:
        name = brick[0].replace(' ', '_').replace('-', '').replace('/', '_').replace('2.0', 'V2')

        print 'Generating {0}_Brick.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick.substitutions'), make_brick_substitutions(brick))

    for bricklet in bricklets:
        name = bricklet[0].replace(' ', '_').replace('-', '').replace('/', '_').replace('2.0', 'V2')

        print 'Generating {0}.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '.substitutions'), make_bricklet_substitutions(bricklet))

if __name__ == "__main__":
    generate(os.getcwd())
