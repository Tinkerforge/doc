
.. _api_bindings_java_android:

Java (Android) - API Bindings
=============================

Für Android können die normalen :ref:`Java Bindings <api_bindings_java>`
verwendet werden. Allgemeine Informationen sind in der Beschreibung der Java
Bindings zu finden, diese Seite befasst sich nur mit Android spezifischen
Dingen.

Im Folgenden wird angenommen, dass die Android Entwicklungsumgebung schon
installiert ist. Für Android-Anfänger empfehlen wir zuerst mit dem
`First App Tutorial
<https://developer.android.com/training/basics/firstapp/index.html>`__ von
Google zu beginnen.


Test eines Beispiels
--------------------

Als Beispiel soll ein kleines Projekt zum Schalten eines Dual Relay Bricklets
erstellt werden. Es sollte leicht sein dieses Beispiel für deine Zwecke
weiterzuentwickeln.

Starte eine neues Android Projekt:

* File
* New
* Project...
* Android Project
* Wähle "Name" (e.g. ``relay``)
* Wähle "Target"
* Wähle "Package Name" (e.g. ``org.example``)
* Klicke Finish

Als nächstes muss das ``Tinkerforge.jar` aus den Java bindings in
den ``PROJECTFOLDER/libs/`` Ordner kopiert werden.

Dann den Quelltext wie unten dargestellt bearbeiten. Vergiss nicht die Host IP
Adresse zu der des PCs auf dem der Brick Daemon läuft zu ändern. Dies kann die
lokale oder die IP Adresse für die Verbindung zum Internet sein. Für letztere
musst auch noch sichergestellt werden, dass der Port des Brick Daemons von außen
erreichbar ist.

Es folgt der Quelltext eines Beispielprogramms, dass ein Dual Relay Bricklet
mit einem Umschaltknopf steuern kann.

.. code-block:: java

 package org.example;

 import android.app.Activity;
 import android.os.Bundle;
 import android.view.View;
 import android.view.View.OnClickListener;
 import android.widget.ToggleButton;

 import com.tinkerforge.BrickletDualRelay;
 import com.tinkerforge.IPConnection;

 public class RelayActivity extends Activity {
     // Change to the IP address of your host
     private static final String host = "192.168.178.35";
     private static final int port = 4223;
     private static final String UID = "Axb";
     private IPConnection ipcon;
     private BrickletDualRelay dr;
     private ToggleButton tb;

     @Override
     public void onCreate(Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);

         try {
             ipcon = new IPConnection();
             dr = new BrickletDualRelay(UID, ipcon);
             ipcon.connect(host, port);
         } catch(Exception e) {
             // Here you might want to give the user a retry button.
             return;
         }

         tb = new ToggleButton(this);
         tb.setOnClickListener(new OnClickListener() {
             public void onClick(View v) {
                 if(tb.isChecked()) {
                     dr.setState(true, false);
                 } else {
                     dr.setState(false, false);
                 }
             }
         });

         setContentView(tb);
     }
 }

Deine App braucht noch Internet Permission (um sich mit dem Netzwerk verbinden
zu dürfen). Füge dazu folgende Zeile:

.. code-block:: xml

 <uses-permission android:name="android.permission.INTERNET" />

zum ``AndroidManifest.xml`` auf der Ebene wie der ``<application>`` Tag hinzu.

Deine app sollte jetzt wie in diesem Bild aussehen:

.. image:: /Images/Screenshots/android_eclipse_small.jpg
   :scale: 100 %
   :alt: Eclipse Konfiguration für Java Bindings in Android
   :align: center
   :target: ../_images/Screenshots/android_eclipse.jpg

Die App kann nun im Simulator getestet werden:

* Run
* Run
* Android Application

.. note::
  Diese Beispiel ruft potentiell blockierende Methoden auf dem UI Thread auf,
  zum Beispiel ``new IPConnection`` und ``setState``. Davon wird im Allgemeinen
  abgeraten, da es zum Hängen des UIs führen kann. Um dies zu vermeiden sollte
  die Kommunikation über die IPConnection in einen extra Thread ausgelagert
  werden, zum Beispiel mit Hilfe eines ``AsyncTask``.

  Seit Android 4.2 führt der Aufruf von ``new IPConnection`` auf dem UI Thread
  zu einer ``andriod.os.NetworkOnMainThreadException``. Siehe diese
  `StackOverflow Frage <https://stackoverflow.com/questions/6343166/android-os-networkonmainthreadexception>`__
  für weitere Informationen.
