from bin.button import Button
from bin.led import Led


class Node(object):

    def __init__(self, button_bus, button_port, led_bus, led_port):
        self.button = self.set_button(button_bus, button_port)
        self.led = self.set_led(led_bus, led_port)
        self.active = False

    def set_button(self, button_bus, button_port):
        return Button(button_bus, button_port)

    def set_led(self, led_bus, led_port):
        return Led(led_bus, led_port)