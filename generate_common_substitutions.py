#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

          # display,        uri
bricks = [('DC Brick',      'dc'),
          ('Debug Brick',   'debug'),
          ('IMU Brick',     'imu'),
          ('IMU Brick 2.0', 'imu_v2'),
          ('Master Brick',  'master'),
          ('RED Brick',     'red'),
          ('Servo Brick',   'servo'),
          ('Stepper Brick', 'stepper')]

             # display,                             uri
bricklets = [('AC Current Bricklet',                'ac_current'),
             ('Accelerometer Bricklet',             'accelerometer'),
             ('Ambient Light Bricklet',             'ambient_light'),
             ('Ambient Light Bricklet 2.0',         'ambient_light_v2'),
             ('Analog In Bricklet',                 'analog_in'),
             ('Analog In Bricklet 2.0',             'analog_in_v2'),
             ('Analog Out Bricklet',                'analog_out'),
             ('Analog Out Bricklet 2.0',            'analog_in_v2'),
             ('Barometer Bricklet',                 'barometer'),
             ('Breakout Bricklet',                  'breakout'),
             ('Color Bricklet',                     'color'),
             ('Current12 Bricklet',                 'current12'),
             ('Current25 Bricklet',                 'current25'),
             ('Distance IR Bricklet',               'distance_ir'),
             ('Distance US Bricklet',               'distance_us'),
             ('Dual Button Bricklet',               'dual_button'),
             ('Dual Relay Bricklet',                'dual_relay'),
             ('Gas Detector Bricklet',              'gas_detector'),
             ('GPS Bricklet',                       'gps'),
             ('Hall Effect Bricklet',               'hall_effect'),
             ('Heart Rate Bricklet',                'heart_rate'),
             ('Humidity Bricklet',                  'humidity'),
             ('Industrial Analog Out Bricklet',     'industrial_analog_out'),
             ('Industrial Digital In 4 Bricklet',   'industrial_digital_in_4'),
             ('Industrial Digital Out 4 Bricklet',  'industrial_digital_out_4'),
             ('Industrial Dual 0-20mA Bricklet',    'industrial_dual_0_20ma'),
             ('Industrial Dual Analog In Bricklet', 'industrial_dual_analog_in'),
             ('Industrial Quad Relay Bricklet',     'industrial_quad_relay'),
             ('IO-16 Bricklet',                     'io16'),
             ('IO-4 Bricklet',                      'io4'),
             ('Joystick Bricklet',                  'joystick'),
             ('Laser Range Finder Bricklet',        'laser_range_finder'),
             ('LCD 16x2 Bricklet',                  'lcd_16x2'),
             ('LCD 20x4 Bricklet',                  'lcd_20x4'),
             ('LED Strip Bricklet',                 'led_strip'),
             ('Line Bricklet',                      'line'),
             ('Linear Poti Bricklet',               'linear_poti'),
             ('Load Cell Bricklet',                 'load_cell'),
             ('Moisture Bricklet',                  'moisture'),
             ('Motion Detector Bricklet',           'motion_detector'),
             ('Multi Touch Bricklet',               'multi_touch'),
             ('NFC/RFID Bricklet',                  'nfc_rfid'),
             ('Piezo Buzzer Bricklet',              'piezo_buzzer'),
             ('Piezo Speaker Bricklet',             'piezo_speaker'),
             ('PTC Bricklet',                       'ptc'),
             ('Remote Switch Bricklet',             'remote_switch'),
             ('Rotary Encoder Bricklet',            'rotary_encoder'),
             ('Rotary Poti Bricklet',               'rotary_poti'),
             ('RS232 Bricklet',                     'rs232'),
             ('Segment Display 4x7 Bricklet',       'segment_display_4x7'),
             ('Solid State Relay Bricklet',         'solid_state_relay'),
             ('Sound Intensity Bricklet',           'sound_intensity'),
             ('Temperature Bricklet',               'temperature'),
             ('Temperature IR Bricklet',            'temperature_ir'),
             ('Tilt Bricklet',                      'tilt'),
             ('Voltage Bricklet',                   'voltage'),
             ('Voltage/Current Bricklet',           'voltage_current'),
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
 To test a {0} you need to have :ref:`Brick Daemon <brickd>` and
 :ref:`Brick Viewer <brickv>` installed. Brick Daemon acts as a proxy between
 the USB interface of the Bricks and the API bindings. Brick Viewer connects
 to Brick Daemon. It helps to figure out basic information about the connected
 Bricks and Bricklets and allows to test them.
""",
'de':
""".. |test_intro| replace::
 Um einen {0} testen zu können müssen zuerst :ref:`Brick Daemon
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
 See the :ref:`Programming Interface <{1}_brick_programming_interface>`
 section for the API of the {0} and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{1}_brick_programming_interface>` listet die
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
 Um ein {0} testen zu können müssen zuerst :ref:`Brick Daemon
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
 See the :ref:`Programming Interface <{1}_bricklet_programming_interface>`
 section for the API of the {0} and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{1}_bricklet_programming_interface>` listet
 die API des {0} und Beispiele in verschiedenen
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
    substitutions += brick_test_pi_ref[lang].format(brick[0], brick[1])

    return substitutions

def make_bricklet_substitutions(bricklet):
    substitutions = ''
    substitutions += '>>>substitutions\n'
    substitutions += bricklet_test_intro[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_connect[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_tab[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_pi_ref[lang].format(bricklet[0], bricklet[1]) + '\n'
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
        name = ' '.join([a for a in brick[0].split(' ') if a != 'Brick']).replace(' ', '_').replace('-', '').replace('/', '_').replace('2.0', 'V2')

        print 'Generating {0}_Brick.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick.substitutions'), make_brick_substitutions(brick))

    for bricklet in bricklets:
        name = ' '.join([a for a in bricklet[0].split(' ') if a != 'Bricklet']).replace(' ', '_').replace('-', '').replace('/', '_').replace('2.0', 'V2')

        print 'Generating {0}.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '.substitutions'), make_bricklet_substitutions(bricklet))

if __name__ == "__main__":
    generate(os.getcwd())
