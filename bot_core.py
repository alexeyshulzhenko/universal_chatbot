
import re
import langid



class Message:
    def check_language(self,text):
        languages = ["en", "ru", "uk"]
        url_re = r"\b(?:https?://|www\.)[a-z0-9-]+(\.[a-z0-9-]+)+(?:[/?].*)?"
        new_text = re.sub(url_re, "", text)
        return str(langid.classify(new_text))
        

