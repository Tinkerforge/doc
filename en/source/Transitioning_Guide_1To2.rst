.. _transition_1to2:

Transitioning from Protocol 1.0 to Protocol 2.0
===============================================

Update Tools and Firmwares
--------------------------

Updating to Protocol 2.0 is quite easy. Start by installing the :ref:`newest
version <downloads_tools>` of the Brick Daemon and the Brick Viewer.

After that you should start by updating all of your Bricks, you can update
them one by one as described :ref:`here <brickv_flash_firmware>`.

To update the Bricklets, there is an automated process. You can fill up one
of your updated Bricks with Bricklets. Click on "Updates" in the Brick
Viewer and use the first tab. There you should see all of your connected
Bricks with the corresponding connected Bricklets. Bricklets that are out
of date are marked red. You can update all Bricklets at once by clicking
on "Auto-Update All Bricklets".

.. image:: /Images/Screenshots/bricklet_auto_update.jpg
   :scale: 100 %
   :alt: Bricklet auto update feature of the Brick Viewer
   :align: center
   :target: _images/Screenshots/bricklet_auto_update.jpg

If the auto update does not work, you can of course still update the
Bricklets individually by using the normal
:ref:`Bricklet updating process <brickv_flash_plugin>`.

In the end, everything should have a version that starts with "2". 

There should also have been a guide on how to update Bricks and Bricklets
with your shipment. If you didn't receive one or only have the old version
for the old protocol, you can download it 
`here <http://download.tinkerforge.com/_stuff/beipackzettel.pdf>`__.

General
-------

As a first step you need to update all of your Bricklet firmwares and
Brick plugins. See above for information about the updating procedure.

The IPConnection has several new functions that are implemented for all 
languages, they include:

* connect
* disconnect
* register_callback (for enumeration)
* get_connection_state
* set_auto_reconnect
* get_auto_reconnect
* set_timeout
* get_timeout
* wait (replacement for join_thread)
* unwait

Additionally, the enumeration callback has now a different signature. With
the returned data it should now be possible to reconstruct the complete
topology of the network of Bricks and Bricklets.

The registration and triggering of the enumeration callback is now split into
two steps.

Documentation for these functions can be found in the IPConnection
documentation for each language, see :ref:`here <api_bindings_ip_connection>`.

Every Brick and Bricklet has the following new functions:

* get_response_expected
* set_response_expected
* set_response_expected_all

Documentation for these functions can be found in the normal programming
language documentation for each Brick and Bricklet.

In the following we will compare relevant code snippets from Protocol 1.0
to equivalents from Protocol 2.0. Keep in mind that you need to use
the :ref:`newest version of the Bindings <downloads_bindings_examples>` for 
your programming languages to be able to utilize the new Protocol 2.0 features.


C/C++
-----

Initialization:

.. code-block:: c

    // 1.0
    IPConnection ipcon;
    if(ipcon_create(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not create connection\n");
        exit(1);
    }

    AmbientLight al;
    ambient_light_create(&al, UID); 

    if(ipcon_add_device(&ipcon, &al) < 0) {
        fprintf(stderr, "Could not connect to Bricklet\n");
        exit(1);
    }

    ...

    ipcon_destroy(&ipcon);

    // 2.0
    IPConnection ipcon;
    ipcon_create(&ipcon);

    AmbientLight al;
    ambient_light_create(&al, UID, &ipcon); 

    if(ipcon_connect(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not connect\n");
        exit(1);
    }

    ...

    ipcon_destroy(&ipcon); // Calls ipcon_disconnect internally

Callbacks:

.. code-block:: c

    // 1.0
    void cb_illuminance(uint16_t illuminance) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE, 
                                    (void *)cb_illuminance);

    // 2.0 (now with user data)
    void cb_illuminance(uint16_t illuminance, void *user_data) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                    (void *)cb_illuminance,
                                    NULL);

New enumeration signature and registration:

.. code-block:: c

    // 1.0
    void cb_enumerate(char *uid, 
                      char *name, 
                      uint8_t stack_id, 
                      bool is_new);

    ipcon_enumerate(&ipcon, cb_enumerate);

    // 2.0
    void cb_enumerate(const char *uid,
                      const char *connected_uid,
                      char position,
                      uint8_t hardware_version[3],
                      uint8_t firmware_version[3],
                      uint16_t device_identifier,
                      uint8_t enumeration_type,
                      void *user_data);

    ipcon_register_callback(&ipcon,
                            IPCON_CALLBACK_ENUMERATE,
                            (void *)cb_enumerate,
                            NULL);

    ipcon_enumerate(&ipcon);

C#
--

General:

There are no unsigned data types used anymore. This was necessary to make
the C# bindings CLS complient (i.e. they can be easily used from other 
.net languages). All unsigned data types have been replaced by the next
higher signed data type.

=============  =============
Data type 1.0  Data type 2.0
=============  =============
uint8          int16
uint16         int32
uint32         int64
uint64         int64
=============  =============

Initialization:

.. code-block:: csharp

    // 1.0
    IPConnection ipcon = new IPConnection(HOST, PORT);    
    BrickletAmbientLight al = new BrickletAmbientLight(UID);    
    ipcon.AddDevice(al);
    ...
    ipcon.Destroy();

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.Connect(HOST, PORT);
    ...
    ipcon.Disconnect();

Callbacks:

.. code-block:: csharp

    // 1.0
    static void IlluminanceCB(ushort illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.RegisterCallback(new BrickletAmbientLight.Illuminance(IlluminanceCB));

    // 2.0: Now with sender object in callback and "+=" syntax to add callback
    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.Illuminance += IlluminanceCB;

New enumeration signature and registration:

.. code-block:: csharp

    // 1.0
    static void EnumerateCB(string uid, 
                            string name, 
                            byte stackID, 
                            bool isNew);

    ipcon.Enumerate(new IPConnection.EnumerateCallback(EnumerateCB));

    // 2.0
    static void EnumerateCB(IPConnection sender,
                            string uid, 
                            string connectedUid, 
                            char position,
                            short[] hardwareVersion, 
                            short[] firmwareVersion,
                            int deviceIdentifier, 
                            short enumerationType);

    ipcon.EnumerateCallback += EnumerateCB;

    ipcon.Enumerate();

Delphi
------

Initialization:

.. code-block:: delphi

  { 1.0 }
  ipcon := TIPConnection.Create(HOST, PORT);
  al := TBrickletAmbientLight.Create(UID);
  ipcon.AddDevice(al);
  ...
  ipcon.Destroy;

  { 2.0 }
  ipcon := TIPConnection.Create;
  al := TBrickletAmbientLight.Create(UID, ipcon);
  ipcon.Connect(HOST, PORT);
  ...
  ipcon.Destroy; { Calls ipcon.Disconnect internally }


Callback:

.. code-block:: delphi

  { 1.0 }
  procedure TExample.IlluminanceCB(const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

  { 2.0: Now with sender object in callback }
  procedure TExample.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

New enumeration signature and registration:

.. code-block:: delphi

    { 1.0 }
    procedure TExample.EnumerateCB(const uid: string; 
                                   const name: string; 
                                   const stackID: byte; 
                                   const isNew: boolean);

    ipcon.Enumerate({$ifdef FPC}@{$endif}EnumerateCB);

    { 2.0 }
    procedure TExample.EnumerateCB(sender: TIPConnection;
                                   const uid: string; 
                                   const connectedUid: string; 
                                   const position: char;
                                   const hardwareVersion: TVersionNumber;
                                   const firmwareVersion: TVersionNumber;
                                   const deviceIdentifier: word; 
                                   const enumerationType: byte);

    ipcon.OnEnumerate := {$ifdef FPC}@{$endif}EnumerateCB;

    ipcon.Enumerate();

Java
----

Initialization:

.. code-block:: java

    // 1.0
    IPConnection ipcon = new IPConnection(host, port);
    BrickletAmbientLight al = new BrickletAmbientLight(UID);
    ipcon.addDevice(al);
    ...
    ipcon.destroy();

    // 2.0
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.connect(host, port);
    ...
    ipcon.disconnect();

New enumeration signature and registration:

.. code-block:: java

    // 1.0
    ipcon.enumerate(new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String name, 
                              short stackID, 
                              boolean isNew);
    });

    // 2.0
    ipcon.addListener(new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String connectedUid, 
                              char position,
                              short[] hardwareVersion, 
                              short[] firmwareVersion,
                              int deviceIdentifier, 
                              short enumerationType);
    });

    ipcon.enumerate();

The TimeoutException was moved from
``com.tinkerforge.IPConnection.TimeoutException`` to
``com.tinkerforge.TimeoutException``.

New Listener Approach:

.. code-block:: java

    // 1.0
    brickletTemperature.addListener(new BrickletTemperature.TemperatureListener() {
        public void temperature(short temperature) {
            System.out.println("Temperature: " + temperature/100.0 + " °C");
        }
    });
    // No removeListener in 1.0

    // 2.0
    brickletTemperature.addTemperatureListener(new BrickletTemperature.TemperatureListener() {
        public void temperature(short temperature) {
            System.out.println("Temperature: " + temperature/100.0 + " °C");
        }
    });

    // Removing listener possible in 2.0
    brickletTemperature.removeTemperatureListener(temperatureListener);

PHP
---

Initialization:

.. code-block:: php

    // 1.0
    $ipcon = new IPConnection($host, $port);
    $al = new BrickletAmbientLight($uid);
    $ipcon->addDevice($al);
    ...
    $ipcon->destroy();

    // 2.0
    $ipcon = new IPConnection();
    $al = new BrickletAmbientLight($uid, $ipcon);
    $ipcon->connect($host, $port);
    ...
    $ipcon->disconnect();

New enumeration signature and registration:

.. code-block:: php

    // 1.0
    function enumerateCB($uid, 
                         $name, 
                         $stackID, 
                         $isNew);

    $ipcon->enumerate('enumerateCB');

    // 2.0
    function enumerateCB($uid, 
                         $connectedUid, 
                         $position,
                         $hardwareVersion,
                         $firmwareVersion,
                         $deviceIdentifier,
                         $enumerationType,
                         $userData);

    $ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE, 'enumerateCB');

    $ipcon->enumerate();

Python
------

Initialization:

.. code-block:: python

    # 1.0
    ipcon = IPConnection(HOST, PORT)
    al = AmbientLight(UID)
    ipcon.add_device(al)
    ...
    ipcon.destroy()

    # 2.0
    ipcon = IPConnection()
    al = AmbientLight(UID, ipcon)
    ipcon.connect(HOST, PORT)
    ...
    ipcon.disconnect()

New enumeration signature and registration:

.. code-block:: python

    # 1.0
    def cb_enumerate(uid, 
                     name, 
                     stack_id, 
                     is_new)

    ipcon.enumerate(cb_enumerate)

    # 2.0
    def cb_enumerate(uid, 
                     connected_uid, 
                     position, 
                     hardware_version, 
                     firmware_version,
                     device_identifier, 
                     enumeration_type)

    ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, cb_enumerate)

    ipcon.enumerate()

Ruby
----

Initialization:

.. code-block:: ruby

    # 1.0
    ipcon = IPConnection.new HOST, PORT
    al = BrickletAmbientLight.new UID
    ipcon.add_device al
    ...
    ipcon.destroy

    # 2.0
    ipcon = IPConnection.new
    al = BrickletAmbientLight.new UID, ipcon
    ipcon.connect HOST, PORT
    ...
    ipcon.disconnect

New enumeration signature and registration:

.. code-block:: ruby

    # 1.0
    ipcon.enumerate do |uid, 
                        name, 
                        stack_id, 
                        is_new|

    # 2.0
    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, 
                                                                  connected_uid,
                                                                  position,
                                                                  hardware_version, 
                                                                  firmware_version,
                                                                  device_identifier, 
                                                                  enumeration_type|

    ipcon.enumerate
