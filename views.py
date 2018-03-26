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

    HISTORY_HEADERS = [['Balance', 'Data']]
    BALANCE_HEADERS = [["Currency", "Balance", "Exchange rate"]]
    BALANCE_TMP = '{e[0]}({e[2]}): {e[1]}'
    HISTORY_TMP = '{e[0]}: {e[1]}'

    def __init__(self, name):
        self.ctrl = FinanceManagerController(name)
        self.bot = telebot.TeleBot(config.token)
        self.name = name
        self.text = None

    def send_message(self, text=None):
        message_text = text if text else self.text
        self.bot.send_message(self.name, message_text)

    def build_message(self, headers, his_bal, tmp):
        message_content = []
        content = headers + his_bal
        for e in content:
            message_content.append(tmp.format(e=e))
        self.text = '\n'.join(message_content)

    def history(self):
        self.build_message(TelegramView.HISTORY_HEADERS, self.ctrl.history, TelegramView.HISTORY_TMP)
        self.send_message()

    def balance(self):
        self.build_message(TelegramView.BALANCE_HEADERS, self.ctrl.balance(), TelegramView.BALANCE_TMP)
        self.send_message()
