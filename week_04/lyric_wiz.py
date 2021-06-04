
import os
import pickle



curr_dir = os.path.dirname(os.path.realpath(__file__))

mnb = pickle.load(open(curr_dir + '/' + 'mnb_model.sav', 'rb'))
rf = pickle.load(open(curr_dir + '/' + 'rf_model.sav', 'rb'))
tf = pickle.load(open(curr_dir + '/' + 'tfidf_vectorizer.sav', 'rb'))

artist_num = 6

line_from_user = input('\n\n*************LYRICS-WIZ**************** \n \nThis cool program can tell you, which\nartist your earworm might be from. \n\nPlease enter lyrics: \n\n')

input_trans = tf.transform([line_from_user])
y_pred_line = mnb.predict(input_trans)
print(f"\nProbably it's by: {(y_pred_line[0] + ' ')}\n")
print('**************************************')
print(f'Probabilities for all artist \nin database: ')
for a in range(artist_num):
    print(f'Probability for {mnb.classes_[a]}: {100* round(mnb.predict_proba(input_trans)[0,a], 2)}%')
