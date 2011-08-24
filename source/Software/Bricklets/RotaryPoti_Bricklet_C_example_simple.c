// tested with 
// gcc -lpthread -lrt -o example_simple bricklet_rotary_poti.c 
//     ip_connection.c example_simple.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_rotary_poti.h"

#define HOST "localhost"
#define PORT 4223
#define UID "2wx" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	RotaryPoti poti;
	rotary_poti_create(&poti, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &poti) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Get current position (value has range -150 to 150)
	int16_t position;
	if(rotary_poti_get_position(&poti, &position) < 0) {
		fprintf(stderr, "Could not get value, probably timeout\n");
		exit(1);
	}

	printf("Position: %d\n", position);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
