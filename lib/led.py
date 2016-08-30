class Led(object):
    def __init__(self, bus, address, port):
        self.bus = bus
        self.address = address
        self.port = port
        self.active = False

    def activate(self):
        self.__toggle(True)
        self.active = True

    def deactivate(self):
        self.__toggle(False)
        self.active = False

    def __toggle(self, state):
        state_list = list(bin(self.active)[2:].zfill(8))

        state_list[self.port] = int(state)
        state = ''.join(state_list)

        state = int(state, 2)
        self.bus.write_byte(self.address, state)
