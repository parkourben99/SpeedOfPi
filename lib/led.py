class Led(object):
    def __init__(self, bus, address, port):
        self.bus = bus
        self.address = address
        self.port = port
        self.active = True
        self.deactivate()

    def activate(self):
        self.__toggle(1)
        self.active = True

    def deactivate(self):
        self.__toggle(0)
        self.active = False

    def __toggle(self, state):
        state_list = list(bin(self.active)[2:].zfill(8))

        state_list[self.port] = state
        state = ''.join(str(e) for e in state_list)
        state = int(state, 2)

        self.bus.write_byte(self.address, state)
