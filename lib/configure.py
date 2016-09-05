import yaml


class Configure(object):
    def __init__(self):
        self.__config = None

    def get_config(self):
        return self.__config

    def read_config(self, file_name='config.yaml'):
        with open(file_name, 'r') as stream:
            try:
                self.__config = yaml.load(stream)
                return True
            except yaml.YAMLError:
                #todo write error message to log/display
                pass

        return False

    def set_config(self):
        self.__config = None

