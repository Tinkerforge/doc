// tested with 
// gcc -lpthread -lrt -o example_stack_status brick_master.c 
//     ip_connection.c example_stack_status.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "brick_master.h"

#define HOST "localhost"
#define PORT 4223
#define UID "aySDPZAhvvd" // Change to your UID

int main() {
	// Create ip connection to brickd
	IPConnection ipcon;
	if(ipcon_create(&ipcon, HOST, PORT) < 0) {
		fprintf(stderr, "Could not create connection\n");
		exit(1);
	}

	// Create device object
	Master master;
	master_create(&master, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &master) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection


	// Get voltage and current from stack (in mV/mA)
	uint16_t voltage; 
	master_get_stack_voltage(&master, &voltage);
	uint16_t current;
	master_get_stack_current(&master, &current);

	printf("Stack Voltage: %f V\n", voltage/1000.0);
	printf("Stack Current: %f V\n", current/1000.0);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
