// tested with 
// gcc -lpthread -lrt -o example_output bricklet_io4.c 
//     ip_connection.c example_output.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_io4.h"

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
	IO4 io;
	io4_create(&io, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &io) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

    // Set pin 1 to output low
    io4_set_configuration(&io, 1 << 1, 'o', false);

    // Set pin 2 and 3 to output high
    io4_set_configuration(&io, (1 << 2) | (1 << 3), 'o', true);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
