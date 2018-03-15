# finance-manager

import click
from terminaltables import AsciiTable

from controllers import FinanceManagerController
from models import CurrencyRatesModel


def out_history(name):
    heading = [['Balance', 'Data']] + FinanceManagerController(name).history
    history = AsciiTable(heading)
    print(history.table)


def out_balance(name):
    ctrl = FinanceManagerController(name)
    rates = CurrencyRatesModel.get_rates()

    content = [["Currency", "Balance", "Exchange rate"]] + ctrl.balance(rates)
    print(AsciiTable(content).table)


@click.command()
@click.option('--income')
@click.option('--costs')
@click.option('--name', prompt='Your name please')
@click.option('--history', is_flag=True)
@click.option('--balance', is_flag=True)
def click_command(income, costs, name, history, balance):
    if income:
        FinanceManagerController(name).update_balance(int(income))
    elif costs:
        FinanceManagerController(name).update_balance(-int(costs))
    elif history:
        out_history(name)
    elif balance:
        out_balance(name)

if __name__ == '__main__':
    click_command()
