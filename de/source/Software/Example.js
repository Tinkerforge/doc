var Tinkerforge = require('Tinkerforge');

var IPConnection = Tinkerforge.IPConnection;

var HOST = 'localhost';
var PORT = 4223;

// Create connection and connect to brickd
ipcon = new IPConnection();
ipcon.connect(HOST, PORT);

// Register Enumerate Callback
ipcon.on(IPConnection.CALLBACK_ENUMERATE,
    // Print incoming enumeration
    function(uid, cuid, pos, hwv, fwv, devid, enumtype) {
        console.log('UID:               '+uid);
        console.log('Enumeration Type:  '+enumtype);
        if(enumtype === IPConnection.ENUMERATION_TYPE_DISCONNECTED) {
            return;
        }
        console.log('Connected UID:     '+cuid);
        console.log('Position:          '+pos);
        console.log('Hardware Version:  '+hwv);
        console.log('Firmware Version:  '+fwv);
        console.log('Device Identifier: '+devid);
        console.log('');
    }
);

// Trigger Enumerate
ipcon.enumerate();

console.log("Press any key to exit ...");
process.stdin.on('data',
    function(data) {
        ipcon.disconnect();
        process.exit(0);
    }
);

