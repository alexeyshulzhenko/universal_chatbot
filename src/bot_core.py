
import re
import os
import langid

from src.mono_api import MonoAPI


class Message:
    
    mono_api = MonoAPI()

    def check_language(self,text):
        url_re = r"\b(?:https?://|www\.)[a-z0-9-]+(\.[a-z0-9-]+)+(?:[/?].*)?"
        new_text = re.sub(url_re, "", text)
        return str(langid.classify(new_text))
        

    def pick_command_en(self, text):
        if (text == "exchange rate"):
            return self.mono_api.get_exchange_rate()
        elif (text == "balance"):
            return self.mono_api.get_balance()
        else: return "Err"


    def process_message(self, text, user, admin_user_id):
        if user == admin_user_id:
            language = self.check_language(text).split(',')[0].replace("'", "").replace("(", "")
            if language == "en":
                answer = self.pick_command_en(text)
            return answer
        else: 
            return "You are not authorised"

