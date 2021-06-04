
import os
import pickle



curr_dir = os.path.dirname(os.path.realpath(__file__))

mnb = pickle.load(open(curr_dir + '/' + 'mnb_model.sav', 'rb'))
rf = pickle.load(open(curr_dir + '/' + 'rf_model.sav', 'rb'))
tf = pickle.load(open(curr_dir + '/' + 'tfidf_vectorizer.sav', 'rb'))



line_from_user = input('\n\n*************LYRICS-WIZ***************** \n \nThis cool program can tell you, \nwhich artist your earworm might be from. \nPlease enter lyrics: ')

input_trans = tf.transform([line_from_user])
y_pred_line = mnb.predict(input_trans)
print(f"With an accurcy of 73% it's by: \n*********************************{5* (y_pred_line[0] + ' ')}")

