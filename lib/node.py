from lib.button import Button
from lib.led import Led
from lib.timer import Timer


class Node(object):
    def __init__(self, bus, node_number, button_address, button_port, led_address, led_port):
        self.__bus = bus
        self.id = node_number
        self.__button = self.__set_button(button_address, button_port)
        self.__led = self.__set_led(led_address, led_port)
        self.__timer = Timer()
        self.active = False

    def __set_button(self, button_address, button_port):
        return Button(self.__bus, button_address, button_port)

    def __set_led(self, led_address, led_port):
        return Led(self.__bus, led_address, led_port)

    def get_button(self):
        return self.__button

    def activate(self):
        self.active = True

        self.__timer.start()
        self.__led.activate()

    def deactivate(self):
        self.active = False
        self.__led.deactivate()

        total_time = self.__timer.stop()
        return total_time
