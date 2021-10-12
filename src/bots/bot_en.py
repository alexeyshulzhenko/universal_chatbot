import nltk, json, random, pickle
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('static/chatbot_model_en.h5')
intents = json.loads(open('static/intents_en.json').read())
words = pickle.load(open('static/words_en.pkl','rb'))
classes = pickle.load(open('static/classes_en.pkl','rb'))

class botEn:

    context = {}
    # preprocessamento input utente
    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    # creazione bag of words
    def bag_of_words(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0]*len(words)
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))

    def calculate_pred(self, sentence, model):
        p = self.bag_of_words(sentence, words,show_details=False)
        res = model.predict(np.array([p]))[0]

        ERROR_THRESHOLD = 0.25

        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list

    def getResponse(self, ints, intents_json, userID='123'):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                # set context for this intent if necessary
                if 'context_set' in i:
                    self.context[userID] = i['context_set']

                # check if this intent is contextual and applies to this user's conversation
                if not 'context_filter' in i or \
                    (userID in self.context and 'context_filter' in i and i['context_filter'] == self.context[userID]):
                    # a random response from the intent
                    result = random.choice(i['responses'])

                # result = random.choice(i['responses'])
                break
        return result


    def init(self, msg):
        ints = self.calculate_pred(msg, model)
        res = self.getResponse(ints, intents)
        return res

# users = ''
# print('Welcome! To exit, type "Exit"')

# bot = botEn()
# while users != 'Exit':
#     users = str(input(""))
#     res = bot.init(users)
#     print('AI:' + res)