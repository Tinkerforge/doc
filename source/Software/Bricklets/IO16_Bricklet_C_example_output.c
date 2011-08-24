// tested with 
// gcc -lpthread -lrt -o example_output bricklet_io16.c 
//     ip_connection.c example_output.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_io16.h"

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
	IO16 io;
	io16_create(&io, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &io) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

    // Set pin 0 on port a to output low
    io16_set_port_configuration(&io, 'a', 1 << 0, 'o', false);

    // Set pin 0 and 7 on port a to output high
    io16_set_port_configuration(&io, 'b', (1 << 0) | (1 << 7), 'o', true);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
