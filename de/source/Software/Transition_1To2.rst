.. _transition_1to2:

Transitioning from Protocol V1 to Protocol V2
=============================================

General
-------

As a first step you need to update all of your Bricklet firmwares and
Brick plugins. See here (TODO) for information about the updating procedure.

TODO: General stuff about the transitioning.

In the following we will compare relevant code snippets from Protocol V1
to equivalents from Protocol V2.


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

    IPConnection ipcon;
    ipcon_create(&ipcon);


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
                                    cb_illuminance);

    // V2 (now with user data)
    void cb_illuminance(uint16_t illuminance, void *user_data) {
        printf("Illuminance: %f Lux.\n", illuminance/10.0);
    }

    ambient_light_register_callback(&al,
                                    AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                    (void *)cb_illuminance,
                                    NULL);

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
uin16         int32
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
    static void IlluminanceCB(object sender, int illuminance)
    {
        System.Console.WriteLine("Illuminance: " + illuminance/10.0 + " Lux");
    }
    al.Illuminance += IlluminanceCB;


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
  procedure TExample.IlluminanceCB(sender: TObject; const illuminance: word);
  begin
    WriteLn(Format('Illuminance: %f Lux', [illuminance/10.0]));
  end;

  al.OnIlluminance := {$ifdef FPC}@{$endif}IlluminanceCB;


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
