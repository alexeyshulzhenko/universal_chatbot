import nltk, json, random, pickle
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('src/bots/chatbot_model_en.h5')
intents = json.loads(open('src/bots/intents_en.json').read())
words = pickle.load(open('src/bots/words_en.pkl','rb'))
classes = pickle.load(open('src/bots/classes_en.pkl','rb'))

class botEn:
    # preprocessamento input utente
    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    # creazione bag of words
    def bow(self, sentence, words, show_details=True):
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
        p = self.bow(sentence, words,show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list

    def getResponse(self, ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result

    def init(self, msg):
        ints = self.calculate_pred(msg, model)
        res = self.getResponse(ints, intents)
        return res

    # utente = ''
    # print('Benvenuto! Per uscire, scrivi "Esci"')

    # while utente != 'esci':
    #     utente = str(input(""))
    #     res = inizia(utente)
    #     print('AI:' + res)