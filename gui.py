from tkinter import *
import time


class GUI(object):
    def __init__(self):
        self.home = Tk()
        l = Label(self.home, text='test')
        l.pack()
        self.home.mainloop()








if __name__ == '__main__':
    gui = GUI()
