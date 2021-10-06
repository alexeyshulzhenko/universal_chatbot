
import re
import langid

from langdetect import DetectorFactory, detect, detect_langs
# class Message:
#     def check_language(self,text):
#         languages = ["en", "ru", "uk"]
#         url_re = r"\b(?:https?://|www\.)[a-z0-9-]+(\.[a-z0-9-]+)+(?:[/?].*)?"
#         new_text = re.sub(url_re, "", text)
#         langs = detect_langs(new_text)  
#         for language in langs:
#             if language.lang in languages:
#                 return  language
#             else:
#                 return "Undefined"


class Message:
    def check_language(self,text):
        languages = ["en", "ru", "uk"]
        url_re = r"\b(?:https?://|www\.)[a-z0-9-]+(\.[a-z0-9-]+)+(?:[/?].*)?"
        new_text = re.sub(url_re, "", text)
        return langid.classify(new_text)
        

