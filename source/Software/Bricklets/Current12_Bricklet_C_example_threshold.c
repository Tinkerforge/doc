// tested with 
// gcc -lpthread -lrt -o example_threshold bricklet_current12.c 
//     ip_connection.c example_threshold.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_current12.h"

#define HOST "localhost"
#define PORT 4223
#define UID "ABCD" // Change to your UID

// Callback for current greater than 5A
void cb_reached(int16_t current) {
	printf("Current is greater than 5A: %f\n", current/1000.0);
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


    // Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    current12_set_debounce_period(&c, 10000);

    // Register threshold reached callback to function cb_reached
    current12_register_callback(&c, 
	                            CURRENT12_CALLBACK_CURRENT_REACHED,
								cb_reached);
	
    // Configure threshold for "greater than 5A" (unit is mA)
    current12_set_current_callback_threshold(&c, '>', 5*1000, 0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
