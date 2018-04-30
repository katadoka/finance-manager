from information import History, Information
from datetime import datetime
from models import CurrencyRatesModel


class FinanceManagerController:

    def __init__(self, name):
        self.information = Information(name)

    @property
    def history(self):
        return self.information.history

    def balance(self):
        content = []
        for i in CurrencyRatesModel.get_rates():
            bal = self.information.current_balance / float(i["buy"])
            content.append([i["ccy"], bal, i["buy"]])
        return [["UAH", self.information.current_balance, 1]] + content

    def update_balance(self, income):
        self.information.amount = int(income)
        self.information.current_balance += int(income)
        history = History(int(income), datetime.now().isoformat())
        self.information.history.append(history)
        self.information.save()
