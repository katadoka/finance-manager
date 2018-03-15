from collections import namedtuple
from models import OsModel

History = namedtuple('History', ['income', 'datetime'])


class Information:

    def __init__(self, name):
        self.name = name
        self.current_balance, self.history = OsModel.load(name)

    def save(self):
        OsModel.save(self.name, self.current_balance, self.history)
