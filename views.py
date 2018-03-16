import telebot
from terminaltables import AsciiTable

import config
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

class TelegramView:

    def __init__(self, name):
        self.ctrl = FinanceManagerController(name)
        self.bot = telebot.TeleBot(config.token)
        self.name = name

    def message(self, text):
        self.bot.send_message(self.name, text)

    def history(self):
        heading = [['Balance', 'Data']] + self.ctrl.history
        self.message(heading)

    def balance(self):
        content = [["Currency", "Balance", "Exchange rate"]] + self.ctrl.balance()
        self.message('\n'.join([f'{e[0]}({e[2]}): {e[1]}' for e in content]))
