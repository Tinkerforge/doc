// tested with 
// gcc -lpthread -lrt -o example_button_callbacks bricklet_lcd_20x4.c 
//     ip_connection.c example_button_callbacks.c
// on Ubuntu

#include <stdio.h>

#include "ip_connection.h"
#include "bricklet_lcd_20x4.h"

#define HOST "localhost"
#define PORT 4223
#define UID "XYZ" // Change to your UID

// Callback functions for button status
void cb_pressed(uint8_t i) {
	printf("Pressed: %d\n", i);
}

void cb_released(uint8_t i) {
	printf("Released: %d\n", i);
}

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

	// Register button status callbacks to cb_pressed and cb_released
	lcd_20x4_register_callback(&lcd, 
	                           LCD_20X4_CALLBACK_BUTTON_PRESSED, 
	                           cb_pressed);
	lcd_20x4_register_callback(&lcd, 
	                           LCD_20X4_CALLBACK_BUTTON_RELEASED, 
	                           cb_released);

	printf("Press ctrl+c to close\n");
	ipcon_join_thread(&ipcon); // Join mainloop of ip connection
}
