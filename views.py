
from terminaltables import AsciiTable

from controllers import FinanceManagerController
from models import CurrencyRatesModel

class AsciiTableView:

    def __init__(self, name):
        self.ctrl = FinanceManagerController(name)
        

    def history(self):
        heading = [['Balance', 'Data']] + self.ctrl.history
        history = AsciiTable(heading)
        print(history.table)

    def balance(self):
        rates = CurrencyRatesModel.get_rates()

        content = [["Currency", "Balance", "Exchange rate"]] + self.ctrl.balance(rates)
        print(AsciiTable(content).table)
