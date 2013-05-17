#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

                            # display,            example,              uri,      filename, getting started
bindings = [('C/C++',             'C',                  'c',      'C',      {'en': 'http://www.cprogramming.com/',
                                                                             'de': 'http://www.cprogramming.com/'}), # http://www.c-howto.de/
            ('C#',                'C#',                 'csharp', 'CSharp', {'en': 'http://csharp.net-tutorials.com/',
                                                                             'de': 'http://csharp.net-tutorials.com/'}),
            ('Delphi',            'Delphi',             'delphi', 'Delphi', {'en': 'http://www.delphibasics.co.uk/',
                                                                             'de': 'http://www.delphi-treff.de/tutorials/grundlagen/'}),
            ('Java',              'Java',               'java',   'Java',   {'en': 'http://docs.oracle.com/javase/tutorial/',
                                                                             'de': 'http://docs.oracle.com/javase/tutorial/'}), # http://openbook.galileocomputing.de/javainsel/
            ('PHP',               'PHP',                'php',    'PHP',    {'en': 'http://www.php.net/manual/en/getting-started.php',
                                                                             'de': 'http://www.php.net/manual/de/getting-started.php'}),
            ('Python',            'Python',             'python', 'Python', {'en': 'http://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
                                                                             'de': 'http://www.python.org/about/gettingstarted/'}),
            ('Ruby',              'Ruby',               'ruby',   'Ruby',   {'en': 'http://www.ruby-lang.org/en/documentation/quickstart/',
                                                                             'de': 'http://www.ruby-lang.org/de/documentation/quickstart/'}),
            ('Visual Basic .NET', 'Visual Basic .NET',  'vbnet',  'VBNET',  {'en': 'http://howtostartprogramming.com/vb-net/',
                                                                             'de': 'http://howtostartprogramming.com/vb-net/'})] # http://openbook.galileocomputing.de/vb_net/index.htm

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

common_intro = {
'en':
"""
>>>intro
For this project we are assuming, that you have a {0} development environment
set up and that you have a rudimentary understanding of the {0} language.

If you are totally new to {0} itself you should start `here <{2}>`__. If you are
new to the Tinkerforge API, you should start :ref:`here <api_bindings_{1}>`.
<<<intro
""",
'de':
"""
>>>intro
Für diese Projekt setzen wir voraus, dass eine {0} Entwicklungsumgebung
eingerichtet ist und ein grundsätzliches Verständnis der {0} Programmiersprache
vorhanden ist.

Falls dies nicht der Fall ist sollte `hier <{2}>`__ begonnen werden. Informationen
über die Tinkerforge API sind dann :ref:`hier <api_bindings_{1}>` zu finden.
<<<intro
"""
}

smoke_detector_example_line = {
'en':
""":ref:`{0} <starter_kit_hardware_hacking_smoke_detector_{1}>`""",
'de':
""":ref:`{0} <starter_kit_hardware_hacking_smoke_detector_{1}>`"""
}

smoke_detector_examples = {
'en':
"""
.. |smoke_detector_examples| replace:: {0}
""",
'de':
"""
.. |smoke_detector_examples| replace:: {0}
"""
}

smoke_detector_examples_toctree_line = {
'en':
"""   SmokeDetector_{0}""",
'de':
"""   SmokeDetector_{0}""",
}

smoke_detector_examples_toctree = {
'en':
""".. toctree::
   :hidden:

{0}
""",
'de':
""".. toctree::
   :hidden:

{0}
"""
}

smoke_detector_example_download_line = {
'en':
"""`{0} <https://github.com/Tinkerforge/hardware-hacking/tree/master/smoke_detector/{1}>`__""",
'de':
"""`{0} <https://github.com/Tinkerforge/hardware-hacking/tree/master/smoke_detector/{1}>`__"""
}

smoke_detector_example_downloads = {
'en':
"""
.. |smoke_detector_examples_download| replace:: {0}
""",
'de':
"""
.. |smoke_detector_examples_download| replace:: {0}
"""
}

smoke_detector_intro = {
'en':
"""
>>>intro
We are also assuming that you have a smoke detector connected to an
:ref:`Analog in Bricklet <analog_in_bricklet>` as described :ref:`here
<starter_kit_hardware_hacking_smoke_detector>`.
<<<intro
""",
'de':
"""
>>>intro
Wir setzen weiterhin voraus, dass ein passender Rauchmelder mit einem
:ref:`Analog in Bricklet <analog_in_bricklet>` verbunden wurde wie :ref:`hier
<starter_kit_hardware_hacking_smoke_detector>` beschrieben.
<<<intro
"""
}

smoke_detector_goals = {
'en':
"""
>>>goals
We are setting the following goal for this project:

* Readout the alarm status of a smoke detector
* and react on its alarm signal.

Since this project will likely run 24/7, we will also make sure
that the application is as robust towards external influences as possible.
The application should still work when

* Bricklets are exchanged (i.e. we don't rely on UIDs),
* Brick Daemon isn't running or is restarted,
* WIFI Extension is out of range or
* Brick is restarted (power loss or accidental USB removal).

In the following we will show step-by-step how this can be achieved.
<<<goals
""",
'de':
"""
>>>goals
Wir setzen uns folgendes Ziel für dieses Projekt:

* Alarmstatus eines Rauchmelders auslesen
* und auf dessen Alarmsignal reagieren.

Da dieses Projekt wahrscheinlich 24/7 laufen wird, wollen wir sicherstellen,
dass das Programm möglichst robust gegen externe Einflüsse ist. Das Programm
sollte weiterhin funktionieren falls

* Bricklets ausgetauscht werden (z.B. verwenden wir keine fixen UIDs),
* Brick Daemon läuft nicht oder wird neu gestartet,
* WIFI Extension ist außer Reichweite oder
* Brick wurde neu gestartet (Stromausfall oder USB getrennt).

Im Folgenden werden wir Schritt für Schritt zeigen wie diese Ziele erreicht
werden können.
<<<goals
"""
}

smoke_detector_steps = {
'en':
"""
.. |step1_start_off| replace::
 To start off, we need to define where our program should connect to:

.. |step1_ip_address| replace::
 If the WIFI Extension is used or if the Brick Daemon is
 running on a different PC, you have to exchange "localhost" with the
 IP address or hostname of the WIFI Extension or PC.

.. |step1_register_callbacks| replace::
 When the program is started, we need to register the |ref_CALLBACK_ENUMERATE|
 |callback| and the |ref_CALLBACK_CONNECTED| |callback| and trigger a first
 enumerate:

.. |step1_enumerate_callback| replace::
 The enumerate callback is triggered if a Brick gets connected over USB or if
 the |ref_enumerate| function is called. This allows to discover the Bricks and
 Bricklets in a stack without knowing their types or UIDs beforehand.

.. |step1_connected_callback| replace::
 The connected callback is triggered if the connection to the WIFI Extension or
 to the Brick Daemon got established. In this callback we need to trigger the
 enumerate again, if the reason is an auto reconnect:

.. |step1_auto_reconnect_callback| replace::
 An auto reconnect means, that the connection to the WIFI Extension or to the
 Brick Daemon was lost and could subsequently be established again. In this
 case the Bricklets may have lost their configurations and we have to
 reconfigure them. Since the configuration is done during the
 enumeration process (see below), we have to trigger another enumeration.

.. |step1_put_together| replace::
 Step 1 put together:

.. |step2_intro| replace::
 During the enumeration we want to configure the Analog In Bricklet. Doing this
 during the enumeration ensures that the Bricklet gets reconfigured if the Brick
 was disconnected or there was a power loss.

.. |step2_enumerate| replace::
 The configurations should be performed on first startup
 (|ENUMERATION_TYPE_CONNECTED|) as well as whenever the enumeration is
 triggered externally by us (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_config1| replace::
 We configure the Analog In Bricklet to call the |cb_voltage_reached| callback
 if the measured voltage reaches 1.2V:

.. |step2_config2| replace::
 The measurement range is set to 0V - 6.05V because we only need to detect if
 the voltage reaches 1.2V. The debounce period is set to 10s (10000ms) to avoid
 being spammed with callbacks.
 
.. |step2_config3| replace::
 This values comes from our tests with the `ELRO FA20RF/2
 <http://www.elro.eu/en/products/cat/flamingo/security1/smoke-detectors/wireless-interconnectable-smoke-detectors>`__
 wireless smoke detector set that we use as an example. You might need to use different
 values depending on your particular device.

.. |step2_put_together| replace::
 Step 2 put together:

.. |step3_intro| replace::
 Now we need to react on the alarm signal of the smoke detector:

.. |step3_complete| replace::
 That's it. If we would copy these three steps together in one file and
 execute it, we would have a working program that reads the alarm status of a
 smoke detector and reacts on its alarm signal!

.. |step3_suggestions| replace::
 Currently the program just outputs a warning. There are several ways to extend
 this. For example, the program could send an email or a text message to notify
 someone about the alarm.

.. |step3_robust1| replace::
 However, we do not meet all of our goals yet. The program is not yet
 robust enough. What happens if can't connect on startup? What happens if
 the enumerate after an auto reconnect doesn't work?

.. |step3_robust2| replace::
 What we need is error handling!

.. |step4_intro1| replace::
 On startup, we need to try to connect until the connection works:

.. |step4_intro2| replace::
 and we need to try enumerating until the message goes through:

.. |step4_sleep_in_c| replace::
 There is no portable sleep function in C. On Windows ``windows.h`` declares
 a ``Sleep`` function that takes the duration in milliseconds. On POSIX
 systems such as Linux and Mac OS X there is a ``sleep`` function declared
 in ``unistd.h`` that takes the duration in seconds.

.. |step4_connect_afterwards| replace::
 With these changes it is now possible to first start the program and
 connect the Master Brick afterwards.

.. |step4_initialization| replace::
 We also have to deal with errors during the initialization:

.. |step4_logging1| replace::
 Additionally we added some logging. With the logging we can later find out
 what exactly caused a potential problem.

.. |step4_logging2| replace::
 For example, if we connect to the Master Brick via Wi-Fi and we have
 regular auto reconnects, it likely means that the Wi-Fi connection is not
 very stable.

.. |step5_intro| replace::
 That's it! We are already done with our hacked smoke detector and all of the
 goals should be met.

.. |step5_put_together| replace::
 Now all of the above put together
""",
'de':
"""
.. |step1_start_off| replace::
 Als Erstes legen wir fest wohin unser Programm sich verbinden soll:

.. |step1_ip_address| replace::
 Falls eine WIFI Extension verwendet wird, oder der Brick Daemon auf einem
 anderen PC läuft, dann muss "localhost" durch die IP Adresse oder den Hostnamen
 der WIFI Extension oder des anderen PCs ersetzt werden.

.. |step1_register_callbacks| replace::
 Nach dem Start des Programms müssen der |ref_CALLBACK_ENUMERATE| |callback|
 und der |ref_CALLBACK_CONNECTED| |callback| registriert und ein erstes
 Enumerate ausgelöst werden:

.. |step1_enumerate_callback| replace::
 Der Enumerate Callback wird ausgelöst wenn ein Brick per USB angeschlossen wird
 oder wenn die |ref_enumerate| Funktion aufgerufen wird. Dies ermöglicht es die
 Bricks und Bricklets im Stapel zu erkennen ohne im Voraus ihre UIDs kennen zu
 müssen.

.. |step1_connected_callback| replace::
 Der Connected Callback wird ausgelöst wenn die Verbindung zur WIFI Extension
 oder zum Brick Daemon hergestellt wurde. In diesem Callback muss wiederum ein
 Enumerate angestoßen werden, wenn es sich um ein Auto-Reconnect handelt:

.. |step1_auto_reconnect_callback| replace::
 Ein Auto-Reconnect bedeutet, dass die Verbindung zur WIFI Extension oder zum
 Brick Daemon verloren gegangen ist und automatisch wiederhergestellt werden
 konnte. In diesem Fall kann es sein, dass die Bricklets ihre Konfiguration
 verloren haben und wir sie neu konfigurieren müssen. Da die Konfiguration
 beim Enumerate (siehe unten) durchgeführt wird, lösen wir einfach noch ein
 Enumerate aus.

.. |step1_put_together| replace::
 Schritt 1 zusammengefügt:

.. |step2_intro| replace::
 Während des Enumerierungsprozesse soll das Analog In Bricklet konfiguriert
 werden. Dadurch ist sichergestellt, dass es neu konfiguriert wird nach
 einem Verbindungsabbruch oder einer Unterbrechung der Stromversorgung.

.. |step2_enumerate| replace::
 Die Konfiguration soll beim ersten Start (|ENUMERATION_TYPE_CONNECTED|)
 durchgeführt werden und auch bei jedem extern ausgelösen Enumerate
 (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_config1| replace::
 Das Analog In Bricklet wird so eingestellt, dass es die |cb_voltage_reached|
 Callback-Funktion aufruft wenn die gemessene Spannung 1,2V erreicht:

.. |step2_config2| replace::
 Der Messbereich wird auf 0V - 6,05V gestellt, dies ausreicht reicht aus um
 Erreichen der 1,2V zu erkennen. Die Entprellperiode wird auf 10s (10000ms)
 gestellt, um zu vermeiden zu viele Callback zu erhalten.
 
.. |step2_config3| replace::
 Diese Werte stammen aus unseren Tests mit dem `ELRO FA20RF/2
 <http://www.elro.eu/de/produkte/cat/flamingo/sicherheit1/rauchmelder/schnurlos-verknuepfbarer-rauchmelder>`__
 Funk-Rauchmelderset das hier als Beispiel verwendet wird. Abhängig vom jeweilig
 verwendeten Gerät können diese Werte abweichen.

.. |step2_put_together| replace::
 Schritt 2 zusammengefügt:

.. |step3_intro| replace::
 Jetzt müssen wir noch auf das Alarmsignal des Rauchmelders reagieren:

.. |step3_complete| replace::
 Das ist es. Wenn wir diese drei Schritte zusammen in eine Datei kopieren und
 ausführen, dann hätten wir jetzt eine funktionierendes Programm, das den
 Alarmstatus eines Rauchmelders ausließt und auf dessen Alarmsignal reagiert.

.. |step3_suggestions| replace::
 In der jetzigen Form gibt das Programm nur eine Meldung aus. Dies kann auf
 verschiedene Weise verbessert werden. Zum Beispiel könnte das Programm jemanden
 per E-Mail oder SMS über den Alarm informieren.

.. |step3_robust1| replace::
 Wie dem auch sei, wir haben noch nicht alle Ziele erreicht. Das Programm ist
 noch nicht robust genug. Was passiert wenn die Verbindung beim Start des
 Programms nicht hergestellt werden kann, oder wenn das Enumerate nach einem
 Auto-Reconnect nicht funktioniert?

.. |step3_robust2| replace::
 Wir brauchen noch Fehlerbehandlung!

.. |step4_intro1| replace::
 Beim Start des Programms versuchen wir solange die Verbindung herzustellen,
 bis es klappt:

.. |step4_intro2| replace::
 und es wird solange versucht ein Enumerate zu starten bis auch dis geklappt
 hat:

.. |step4_sleep_in_c| replace::
 Es gibt keine portable Sleep Funktion in C. Auf Windows deklariert `windows.h``
 eine ``Sleep`` Funktion die die Wartedauer in Millisekunden übergeben bekommt.
 Auf POSIX Systemen wie Linux und Mac OS X gibt es eine ``sleep`` Funktion
 deklariert in ``unistd.h`` die die Wartedauer in Sekunden übergeben bekommt.

.. |step4_connect_afterwards| replace::
 Mit diesen Änderungen kann das Programm schon gestartet werden bevor der
 Master Brick angeschlossen ist.

.. |step4_initialization| replace::
 Es müssen auch noch mögliche Fehler während des Enumerierungsprozesses
 behandelt werden:

.. |step4_logging1| replace::
 Zusätzlich wollen wir noch ein paar Logausgaben einfügen. Diese ermöglichen es
 später herauszufinden was ein mögliches Problem ausgelöst hat.

.. |step4_logging2| replace::
 Zum Beispiel, wenn der Master Brick über WLAN angebunden ist und häufig
 Auto-Reconnects auftreten, dann ist wahrscheinlich die WLAN Verbindung nicht
 sehr stabil.

.. |step5_intro| replace::
 Jetzt sind alle für gesteckten Ziele für unseren gehackten Rauchmelder erreicht.

.. |step5_put_together| replace::
 Das gesamte Programm für die Wetterstation
"""
}

def make_substitutions():
    substitutions = ''

    formated_binding_names = []
    for binding in bindings:
        formated_binding_names.append(binding_name[lang].format(binding[0], binding[2]))

    substitutions += binding_names[lang].format(', '.join(formated_binding_names)) + '\n'

    example_lines = []
    for binding in bindings:
        example_lines.append(smoke_detector_example_line[lang].format(binding[1], binding[2]))

    substitutions += smoke_detector_examples[lang].format(', '.join(example_lines))

    examples_toctree_lines = []
    for binding in bindings:
        examples_toctree_lines.append(smoke_detector_examples_toctree_line[lang].format(binding[3]))

    substitutions += smoke_detector_examples_toctree[lang].format('\n'.join(examples_toctree_lines))

    example_download_lines = []
    for binding in bindings:
        example_download_lines.append(smoke_detector_example_download_line[lang].format(binding[1], binding[2]))

    substitutions += smoke_detector_example_downloads[lang].format(', '.join(example_download_lines))

    return substitutions

def make_common_substitutions(binding):
    substitutions = ''
    substitutions += common_intro[lang].format(binding[1], binding[2], binding[4][lang])

    return substitutions

def make_smoke_detector_substitutions(binding):
    substitutions = ''
    substitutions += smoke_detector_intro[lang] + '\n'
    substitutions += smoke_detector_goals[lang] + '\n'
    substitutions += '>>>substitutions\n'
    substitutions += smoke_detector_steps[lang] + '\n'
    substitutions += '<<<substitutions\n'

    return substitutions

def make_smoke_detector_toctree():
    toctree_lines = []
    for binding in bindings:
        toctree_lines.append(smoke_detector_examples_toctree_line[lang].format(binding[3]))

    return smoke_detector_examples_toctree[lang].format('\n'.join(toctree_lines))

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        print 'Wrong working directory'
        sys.exit(1)

    print 'Generating HardwareHacking.substitutions'
    file(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'HardwareHacking.substitutions'), 'wb').write(make_substitutions())

    for binding in bindings:
        print 'Generating {0}Common.substitutions (HardwareHacking)'.format(binding[3])
        file(os.path.join(path, 'source', 'Kits', 'HardwareHacking', binding[3] + 'Common.substitutions'), 'wb').write(make_common_substitutions(binding))

    for binding in bindings:
        print 'Generating SmokeDetector_{0}.substitutions (HardwareHacking)'.format(binding[3])
        file(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'SmokeDetector_' + binding[3] + '.substitutions'), 'wb').write(make_smoke_detector_substitutions(binding))

    print 'Generating SmokeDetector.toctree (HardwareHacking)'
    file(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'SmokeDetector.toctree'), 'wb').write(make_smoke_detector_toctree())

if __name__ == "__main__":
    generate(os.getcwd())
