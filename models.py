import json
import os

import requests
from bs4 import BeautifulSoup

import sqlite3
from datetime import datetime
from peewee import fn

from modelsorm import User, Amount


class CurrencyRatesModel:

    RATES_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    @staticmethod
    def get_rates():
        response = requests.get(CurrencyRatesModel.RATES_API)
        soup = BeautifulSoup(response.content, 'html.parser')
        rates = json.loads(str(soup))
        return rates


class DBModel:

    @staticmethod
    def load(name):
        User.get_or_create(username=name)
        query = (Amount
                .select(Amount.user, Amount.amount, Amount.date_time)
                .where(Amount.user == name)
                .order_by(Amount.date_time))
        information_history = []
        current_balance = 0
        for row in query:
            information_history.append([row.amount, row.date_time])
            current_balance += row.amount
        return current_balance, information_history


    @staticmethod
    def save(information):
        Amount.get_or_create(user=information.name, 
            amount=information.amount, date_time=datetime.now().isoformat())


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
    def save(information):
        OsModel._check_directory()
        information_dict = {"current_balance": information.current_balance, "history": information.history}
        with open(OsModel.FILE_TMP.format(information.name), 'w') as f_out:
            json.dump(information_dict, f_out)
