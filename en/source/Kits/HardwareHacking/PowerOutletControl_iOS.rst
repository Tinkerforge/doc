
.. |name| replace:: iOS
.. |ref_CALLBACK_ENUMERATE| replace:: :c:data:`IPCON_CALLBACK_ENUMERATE`
.. |ref_connect| replace:: :c:func:`ipcon_connect`
.. |connect| replace:: ``ipcon_connect()``
.. |set_monoflop| replace:: ``industrial_quad_relay_set_monoflop(&relay, selection_mask, 15, 500)``
.. |ref_get_identity| replace:: :c:func:`industrial_quad_relay_get_identity` function
.. |async_helper| replace:: a `Grand Central Dispatch (GCD) <https://en.wikipedia.org/wiki/Grand_Central_Dispatch>`__ block

.. include:: PowerOutletControl.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_power_outlet_control_ios:

Control Remote Mains Switches using iOS
=======================================

.. include:: iOSCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: PowerOutletControl.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

The complete Xcode project can be downloaded `here
<https://github.com/Tinkerforge/hardware-hacking/tree/master/power_outlet_control_smart_phone/ios>`__.


Goals
-----

.. include:: PowerOutletControl.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Creating the GUI
------------------------

After creating a new "iOS Single View Application" named "Power Outlet Control"
in Xcode we start with creating the GUI in the Interface Builder:

.. image:: /Images/Kits/hardware_hacking_power_outlet_control_ios_gui.jpg
   :scale: 100 %
   :alt: App GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_power_outlet_control_ios_gui.jpg

Three "Text Field" elements allow to enter the host, port and UID of the
Industrial Quad Relay Bricklet. The next element is a "Button" to connect and
disconnect. Below that go four "Button" elements to trigger the different
switches on the remote control. The final element is an "Indicator" (not
visible on screenshot) that will be used to indicate that a connection attempt
is in progress.

Now the GUI layout is finished. To access the GUI components in the Objective-C
code we add an ``IBOutlet`` for each GUI element to the ``ViewController``
interface:

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        IBOutlet UITextField *hostTextField;
        IBOutlet UITextField *portTextField;
        IBOutlet UITextField *uidTextField;
        IBOutlet UIButton *connectButton;
        IBOutlet UIButton *aOnButton;
        IBOutlet UIButton *aOffButton;
        IBOutlet UIButton *bOnButton;
        IBOutlet UIButton *bOffButton;
        IBOutlet UIActivityIndicatorView *indicator;
    }

    @property (nonatomic, retain) UITextField *hostTextField;
    @property (nonatomic, retain) UITextField *portTextField;
    @property (nonatomic, retain) UITextField *uidTextField;
    @property (nonatomic, retain) UIButton *connectButton;
    @property (nonatomic, retain) UIButton *aOnButton;
    @property (nonatomic, retain) UIButton *aOffButton;
    @property (nonatomic, retain) UIButton *bOnButton;
    @property (nonatomic, retain) UIButton *bOffButton;
    @property (nonatomic, retain) UIActivityIndicatorView *indicator;

    @end

Now these ``IBOutlet`` have to be connected to the GUI elements in the
Interface Builder. To do this create a new "Referencing Outlet" between each
GUI element and its corresponding ``IBOutlet`` of the "File's Owner" using the
context menu of each GUI element.

Finally we add a ``IBAction`` method for each "Button" element to the
``ViewController`` interface, to be able to react on button presses:

.. code-block:: objc

    @interface ViewController : UIViewController
    {
        // [...]
    }

    // [...]

    - (IBAction)connectPressed:(id)sender;
    - (IBAction)aOnPressed:(id)sender;
    - (IBAction)aOffPressed:(id)sender;
    - (IBAction)bOnPressed:(id)sender;
    - (IBAction)bOffPressed:(id)sender;

    @end

To have this methods called correctly they have to be connected to the
"Touch Up Inside" events of the corresponding buttons in the Interface Builder.
This is similar to the way ``IBOutlet`` are connected to their GUI elements.


Step 2: Discover Bricks and Bricklets
-------------------------------------

This step is similar to step 1 in the
:ref:`Read out Smoke Detectors using C
<starter_kit_hardware_hacking_smoke_detector_c_step1>` project.
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

Before the GCD block (``^{ ... }``) is queued for execution the host, port
and UID configuration from the GUI elements is stores in local variables. This
is necessary, because this information is needed inside ``^{ ... }``, but
accessing the GUI elements is not allowed inside ``^{ ... }`` as it will be
executed on a different thread. Now the ``^{ ... }`` can create an
``IPConnection`` and ``IndustrialQuadRelay`` object and call the
``ipcon_connect()`` function.

Finally, ``connect`` should called when the connect button is clicked:

.. code-block:: objc

    - (IBAction)connectPressed:(id)sender
    {
        [self connect];
    }

|step2_finish|


Step 3: Triggering Switches
---------------------------

|step3_intro|

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

To trigger the switch "A ON" of the remote control the relays 0 and 2 of the
Industrial Quad Relay Bricklet have to be closed. This is represented by the
selection mask ``(1 << 0) | (1 << 2)``.

The ``IBAction`` methods for each of the four trigger buttons call the
``industrial_quad_relay_set_monoflop()`` function of the Industrial Quad Relay
Bricklet with the corresponding selection mask to trigger a switch on the
remote control. These calls are wrapped into GCD blocks to avoid doing a
potentially blocking operation on the main thread of the app:

.. code-block:: objc

    - (IBAction)aOnPressed:(id)sender
    {
        dispatch_async(queue, ^{
            industrial_quad_relay_set_monoflop(&relay, (1 << 0) | (1 << 2), 15, 500);
        });
    }

    - (IBAction)aOffPressed:(id)sender
    {
        dispatch_async(queue, ^{
            industrial_quad_relay_set_monoflop(&relay, (1 << 0) | (1 << 3), 15, 500);
        });
    }

    - (IBAction)bOnPressed:(id)sender
    {
        dispatch_async(queue, ^{
            industrial_quad_relay_set_monoflop(&relay, (1 << 1) | (1 << 2), 15, 500);
        });
    }

    - (IBAction)bOffPressed:(id)sender
    {
        dispatch_async(queue, ^{
            industrial_quad_relay_set_monoflop(&relay, (1 << 1) | (1 << 3), 15, 500);
        });
    }

|step3_monoflop|

|step3_finish1|

|step3_finish2|


Step 4: More GUI logic
----------------------

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

After the connection got established a GCD block is added to the main queue to
change the text on the connect button. Blocks in the main queue are executed
by the main thread that is allowed to interact with the GUI.

We also add a new ``connected`` variable to the ``ViewController`` to keep
track of the GUI state. Then the ``IBAction`` method for the connect button
knows when to call ``connect`` and when to call the new ``disconnect`` method:

.. code-block:: objc

    - (IBAction)connectPressed:(id)sender
    {
        if (!connected) {
            [self connect];
        } else {
            [self disconnect];
        }
    }

We don't want to call the :c:func:`ipcon_disconnect` function directly, because
it might take a moment and block the GUI during that period of time. Instead
``ipcon_disconnect()`` will be called from another GCD block, so it will run
in the background and the GUI stays responsive:

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

Once the connection is closed the title on the connect button is changed and the
``connected`` variable is set to ``NO`` so a new connection will be establish
if the connect button is clicked again.

|step4_disabled_gui|

The ``connect`` and the ``disconnect`` methods are extended to disable and
enable the GUI elements according to the current connection state:

.. code-block:: objc

    - (void)viewDidLoad
    {
        // [...]

        aOnButton.enabled = NO;
        aOffButton.enabled = NO;
        bOnButton.enabled = NO;
        bOffButton.enabled = NO;
    }

.. code-block:: objc

    - (void)connect
    {
        // [...]

        hostTextField.enabled = NO;
        portTextField.enabled = NO;
        uidTextField.enabled = NO;
        connectButton.enabled = NO;
        aOnButton.enabled = NO;
        aOffButton.enabled = NO;
        bOnButton.enabled = NO;
        bOffButton.enabled = NO;

        dispatch_async(queue, ^{
            // [...]

            dispatch_async(dispatch_get_main_queue(), ^{
                // [...]

                connectButton.enabled = YES;
                aOnButton.enabled = YES;
                aOffButton.enabled = YES;
                bOnButton.enabled = YES;
                bOffButton.enabled = YES;
            });
        });
    }

.. code-block:: objc

    - (void)disconnect
    {
        connectButton.enabled = NO;
        aOnButton.enabled = NO;
        aOffButton.enabled = NO;
        bOnButton.enabled = NO;
        bOffButton.enabled = NO;

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


Step 5: Error Handling and Reporting
------------------------------------

We will use similar principals as in step 4 of the
:ref:`Read out Smoke Detectors using C
<starter_kit_hardware_hacking_smoke_detector_c_step4>` project, but with some
changes to make it work in a GUI program.

We can't just use ``printf()`` for error reporting because there is no console
window in an app. Instead dialog boxes are used.

The ``connect`` method has to validate the user input before using it. An
``UIAlertView`` is used to report possible problems:

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

Also the progress indicator is made visible to indicate that a connection
attempt is in progress:

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

The call of ``ipcon_connect()`` might fail, because host or port might be
wrong. We need to check for this and report an error in that case:

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

In both cases an ``UIAlertView`` with ``delegate`` set to ``self`` is used to
report the error. The delegate has to conform to the ``UIAlertViewDelegate``
protocol by implementing a ``clickedButtonAtIndex`` method, which is called if
the user clicks a button the the ``UIAlertView``. We can use this to realize
a retry button. If the retry button (``buttonIndex == 1``) is clicked then
``connect`` is called again, otherwise the connection attempt is aborted and
the GUI is changed to the correct state:

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


Step 6: Persistent Configuration and State
------------------------------------------

The app doesn't store its configuration yet. iOS provides the ``NSUserDefaults``
class to take care of this. Two new methods are added to the ``ViewController``
to save and restore the current state:

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

Then the ``AppDelegate`` is changed to call them in the right places:

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


Step 7: Everything put together
-------------------------------

|step7_intro|

|step7_together| (Downloads: `ViewController.h
<https://raw.githubusercontent.com/Tinkerforge/hardware-hacking/master/power_outlet_control_smart_phone/ios/PowerOutletControl/ViewController.h>`__,
`ViewController.m
<https://raw.githubusercontent.com/Tinkerforge/hardware-hacking/master/power_outlet_control_smart_phone/ios/PowerOutletControl/ViewController.m>`__):

.. literalinclude:: ../../../../../hardware-hacking/power_outlet_control_smart_phone/ios/PowerOutletControl/ViewController.h
 :language: objc
 :tab-width: 4

.. literalinclude:: ../../../../../hardware-hacking/power_outlet_control_smart_phone/ios/PowerOutletControl/ViewController.m
 :language: guess
 :tab-width: 4
