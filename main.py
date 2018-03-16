# finance-manager

import click

from controllers import FinanceManagerController
from views import AsciiTableView

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
        AsciiTableView(name).history()
    elif balance:
        AsciiTableView(name).balance()

if __name__ == '__main__':
    click_command()
