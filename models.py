from constans import RATES_API, OUTPUT_DIR, FILE_TMP
import json
import os


class OsModel:

    @staticmethod
    def load(name):
        if not os.path.isfile(FILE_TMP.format(name)):
            return 0, []

        with open(FILE_TMP.format(name), 'r') as f_in:
            information = json.load(f_in)

        return information['current_balance'], information['history']

    @staticmethod
    def save(name, current_balance, history):
        information = {"current_balance": current_balance, "history": history}
        with open(FILE_TMP.format(name), 'w') as f_out:
            json.dump(information, f_out)
