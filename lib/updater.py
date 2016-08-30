import git
import os


class Updater(object):
    def __init__(self):
        self.repo = git.Repo(os.getcwd())

    def check(self):
        self.repo.remote().fetch()

        diff = self.repo.index.diff('origin/master')
        return bool(diff)

    def update(self):
        self.repo.remote().pull()
