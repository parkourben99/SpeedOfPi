class Button(object):
    def __init__(self, bus, port):
        self.bus = bus
        self.port = port
        self.active = False
