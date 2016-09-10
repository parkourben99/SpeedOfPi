class Led(object):
    def __init__(self, bus, address, port):
        self.bus = bus
        self.address = address
        self.port = port
        self.active = False

    def activate(self):
        self.__toggle(1)
        self.active = True

    def deactivate(self):
        self.__toggle(0)
        self.active = False

    def __toggle(self, state):
        state_list = list(bin(self.active)[2:].zfill(8))

        print(state)
        print(state_list)

        state_list[self.port] = state
        state = ''.join(state_list)

        print(state_list)
        print(state)

        state = int(state, 2)

        print(state)

        self.bus.write_byte(self.address, state)
