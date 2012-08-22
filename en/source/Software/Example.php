<?php

require_once('Tinkerforge/IPConnection.php');

use Tinkerforge\IPConnection;

$host = 'localhost';
$port = 4223;

function enumerateCB($uid, $name, $stackID, $isNew)
{
    if ($isNew) {
        echo "New device:\n";
    } else {
        echo "Removed device:\n";
    }

    echo " Name:     $name\n";
    echo " UID:      $uid\n";
    echo " Stack ID: $stackID\n";
    echo "\n";
}

$ipcon = new IPConnection($host, $port); // Create IP connection to brickd

$ipcon->enumerate('enumerateCB'); // Enumerate Bricks and Bricklets

echo "Press ctrl+c to exit\n";
$ipcon->dispatchCallbacks(-1); // Dispatch callbacks forever

?>
