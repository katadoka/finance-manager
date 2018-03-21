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

    @staticmethod
    def build_massage(content, tmp='{e[0]}: {e[1]}'):
        massage_content = []
        for e in content:
            massage_content.append(tmp.format(e=e))
        return massage_content

    def history(self):
        content = [['Balance', 'Data']] + self.ctrl.history
        history = TelegramView.build_massage(content)
        self.message('\n'.join(history))

    def balance(self):
        content = [["Currency", "Balance", "Exchange rate"]] + self.ctrl.balance()
        balance = TelegramView.build_massage(content, tmp='{e[0]}({e[2]}): {e[1]}')
        self.message('\n'.join(balance))
