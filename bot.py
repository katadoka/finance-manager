import telebot

import config
from controllers import FinanceManagerController
from views import TelegramView


bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    command =  message.text.split()
    name = message.chat.id
    if command[0] in ['history', 'h']:
        TelegramView(name).history()
    elif command[0] in ['balance', 'b']:
        TelegramView(name).balance()
    else:
        try:
            amount = int(command[0])
            FinanceManagerController(name).update_balance(amount)
        except ValueError:
            TelegramView(name).message(
                "Wrong choise. Valid values: balance, b, history, h, <number>")

if __name__ == '__main__':
    bot.polling(none_stop=True)
