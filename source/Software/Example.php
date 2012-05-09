<?php

require_once('Tinkerforge/IPConnection.php');

use Tinkerforge\IPConnection;

$host = 'localhost';
$port = 4223;

function cb_enumerate($uid, $name, $stackID, $isNew)
{
    if ($isNew) {
        echo "New device:\n";
    } else {
        echo "Removed device:\n";
    }

    echo " Name:     $name\n";
    echo " UID:      $uid\n";
    echo " Stack ID: $stackID\n";
}

$ipcon = new IPConnection($host, $port); // Create IP connection to brickd

$ipcon->enumerate('cb_enumerate'); // Enumerate Bricks and Bricklets

echo "Press ctrl+c to exit\n";
$ipcon->dispatchCallbacks(-1); // Dispatch callbacks forever

?>
