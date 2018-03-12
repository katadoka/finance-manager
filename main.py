# finance-manager

from datetime import datetime
from constans import BASE_URL, BASE_DIR, FILE_TMP
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
import json
import click
import os
import requests


def input_income(name, income):
    if os.path.isfile(FILE_TMP.format(name)):
        with open(FILE_TMP.format(name), 'r') as f_in:
            information = json.load(f_in)
    else:
        information = {
            "current_balance": 0,
            "history": []
        }
    information["current_balance"] += int(income)
    information["history"].append((int(income), datetime.now().isoformat()))

    with open(FILE_TMP.format(name), 'w') as f_out:
        json.dump(information, f_out)


def input_costs(name, costs):
    if os.path.isfile(FILE_TMP.format(name)):
        with open(FILE_TMP.format(name), 'r') as f_in:
            information = json.load(f_in)
    else:
        information = {
            "current_balance": 0,
            "history": []
        }
    information["current_balance"] -= int(costs)
    information["history"].append((-int(costs), datetime.now().isoformat()))

    with open(FILE_TMP.format(name), 'w') as f_out:
        json.dump(information, f_out)


def out_history(name):
    if not os.path.isfile(FILE_TMP.format(name)):
        raise Exception(f'This {name}.txt is missing')

    with open(FILE_TMP.format(name), 'r') as f_in:
        information = json.load(f_in)
        heading = [['Balance', 'Data']] + information["history"]
        history = AsciiTable(heading)
        print(history.table)


def out_balance(name):
    if not os.path.isfile(FILE_TMP.format(name)):
        raise Exception(f'This {name}.txt is missing')
    with open(FILE_TMP.format(name), 'r') as f_in:
        information = json.load(f_in)
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        currency_rates = json.loads(str(soup))
        heading_balance = []
        for i in currency_rates:
            bal = information["current_balance"] / float(i["buy"])
            heading_balance.append([i["ccy"], bal, i["buy"]])
        headings = [["Currency", "Balance", "Exchange rate"]] + heading_balance
        print(AsciiTable(headings).table)


@click.command()
@click.option('--income')
@click.option('--costs')
@click.option('--name', prompt='Your name please')
@click.option('--history', is_flag=True)
@click.option('--balance', is_flag=True)
def click_command(income, costs, name, history, balance):
    if not os.path.isdir(BASE_DIR):
        os.makedirs(BASE_DIR)
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
