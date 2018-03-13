from collections import namedtuple
from constans import RATES_API, OUTPUT_DIR, FILE_TMP
import json
import os

History = namedtuple('History', ['income', 'datetime'])


class Information:

    def __init__(self, name):
        self.name = name
        # self.current_balance, self.history = OsModel.load(name)

        if os.path.isfile(FILE_TMP.format(self.name)):
            with open(FILE_TMP.format(self.name), 'r') as f_in:
                information = json.load(f_in)
                self.current_balance = information['current_balance']
                self.history = information['history']
        else:
            self.current_balance = 0
            self.history = []

    def save(self):
        # OsModel.save(self.name, self.current_balance, self.history)
        information = {"current_balance": self.current_balance, "history": self.history}
        with open(FILE_TMP.format(self.name), 'w') as f_out:
            json.dump(information, f_out)
