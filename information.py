from collections import namedtuple
from models import DBModel

History = namedtuple('History', ['income', 'datetime'])


class Information:

    def __init__(self, name):
        self.name = name
        self.current_balance, self.history = DBModel.load(name)

    def save(self):
        DBModel.save(self)
