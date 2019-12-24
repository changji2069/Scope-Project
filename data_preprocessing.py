import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import nltk
import string
import pylab as pyplt
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os

# reading the csv datasets
for csv_file in os.listdir('processed_dataset/train')[:1]:
    df = pd.read_csv('processed_dataset/train/' + csv_file, encoding = 'ISO-8859-1')
    category = df.groupby('type')
    print(category.size())

    # remove news article with less than 5 words
    for i in range(len(df['news'])):
        if len(df['news'][i].split()) < 5:
            df = df.drop([i])

    #remove words with length < 3:
    def remove_short_word(text): 
        return ' '.join(word for word in text.split() if len(word)>3)
    for i in range(len(df['news'])):
        df['news'][i] = remove_short_word(df['news'][i])

    # remove punctuations
    def remove_punctuation(text):
        string_no_punctuation = text.translate(str.maketrans('', '', string.punctuation))
        return string_no_punctuation
    for i in range(len(df['news'])):
        df['news'][i] = remove_punctuation(df['news'][i])

    # remove stop-words
    def remove_stopword(text):
        return ' '.join(word for word in text.split() if word not in stopwords.words('english'))
    for i in range(len(df['news'])):
        df['news'][i] = remove_stopword(df['news'][i])

    # stemming (Porter's)
    stemmer = PorterStemmer()
    def word_stemmer(text):
        return ' '.join(stemmer.stem(word) for word in text.split())
    for i in range(len(df['news'])):
        df['news'][i] = word_stemmer(df['news'][i])
