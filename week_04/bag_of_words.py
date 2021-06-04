
import os
import re
import numpy as np
import pandas as pd

import pickle

from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

curr_dir = os.path.dirname(os.path.realpath(__file__))


def read_n_concat(df1, df2):
    df_a = pd.read_csv(f'data/{df1}.csv')
    df_b = pd.read_csv(f'data/{df2}.csv')
    new_df = pd.concat([df_a, df_b], axis=0, ignore_index=True)
    new_df.drop('Unnamed: 0', axis=1, inplace = True)
    return new_df

def add_new_artist(lyrics_df, new_artist):
    df_new_artist = pd.read_csv(curr_dir + f'/data/{new_artist}.csv')
    new_df = pd.concat([lyrics_df, df_new_artist], axis=0, ignore_index=True)
    new_df.drop('Unnamed: 0', axis=1, inplace = True)
    return new_df


lyrics_df = read_n_concat('Eminem', 'Drake')
lyrics_df = add_new_artist(lyrics_df, 'Beyoncé')
lyrics_df['lyrics'] = (lyrics_df['title']+ ' ')*3 + ' ' + lyrics_df['lyrics']
lyrics_df = add_new_artist(lyrics_df, 'Queen')
lyrics_df = add_new_artist(lyrics_df, 'Imagine-Dragons')
lyrics_df = add_new_artist(lyrics_df, 'Taylor-Swift')

lyrics_df.drop_duplicates(subset ='title', keep = False, inplace = True)

X = lyrics_df.drop('artist', axis=1) #all features minus Class
y = lyrics_df['artist'] #just the Class columns

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, stratify=y)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

tf = TfidfVectorizer(lowercase=True, stop_words = 'english', token_pattern = '(?u)\\b[a-zA-Z]+\\b', ngram_range = (1,3))
vectorizer = tf.fit_transform(X_train['lyrics'])
X_test_vec = tf.transform(X_test['lyrics'])

mnb = MultinomialNB()
mnb.fit(vectorizer, y_train) 
mnb_y_pred = mnb.predict(X_test_vec)

rf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=10)
rf.fit(vectorizer, y_train)
rf_y_pred = rf.predict(X_test_vec)

print(f'The accuracy of the Naive Bayes model is: {round(accuracy_score(y_test, rf_y_pred), 3)}')
print(f'The accuracy of the Random Forest model is: {round(accuracy_score(y_test, rf_y_pred), 3)}')

pickle.dump(mnb, open(curr_dir + '/' + 'mnb_model.sav', 'wb'))
pickle.dump(rf, open(curr_dir + '/' + 'rf_model.sav', 'wb'))
pickle.dump(tf, open(curr_dir + '/' + 'tfidf_vectorizer.sav', 'wb'))