#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import Temperature

HOST = "localhost"
PORT = 4223
UID_TEMPERATURE = "XYZ" # Enter Temperature Bricklet UID here

class Window(QtGui.QWidget):
    qtcb_temperature = QtCore.pyqtSignal(int)

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Refresh', self)
        self.button.clicked.connect(self.handle_button)
        self.label = QtGui.QLabel('TBD')
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.ipcon = IPConnection()
        self.temperature = Temperature(UID_TEMPERATURE, self.ipcon)
        self.ipcon.connect(HOST, PORT)

        # We send the callback through the Qt signal/slot
        # system to make sure that we can change the label
        self.qtcb_temperature.connect(self.cb_temperature)
        self.temperature.register_callback(Temperature.CALLBACK_TEMPERATURE, self.qtcb_temperature.emit)

        # Refresh every second
        self.temperature.set_temperature_callback_period(1000)
        
        # Refresh once on startup
        self.handle_button()

    # Refresh by hand
    def handle_button(self):
        self.cb_temperature(self.temperature.get_temperature())

    def cb_temperature(self, temperature):
        # Show temperature
        self.label.setText(u"Temperature: {0} °C".format(temperature/100.0))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()              # In window
    # window.showFullScreen()  # Fullscreen
    sys.exit(app.exec_())
