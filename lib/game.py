import time
import random
from lib.scorer import Scorer


class Game(object):
    def __init__(self, difficulty):
        self.nodes = {}
        self.difficulty = difficulty
        self.scorer = Scorer(self.difficulty)
        self.active_nodes = []

    def multi_player(self, nodes):
        self.nodes = nodes

    def single_player(self, nodes):
        self.nodes = nodes
        self.game_loop()

    def start_game(self): pass

    def get_random_node(self):
        nodes = list(self.nodes.keys())
        available = list(set(nodes) - set(self.active_nodes))

        return random.choice(available) if available else available

    def game_loop(self):
        start_time = time.time()
        end_time = start_time + (60 * 1)

        while (end_time - start_time) > 0:
            node = self.get_random_node()
            if node:
                self.nodes[node].activate()
                print(str(node) + ' activated!')

                self.active_nodes.append(node)

                self.nodes[node].deactivate()
            else:
                print('no nodes left!')
                # exit()


