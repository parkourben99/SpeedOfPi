import time


class Timer(object):
    def __init__(self):
        self.__start_time = 0
        self.__end_time = 0

    def start(self):
        self.__start_time = time.time()

    def stop(self):
        self.__end_time = time.time()

        total_time = self.__calc_total_time()
        self.__reset()

        return total_time

    def __calc_total_time(self):
        return self.__end_time - self.__start_time

    def __reset(self):
        self.__start_time = 0
        self.__end_time = 0
