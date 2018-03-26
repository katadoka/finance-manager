import json
import os

import requests
from bs4 import BeautifulSoup

import sqlite3
from peewee import *

class OsModel:

    OUTPUT_DIR = 'output'
    FILE_TMP = os.path.join(OUTPUT_DIR, '{}.txt')

    @staticmethod
    def _check_directory():
        if not os.path.isdir(OsModel.OUTPUT_DIR):
            os.makedirs(OsModel.OUTPUT_DIR)

    @staticmethod
    def load(name):
        OsModel._check_directory()
        if not os.path.isfile(OsModel.FILE_TMP.format(name)):
            return 0, []

        with open(OsModel.FILE_TMP.format(name), 'r') as f_in:
            information = json.load(f_in)

        return information['current_balance'], information['history']

    @staticmethod
    def save(name, current_balance, history):
        OsModel._check_directory()
        information = {"current_balance": current_balance, "history": history}
        with open(OsModel.FILE_TMP.format(name), 'w') as f_out:
            json.dump(information, f_out)


class CurrencyRatesModel:

    RATES_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    @staticmethod
    def get_rates():
        response = requests.get(CurrencyRatesModel.RATES_API)
        soup = BeautifulSoup(response.content, 'html.parser')
        rates = json.loads(str(soup))
        return rates
