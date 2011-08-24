// tested with 
// gcc -lpthread -lrt -o example_hello_world bricklet_lcd_20x4.c 
//     ip_connection.c example_hello_world.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_lcd_20x4.h"

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
	LCD20x4 lcd;
	lcd_20x4_create(&lcd, UID); 

	// Add device to ip connection
	if(ipcon_add_device(&ipcon, &lcd) < 0) {
		fprintf(stderr, "Could not connect to Brick\n");
		exit(1);
	}
	// Don't use device before it is added to a connection

	// Turn backlight on
	lcd_20x4_backlight_on(&lcd);

	// Write "Hello World"
	lcd_20x4_write_line(&lcd, 0, 0, "Hello World");

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
