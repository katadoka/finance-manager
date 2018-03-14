from collections import namedtuple
from constans import RATES_API, OUTPUT_DIR, FILE_TMP
from models import OsModel
import json
import os

History = namedtuple('History', ['income', 'datetime'])


class Information:

    def __init__(self, name):
        self.name = name
        self.current_balance, self.history = OsModel.load(name)

    def save(self):
        OsModel.save(self.name, self.current_balance, self.history)
