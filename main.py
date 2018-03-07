# finance-manager

from datetime import datetime
import json
import click
import os
import requests
from bs4 import BeautifulSoup
from terminaltables import AsciiTable


BASE_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


def input_income(name, income):
    if os.path.isfile(f'{name}.txt'):
        with open(f'{name}.txt', 'r') as f_in:
            information = json.load(f_in)
    else:
        information = {
            "current_balance": 0,
            "history": []
        }
    information["current_balance"] += int(income)
    information["history"].append((int(income), datetime.now().isoformat()))

    with open(f'{name}.txt', 'w') as f_out:
        json.dump(information, f_out)


def input_costs(name, costs):
    if os.path.isfile(f'{name}.txt'):
        with open(f'{name}.txt', 'r') as f_in:
            information = json.load(f_in)
    else:
        information = {
            "current_balance": 0,
            "history": []
        }
    information["current_balance"] -= int(costs)
    information["history"].append((-int(costs), datetime.now().isoformat()))

    with open(f'{name}.txt', 'w') as f_out:
        json.dump(information, f_out)


def out_history(name):
    if not os.path.isfile(f'{name}.txt'):
        raise Exception(f'This {name}.txt is missing')

    with open(f'{name}.txt', 'r') as f_in:
        information = json.load(f_in)
        heading = [['Balance', 'Data']] + information["history"]
        history = AsciiTable(heading)
        print(history.table)


def out_balance(name):
    if not os.path.isfile(f'{name}.txt'):
        raise Exception(f'This {name}.txt is missing')
    with open(f'{name}.txt', 'r') as f_in:
        information = json.load(f_in)
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        currency_rates = json.loads(str(soup))
        heading_balance = []
        for i in currency_rates:
            currency = i["ccy"]
            rate = i["buy"]
            bal = information["current_balance"] / float(i["buy"])
            heading_balance.append([str(currency), str(bal), str(rate)])
        headings = [["Currency", "Balance", "Exchange rate"]] + heading_balance
        balance = AsciiTable(headings)
        print(balance.table)


@click.command()
@click.option('--income')
@click.option('--costs')
@click.option('--name', prompt='Your name please')
@click.option('--history', is_flag=True)
@click.option('--balance', is_flag=True)
def click_command(income, costs, name, history, balance):
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
