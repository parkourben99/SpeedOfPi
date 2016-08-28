import yaml


class Configure(object):
    def __init__(self):
        self.config = None
        self.read_file()

    def get_config(self):
        return self.config

    def read_file(self): pass
