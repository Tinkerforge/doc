
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Garagentor mit iOS fernsteuern

.. |name| replace:: iOS
.. |ref_CALLBACK_ENUMERATE| replace:: :c:data:`IPCON_CALLBACK_ENUMERATE`
.. |ref_connect| replace:: :c:func:`ipcon_connect`
.. |connect| replace:: ``ipcon_connect()``
.. |set_monoflop| replace:: ``industrial_quad_relay_set_monoflop(&relay, 1 << 0, 15, 500)``
.. |ref_get_identity| replace:: :c:func:`industrial_quad_relay_get_identity` Funktion
.. |async_helper| replace:: einem `Grand Central Dispatch (GCD) <http://de.wikipedia.org/wiki/Grand_Central_Dispatch>`__ Block

.. include:: GarageControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_garage_control_ios:

Garagentor mit iOS fernsteuern
==============================

.. include:: iOSCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: GarageControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Das vollständige Xcode Projekt kann `hier
<https://github.com/Tinkerforge/hardware-hacking/tree/master/garage_control_smart_phone/ios>`__
heruntergeladen werden. Eine Demo-App basierend auf diesem Projekt steht im
`App Store <https://itunes.apple.com/en/app/garage-control/id739047995?&mt=8>`__
zur Verfügung.


Ziele
-----

.. include:: GarageControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Die GUI erstellen
----------------------------

Nach dem Erstellen einer neuen "iOS Single View Application" namens
"Garage Control" in Xcode beginnen wir mit der Erstellung der GUI im Interface
Builder:

.. image:: /Images/Kits/hardware_hacking_garage_control_ios_gui.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_control_ios_gui.jpg

Drei "Text Field" Elemente ermöglichen die Eingabe von Host, Port und UID des
Industrial Quad Relay Bricklets. Das nächste Element ist ein "Button" für den
Aufbau und das Trennen der Verbindung. Dann folgt ein "Button" Element für das
Auslösen eines Tastendrucks auf der gehackten Fernbedienung. Unterhalb der
Knöpfe folgt ein "Indicator" Element (nicht sichtbar im Screenshot), das einen
laufenden Verbindungsversuch anzeigen wird.

Damit ist das Layout des GUIs fertig. Um auf die GUI Elemente von Objective-C
aus zugreifen zu können fügen wir ein ``IBOutlet`` für jedes GUI Element dem
``ViewController`` Interface hinzu:

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        IBOutlet UITextField *hostTextField;
        IBOutlet UITextField *portTextField;
        IBOutlet UITextField *uidTextField;
        IBOutlet UIButton *connectButton;
        IBOutlet UIButton *triggerButton;
        IBOutlet UIActivityIndicatorView *indicator;
    }

    @property (nonatomic, retain) UITextField *hostTextField;
    @property (nonatomic, retain) UITextField *portTextField;
    @property (nonatomic, retain) UITextField *uidTextField;
    @property (nonatomic, retain) UIButton *connectButton;
    @property (nonatomic, retain) UIButton *triggerButton;
    @property (nonatomic, retain) UIActivityIndicatorView *indicator;

    @end

Diese ``IBOutlet`` müssen jetzt im Interface Builder mit den GUI Elementen
verbunden werden. Dazu über das jeweilige Kontextmenu der GUI Elemente einen
neuen "Referencing Outlet" zwischen jedem GUI Element und dem entsprechenden
``IBOutlet`` des "File's Owner" erzeugen.

Zuletzt fügen wir noch eine ``IBAction`` Methode für jedes "Button" Element zum
``ViewController`` Interface hinzu, um auf das Drücken der Knöpfe reagieren zu
können:

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        // [...]
    }

    // [...]

    - (IBAction)connectPressed:(id)sender;
    - (IBAction)triggerPressed:(id)sender;

    @end

Damit diese Methoden auch aufgerufen werden müssen sie im Interface Builder mit
den "Touch Up Inside" Events der entsprechenden Knöpfe verbunden werden. Dies
ist ähnlich zur der Art und Weise wie die ``IBOutlet`` mit ihren GUI Elementen
verbunden sind.


Schritt 2: Bricks und Bricklets erkennen
----------------------------------------

Dieser Schritt ist ähnlich zu Schritt 1 des
:ref:`Rauchmelder mit C auslesen
<starter_kit_hardware_hacking_smoke_detector_c_step1>` Projekts.
|step2_discover_by_uid|

|step2_async|

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        // [...]

        dispatch_queue_t queue;
        IPConnection ipcon;
        IndustrialQuadRelay relay;
    }

.. code-block:: objc

    - (void)viewDidLoad
    {
        // [...]

        queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    }

    - (void)connect
    {
        NSString *host = hostTextField.text;
        NSString *port = portTextField.text;
        NSString *uid = uidTextField.text;

        dispatch_async(queue, ^{
            ipcon_create(&ipcon);
            industrial_quad_relay_create(&relay, [uid UTF8String], &ipcon);
            ipcon_connect(&ipcon, [host UTF8String], [port intValue]);
        });
    }

Bevor der GCD Block (``^{ ... }``) zur Ausführung gebracht werden kann müssen
Host, Port und UID Konfiguration von den GUI Elementen in lokale Variablen
zwischengespeichert werden. Dies ist notwendig, da diese Information innerhalb
von ``^{ ... }`` benötigt werden, der Zugriff auf GUI Element innerhalb von
``^{ ... }`` aber nicht erlaubt ist, da der Block auf einem anderen Thread
ausgeführt werden wird. Jetzt kann ``^{ ... }`` die ``IPConnection`` und
``IndustrialQuadRelay`` Objekte erzeugen und ``ipcon_connect()`` aufrufen.

Schlussendlich soll ``connect`` aufgerufen werden, wenn der Connect-Knopf
geklickt wird:

.. code-block:: objc

    - (IBAction)connectPressed:(id)sender
    {
        [self connect];
    }

|step2_finish|


Schritt 3: Taster auslösen
--------------------------

|step3_intro|

Die ``IBAction`` Methode des Trigger-Knopf ruft die
``industrial_quad_relay_set_monoflop()`` Funktion des Industrial Quad Relay
Bricklets auf, um einen Taster auf der Fernbedienung zu drücken. Dieser Aufruf
ist in einen GCD Block verpackt, um zu vermeiden etwas potentiell blockierendes
im Haupt-Thread der App zu tun:

.. code-block:: objc

    - (IBAction)triggerPressed:(id)sender
    {
        dispatch_async(queue, ^{
            industrial_quad_relay_set_monoflop(&relay, (1 << 0), (1 << 0), 1500);
        });
    }

|step3_monoflop|

|step3_finish1|

|step3_finish2|


Schritt 4: Weitere GUI-Logik
----------------------------

|step4_intro|

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        // [...]

        BOOL connected;
    }

.. code-block:: objc

    - (void)viewDidLoad
    {
        // [...]

        connected = NO;
    }

    - (void)connect
    {
        // [...]

        dispatch_async(queue, ^{
            // [...]

            dispatch_async(dispatch_get_main_queue(), ^{
                [connectButton setTitle:@"Disconnect" forState: UIControlStateNormal];

                connected = YES;
            });
        });
    }

Nachdem die Verbindung hergestellt wurde wird ein GCD Block zur Haupt-Queue
hinzugefügt in dem der Text des Connect-Knopfes geändert wird. Blöcke in der
Haupt-Queue werden durch den Haupt-Thread ausgeführt, dieser darf mit dem GUI
interagieren.

Es wird auch einen neue ``connected`` Variable zum ``ViewController``
hinzugefügt, um den Zustand des GUI zu speichern. Dadurch kann die ``IBAction``
des Connect-Knopfes dann entscheiden ob ``connect`` oder ``disconnect``
aufgerufen werden sollen:

.. code-block:: objc

    - (IBAction)connectPressed:(id)sender
    {
        if (!connected) {
            [self connect];
        } else {
            [self disconnect];
        }
    }

Die :c:func:`ipcon_disconnect` Funktion soll nicht direkt aufgerufen werden,
da diese einen Moment dauern kann und in dieser Zeit die GUI blockiert ist.
Stattdessen wird ``ipcon_disconnect()`` in einem GCD Block aufgerufen, wodurch
es im Hintergrund ausgeführt und die GUI nicht blockiert wird:

.. code-block:: objc

    - (void)disconnect
    {
        dispatch_async(queue, ^{
            ipcon_disconnect(&ipcon);
            industrial_quad_relay_destroy(&relay);
            ipcon_destroy(&ipcon);

            dispatch_async(dispatch_get_main_queue(), ^{
                [connectButton setTitle:@"Connect" forState: UIControlStateNormal];

                connected = NO;
            });
        });
    }

Sobald die Verbindung getrennt wurde wird der Title des Connect-Knopf geändert
und die ``connected`` Variable wird auf ``NO`` gesetzt, so dass die Verbindung
neu aufbaut wird wenn der Connect-Knopf das nächste mal geklickt wird.

|step4_disabled_gui|

Die ``connect`` und die ``disconnect`` Methode werden so erweitert, dass sie
die GUI Elemente abhängig von dem aktuellen Zustand der Verbindung aktivieren
oder deaktivieren:

.. code-block:: objc

    - (void)viewDidLoad
    {
        // [...]

        triggerButton.enabled = NO;
    }

.. code-block:: objc

    - (void)connect
    {
        // [...]

        hostTextField.enabled = NO;
        portTextField.enabled = NO;
        uidTextField.enabled = NO;
        connectButton.enabled = NO;
        triggerButton.enabled = NO;

        dispatch_async(queue, ^{
            // [...]

            dispatch_async(dispatch_get_main_queue(), ^{
                // [...]

                connectButton.enabled = YES;
                triggerButton.enabled = YES;
            });
        });
    }

.. code-block:: objc

    - (void)disconnect
    {
        connectButton.enabled = NO;
        triggerButton.enabled = NO;

        dispatch_async(queue, ^{
            // [...]

            dispatch_async(dispatch_get_main_queue(), ^{
                // [...]

                connectButton.enabled = YES;
                hostTextField.enabled = YES;
                portTextField.enabled = YES;
                uidTextField.enabled = YES;
            });
        });
    }

|step4_robust1|

|step4_robust2|


Schritt 5: Fehlerbehandlung und Reporting
-----------------------------------------

Es werden die gleichen Konzepte wie in Schritt 4 des
:ref:`Rauchmelder mit C auslesen
<starter_kit_hardware_hacking_smoke_detector_c_step4>` Projekts angewandt,
allerdings mit Abwandlungen damit sie in einem GUI Programm funktionieren.

Wir können nicht einfach ``printf()`` für Fehlermeldungen verwenden, da dies
ein GUI Programm ist und kein Konsolenfenster hat. Stattdessen werden
Dialogboxen verwendet.

Die ``connect`` Methode muss die Benutzereingaben validieren bevor sie
verwendet werden. Mittels ``UIAlertView`` werden mögliche Probleme gemeldet:

.. code-block:: objc

    - (void)connect
    {
        NSString *host = hostTextField.text;
        NSString *port = portTextField.text;
        NSString *uid = uidTextField.text;

        if ([host length] == 0 || [port length] == 0 || [uid length] == 0) {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error" message:@"Host/Port/UID cannot be empty"
                                                      delegate:nil cancelButtonTitle:nil otherButtonTitles:@"Okay", nil];
            [alert show];
            return;
        }

        int portNumber = [port intValue];
        NSString *reformatedPort = [NSString stringWithFormat:@"%d", portNumber];

        if (portNumber < 1 || portNumber > 65535 || ![port isEqualToString:reformatedPort]) {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error" message:@"Port number is invalid"
                                                      delegate:nil cancelButtonTitle:nil otherButtonTitles:@"Okay", nil];
            [alert show];
            return;
        }

        // [...]
    }

Das "Indicator" Element wird eingeblendet um auf den laufenden
Verbindungsversuch hinzuweisen:

.. code-block:: objc

    - (void)viewDidLoad
    {
        // [...]

        [indicator setHidden:YES];
    }

    - (void)connect
    {
        // [...]

        [indicator setHidden:NO];
        [indicator startAnimating];

        // [...]

        dispatch_async(queue, ^{
            // [...]

            dispatch_async(dispatch_get_main_queue(), ^{
                [indicator setHidden:YES];

                // [...]
            });
        });
    }

Der Aufruf von ``ipcon_connect()`` kann fehlschlagen, z.B. weil Host oder Port
nicht stimmen. In diesem Fall muss ein Fehler gemeldet werden:

.. code-block:: objc

    - (void)connect
    {
        // [...]

        dispatch_async(queue, ^{
            ipcon_create(&ipcon);
            industrial_quad_relay_create(&relay, [uid UTF8String], &ipcon);

            if (ipcon_connect(&ipcon, [host UTF8String], portNumber) < 0) {
                industrial_quad_relay_destroy(&relay);
                ipcon_destroy(&ipcon);

                dispatch_async(dispatch_get_main_queue(), ^{
                    [indicator setHidden:YES];

                    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error"
                                                              message:[NSString stringWithFormat:@"Could not connect to %@:%d", host, portNumber]
                                                              delegate:self cancelButtonTitle:@"Cancel" otherButtonTitles:@"Retry", nil];
                    [alert show];
                });

                return;
            }

            // [...]
        });
    }

|step5_check_identity|

.. code-block:: objc

    - (void)connect
    {
        // [...]

        dispatch_async(queue, ^{
            // [...]

            char uid_[8];
            char connected_uid[8];
            char position;
            uint8_t hardware_version[3];
            uint8_t firmware_version[3];
            uint16_t device_identifier;

            if (industrial_quad_relay_get_identity(&relay, uid_, connected_uid, &position,
                                                   hardware_version, firmware_version, &device_identifier) < 0 ||
                device_identifier != INDUSTRIAL_QUAD_RELAY_DEVICE_IDENTIFIER) {
                dispatch_async(dispatch_get_main_queue(), ^{
                    [indicator setHidden:YES];

                    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error"
                                                              message:[NSString stringWithFormat:@"Could not find Industrial Quad Relay Bricklet [%@]", uid]
                                                              delegate:self cancelButtonTitle:@"Cancel" otherButtonTitles:@"Retry", nil];
                    [alert show];
                });

                return;
            }

            // [...]
        });
    }

In beiden Fällen wird eine ``UIAlertView`` mit ``delegate`` auf ``self``
gesetzt verwendet, um den Fehler zu melden. Der Delegate muss dem
``UIAlertViewDelegate`` Protokoll entsprechen und eine ``clickedButtonAtIndex``
Methode implementieren, welche aufgerufen wird wenn ein Knopf der
``UIAlertView`` geklickt wird. Dies können wir verwenden um einen Retry-Knopf
zu realisieren. Wird der Retry-Knopf (``buttonIndex == 1``) geklickt dann wird
``connect`` erneut aufgerufen, andernfalls wird der Verbindungsversuch
aufgegeben sichergestellt, dass sich das GUI im richtigen Zustand befindet:

.. code-block:: objc

    - (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex
    {
        if (buttonIndex == 1) {
            [self connect];
        } else {
            [connectButton setTitle:@"Connect" forState: UIControlStateNormal];

            connectButton.enabled = YES;
            hostTextField.enabled = YES;
            portTextField.enabled = YES;
            uidTextField.enabled = YES;
        }
    }

|step5_finish|


Schritt 6: Konfiguration und Zustand speichern
----------------------------------------------

Die App speichert die Konfiguration noch nicht. iOS bietet dafür die
``NSUserDefaults`` Klasse an. Zwei neue Methoden werden dem ``ViewController``
hinzugefügt um die Konfiguration zu speichern und wieder zu laden:

.. code-block:: objc

    - (void)saveState
    {
        [[NSUserDefaults standardUserDefaults] setObject:hostTextField.text forKey:@"host"];
        [[NSUserDefaults standardUserDefaults] setObject:portTextField.text forKey:@"port"];
        [[NSUserDefaults standardUserDefaults] setObject:uidTextField.text forKey:@"uid"];
        [[NSUserDefaults standardUserDefaults] setBool:connected forKey:@"connected"];
    }

.. code-block:: objc

    - (void)restoreState
    {
        NSString *host = [[NSUserDefaults standardUserDefaults] stringForKey:@"host"];
        NSString *port = [[NSUserDefaults standardUserDefaults] stringForKey:@"port"];
        NSString *uid = [[NSUserDefaults standardUserDefaults] stringForKey:@"uid"];

        if (host != nil) {
            hostTextField.text = host;
        }

        if (port != nil) {
            portTextField.text = port;
        }

        if (uid != nil) {
            uidTextField.text = uid;
        }

        if ([[NSUserDefaults standardUserDefaults] boolForKey:@"connected"] && !connected) {
            [self connect];
        }
    }

Dann wird noch der ``AppDelegate`` so geändert, dass die neuen Methoden zum
richtigen Zeitpunkt aufgerufen werden:

.. code-block:: objc

    - (void)applicationDidEnterBackground:(UIApplication *)application
    {
        [self.viewController saveState];
    }

.. code-block:: objc

    - (void)applicationDidBecomeActive:(UIApplication *)application
    {
        [self.viewController restoreState];
    }

|step6_finish|


Schritt 7: Alles zusammen
-------------------------

|step7_intro|

|step7_together| (Downloads: `ViewController.h
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/ios/GarageControl/ViewController.h>`__,
`ViewController.m
<https://raw.github.com/Tinkerforge/hardware-hacking/master/garage_control_smart_phone/ios/GarageControl/ViewController.m>`__):

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/ios/GarageControl/ViewController.h
 :language: objc
 :tab-width: 4

.. literalinclude:: ../../../../../hardware-hacking/garage_control_smart_phone/ios/GarageControl/ViewController.m
 :language: guess
 :tab-width: 4
