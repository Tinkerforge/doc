// tested with 
// gcc -lpthread -lrt -o example_find_corners bricklet_joystick.c 
//     ip_connection.c example_find_corners.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_joystick.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abcd" // Change to your UID

// Callback for x and y position outside of -99, 99
void cb_reached(int16_t x, int16_t y) {
	if(x == 100 && y == 100) {
		printf("Top Right\n");
	} else if(x == -100 && y == 100) {
		printf("Top Left\n");
	} else if(x == -100 && y == -100) {
		printf("Bottom Left\n");
	} else if(x == 100 && y == -100) {
		printf("Bottom Right\n");
	} else {
		// This can't happen, the threshold is configured to:
		// "outside of -99, 99"
		printf("Error");
	}
}

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Joystick js;
	joystick_create(&js, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &js) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

    // Get threshold callbacks with a debounce time of 0.2 seconds (200ms)
    joystick_set_debounce_period(&js, 200);

    // Register threshold reached callback to function cb_reached
    joystick_register_callback(&js,
	                           JOYSTICK_CALLBACK_POSITION_REACHED,
	                           cb_reached);
	
    // Configure threshold for "x and y value outside of -99 and 99" 
    joystick_set_position_callback_threshold(&js, 'o', -99, 99, -99, 99);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
