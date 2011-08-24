// tested with 
// gcc -lpthread -lrt -o example_beep bricklet_piezo_buzzer.c 
//     ip_connection.c example_beep.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_piezo_buzzer.h"

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
	PiezoBuzzer pb;
	piezo_buzzer_create(&pb, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &pb) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Make 2 second beep
    piezo_buzzer_beep(&pb, 2000);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
