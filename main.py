#import smbus
import time

from lib.updater import Updater
from lib.configure import Configure
from lib.node import Node
from lib.game import Game


class SpeedOfPi(object):
    def __init__(self):
        self.bus = '3' #smbus.SMBus(1)
        self.nodes = {}

        self.config = Configure()
        self.load_config()

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
                # throw exception here so user checks config file
                print('unable to load node ' + node[0])

    def load_config(self):
        if not self.config.read_config():
            print('Could not read file. would you like to setup nodes?')
            print('Would you like to setup nodes?')
            #todo expect keyboad input [Y/n] (Y,y, yes, YES, *enter)
            #if no exit else run set_config()
            exit()

        node_config = self.config.get_config()
        self.create_nodes(node_config)

    def set_config(self):
        self.config.set_config()

    def update(self):
        updater = Updater()

        if updater.check():
            updater.update()
        else:
            print("You are up to date!")

    def multi_player(self):
        difficulty = 1
        game = Game(difficulty)
        game.multi_player(self.nodes)

    def single_player(self):
        difficulty = 1
        game = Game(difficulty)
        game.single_player(self.nodes)

if __name__ == '__main__':
    a = SpeedOfPi()
    a.single_player()