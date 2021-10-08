import requests
import sys
import os, sys
import pandas as pd

class MonoAPI:

    token = str(os.environ['T_TOKEN'])
    
    basic_url = "https://api.monobank.ua/"
    
    iso_4217 = pd.read_csv("./static/iso-4217.csv")
    
    

# Public API does not require authentefocation
    def get_exchange_rate(self):
        url = self.basic_url + "/bank/currency"
        response = requests.get(url).json()
        if len(response) > 0 :
            response_df = pd.json_normalize(response)
            response_df["date"] = pd.to_datetime(response_df["date"],unit="s") 
            rate_line =  response_df.sort_values(by='date', ascending=False).head(1)
            cur_a = self.iso_4217[self.iso_4217["NumericCode"] == int(rate_line["currencyCodeA"])]["AlphabeticCode"].item()
            cur_b = self.iso_4217[self.iso_4217["NumericCode"] == int(rate_line["currencyCodeB"])]["AlphabeticCode"].item()
            date = str(rate_line["date"].item())
            sel_rate = str(rate_line["rateSell"].item())
            buy_rate = str(rate_line["rateBuy"].item())
            return "Rate for " + cur_a + " to " + cur_b + " for " +  date + " is: sell " + sel_rate + " buy " + buy_rate
        else:
            return "Please try again later"

# Private API require MONO Token
    def get_balance(self):
        url = self.basic_url + "/personal/client-info"
        headers = {'X-Token': self.token}
        response = requests.get(url, headers=headers).json()

        return "Hello"
