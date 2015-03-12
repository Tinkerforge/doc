
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Funksteckdosen in C# mit GUI fernsteuern

.. _starter_kit_hardware_hacking_remote_switch_gui_csharp:

Funksteckdosen in C# mit GUI fernsteuern
========================================

.. include:: CSharpCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

Wir setzen weiterhin voraus, dass die Fernbedienung mit einem
:ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
verbunden wurde wie :ref:`hier <starter_kit_hardware_hacking_remote_switch_hardware_setup>`
beschrieben.

Eine Demo-Anwendung basierend auf diesem Projekt ist verfügbar:
(Download: `Windows, Linux, Mac OS X
<https://github.com/Tinkerforge/hardware-hacking/raw/master/remote_switch_gui/csharp/RemoteSwitchGUI.exe>`__):

* Auf Windows wird das `.NET Framework
  <http://www.microsoft.com/de-de/download/details.aspx?id=30653>`__ benötigt,
  dies ist typischerweise aber bereits installiert.
* Auf Linux wird die `Mono Runtime for Linux
  <http://www.mono-project.com/Mono:Linux>`__ benötigt, dies ist typischerweise
  aber bereits auch installiert.
* Auf Mac OS X wird die `Mono Runtime for Mac OS X
  <http://www.mono-project.com/Mono:OSX>`__ benötigt. Seit Mac OS 10.8 muss
  außerdem noch `XQuartz <http://xquartz.macosforge.org/>`__ installiert werden
  damit die Mono Runtime richtig funktioniert. Jetzt kann die Demo-Anwendung
  mittels ``mono RemoteSwitchGUI.exe`` aus einem Terminal-Fenster heraus
  gestartet werden.


Ziele
-----

In diesem Projekt wird ein robustes GUI Programm erstellt, das die
Funktionalität der realen Fernbedienung nachbildet.


Schritt 1: Die GUI erstellen
----------------------------

Das Programm wird ein einfaches `Windows Forms
<http://en.wikipedia.org/wiki/Windows_Forms>`__ GUI erstellt mit vier Knöpfen
und einer Liste für Statusmeldungen:

.. image:: /Images/Kits/hardware_hacking_remote_switch_csharp_gui.jpg
   :scale: 100 %
   :alt: Windows Forms GUI
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_switch_csharp_gui.jpg

Als erstes wird eine ``Form`` mit Titel und Größe erstellt:

.. code-block:: csharp

    class RemoteSwitchGUI : Form
    {
        public RemoteSwitchGUI()
        {
            Text = "Remote Switch";
            Size = new Size(300, 500);
        }

        static public void Main()
        {
            Application.Run(new RemoteSwitchGUI());
        }
    }

Dann wird ein 40 Pixel hohes Panel für die Knöpfe an der oberen Kante eingefügt.
Die Liste für Statusmeldungen füllt den Rest der Form:

.. code-block:: csharp

    public RemoteSwitchGUI()
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

Die ``CreateButton()`` Methode erzeugt einen neuen Knopf mit vergebenem Namen
und vorgegebener Position:

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

Zuletzt werden die vier Knöpfe erzeugt, einen für jeden zu steuernden Knopf auf
der Fernbedienung:

.. code-block:: csharp

    public RemoteSwitchGUI()
    {
        // [...]

        buttonAOn  = CreateButton("A On",   10);
        buttonAOff = CreateButton("A Off",  70);
        buttonBOn  = CreateButton("B On",  130);
        buttonBOff = CreateButton("B Off", 190);

Das GUI ist jetzt fertig.


Schritt 2: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

Dieser Schritt ist der gleiche wie Schritt 1 aus dem
:ref:`Rauchmelder mit C# auslesen
<starter_kit_hardware_hacking_smoke_detector_csharp_step1>` Projekts,
allerdings mit ein paar Änderungen, damit es in einem GUI Programm ordentlich
funktioniert.

Die :csharp:func:`Connect() <IPConnection::Connect>` Methode soll nicht direkt
aufgerufen werden, da dies einen Moment dauern kann und in dieser Zeit die GUI
nicht auf den Benutzer reagieren könnte. Daher wird ``Connect()`` aus einem
extra Thread aufgerufen werden, so dass es im Hintergrund ausgeführt wird und
die GUI nicht blockiert wird:

.. code-block:: csharp

    public RemoteSwitchGUI()
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

Die ``ConnectedCB`` Callback-Funktion ist die die gleiche wie im Rauchmelder
Projekt. Aber die ``EnumerateCB`` Callback-Funktion ist einfacher, da das
Industrial Quad Relay Bricklet nicht extra konfiguriert werden muss für diese
Projekt:

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


Schritt 3: Taster auslösen
--------------------------

Die Verbindung wurde hergestellt und ein Industrial Quad Relay Bricklet wurde
gefunden, aber es fehlt noch die Logik um einen Klick auf einen Knopf des
Programms in das Auslösen einen Tasters auf der Fernbedienung zu übersetzen.

Dafür wird ein Delegate zum ``Click``-Event eines jeden Knopfes hinzugefügt.
Der Delegate ruft dann eine ``TriggerSwitch()`` Methode mit einer gegebenen
Bitmaske auf. Diese Bitmaske legt fest welche Relais des Industrial Quad Relay
Bricklets geschlossen werden sollen, wenn ein bestimmter Knopf geklickt wird:

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
geschlossen werden. Dies wird durch die Bitmaske ``(1 << 0) | (1 << 2)``
repräsentiert.

Der Konstruktor wird so abgewandelt, dass er ``CreateButton()`` mit den
passenden Bitmasken für jeden Knopf aufruft:

.. code-block:: csharp

    public RemoteSwitchGUI()
    {
        // [...]

        buttonAOn  = CreateButton("A On",   10, (1 << 0) | (1 << 2));
        buttonAOff = CreateButton("A Off",  70, (1 << 0) | (1 << 3));
        buttonBOn  = CreateButton("B On",  130, (1 << 1) | (1 << 2));
        buttonBOff = CreateButton("B Off", 190, (1 << 1) | (1 << 3));

.. FIXME: Add a sentence about the matrix layout of the switch circuit and how
          this maps to the selection mask

Die ``TriggerSwitch()`` Methode benutzt :csharp:func:`SetMonoflop()
<BrickletIndustrialQuadRelay::SetMonoflop>` um eine Tasterdruck
auf der Fernbedienung auszulösen. Ein Monoflop setzt einen neuen Zustand
(Relais offen oder geschlossen) und hält diesen für eine bestimmte Zeit
(0,5s in diesem Fall). Nach dieser Zeit wird der vorheriger Zustand
wiederhergestellt. Dieses Ansatz simuliert einen Tasterdruck der für 0,5s
anhält.

.. code-block:: csharp

    private void TriggerSwitch(int selectionMask)
    {
        brickletIndustrialQuadRelay.SetMonoflop(selectionMask, 15, 500);
    }

Das ist es. Wenn wir diese drei Schritte zusammen in eine Datei kopieren und
ausführen, dann hätten wir jetzt eine funktionierendes Programm, das
Funksteckdosen über deren gehackte Fernbedienung fernsteuern kann!

Das Programm ist noch nicht robust genug. Was passiert wenn die Verbindung beim
Start des Programms nicht hergestellt werden kann, oder wenn das Enumerate nach
einem Auto-Reconnect nicht funktioniert?

Wir brauchen noch Fehlerbehandlung!


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

Es werden die gleichen Konzepte wie in Schritt 4 des
:ref:`Rauchmelder mit C# auslesen
<starter_kit_hardware_hacking_smoke_detector_csharp_step4>` Projekts verwendet,
aber mit einigen Abwandelungen, damit sie in einem GUI Programm richtig
funktionieren.

Wir können nicht einfach ``System.Console.WriteLine()`` für Logausgaben
verwenden, da dies ein GUI Programm ist und kein Konsolenfenster hat.
Stattdessen werden die Logausgaben in einer Liste im GUI ausgegeben.

Dieser Ansatz hat aber noch ein Problem. Die Verbindung wird in einem extra
Thread hergestellt, allerdings darf nur der Haupt-Thread mit der GUI
interagieren. Glücklicherweise bietet C# die ``Invoke()`` Methode, die es
erlaubt aus anderen Threads Code im Haupt-Thread auszuführen und so korrekt
mit der GUI zu interagieren. Mit dieser Methode erstellen wir eine ``Log()``
Methode, die es allen Threads erlaubt Logausgaben in die Liste für
Statusmeldungen zu schreiben:

.. code-block:: csharp

    private void Log(string message)
    {
        Invoke((MethodInvoker) delegate() { listBox.Items.Add(message); });
    }

Alle Änderungen die in Schritt 4 des Rauchmelder Projekts beschrieben werden
sind hier auch notwendig. Zusätzlich müssen noch mögliche Fehler in der
``TriggerSwitch()`` Methode behandelt werden:

.. code-block:: csharp

    private void TriggerSwitch(string name, int selectionMask)
    {
        if(brickletIndustrialQuadRelay == null) {
            Log("No Industrial Quad Relay Bricklet found");
            return;
        }

        try
        {
            brickletIndustrialQuadRelay.SetMonoflop(selectionMask, 15, 500);
            Log("Triggered '" + name + "'");
        }
        catch(TinkerforgeException e)
        {
            Log("Trigger '" + name + "' Error: " + e.Message);
        }
    }

Für bessere Logausgaben wird der Name des Knopfes an ``TriggerSwitch()``
übergeben, so dass dieser in Logausgaben angezeigt werden kann.

Schlussendlich, da der Thread der die Verbindung aufbaut jetzt mit der GUI
interagiert kann er nicht mehr direkt im Konstruktor gestartet werden.
Stattdessen wird der Thread erst gestartet wenn die GUI das erst Mal angezeigt
wird. Der ``Load``-Event kann dafür verwendet werden:

.. code-block:: csharp

    public RemoteSwitchGUI()
    {
        // [...]

        Load += delegate(object sender, System.EventArgs e)
        {
            Thread thread = new Thread(delegate() { Connect(); });
            thread.IsBackground = true;
            thread.Start();
        };
    }


Schritt 5: Alles zusammen
-------------------------

Das ist es! Das C# Programm zum Fernsteuern der gehackten Funksteckdosen ist
fertig und sollte nun alle gesteckten Ziele erfüllen.

Das gesamte Programm in einem Stück (`download
<https://raw.githubusercontent.com/Tinkerforge/hardware-hacking/master/remote_switch_gui/csharp/RemoteSwitchGUI.cs>`__):

.. literalinclude:: ../../../../../hardware-hacking/remote_switch_gui/csharp/RemoteSwitchGUI.cs
 :language: csharp
 :tab-width: 4
