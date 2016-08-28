import os
import time
import smbus
import yaml
from bin.updater import Updater


class SpeedOfPi(object):

    def __init__(self):
        bus = smbus.SMBus(1)

    def create_nodes(self): pass

    def get_config(self): pass

    def set_config(self): pass

    def update(self):
        updater = Updater()
        needs_update = updater.check()
        if needs_update:
            print("There is an update")
            print("Downloading update now")
            updater.update()
        else:
            print("You are up to date!")

    def multi_player(self): pass

    def single_player(self): pass

    def loop(self): pass

