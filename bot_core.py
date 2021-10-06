import gcld3
import re

# class Message:
#     def check_language(self,text):
#         url_re = r"\b(?:https?://|www\.)[a-z0-9-]+(\.[a-z0-9-]+)+(?:[/?].*)?"
#         new_text = re.sub(url_re, "", text)
#         lang = cld3.get_language(new_text).language
#         return str(lang)

class Message:
    def check_language(self,text):
        languages = ["en", "ru", "uk"]
        detector = gcld3.NNetLanguageIdentifier(min_num_bytes=10, max_num_bytes=1000)
        result = detector.FindTopNMostFreqLangs(text=text, num_langs=5)
        for i in result:
            if i.language in languages:
                return str(i.language)
            else: return "undefined"