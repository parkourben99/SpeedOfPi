import cmd
import os
import argparse
from lib.main import SpeedOfPi


class CLI(cmd.Cmd):
    def __init__(self):
        self.game = SpeedOfPi()
        self.update_available = None
        cmd.Cmd.__init__(self)
        os.system('clear')
        self.prompt = "-->>"
        self.intro = "SpeedOfPi Command line interface"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd
           documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)  # Clean up command completion
        print("Exiting...")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        print("Unable to find '{command}' for help on commands type: help".format(command=line))

    def do_clear(self, args):
        """clears the screen"""
        os.system('clear')
        print(self.intro)

    def do_play(self, args):
        self.game.single_player()

    def do_update(self, args):
        """check for updates"""
        if not self.update_available:
            print("Checking for updates")
            if not self.update_check():
                print("No updates available")
                return

        if not args:
            self.game.update()
            print("Updating to latest stable version")
        else:
            parser = argparse.ArgumentParser()
            parser.add_argument(dest="branch")

            output, unknownArgs = parser.parse_known_args(args.split())
            self.game.update(output.branch)
            print("Updating to latest beta version")

    def update_check(self, branch=False):
        self.update_available = self.game.update_available(branch)
        return self.update_available

if __name__ == '__main__':
    cli = CLI()
    cli.cmdloop()

