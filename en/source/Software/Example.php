<?php

require_once('Tinkerforge/IPConnection.php');

use Tinkerforge\IPConnection;

$host = 'localhost';
$port = 4223;

function enumerateCB($uid, $connectedUid, $position, $hardwareVersion, $firmwareVersion, $deviceIdentifier, $enumerationType)
{
	echo "UID:               $uid\n";
	echo "Enumeration Type:  $enumerationType\n";

    if($enumerationType == IPConnection::ENUMERATION_TYPE_DISCONNECTED) {
		return;
    }

	echo "Connected UID:     $connectedUid\n";
	echo "Position:          $position\n";
	echo "Hardware Version:  $hardwareVersion[0].$hardwareVersion[1].$hardwareVersion[2]\n";
	echo "Firmware Version:  $firmwareVersion[0].$firmwareVersion[1].$firmwareVersion[2]\n";
	echo "Device Identifier: $deviceIdentifier\n";
    echo "\n";
}

// Create IP connection and connect to brickd
$ipcon = new IPConnection();
$ipcon->connect($host, $port);

// Register enumeration callback to "enumerateCB"
$ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE, 'enumerateCB');

$ipcon->enumerate();

echo "Press ctrl+c to exit\n";
$ipcon->dispatchCallbacks(-1); // Dispatch callbacks forever

?>
