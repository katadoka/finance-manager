import telebot

import config
from controllers import FinanceManagerController
from views import AsciiTableView


bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    command =  message.text.split()
    name = message.chat.id
    if command[0] == 'income':
        FinanceManagerController(name).update_balance(int(command[1]))
    elif command[0] == 'costs':
        FinanceManagerController(name).update_balance(-int(command[1]))
    elif command[0] == 'history':
        AsciiTableView(name).history()
    elif command[0] == 'balance':
        AsciiTableView(name).balance()

if __name__ == '__main__':
    bot.polling(none_stop=True)
