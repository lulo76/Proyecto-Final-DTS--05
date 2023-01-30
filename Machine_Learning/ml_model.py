import unicodedata
import string
import numpy as np
import sklearn
from gensim.models import Word2Vec
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
import pickle

with open("./Models/vectorizer.pickle", "rb") as f:
    model_vectorizer = pickle.load(f)

with open("./Models/Word2Vect.pickle", "rb") as f:
    model_word2vect = pickle.load(f)

with open("./Models/MLPClassifier.pickle", "rb") as f:
    model_mlp = pickle.load(f)

model_cnn = keras.models.load_model('./Models/model_cnn.h5')
model_lstm = keras.models.load_model('./Models/model_lstm.h5')

def sentence_cleansing(sentence):
    
    sentence = sentence.strip()
    sentence = sentence.lstrip()
    sentence = sentence.rstrip()
    sentence = sentence.lower() #convertir frase a minusculas
    
    sentence = ''.join((c for c in unicodedata.normalize('NFD',sentence) if unicodedata.category(c) != 'Mn'))
    
    for i in range(100):
        sentence = sentence.replace('  ',' ')
    
    replacements = ''
    for i in list(range(0,32))+list(range(33,97))+list(range(123,1000)):
        sentence = sentence.replace(chr(i),'')
                
    # Quitar palabras que tinen una letra repetida mas de 3 veces y juntas 
    abc = string.ascii_lowercase
    for word in sentence.split():
        remove_word = False
        for char in abc:
            if word.find(3*char) != -1:
                remove_word = True
                break
                
        if (word.find('a') == -1 and 
            word.find('e') == -1 and 
            word.find('i') == -1 and 
            word.find('o') == -1 and 
            word.find('u') == -1):
            remove_word = True
                
        if(remove_word):
            index = sentence.find(word)
            sentence = sentence[0:index] + sentence[index+len(word)+1:len(sentence)]
    
    sentence = sentence.strip()
    sentence = sentence.lstrip()
    sentence = sentence.rstrip()
    
    return sentence

def tokenize_sentences(sentences):
    tokenized_sentences = []
    for sentence in sentences:
        tokenized_sentences.append(sentence.split())
    return tokenized_sentences

def vectorice_sentences(sentences):
    vectoriced_sentences = []
    for sentence in sentences:
        vectoriced_sentence = []
        for word in sentence:
            if word in model_word2vect.wv.key_to_index:
                vectoriced_sentence.append(model_word2vect.wv.key_to_index[word])
            else:
                vectoriced_sentence.append(0)
        vectoriced_sentences.append(vectoriced_sentence)
    return vectoriced_sentences

def predict(sentence):
    
    sentence_cleaned = sentence_cleansing(sentence)
    sentence_vectorized = model_vectorizer.transform([sentence_cleaned]).toarray()

    print(sentence_vectorized)
    print(model_mlp.best_estimator_)

    pred_mlp = model_mlp.predict_proba(sentence_vectorized)

    sentence_tokenized = tokenize_sentences([sentence])
    sentence_vectorized = vectorice_sentences(sentence_tokenized)
    sentence_vectorized = pad_sequences(sentence_vectorized, maxlen=50)
    pred_cnn = model_cnn.predict(sentence_vectorized)
    pred_lstm = model_lstm.predict(sentence_vectorized)

    return {'mlp':pred_mlp[0,1], 'cnn': pred_cnn[0,0], 'lstm': pred_lstm[0,0]}