// tested with 
// gcc -lpthread -lrt -o example_simple bricklet_joystick.c 
//     ip_connection.c example_simple.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_joystick.h"

#define HOST "localhost"
#define PORT 4223
#define UID "abcd" // Change to your UID

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

	// Get current position (x and y value)
	int16_t pos_x;
	int16_t pos_y;
	if(joystick_get_position(&js, &pos_x, &pos_y) < 0) {
		fprintf(stderr, "Could not get value, probably timeout\n");
		exit(1);
	}

	printf("Position: %d, %d\n", pos_x, pos_y);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
