
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Remote Switches using C#

.. _starter_kit_hardware_hacking_remote_switch_gui_csharp:

Control Remote Switches with a GUI using C#
===========================================

.. include:: CSharpCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

We are also assuming that you have a remote control connected to
an :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>` as
described :ref:`here <starter_kit_hardware_hacking_remote_switch>`.


Goals
-----

In this project we will create a robust GUI program that resembles the
functionality of the actual remote control.

The program will reuse some common parts of the :ref:`Read out Smoke Detectors
using C# <starter_kit_hardware_hacking_smoke_detector_csharp>` project.


Step 1: Create the GUI
----------------------

The program will have a simple `Windows Forms
<http://en.wikipedia.org/wiki/Windows_Forms>`__ GUI that contains four buttons
and a list box for status messages:

.. image:: /Images/Kits/hardware_hacking_remote_switch_csharp_gui.jpg
   :scale: 100 %
   :alt: Windows Forms GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_switch_csharp_gui.jpg

We start with a simple ``Form`` that has title and size:

.. code-block:: csharp

    class RemoteSwitch : Form
    {
        public RemoteSwitch()
        {
            Text = "Remote Switch";
            Size = new Size(300, 500);
        }

        static public void Main()
        {
            Application.Run(new RemoteSwitch());
        }
    }

Then a 40 pixel height panel for the buttons is added on the top border and a
list box for status messages fills the rest of the form:

.. code-block:: csharp

    public RemoteSwitch()
    {
        Text = "Remote Switch";
        Size = new Size(300, 500);

        panel = new Panel();
        panel.Parent = this;
        panel.Height = 40;
        panel.Dock = DockStyle.Top;

        listBox = new ListBox();
        listBox.Parent = this;
        listBox.Dock = DockStyle.Fill;
        listBox.BringToFront();

The ``CreateButton()`` method creates a new button with a given name and
position:

.. code-block:: csharp

    private Button CreateButton(string name, int x)
    {
        Button button = new Button();

        button.Text = name;
        button.Parent = panel;
        button.Width = 50;
        button.Location = new Point(x, 10);

        return button;
    }

Finally four buttons are created, one for each button on the remote control
that we want to be able to trigger:

.. code-block:: csharp

    public RemoteSwitch()
    {
        // [...]

        buttonAOn  = CreateButton("A On",   10);
        buttonAOff = CreateButton("A Off",  70);
        buttonBOn  = CreateButton("B On",  130);
        buttonBOff = CreateButton("B Off", 190);

Now the GUI is finished.


Step 2: Discover Bricks and Bricklets
-------------------------------------

This step is basically the same as step 1 in the :ref:`Read out Smoke Detectors
using C# <starter_kit_hardware_hacking_smoke_detector_csharp_step1>` project,
but with some changes to make it work in a GUI program.

We don't want to call the :csharp:func:`Connect() <IPConnection::Connect>`
method directly, because it might take a moment and block the GUI during that
period of time. Instead ``Connect()`` will be called from a thread, so it will
run in the background and the GUI stays responsive:

.. code-block:: csharp

    public RemoteSwitch()
    {
        // [...]

        Thread thread = new Thread(delegate() { Connect(); });
        thread.IsBackground = true;
        thread.Start();
    }

    private void Connect()
    {
        ipcon = new IPConnection();
        ipcon.Connect(HOST, PORT);

        ipcon.EnumerateCallback += EnumerateCB;
        ipcon.Connected += ConnectedCB;

        ipcon.Enumerate();
    }

The ``ConnectedCB`` callback function is the same as in the smoke detector
project. But the ``EnumerateCB`` callback function is simpler because the
Industrial Quad Relay Bricklet does not need any configuration for this project:

.. code-block:: csharp

    private void EnumerateCB(IPConnection sender, string UID, string connectedUID, char position,
                             short[] hardwareVersion, short[] firmwareVersion,
                             int deviceIdentifier, short enumerationType)
    {
        if(enumerationType == IPConnection.ENUMERATION_TYPE_CONNECTED ||
           enumerationType == IPConnection.ENUMERATION_TYPE_AVAILABLE)
        {
            if(deviceIdentifier == BrickletIndustrialQuadRelay.DEVICE_IDENTIFIER)
            {
                brickletIndustrialQuadRelay = new BrickletIndustrialQuadRelay(UID, ipcon);
            }
        }
    }


Step 3: Triggering Switches
---------------------------

The connection is established and an Industrial Quad Relay Bricklet is found
but there is no logic yet to trigger a switch if a button is clicked.

A delegate is added to the ``Click`` event of the button that calls a
``TriggerSwitch()`` method with the given selection mask. This mask defines
which switches of the Industrial Quad Relay Bricklet should be closed if the
specific button is clicked:

.. code-block:: csharp

    private Button CreateButton(string name, int x, int selectionMask)
    {
        // [...]

        button.Click += delegate(object sender, System.EventArgs e)
        {
            TriggerSwitch(selectionMask);
        };

        return button;
    }

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
closed. This is represented by the selection mask ``(1 << 0) | (1 << 2)``.

The constructor is changed to call ``CreateButton()`` with the correct
selection mask for each button:

.. code-block:: csharp

    public RemoteSwitch()
    {
        // [...]

        buttonAOn  = CreateButton("A On",   10, (1 << 0) | (1 << 2));
        buttonAOff = CreateButton("A Off",  70, (1 << 0) | (1 << 3));
        buttonBOn  = CreateButton("B On",  130, (1 << 1) | (1 << 2));
        buttonBOff = CreateButton("B Off", 190, (1 << 1) | (1 << 3));

.. FIXME: Add a sentence about the matrix layout of the switch circuit and how
          this maps to the selection mask

The ``TriggerSwitch()`` method then just starts a 1.5s (1500ms) monoflop on the
selected switches to simulate a button press on the remote control:

.. code-block:: csharp

    private void TriggerSwitch(int selectionMask)
    {
        brickletIndustrialQuadRelay.SetMonoflop(selectionMask, 255, 1500);
    }

That's it. If we would copy these three steps together in one file and execute
it, we would have a working program that can control remote switches using
their hacked remote control!

But the program is not yet robust enough. What happens if it can't connect on
startup? What happens if the enumerate after an auto reconnect doesn't work?

What we need is error handling!


Step 4: Error handling and Logging
----------------------------------

We will use the same principals as in step 4 of the :ref:`Read out Smoke
Detectors using C# <starter_kit_hardware_hacking_smoke_detector_csharp_step4>`
project, but with some changes to make it work in a GUI program.

We can't just use ``System.Console.WriteLine()`` for logging because this is a
GUI program and there is no console window. Instead the list box is going to
display the log messages.

But there is still a problem with that approach. The connection is established
on an extra thread, but only the main thread can safely interact with the
GUI. Luckily C# provides the ``Invoke()`` method that allows all threads to run
code on the main thread and safely interact with the GUI. With this method we
can create a ``Log()`` method that allows all threads to write to the list box
in a safe way:

.. code-block:: csharp

    private void Log(string message)
    {
        Invoke((MethodInvoker) delegate() { listBox.Items.Add(message); });
    }

All the changes described in step 4 of the smoke detector project apply here as
well. In addition we have to deal with errors in ``TriggerSwitch()`` too:

.. code-block:: csharp

    private void TriggerSwitch(string name, int selectionMask)
    {
        if(brickletIndustrialQuadRelay == null) {
            Log("No Industrial Quad Relay Bricklet found");
            return;
        }

        try
        {
            brickletIndustrialQuadRelay.SetMonoflop(selectionMask, 255, 1500);
            Log("Triggered '" + name + "'");
        }
        catch(TinkerforgeException e)
        {
            Log("Trigger '" + name + "' Error: " + e.Message);
        }
    }

To get nicer log messages the button name is passed to ``TriggerSwitch()`` so
it can be included in the log messages.

Finally, because the connect thread interacts with the GUI now it cannot be
started directly from the constructor anymore. Instead it is started when the
GUI is shown for the first time. The ``Load`` event can be used for this:

.. code-block:: csharp

    public RemoteSwitch()
    {
        // [...]

        Load += delegate(object sender, System.EventArgs e)
        {
            Thread thread = new Thread(delegate() { Connect(); });
            thread.IsBackground = true;
            thread.Start();
        };
    }


Step 5: Everything put together
-------------------------------

That's it! We are done with our hacked remote switch and all of the goals
should be met.

Now all of the above put together (`download
<https://raw.github.com/Tinkerforge/hardware-hacking/master/remote_switch_gui/csharp/RemoteSwitch.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/remote_switch_gui/csharp/RemoteSwitch.cs
 :language: csharp
 :tab-width: 4
