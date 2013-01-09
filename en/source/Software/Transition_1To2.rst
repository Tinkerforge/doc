.. _transition_1to2:

Transitioning from Protocol V1 to Protocol V2
=============================================

Update Tools and Firmwares
--------------------------

Updating to Protocol V2 is quite easy. Start by installing the :ref:`newest
version <downloads_tools>` of the Brick Daemon and the Brick Viewer.

After that you should start by updating all of your Bricks, you can update
them one by one as described :ref:`here <brickv_flash_firmware>`.

To update the Bricklets, there is an automated process. You can fill up one
of your updates Bricks with Bricklets, click on "Updates" in the Brick
Viewer and use the first tab. There you should see all of your connected
Bricks with the corresponding connected Bricklets. Bricklets that are out
of date are marked red. You can update all Bricklets at once by clicking
on "Auto-Update All Bricklets".

.. image:: /Images/Screenshots/bricklet_auto_update.jpg
   :scale: 100 %
   :alt: Bricklet auto update feature of the Brick Viewer
   :align: center
   :target: ../_images/Screenshots/bricklet_auto_update.jpg

If the auto update does not work, you can of course still update the
Bricklets individually by using the normal
:ref:`Bricklet updating process <brickv_flash_plugin>`.

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
* wait (replacement for join)
* unwait

Additionally, the enumeration callback has now a different signature. With
the returned data it should now be possible to reconstruct the complete
topology of the network of Bricks and Bricklets.

Documentation for these functions can be found in the IPConnection
documentation for each language, see :ref:`here <api_bindings_ip_connection>`.

Every Brick and Bricklet has the following new functions:

* get_response_expected
* set_response_expected
* set_response_expected_all

Documentation for these functions can be found in the normal programming
language documentation for each Brick and Bricklet.

In the following we will compare relevant code snippets from Protocol V1
to equivalents from Protocol V2. Keep in mind that you need to use
the :ref:`newest version of the Bindings <bindings_examples>` for your 
programming languages to be able to utilize the new Protocol V2 features.


C/C++
-----

Initialization:

.. code-block:: c

    // V1
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

    // V2
    IPConnection ipcon;
    ipcon_create(&ipcon);

    AmbientLight al;
    ambient_light_create(&al, UID, &ipcon); 

    if(ipcon_connect(&ipcon, HOST, PORT) < 0) {
        fprintf(stderr, "Could not connect\n");
        exit(1);
    }

Callbacks:

.. code-block:: c

    // V1
    void cb_illuminance(uint16_t illuminance) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE, 
                                    (void *)cb_illuminance);

    // V2 (now with user data)
    void cb_illuminance(uint16_t illuminance, void *user_data) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                    (void *)cb_illuminance,
                                    NULL);

New Enumeration signature:

.. code-block:: c

    // V1
    void cb_enumerate(char *uid, 
                      char *name, 
                      uint8_t stack_id, 
                      bool is_new)

    // V2
    void cb_enumerate(const char *uid,
                      const char *connected_uid,
                      char position,
                      uint8_t hardware_version[3],
                      uint8_t firmware_version[3],
                      uint16_t device_identifier,
                      uint8_t enumeration_type,
                      void *user_data) {

C#
--

General:

There are no unsigned data types used anymore. This was necessary to make
the C# bindings CLS complient (i.e. they can be easily used from other 
.net languages). All unsigned data types have been replaced by the next
higher signed data type.

============  ============
Data type V1  Data type V2
============  ============
uint8         int16
uint16        int32
uint32        int64
uint64        int64
============  ============

Initialization:

.. code-block:: csharp

    // V1
    IPConnection ipcon = new IPConnection(HOST, PORT);    
    BrickletAmbientLight al = new BrickletAmbientLight(UID);    
    ipcon.AddDevice(al);

    // V2
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.Connect(HOST, PORT);


Callbacks:

.. code-block:: csharp

    // V1
    static void IlluminanceCB(ushort illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.RegisterCallback(new BrickletAmbientLight.Illuminance(IlluminanceCB));

    // V2: Now with sender object in callback and "+=" syntax to add callback
    static void IlluminanceCB(BrickletAmbientLight sender, int illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.Illuminance += IlluminanceCB;

New Enumeration signature:

.. code-block:: csharp

    // V1
    static void EnumerateCB(string uid, 
                            string name, 
                            byte stackID, 
                            bool isNew)

    // V2
    static void EnumerateCB(IPConnection sender,
                            string uid, 
                            string connectedUid, 
                            char position,
                            short[] hardwareVersion, 
                            short[] firmwareVersion,
                            int deviceIdentifier, 
                            short enumerationType)

Delphi
------

Initialization:

.. code-block:: delphi

  { V1 }
  ipcon := TIPConnection.Create(HOST, PORT);
  al := TBrickletAmbientLight.Create(UID);
  ipcon.AddDevice(al);

  { V2 }
  ipcon := TIPConnection.Create;
  al := TBrickletAmbientLight.Create(UID, ipcon);
  ipcon.Connect(HOST, PORT);


Callback:

.. code-block:: delphi

  { V1 }
  procedure TExample.IlluminanceCB(const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

  { V2: Now with sender object in callback }
  procedure TExample.IlluminanceCB(sender: TBrickletAmbientLight; const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;

New Enumeration signature:

.. code-block:: delphi

    // V1
    procedure TExample.EnumerateCB(const uid: string; 
                                   const name: string; 
                                   const stackID: byte; 
                                   const isNew: boolean);

    // V2
    procedure TExample.EnumerateCB(TIPConnection: TObject;
                                   const uid: string; 
                                   const connectedUid: string; 
                                   const position: char;
                                   const hardwareVersion: TVersionNumber;
                                   const firmwareVersion: TVersionNumber;
                                   const deviceIdentifier: word; 
                                   const enumerationType: byte);


Java
----

Initialization:

.. code-block:: java

    // V1
    IPConnection ipcon = new IPConnection(host, port);
    BrickletAmbientLight al = new BrickletAmbientLight(UID);
    ipcon.addDevice(al);

    // V2
    IPConnection ipcon = new IPConnection();
    BrickletAmbientLight al = new BrickletAmbientLight(UID, ipcon);
    ipcon.connect(host, port);

New Enumeration signature:

.. code-block:: java

    // V1
    new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String name, 
                              short stackID, 
                              boolean isNew);
    }

    // V2
    new IPConnection.EnumerateListener() {
        public void enumerate(String uid, 
                              String connectedUid, 
                              char position,
                              short[] hardwareVersion, 
                              short[] firmwareVersion,
                              int deviceIdentifier, 
                              short enumerationType);
    }

PHP
---

Initialization:

.. code-block:: php

    // V1
    $ipcon = new IPConnection($host, $port);
    $al = new BrickletAmbientLight($uid);
    $ipcon->addDevice($al);

    // V2
    $ipcon = new IPConnection();
    $al = new BrickletAmbientLight($uid, $ipcon);
    $ipcon->connect($host, $port);

New Enumeration signature:

.. code-block:: php

    // V1
    function enumerateCB($uid, 
                         $name, 
                         $stackID, 
                         $isNew)

    // V2
    function enumerateCB($uid, 
                         $connectedUid, 
                         $position,
                         $hardwareVersion,
                         $firmwareVersion,
                         $deviceIdentifier,
                         $enumerationType)

Python
------

Initialization:

.. code-block:: python

    # V1
    ipcon = IPConnection(HOST, PORT)
    al = AmbientLight(UID)
    ipcon.add_device(al)

    # V2
    ipcon = IPConnection()
    al = AmbientLight(UID, ipcon)
    ipcon.connect(HOST, PORT)

New Enumeration signature:

.. code-block:: python

    // V1
    def cb_enumerate(uid, 
                     name, 
                     stack_id, 
                     is_new):

    // V2
    def cb_enumerate(uid, 
                     connected_uid, 
                     position, 
                     hardware_version, 
                     firmware_version,
                     device_identifier, 
                     enumeration_type):

Ruby
----

Initialization:

.. code-block:: ruby

    # V1
    ipcon = IPConnection.new HOST, PORT
    al = BrickletAmbientLight.new UID
    ipcon.add_device al

    # V2
    ipcon = IPConnection.new
    al = BrickletAmbientLight.new UID, ipcon
    ipcon.connect HOST, PORT

New Enumeration signature:

.. code-block:: ruby

    // V1
    ipcon.enumerate do |uid, 
                        name, 
                        stack_id, 
                        is_new|

    // V2
    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, 
                                                                  connected_uid,
                                                                  position,
                                                                  hardware_version, 
                                                                  firmware_version,
                                                                  device_identifier, 
                                                                  enumeration_type|
