import git
import os


class Updater(object):
    def __init__(self):
        self.repo = git.Repo(os.getcwd())

    def check(self, branch='origin/master'):
        self.repo.remote().fetch()

        diff = self.repo.index.diff(branch)
        return bool(diff)

    def update(self):
        self.repo.remote().pull()
