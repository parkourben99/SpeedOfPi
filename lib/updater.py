import git
import os


class Updater(object):
    def __init__(self, is_develop):
        self.repo = git.Repo(os.getcwd())
        self.branch = 'origin/master' if not is_develop else 'origin/develop'

    def check(self):
        self.repo.remote().fetch()

        diff = self.repo.index.diff(self.branch)
        return bool(diff)

    def update(self):
        # todo pull from branch
        self.repo.remote().pull()
