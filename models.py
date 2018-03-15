import json
import os

import requests
from bs4 import BeautifulSoup


class OsModel:

    RATES_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    OUTPUT_DIR = 'output'
    FILE_TMP = os.path.join(OUTPUT_DIR, '{}.txt')

    @staticmethod
    def _check_directory():
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    @staticmethod
    def load(name):
        OsModel._check_directory()
        if not os.path.isfile(FILE_TMP.format(name)):
            return 0, []

        with open(FILE_TMP.format(name), 'r') as f_in:
            information = json.load(f_in)

        return information['current_balance'], information['history']

    @staticmethod
    def save(name, current_balance, history):
        OsModel._check_directory()
        information = {"current_balance": current_balance, "history": history}
        with open(FILE_TMP.format(name), 'w') as f_out:
            json.dump(information, f_out)


class CurrencyRatesModel:

    @staticmethod
    def get_rates():
        response = requests.get(RATES_API)
        soup = BeautifulSoup(response.content, 'html.parser')
        rates = json.loads(str(soup))
        return rates
