# finance-manager

from datetime import datetime
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
from information import History, Information
from constans import RATES_API, OUTPUT_DIR, FILE_TMP
import json
import click
import os
import requests


def input_income(name, income):
    information = Information(name)
    information.current_balance += int(income)
    history = History(int(income), datetime.now().isoformat())
    information.history.append(history)
    information.save()


def input_costs(name, costs):
    input_income(name, -int(costs))


def out_history(name):
    information = Information(name)
    heading = [['Balance', 'Data']] + information.history
    history = AsciiTable(heading)
    print(history.table)


def out_balance(name):
    information = Information(name)
    response = requests.get(RATES_API)
    soup = BeautifulSoup(response.content, 'html.parser')
    currency_rates = json.loads(str(soup))
    content = []
    for i in currency_rates:
        bal = information.current_balance / float(i["buy"])
        content.append([i["ccy"], bal, i["buy"]])
    balances = [["UAH", information.current_balance, 1]]
    headings = [["Currency", "Balance", "Exchange rate"]] + balances + content
    print(AsciiTable(headings).table)


@click.command()
@click.option('--income')
@click.option('--costs')
@click.option('--name', prompt='Your name please')
@click.option('--history', is_flag=True)
@click.option('--balance', is_flag=True)
def click_command(income, costs, name, history, balance):
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if income:
        input_income(name, income)
    elif costs:
        input_costs(name, costs)
    elif history:
        out_history(name)
    elif balance:
        out_balance(name)

if __name__ == '__main__':
    click_command()
