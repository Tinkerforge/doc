// tested with 
// gcc -lpthread -lrt -o example_simple bricklet_humidity.c 
//     ip_connection.c example_simple.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_humidity.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Humidity h;
	humidity_create(&h, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &h) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Get current humidity (unit is %RH/10)
	uint16_t humidity;
	if(humidity_get_humidity(&h, &humidity) < 0) {
		fprintf(stderr, "Could not get value, probably timeout\n");
		exit(1);
	}

	printf("Relative Humidity: %f %%RH\n", humidity/10.0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
