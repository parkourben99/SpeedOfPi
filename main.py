import smbus
from lib.updater import Updater
from lib.configure import Configure
from lib.node import Node


class SpeedOfPi(object):
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.nodes = {}

    def create_nodes(self, node_config):
        for node in node_config['nodes']:
            try:
                node_number = list(node)[0]
                button_address = node[node_number][0]['button'][0]['address']
                button_port = node[node_number][0]['button'][1]['port']
                led_address = node[node_number][1]['led'][0]['address']
                led_port = node[node_number][1]['led'][1]['port']

                self.nodes[node_number] = Node(self.bus, button_address, button_port, led_address, led_port)
            except:
                print('unable to load node ' + node[0])

    def get_config(self):
        config = Configure()
        if not config.read_config():
            print('Could not read file')
            exit()

        node_config = config.get_config()
        self.create_nodes(node_config)

    def set_config(self): pass

    def update(self):
        updater = Updater()

        if updater.check():
            updater.update()
        else:
            print("You are up to date!")

    def multi_player(self): pass

    def single_player(self): pass

    def loop(self): pass
