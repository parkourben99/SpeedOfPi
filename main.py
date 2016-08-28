import smbus
from bin.updater import Updater
from bin.configure import Configure


class SpeedOfPi(object):
    def __init__(self):
        self.bus = smbus.SMBus(1)

    def create_nodes(self, node_config): pass

    def get_config(self):
        config = Configure()

        try:
            node_config = config.get_config()
            self.create_nodes(node_config)
        except FileNotFoundError:
            print("Please set the config")
            exit()

    def set_config(self): pass

    def update(self):
        updater = Updater()
        needs_update = updater.check()
        if needs_update:
            updater.update()
        else:
            print("You are up to date!")

    def multi_player(self): pass

    def single_player(self): pass

    def loop(self): pass

