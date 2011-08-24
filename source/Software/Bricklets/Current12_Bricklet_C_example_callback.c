// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_current12.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_current12.h"

#define HOST "localhost"
#define PORT 4223
#define UID "ABCD" // Change to your UID

// Callback function for current callback (parameter has unit mA)
void cb_current(int16_t current) {
	printf("Current: %f A\n", current/1000.0);
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Current12 c;
	current12_create(&c, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &c) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Set Period for current callback to 1s (1000ms)
	// Note: The callback is only called every second if the 
	//       current has changed since the last call!
	current12_set_current_callback_period(&c, 1000);

	// Register current callback to function cb_current
	current12_register_callback(&c, CURRENT12_CALLBACK_CURRENT, cb_current);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
