import yaml


class Configure(object):
    def __init__(self):
        self.config = None

    def get_config(self):
        return self.config

    def read_config(self, file_name='config.yaml'):
        with open(file_name, 'r') as stream:
            try:
                self.config = yaml.load(stream)
                return True
            except yaml.YAMLError: pass

        return False
