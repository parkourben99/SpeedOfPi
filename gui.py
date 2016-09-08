from tkinter import *
import time
from lib.main import SpeedOfPi
from tkinter.ttk import *


class GUI(object):
    def __init__(self):
        self.game = SpeedOfPi()

        root = Tk()
        root.title('SpeedOfPi')

        # bring to front always
        root.lift()
        root.attributes('-topmost', True)

        # set full screen and not able to resize
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        root.resizable(width=False, height=False)

        self.frame = Frame(root, padding=(10, 10, 10, 10))
        self.frame.pack()
        self.create_buttons()

        root.mainloop()

    def create_buttons(self):
        single_player_btn = Button(self.frame, text="Single Player", command=self.single_player)
        single_player_btn.pack(side="top", padx=10, pady=10)

        multi_player_btn = Button(self.frame, text="Multi Player", command=self.multi_player)
        multi_player_btn.pack(side="top", padx=10, pady=10)

        edit_config_btn = Button(self.frame, text="Settings", command=self.settings)
        edit_config_btn.pack(side="top", padx=10, pady=10)

        update_btn = Button(self.frame, text="Update", command=self.update_game)
        update_btn.pack(side="top", padx=10, pady=10)

        help_btn = Button(self.frame, text="Help", command=self.help)
        help_btn.pack(side="top", padx=10, pady=10)

        about_btn = Button(self.frame, text="About", command=self.about)
        about_btn.pack(side="top", padx=10, pady=10)

        exit_btn = Button(self.frame, text="Exit", command=quit)
        exit_btn.pack(side="top", padx=10, pady=10)

    def single_player(self):
        # todo show choose difficulty window
        self.game.single_player()

    def multi_player(self):
        # todo show choose difficulty window
        self.game.multi_player()

    def settings(self):
        print('settings button')

    def update_game(self):
        is_updatable = self.game.update_available()
        print(is_updatable)

    def help(self):
        print('help button')

    def about(self):
        print('about button')


if __name__ == '__main__':
    gui = GUI()
