
from terminaltables import AsciiTable

from controllers import FinanceManagerController


class AsciiTableView:

    def __init__(self, name):
        self.ctrl = FinanceManagerController(name)

    def history(self):
        heading = [['Balance', 'Data']] + self.ctrl.history
        history = AsciiTable(heading)
        print(history.table)

    def balance(self):
        content = [["Currency", "Balance", "Exchange rate"]] + self.ctrl.balance()
        print(AsciiTable(content).table)
