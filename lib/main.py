import smbus
from lib.updater import Updater
from lib.configure import Configure
from lib.node import Node
from lib.difficulty import Difficulty
from lib.game import Game


class SpeedOfPi(object):
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.nodes = {}
        self.config = Configure()
        self.updater = None
        self.difficulty = Difficulty()

    def create_nodes(self, node_config):
        for node in node_config['nodes']:
            try:
                node_number = list(node)[0]
                button_address = node[node_number][0]['button'][0]['address']
                button_port = node[node_number][0]['button'][1]['port']
                led_address = node[node_number][1]['led'][0]['address']
                led_port = node[node_number][1]['led'][1]['port']

                self.nodes[node_number] = Node(self.bus, node_number, button_address, button_port, led_address, led_port)
            except:
                raise Exception("Config is incorrect on {node}".format(node=node[0]))

    #     self.nodes_init()
    #
    # def nodes_init(self):
    #     self.bus.write_bt

    def load_config(self):
        if not self.config.read_config():
            raise Exception('Could not read file')

        node_config = self.config.get_config()
        self.create_nodes(node_config)

    def set_config(self):
        self.config.set_config()

    def set_difficulty(self, level):
        self.difficulty.set(level)

    def get_difficulties(self):
        return self.difficulty.all()

    def update_available(self, is_develop=False):
        self.updater = Updater(is_develop)
        return self.updater.check()

    def update(self, is_develop=False):
        if not self.updater:
            self.updater = Updater(is_develop)

        self.updater.update()

    def multi_player(self):
        if not self.nodes:
            self.load_config()

        game = Game(self.difficulty)
        game.multi_player(self.nodes)

    def single_player(self):
        if not self.nodes:
            self.load_config()

        game = Game(self.difficulty)
        game.single_player(self.nodes)

# todo
# set all led off when loading the game
# flash all leds to start the game
# create wiring map
