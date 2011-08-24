// tested with 
// gcc -lpthread -lrt -o example_simple bricklet_current12.c 
//     ip_connection.c example_simple.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_current12.h"

#define HOST "localhost"
#define PORT 4223
#define UID "ABCD" // Change to your UID

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

	// Get current current (unit is mA)
	int16_t current;
	if(current12_get_current(&c, &current) < 0) {
		fprintf(stderr, "Could not get value, probably timeout\n");
		exit(1);
	}

	printf("Current: %f A\n", current/1000.0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
