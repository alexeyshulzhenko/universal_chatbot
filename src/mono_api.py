import requests
import os

class MonoAPI:

    token = str(os.environ['T_TOKEN'])
    basic_url = "https://api.monobank.ua/"

# Public API does not require authentefocation
    def get_exchange_rate(self):
        url = self.basic_url + "/bank/currency"
        response = requests.get(url).text
        return response

# Private API require MONO Token
    def get_balance(self):
        return "test"