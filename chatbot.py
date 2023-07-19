import random
import json
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = tf.keras.models.load_model('chatbotmodel.h5') 

# Cleaning up the sentence func
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# Indicate if there is word or not with full of list 1 and 0s
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
            # otherwise its automatically zero
    return np.array(bag)

# Predict func
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# For chatting with Chatbot
def get_repsonse(intents_list, intent_json):
    tag = intents_list[0]['intent']
    list_of_intents = intent_json['intents']

    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('Chatbot is ready to talk:\n')

while True:
    message = input("")
    ints = predict_class(message)
    res = get_repsonse(ints, intents)
    print(res)