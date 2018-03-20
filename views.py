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

    def view_massage_history(heading):
        history = []
        for e in heading:
            history.append(f'{e[0]}: {e[1]}')
        return history

    def view_massage_balance(content):
        balance = []
        for e in content:
            balance.append(f'{e[0]}({e[2]}): {e[1]}')
        return balance

    def history(self):
        heading = [['Balance', 'Data']] + self.ctrl.history
        history = view_massage_history(heading)
        self.message('\n'.join(history))

    def balance(self):
        content = [["Currency", "Balance", "Exchange rate"]] + self.ctrl.balance()
        balance = view_massage_balance(content)
        self.message('\n'.join(balance))
