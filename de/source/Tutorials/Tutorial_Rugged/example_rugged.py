#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_20x4 import LCD20x4
from tinkerforge.bricklet_temperature import Temperature

# This class will use any LCD Bricklet and Temperature Bricklet that
# are connected to the PC and display the temperature on the LCD.
#
# The program should stay stable if Bricks are connected/disconnected,
# if the Brick Daemon is restarted or if a WiFi/RS485 connection is lost.
# It will also keep working if you exchange the Master or one of the
# Bricklets by a new one of the same type.
#
# If a Brick or Bricklet loses its state (e.g. callback configuration)
# while the connection was lost, it will automatically be reconfigured
# accordingly.
class ExampleRugged:
    HOST = "localhost"
    PORT = 4223

    def __init__(self):
        self.lcd = None
        self.temp = None

        # Create IP Connection
        self.ipcon = IPConnection() 

        # Register IP Connection callbacks
        self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, 
                                     self.cb_enumerate)
        self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED, 
                                     self.cb_connected)

        # Connect to brickd, will trigger cb_connected
        self.ipcon.connect(ExampleRugged.HOST, ExampleRugged.PORT) 

        self.ipcon.enumerate()

    # Callback switches lcd backlight on/off based on lcd button 0
    def cb_button_pressed(self, button):
        if self.lcd:
            if button == 0:
                if self.lcd.is_backlight_on():
                    self.lcd.backlight_off()
                else:
                    self.lcd.backlight_on()

    # Callback updates temperature displayed on lcd
    def cb_temperature(self, temperature):
        if self.lcd:
            self.lcd.clear_display()
            s = 'Temperature: {0:.2f}{1:c}C'.format(temperature/100.0, 0xdf)
            self.lcd.write_line(0, 0, s)

    # Callback handles device connections and configures possibly lost 
    # configuration of lcd and temperature callbacks, backlight etc.
    def cb_enumerate(self, uid, connected_uid, position, hardware_version, 
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
            
            # Enumeration is for LCD Bricklet
            if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
                # Create lcd device object
                self.lcd = LCD20x4(uid, self.ipcon) 
                self.lcd.register_callback(self.lcd.CALLBACK_BUTTON_PRESSED, 
                                           self.cb_button_pressed)
                self.lcd.clear_display()
                self.lcd.backlight_on()
            # Enumeration is for Temperature Bricklet
            if device_identifier == Temperature.DEVICE_IDENTIFIER:
                # Create temperature device object
                self.temp = Temperature(uid, self.ipcon) 
                self.temp.register_callback(self.temp.CALLBACK_TEMPERATURE, 
                                            self.cb_temperature)

                self.temp.set_temperature_callback_period(50)

    # Callback handles reconnection of IP Connection
    def cb_connected(self, connected_reason):
        # Enumerate devices again. If we reconnected, the Bricks/Bricklets
        # may have been offline and the configuration may be lost.
        # In this case we don't care for the reason of the connection
        self.ipcon.enumerate()
        

if __name__ == "__main__":
    ExampleRugged()
    raw_input('Press key to exit\n') # Use input() in Python 3
