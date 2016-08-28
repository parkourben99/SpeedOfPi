import git
import os


class Updater(object):
    def __init__(self):
        self.repo = git.Repo(os.path.dirname(os.path.abspath(__file__)))
        self.head = self.repo.remotes.origin

    def check(self):
        self.head.fetch()
        diff = self.head.diff()

        return bool(diff)

    def update(self):
        self.head.pull()