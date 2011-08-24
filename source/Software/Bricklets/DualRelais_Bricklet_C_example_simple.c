// tested with 
// gcc -lpthread -lrt -o example_simple bricklet_dual_relais.c 
//     ip_connection.c example_simple.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_dual_relais.h"

#define HOST "localhost"
#define PORT 4223
#define UID "xyz" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	DualRelais dr;
	dual_relais_create(&dr, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &dr) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Turn relais 1 on and relais 2 off.
	dual_relais_set_state(&dr, true, false);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
