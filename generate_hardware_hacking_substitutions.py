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

android_common_intro = {
'en':
"""
>>>intro
For this project we are assuming, that you have the `Android SDK
<http://developer.android.com/sdk/index.html>`__ set up and that you have a
rudimentary understanding of the Java language.

If you are totally new to Java itself you should start
`here <http://docs.oracle.com/javase/tutorial/>`__.
If you are new to the Tinkerforge API, you should start
:ref:`here <api_bindings_java_android>`.
<<<intro
""",
'de':
"""
>>>intro
Für diese Projekt setzen wir voraus, dass das `Android SDK
<http://developer.android.com/sdk/index.html>`__
eingerichtet ist und ein grundsätzliches Verständnis der Java Programmiersprache
vorhanden ist.

Falls dies nicht der Fall ist sollte
`hier <http://docs.oracle.com/javase/tutorial/>`__ begonnen werden. Informationen
über die Tinkerforge API sind dann :ref:`hier <api_bindings_java>` zu finden.
<<<intro
"""
}

windows_phone_common_intro = {
'en':
"""
>>>intro
For this project we are assuming, that you have the `Windows Phone SDK
<https://dev.windowsphone.com/en-us/downloadsdk>`__ set up and that you have a
rudimentary understanding of the C# language.

If you are totally new to C# itself you should start
`here <http://csharp.net-tutorials.com/>`__.
If you are new to the Tinkerforge API, you should start
:ref:`here <api_bindings_csharp_windows_phone>`.
<<<intro
""",
'de':
"""
>>>intro
Für diese Projekt setzen wir voraus, dass das `Windows Phone SDK
<https://dev.windowsphone.com/de-de/downloadsdk>`__
eingerichtet ist und ein grundsätzliches Verständnis der C# Programmiersprache
vorhanden ist.

Falls dies nicht der Fall ist sollte
`hier <http://csharp.net-tutorials.com/>`__ begonnen werden. Informationen
über die Tinkerforge API sind dann :ref:`hier <api_bindings_csharp>` zu finden.
<<<intro
"""
}


remote_switch_example_line = {
'en':
""":ref:`{0} <starter_kit_hardware_hacking_remote_switch_{1}>`""",
'de':
""":ref:`{0} <starter_kit_hardware_hacking_remote_switch_{1}>`"""
}

remote_switch_examples = {
'en':
"""
.. |remote_switch_examples| replace:: {0}
""",
'de':
"""
.. |remote_switch_examples| replace:: {0}
"""
}

remote_switch_examples_toctree_line = {
'en':
"""   RemoteSwitch_{0}""",
'de':
"""   RemoteSwitch_{0}""",
}

remote_switch_examples_toctree = {
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

remote_switch_example_download_line = {
'en':
"""`{0} <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch/{1}>`__""",
'de':
"""`{0} <https://github.com/Tinkerforge/hardware-hacking/tree/master/remote_switch/{1}>`__"""
}

remote_switch_example_downloads = {
'en':
"""
.. |remote_switch_examples_download| replace:: {0}
""",
'de':
"""
.. |remote_switch_examples_download| replace:: {0}
"""
}

remote_switch_intro = {
'en':
"""
>>>intro
We are also assuming that you have the remote control connected to an
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
as described :ref:`here <starter_kit_hardware_hacking_remote_switch_hardware_setup>`.
<<<intro
""",
'de':
"""
>>>intro
Wir setzen weiterhin voraus, dass die Fernbedienung mit einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
verbunden wurde wie :ref:`hier <starter_kit_hardware_hacking_remote_switch_hardware_setup>`
beschrieben.
<<<intro
"""
}

remote_switch_goals = {
'en':
"""
>>>goals
The goal of this little project is to give an idea how the relays of the
Industrial Quad Relay Bricklets have to be switched to turn the mains
switches on/off.

The following code uses |ref_set_monoflop| to trigger a button
press on the remote control. A monoflop will set a new state (relay open or close)
and hold it for a given time (1.5s in the example code). After this time
the previous state is restored. This approach simulates a button click that
takes 1.5s (1500ms).

According to the :ref:`hardware setup section
<starter_kit_hardware_hacking_remote_switch_hardware_setup_relay_matrix>` the
inputs of the remote control should be connected as follows:

====== =====
Signal Relay
====== =====
A      0
B      1
ON     2
OFF    3
====== =====

To trigger the switch "A ON" of the remote control the relays 0 and 2 have to be
closed. This is represented by the selection mask |bitmask_02|.

So the monoflop function should be called with this selection mask and
a time of 1500ms to simulate a button press of "A ON". See the following
source code for a minimal example.
<<<goals
""",
'de':
"""
>>>goals
Das Ziel dieses kleinen Projekts ist es, eine Vorstellung darüber zu vermitteln
wie die Relais des Industrial Quad Relay Bricklets geschaltet werden müssen,
damit die Funksteckdosen an- und ausgeschaltet werden können.

Der folgende Quelltext benutzt |ref_set_monoflop| um eine Knopfdruck
auf der Fernbedienung auszulösen. Ein Monoflop setzt einen neuen Zustand
(Relais offen oder geschlossen) und hält diesen für eine bestimmte Zeit
(1,5s im Beispielquelltext). Nach dieser Zeit wird der vorheriger Zustand
wiederhergestellt. Dieses Ansatz simuliert einen Knopfdruck der für 1,5s
(1500ms) anhält.

Gemäße der :ref:`Hardware-Aufbau Beschreibung
<starter_kit_hardware_hacking_remote_switch_hardware_setup_relay_matrix>`
ist die Fernbedienung wie folgt mit den Relais verbunden:

====== ======
Signal Relais
====== ======
A      0
B      1
ON     2
OFF    3
====== ======

Um "A ON" auf der Fernbedienung auszulösen müssen also die Relais 0 und 2
geschlossen werden. Dies wird durch die Bitmaske |bitmask_02| repräsentiert.

Die Monoflop-Funktion kann also mit dieser Bitmaske und einer
Zeit von 1500ms aufgerufen werden um einen Knopfdruck von "A ON"
zu simulieren. Im Folgenden wird dies in einem minimalen Beispielquelltext
dargestellt.
<<<goals
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
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` as
described :ref:`here <starter_kit_hardware_hacking_smoke_detector_hardware_setup>`.
<<<intro
""",
'de':
"""
>>>intro
Wir setzen weiterhin voraus, dass ein passender Rauchmelder mit einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` verbunden
wurde wie :ref:`hier <starter_kit_hardware_hacking_smoke_detector_hardware_setup>`
beschrieben.
<<<intro
"""
}

smoke_detector_goals = {
'en':
"""
>>>goals
We are setting the following goal for this project:

* Read out the alarm status of a smoke detector
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
 During the enumeration we want to configure the Industrial Digital In 4 Bricklet.
 Doing this during the enumeration ensures that the Bricklet gets reconfigured
 if the Brick was disconnected or there was a power loss.

.. |step2_enumerate| replace::
 The configurations should be performed on first startup
 (|ENUMERATION_TYPE_CONNECTED|) as well as whenever the enumeration is
 triggered externally by us (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_config| replace::
 We configure the Industrial Digital In 4 Bricklet to call the |cb_interrupt|
 callback if a change of the voltage level on any input pin is detected. The
 debounce period is set to 10s (10000ms) to avoid being spammed with callbacks.
 Interrupt detection is enabled for all inputs (15 = 0b1111).

.. |step2_put_together| replace::
 Step 2 put together:

.. |step3_intro| replace::
 Now we need to react on the alarm signal of the smoke detector. But we want to
 react only if the LED is turned on, not if it is turn off. This is done by
 checking |value_mask| for being ``> 0``. In that case there is a voltage
 applied to at least one input, therefore, the LED is on.

.. |step3_complete| replace::
 That's it. If we would copy these three steps together in one file and
 execute it, we would have a working program that reads the alarm status of a
 hacked smoke detector and reacts on its alarm signal!

.. |step3_suggestions| replace::
 Currently the program just outputs a warning. There are several ways to extend
 this. For example, the program could send an email or a text message to notify
 someone about the alarm.

.. |step3_robust1| replace::
 However, we do not meet all of our goals yet. The program is not yet
 robust enough. What happens if it can't connect on startup? What happens if
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
 Während des Enumerierungsprozesses soll das Industrial Digital In 4 Bricklet
 konfiguriert werden. Dadurch ist sichergestellt, dass es neu konfiguriert wird
 nach einem Verbindungsabbruch oder einer Unterbrechung der Stromversorgung.

.. |step2_enumerate| replace::
 Die Konfiguration soll beim ersten Start (|ENUMERATION_TYPE_CONNECTED|)
 durchgeführt werden und auch bei jedem extern ausgelösten Enumerate
 (|ENUMERATION_TYPE_AVAILABLE|):

.. |step2_config| replace::
 Das Industrial Digital In 4 Bricklet wird so eingestellt, dass es die
 |cb_interrupt| Callback-Funktion aufruft wenn sich die Spannung an einem
 der Eingänge verändert. Die Entprellperiode wird auf 10s (10000ms) gestellt,
 um zu vermeiden zu viele Callback zu erhalten. Interrupterkennung wird für
 alle Eingänge aktiviert (15 = 0b1111).

.. |step2_put_together| replace::
 Schritt 2 zusammengefügt:

.. |step3_intro| replace::
 Jetzt müssen wir noch auf das Alarmsignal des Rauchmelders reagieren. Es soll
 aber nur auf das Einschalten der LED reagiert werden, nicht auf das
 Ausschalten. Dazu wird |value_mask| auf ``> 0`` geprüft, in diesem Fall liegt
 an mindesten einem Eingang eine Spannung an, sprich die LED leuchtet.

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
 und es wird solange versucht ein Enumerate zu starten bis auch dies geklappt
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
 Das gesamte Programm für den gehackten Rauchmelder
"""
}


garage_control_intro = {
'en':
"""
>>>intro
We are also assuming that you have a remote control connected to
an :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` as
described :ref:`here <starter_kit_hardware_hacking_garage_control_hardware_setup>`.
<<<intro
""",
'de':
"""
>>>intro
Wir setzen weiterhin voraus, dass die Fernbedienung mit einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` verbunden
wurde wie :ref:`hier <starter_kit_hardware_hacking_garage_control_hardware_setup>`
beschrieben.
<<<intro
"""
}

garage_control_goals = {
'en':
"""
>>>goals
In this project we will create a simple |name| app that resembles the
functionality of the actual remote control.
<<<goals
""",
'de':
"""
>>>goals
In diesem Projekt werden wir eine einfach |name| App entwickeln, die die
Funktionalität der eigentlichen Fernbedienung nachbildet.
<<<goals
"""
}

garage_control_steps = {
'en': """
.. |step2_discover_by_uid| replace::
 We apply some changes to make it work in a GUI program and instead of using the
 |ref_CALLBACK_ENUMERATE| to discover the Industrial Quad Relay Bricklet its UID
 has to be specified. This approach allows to pick the correct Industrial Quad
 Relay Bricklet even if multiple are connected to the same host at once.

.. |step2_async| replace::
 We don't want to call the |ref_connect| method directly, because it might take
 a moment and block the GUI during that period of time. Instead |connect| will
 be called by a |async_helper|, so it will run in the background and the GUI
 stays responsive:

.. |step2_finish| replace::
 Host, port and UID can now be configured and a click on the connect button
 establishes the connection.

.. |step3_intro| replace::
 The connection is established and the Industrial Quad Relay Bricklet is found
 but there is no logic yet to trigger the switch on the remote control if the
 trigger button is clicked.

.. |step3_monoflop| replace::
 The call to |set_monoflop| closes the first relay for 1.5s then opens it again.

.. |step3_finish1| replace::
 That's it. If we would copy these three steps together in one file, we would
 have a working app that allows a smart phone to control a garage door opener
 using its hacked remote control!

.. |step3_finish2| replace::
 We don't have a disconnect button yet and the trigger button can be clicked
 before the connection is established. We need some more GUI logic!

.. |step4_intro| replace::
 There is no button to close the connection again after it got established. The
 connect button could do this. When the connection is established it should
 allow to disconnect it again:

.. |step4_disabled_gui| replace::
 Finally, the user should not be able to change the content of the text fields
 during the time the connection gets established and the trigger button should
 not be clickable if there is no connection.

.. |step4_robust1| replace::
 But the program is not yet robust enough. What happens if can't connect? What
 happens if there is no Industrial Quad Relay Bricklet with the given UID?

.. |step4_robust2| replace::
 What we need is error handling!

.. |step5_connect_result1| replace::
 SUCCESS: The connection got established and an Industrial Quad Relay Bricklet
 with the given UID was found.

.. |step5_connect_result2| replace::
 NO_CONNECTION: The connection could not be established.

.. |step5_connect_result3| replace::
 NO_DEVICE: The connection got established but there was no Industrial Quad
 Relay Bricklet with the given UID.

.. |step5_check_identity| replace::
 The |ref_get_identity| method is used to check that the device for the given
 UID really is an Industrial Quad Relay Bricklet. If this is not the case then
 the connection gets closed:

.. |step5_success| replace::
 In case the connection attempt was successful the original logic stays the same:

.. |step5_finish| replace::
 Now the app can connect to an configurable host and port and trigger a button
 on the remote control of your garage door opener using an Industrial Quad Relay
 Bricklet.

.. |step6_finish| replace::
 Now the configuration and state is stored persistent across a restart of the app.

.. |step7_intro| replace::
 That's it! We are done with the app for our hacked garage door opener remote
 control.

.. |step7_together| replace::
 Now all of the above put together
""",
'de': """
.. |step2_discover_by_uid| replace::
 Einige Änderungen sind notwendig damit es in einem GUI Programm funktioniert.
 Statt dem |ref_CALLBACK_ENUMERATE| zum Erkennen des Industrial Quad Relay
 Bricklets verwenden muss dessen UID angegeben werden. Dieser Ansatz erlaubt es
 gezielt ein Industrial Quad Relay Bricklet auszuwählen, selbst wenn mehrere am
 gleichen Host angeschlossen sind.

.. |step2_async| replace::
 Die |ref_connect| Methode soll nicht direkt aufgerufen werden, da dies einen
 Moment dauern kann und in dieser Zeit die GUI nicht auf den Benutzer reagieren
 könnte. Daher wird |connect| aus einem |async_helper| aufgerufen werden, so
 dass es im Hintergrund ausgeführt und die GUI nicht blockiert wird:

.. |step2_finish| replace::
 Host, Port und UID können jetzt eingestellt werden und ein Klick auf den
 Connect Knopf stellt die Verbindung her.

.. |step3_intro| replace::
 Die Verbindung ist hergestellt und das Industrial Quad Relay Bricklet wurde
 gefunden, aber es fehlt noch die Logik um einen Taster auf der Fernbedienung
 auszulösen wenn der Knopf geklickt wurde.

.. |step3_monoflop| replace::
 Der Aufruf von |set_monoflop| schließt das erste Relais für 1,5s und öffnet
 es dann wieder.

.. |step3_finish1| replace::
 Das ist es. Wenn wir diese drei Schritte zusammen in eine Datei kopieren, dann
 hätten wir jetzt eine funktionierende App, die es ermöglicht vom Smartphone
 aus den Garagentoröffner mittels dessen gehackter Fernbedienung zu steuern.

.. |step3_finish2| replace::
 Es fehlt noch ein Disconnect-Knopf und der Trigger-Knopf kann auch geklickt
 werden obwohl keine Verbindung besteht. Es fehlt also noch etwas mehr
 GUI-Logik!

.. |step4_intro| replace::
 Es gibt noch keinen Knopf um die Verbindung wieder zu trennen nachdem sie
 aufgebaut wurde. Der Connect-Knopf könnte dies tun. Wenn die Verbindung
 aufgebaut ist sollte er bei einem Klick die Verbindung wieder trennen:

.. |step4_disabled_gui| replace::
 Außerdem sollte der Benutzer nicht den Inhalt der Eingabefelder ändern können
 solange die Verbindung aufgebaut wird oder besteht und der Trigger-Knopf sollte
 nicht klickbar sein wenn keine Verbindung besteht.

.. |step4_robust1| replace::
 Das Programm ist noch nicht robust genug. Was passiert wenn die Verbindung
 nicht hergestellt werden kann? Was passiert wenn kein Industrial Quad Relay
 Bricklet mit passender UID gefunden werden kann?

.. |step4_robust2| replace::
 Wir brauchen noch Fehlerbehandlung!

.. |step5_connect_result1| replace::
 SUCCESS: Die Verbindung wurde hergestellt und ein Industrial Quad Relay
 Bricklet mit passender UID wurde gefunden.

.. |step5_connect_result2| replace::
 NO_CONNECTION: Die Verbindung konnte nicht hergestellt werden.

.. |step5_connect_result3| replace::
 NO_DEVICE: Die Verbindung wurde hergestellt, aber es wurde kein Industrial Quad
 Relay Bricklet mit passender UID gefunden.

.. |step5_check_identity| replace::
 Mit der |ref_get_identity| Methode wird überprüft, ob die angegebene UID
 wirklich zu einem Industrial Quad Relay Bricklet gehört. Falls das nicht der
 Fall ist wird die Verbindung getrennt:

.. |step5_success| replace::
 Im Falle, dass die Verbindung erfolgreich war bleibt die ursprüngliche Logik
 bestehen:

.. |step5_finish| replace::
 Die App kann sich zum eingestellten Host und Port verbinden und einen Taster
 auf der Fernbedienung des Garagentoröffners mittels eines Industrial
 Quad Relay Bricklets betätigen.

.. |step6_finish| replace::
 Jetzt wird die Konfiguration und der Zustand dauerhaft. auch über einen
 Neustart der App hinweg, gespeichert.

.. |step7_intro| replace::
 Das ist es! Die App für die gehackte Fernbedienung des Garangentoröffners ist
 fertig.

.. |step7_together| replace::
 Das Hauptprogramm in einem Stück
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


    example_lines = []
    for binding in bindings:
        example_lines.append(remote_switch_example_line[lang].format(binding[1], binding[2]))

    substitutions += remote_switch_examples[lang].format(', '.join(example_lines))

    examples_toctree_lines = []
    for binding in bindings:
        examples_toctree_lines.append(remote_switch_examples_toctree_line[lang].format(binding[3]))

    substitutions += remote_switch_examples_toctree[lang].format('\n'.join(examples_toctree_lines))

    example_download_lines = []
    for binding in bindings:
        example_download_lines.append(remote_switch_example_download_line[lang].format(binding[1], binding[2]))

    substitutions += remote_switch_example_downloads[lang].format(', '.join(example_download_lines))

    return substitutions

def make_common_substitutions(binding):
    substitutions = ''
    substitutions += common_intro[lang].format(binding[1], binding[2], binding[4][lang])

    return substitutions

def make_android_common_substitutions():
    substitutions = ''
    substitutions += android_common_intro[lang]

    return substitutions

def make_windows_phone_common_substitutions():
    substitutions = ''
    substitutions += windows_phone_common_intro[lang]

    return substitutions


def make_smoke_detector_substitutions():
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


def make_remote_switch_substitutions():
    substitutions = ''
    substitutions += remote_switch_intro[lang] + '\n'
    substitutions += remote_switch_goals[lang] + '\n'

    return substitutions

def make_remote_switch_toctree():
    toctree_lines = []
    for binding in bindings:
        toctree_lines.append(remote_switch_examples_toctree_line[lang].format(binding[3]))

    return remote_switch_examples_toctree[lang].format('\n'.join(toctree_lines))


def make_garage_control_substitutions():
    substitutions = ''
    substitutions += garage_control_intro[lang] + '\n'
    substitutions += garage_control_goals[lang] + '\n'
    substitutions += '>>>substitutions\n'
    substitutions += garage_control_steps[lang] + '\n'
    substitutions += '<<<substitutions\n'

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

    print 'Generating HardwareHacking.substitutions'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'HardwareHacking.substitutions'), make_substitutions())

    for binding in bindings:
        print 'Generating {0}Common.substitutions (HardwareHacking)'.format(binding[3])
        write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', binding[3] + 'Common.substitutions'), make_common_substitutions(binding))

    print 'Generating AndroidCommon.substitutions (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'AndroidCommon.substitutions'), make_android_common_substitutions())

    print 'Generating WindowsPhoneCommon.substitutions (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'WindowsPhoneCommon.substitutions'), make_windows_phone_common_substitutions())

    print 'Generating SmokeDetector.substitutions (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'SmokeDetector.substitutions'), make_smoke_detector_substitutions())
    print 'Generating SmokeDetector.toctree (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'SmokeDetector.toctree'), make_smoke_detector_toctree())

    print 'Generating RemoteSwitch.substitutions (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'RemoteSwitch.substitutions'), make_remote_switch_substitutions())
    print 'Generating RemoteSwitch.toctree (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'RemoteSwitch.toctree'), make_remote_switch_toctree())

    print 'Generating GarageControl.substitutions (HardwareHacking)'
    write_if_changed(os.path.join(path, 'source', 'Kits', 'HardwareHacking', 'GarageControl.substitutions'), make_garage_control_substitutions())

if __name__ == "__main__":
    generate(os.getcwd())
