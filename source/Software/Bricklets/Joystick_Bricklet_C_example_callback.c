// tested with 
// gcc -lpthread -lrt -o example_callback bricklet_joystick.c 
//     ip_connection.c example_callback.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_joystick.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abcd" // Change to your UID

// Callback function for pressed and released events 
void cb_pressed(void) {
	printf("Pressed\n");
}

void cb_released(void) {
	printf("Released\n");
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

	// Register callbacks for pressed and released events
	joystick_register_callback(&js, JOYSTICK_CALLBACK_PRESSED, cb_pressed);
	joystick_register_callback(&js, JOYSTICK_CALLBACK_RELEASED, cb_released);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
